import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

def check_url(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6, context=ctx) as r:
            return True, r.status, len(r.read())
    except Exception as e:
        return False, str(e), 0

print("Probando URLs oficiales directas...")
# Barney's Farm
bf_candidates = [
    'https://www.barneysfarm.com/images/products/__lsd_circle_new_21_128844.webp',
    'https://www.barneysfarm.com/images/products/lsd_circle_new_21_128844.webp',
    'https://www.barneysfarm.com/images/cache/1000/1000/crop/lsd-strain-weed-bud.jpg',
    'https://www.barneysfarm.com/images/products/__zkittlez-og-auto_circle_new_21_128844.webp',
]
for u in bf_candidates:
    ok, st, sz = check_url(u)
    print(f"BF: {u} -> {ok} ({st}, {sz} bytes)")

# Heavyweight Seeds
hw_candidates = [
    'https://heavyweightseeds.es/',
    'https://heavyweightseeds.com/',
    'https://heavyweightseeds.com/wp-content/uploads/2018/06/Lemon-Cake-700x700.jpg',
    'https://heavyweightseeds.com/wp-content/uploads/2018/06/Fruit-Punch-700x700.jpg',
]
for u in hw_candidates:
    ok, st, sz = check_url(u)
    print(f"HW: {u} -> {ok} ({st}, {sz} bytes)")
