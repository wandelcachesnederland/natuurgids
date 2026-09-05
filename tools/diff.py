# -*- coding: utf-8 -*-
"""Vergelijk bronlijst met de kaarten in nature-data/reserves-*.json.
Draai vanuit repo-root: python3 tools/diff.py"""
import re, io, json, unicodedata, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace('&amp;', '&').replace('\u2019', "'")
    s = re.sub(r"^(de|het|'t|'s|een)\s+", '', s.strip())
    return re.sub(r'[^a-z0-9]', '', s)

# laad alle records uit de chunks
meta = json.load(io.open(os.path.join(ROOT, 'nature-data', 'index.json'), encoding='utf-8'))
cards = {}
for fn in meta['files']:
    data = json.load(io.open(os.path.join(ROOT, 'nature-data', fn), encoding='utf-8'))
    for rec in sorted(data, key=lambda r: r.get('id', 0)):
        name = rec.get('name') or ''
        if name:
            cards.setdefault(norm(name), rec['id'])

missing, seen = [], set()
for line in io.open(os.path.join(ROOT, 'nature-data', 'bronlijst-boek.txt'), encoding='utf-8'):
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
