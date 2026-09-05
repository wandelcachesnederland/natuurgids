# -*- coding: utf-8 -*-
"""OUD: haalde kaarten uit de HTML en schreef ze als JSON-chunk.

Sinds de data-migratie (tools/split-data.py) is de kaartdata verplaatst naar
nature-data/reserves-*.json; nieuwe kaarten worden daar door tools/mk.py
direct in geschreven. Deze tool bestaat alleen nog voor het geval iemand een
oude full-HTML-versie (met <article>-kaarten) naar JSON wil omzetten.
"""
import re, io, json, sys
from html import unescape

lo, hi = int(sys.argv[1]), int(sys.argv[2])
h = io.open('natuurgids-nederland.html', encoding='utf-8').read()
if '<article class=' not in h:
    print('geen <article>-kaarten in de HTML — data zit in nature-data/*.json '
          '(zie tools/split-data.py en tools/mk.py)')
    sys.exit(0)

def strip(s):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', '', s))).strip()

def half(block, lang):
    m = re.search(r'<div class="c-%s">(.*?)\n  </div>' % lang, block, re.S)
    if not m:
        return None
    b = m.group(1)
    tm = re.search(r'<div class="tags">(.*?)</div>', b, re.S)
    tags = re.findall(r'<span class="tag[^"]*">(.*?)</span>', tm.group(1), re.S) if tm else []
    n2k = re.search(r'<div class="n2kbox">(.*?)</div>', b, re.S)
    def one(pat):
        mm = re.search(pat, b, re.S)
        return strip(mm.group(1)) if mm else ''
    def lst(head):
        mm = re.search(r'<h3>%s[^<]*</h3>\s*<ul>(.*?)</ul>' % head, b, re.S)
        return [strip(x) for x in re.findall(r'<li>(.*?)</li>', mm.group(1), re.S)] if mm else []
    return {
        'tags': [strip(t) for t in tags],
        'location': one(r'<p class="loc">(.*?)</p>'),
        'description': one(r'<p class="desc">(.*?)</p>'),
        'meta': one(r'<div class="meta">(.*?)</div>'),
        'natura2000': strip(n2k.group(1)) if n2k else '',
        'why_visit': lst('\U0001f50d'),
        'periodic_phenomena': lst('\u26a1'),
        'wildlife': [strip(c) for c in re.findall(r'<span class="chip">(.*?)</span>', b, re.S)],
        'trailheads': lst('\U0001f4cd'),
        'footer': one(r'<div class="foot">(.*?)</div>'),
    }

out = []
for m in re.finditer(r'<article class="([^"]*)" id="nr(\d+)">(.*?)</article>', h, re.S):
    n = int(m.group(2))
    if not (lo <= n <= hi):
        continue
    body = m.group(3)
    nm = re.search(r'<h2>.*?</span>\s*(.*?)</h2>', body, re.S)
    nl, en = half(body, 'nl'), half(body, 'en')
    rec = {'id': n, 'name': strip(nm.group(1)) if nm else '',
           'number': nl['tags'][-1] if nl and nl['tags'] else '', 'nl': nl, 'en': en}
    if m.group(1) != 'card':
        rec['card_class'] = m.group(1)
    out.append(rec)

path = 'nature-data/reserves-%d-%d.json' % (lo, hi)
json.dump(out, io.open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%s: %d records (%d-%d)' % (path, len(out), out[0]['id'], out[-1]['id']))
