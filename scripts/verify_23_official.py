#!/usr/bin/env python3
import os
import sys
import re
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

DATA_JS = r'd:\cannaculture\js\data.js'
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

target_ids = [
    "bf-pineapple-express",
    "sweet-cream-caramel",
    "rqs-fat-banana",
    "rqs-amnesia-haze",
    "sensi-northern-lights",
    "blimburn-girl-scout-cookies",
    "bsf-lebron-haze-auto",
    "sensi-black-domina",
    "pyramid-anesthesia",
    "serious-biddy-early",
    "bsf-green-tiger-fast",
    "serious-chronic",
    "serious-warlock",
    "serious-kali-bubba",
    "ripper-sideral",
    "cpg-la-bomba",
    "eth-candy-store",
    "paradise-sunset-paradise",
    "positronics-blue-rhino",
    "paradise-opium",
    "aceseeds-zamaldelica",
    "aceseeds-congo",
    "ths-bubblegum"
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

print("=== VERIFYING EXACT 23 STRAINS IN DATA.JS ===")
for sid in target_ids:
    if sid in entries:
        e = entries[sid]
        img_p = e['image']
        full_p = os.path.join('d:/cannaculture', img_p)
        exists = os.path.exists(full_p)
        if exists:
            sz = os.path.getsize(full_p) // 1024
            im = Image.open(full_p)
            print(f"✅ [{e['bank']}] {e['name']} ({sid}) -> {img_p} | {sz} KB | {im.size[0]}x{im.size[1]}px")
        else:
            print(f"❌ MISSING FILE: {full_p}")
    else:
        print(f"❌ ID NOT FOUND: {sid}")
