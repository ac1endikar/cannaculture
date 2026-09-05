import urllib.request
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

urls = [
    'https://growdiaries.com/seedbank/soma-seeds/white-willow',
    'https://growdiaries.com/seedbank/soma-seeds/white-light',
    'https://growdiaries.com/seedbank/soma-seeds/free-tibet',
    'https://growdiaries.com/seedbank/soma-seeds'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"=== {u} ({resp.status}) ===")
            imgs = re.findall(r'https://[^"]*(?:seed_item_photos|diaries|crop|diary_photos)[^"]*\.(?:jpg|png|webp)', html, re.IGNORECASE)
            for img in set(imgs):
                print("  ", img)
    except Exception as e:
        print(f"Error {u}: {e}")
