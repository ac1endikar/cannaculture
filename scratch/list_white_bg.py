import json
from PIL import Image
import os, re, sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
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

white_bg = []
for e in entries:
    fname = e['image'][4:] if e['image'].startswith('img/') else os.path.basename(e['image'].split('?')[0])
    abs_p = os.path.join(IMG_DIR, fname)
    if not os.path.exists(abs_p):
        continue
    try:
        with Image.open(abs_p) as im:
            im_rgb = im.convert('RGB')
            im_thumb = im_rgb.resize((50, 50), Image.Resampling.BILINEAR)
            pixels = [im_thumb.getpixel((x, y)) for y in range(50) for x in range(50)]
            border_pixels = [im_thumb.getpixel((x, y)) for y in range(50) for x in range(50) if y == 0 or y == 49 or x == 0 or x == 49]
            wb_count = sum(1 for (r, g, b) in border_pixels if r > 230 and g > 230 and b > 230)
            wb_pct = (wb_count / len(border_pixels)) * 100
            avg_bright = sum((r + g + b) / 3 for (r, g, b) in pixels) / len(pixels)
            if wb_pct > 40.0 or avg_bright > 215:
                white_bg.append({
                    'wb_pct': wb_pct,
                    'avg_bright': avg_bright,
                    'id': e['id'],
                    'name': e['name'],
                    'bank': e['bank'],
                    'fname': fname,
                    'size': im.size,
                    'kb': os.path.getsize(abs_p) // 1024
                })
    except Exception as ex:
        pass

print(f"Total cepas actuales con fondo blanco: {len(white_bg)}")
white_bg.sort(key=lambda x: x['wb_pct'], reverse=True)

with open(r'd:\cannaculture\scratch\white_bg_list.json', 'w', encoding='utf-8') as f:
    json.dump(white_bg, f, ensure_ascii=False, indent=2)

for i, x in enumerate(white_bg, 1):
    print(f"{i:2d}. {x['wb_pct']:5.1f}% blanco ({x['avg_bright']:5.1f} brillo) | [{x['bank']}] {x['name']} ({x['id']}) -> {x['fname']} {x['size']}")
