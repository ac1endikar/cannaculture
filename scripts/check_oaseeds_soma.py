import urllib.request
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def search_oaseeds():
    url = "https://oaseeds.com/es/103-soma-seeds"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        products = re.findall(r'<a[^>]+class="thumbnail product-thumbnail"[^>]*>.*?<img[^>]+src="([^"]+)"[^>]*alt="([^"]+)"', html, re.DOTALL)
        if not products:
            products = re.findall(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]+)"[^>]*class="[^"]*product', html)
        print(f"Oaseeds Soma products: {len(products)}")
        for p in products[:20]:
            print(" ", p)
    except Exception as e:
        print("Oaseeds error:", e)

search_oaseeds()
