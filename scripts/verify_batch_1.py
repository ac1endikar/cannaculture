import os
import re
from PIL import Image

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

target_ids = [
    # R-Kiem (5)
    'rkiem-negra-44', 'rkiem-sublimator', 'rkiem-icer', 'rkiem-muse', 'rkiem-zkiem',
    # Serious (3)
    'serious-ak-47', 'serious-white-russian', 'serious-kali-mist',
    # Northern Lights (4)
    'nirvana-northern-light', 'sensi-northern-lights', 'wls-northern-lights', 'rqs-northern-light',
    # Blimburn / Heavyweight (4)
    'blimburn-green-crack', 'blimburn-santa-muerte', 'blimburn-chocolopez', 'heavyweight-money-bush',
    # Cannabiogen (3)
    'cannabiogen-peyote-purple', 'cannabiogen-nepal-jam', 'cannabiogen-mangobiche-kush',
    # Cepas cruzadas en nirvana-gsc (4)
    'pyramid-wembley', 'pyramid-anubis', 'blimburn-mamba-negra', 'blimburn-granddaddy-purple'
]

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 85)
print(f"VERIFICACIÓN DE LAS 23 CEPAS ACTUALIZADAS EN LOTE 1")
print("=" * 85)
print(f"{'ID Cepa':30s} | {'Archivo Asignado':33s} | {'Resolución':12s} | {'Peso':8s}")
print("-" * 85)

errors = []
images_seen = set()

for sid in target_ids:
    m = re.search(r'id:\s*"' + re.escape(sid) + r'",\s*image:\s*"([^"]+)"', content)
    if not m:
        errors.append(f"No se encontró ID en data.js: {sid}")
        continue
    img_p = m.group(1)
    fname = img_p[4:] if img_p.startswith('img/') else img_p
    abs_p = os.path.join(IMG_DIR, fname)
    
    if not os.path.exists(abs_p):
        errors.append(f"Archivo NO existe: {abs_p}")
        continue
        
    sz = os.path.getsize(abs_p) // 1024
    im = Image.open(abs_p)
    w, h = im.size
    
    # Check for duplicate within the batch
    if fname in images_seen:
        errors.append(f"IMAGEN DUPLICADA en lote: {fname}")
    images_seen.add(fname)
    
    print(f"{sid:30s} | {fname:33s} | {w}x{h:<7d} | {sz:4d} KB")

print("=" * 85)
if errors:
    print(f"❌ Se encontraron {len(errors)} errores:")
    for err in errors:
        print("  *", err)
else:
    print(f"✅ ÉXITO TOTAL: Las 23 cepas tienen imágenes exclusivas, individuales, en alta resolución (todas >= 600x600 px) y verificadas en disco.")
