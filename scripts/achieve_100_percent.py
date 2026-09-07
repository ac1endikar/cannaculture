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

# 1. Limpiar cannabiogen-leshaze-bud.jpg
p_leshaze = os.path.join(IMG_DIR, 'cannabiogen-leshaze-bud.jpg')
im = Image.open(p_leshaze).convert('RGB')
w, h = im.size

# Crear backdrop oscuro
base = Image.new('RGB', (w, h), (7, 10, 9))
glow = Image.new('L', (100, 100), 0)
g_draw = ImageDraw.Draw(glow)
for r in range(45, 0, -2):
    intensity = int(75 * (1.0 - (r / 45.0)))
    g_draw.ellipse([50 - r, 50 - r, 50 + r, 50 + r], fill=intensity)
glow_resized = glow.resize((w, h), Image.Resampling.BICUBIC)
center_glow = Image.new('RGB', (w, h), (22, 32, 27))
backdrop = Image.composite(center_glow, base, glow_resized)

# Mascara por floodfill directo en escala 1:1
pad = Image.new('RGB', (w + 2, h + 2), (255, 255, 255))
pad.paste(im, (1, 1))

# Inundar con color (1, 2, 3) desde los 4 bordes
for corner in [(0, 0), (w + 1, 0), (0, h + 1), (w + 1, h + 1)]:
    ImageDraw.floodfill(pad, corner, (1, 2, 3), thresh=100)

mask = Image.new('L', (w, h), 255)
for y in range(h):
    for x in range(w):
        if pad.getpixel((x + 1, y + 1)) == (1, 2, 3):
            mask.putpixel((x, y), 0)

final_leshaze = Image.composite(im, backdrop, mask)
final_leshaze.save(p_leshaze, 'JPEG', quality=95, optimize=True)
print("cannabiogen-leshaze-bud.jpg procesado.")

# 2. Actualizar data.js para ripper-washing-machine y 00s-afghan-mass
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

# ripper-washing-machine -> ripper-washing-machine.jpg
content = re.sub(
    r'(id:\s*"ripper-washing-machine"[\s\S]*?image:\s*")[^"]+(")',
    r'\g<1>img/ripper-washing-machine.jpg\g<2>',
    content
)

# 00s-afghan-mass -> wls-afghani-1-cand0.jpg
content = re.sub(
    r'(id:\s*"00s-afghan-mass"[\s\S]*?image:\s*")[^"]+(")',
    r'\g<1>img/wls-afghani-1-cand0.jpg\g<2>',
    content
)

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(content)

print("data.js actualizado para ripper-washing-machine y 00s-afghan-mass.")

# 3. Recompilar bundle.js
import subprocess
res = subprocess.run(["python", os.path.join(BASE_DIR, "scripts", "build_bundle.py")], capture_output=True, text=True)
print("bundle.js recompilado:", res.stdout.strip())
