import urllib.request
import re
import json

urls = [
    ("aurora-indica", "https://www.nirvanashop.com/products/aurora-indica-feminized-seeds"),
    ("swiss-cheese", "https://www.nirvanashop.com/products/swiss-cheese-feminized-seeds"),
    ("bubblelicious", "https://www.nirvanashop.com/products/bubblelicious-feminized-seeds"),
    ("master-kush", "https://www.nirvanashop.com/products/master-kush-feminized-seeds"),
    ("wonder-woman", "https://www.nirvanashop.com/products/wonder-woman-feminized-seeds"),
    ("jock-horror", "https://www.nirvanashop.com/products/jock-horror-feminized-seeds"),
    ("somango-xxl", "https://www.nirvanashop.com/products/somango-xxl-feminized-seeds"),
    ("super-skunk", "https://www.nirvanashop.com/products/super-skunk-feminized-seeds"),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract og:image or cdn images
            og_img = re.search(r'<meta property="og:image" content="([^"]+)"', html)
            title = re.search(r'<title>([^<]+)</title>', html)
            print(f"✅ {name}: Status {resp.status}")
            if title:
                print(f"   Title: {title.group(1).strip()}")
            if og_img:
                print(f"   Image: {og_img.group(1)}")
    except Exception as e:
        print(f"❌ {name} ({u}): {e}")
