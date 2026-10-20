import urllib.request
import re

urls = [
    'https://dutch-passion.com/en/blog/white-widow-grow-review-n1012',
    'https://dutch-passion.com/en/blog/top-5-white-widow-grow-reviews-n1098',
    'https://dutch-passion.com/es/blog/white-widow-seguimiento-de-cultivo-n1012',
]

headers = {'User-Agent': 'Mozilla/5.0'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://dutch-passion\.com/img/cms/[^"\']+\.(?:jpg|png|webp)', html)
            print(f"=== {u} ({len(imgs)} imgs) ===")
            for img in set(imgs):
                print(" ", img)
    except Exception as e:
        print(f"Failed {u}: {e}")
