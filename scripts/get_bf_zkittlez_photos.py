import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

url = 'https://www.barneysfarm.com/zkittlez-og-auto-472'
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

imgs = re.findall(r'https?://[^\s"\'>]+?\.(?:jpg|jpeg|png|webp)', html)
imgs = [i for i in set(imgs) if any(k in i.lower() for k in ('zkittlez', 'products'))]
print(f"Imágenes de Zkittlez OG en {url} ({len(imgs)}):")
for img in sorted(imgs):
    try:
        req2 = urllib.request.Request(img, headers=HEADERS)
        with urllib.request.urlopen(req2, timeout=5, context=ctx) as r2:
            data = r2.read()
            im = Image.open(io.BytesIO(data))
            print(f"  [OK] {img} -> {im.size} px ({len(data)//1024} KB)")
    except Exception as ex:
        pass
