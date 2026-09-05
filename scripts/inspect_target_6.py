#!/usr/bin/env python3
"""
Inspect the 6 target entries in data.js.
"""
import re

DATA_JS = r'd:\cannaculture\js\data.js'
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

target_ids = [
    "pyramid-galaxy",
    "nirvana-gsc",
    "nirvana-gelato",
    "bsf-lebron-haze",
    "bsf-lebron-haze-auto",
    "paradise-sunset-paradise"
]

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

for tid in target_ids:
    if tid in entries:
        print(f"ID: {tid} | Name: {entries[tid]['name']} | Bank: {entries[tid]['bank']} | Img: {entries[tid]['image']}")
    else:
        print(f"ID: {tid} NOT FOUND")
