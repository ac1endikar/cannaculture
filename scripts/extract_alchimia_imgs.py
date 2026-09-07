import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

for name, u in [("Sandstorm", "https://www.alchimiaweb.com/sandstorm-product-304.php"), ("Caribe", "https://www.alchimiaweb.com/caribe-product-303.php")]:
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://[^"\'>\s]+\.(?:jpg|png|webp)', html)
    print(f"[{name}] Imágenes:")
    for img in set(imgs):
        if "product" in img or "images" in img or "ils" in img:
            print(" ", img)
