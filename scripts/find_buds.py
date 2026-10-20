import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls_to_test = [
    # BF LSD
    ('bf-lsd', 'https://www.barneysfarm.com/lsd-46'),
    ('heavyweight-fruit-punch', 'https://www.alchimiaweb.com/fruit-punch-product-4796.php'),
    ('heavyweight-lemon-cake', 'https://www.alchimiaweb.com/lemon-cake-product-10651.php'),
]

for sid, url in urls_to_test:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https?://[^"\'>]+\.(?:jpg|jpeg|png|webp)', html)
            print(f"\n=== {sid} ({url}) ===")
            buds = [img for img in imgs if any(k in img.lower() for k in ('bud', 'product', 'fruit', 'lemon', 'lsd'))]
            for b in buds[:5]:
                print("  ", b)
    except Exception as e:
        print(f"Error {sid}: {e}")
