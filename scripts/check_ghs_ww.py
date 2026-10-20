import urllib.request
import re

url = "https://greenhouseseeds.nl/products/white-widow"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://[^"]*greenhouseseeds\.nl[^"]*\.(?:jpg|png|webp)', html)
    print(f"Greenhouse images: {len(imgs)}")
    for img in sorted(set(imgs)):
        print(" ", img)
except Exception as e:
    print("Error:", e)
