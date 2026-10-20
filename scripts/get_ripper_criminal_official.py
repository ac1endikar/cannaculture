import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

urls = [
    "https://www.ripperseeds.com/es/semillas-feminizadas/criminal-plus",
    "https://www.ripperseeds.com/en/feminized-seeds/criminal-plus",
    "https://www.ripperseeds.com/es/inicio/2-criminal-semillas-feminizadas-de-marihuana.html",
    "https://www.ripperseeds.com/es/semillas-feminizadas/2-criminal-semillas-feminizadas-de-marihuana.html"
]

for url in urls:
    print(f"Trying {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"Success! Length: {len(html)}")
            imgs = re.findall(r'https://[^"\'>]+large_default[^"\'>]+\.jpg', html)
            for im in set(imgs):
                print("  Img:", im)
            break
    except Exception as e:
        print("  Failed:", e)
