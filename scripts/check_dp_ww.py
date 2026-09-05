import urllib.request
import re

url = "https://dutch-passion.com/en/cannabis-seeds/white-widow"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://[^"]*dutch-passion[^"]*\.(?:jpg|png|webp)', html)
    print(f"Total Dutch Passion images: {len(imgs)}")
    for img in sorted(set(imgs)):
        if any(k in img.lower() for k in ['white', 'widow', 'product', 'media']):
            print(" ", img)
except Exception as e:
    print("Error:", e)
