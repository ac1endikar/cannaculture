#!/usr/bin/env python3
import urllib.request
from PIL import Image
import io

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

gsc_urls = [
    "https://eurogrow.es/28292-large_default/girl-scout-cookies-nirvana.jpg",
    "https://eurogrow.es/28292-home_default/girl-scout-cookies-nirvana.jpg",
    "https://bucket.growdiaries.com/static/seed_item_photos/3860/girl-scout-cookies_700.webp",
    "https://www.zamnesia.com/5135-26305/nirvana-girl-scout-cookies-feminized.jpg",
    "https://www.zamnesia.com/5135-35058-large2x/nirvana-girl-scout-cookies-feminized.jpg",
    "https://www.growbarato.net/26359-home_default/girl-scout-cookies-nirvana.jpg",
    "https://www.alchimiaweb.com/ils/10160217/thumb-0/6/girl-scout-cookies.webp"
]

for u in gsc_urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            print(f"OK ({len(data)//1024}KB, {im.size[0]}x{im.size[1]}px): {u}")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
