import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

urls = [
    "https://humboldtseedcompany.com/caramel-cream/",
    "https://humboldtseedcompany.com/product/caramel-cream/",
    "https://humboldtseedcompany.es/variedades/caramel-cream/"
]

for u in urls:
    print(f"Trying {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"Success! Length: {len(html)}")
            imgs = re.findall(r'https://[^"\'>]+humboldtseedcompany[^"\'>]+\.(?:jpg|jpeg|png|webp)', html)
            for im in set(imgs):
                if any(k in im.lower() for k in ['caramel', 'cream', 'uploads']):
                    print("  Img:", im)
            break
    except Exception as e:
        print("  Error:", e)
