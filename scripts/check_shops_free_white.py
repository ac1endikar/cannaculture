import urllib.request
import urllib.parse
import re
import json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

sites = [
    ('Alchimia', 'https://www.alchimiaweb.com/es/buscar?controller=search&s=Free+White'),
    ('Growbarato', 'https://www.growbarato.net/buscar?controller=search&s=Free+White'),
    ('Oaseeds', 'https://oaseeds.com/es/buscar?controller=search&s=Free+White'),
    ('Seedfinder', 'https://en.seedfinder.eu/search/results/?q=Free+White')
]

for name, url in sites:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as r:
            content = r.read().decode('utf-8', errors='ignore')
        print(f"=== {name} ===")
        # Look for product titles
        titles = re.findall(r'<a[^>]+class="[^"]*product-name[^"]*"[^>]*title="([^"]+)"', content)
        if not titles:
            titles = re.findall(r'class="product-title"[^>]*><a[^>]*>([^<]+)</a>', content)
        if not titles:
            titles = re.findall(r'<h3[^>]*><a[^>]*>([^<]+)</a>', content)
        print("Titles found:", titles[:5])
    except Exception as e:
        print(f"Error {name}: {e}")
