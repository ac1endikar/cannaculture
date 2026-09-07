import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Blue Pyramid & Shark
for u in ["https://pyramidseeds.com/6-product_main/blue-pyramid.jpg", "https://pyramidseeds.com/es/semillas-feminizadas/3-shark.html"]:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            print(f"Status {r.getcode()} for {u}")
            if u.endswith(".html"):
                html = r.read().decode('utf-8', errors='ignore')
                imgs = re.findall(r'https://pyramidseeds\.com/\d+-product_main/[^"\'>\s]+\.jpg', html)
                print("  Imágenes Shark:", imgs)
    except Exception as e:
        print(f"Error {u}: {e}")
