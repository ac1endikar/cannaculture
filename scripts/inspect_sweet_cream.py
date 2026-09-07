import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

u = "https://sweetseeds.com/es/semillas-fotodependientes/35-cream-caramel.html"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

imgs = re.findall(r'https://sweetseeds\.com/\d+-[^"\'>\s]+\.(?:jpg|png|webp)', html)
print("Imágenes en 35-cream-caramel:")
for img in set(imgs):
    if "thickbox" in img or "large" in img:
        print(" ", img)
        r2 = urllib.request.urlopen(urllib.request.Request(img, headers=headers), timeout=5, context=ctx)
        im = Image.open(io.BytesIO(r2.read())).convert('RGB')
        print(f"    Size: {im.size}")
