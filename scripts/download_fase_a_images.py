import urllib.request
import os
import sys
import ssl
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://seedfinder.eu/'
}

image_sources = [
    ("sugar-black-rose", "https://www.deliciousseeds.com/media/catalog/product/s/u/sugar-black-rose_7.jpg"),
    ("eleven-roses", "https://www.deliciousseeds.com/media/catalog/product/e/l/eleven-roses_1.jpg"),
    ("golosa", "https://www.deliciousseeds.com/media/catalog/product/g/o/golosa-3_5.jpg"),
    ("marmalate", "https://www.deliciousseeds.com/media/catalog/product/m/a/marmalate-fem-web.jpg"),
    ("cotton-candy-kush", "https://www.deliciousseeds.com/media/catalog/product/c/o/cotton_candy_5.jpg"),
    ("caramelo", "https://www.deliciousseeds.com/media/catalog/product/c/a/caramelo_6.jpg"),
    ("critical-kali-mist", "https://seedfinder.eu/storage/pics/galerie/Delicious_Seeds/Critical_Kali_Mist/08081480245240788.jpg"),
    ("unknown-kush", "https://www.deliciousseeds.com/media/catalog/product/d/e/desconocida-kush-marca.jpg"),
    ("super-silver-haze-mrnice", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Super_Silver_Haze/14102403717444728.jpg"),
    ("black-widow", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Black_Widow/15031979555231669.jpg"),
    ("critical-mass-mrnice", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Critical_Mass/30041966787247587.jpg"),
    ("medicine-man", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Medicine_Man/27022106223475427.jpg"),
    ("nevilles-haze-mrnice", "https://seedfinder.eu/storage/pics/galerie/Green_House_Seeds/Nevilles_Haze/12101832566233821.jpg"),
    ("early-skunk-mrnice", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Early_Skunk/21022019399949710.jpg"),
    ("shark-shock", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Shark_Shock/01051860900114396.jpg"),
    ("mango-haze", "https://seedfinder.eu/storage/pics/galerie/Mr_Nice_Seedbank/Mango_Haze/17091470437559408.jpg"),
]

os.makedirs('images/strains', exist_ok=True)
os.makedirs('img', exist_ok=True)

print("Descargando y procesando las 16 imágenes botánicas reales oficiales...")

for sid, url in image_sources:
    out_jpg = f"images/strains/{sid}.jpg"
    out_webp = f"images/strains/{sid}.webp"
    img_dir_jpg = f"img/{sid}.jpg"
    img_dir_webp = f"img/{sid}.webp"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            raw_data = resp.read()
            im = Image.open(io.BytesIO(raw_data))
            im_rgb = im.convert('RGB')
            
            # Crop to square if needed, focusing on center/bud
            w, h = im_rgb.size
            min_dim = min(w, h)
            left = (w - min_dim) // 2
            top = (h - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim
            im_cropped = im_rgb.crop((left, top, right, bottom))
            
            # Resize to high resolution 800x800
            im_800 = im_cropped.resize((800, 800), Image.Resampling.LANCZOS)
            
            # Save JPG and WebP in images/strains and img/
            im_800.save(out_jpg, 'JPEG', quality=92)
            im_800.save(out_webp, 'WEBP', quality=92)
            im_800.save(img_dir_jpg, 'JPEG', quality=92)
            im_800.save(img_dir_webp, 'WEBP', quality=92)
            
            print(f"✅ {sid:25} -> {out_jpg} ({os.path.getsize(out_jpg):,} B, {im_800.size[0]}x{im_800.size[1]})")
    except Exception as e:
        print(f"❌ Error en {sid} ({url}): {e}")

print("\nVerificación final de archivos en disco:")
for sid, _ in image_sources:
    p = f"images/strains/{sid}.jpg"
    print(f"  {p}: {'EXISTE' if os.path.exists(p) else 'NO EXISTE'} ({os.path.getsize(p) if os.path.exists(p) else 0:,} B)")
