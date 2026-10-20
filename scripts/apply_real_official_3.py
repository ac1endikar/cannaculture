import urllib.request
import ssl
import os
import sys
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

downloads = [
    {
        'id': 'bf-lsd',
        'fname': 'bf-lsd-official-real.jpg',
        'url': 'https://www.barneysfarm.com/images/products/lsd_1_634481.jpg',
        'source': 'Barneys Farm Oficial'
    },
    {
        'id': 'heavyweight-lemon-cake',
        'fname': 'heavyweight-lemon-cake-official-real.jpg',
        'url': 'https://heavyweightseeds.com/wp-content/uploads/2018/10/LemonCakeG1.jpg',
        'source': 'Heavyweight Seeds Oficial'
    },
    {
        'id': 'heavyweight-fruit-punch',
        'fname': 'heavyweight-fruit-punch-official-real.jpg',
        'url': 'https://heavyweightseeds.com/wp-content/uploads/2018/10/FruitPungG1.jpg',
        'source': 'Heavyweight Seeds Oficial'
    }
]

print("=== DESCARGANDO FOTOS OFICIALES 100% REALES ===")
for d in downloads:
    dest = os.path.join(IMG_DIR, d['fname'])
    req = urllib.request.Request(d['url'], headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        data = r.read()
    im = Image.open(io.BytesIO(data)).convert('RGB')
    
    # Recorte 1:1 centrado
    w, h = im.size
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im_crop = im.crop((left, top, left + crop_sz, top + crop_sz))
    if crop_sz < 600:
        im_crop = im_crop.resize((600, 600), Image.Resampling.LANCZOS)
    im_crop.save(dest, 'JPEG', quality=95, optimize=True)
    print(f"Descargado {d['fname']}: {im_crop.size} px ({os.path.getsize(dest)//1024} KB)")
    print(f"  URL origen: {d['url']}")

# Actualizar data.js
with open(DATA_JS, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('image: "img/bf-lsd-bud-hd.jpg"', 'image: "img/bf-lsd-official-real.jpg"')
text = text.replace('image: "img/heavyweight-lemon-cake-bud-hd.jpg"', 'image: "img/heavyweight-lemon-cake-official-real.jpg"')
text = text.replace('image: "img/heavyweight-fruit-punch-bud-hd.jpg"', 'image: "img/heavyweight-fruit-punch-official-real.jpg"')

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(text)

print("\n=== DATA.JS ACTUALIZADO ===")
