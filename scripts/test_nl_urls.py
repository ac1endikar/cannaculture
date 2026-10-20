#!/usr/bin/env python3
import urllib.request
from PIL import Image
import io

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

nl_urls = [
    "https://img.sensiseeds.com/images/thumbs/0000684_northern-lights-feminized-seeds_800.png",
    "https://www.zamnesia.com/284-15904-large2x/royal-queen-seeds-northern-light-feminized.jpg",
    "https://eurogrow.es/19510-large_default/northern-light.jpg",
    "https://eurogrow.es/19510-home_default/northern-light.jpg",
    "https://eurogrow.es/28296-large_default/northern-lights-auto.jpg",
    "https://www.growbarato.net/1446-large_default/northern-lights-nirvana.jpg",
    "https://www.growbarato.net/1355-large_default/northern-light-royal-queen-seeds.jpg",
    "https://www.alchimiaweb.com/ils/13003015/thumb-0/6/northern-lights.webp",
]

for u in nl_urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            print(f"OK ({len(data)//1024}KB, {im.size[0]}x{im.size[1]}px): {u}")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
