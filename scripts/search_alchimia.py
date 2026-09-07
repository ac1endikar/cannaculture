import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

queries = [
    'lemon-og-candy',
    'kmintz',
    'criminal-plus',
    'black-jack',
    'sensi-amnesia',
    'cream-caramel',
    'zkittlez-og',
    'white-widow',
    'terple',
    'rainbow-studz'
]

for q in queries:
    url = f'https://www.alchimiaweb.com/es/buscar?controller=search&s={q}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Extract product page URLs
            prod_links = re.findall(r'https?://www\.alchimiaweb\.com/es/[a-z0-9\-]+\.html', html)
            print(f"Query: {q} -> Found {len(prod_links)} product links")
            if prod_links:
                print(f"  First: {prod_links[0]}")
    except Exception as e:
        print(f"Query {q} failed: {e}")
