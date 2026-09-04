# -*- coding: utf-8 -*-
"""Helpers voor het toevoegen van kaarten aan de nature-data JSON-chunks.

Sinds de data-migratie (tools/split-data.py) is de kaartdata verplaatst uit
natuurgids-nederland.html naar nature-data/reserves-*.json. Dit module:

  * card()            — bouwt net als vroeger de volledige kaart-HTML (voor de
                        renderer + als tussenstap), maar retourneert ook de
                        losse nl_html/en_html blokken;
  * insert(cards, after_id) — schrijft de kaart-records in de juiste JSON-chunk
                        (achter de kaart met id after_id), werkt index.json bij
                        en hangt de TOC-<li>'s aan de statische inhoudsopgave in
                        de HTML (de enige HTML-aanpassing per kaart);
  * progress()        — meldt de voortgang (de HTML-progressiebalk wordt op
                        runtime gevuld vanuit index.json);
  * check()           — valideert de JSON-chunks;
  * blog()            — voegt een blogpost toe aan de HTML (ongewijzigd).

Draai batchscripts vanuit de repo-root:  python3 tools/b36r.py
"""
import re, io, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = 'natuurgids-nederland.html'
INDEX = 'nature-data/index.json'

sys.path.insert(0, os.path.join(ROOT, 'tools'))
try:
    import importlib.util
    _spec = importlib.util.spec_from_file_location(
        'split_data', os.path.join(ROOT, 'tools', 'split-data.py'))
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    half_summary = _mod.half_summary
except Exception:
    half_summary = None


def _summary(html, lang):
    """Lees de tekst-samenvatting uit een c-nl/c-en blok; nooit een harde fout."""
    if not half_summary:
        return {}
    try:
        out = half_summary(html.strip(), lang)
        return out if isinstance(out, dict) else {}
    except Exception:
        return {}


def _read(p):
    return io.open(os.path.join(ROOT, p), encoding='utf-8').read()


def _write(p, s):
    io.open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)


def _ul(items):
    return '\n'.join('      <li>%s</li>' % i for i in items)


def _chips(items):
    return ''.join('<span class="chip">%s</span>' % c for c in items)


def _half(num, name, d, lang, n2k):
    T = {
        'nl': ('Waarom bezoeken &amp; hoogtepunten', 'Periodieke verschijnselen &amp; evenementen',
               'Fauna &amp; bijzondere flora', 'Aanbevolen startpunten &amp; parkeren'),
        'en': ('Why visit &amp; highlights', 'Periodic phenomena &amp; events',
               'Wildlife &amp; special flora', 'Recommended trailheads &amp; parking'),
    }[lang]
    tags = d['tags']
    t = '<span class="tag prov">%s</span>' % tags[0]
    t += ''.join('<span class="tag">%s</span>' % x for x in tags[1:-1])
    if n2k:
        t += '\n      <span class="tag n2k">\U0001f1ea\U0001f1fa Natura 2000</span>'
    t += '\n      <span class="tag">%s</span>' % tags[-1]
    n2kbox = ''
    if n2k:
        n2kbox = '\n    <div class="n2kbox">\U0001f1ea\U0001f1fa <b>Natura 2000</b> %s</div>' % n2k
    return '''  <div class="c-%s">
    <div class="tags">%s</div>
    <h2><span class="num">%s</span>%s</h2>
    <p class="loc">%s</p>
    <p class="desc">%s</p>
    <div class="meta">%s</div>%s
    <h3>\U0001f50d %s</h3>
    <ul>
%s
    </ul>
    <h3>\u26a1 %s</h3>
    <ul>
%s
    </ul>
    <h3>\U0001f43e %s</h3>
    <p class="chips">%s</p>
    <h3>\U0001f4cd %s</h3>
    <ul>
%s
    </ul>
    <div class="foot">%s</div>
  </div>''' % (lang, t, num, name, d['loc'], d['desc'], d['meta'], n2kbox,
               T[0], _ul(d['why']), T[1], _ul(d['phen']),
               T[2], _chips(d['wild']), T[3], _ul(d['trail']), d['foot'])


def card(num, name, nl, en, card_class='card', n2k=None, n2k_en=None):
    """nl/en: dicts met keys tags, loc, desc, meta, why, phen, wild, trail, foot"""
    keys = ('tags', 'loc', 'desc', 'meta', 'why', 'phen', 'wild', 'trail', 'foot')
    for d, lbl in ((nl, 'nl'), (en, 'en')):
        miss = [k for k in keys if k not in d]
        if miss:
            raise ValueError('kaart %s (%s): ontbrekende %s-velden: %s' % (num, name, lbl, miss))
    nl_html = _half(num, name, nl, 'nl', n2k)
    en_html = _half(num, name, en, 'en', n2k_en or n2k)
    html = '<article class="%s" id="nr%s">\n%s\n%s\n</article>\n' % (
        card_class, num, nl_html, en_html)
    number = next((t for t in nl.get('tags', []) if re.match(r'^list \d+ \u00b7 no\. \d+$', t.strip())), '')
    out = {
        'num': int(num), 'name': name,
        'nl': nl, 'en': en, 'html': html,
        'nl_html': nl_html, 'en_html': en_html, 'number': number,
        'card_class': card_class if card_class != 'card' else None,
    }
    if n2k:
        out['n2k'] = n2k
    return out


# --------------------------------------------------------------------------
# JSON-chunk administratie
# --------------------------------------------------------------------------

def _chunk_ranges():
    meta = json.loads(_read(INDEX))
    ranges = []
    for fn in meta['files']:
        m = re.match(r'^reserves-(\d+)-(\d+)\.json$', fn)
        if m:
            ranges.append((fn, int(m.group(1)), int(m.group(2))))
    ranges.sort(key=lambda r: r[1])
    return ranges, meta


def _index_path():
    return os.path.join(ROOT, INDEX)


def _load_chunk(fn):
    return json.load(io.open(os.path.join(ROOT, 'nature-data', fn), encoding='utf-8'))


def _save_chunk(fn, recs):
    json.dump(recs, io.open(os.path.join(ROOT, 'nature-data', fn), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


def _save_index(meta):
    s = json.dumps(meta, ensure_ascii=False, indent=4)
    _write(INDEX, s)


def _record_of(c):
    """Bouw een chunk-record (nl_html/en_html + tekstvelden) uit een card()."""
    rec = {'id': c['num'], 'name': c['name'], 'number': c['number'],
           'nl': None, 'en': None,
           'nl_html': c['nl_html'], 'en_html': c['en_html']}
    rec['nl'] = _summary(c['nl_html'], 'nl')
    rec['en'] = _summary(c['en_html'], 'en')
    if c.get('card_class'):
        rec['card_class'] = c['card_class']
    return rec


def insert(cards, after_id=None, chunk=None):
    """Voeg kaart-records toe aan de JSON-chunk en werk TOC + index bij.

    after_id: id van de bestaande kaart waarna de nieuwe kaarten komen
              (in dezelfde chunk). None = achteraan de chunk van het laatste id.
    chunk:    optioneel bestandsnaam (reserves-A-B.json) om naar te schrijven.
    """
    ranges, meta = _chunk_ranges()
    if not chunk:
        # kies de chunk op basis van after_id, of anders de hoogste chunk
        if after_id is not None:
            for fn, a, b in ranges:
                if a <= int(after_id) <= b:
                    chunk = fn
                    break
        if not chunk:
            chunk = ranges[-1][0]
    fn, a, b = next((r for r in ranges if r[0] == chunk), (None, None, None))
    if fn is None:
        raise ValueError('onbekende chunk %s' % chunk)

    recs = _load_chunk(fn)
    existing = {r['id'] for r in recs}
    for c in cards:
        if c['num'] in existing:
            raise ValueError('kaart %d bestaat al in %s' % (c['num'], fn))
        if not (a <= c['num'] <= b):
            raise ValueError('kaart %d past niet in range %d-%d van %s'
                             % (c['num'], a, b, fn))

    new_recs = [_record_of(c) for c in cards]
    if after_id is None:
        recs = recs + new_recs
    else:
        idx = next((i for i, r in enumerate(recs) if r['id'] == int(after_id)), None)
        if idx is None:
            raise ValueError('after_id %s niet gevonden in %s' % (after_id, fn))
        recs = recs[:idx + 1] + new_recs + recs[idx + 1:]
    recs.sort(key=lambda r: r['id'])
    _save_chunk(fn, recs)

    # index.json bijwerken (counts, ranges, totaal)
    for c in meta['chunks']:
        if c['file'] == fn:
            c['count'] = len(recs)
            c['id_range'] = '%d-%d' % (recs[0]['id'], recs[-1]['id'])
            if fn.endswith('-1831.json'):
                c['note'] = 'in progress \u2014 currently %d-%d' % (recs[0]['id'], recs[-1]['id'])
    meta['total_reserves'] = sum(
        c['count'] for c in meta['chunks'])
    _save_index(meta)

    # statische TOC in de HTML aanvullen (vóór de sluitende </ol>)
    h = _read(HTML)
    m = re.search(r'<ol class="toclist"[^>]*>', h)
    if not m:
        raise ValueError('toclist niet gevonden in HTML')
    ol_end = h.index('</ol>', m.end())
    toc = ''.join('<li><a href="#nr%02d">%s</a></li>\n'
                  % (c['num'], c['name'].replace('&', '&amp;')) for c in cards)
    h = h[:ol_end] + toc + h[ol_end:]
    _write(HTML, h)

    print('chunk %s: %d records (toegevoegd %d, totaal %d)'
          % (fn, len(recs), len(cards), meta['total_reserves']))
    return len(cards)


def progress(done, total=2373):
    """Progressiemelding; de balk/teller in de HTML wordt op runtime gevuld
    uit nature-data/index.json (total_reserves / book_total)."""
    pct = round(done * 100.0 / total, 1)
    print('progress: %d of %d reserves (%.1f%%)' % (done, total, pct))
    return pct


def blog(html):
    h = _read(HTML)
    a = h.index('<div id="tab-blog">')
    i = h.index('<div class="post">', a)
    _write(HTML, h[:i] + html.rstrip() + '\n' + h[i:])


def check():
    ranges, meta = _chunk_ranges()
    total = 0
    dup = []
    ids = []
    for fn, a, b in ranges:
        recs = _load_chunk(fn)
        total += len(recs)
        ids.extend(r['id'] for r in recs)
        for r in recs:
            if not (r.get('nl_html') and r.get('en_html')):
                print('  ! %s: record %d mist nl_html/en_html' % (fn, r.get('id')))
    seen = set()
    for n in ids:
        if n in seen:
            dup.append(n)
        seen.add(n)
    missing = sorted(set(range(1, total + 1)) - set(ids))
    print('kaarten %d in %d chunks; %s; missend %s%s' % (
        total, len(ranges), 'geen duplicaten' if not dup else 'DUPLICATEN %s' % dup,
        missing[:8] if missing else 'geen',
        ' ; totaal index=%d' % meta['total_reserves']))
    return total
