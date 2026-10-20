#!/usr/bin/env python3
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DATA_JS = r'd:\cannaculture\js\data.js'

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

# Exact mapping for the 23 requested strains to their downloaded official photos
OFFICIAL_MAPPINGS = {
    "bf-pineapple-express": "img/bf-pineapple-express-official.jpg",
    "sweet-cream-caramel": "img/sweet-cream-caramel-official.jpg",
    "rqs-fat-banana": "img/rqs-fat-banana-official.jpg",
    "rqs-amnesia-haze": "img/rqs-amnesia-haze-official.jpg",
    "sensi-northern-lights": "img/sensi-northern-lights-official.jpg",
    "blimburn-girl-scout-cookies": "img/blimburn-girl-scout-cookies-official.jpg",
    "bsf-lebron-haze-auto": "img/bsf-lebron-haze-auto-official.jpg",
    "sensi-black-domina": "img/sensi-black-domina-official.jpg",
    "pyramid-anesthesia": "img/pyramid-anesthesia-official.jpg",
    "serious-biddy-early": "img/serious-biddy-early-official.jpg",
    "bsf-green-tiger-fast": "img/bsf-green-tiger-official.jpg",
    "serious-chronic": "img/serious-chronic-official.jpg",
    "serious-warlock": "img/serious-warlock-official.jpg",
    "serious-kali-bubba": "img/serious-kali-bubba-official.jpg",
    "ripper-sideral": "img/ripper-sideral-official.jpg",
    "cpg-la-bomba": "img/cpg-la-bomba-official.jpg",
    "eth-candy-store": "img/eth-candy-store-official.jpg",
    "paradise-sunset-paradise": "img/paradise-sunset-paradise-official.jpg",
    "positronics-blue-rhino": "img/positronics-blue-rhino-official.jpg",
    "paradise-opium": "img/paradise-opium-official.jpg",
    "aceseeds-zamaldelica": "img/aceseeds-zamaldelica-official.jpg",
    "aceseeds-congo": "img/aceseeds-congo-official.jpg",
    "ths-bubblegum": "img/ths-bubblegum-official.jpg",
}

for sid, img_path in OFFICIAL_MAPPINGS.items():
    # Match strain block with id: "sid" and replace its image field
    # Handles both 'id: "sid",\n image: "..."' and 'image: "...",\n id: "sid"'
    p1 = rf'(id:\s*"{sid}"[\s\S]*?image:\s*")[^"]+(")'
    p2 = rf'(image:\s*")[^"]+("[\s\S]*?id:\s*"{sid}")'
    
    if re.search(p1, content):
        content = re.sub(p1, rf'\g<1>{img_path}\2', content)
        print(f"Updated (p1): {sid} -> {img_path}")
    elif re.search(p2, content):
        content = re.sub(p2, rf'\g<1>{img_path}\2', content)
        print(f"Updated (p2): {sid} -> {img_path}")
    else:
        print(f"WARNING: ID not found in data.js: {sid}")

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSuccessfully updated all 23 strain mappings in data.js!")
