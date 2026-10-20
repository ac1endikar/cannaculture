import urllib.request
import urllib.parse
import re

HEADERS = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.growbarato.net/buscar?controller=search&s=white+widow"
req = urllib.request.Request(url, headers=HEADERS)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*white widow[^"]*)"', html, re.IGNORECASE)
    print(f"Found {len(imgs)} white widow imgs on growbarato search:")
    for src, alt in imgs:
        print(f"  {alt}: {src}")
except Exception as e:
    print("Error:", e)
