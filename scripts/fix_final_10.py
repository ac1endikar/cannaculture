import os
import sys
import re
from PIL import Image, ImageDraw

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"d:\cannaculture"
IMG_DIR = os.path.join(BASE_DIR, "img")
DATA_JS = os.path.join(BASE_DIR, "js", "data.js")

def create_studio_dark_backdrop(width, height):
    base = Image.new('RGB', (width, height), (7, 10, 9))
    glow = Image.new('L', (100, 100), 0)
    g_draw = ImageDraw.Draw(glow)
    for r in range(45, 0, -2):
        intensity = int(75 * (1.0 - (r / 45.0)))
        g_draw.ellipse([50 - r, 50 - r, 50 + r, 50 + r], fill=intensity)
    glow_resized = glow.resize((width, height), Image.Resampling.BICUBIC)
    center_glow = Image.new('RGB', (width, height), (22, 32, 27))
    backdrop = Image.composite(center_glow, base, glow_resized)
    return backdrop

def studio_dark_transform(file_path):
    im = Image.open(file_path).convert('RGB')
    w, h = im.size
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im = im.crop((left, top, left + crop_sz, top + crop_sz))
    if crop_sz < 600:
        im = im.resize((600, 600), Image.Resampling.LANCZOS)
    
    orig_w, orig_h = im.size
    
    # Redimensionar temporalmente para flood fill rápido
    fw = 600
    work_im = im.resize((fw, fw), Image.Resampling.BILINEAR)
    
    pad_im = Image.new('RGB', (fw + 2, fw + 2), (255, 255, 255))
    pad_im.paste(work_im, (1, 1))
    
    ImageDraw.floodfill(pad_im, (0, 0), (254, 254, 254), thresh=65)
    
    mask = Image.new('L', (orig_w, orig_h), 255)
    m_draw = ImageDraw.Draw(mask)
    
    scale_x = orig_w / fw
    scale_y = orig_h / fw
    
    # Recorrer píxeles floodfilled
    for py in range(fw):
        for px in range(fw):
            pr, pg, pb = pad_im.getpixel((px + 1, py + 1))
            if pr == 254 and pg == 254 and pb == 254:
                rx = int(px * scale_x)
                ry = int(py * scale_y)
                rx2 = int((px + 1) * scale_x)
                ry2 = int((py + 1) * scale_y)
                m_draw.rectangle([rx, ry, rx2, ry2], fill=0)
                
    backdrop = create_studio_dark_backdrop(orig_w, orig_h)
    composed = Image.composite(im, backdrop, mask)
    composed.save(file_path, 'JPEG', quality=95, optimize=True)
    print(f"  ✓ Fondo oscuro aplicado a {os.path.basename(file_path)}: {composed.size} px")

# 1. Aplicar fondo oscuro a las 8 imágenes con fondo blanco
white_bg_files = [
    'ripper-washing-machine-bud.jpg',
    'pyramid-blue-pyramid-bud.jpg',
    'cannabiogen-sandstorm-bud.jpg',
    'cannabiogen-leshaze-bud.jpg',
    'sensi-sensi-amnesia-bud.jpg',
    'dp-skywalker-og.jpg',
    'dna-lemon-skunk.jpg',
    'tfd-the-real-mccoy.jpg'
]

print("Paso 1: Aplicando fondo oscuro de estudio a imágenes botánicas...")
for f in white_bg_files:
    p = os.path.join(IMG_DIR, f)
    if os.path.exists(p):
        studio_dark_transform(p)

# 2. Desvincular 00s-afghan-mass en data.js asignándole wls-afghani-1-cand1.jpg (escalada a 600x600 si es necesario)
cand_path = os.path.join(IMG_DIR, 'wls-afghani-1-cand1.jpg')
if os.path.exists(cand_path):
    with Image.open(cand_path) as im:
        if im.size[0] < 600 or im.size[1] < 600:
            im_crop = im.resize((600, 600), Image.Resampling.LANCZOS)
            im_crop.save(cand_path, 'JPEG', quality=95)

with open(DATA_JS, 'r', encoding='utf-8') as f:
    text = f.read()

# Actualizar en data.js para 00s-afghan-mass
# Buscar bloque de 00s-afghan-mass
pattern = r'(id:\s*"00s-afghan-mass"[\s\S]*?image:\s*")img/[^"]+(")'
text = re.sub(pattern, r'\g<1>img/wls-afghani-1-cand1.jpg\g<2>', text)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(text)

print("Paso 2: 00s-afghan-mass asignada a wls-afghani-1-cand1.jpg (desvinculada de Afghani #1).")

# 3. Recompilar bundle.js
import subprocess
res = subprocess.run(["python", os.path.join(BASE_DIR, "scripts", "build_bundle.py")], capture_output=True, text=True)
print(f"Paso 3: bundle.js recompilado ({res.stdout.strip()})")
