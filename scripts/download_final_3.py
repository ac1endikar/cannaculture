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

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

final_three = [
    {
        "id": "bsf-lebron-haze-auto",
        "name": "Lebron Haze XXL Auto",
        "bank": "BSF Seeds",
        "new_filename": "bsf-lebron-haze-auto-official.jpg",
        "urls": [
            "https://www.zamnesia.com/6224-43078/bsf-seeds-lebron-haze-feminize.jpg",
            "https://eurogrow.es/20149-home_default/lebron-haze.jpg"
        ]
    },
    {
        "id": "bsf-green-tiger-fast",
        "name": "Green Tiger (Faster)",
        "bank": "BSF Seeds",
        "new_filename": "bsf-green-tiger-official.jpg",
        "urls": [
            "https://eurogrow.es/20156-large_default/green-tiger-fast-version.jpg",
            "https://florprohibida.com/11707-superlarge_default/lebron-haze.jpg"
        ]
    },
    {
        "id": "aceseeds-congo",
        "name": "Congo",
        "bank": "ACE Seeds",
        "new_filename": "aceseeds-congo-official.jpg",
        "urls": [
            "https://www.aceseeds.org/wp-content/uploads/2015/12/congo_4.jpg",
            "https://www.zamnesia.com/3050-7050-large/ace-seeds-congo-feminized.jpg"
        ]
    }
]

with open(DATA_JS, 'r', encoding='utf-8') as f:
    data_code = f.read()

for item in final_three:
    sid = item['id']
    name = item['name']
    bank = item['bank']
    dest_fname = item['new_filename']
    dest_path = os.path.join(IMG_DIR, dest_fname)
    
    if os.path.exists(dest_path):
        try: os.remove(dest_path)
        except: pass
        
    for url in item['urls']:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                raw_data = resp.read()
                if len(raw_data) < 10 * 1024: continue
                img = Image.open(io.BytesIO(raw_data))
                if img.mode != 'RGB': img = img.convert('RGB')
                img.save(dest_path, 'JPEG', quality=95, optimize=True)
                sz = os.path.getsize(dest_path) // 1024
                print(f"✅ [{bank}] {name} ➔ img/{dest_fname} ({sz} KB) from: {url[:60]}")
                
                # Update in data.js
                pattern = rf'(id:\s*"{re.escape(sid)}",[\s\S]*?image:\s*")[^"]+(")'
                if re.search(pattern, data_code):
                    data_code = re.sub(pattern, rf'\g<1>img/{dest_fname}\2', data_code)
                break
        except Exception as e:
            print(f"Failed {url}: {e}")

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(data_code)

print("Saved all updates to data.js!")
