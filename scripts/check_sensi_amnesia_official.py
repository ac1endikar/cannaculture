import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

urls = [
    "https://sensiseeds.com/es/semillas-feminizadas/sensi-seeds/sensi-amnesia",
    "https://sensiseeds.com/en/feminized-seeds/sensi-seeds/sensi-amnesia",
    "https://sensiseeds.com/es/semillas-feminizadas/sensi-seeds/sensi-amnesia-xxl-autofloreciente",
    "https://sensiseeds.com/en/feminized-seeds/sensi-seeds/sensi-amnesia-auto"
]

for u in urls:
    print(f"Trying {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://[^"\'>]+media[^"\'>]+\.(?:jpg|jpeg|png|webp)', html)
            imgs = [i for i in set(imgs) if any(k in i.lower() for k in ['sensi-amnesia', 'product'])]
            print(f"Found {len(imgs)} imgs in {u}")
            for im in imgs:
                print(" ", im)
            break
    except Exception as e:
        print(" Error:", e)
