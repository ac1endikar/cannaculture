import urllib.request
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = [
    'https://www.cannapot.com/shop/cannabis-seeds/soma-seeds/white-willow_en.html',
    'https://www.cannapot.com/shop/cannabis-seeds/soma-seeds/white-light_en.html',
    'https://www.cannapot.com/shop/cannabis-seeds/soma-seeds/free-tibet_en.html',
    'https://oaseeds.com/es/1014-soma-seeds-white-willow.html',
    'https://alphagrowers.es/producto/white-willow-de-soma-sacred-seeds/',
    'https://matillaplant.com/tienda/semillas-marihuana/soma-sacred-seeds/white-willow/'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
            print(f"=== {u} ({len(imgs)} imgs) ===")
            for img in imgs:
                if any(k in img.lower() for k in ['white', 'willow', 'tibet', 'product', 'upload']):
                    print("  ", img)
    except Exception as e:
        print(f"Failed {u}: {e}")
