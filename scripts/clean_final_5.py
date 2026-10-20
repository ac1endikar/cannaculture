import os
import sys
from PIL import Image, ImageDraw

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"d:\cannaculture"
IMG_DIR = os.path.join(BASE_DIR, "img")

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

def clean_to_dark(fname, thresh=90):
    p = os.path.join(IMG_DIR, fname)
    if not os.path.exists(p):
        print(f"No existe: {p}")
        return
    im = Image.open(p).convert('RGB')
    w, h = im.size
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im = im.crop((left, top, left + crop_sz, top + crop_sz))
    if crop_sz < 600:
        im = im.resize((600, 600), Image.Resampling.LANCZOS)
    
    orig_w, orig_h = im.size
    fw = 600
    work_im = im.resize((fw, fw), Image.Resampling.BILINEAR)
    
    # Rellenar desde las 4 esquinas
    pad = Image.new('RGB', (fw + 2, fw + 2), (255, 255, 255))
    pad.paste(work_im, (1, 1))
    
    for corner in [(0, 0), (fw + 1, 0), (0, fw + 1), (fw + 1, fw + 1)]:
        ImageDraw.floodfill(pad, corner, (254, 254, 254), thresh=thresh)
        
    mask = Image.new('L', (orig_w, orig_h), 255)
    m_draw = ImageDraw.Draw(mask)
    
    scale_x = orig_w / fw
    scale_y = orig_h / fw
    
    for py in range(fw):
        for px in range(fw):
            pr, pg, pb = pad.getpixel((px + 1, py + 1))
            if pr == 254 and pg == 254 and pb == 254:
                rx = int(px * scale_x)
                ry = int(py * scale_y)
                rx2 = int((px + 1) * scale_x)
                ry2 = int((py + 1) * scale_y)
                m_draw.rectangle([rx, ry, rx2, ry2], fill=0)
                
    backdrop = create_studio_dark_backdrop(orig_w, orig_h)
    composed = Image.composite(im, backdrop, mask)
    composed.save(p, 'JPEG', quality=95, optimize=True)
    print(f"Limpiado {fname} a {composed.size} px")

target_5 = [
    'ripper-washing-machine-bud.jpg',
    'cannabiogen-leshaze-bud.jpg',
    'dp-skywalker-og.jpg',
    'wls-afghani-1-cand1.jpg',
    'tfd-the-real-mccoy.jpg'
]

for f in target_5:
    clean_to_dark(f, thresh=90)
