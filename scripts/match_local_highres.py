#!/usr/bin/env python3
"""
Find existing high-res pictures in img/ that can be mapped to strains in data.js
"""
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

all_img_files = os.listdir('img')

print(f"Total files in img/: {len(all_img_files)}")

# Check for each strain if there's a better matching file in img/
suggestions = []
for e in entries:
    cur_img = e['image']
    cur_fname = cur_img[4:] if cur_img.startswith('img/') else os.path.basename(cur_img.split('?')[0])
    cur_size = os.path.getsize(os.path.join('img', cur_fname)) // 1024 if os.path.exists(os.path.join('img', cur_fname)) else 0
    
    # Generate keywords for this strain
    s_slug = re.sub(r'[^a-zA-Z0-9]', '', e['name'].lower())
    
    # Find matching files in img/
    matches = []
    for f in all_img_files:
        if not f.endswith('.jpg'): continue
        f_clean = re.sub(r'[^a-zA-Z0-9]', '', f.lower())
        if s_slug in f_clean or f_clean in s_slug:
            f_size = os.path.getsize(os.path.join('img', f)) // 1024
            if f_size > cur_size and f_size >= 65:
                matches.append((f, f_size))
                
    if matches:
        matches.sort(key=lambda x: x[1], reverse=True)
        suggestions.append((e['id'], e['name'], e['bank'], cur_fname, cur_size, matches[0][0], matches[0][1]))

print(f"\nFound {len(suggestions)} strains that have a higher resolution image already in img/:")
for sid, name, bank, cur_f, cur_sz, better_f, better_sz in suggestions[:30]:
    print(f"  [{bank}] {name}: current {cur_f} ({cur_sz}KB) -> BETTER: {better_f} ({better_sz}KB)")
