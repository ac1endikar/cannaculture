#!/usr/bin/env python3
import os
import re

with open('js/data.js', encoding='utf-8') as f:
    lines = f.readlines()

entries = []
current = {}
for line in lines:
    ls = line.strip()
    m = re.match(r'id:\s*"([^"]+)"', ls)
    if m: current['id'] = m.group(1)
    m = re.match(r'name:\s*"([^"]+)"', ls)
    if m: current['name'] = m.group(1)
    m = re.match(r'bank:\s*"([^"]+)"', ls)
    if m: current['bank'] = m.group(1)
    m = re.match(r'image:\s*"([^"]+)"', ls)
    if m: current['image'] = m.group(1)
    if ls in ('},', '}') and 'image' in current and 'name' in current:
        entries.append(dict(current))
        current = {}

low_strains = []
for e in entries:
    img = e['image']
    fname = img[4:] if img.startswith('img/') else os.path.basename(img.split('?')[0])
    p = os.path.join('img', fname)
    if os.path.exists(p):
        kb = os.path.getsize(p) // 1024
        if kb < 65:
            low_strains.append((e['id'], e['name'], e['bank'], fname, kb))

print(f"Total remaining < 65KB: {len(low_strains)}")
for sid, name, bank, fname, kb in low_strains:
    print(f"  '{sid}': ('{name}', '{bank}', '{fname}', {kb}KB),")
