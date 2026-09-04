# -*- coding: utf-8 -*-
"""Helpers voor het toevoegen van kaarten aan natuurgids-nederland.html.

Draai batchscripts vanuit de repo-root:  python3 tools/b29.py
"""
import re, io

HTML = 'natuurgids-nederland.html'

def _read():
    return io.open(HTML, encoding='utf-8').read()

def _write(s):
    io.open(HTML, 'w', encoding='utf-8').write(s)

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
    html = '<article class="%s" id="nr%s">\n%s\n%s\n</article>\n' % (
        card_class, num, _half(num, name, nl, 'nl', n2k),
        _half(num, name, en, 'en', n2k_en or n2k))
    return {'num': num, 'name': name, 'html': html}

def insert(cards, after_id, tocsec=None):
    h = _read()
    m = re.search(r'<article class="[^"]*" id="nr%s">.*?</article>\n' % after_id, h, re.S)
    if not m:
        raise ValueError('after_id nr%s niet gevonden' % after_id)
    h = h[:m.end()] + ''.join(c['html'] for c in cards) + h[m.end():]
    toc = ''.join('<li><a href="#nr%s">%s</a></li>\n' % (c['num'], c['name']) for c in cards)
    if tocsec:
        toc = '<div class="tocsec">%s</div>\n' % tocsec + toc
    # anker op de LAATSTE tocsec-kop, zodat nieuwe lists automatisch meegaan
    anchor = h.rindex('<div class="tocsec">List ')
    end = h.index('</ol>', anchor)
    _write(h[:end] + toc + h[end:])
    return len(cards)

def progress(done, total=2373):
    h = _read()
    pct = round(done * 100.0 / total, 1)
    h = re.sub(r'(<div class="progressbar"><i style="width:)[\d.]+(%")', r'\g<1>%s\g<2>' % pct, h, count=1)
    h = re.sub(r'(<b>Progress: )\d+( of \d+ reserves</b>)', r'\g<1>%s\g<2>' % done, h, count=1)
    _write(h)
    return pct

def blog(html):
    h = _read()
    a = h.index('<div id="tab-blog">')
    i = h.index('<div class="post">', a)
    _write(h[:i] + html.rstrip() + '\n' + h[i:])

def check():
    h = _read()
    nums = re.findall(r'<article class="[^"]*" id="nr(\d+)"', h)
    dup = sorted(set(n for n in nums if nums.count(n) > 1))
    print('kaarten %d c-nl %d c-en %d laatste %s%s' % (
        len(nums), h.count('class="c-nl"'), h.count('class="c-en"'), nums[-3:],
        (' DUPLICATEN %s' % dup) if dup else ''))
