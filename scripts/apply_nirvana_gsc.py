#!/usr/bin/env python3
import os
import sys
import re
import urllib.request
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

url = "https://eurogrow.es/28292-large_default/girl-scout-cookies-nirvana.jpg"
dest_fname = "nirvana-gsc-real.jpg"
dest_path = os.path.join(IMG_DIR, dest_fname)

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
with urllib.request.urlopen(req) as resp:
    data = resp.read()
    img = Image.open(io.BytesIO(data))
    if img.mode != 'RGB': img = img.convert('RGB')
    img.save(dest_path, 'JPEG', quality=95, optimize=True)
    print(f"Downloaded {dest_fname} ({os.path.getsize(dest_path)//1024} KB | {img.size[0]}x{img.size[1]}px)")

with open(DATA_JS, 'r', encoding='utf-8') as f:
    code = f.read()

# Update nirvana-gsc
p1 = r'(id:\s*"nirvana-gsc"[\s\S]*?image:\s*")[^"]+(")'
p2 = r'(image:\s*")[^"]+("[\s\S]*?id:\s*"nirvana-gsc")'
if re.search(p1, code):
    code = re.sub(p1, rf'\g<1>img/{dest_fname}\2', code)
elif re.search(p2, code):
    code = re.sub(p2, rf'\g<1>img/{dest_fname}\2', code)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated nirvana-gsc in data.js!")
