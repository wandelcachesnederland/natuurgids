# -*- coding: utf-8 -*-
"""One-time migration: move ALL card data out of natuurgids-nederland.html into
nature-data/reserves-*.json, and slim the HTML down to a shell that renders the
cards at runtime from those JSON chunks.

The JSON chunk records gain two lossless fields per card:
  nl_html / en_html  — the verbatim inner markup of the <div class="c-nl"> and
                       <div class="c-en"> blocks, so the renderer can rebuild
                       the cards pixel-identical (colours, <b>, .months,
                       .chip, tags incl. prov/n2k/peak classes, …).

The existing text-summary fields (nl/en) are regenerated with the exact same
parser as tools/export.py, so the text API keeps working unchanged.

Run from the repo root:  python3 tools/split-data.py
"""
import re, io, json, sys
from html import unescape

HTML = 'natuurgids-nederland.html'
INDEX = 'nature-data/index.json'

def read(p):
    return io.open(p, encoding='utf-8').read()

def write(p, s):
    io.open(p, 'w', encoding='utf-8').write(s)

# --------------------------------------------------------------------------
# Robust div-block extraction (depth counted) for the c-nl / c-en wrappers
# --------------------------------------------------------------------------
_TAG = re.compile(r'<div\b[^>]*>|</div>')

def take_div(s, i):
    """s[i] starts with '<div…>'.  Return (outer_html, index_one_past_closing)."""
    depth = 0
    j = i
    while True:
        m = _TAG.search(s, j)
        if not m:
            raise ValueError('unbalanced div')
        if m.group(0).startswith('</'):
            depth -= 1
            if depth == 0:
                return s[i:m.end()], m.end()
        else:
            depth += 1
        j = m.end()

# --------------------------------------------------------------------------
# Text-summary parser — identical to tools/export.py (kept in sync)
# --------------------------------------------------------------------------
def strip_html(s):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', '', s))).strip()

def half_summary(block, lang):
    """Parse the text fields out of a verbatim c-nl / c-en block.

    Uses the inner content directly (the outer <div class="c-lang"> wrapper is
    already isolated by the depth-counting parser), so it works for both the
    modern cards (block closes on its own line) and the older coloured cards
    (block closes with '</div></div>').
    """
    assert block.startswith('<div class="c-%s">' % lang) and block.endswith('</div>')
    b = block[len('<div class="c-%s">' % lang):-len('</div>')]
    tm = re.search(r'<div class="tags">(.*?)</div>', b, re.S)
    tags = re.findall(r'<span class="tag[^"]*">(.*?)</span>', tm.group(1), re.S) if tm else []
    n2k = re.search(r'<div class="n2kbox[^"]*">(.*?)</div>', b, re.S)

    def one(pat):
        mm = re.search(pat, b, re.S)
        return strip_html(mm.group(1)) if mm else ''

    def lst(head):
        mm = re.search(r'<h3>%s[^<]*</h3>\s*<ul>(.*?)</ul>' % head, b, re.S)
        return [strip_html(x) for x in re.findall(r'<li>(.*?)</li>', mm.group(1), re.S)] if mm else []

    out = {
        'tags': [strip_html(t) for t in tags],
        'location': one(r'<p class="loc">(.*?)</p>'),
        'description': one(r'<p class="desc">(.*?)</p>'),
        'meta': one(r'<div class="meta">(.*?)</div>'),
        'natura2000': strip_html(n2k.group(1)) if n2k else '',
        'why_visit': lst('\U0001f50d'),
        'periodic_phenomena': lst('\u26a1'),
        'wildlife': [strip_html(c) for c in re.findall(r'<span class="chip">(.*?)</span>', b, re.S)],
        'trailheads': lst('\U0001f4cd'),
        'footer': one(r'<div class="foot">(.*?)</div>'),
    }
    note = one(r'<p class="note">(.*?)</p>')
    if note:
        out['note'] = note
    return out

# --------------------------------------------------------------------------
# Parse every article
# --------------------------------------------------------------------------
def parse_articles(h):
    recs = []
    for m in re.finditer(r'<article class="([^"]*)" id="nr(\d+)">(.*?)</article>', h, re.S):
        cls, n, body = m.group(1), int(m.group(2)), m.group(3)
        halves = {}
        for lang in ('nl', 'en'):
            key = '<div class="c-%s">' % lang
            i = body.find(key)
            if i == -1:
                raise ValueError('card %d: missing c-%s' % (n, lang))
            block, _ = take_div(body, i)
            halves[lang] = block
        # full name from the first h2 (NL half); raw text kept as in the HTML
        # (entities like &amp; stay as-is, matching the historic export)
        nm = re.search(r'<h2>\s*<span[^>]*class="num"[^>]*>\s*\d+\s*</span>\s*(.*?)\s*</h2>', halves['nl'], re.S)
        name = re.sub(r'\s+', ' ', nm.group(1)).strip() if nm else ''
        # card class as the full article class attribute ('card', 'card peat', …)
        toks = cls.split()
        card_class = cls if toks and toks[0] == 'card' and len(toks) > 1 else None
        summ = {}
        for lang in ('nl', 'en'):
            summ[lang] = half_summary(halves[lang], lang) or {}
        number = ''
        for t in summ['nl'].get('tags', []):
            if re.match(r'^list \d+ \u00b7 no\. \d+$', t.strip()):
                number = t.strip()
                break
        rec = {'id': n, 'name': name, 'number': number,
               'nl': summ['nl'], 'en': summ['en'],
               'nl_html': halves['nl'], 'en_html': halves['en']}
        if card_class:
            rec['card_class'] = card_class
        recs.append(rec)
    recs.sort(key=lambda r: r['id'])
    return recs

# --------------------------------------------------------------------------
# Chunk routing (file names reserves-A-B.json, from index.json 'files')
# --------------------------------------------------------------------------
def chunk_files(meta):
    out = []
    for fn in meta['files']:
        m = re.match(r'^reserves-(\d+)-(\d+)\.json$', fn)
        if not m:
            raise ValueError('unexpected chunk filename: %s' % fn)
        out.append((fn, int(m.group(1)), int(m.group(2))))
    out.sort(key=lambda x: x[1])
    return out

def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    html_path = HTML
    slim = True
    if '--no-html' in argv:
        slim = False
        argv = [a for a in argv if a != '--no-html']
    if argv:
        html_path = argv[0]

    h = read(html_path)
    recs = parse_articles(h)
    ids = [r['id'] for r in recs]
    if not ids:
        sys.exit('no articles found in %s — nothing to migrate' % html_path)
    assert ids == list(range(1, ids[-1] + 1)), 'ids not contiguous 1..%d' % ids[-1]
    print('parsed %d articles, ids 1..%d, contiguous' % (len(recs), ids[-1]))

    meta = json.loads(read(INDEX))
    chunks = chunk_files(meta)

    by_id = {r['id']: r for r in recs}
    written = {}
    for fn, a, b in chunks:
        sel = [by_id[i] for i in range(a, b + 1) if i in by_id]
        written[fn] = sel
        json.dump(sel, io.open('nature-data/' + fn, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        print('  %-28s %d records' % (fn, len(sel)))

    total = sum(len(v) for v in written.values())
    assert total == len(recs), 'routed %d != %d' % (total, len(recs))

    # ---- index.json: update total + chunk counts -------------------------
    for c in meta['chunks']:
        sel = written.get(c['file'], [])
        c['count'] = len(sel)
        if sel:
            c['id_range'] = '%d-%d' % (sel[0]['id'], sel[-1]['id'])
        if c['file'].endswith('-1831.json') and sel:
            c['note'] = 'in progress \u2014 currently %d-%d' % (sel[0]['id'], sel[-1]['id'])
    meta['total_reserves'] = total
    if 'book_total' not in meta:
        meta['book_total'] = 2373
    # original formatting: indent 4, no trailing newline
    s = json.dumps(meta, ensure_ascii=False, indent=4)
    write(INDEX, s)
    print('index.json: total_reserves=%d, book_total=%d' % (total, meta['book_total']))

    # ---- slim the HTML (only when run against the full HTML file) ----------
    import os
    if slim:
        a = h.index('<article class=')
        last = h.rindex('</article>')
        z = last + len('</article>')
        region = h[a:z]
        # legacy section headers (<h2 class="grouphdr">) that sat between cards:
        # keep them in nature-data/sections.json for the runtime renderer
        arts = [(m.start(), int(m.group(1)))
                for m in re.finditer(r'<article\b[^>]*\bid="nr(\d+)"', region)]
        secs = []
        for m in re.finditer(r'<h2 class="grouphdr[^>]*>.*?</h2>', region, re.S):
            na = next((aid for pos, aid in arts if pos > m.start()), None)
            if na is not None:
                secs.append({'before': na, 'html': m.group(0)})
        if secs:
            json.dump(secs, io.open('nature-data/sections.json', 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)
            print('sections.json: %d headers preserved' % len(secs))
        region = re.sub(r'<h2 class="grouphdr[^>]*>.*?</h2>\s*', '', region, flags=re.S)
        before, after = h[:a], h[z:]
        assert '</div>' in after and 'tab-warn' in after, 'unexpected tail structure'
        shell = before + '<div id="cards"></div>\n' + after
        write(HTML, shell)
        print('html: %d bytes -> %d bytes' % (os.path.getsize(HTML), len(shell.encode('utf-8'))))
    else:
        print('html: not touched (--no-html), %d bytes' % os.path.getsize(HTML))

    # ---- self check -------------------------------------------------------
    import glob
    allrec = []
    for fn in sorted(glob.glob('nature-data/reserves-*.json')):
        data = json.load(io.open(fn, encoding='utf-8'))
        if isinstance(data, list):
            allrec.extend(data)
    print('json totals: %d records across %d chunks' % (len(allrec), len(written)))
    missing = [r for r in allrec if not r.get('nl_html') or not r.get('en_html')]
    print('records lacking nl_html/en_html: %d' % len(missing))
    dups = len(allrec) - len({r['id'] for r in allrec})
    print('duplicate ids in json: %d' % dups)
    if missing or dups or len(allrec) != total:
        sys.exit('SELF CHECK FAILED')

if __name__ == '__main__':
    main()
