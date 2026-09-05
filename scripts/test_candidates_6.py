#!/usr/bin/env python3
"""
Find full-flower / plant macro photos for:
1. Galaxy (Pyramid Seeds) - Full flower
2. Girl Scout Cookies (Nirvana Seeds)
3. Gelato (Nirvana Seeds)
4. Lebron Haze Feminizada (BSF Seeds)
5. Lebron Haze XXL Auto (BSF Seeds)
6. Sunset Paradise (Paradise Seeds)
"""
import urllib.request
from PIL import Image
import io

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

candidates = {
    "pyramid-galaxy": [
        "https://eurogrow.es/19717-large_default/galaxy.jpg",
        "https://www.alchimiaweb.com/ils/13003015/thumb-0/6/galaxy.webp",
        "https://bucket.growdiaries.com/static/seed_item_photos/2458/galaxy_700.webp",
        "https://pevgrow.com/34125-large_default/galaxy-pyramid-seeds.jpg",
        "https://www.growbarato.net/19717-large_default/galaxy.jpg"
    ],
    "nirvana-gsc": [
        "https://www.growbarato.net/26359-large_default/girl-scout-cookies-nirvana.jpg",
        "https://eurogrow.es/28292-large_default/girl-scout-cookies-nirvana.jpg",
        "https://pevgrow.com/34130-large_default/girl-scout-cookies-nirvana.jpg"
    ],
    "nirvana-gelato": [
        "https://eurogrow.es/28295-large_default/gelato-nirvana.jpg",
        "https://www.growbarato.net/26362-large_default/gelato-nirvana.jpg",
        "https://pevgrow.com/34135-large_default/gelato-nirvana.jpg"
    ],
    "bsf-lebron-haze-fem": [
        "https://eurogrow.es/20149-large_default/lebron-haze.jpg",
        "https://www.gbthegreenbrand.com/29104-large_default/lebron-haze.jpg",
        "https://florprohibida.com/11707-superlarge_default/lebron-haze.jpg"
    ],
    "bsf-lebron-haze-auto": [
        "https://eurogrow.es/20150-large_default/lebron-haze-xxl-auto.jpg",
        "https://www.gbthegreenbrand.com/29105-large_default/lebron-haze-xxl-auto.jpg",
        "https://florprohibida.com/11708-superlarge_default/lebron-haze-auto.jpg"
    ],
    "paradise-sunset-paradise": [
        "https://www.paradise-seeds.com/wp-content/uploads/2021/04/Sunset-Paradise.jpg",
        "https://us.paradise-seeds.com/wp-content/uploads/2024/03/Paradise-Seeds-Cannabis-1.webp",
        "https://www.alchimiaweb.com/ils/14002015/thumb-0/6/sunset-paradise.webp"
    ]
}

print("=== TESTING CANDIDATES FOR THE 6 GENETICS ===")
for key, urls in candidates.items():
    print(f"\n[{key}]:")
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = resp.read()
                im = Image.open(io.BytesIO(data))
                print(f"  OK ({len(data)//1024}KB | {im.size[0]}x{im.size[1]}px): {u}")
        except Exception as e:
            print(f"  FAIL: {u} -> {e}")
