import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

urls = [
    "https://www.zamnesia.com/8302-sensi-seeds-sensi-amnesia-feminized.html",
    "https://www.zamnesia.com/es/8302-sensi-seeds-sensi-amnesia-feminizada.html",
    "https://www.zamnesia.com/8303-sensi-seeds-sensi-amnesia-auto.html",
    "https://www.zamnesia.com/es/8303-sensi-seeds-sensi-amnesia-auto.html"
]

for u in urls:
    print(f"Trying {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://[^"\'>]+\.(?:jpg|jpeg|png|webp)', html)
            imgs = [i for i in set(imgs) if any(k in i.lower() for k in ['sensi', 'amnesia', 'media', 'product'])]
            print(f"Found {len(imgs)} imgs in {u}")
            for im in imgs:
                print(" ", im)
            break
    except Exception as e:
        print(" Error:", e)
