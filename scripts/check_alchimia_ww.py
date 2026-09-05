import urllib.request
import re

HEADERS = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.alchimiaweb.com/es/buscar?controller=search&s=white+widow"
req = urllib.request.Request(url, headers=HEADERS)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*white widow[^"]*)"', html, re.IGNORECASE)
    print(f"Alchimia search: {len(imgs)} images found")
    for src, alt in imgs[:10]:
        print(f"  {alt}: {src}")
except Exception as e:
    print("Alchimia search error:", e)
