import urllib.request
import re

url = "https://www.royalqueenseeds.com/feminized-seeds/122-white-widow.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://[^"]*royalqueenseeds\.com[^"]*\.(?:jpg|png|webp)', html)
    print(f"RQS images: {len(imgs)}")
    for img in sorted(set(imgs)):
        if any(k in img.lower() for k in ['white-widow', 'product', 'gallery']):
            print(" ", img)
except Exception as e:
    print("Error:", e)
