import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

strains = [
    ("aurora-indica", "https://nirvanashop.com/es/products/aurora-indica-feminized"),
    ("swiss-cheese", "https://nirvanashop.com/es/products/swiss-cheese-feminized"),
    ("bubblelicious", "https://nirvanashop.com/es/products/bubblelicious-feminized"),
    ("master-kush", "https://nirvanashop.com/es/products/master-kush-feminized"),
    ("wonder-woman", "https://nirvanashop.com/es/products/wonder-woman-feminized"),
    ("jock-horror", "https://nirvanashop.com/es/products/jock-horror-feminized"),
    ("somango-xxl", "https://nirvanashop.com/es/products/somango-xxl-feminized"),
    ("super-skunk", "https://nirvanashop.com/es/products/super-skunk-feminized"),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for name, u in strains:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>([^<]+)</title>', html)
            og_img = re.search(r'<meta property="og:image" content="([^"]+)"', html)
            thc_m = re.search(r'([0-9]+(?:\.[0-9]+)?\s*%\s*-\s*[0-9]+(?:\.[0-9]+)?\s*%\s*THC|\bTHC\s*[0-9]+(?:\.[0-9]+)?%)', html, re.IGNORECASE)
            print(f"✅ {name}: {resp.status}")
            if title_m:
                print(f"   Title: {title_m.group(1).strip()}")
            if og_img:
                print(f"   Image: {og_img.group(1)}")
            if thc_m:
                print(f"   THC info: {thc_m.group(0)}")
    except Exception as e:
        print(f"❌ {name} ({u}): {e}")
