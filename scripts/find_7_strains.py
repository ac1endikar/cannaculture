#!/usr/bin/env python3
"""
Find exact matching entries for the 7 requested strains.
"""
import re

DATA_JS = r'd:\cannaculture\js\data.js'
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

strains = [
    ('Cream Caramel', ['sweet-cream-caramel', 'cream-caramel']),
    ('Northern Light', ['northern-light', 'northern-lights']),
    ('Galaxy', ['pyramid-galaxy', 'galaxy']),
    ('Girl Scout Cookies (Nirvana)', ['nirvana-gsc', 'gsc']),
    ('Lebron Haze (BSF)', ['bsf-lebron-haze', 'bsf-lebron-haze-auto']),
    ('Nefertiti', ['pyramid-nefertiti', 'nefertiti']),
    ('Sunset Paradise', ['paradise-sunset-paradise', 'sunset-paradise']),
]

entries = []
current = {}
for line in content.split('\n'):
    ls = line.strip()
    m = re.match(r'id:\s*"([^"]+)"', ls)
    if m: current['id'] = m.group(1)
    m = re.match(r'name:\s*"([^"]+)"', ls)
    if m: current['name'] = m.group(1)
    m = re.match(r'bank:\s*"([^"]+)"', ls)
    if m: current['bank'] = m.group(1)
    m = re.match(r'image:\s*"([^"]+)"', ls)
    if m: current['image'] = m.group(1)
    if ls in ('},', '}') and 'image' in current and 'name' in current and 'id' in current:
        entries.append(dict(current))
        current = {}

for label, keys in strains:
    print(f"\n=== {label} ===")
    for e in entries:
        if any(k in e['id'].lower() or k in e['name'].lower() for k in keys):
            print(f"  ID: {e['id']} | Bank: {e['bank']} | Name: {e['name']} | Img: {e['image']}")
