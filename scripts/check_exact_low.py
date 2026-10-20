#!/usr/bin/env python3
import os
import re

with open('js/data.js', encoding='utf-8') as f:
    content = f.read()

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
    if ls in ('},', '}') and 'image' in current and 'name' in current:
        entries.append(dict(current))
        current = {}

for e in entries:
    img = e['image']
    fname = img[4:] if img.startswith('img/') else os.path.basename(img.split('?')[0])
    p = os.path.join('img', fname)
    if not os.path.exists(p):
        print(f"MISSING: {e['id']} -> {e['name']} ({e['bank']}) => {e['image']}")
    else:
        kb = os.path.getsize(p) // 1024
        if kb < 65:
            print(f"LOW ({kb}KB): {e['id']} -> {e['name']} ({e['bank']}) => {e['image']}")

print(f"Total entries analyzed: {len(entries)}")
