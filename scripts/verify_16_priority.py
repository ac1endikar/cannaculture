import os
import re
from PIL import Image

TARGETS = [
    ("Caramel Cream / Cream Caramel", "sweet-cream-caramel", "img/sweet-cream-caramel-bud-hd.jpg", "https://sweetseeds.com/9665-thickbox_default/cream-caramel.jpg"),
    ("Caramel Cream (00 Seeds)", "oo-caramel-cream", "img/oo-caramel-cream-bud-hd.jpg", "https://sweetseeds.com/9665-thickbox_default/cream-caramel.jpg"),
    ("Guawi (ACE Seeds)", "aceseeds-guawi", "img/aceseeds-guawi-bud-hd.jpg", "https://www.lahuertagrowshop.com/7259-large_default/guawi-ace-seeds.jpg"),
    ("Malawi (ACE Seeds)", "aceseeds-malawi", "img/aceseeds-malawi-bud-hd.jpg", "https://www.lahuertagrowshop.com/2339-large_default/malawi-regular-ace-seeds.jpg"),
    ("Super Malawi Haze (ACE Seeds)", "aceseeds-super-malawi-haze", "img/aceseeds-super-malawi-haze-bud-hd.jpg", "https://www.lahuertagrowshop.com/5516-large_default/super-malawi-haze-ace-seeds.jpg"),
    ("Valley Girl (Archive Seed Bank)", "arc-valley-girl", "img/arc-valley-girl-bud-hd.jpg", "https://www.lahuertagrowshop.com/9780-large_default/valley-girl-archive-seed-bank.jpg"),
    ("Zkittlez OG (Barney's Farm)", "bf-zkittlez-og", "img/bf-zkittlez-og-bud-hd.jpg", "https://www.barneysfarm.com/images/products/zkittlez-og-auto_1_211697.jpg"),
    ("Gorilla Ghost (BSF Seeds)", "bsf-gorilla-ghost", "img/bsf-gorilla-ghost-bud-hd.jpg", "https://www.growbarato.net/37188-large_default/gorilla-ghost.jpg"),
    ("Sandstorm (Cannabiogen)", "cannabiogen-sandstorm", "img/cannabiogen-sandstorm-bud-hd.jpg", "https://www.growbarato.net/27357-large_default/sandstorm.jpg"),
    ("Leshaze (Cannabiogen)", "cannabiogen-leshaze", "img/cannabiogen-leshaze-bud-hd.jpg", "https://www.growbarato.net/27359-large_default/leshaze.jpg"),
    ("Cheese (Dinafem)", "dinafem-cheese", "img/dinafem-cheese-bud-hd.jpg", "https://www.growbarato.net/26307-large_default/cheese.jpg"),
    ("Exodus Cheese (Green House)", "ghs-exodus-cheese", "img/ghs-exodus-cheese-bud-hd.jpg", "https://www.growbarato.net/26359-large_default/exodus-cheese.jpg"),
    ("Passion Fruit (Dutch Passion)", "dp-passion-fruit", "img/dp-passion-fruit-bud-hd.jpg", "https://dutch-passion.com/2866-large_default/passion-fruit.jpg"),
    ("Fruit Punch (Heavyweight Seeds)", "heavyweight-fruit-punch", "img/heavyweight-fruit-punch-bud-hd.jpg", "https://www.growbarato.net/26852-large_default/fruit-punch.jpg"),
    ("Terple (In-House Genetics)", "ihg-terple", "img/ihg-terple-bud-hd.jpg", "https://cdn.prod.website-files.com/65984dad3dc673726cd63bca/669165757a5711411936d057_map4.jpg"),
    ("Northern Light (Nirvana)", "nirvana-northern-light", "img/nirvana-northern-light-bud-hd.jpg", "https://herbiesheadshop.com/resized/origin/common/83/northern-light-regular-nirvana-seeds--1--buds.jpg__Lwb9YVm9OxSBGNVQ.jpg"),
    ("Northern Lights (Sensi Seeds)", "sensi-northern-lights", "img/sensi-northern-lights-bud-hd.jpg", "https://img.sensiseeds.com/images/thumbs/0000684_northern-lights-feminized-seeds_800.png"),
    ("Gelato (Nirvana Seeds)", "nirvana-gelato", "img/nirvana-gelato-bud-hd.jpg", "https://www.growbarato.net/32598-large_default/gelato-auto.jpg"),
    ("White Widow (Green House)", "ghs-white-widow", "img/ghs-white-widow-bud-hd.jpg", "https://www.growbarato.net/26356-large_default/white-widow-feminizada-green-house-seeds.jpg")
]

print("=== VERIFICACIÓN DE ARCHIVOS Y ESTÁNDAR VISUAL ===")
with open("js/data.js", "r", encoding="utf-8") as f:
    data_js = f.read()

with open("js/bundle.js", "r", encoding="utf-8") as f:
    bundle_js = f.read()

all_passed = True
for name, tid, path, url in TARGETS:
    if not os.path.exists(path):
        print(f"❌ ARCHIVO NO EXISTE: {path}")
        all_passed = False
        continue
        
    with Image.open(path) as img:
        w, h = img.size
        is_square = (w == h)
        is_hd = (w >= 600 and h >= 600)
        im_rgb = img.convert("RGB")
        corners = [im_rgb.getpixel((0,0)), im_rgb.getpixel((w-1,0)), im_rgb.getpixel((0,h-1)), im_rgb.getpixel((w-1,h-1))]
        avg_corner = sum(sum(c) for c in corners) / 12
        is_dark = (avg_corner <= 75)
        
        in_data = f'"{path}"' in data_js or f"'{path}'" in data_js
        in_bundle = f'"{path}"' in bundle_js or f"'{path}'" in bundle_js
        
        status = "[OK]" if (is_square and is_hd and is_dark and in_data and in_bundle) else "[WARN]"
        if status != "[OK]":
            all_passed = False
            
        print(f"{status} | {name:<32} | {path:<38} | {w}x{h} px | Corner Avg: {avg_corner:.1f} | in_data: {in_data} | in_bundle: {in_bundle}")

print(f"\nResultado global: {'TODAS LAS PRUEBAS SUPERADAS (100% OK)' if all_passed else 'HAY ERRORES'}")

