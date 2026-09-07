import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

candidates = [
    "ak-48-feminized",
    "swiss-cheese",
    "swiss-cheese-feminized-seeds",
    "chrystal-feminized",
    "ice-cream-cake-feminized",
    "blue-mystic-feminized",
    "blackjack-feminized",
    "papaya-feminized",
    "hawaii-maui-waui-feminized",
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for handle in candidates:
    u = f"https://nirvanashop.com/es/products/{handle}"
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>([^<]+)</title>', html)
            og_img = re.search(r'<meta property="og:image" content="([^"]+)"', html)
            print(f"✅ {handle}: {resp.status}")
            if title_m:
                print(f"   Title: {title_m.group(1).strip()}")
            if og_img:
                print(f"   Image: {og_img.group(1)}")
    except Exception as e:
        # print(f"❌ {handle}: {e}")
        pass
