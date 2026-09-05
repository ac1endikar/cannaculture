import urllib.request
import re

urls = [
    'https://seedfinder.eu/en/strain-info/white-willow/soma-seeds/gallery',
    'https://seedfinder.eu/en/strain-info/free-tibet/soma-seeds/gallery'
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            pics = re.findall(r'https://seedfinder\.eu/storage/pics/galerie/[^"\']+\.jpg', html)
            print(f"=== {u} ({len(pics)} pics) ===")
            for p in sorted(set(pics)):
                print(" ", p)
    except Exception as e:
        print(f"Error {u}: {e}")
