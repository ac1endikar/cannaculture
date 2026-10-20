#!/usr/bin/env python3
import os
import re
import json

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

ok = []
missing = []
low = []
for e in entries:
    img = e['image']
    fname = img[4:] if img.startswith('img/') else os.path.basename(img.split('?')[0])
    p = os.path.join('img', fname)
    if not os.path.exists(p):
        missing.append((e, fname, 0, 'MISSING'))
    else:
        kb = os.path.getsize(p) // 1024
        if kb < 30:
            missing.append((e, fname, kb, 'UNDER_30KB'))
        elif kb < 65:
            low.append((e, fname, kb, 'LOW_QUALITY'))
        else:
            ok.append((e, fname, kb, 'OK'))

print(f"Total Strains: {len(entries)}")
print(f"OK (>65KB): {len(ok)}")
print(f"Low Quality (30-65KB): {len(low)}")
print(f"Critical / Missing (<30KB): {len(missing)}")

print("\n=== CRITICAL / MISSING ===")
for e, fname, kb, status in missing:
    print(f"[{status}] [{e['bank']}] {e['name']} -> {fname} ({kb}KB)")

print("\n=== LOW QUALITY (30-65KB) SAMPLE ===")
for e, fname, kb, status in low[:15]:
    print(f"[{kb}KB] [{e['bank']}] {e['name']} -> {fname}")
