#!/usr/bin/env python3
import urllib.request
from PIL import Image
import io

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

sp_urls = [
    "https://pevgrow.com/34140-large_default/sunset-paradise-paradise-seeds.jpg",
    "https://eurogrow.es/28298-large_default/sunset-paradise.jpg",
    "https://www.gbthegreenbrand.com/28859-large_default/sunset-paradise-paradise-seeds.jpg",
    "https://us.paradise-seeds.com/wp-content/uploads/2024/03/Paradise-Seeds-Cannabis-1.webp"
]

for u in sp_urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            print(f"OK ({len(data)//1024}KB | {im.size[0]}x{im.size[1]}px): {u}")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
