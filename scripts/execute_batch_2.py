#!/usr/bin/env python3
"""
Corrección de Auditoría - Lote 2: Fondos Blancos y Packshots a Macro Oscuro
Erradica los fondos blancos planos y los sustituye por macro botánica en fondo oscuro de estudio.
"""
import os
import sys
import re
import json
from PIL import Image, ImageDraw, ImageFilter, ImageOps

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'
INDEX_HTML = r'd:\cannaculture\index.html'

def create_studio_backdrop(width, height):
    """Fondo de estudio fotográfico oscuro con sutil resplandor central esmeralda."""
    base = Image.new('RGB', (width, height), (7, 10, 9))
    glow = Image.new('L', (100, 100), 0)
    g_draw = ImageDraw.Draw(glow)
    for r in range(48, 0, -1):
        intensity = int(255 * (1.0 - (r / 48) ** 1.6))
        g_draw.ellipse([50 - r, 50 - r, 50 + r, 50 + r], fill=intensity)
    glow_resized = glow.resize((width, height), Image.Resampling.BICUBIC)
    center_glow = Image.new('RGB', (width, height), (22, 32, 27))
    backdrop = Image.composite(center_glow, base, glow_resized)
    return backdrop

def studio_dark_transform(input_path, output_path, min_dim=600):
    """
    Aísla la flor/cogollo del fondo blanco plano mediante flood-fill desde bordes
    y la compone sobre un fondo oscuro de estudio, garantizando dimensiones >= 600px.
    """
    im = Image.open(input_path).convert('RGB')
    w, h = im.size
    
    # Escalar si es menor a min_dim en ambas dimensiones
    if w < min_dim or h < min_dim:
        scale = max(min_dim / w, min_dim / h)
        w, h = int(w * scale), int(h * scale)
        im = im.resize((w, h), Image.Resampling.LANCZOS)
        
    orig_w, orig_h = w, h
    fw_scale = 1.0
    if w > 1200 or h > 1200:
        fw_scale = 1200 / max(w, h)
        work_im = im.resize((int(w * fw_scale), int(h * fw_scale)), Image.Resampling.BILINEAR)
    else:
        work_im = im
        
    ww, wh = work_im.size
    
    # Detectar píxeles blancos en bordes
    rgb_pix = work_im.load()
    white_mask = Image.new('L', (ww, wh), 0)
    w_draw = white_mask.load()
    
    for y in range(wh):
        for x in range(ww):
            r, g, b = rgb_pix[x, y]
            if r > 215 and g > 215 and b > 215:
                w_draw[x, y] = 255
                
    # Flood-fill conexo desde los bordes para no tocar tricomas interiores
    padded = Image.new('L', (ww + 2, wh + 2), 255)
    padded.paste(white_mask, (1, 1))
    ImageDraw.floodfill(padded, (0, 0), 128)
    
    cropped = padded.crop((1, 1, ww + 1, wh + 1))
    bg_mask = cropped.point(lambda p: 255 if p == 128 else 0)
    
    if fw_scale != 1.0:
        bg_mask = bg_mask.resize((orig_w, orig_h), Image.Resampling.BILINEAR)
        
    blurred_bg = bg_mask.filter(ImageFilter.GaussianBlur(radius=2.0))
    fg_mask = ImageOps.invert(blurred_bg)
    
    backdrop = create_studio_backdrop(orig_w, orig_h)
    result = Image.composite(im, backdrop, fg_mask)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    result.save(output_path, 'JPEG', quality=95)
    
    # Comprobar bordes blancos finales
    thumb = result.resize((50, 50))
    border_pixels = [thumb.getpixel((x, y)) for y in range(50) for x in range(50) if y == 0 or y == 49 or x == 0 or x == 49]
    wb_count = sum(1 for (r, g, b) in border_pixels if r > 200 and g > 200 and b > 200)
    wb_pct = (wb_count / len(border_pixels)) * 100
    return orig_w, orig_h, wb_pct

# 1. Cargar lista de cepas con fondo blanco
with open(r'd:\cannaculture\scratch\white_bg_list.json', 'r', encoding='utf-8') as f:
    white_bg_items = json.load(f)

print("=" * 80)
print(f"PASO 1: TRANSFORMACIÓN A FONDO ESTUDIO OSCURO ({len(white_bg_items)} CEPAS)")
print("=" * 80)

# Mapeo de reemplazos prioritarios si hay archivo específico previo en img/
DEDICATED_INPUTS = {
    'bf-lsd': 'bf-lsd.jpg',
    '00s-cheese-xl': '00s-cheese-xl.jpg',
    'dna-gmo-kosher': 'dna-gmo-kosher.jpg',
    'dna-sleestack': 'dna-sleestack.jpg',
    'dna-sour-tangie': 'dna-sour-tangie.jpg',
    'heavyweight-lemon-cake': 'heavyweight-lemon-cake-bud.jpg',
    'bsf-el-gaucho-fast': 'bsf-el-gaucho-fast.jpg',
    'blimburn-gorilla-glue-4': 'blimburn-gorilla-glue-4-bud.jpg',
    'blimburn-bcn-diesel': 'blimburn-bcn-diesel-bud.jpg',
    'heavyweight-fruit-punch': 'heavyweight-fruit-punch-bud.jpg',
    'heavyweight-strawberry-cake': 'heavyweight-strawberry-cake-bud.jpg',
    'positronics-purple-haze': 'positronics-purple-haze-bud.jpg',
    'positronics-claustrum': 'positronics-claustrum-flowering-real.jpg',
    'raw-peeled-banana': 'raw-peeled-banana.jpg',
    'soma-somango': 'soma-somango.jpg',
}

strain_updates = {}
processed_count = 0

for item in white_bg_items:
    sid = item['id']
    name = item['name']
    bank = item['bank']
    cur_fname = item['fname']
    
    # Seleccionar mejor entrada
    inp_fname = DEDICATED_INPUTS.get(sid, cur_fname)
    inp_path = os.path.join(IMG_DIR, inp_fname)
    if not os.path.exists(inp_path):
        inp_path = os.path.join(IMG_DIR, cur_fname)
        
    out_fname = f"{sid}-bud-hd.jpg"
    out_path = os.path.join(IMG_DIR, out_fname)
    
    try:
        w, h, wb_pct = studio_dark_transform(inp_path, out_path, min_dim=600)
        sz_kb = os.path.getsize(out_path) // 1024
        print(f"  [{processed_count+1:2d}/{len(white_bg_items)}] {sid}: {w}x{h} px ({sz_kb}KB, {wb_pct:.1f}% blanco) -> {out_fname}")
        strain_updates[sid] = f"img/{out_fname}"
        processed_count += 1
    except Exception as ex:
        print(f"  [ERROR] {sid} ({inp_path}): {ex}")

print(f"\nTotal imágenes procesadas con éxito: {processed_count} / {len(white_bg_items)}")

# 2. Actualizar js/data.js
print("\n" + "=" * 80)
print(f"PASO 2: ACTUALIZACIÓN DE DATA.JS ({len(strain_updates)} CEPAS)")
print("=" * 80)

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
    if m_img and current_strain_id in strain_updates:
        new_img = strain_updates[current_strain_id]
        old_img = m_img.group(1)
        line = re.sub(r'image:\s*"[^"]+"', f'image: "{new_img}"', line)
        updated_count += 1
        current_strain_id = None
        
    updated_lines.append(line)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)

print(f"Total registros actualizados en data.js: {updated_count}")

# 3. Recompilar bundle.js
print("\n" + "=" * 80)
print("PASO 3: RECOMPILACIÓN DE BUNDLE.JS")
print("=" * 80)
os.system(f'python "{os.path.join(os.path.dirname(__file__), "build_bundle.py")}"')

# 4. Actualizar versión de caché en index.html
print("\n" + "=" * 80)
print("PASO 4: ACTUALIZACIÓN DE CACHÉ EN INDEX.HTML A ?v=2026_phase2_custom3_v112")
print("=" * 80)
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

NEW_VERSION = "2026_phase2_custom3_v112"
html_updated = re.sub(r'bundle\.js\?v=[^"]+', f'bundle.js?v={NEW_VERSION}', html)

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(html_updated)

print(f"index.html actualizado a bundle.js?v={NEW_VERSION}")
