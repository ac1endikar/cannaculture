#!/usr/bin/env python3
"""
Compare current data.js with initial backup to list exactly which strains were modified.
"""
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

CURRENT = r'd:\cannaculture\js\data.js'
ORIGINAL = r'd:\cannaculture\js\data.js.backup_phase1'

def parse_strains_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    entries = {}
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
            entries[current['id']] = dict(current)
            current = {}
    return entries

cur_strains = parse_strains_file(CURRENT)
orig_strains = parse_strains_file(ORIGINAL) if os.path.exists(ORIGINAL) else {}

diffs = []
for sid, c in cur_strains.items():
    orig_img = orig_strains.get(sid, {}).get('image', 'N/A')
    cur_img = c['image']
    
    # Check current file size
    fname = cur_img.replace('img/', '')
    cur_sz = os.path.getsize(os.path.join('d:/cannaculture/img', fname)) // 1024 if os.path.exists(os.path.join('d:/cannaculture/img', fname)) else 0
    
    if orig_img != cur_img or 'duplicate' in orig_img or 'missing' in orig_img:
        diffs.append({
            'id': sid,
            'name': c['name'],
            'bank': c['bank'],
            'old_image': orig_img,
            'new_image': cur_img,
            'new_size_kb': cur_sz
        })

print(f"Total modified strains: {len(diffs)} / {len(cur_strains)}")
by_bank = {}
for d in diffs:
    by_bank.setdefault(d['bank'], []).append(d)

for bank, strains in sorted(by_bank.items()):
    print(f"\n[{bank}] ({len(strains)} genéticas modificadas con fotos reales):")
    for s in strains:
        print(f"  * {s['name']}: {s['old_image']} -> {s['new_image']} ({s['new_size_kb']} KB)")
