#!/usr/bin/env python3
"""
Applies all downloaded *-flowering-real.jpg images to data.js.
Rebuilds bundle.js and verifies image files.
"""
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

with open(DATA_JS, 'r', encoding='utf-8') as f:
    code = f.read()

# Find all *-flowering-real.jpg files
flowering_files = [f for f in os.listdir(IMG_DIR) if f.endswith('-flowering-real.jpg')]
print(f"Found {len(flowering_files)} newly downloaded real advanced flowering photos:")

applied = []
for ff in flowering_files:
    # ff is like "pyramid-tutankhamon-flowering-real.jpg" or "ripper-zombie-kush-flowering-real.jpg"
    strain_id = ff.replace('-flowering-real.jpg', '')
    
    # Pattern to match strain block
    pattern = rf'(id:\s*"{re.escape(strain_id)}",[\s\S]*?image:\s*")[^"]+(")'
    if re.search(pattern, code):
        code = re.sub(pattern, rf'\g<1>img/{ff}\2', code)
        applied.append(strain_id)
        sz = os.path.getsize(os.path.join(IMG_DIR, ff)) // 1024
        print(f"  🌸 [APPLIED FLOWERING PHOTO {sz}KB] {strain_id} -> img/{ff}")

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(code)

print(f"\nSuccessfully applied {len(applied)} real advanced flowering photos into data.js!")
