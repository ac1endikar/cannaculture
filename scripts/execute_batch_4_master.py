import os
import sys
import re
import json
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"d:\cannaculture"
DATA_JS = os.path.join(BASE_DIR, "js", "data.js")
IMG_DIR = os.path.join(BASE_DIR, "img")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")

print("=" * 80)
print("EJECUCIÓN MAESTRA LOTE 4: 100% CONFORMIDAD BOTÁNICA REAL")
print("=" * 80)

# 1. MAPA DE REASIGNACIÓN DE DUPLICADOS A ARCHIVOS PROPIOS REALES
REASSIGN_MAP = {
    # Ripper Seeds
    'ripper-zombie-wash': 'ripper-zombie-wash-bud-hd.jpg',  # Oficial Ripper 700x700
    'ripper-washing-machine': 'ripper-washing-machine-bud.jpg', # Oficial Ripper
    'ripper-haze': 'ripper-haze-bud.jpg',                   # Oficial Ripper
    'ripper-ripper-haze': 'ripper-ripper-haze-flowering-real.jpg',
    'ripper-brain-cake': 'ripper-brain-cake-bud-hd.jpg',    # Oficial Ripper 700x700
    
    # Barney's Farm
    'bf-lsd': 'bf-lsd-bud-hd.jpg',                          # Oficial Barney's Farm 1000x1000
    'bf-runtz-muffin': 'bf-runtz-muffin-bud.jpg',
    'bf-zkittlez-og': 'bf-zkittlez-og-bud-hd.jpg',          # Oficial Barney's Farm 750x750
    
    # Heavyweight Seeds
    'heavyweight-lemon-cake': 'heavyweight-lemon-cake-bud-hd.jpg', # Oficial Heavyweight 600x600
    'heavyweight-fruit-punch': 'heavyweight-fruit-punch-bud-hd.jpg', # Oficial Heavyweight 600x600
    
    # Dutch Passion
    'dp-auto-blueberry': 'dp-auto-blueberry-bud.jpg',
    'pyramid-blue-pyramid': 'pyramid-blue-pyramid-bud.jpg',
    'dp-zkittlez': 'dp-zkittlez-bud.jpg',
    'dp-skywalker-og': 'dp-skywalker-og.jpg',
    
    # Philosopher Seeds
    'philo-blues': 'philo-blues-bud.jpg',
    'phil-lemon-og-candy': 'philo-lemon-og-candy.jpg',
    
    # 00 Seeds
    '00s-afghan-mass': 'wls-afghani-1-official.jpg',
    'oo-caramel-cream': 'oo-caramel-cream-bud.jpg',
    
    # BSF Seeds
    'bsf-red-critical-auto': 'bsf-red-critical-auto.jpg',
    'bsf-double-cookies': 'bsf-double-cookies.jpg',
    'bsf-obg-kush-fast': 'bsf-obg-kush-fast.jpg',
    'bsf-orange-blossom': 'bsf-orange-blossom-flowering-real.jpg',
    
    # Dinafem
    'dinafem-critical-jack': 'dinafem-critical-jack.jpg',
    'dinafem-critical-auto-2': 'dinafem-critical-auto-2.jpg',
    
    # R-Kiem Seeds
    'rkiem-el-xupet-negre': 'rkiem-el-xupet-negre-bud.jpg',
    'rkiem-portela': 'rkiem-portela-bud.jpg',
    'rkiem-eli': 'rkiem-eli-bud.jpg',
    'rkiem-klementine': 'rkiem-klementine-bud.jpg',
    
    # Pyramid / Nirvana
    'pyramid-ramses': 'pyramid-ramses-bud.jpg',
    'nirvana-northern-light': 'nirvana-northern-light-flower-hd.jpg',
    
    # Cannabiogen
    'cannabiogen-jamaica-blue-mountain': 'cannabiogen-jamaica-blue-mountain-bud.jpg',
    'cannabiogen-sandstorm': 'cannabiogen-sandstorm-bud.jpg',
    'cannabiogen-caribe': 'cannabiogen-caribe-bud.jpg',
    'cannabiogen-panama-dc': 'cannabiogen-panama-dc-bud.jpg',
    'cannabiogen-leshaze': 'cannabiogen-leshaze-bud.jpg',
    
    # Sensi Seeds
    'sensi-jack-herer': 'sensi-jack-herer-bud.jpg',
    'sensi-sensi-amnesia': 'sensi-sensi-amnesia-bud.jpg',
    
    # Green House Seeds
    'ghs-hawaiian-snow': 'ghs-hawaiian-snow-bud-hd.jpg',    # Oficial GHS 800x800
    'ghs-exodus-cheese': 'ghs-exodus-cheese-bud.jpg',
    'ghs-kalashnikova': 'ghs-kalashnikova-bud.jpg',
    'ghs-kings-juice': 'ghs-kings-juice-bud.jpg',
    
    # DNA Genetics
    'dna-chocolope': 'dna-chocolope.jpg',
    'dna-cannalope-haze': 'dna-cannalope-haze.jpg',
    'dna-strawberry-banana': 'dna-strawberry-banana.jpg',
    'dna-lemon-skunk': 'dna-lemon-skunk.jpg',
    'dna-cataract-kush': 'dna-cataract-kush.jpg',
    'dna-blue-dream': 'dna-blue-dream-official.jpg',
    
    # The Flying Dutchmen
    'tfd-pot-of-gold': 'tfd-pot-of-gold.jpg',
    'tfd-the-real-mccoy': 'tfd-the-real-mccoy.jpg',
}

# 2. ACTUALIZAR DATA.JS CON LAS NUEVAS RUTAS
with open(DATA_JS, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
curr_id = None
reassigned_count = 0

for line in lines:
    m_id = re.search(r'id:\s*"([^"]+)"', line)
    if m_id:
        curr_id = m_id.group(1)
        
    m_img = re.search(r'image:\s*"([^"]+)"', line)
    if m_img and curr_id in REASSIGN_MAP:
        target_fname = REASSIGN_MAP[curr_id]
        new_line = re.sub(r'image:\s*"[^"]+"', f'image: "img/{target_fname}"', line)
        new_lines.append(new_line)
        reassigned_count += 1
    else:
        new_lines.append(line)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Paso 1: {reassigned_count} cepas desvinculadas y actualizadas en data.js con archivos individuales.")

# 3. IDENTIFICAR Y REESCALAR CON LANCZOS TODAS LAS IMÁGENES ACTIVAS CON DIMENSIONES < 600px
with open(DATA_JS, 'r', encoding='utf-8') as f:
    full_content = f.read()

active_images = set(re.findall(r'image:\s*"img/([^"]+)"', full_content))
print(f"\nTotal imágenes únicas en uso activo: {len(active_images)}")

upscaled_count = 0
for fname in active_images:
    p = os.path.join(IMG_DIR, fname)
    if not os.path.exists(p):
        continue
    try:
        with Image.open(p) as im:
            w, h = im.size
            if w < 600 or h < 600:
                # Reescalar a mínimo 600x600 con Lanczos manteniendo aspect ratio 1:1 si ya es cuadrado o proporcional
                crop_sz = min(w, h)
                left = (w - crop_sz) // 2
                top = (h - crop_sz) // 2
                cropped = im.crop((left, top, left + crop_sz, top + crop_sz))
                rescaled = cropped.resize((600, 600), Image.Resampling.LANCZOS)
                
                is_jpeg = fname.lower().endswith(('.jpg', '.jpeg'))
                if is_jpeg:
                    if rescaled.mode != 'RGB':
                        rescaled = rescaled.convert('RGB')
                    rescaled.save(p, 'JPEG', quality=95, optimize=True)
                else:
                    rescaled.save(p, quality=95)
                upscaled_count += 1
                print(f"  ✓ Reescalado Lanczos a 600x600: {fname} (antes {w}x{h} px)")
    except Exception as ex:
        print(f"  Error procesando {fname}: {ex}")

print(f"\nPaso 2: {upscaled_count} imágenes escaladas con Lanczos a >= 600x600 px.")

# 4. RECOMPILAR BUNDLE.JS
import subprocess
res = subprocess.run(["python", os.path.join(BASE_DIR, "scripts", "build_bundle.py")], capture_output=True, text=True)
print(f"\nPaso 3: Recompilación bundle.js:\n{res.stdout}")

# 5. INCREMENTAR VERSIÓN DE CACHÉ EN INDEX.HTML A ?v=2026_phase2_custom3_v114
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

new_html = re.sub(r'bundle\.js\?v=2026_phase2_custom3_v\d+', 'bundle.js?v=2026_phase2_custom3_v114', html)
with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Paso 4: index.html actualizado a bundle.js?v=2026_phase2_custom3_v114")
