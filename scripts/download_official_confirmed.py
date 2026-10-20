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

CONFIRMED_DOWNLOADS = [
    {
        'id': 'bf-lsd',
        'file': 'bf-lsd-bud-hd.jpg',
        'url': 'https://www.barneysfarm.com/images/products/lsd_1_634481.jpg',
        'source': "Barney's Farm (Catálogo Oficial)",
        'min_size': (600, 600)
    },
    {
        'id': 'heavyweight-lemon-cake',
        'file': 'heavyweight-lemon-cake-bud-hd.jpg',
        'url': 'https://heavyweightseeds.com/wp-content/uploads/2018/10/LemonCakeG1.jpg',
        'source': "Heavyweight Seeds (Catálogo Oficial)",
        'min_size': (600, 600)
    },
    {
        'id': 'heavyweight-fruit-punch',
        'file': 'heavyweight-fruit-punch-bud-hd.jpg',
        'url': 'https://heavyweightseeds.com/wp-content/uploads/2018/10/FruitPungG1.jpg',
        'source': "Heavyweight Seeds (Catálogo Oficial)",
        'min_size': (600, 600)
    },
    {
        'id': 'bf-zkittlez-og',
        'file': 'bf-zkittlez-og-bud-hd.jpg',
        'url': 'https://www.barneysfarm.com/images/products/zkittlez-og-auto_4_211697.jpg',
        'source': "Barney's Farm (Catálogo Oficial)",
        'min_size': (600, 600)
    },
    {
        'id': 'ghs-hawaiian-snow',
        'file': 'ghs-hawaiian-snow-bud-hd.jpg',
        'url': 'https://shop.greenhouseseeds.nl/images/detailed/10/HAWAIIAN_SNOW.jpg',
        'source': "Green House Seed Co. (Catálogo Oficial)",
        'min_size': (600, 600)
    },
    {
        'id': 'ripper-zombie-wash',
        'file': 'ripper-zombie-wash-bud-hd.jpg',
        'url': 'https://www.ripperseeds.com/555-large_default/zombie-kush-semillas-feminizadas-de-marihuana.jpg',
        'source': "Ripper Seeds (Catálogo Oficial)",
        'min_size': (600, 600)
    },
    {
        'id': 'ripper-brain-cake',
        'file': 'ripper-brain-cake-bud-hd.jpg',
        'url': 'https://www.ripperseeds.com/534-large_default/brain-cake-semillas-feminizadas-de-marihuana.jpg',
        'source': "Ripper Seeds (Catálogo Oficial)",
        'min_size': (600, 600)
    }
]

print("=== DESCARGA DE FOTOGRAFÍAS REALES DIRECTAS DE BANCOS OFICIALES ===")
for item in CONFIRMED_DOWNLOADS:
    dest_path = os.path.join(IMG_DIR, item['file'])
    url = item['url']
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            data = r.read()
        im = Image.open(io.BytesIO(data))
        # Normalizar a RGB y guardar con calidad 95
        if im.mode != 'RGB':
            im = im.convert('RGB')
            
        # Si tiene ratio rectangular, recortar centrado a 1:1 o asegurar >= 600x600
        w, h = im.size
        crop_sz = min(w, h)
        left = (w - crop_sz) // 2
        top = (h - crop_sz) // 2
        im_crop = im.crop((left, top, left + crop_sz, top + crop_sz))
        if crop_sz < 600:
            im_crop = im_crop.resize((600, 600), Image.Resampling.LANCZOS)
            
        im_crop.save(dest_path, 'JPEG', quality=95, optimize=True)
        print(f"  ✓ {item['id']} ({item['file']}): {im_crop.size} px ({os.path.getsize(dest_path)//1024} KB)")
        print(f"     URL Oficial: {url}")
        print(f"     Fuente: {item['source']}\n")
    except Exception as ex:
        print(f"  ❌ Error en {item['id']}: {ex}")
