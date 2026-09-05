import urllib.request
import re

urls = [
    'https://en.seedfinder.eu/strain-info/white-willow/soma-seeds/',
    'https://en.seedfinder.eu/strain-info/free-tibet/soma-seeds/',
    'https://en.seedfinder.eu/strain-info/white-light/soma-seeds/',
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"=== {u} ({len(html)} bytes) ===")
            # Look for picture gallery links
            gallery = re.findall(r'href="([^"]*(?:picture|foto|gallery|galerie)[^"]*)"', html, re.IGNORECASE)
            print("Gallery links:", gallery)
            img_srcs = re.findall(r'src="([^"]*(?:pics|database|upload)[^"]*)"', html, re.IGNORECASE)
            print("Image srcs:", img_srcs)
    except Exception as e:
        print(f"Error {u}: {e}")
