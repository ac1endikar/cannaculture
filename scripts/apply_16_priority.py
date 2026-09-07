import os
import re
import io
import urllib.request
from collections import deque
from PIL import Image, ImageFilter

STRAINS_CONFIG = [
    {
        "strain": "Cream Caramel / Caramel Cream",
        "id": "sweet-cream-caramel",
        "url": "https://sweetseeds.com/9665-thickbox_default/cream-caramel.jpg",
        "filename": "sweet-cream-caramel-bud-hd.jpg"
    },
    {
        "strain": "Caramel Cream (00 Seeds)",
        "id": "oo-caramel-cream",
        "url": "https://sweetseeds.com/9665-thickbox_default/cream-caramel.jpg",
        "filename": "oo-caramel-cream-bud-hd.jpg"
    },
    {
        "strain": "Guawi",
        "id": "aceseeds-guawi",
        "url": "https://www.lahuertagrowshop.com/7259-large_default/guawi-ace-seeds.jpg",
        "filename": "aceseeds-guawi-bud-hd.jpg"
    },
    {
        "strain": "Malawi",
        "id": "aceseeds-malawi",
        "url": "https://www.lahuertagrowshop.com/2339-large_default/malawi-regular-ace-seeds.jpg",
        "filename": "aceseeds-malawi-bud-hd.jpg"
    },
    {
        "strain": "Super Malawi Haze",
        "id": "aceseeds-super-malawi-haze",
        "url": "https://www.lahuertagrowshop.com/5516-large_default/super-malawi-haze-ace-seeds.jpg",
        "filename": "aceseeds-super-malawi-haze-bud-hd.jpg"
    },
    {
        "strain": "Valley Girl",
        "id": "arc-valley-girl",
        "url": "https://www.lahuertagrowshop.com/9780-large_default/valley-girl-archive-seed-bank.jpg",
        "filename": "arc-valley-girl-bud-hd.jpg"
    },
    {
        "strain": "Zkittlez OG",
        "id": "bf-zkittlez-og",
        "url": "https://www.barneysfarm.com/images/products/zkittlez-og-auto_1_211697.jpg",
        "filename": "bf-zkittlez-og-bud-hd.jpg"
    },
    {
        "strain": "Gorilla Ghost",
        "id": "bsf-gorilla-ghost",
        "url": "https://www.growbarato.net/37188-large_default/gorilla-ghost.jpg",
        "filename": "bsf-gorilla-ghost-bud-hd.jpg"
    },
    {
        "strain": "Sandstorm",
        "id": "cannabiogen-sandstorm",
        "url": "https://www.growbarato.net/27357-large_default/sandstorm.jpg",
        "filename": "cannabiogen-sandstorm-bud-hd.jpg"
    },
    {
        "strain": "Leshaze",
        "id": "cannabiogen-leshaze",
        "url": "https://www.growbarato.net/27359-large_default/leshaze.jpg",
        "filename": "cannabiogen-leshaze-bud-hd.jpg"
    },
    {
        "strain": "Cheese (Dinafem)",
        "id": "dinafem-cheese",
        "url": "https://www.growbarato.net/26307-large_default/cheese.jpg",
        "filename": "dinafem-cheese-bud-hd.jpg"
    },
    {
        "strain": "Exodus Cheese (Green House)",
        "id": "ghs-exodus-cheese",
        "url": "https://www.growbarato.net/26359-large_default/exodus-cheese.jpg",
        "filename": "ghs-exodus-cheese-bud-hd.jpg"
    },
    {
        "strain": "Passion Fruit",
        "id": "dp-passion-fruit",
        "url": "https://dutch-passion.com/2866-large_default/passion-fruit.jpg",
        "filename": "dp-passion-fruit-bud-hd.jpg"
    },
    {
        "strain": "Fruit Punch",
        "id": "heavyweight-fruit-punch",
        "url": "https://www.growbarato.net/26852-large_default/fruit-punch.jpg",
        "filename": "heavyweight-fruit-punch-bud-hd.jpg"
    },
    {
        "strain": "Terple",
        "id": "ihg-terple",
        "url": "https://cdn.prod.website-files.com/65984dad3dc673726cd63bca/669165757a5711411936d057_map4.jpg",
        "filename": "ihg-terple-bud-hd.jpg"
    },
    {
        "strain": "Northern Light (Nirvana)",
        "id": "nirvana-northern-light",
        "url": "https://herbiesheadshop.com/resized/origin/common/83/northern-light-regular-nirvana-seeds--1--buds.jpg__Lwb9YVm9OxSBGNVQ.jpg",
        "filename": "nirvana-northern-light-bud-hd.jpg"
    },
    {
        "strain": "Northern Lights (Sensi)",
        "id": "sensi-northern-lights",
        "url": "https://img.sensiseeds.com/images/thumbs/0000684_northern-lights-feminized-seeds_800.png",
        "filename": "sensi-northern-lights-bud-hd.jpg"
    },
    {
        "strain": "Gelato",
        "id": "nirvana-gelato",
        "url": "https://www.growbarato.net/32598-large_default/gelato-auto.jpg",
        "filename": "nirvana-gelato-bud-hd.jpg"
    },
    {
        "strain": "White Widow",
        "id": "ghs-white-widow",
        "url": "https://www.growbarato.net/26356-large_default/white-widow-feminizada-green-house-seeds.jpg",
        "filename": "ghs-white-widow-bud-hd.jpg"
    }
]

def process_botanical_image(img_bytes, target_size=600):
    im = Image.open(io.BytesIO(img_bytes))
    
    # 1. Alpha composite if RGBA
    if im.mode == 'RGBA':
        r, g, b, a = im.split()
        bg = Image.new('RGB', im.size, (14, 18, 24))
        im = Image.composite(Image.merge('RGB', (r, g, b)), bg, a)
    else:
        im = im.convert('RGB')
        
    w, h = im.size
    
    # 2. Check if background is light / white / isolated
    corner_colors = [im.getpixel((0,0)), im.getpixel((w-1,0)), im.getpixel((0,h-1)), im.getpixel((w-1,h-1))]
    avg_brightness = sum(sum(c) for c in corner_colors) / (4 * 3)
    is_light = any(sum(c)/3 > 140 for c in corner_colors) or avg_brightness > 120
    
    if is_light:
        pixels = im.load()
        visited = bytearray(w * h)
        queue = deque()
        
        avg_r = sum(c[0] for c in corner_colors) / 4
        avg_g = sum(c[1] for c in corner_colors) / 4
        avg_b = sum(c[2] for c in corner_colors) / 4
        
        def is_bg(x, y):
            p = pixels[x, y]
            dist = abs(p[0] - avg_r) + abs(p[1] - avg_g) + abs(p[2] - avg_b)
            return (p[0] > 160 and p[1] > 160 and p[2] > 160) or (dist < 55 and sum(p)/3 > 95)
            
        for x in range(w):
            if is_bg(x, 0):
                queue.append((x, 0))
                visited[0 * w + x] = 1
            if is_bg(x, h - 1):
                queue.append((x, h - 1))
                visited[(h - 1) * w + x] = 1
        for y in range(h):
            if is_bg(0, y):
                queue.append((0, y))
                visited[y * w + 0] = 1
            if is_bg(w - 1, y):
                queue.append((w - 1, y))
                visited[y * w + (w - 1)] = 1
                
        while queue:
            cx, cy = queue.popleft()
            for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
                if 0 <= nx < w and 0 <= ny < h:
                    idx = ny * w + nx
                    if not visited[idx] and is_bg(nx, ny):
                        visited[idx] = 1
                        queue.append((nx, ny))
                        
        mask = Image.new('L', (w, h), 0)
        mask_data = bytearray(w * h)
        for i in range(w * h):
            if visited[i]:
                mask_data[i] = 255
        mask.frombytes(bytes(mask_data))
        mask = mask.filter(ImageFilter.GaussianBlur(1.5))
        
        dark_bg = Image.new('RGB', (w, h), (14, 18, 24))
        im = Image.composite(dark_bg, im, mask)
        
    # 3. Square Crop (Center 1:1)
    w, h = im.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    im_square = im.crop((left, top, left + min_dim, top + min_dim))
    
    # 4. Dimension Normalization
    if min_dim < target_size:
        im_square = im_square.resize((target_size, target_size), Image.Resampling.LANCZOS)
    elif min_dim > 1200:
        im_square = im_square.resize((1000, 1000), Image.Resampling.LANCZOS)
        
    return im_square

def run():
    print("=== INICIANDO DESCARGA Y PROCESAMIENTO BOTÁNICO REAL ===")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    results = []
    
    for item in STRAINS_CONFIG:
        tid = item["id"]
        url = item["url"]
        fname = item["filename"]
        target_path = os.path.join("img", fname)
        
        print(f"\nProcesando [{tid}]...")
        print(f"  URL: {url}")
        
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw_bytes = resp.read()
                print(f"  Descargados: {len(raw_bytes)} bytes")
                
                processed_img = process_botanical_image(raw_bytes, 600)
                processed_img.save(target_path, "JPEG", quality=95, optimize=True)
                
                final_size = processed_img.size
                corner_px = processed_img.getpixel((0,0))
                print(f"  Guardado: {target_path} ({final_size[0]}x{final_size[1]} px), Corner: {corner_px}")
                
                results.append({
                    "strain": item["strain"],
                    "id": tid,
                    "file": f"img/{fname}",
                    "resolution": f"{final_size[0]}x{final_size[1]} px",
                    "url": url
                })
        except Exception as e:
            print(f"  ERROR descargando/procesando {tid}: {e}")
            raise e
            
    print("\n=== ACTUALIZANDO JS/DATA.JS ===")
    with open("js/data.js", "r", encoding="utf-8") as f:
        data_content = f.read()
        
    for res in results:
        tid = res["id"]
        new_img = res["file"]
        # Pattern to replace image property inside the strain object
        pattern = re.compile(rf'(id:\s*["\']{re.escape(tid)}["\'].*?image:\s*["\'])([^"\']+)(["\'])', re.DOTALL)
        if pattern.search(data_content):
            data_content = pattern.sub(rf'\g<1>{new_img}\g<3>', data_content, count=1)
            print(f"  Actualizado en data.js: {tid} -> {new_img}")
        else:
            print(f"  ADVERTENCIA: No se encontró {tid} en data.js")
            
    with open("js/data.js", "w", encoding="utf-8") as f:
        f.write(data_content)
        
    print("\n=== TABLA DE RESULTADOS ===")
    print(f"{'Cepa':<30} | {'ID':<28} | {'Archivo guardado':<35} | {'Resolución':<12} | URL real")
    print("-" * 140)
    for r in results:
        print(f"{r['strain']:<30} | {r['id']:<28} | {r['file']:<35} | {r['resolution']:<12} | {r['url']}")
        
if __name__ == "__main__":
    run()
