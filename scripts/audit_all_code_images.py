#!/usr/bin/env python3
"""
Find all image references across HTML, CSS, and JS files.
"""
import os
import re

ROOT = r'd:\cannaculture'

files_to_check = [
    'index.html',
    'css/styles.css',
    'js/app.js',
    'js/ai-sommelier.js',
    'js/data.js',
    'js/matcher.js',
    'js/bitacora.js',
    'js/tools.js',
    'js/missions.js',
]

found_images = {}

for rel_p in files_to_check:
    abs_p = os.path.join(ROOT, rel_p)
    if not os.path.exists(abs_p): continue
    with open(abs_p, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # Extract image paths
    matches = re.findall(r'["\'\(]([^"\'\)]*?\.(?:jpg|jpeg|png|webp|avif|svg)(?:\?[^"\'\)]*)?)["\'\)]', text, re.I)
    for m in matches:
        # filter out external urls or http
        clean_m = m.split('?')[0].strip()
        if not clean_m.startswith('http'):
            found_images.setdefault(clean_m, []).append(rel_p)

print(f"Total unique local image assets referenced across all code: {len(found_images)}")
print("\n--- Non-strain UI Assets & Icons ---")
for img_path, sources in sorted(found_images.items()):
    if not any(b in img_path for b in ['sensi', 'rqs', 'sweet', 'ripper', 'bf', 'dp', 'dna', 'ghs', 'oo', 'philo', 'rkiem', 'cannabiogen', 'pyramid', 'heavyweight', 'aceseeds', 'bsf', 'hso', 'nirvana', 'paradise', 'thseeds', 'wls', 'barneys', 'dinafem', 'tfd', 'raw', 'exotic']):
        exists = os.path.exists(os.path.join(ROOT, img_path.lstrip('/')))
        sz = os.path.getsize(os.path.join(ROOT, img_path.lstrip('/')))//1024 if exists else 0
        print(f"  {img_path} (exists={exists}, size={sz}KB) -> used in: {sources}")
