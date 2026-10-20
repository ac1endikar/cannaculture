#!/usr/bin/env python3
"""
Corrección de Auditoría - Lote 1: Placeholders y Duplicados Masivos
Desvincula las fotos compartidas y dota de identidad botánica individual a cada variedad.
"""
import os
import sys
import re
import urllib.request
import ssl
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'
INDEX_HTML = r'd:\cannaculture\index.html'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

def download_and_save(url, output_fname, min_dim=600):
    output_path = os.path.join(IMG_DIR, output_fname)
    if os.path.exists(output_path) and os.path.getsize(output_path) > 30000:
        try:
            im = Image.open(output_path)
            if im.size[0] >= min_dim and im.size[1] >= min_dim:
                print(f"  [EXISTE OK] {output_fname} ({im.size}, {os.path.getsize(output_path)//1024} KB)")
                return True
        except Exception:
            pass

    print(f"  [DESCARGANDO] {url} -> {output_fname}...")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            data = r.read()
            im = Image.open(io.BytesIO(data))
            if im.mode in ('RGBA', 'P'):
                im = im.convert('RGB')
            w, h = im.size
            if w < min_dim or h < min_dim:
                print(f"  [AVISO DIMENSION] {output_fname}: {w}x{h} px (menor a {min_dim}px)")
            im.save(output_path, 'JPEG', quality=95)
            print(f"  [OK] Guardado {output_fname} ({w}x{h} px, {os.path.getsize(output_path)//1024} KB)")
            return True
    except Exception as e:
        print(f"  [ERROR] No se pudo descargar {url}: {e}")
        return False

# 1. Tareas de Descarga para Lote 1
DOWNLOADS = [
    # Grupo 1: R-Kiem Seeds
    ('https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/negra44.jpg', 'rkiem-negra-44-hd.jpg'),
    ('https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/sublimator.jpg', 'rkiem-sublimator-hd.jpg'),
    ('https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/Icer.jpg', 'rkiem-icer-hd.jpg'),
    ('https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/muse.jpg', 'rkiem-muse-hd.jpg'),
    ('https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/Zkiem.jpg', 'rkiem-zkiem-hd.jpg'),

    # Grupo 2: Serious Seeds
    ('https://www.seriousseeds.com/sites/default/files/gallery/ak-47_fem_dry009_copyright-by-gbi-2012.jpg', 'serious-ak47-bud-hd.jpg'),
    ('https://www.seriousseeds.com/sites/default/files/gallery/white-russian-topbud---choice-1-pic.jpg', 'serious-white-russian-bud-hd.jpg'),
    ('https://www.seriousseeds.com/sites/default/files/gallery/kali-mist-topbud---choice-1-pic.jpg', 'serious-kali-mist-bud-hd.jpg'),

    # Grupo 4: Blimburn / Heavyweight
    ('https://blimburnseeds.com/wp-content/uploads/2023/01/Green-crack-1-1024x1024.jpg.webp', 'blimburn-green-crack-hd.jpg'),
    ('https://oaseeds.com/8381-thickbox_default/blimburn-seeds-santa-muerte.jpg', 'blimburn-santa-muerte-hd.jpg'),
    ('https://blimburnseeds.com/wp-content/uploads/2021/04/Chocolopez.webp', 'blimburn-chocolopez-hd.jpg'),
    ('https://heavyweightseeds.com/wp-content/uploads/2018/10/MoneyBushG1.jpg', 'heavyweight-money-bush-hd.jpg'),

    # Grupo 5: Cannabiogen
    ('https://mr-hanf.de/images/product_images/popup_images/Peyote%20Purple-8.webp', 'cannabiogen-peyote-purple-hd.jpg'),
    ('https://herbiesheadshop.com/resized/origin/common/26/Nepal-Jam-Regulars-socvetiya.jpg__imvBw8FDRduo2vV9.jpg', 'cannabiogen-nepal-jam-hd.jpg'),
    ('https://www.mrnatural.es/6064-thickbox_default/mangobiche-kush.jpg', 'cannabiogen-mangobiche-kush-hd.jpg'),

    # Grupo 6: Cepas cruzadas en nirvana-gsc
    ('https://pyramidseeds.com/19-product_main/wembley.jpg', 'pyramid-wembley-hd.jpg'),
    ('https://pyramidseeds.com/5-product_main/anubis.jpg', 'pyramid-anubis-hd.jpg'),
    ('https://blimburnseeds.com/wp-content/uploads/2021/04/Mamba-Negra.webp', 'blimburn-mamba-negra-hd.jpg'),
    ('https://blimburnseeds.com/wp-content/uploads/2021/04/Grandaddy-purple.jpeg', 'blimburn-granddaddy-purple-hd.jpg'),
]

print("=" * 70)
print("PASO 1: DESCARGA DE IMÁGENES BOTÁNICAS INDIVIDUALES")
print("=" * 70)
for url, fname in DOWNLOADS:
    download_and_save(url, fname)

# 2. Mapeo de cepa ID -> nueva imagen
STRAIN_UPDATES = {
    # Grupo 1: R-Kiem Seeds (mantener rkiem-2y2 con su foto)
    'rkiem-negra-44': 'img/rkiem-negra-44-hd.jpg',
    'rkiem-sublimator': 'img/rkiem-sublimator-hd.jpg',
    'rkiem-icer': 'img/rkiem-icer-hd.jpg',
    'rkiem-muse': 'img/rkiem-muse-hd.jpg',
    'rkiem-zkiem': 'img/rkiem-zkiem-hd.jpg',

    # Grupo 2: Serious Seeds (mantener serious-serious-happiness con su foto)
    'serious-ak-47': 'img/serious-ak47-bud-hd.jpg',
    'serious-white-russian': 'img/serious-white-russian-bud-hd.jpg',
    'serious-kali-mist': 'img/serious-kali-mist-bud-hd.jpg',

    # Grupo 3: Variantes Northern Lights (cada banco con foto específica)
    'nirvana-northern-light': 'img/nirvana-northern-light-flower-hd.jpg',
    'sensi-northern-lights': 'img/sensi-northern-lights-bud.jpg',
    'wls-northern-lights': 'img/wls-northern-lights.jpg',
    'rqs-northern-light': 'img/northern-lights-real-hd.jpg',

    # Grupo 4: Blimburn / Heavyweight (mantener heavyweight-goldmine con su foto)
    'blimburn-green-crack': 'img/blimburn-green-crack-hd.jpg',
    'blimburn-santa-muerte': 'img/blimburn-santa-muerte-hd.jpg',
    'blimburn-chocolopez': 'img/blimburn-chocolopez-hd.jpg',
    'heavyweight-money-bush': 'img/heavyweight-money-bush-hd.jpg',

    # Grupo 5: Cannabiogen (mantener cannabiogen-hash-fruit con su foto)
    'cannabiogen-peyote-purple': 'img/cannabiogen-peyote-purple-hd.jpg',
    'cannabiogen-nepal-jam': 'img/cannabiogen-nepal-jam-hd.jpg',
    'cannabiogen-mangobiche-kush': 'img/cannabiogen-mangobiche-kush-hd.jpg',

    # Grupo 6: Cepas cruzadas en nirvana-gsc
    'pyramid-wembley': 'img/pyramid-wembley-hd.jpg',
    'pyramid-anubis': 'img/pyramid-anubis-hd.jpg',
    'blimburn-mamba-negra': 'img/blimburn-mamba-negra-hd.jpg',
    'blimburn-granddaddy-purple': 'img/blimburn-granddaddy-purple-hd.jpg',
}

print("\n" + "=" * 70)
print("PASO 2: ACTUALIZACIÓN DE DATA.JS")
print("=" * 70)

with open(DATA_JS, 'r', encoding='utf-8') as f:
    lines = f.readlines()

updated_lines = []
current_strain_id = None
updated_count = 0

for line in lines:
    m_id = re.search(r'id:\s*"([^"]+)"', line)
    if m_id:
        current_strain_id = m_id.group(1)
        
    m_img = re.search(r'image:\s*"([^"]+)"', line)
    if m_img and current_strain_id in STRAIN_UPDATES:
        new_img = STRAIN_UPDATES[current_strain_id]
        old_img = m_img.group(1)
        line = re.sub(r'image:\s*"[^"]+"', f'image: "{new_img}"', line)
        print(f"  [DATA.JS] {current_strain_id}: {old_img} -> {new_img}")
        updated_count += 1
        # reset to avoid multiple replacements if image field repeated
        current_strain_id = None
        
    updated_lines.append(line)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)

print(f"\nTotal cepas actualizadas en data.js: {updated_count} / {len(STRAIN_UPDATES)}")

print("\n" + "=" * 70)
print("PASO 3: RECOMPILACIÓN DE BUNDLE.JS")
print("=" * 70)
os.system(f'python "{os.path.join(os.path.dirname(__file__), "build_bundle.py")}"')

print("\n" + "=" * 70)
print("PASO 4: ACTUALIZACIÓN DE VERSIÓN DE CACHÉ EN INDEX.HTML")
print("=" * 70)
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

NEW_VERSION = "2026_phase2_custom3_v111"
html_updated = re.sub(r'bundle\.js\?v=[^"]+', f'bundle.js?v={NEW_VERSION}', html)

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(html_updated)

print(f"index.html actualizado con script bundle.js?v={NEW_VERSION}")
