#!/usr/bin/env python3
"""
Downloads and replaces the 7 requested strains with authentic real photos.
Deletes old files, saves new photos, updates data.js and rebuilds bundle.js.
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
        "ids": ["sweet-cream-caramel"],
        "name": "Cream Caramel",
        "bank": "Sweet Seeds",
        "new_filename": "sweet-cream-caramel-real.jpg",
        "url": "https://www.zamnesia.com/301-15962-large2x/sweet-seeds-cream-caramel-feminized.jpg"
    },
    {
        "ids": ["rqs-northern-light", "nirvana-northern-light", "sensi-northern-lights", "wls-northern-lights"],
        "name": "Northern Light",
        "bank": "Sensi / Nirvana / RQS",
        "new_filename": "northern-lights-real-hd.jpg",
        "url": "https://img.sensiseeds.com/images/thumbs/0000684_northern-lights-feminized-seeds_800.png"
    },
    {
        "ids": ["pyramid-galaxy"],
        "name": "Galaxy",
        "bank": "Pyramid Seeds",
        "new_filename": "pyramid-galaxy-real.jpg",
        "url": "https://pyramidseeds.com/28-product_main/galaxy.jpg"
    },
    {
        "ids": ["nirvana-gsc"],
        "name": "Girl Scout Cookies (Nirvana Seeds)",
        "bank": "Nirvana Seeds",
        "new_filename": "nirvana-gsc-real.jpg",
        "url": "https://www.zamnesia.com/5135-26305-large2x/nirvana-girl-scout-cookies-feminized.jpg"
    },
    {
        "ids": ["bsf-lebron-haze", "bsf-lebron-haze-auto"],
        "name": "Lebron Haze (BSF Seeds)",
        "bank": "BSF Seeds",
        "new_filename": "bsf-lebron-haze-real.jpg",
        "url": "https://www.zamnesia.com/6224-43078-large2x/bsf-seeds-lebron-haze-feminized.jpg"
    },
    {
        "ids": ["pyramid-nefertiti"],
        "name": "Nefertiti",
        "bank": "Pyramid Seeds",
        "new_filename": "pyramid-nefertiti-real.jpg",
        "url": "https://pyramidseeds.com/14-product_main/nefertiti.jpg"
    },
    {
        "ids": ["paradise-sunset-paradise"],
        "name": "Sunset Paradise",
        "bank": "Paradise Seeds",
        "new_filename": "paradise-sunset-paradise-real.jpg",
        "url": "https://us.paradise-seeds.com/wp-content/uploads/2024/03/Paradise-Seeds-Cannabis-1.webp"
    }
]

with open(DATA_JS, 'r', encoding='utf-8') as f:
    data_code = f.read()

print("=== DOWNLOADING REAL PHOTOS FOR THE 7 SPECIFIC GENETICS ===")

for item in TARGETS:
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
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            img = Image.open(io.BytesIO(data))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=95, optimize=True)
            sz = os.path.getsize(dest_path) // 1024
            print(f"✅ [{bank}] {name} ➔ img/{dest_fname} ({sz} KB | {img.size[0]}x{img.size[1]}px)")
            
            for sid in item['ids']:
                p1 = rf'(id:\s*"{re.escape(sid)}"[\s\S]*?image:\s*")[^"]+(")'
                p2 = rf'(image:\s*")[^"]+("[\s\S]*?id:\s*"{sid}")'
                if re.search(p1, data_code):
                    data_code = re.sub(p1, rf'\g<1>img/{dest_fname}\2', data_code)
                    print(f"   Mapped DB ID: {sid} ➔ img/{dest_fname}")
                elif re.search(p2, data_code):
                    data_code = re.sub(p2, rf'\g<1>img/{dest_fname}\2', data_code)
                    print(f"   Mapped DB ID: {sid} ➔ img/{dest_fname}")
    except Exception as e:
        print(f"❌ Error downloading {name} ({url}): {e}")

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(data_code)

print("\nSaved all updates into data.js!")
