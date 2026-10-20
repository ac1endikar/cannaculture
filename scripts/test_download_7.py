#!/usr/bin/env python3
"""
Test downloading authentic photos from major distributor / breeder catalogs for the 7 strains.
"""
import os
import urllib.request
from PIL import Image
import io

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

test_targets = [
    ("sweet-cream-caramel", "Cream Caramel", [
        "https://www.zamnesia.com/301-15962-large2x/sweet-seeds-cream-caramel-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/1380/cream-caramel_700.webp",
        "https://eurogrow.es/19525-home_default/cream-caramel.jpg",
        "https://sweetseeds.com/9665/cream-caramel.jpg"
    ]),
    ("rqs-northern-light", "Northern Light RQS", [
        "https://www.royalqueenseeds.com/116-2009-thickbox/northern-light.jpg",
        "https://www.zamnesia.com/284-15904-large2x/royal-queen-seeds-northern-light-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/1344/northern-light_700.webp"
    ]),
    ("nirvana-northern-light", "Northern Light Nirvana", [
        "https://www.zamnesia.com/139-15891-large2x/nirvana-northern-light-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/1723/northern-light_700.webp",
        "https://www.growbarato.net/1446-large_default/northern-lights-nirvana.jpg"
    ]),
    ("pyramid-galaxy", "Galaxy Pyramid Seeds", [
        "https://www.zamnesia.com/492-15975-large2x/pyramid-seeds-galaxy-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/2458/galaxy_700.webp",
        "https://pyramidseeds.com/28-product_main/galaxy.jpg",
        "https://eurogrow.es/19717-home_default/galaxy.jpg"
    ]),
    ("nirvana-gsc", "Girl Scout Cookies Nirvana", [
        "https://www.zamnesia.com/5135-26305-large2x/nirvana-girl-scout-cookies-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/3860/girl-scout-cookies_700.webp",
        "https://www.growbarato.net/26359-large_default/girl-scout-cookies-nirvana.jpg"
    ]),
    ("bsf-lebron-haze", "Lebron Haze BSF", [
        "https://www.zamnesia.com/6224-43078-large2x/bsf-seeds-lebron-haze-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/4774/lebron-haze_700.webp",
        "https://eurogrow.es/20149-home_default/lebron-haze.jpg"
    ]),
    ("pyramid-nefertiti", "Nefertiti Pyramid Seeds", [
        "https://www.zamnesia.com/488-15974-large2x/pyramid-seeds-nefertiti-feminized.jpg",
        "https://bucket.growdiaries.com/static/seed_item_photos/2464/nefertiti_700.webp",
        "https://pyramidseeds.com/14-product_main/nefertiti.jpg",
        "https://eurogrow.es/19721-home_default/nefertiti.jpg"
    ]),
    ("paradise-sunset-paradise", "Sunset Paradise Paradise Seeds", [
        "https://www.zamnesia.com/8381-27488-large2x/paradise-seeds-sunset-paradise-feminized.jpg",
        "https://us.paradise-seeds.com/wp-content/uploads/2024/03/Paradise-Seeds-Cannabis-1.webp",
        "https://bucket.growdiaries.com/static/seed_item_photos/5430/sunset-paradise_700.webp"
    ]),
]

for sid, label, urls in test_targets:
    found = False
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = resp.read()
                if len(data) > 15 * 1024:
                    im = Image.open(io.BytesIO(data))
                    print(f"OK ({len(data)//1024}KB, {im.size[0]}x{im.size[1]}px): [{sid}] {label} -> {u}")
                    found = True
                    break
        except Exception as e:
            # print(f"  FAIL {u} -> {e}")
            pass
    if not found:
        print(f"FAILED ALL URLS FOR [{sid}] {label}")
