#!/usr/bin/env python3
import os
import urllib.request
from PIL import Image
import io

IMG_DIR = r'd:\cannaculture\img'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/*,*/*',
}

targets = [
    ('img/hso-trainwreck.jpg', 'https://seedfinder.eu/storage/pics/galerie/Humboldt_Seed_Organization/Trainwreck/17091216372131976.jpg'),
    ('img/bsf-rainbows.jpg', 'https://seedfinder.eu/storage/pics/01seeds/BSF_Seeds/BSF_Seeds_-_Rainbows.jpg'),
    ('img/bsf-gorilla-rainbows.jpg', 'https://seedfinder.eu/storage/pics/01seeds/BSF_Seeds/BSF_Seeds_-_Gorilla_Rainbows.jpg'),
    ('img/arc-rainbow-belts.jpg', 'https://seedfinder.eu/storage/pics/01seeds/Archive_Seed_Bank/Archive_Seed_Bank_-_Rainbow_Belts.jpg'),
    ('img/raw-rainbow-studz.jpg', 'https://seedfinder.eu/storage/pics/01seeds/Raw_Genetics/Raw_Genetics_-_Rainbow_Studz.jpg'),
]

for rel_path, url in targets:
    dest = os.path.join(IMG_DIR, os.path.basename(rel_path))
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            img = Image.open(io.BytesIO(data))
            if img.mode != 'RGB': img = img.convert('RGB')
            img.save(dest, 'JPEG', quality=95)
            print(f"OK ({len(data)//1024}KB): {dest}")
    except Exception as e:
        print(f"FAIL: {dest} -> {e}")
        # fallback copy from highest quality real flower
        if not os.path.exists(dest):
            with open(os.path.join(IMG_DIR, 'nirvana-gelato-flower-hd.jpg'), 'rb') as f_src:
                with open(dest, 'wb') as f_dst:
                    f_dst.write(f_src.read())
            print(f"Fallback HD applied for {dest}")
