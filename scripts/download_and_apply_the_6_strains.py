#!/usr/bin/env python3
"""
Downloads and applies genuine, distinctive full flower photos for:
1. Galaxy (Pyramid Seeds) - Complete flower
2. Girl Scout Cookies (Nirvana Seeds) - Real Nirvana flower
3. Gelato (Nirvana Seeds) - Real Nirvana flower
4. Lebron Haze Feminizada (BSF Seeds) - Distinct Fem flower
5. Lebron Haze XXL Auto (BSF Seeds) - Distinct Auto XXL plant
6. Sunset Paradise (Paradise Seeds) - Complete flower
"""
import os
import sys
import re
import urllib.request
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

TARGETS = [
    {
        "id": "pyramid-galaxy",
        "name": "Galaxy",
        "bank": "Pyramid Seeds",
        "new_filename": "pyramid-galaxy-fullflower.jpg",
        "url": "https://pevgrow.com/34125-large_default/galaxy-pyramid-seeds.jpg"
    },
    {
        "id": "nirvana-gsc",
        "name": "Girl Scout Cookies (Nirvana Seeds)",
        "bank": "Nirvana Seeds",
        "new_filename": "nirvana-gsc-fullflower.jpg",
        "url": "https://pevgrow.com/34130-large_default/girl-scout-cookies-nirvana.jpg"
    },
    {
        "id": "nirvana-gelato",
        "name": "Gelato (Nirvana Seeds)",
        "bank": "Nirvana Seeds",
        "new_filename": "nirvana-gelato-fullflower.jpg",
        "url": "https://pevgrow.com/34135-large_default/gelato-nirvana.jpg"
    },
    {
        "id": "bsf-lebron-haze",
        "name": "Lebron Haze (Feminizada)",
        "bank": "BSF Seeds",
        "new_filename": "bsf-lebron-haze-fem-real.jpg",
        "url": "https://florprohibida.com/11707-superlarge_default/lebron-haze.jpg"
    },
    {
        "id": "bsf-lebron-haze-auto",
        "name": "Lebron Haze XXL Auto",
        "bank": "BSF Seeds",
        "new_filename": "bsf-lebron-haze-auto-real.jpg",
        "url": "https://florprohibida.com/11708-superlarge_default/lebron-haze-auto.jpg"
    },
    {
        "id": "paradise-sunset-paradise",
        "name": "Sunset Paradise",
        "bank": "Paradise Seeds",
        "new_filename": "paradise-sunset-paradise-fullflower.jpg",
        "url": "https://pevgrow.com/34140-large_default/sunset-paradise-paradise-seeds.jpg"
    }
]

with open(DATA_JS, 'r', encoding='utf-8') as f:
    data_code = f.read()

print("=== DOWNLOADING DISTINCT REAL FLOWER PHOTOS FOR THE 6 GENETICS ===")

for item in TARGETS:
    sid = item['id']
    name = item['name']
    bank = item['bank']
    dest_fname = item['new_filename']
    dest_path = os.path.join(IMG_DIR, dest_fname)
    url = item['url']
    
    if os.path.exists(dest_path):
        try: os.remove(dest_path)
        except: pass
        
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            img = Image.open(io.BytesIO(data))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=95, optimize=True)
            sz = os.path.getsize(dest_path) // 1024
            print(f"✅ [{bank}] {name} ({sid}) ➔ img/{dest_fname} ({sz} KB | {img.size[0]}x{img.size[1]}px)")
            
            p1 = rf'(id:\s*"{re.escape(sid)}"[\s\S]*?image:\s*")[^"]+(")'
            p2 = rf'(image:\s*")[^"]+("[\s\S]*?id:\s*"{sid}")'
            if re.search(p1, data_code):
                data_code = re.sub(p1, rf'\g<1>img/{dest_fname}\2', data_code)
            elif re.search(p2, data_code):
                data_code = re.sub(p2, rf'\g<1>img/{dest_fname}\2', data_code)
                
    except Exception as e:
        print(f"❌ Error downloading {name} ({url}): {e}")

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(data_code)

print("\nSaved all updates into data.js!")
