import urllib.request
import urllib.parse
import json
import re
import os
import sys
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

category_urls = [
    "https://www.thseeds.com/en/cannabis-seeds.html",
    "https://www.thseeds.com/en/cannabis-seeds/feminized-cannabis-seeds.html",
    "https://www.thseeds.com/en/cannabis-seeds/regular-cannabis-seeds.html",
    "https://www.thseeds.com/en/cannabis-seeds/autoflowering-cannabis-seeds.html",
    "https://www.thseeds.com/es/semillas-de-cannabis.html",
    "https://www.thseeds.com/es/semillas-de-cannabis/semillas-de-cannabis-feminizadas.html"
]

product_urls = set()

for cat in category_urls:
    try:
        req = urllib.request.Request(cat, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        # Find product links
        found = re.findall(r'href=["\'](https?://www\.thseeds\.com/(?:en|es)/[^"\']+\.html)["\']', html)
        for link in found:
            if not any(x in link for x in ['clothing', 'cart', 'checkout', 'login', 'account', 'customer', 'news', 'rss', 'wishlist']):
                # Ignore category pages themselves
                if not link.endswith(('cannabis-seeds.html', 'feminized-cannabis-seeds.html', 'regular-cannabis-seeds.html', 'autoflowering-cannabis-seeds.html', 'semillas-de-cannabis.html', 'cbd-strains.html')):
                    product_urls.add(link)
    except Exception as e:
        print(f"Error reading {cat}: {e}")

print(f"Total T.H.Seeds product pages found: {len(product_urls)}")
for p in sorted(list(product_urls)):
    print("  -", p)
