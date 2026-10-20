import urllib.request
import re

urls = [
    'https://en.seedfinder.eu/strain-info/white-light/soma-seeds/',
    'https://en.seedfinder.eu/strain-info/white-willow/soma-seeds/',
    'https://en.seedfinder.eu/strain-info/free-tibet/soma-seeds/'
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        print(f"=== {u} ===")
        # Look for JavaScript images array
        m = re.findall(r'(\{[^}]*big[^}]*\})', html)
        for obj in m:
            print("  ", obj)
    except Exception as e:
        print(f"Error {u}: {e}")
