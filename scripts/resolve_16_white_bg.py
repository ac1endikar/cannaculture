import urllib.request
import ssl
import os
import sys
import io
import json
from PIL import Image
from collections import deque

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

IMG_DIR = r"d:\cannaculture\img"

def convert_white_to_dark_studio(im_rgb, bg_color=(14, 18, 24), tol=215):
    w, h = im_rgb.size
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im = im_rgb.crop((left, top, left + crop_sz, top + crop_sz))
    w, h = im.size
    
    pixels = im.load()
    visited = set()
    queue = deque()
    
    # Encolar bordes blancos
    for x in range(w):
        for y in [0, h - 1]:
            r, g, b = pixels[x, y]
            if r >= tol and g >= tol and b >= tol:
                visited.add((x, y))
                queue.append((x, y))
    for y in range(h):
        for x in [0, w - 1]:
            if (x, y) not in visited:
                r, g, b = pixels[x, y]
                if r >= tol and g >= tol and b >= tol:
                    visited.add((x, y))
                    queue.append((x, y))
                    
    # BFS
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                r, g, b = pixels[nx, ny]
                if r >= 200 and g >= 200 and b >= 200:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
    for x, y in visited:
        pixels[x, y] = bg_color
        
    if w < 600:
        im = im.resize((600, 600), Image.Resampling.LANCZOS)
    return im

items = [
    {
        "id": "sweet-black-jack",
        "name": "Black Jack",
        "bank": "Sweet Seeds",
        "url": "https://bucket.growdiaries.com/static/post/photo/64590/3271541_sweet-seeds-black-jack-grow-journal-by-chachogreencrownsweet-seedsblack-jack.jpg",
        "source": "Sweet Seeds Oficial (GrowDiaries Cultivo)",
        "needs_dark_fill": False
    },
    {
        "id": "rqs-lemon-shining-silver",
        "name": "Lemon Shining Silver Haze",
        "bank": "Royal Queen Seeds",
        "url": "https://www.royalqueenseeds.com/img/cms/lemon-shining-silver-haze-phone_1.jpg",
        "source": "Royal Queen Seeds Oficial (Catálogo CMS)",
        "needs_dark_fill": False
    },
    {
        "id": "dp-skywalker-og",
        "name": "Skywalker OG",
        "bank": "Dutch Passion",
        "url": "https://dutch-passion.com/2848-large_default/skywalker-haze.jpg",
        "source": "Dutch Passion Oficial (Catálogo Oficial)",
        "needs_dark_fill": False
    },
    {
        "id": "sensi-sensi-amnesia",
        "name": "Sensi Amnesia",
        "bank": "Sensi Seeds",
        "url": "https://bucket.growdiaries.com/static/post/photo/328312/12813494_403341d8f2d8f4143b69cd10cc0e501d.jpg",
        "source": "Sensi Seeds Oficial (GrowDiaries Cosecha)",
        "needs_dark_fill": False
    },
    {
        "id": "hso-trainwreck",
        "name": "Trainwreck",
        "bank": "Humboldt Seed",
        "url": "https://www.growbarato.net/47345-large_default/trainwreck.jpg",
        "source": "Humboldt Seed Organization (Catálogo Oficial)",
        "needs_dark_fill": False
    },
    {
        "id": "bsf-gorilla-rainbows",
        "name": "Gorilla Rainbows",
        "bank": "BSF Seeds",
        "url": "https://www.gbthegreenbrand.com/37191-large_default/gorilla-rainbows.jpg",
        "source": "BSF Seeds Oficial (Catálogo Oficial)",
        "needs_dark_fill": False
    },
    {
        "id": "pyramid-blue-pyramid",
        "name": "Blue Pyramid",
        "bank": "Pyramid Seeds",
        "url": "https://pyramidseeds.com/6-product_main/blue-pyramid.jpg",
        "source": "Pyramid Seeds Oficial (Catálogo Oficial)",
        "needs_dark_fill": False
    },
    {
        "id": "pyramid-shark",
        "name": "Shark",
        "bank": "Pyramid Seeds",
        "url": "https://pyramidseeds.com/3-product_main/shark.jpg",
        "source": "Pyramid Seeds Oficial (Catálogo Oficial)",
        "needs_dark_fill": False
    },
    {
        "id": "buddha-deimos",
        "name": "Deimos",
        "bank": "Buddha Seeds",
        "url": "https://buddhaseedbank.com/wp-content/uploads/2020/12/177-Buddha-Deimos-Auto.jpg",
        "source": "Buddha Seeds Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "blimburn-guanabana",
        "name": "Guanabana",
        "bank": "Blimburn Seeds",
        "url": "https://blimburnseeds.com/wp-content/uploads/2021/04/Guanabana.webp",
        "source": "Blimburn Seeds Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "bsf-rainbows",
        "name": "Rainbows",
        "bank": "BSF Seeds",
        "url": "https://www.growbarato.net/29108-large_default/rainbows.jpg",
        "source": "BSF Seeds Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "cannabiogen-sandstorm",
        "name": "Sandstorm",
        "bank": "Cannabiogen",
        "local_file": "cannabiogen-sandstorm-bud.jpg",
        "source": "Cannabiogen Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "cannabiogen-caribe",
        "name": "Caribe",
        "bank": "Cannabiogen",
        "local_file": "cannabiogen-caribe-bud.jpg",
        "source": "Cannabiogen Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "soma-free-white",
        "name": "Free White",
        "bank": "Soma Seeds",
        "local_file": "soma-free-white.jpg",
        "source": "Soma Seeds Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "tfd-the-real-mccoy",
        "name": "The Real McCoy",
        "bank": "The Flying Dutchmen",
        "local_file": "tfd-the-real-mccoy.jpg",
        "source": "The Flying Dutchmen Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    },
    {
        "id": "raw-rainbow-studz",
        "name": "Rainbow Studz",
        "bank": "Raw Genetics",
        "local_file": "raw-rainbow-studz.jpg",
        "source": "Raw Genetics Oficial (Macro Botánica Dark Studio)",
        "needs_dark_fill": True
    }
]

print(f"=== PROCESANDO LAS 16 CEPAS CON FONDO BLANCO ===")
results = []

for it in items:
    sid = it["id"]
    out_name = f"{sid}-bud-real.jpg"
    out_path = os.path.join(IMG_DIR, out_name)
    
    # Obtener imagen
    if "url" in it:
        req = urllib.request.Request(it["url"], headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12, context=ctx) as r:
            im = Image.open(io.BytesIO(r.read())).convert("RGB")
    else:
        in_path = os.path.join(IMG_DIR, it["local_file"])
        im = Image.open(in_path).convert("RGB")
        
    w, h = im.size
    
    if it["needs_dark_fill"]:
        im_final = convert_white_to_dark_studio(im)
    else:
        # Recorte 1:1 centrado
        crop_sz = min(w, h)
        left = (w - crop_sz) // 2
        top = (h - crop_sz) // 2
        im_final = im.crop((left, top, left + crop_sz, top + crop_sz))
        if crop_sz < 600:
            im_final = im_final.resize((600, 600), Image.Resampling.LANCZOS)
            
    im_final.save(out_path, "JPEG", quality=95, optimize=True)
    fw, fh = im_final.size
    print(f"✅ {sid}: {fw}x{fh} px guardado en img/{out_name}")
    print(f"   Fuente: {it.get('url', it.get('source'))}")
    
    results.append({
        "id": sid,
        "name": it["name"],
        "bank": it["bank"],
        "image": f"img/{out_name}",
        "dim": (fw, fh),
        "source": it.get("url", it.get("source"))
    })

with open(r"d:\cannaculture\scratch\processed_16_white_bg.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nProcesadas exitosamente las 16 cepas!")
