#!/usr/bin/env python3
"""
Auditoría visual de catálogo y detección de imágenes no conformes:
- Resolución < 600x600 px
- Fondos blancos planos (border/edge whiteness)
- Logos, gráficos, packaging o imágenes no botánicas
- Ratios de aspecto anómalos (banners/tiras)
- Imágenes duplicadas entre distintas genéticas
"""
import os
import re
import sys
import json
from collections import defaultdict
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

entries = []
current = {}
for line in content.split('\n'):
    ls = line.strip()
    m = re.match(r'id:\s*"([^"]+)"', ls)
    if m: current['id'] = m.group(1)
    m = re.match(r'name:\s*"([^"]+)"', ls)
    if m: current['name'] = m.group(1)
    m = re.match(r'bank:\s*"([^"]+)"', ls)
    if m: current['bank'] = m.group(1)
    m = re.match(r'image:\s*"([^"]+)"', ls)
    if m: current['image'] = m.group(1)
    if ls in ('},', '}') and 'image' in current and 'name' in current:
        entries.append(dict(current))
        current = {}

print(f"Auditoría de {len(entries)} genéticas en data.js...\n")

# Track duplicate usage
image_to_strains = defaultdict(list)
for e in entries:
    fname = e['image'][4:] if e['image'].startswith('img/') else os.path.basename(e['image'].split('?')[0])
    image_to_strains[fname].append(e)

# Categorías de reporte
missing_files = []
non_cannabis_or_dupes = []
white_backgrounds = []
low_resolutions = []
ratio_skewed = []

all_flagged = {}

for e in entries:
    img_p = e['image']
    fname = img_p[4:] if img_p.startswith('img/') else os.path.basename(img_p.split('?')[0])
    abs_p = os.path.join(IMG_DIR, fname)
    
    strain_issues = []
    
    if not os.path.exists(abs_p):
        strain_issues.append("ARCHIVO_NO_EXISTE")
        missing_files.append((e, fname, "Archivo no existe en disco"))
        all_flagged[e['id']] = {'entry': e, 'issues': strain_issues, 'meta': {'fname': fname}}
        continue
        
    try:
        with Image.open(abs_p) as im:
            w, h = im.size
            ratio = w / h
            
            # Convert to RGB for pixel inspection
            im_rgb = im.convert('RGB')
            sample_size = 50
            im_thumb = im_rgb.resize((sample_size, sample_size), Image.Resampling.BILINEAR)
            pixels = [im_thumb.getpixel((x, y)) for y in range(sample_size) for x in range(sample_size)]
            
            # Border pixels
            border_pixels = []
            for y in range(sample_size):
                for x in range(sample_size):
                    if y == 0 or y == sample_size - 1 or x == 0 or x == sample_size - 1:
                        border_pixels.append(im_thumb.getpixel((x, y)))
                        
            white_border_count = sum(1 for (r, g, b) in border_pixels if r > 230 and g > 230 and b > 230)
            white_border_pct = (white_border_count / len(border_pixels)) * 100
            avg_brightness = sum((r + g + b) / 3 for (r, g, b) in pixels) / len(pixels)
            
            # Check duplicate usage (placeholder reuse)
            shared_with = [s for s in image_to_strains[fname] if s['id'] != e['id']]
            if shared_with:
                desc = f"Imagen compartida con {len(shared_with)} cepas más (ej: {', '.join([s['name'] for s in shared_with[:2]])})"
                strain_issues.append(f"DUPLICADO: {desc}")
                non_cannabis_or_dupes.append((e, fname, desc))
                
            # Suspicious names
            suspicious_words = ['logo', 'package', 'packshot', 'box', 'icon', 'vector', 'placeholder', 'blank', 'banner']
            clean_fname = fname.lower().replace('bruce-banner', '')
            found_words = [sw for sw in suspicious_words if sw in clean_fname]
            if found_words:
                desc = f"Nombre sospechoso ({', '.join(found_words)})"
                strain_issues.append(f"NOMBRE_NO_BOTANICO: {desc}")
                non_cannabis_or_dupes.append((e, fname, desc))
                
            # White background
            if white_border_pct > 40.0 or avg_brightness > 215:
                desc = f"{white_border_pct:.1f}% borde blanco (brillo medio {avg_brightness:.1f}/255)"
                strain_issues.append(f"FONDO_BLANCO: {desc}")
                white_backgrounds.append((e, fname, desc))
                
            # Low resolution (< 600x600 px)
            if w < 600 or h < 600:
                desc = f"{w}x{h} px (mínimo requerido: 600x600 px)"
                strain_issues.append(f"RESOLUCION_BAJA: {desc}")
                low_resolutions.append((e, fname, desc))
                
            # Ratio anómalo
            if ratio < 0.60 or ratio > 1.70:
                desc = f"Ratio {ratio:.2f} ({w}x{h} px - formato tira/banner)"
                strain_issues.append(f"RATIO_ANOMALO: {desc}")
                ratio_skewed.append((e, fname, desc))
                
            meta = {
                'dimensions': f"{w}x{h}",
                'ratio': f"{ratio:.2f}",
                'white_border_pct': f"{white_border_pct:.1f}%",
                'avg_brightness': f"{avg_brightness:.1f}",
                'filesize_kb': os.path.getsize(abs_p) // 1024,
                'fname': fname
            }
            
            if strain_issues:
                all_flagged[e['id']] = {'entry': e, 'issues': strain_issues, 'meta': meta}
                
    except Exception as ex:
        strain_issues.append(f"ERROR_LECTURA: {ex}")
        missing_files.append((e, fname, f"Error lectura: {ex}"))
        all_flagged[e['id']] = {'entry': e, 'issues': strain_issues, 'meta': {'fname': fname}}

# Print Summary
print("=" * 80)
print(f"RESUMEN EJECUTIVO - AUDITORÍA VISUAL")
print("=" * 80)
print(f"Total genéticas analizadas: {len(entries)}")
print(f"Genéticas 100% conformes:   {len(entries) - len(all_flagged)}")
print(f"Genéticas con no-conformidad: {len(all_flagged)}")
print("-" * 80)
print(f"1. Archivos inexistentes o corruptos:        {len(missing_files)}")
print(f"2. Imágenes no botánicas / duplicadas/logos: {len(non_cannabis_or_dupes)}")
print(f"3. Fondos blancos planos (incompatibles UI): {len(white_backgrounds)}")
print(f"4. Resolución baja (< 600x600 px):           {len(low_resolutions)}")
print(f"5. Ratios anómalos (banners/tiras):          {len(ratio_skewed)}")
print("=" * 80)

# Save structured report
report_data = {
    'total_strains': len(entries),
    'total_flagged': len(all_flagged),
    'missing_files': [{'id': e['id'], 'name': e['name'], 'bank': e['bank'], 'file': f, 'detail': d} for e, f, d in missing_files],
    'non_cannabis_or_dupes': [{'id': e['id'], 'name': e['name'], 'bank': e['bank'], 'file': f, 'detail': d} for e, f, d in non_cannabis_or_dupes],
    'white_backgrounds': [{'id': e['id'], 'name': e['name'], 'bank': e['bank'], 'file': f, 'detail': d} for e, f, d in white_backgrounds],
    'low_resolutions': [{'id': e['id'], 'name': e['name'], 'bank': e['bank'], 'file': f, 'detail': d} for e, f, d in low_resolutions],
    'ratio_skewed': [{'id': e['id'], 'name': e['name'], 'bank': e['bank'], 'file': f, 'detail': d} for e, f, d in ratio_skewed],
    'flagged_strains': all_flagged
}

with open(r'd:\cannaculture\scratch\visual_audit_report.json', 'w', encoding='utf-8') as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print("\nReporte JSON detallado guardado en scratch/visual_audit_report.json")
