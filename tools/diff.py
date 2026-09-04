# -*- coding: utf-8 -*-
"""Vergelijk bronlijst met de HTML. Draai vanuit repo-root: python3 tools/diff.py"""
import re, io, json, unicodedata

h = io.open('natuurgids-nederland.html', encoding='utf-8').read()

def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace('&amp;', '&').replace('\u2019', "'")
    s = re.sub(r"^(de|het|'t|'s|een)\s+", '', s.strip())
    return re.sub(r'[^a-z0-9]', '', s)

cards = {}
for m in re.finditer(r'<article class="([^"]*)" id="nr(\d+)">(.*?)</article>', h, re.S):
    nm = re.search(r'<h2>.*?</span>\s*(.*?)</h2>', m.group(3), re.S)
    if nm:
        cards[norm(nm.group(1))] = int(m.group(2))

missing, seen = [], set()
for line in io.open('nature-data/bronlijst-boek.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    p = line.split('|')
    if len(p) < 4:
        continue
    key = norm(p[2])
    if key in cards or key in seen:
        continue
    seen.add(key)
    missing.append({'groep': int(p[0]), 'nr': int(p[1]), 'naam': p[2], 'pagina': p[3]})

json.dump(missing, io.open('/tmp/missing.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('kaarten %d ontbrekend %d' % (len(cards), len(missing)))
for i, x in enumerate(missing[:20]):
    print(i, x['groep'], x['naam'], x['pagina'])
