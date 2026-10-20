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

url = 'https://www.ripperseeds.com/es/feminizadas/fuel-og-semillas-feminizadas-de-marihuana'
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

# Buscar todas las imágenes que contengan un número seguido de - o large_default
imgs = re.findall(r'https?://[^\s"\'>]+?\.(?:jpg|jpeg|webp)', html)
cand = [i for i in set(imgs) if 'ripperseeds.com' in i and any(x in i for x in ('thickbox', 'large_default', 'fuel'))]
for c in cand:
    try:
        req2 = urllib.request.Request(c, headers=HEADERS)
        with urllib.request.urlopen(req2, timeout=4, context=ctx) as r2:
            data = r2.read()
            im = Image.open(io.BytesIO(data))
            print(f"[OK] {c} -> {im.size} px ({len(data)//1024} KB)")
    except Exception as e:
        pass
