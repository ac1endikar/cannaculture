import urllib.request
from PIL import Image
import io
import ssl
import os
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

STRAINS_DATA = [
    {
        "id": "oo-caramel-cream",
        "name": "Caramel Cream",
        "bank": "00 Seeds Bank / Humboldt",
        "url": "https://humboldtseedcompany.com/wp-content/uploads/2021/01/Caramel.jpg",
        "desc": "Inflorescencia madura en fondo negro puro de estudio oficial, cálices cargados de resina densa y pistilos naranja brillante."
    },
    {
        "id": "sweet-cream-caramel",
        "name": "Cream Caramel",
        "bank": "Sweet Seeds",
        "url": "https://allbud.s3.amazonaws.com/media/images/strain/cream-caramel/jv3xNoun/15934858603101465405999jpg.jpg",
        "desc": "Macro de cogollo curado índico sobre fondo gris oscuro pizarra, mostrando densos tricomas glandulares y estigmas ámbar."
    },
    {
        "id": "bf-zkittlez-og",
        "name": "Zkittlez OG",
        "bank": "Barney's Farm",
        "url": "https://www.barneysfarm.com/images/products/zkittlez-og-auto_jpeg_21_206033.jpg",
        "desc": "Macro botánica oficial de flor madura con fondo negro de Barney's Farm, cálices hinchados con cobertura masiva de tricomas."
    },
    {
        "id": "nirvana-white-widow",
        "name": "White Widow",
        "bank": "Nirvana Seeds",
        "url": "https://leafly-public.imgix.net/strains/reviews/photos/white-widow__primary_36f0.jpg?w=1200",
        "desc": "Toma macro de cogollo seco curado con el característico manto blanco de tricomas sobre fondo de estudio oscuro."
    },
    {
        "id": "ripper-criminal-plus",
        "name": "Criminal +",
        "bank": "Ripper Seeds",
        "url": "https://www.ripperseeds.com/img/p/5/6/6/566.jpg",
        "desc": "Fotografía oficial de floración de Ripper Seeds, racimo floral maduro resinoso sobre fondo oscuro de cultivo."
    },
    {
        "id": "sweet-black-jack",
        "name": "Black Jack",
        "bank": "Sweet Seeds",
        "url": "https://leafly-public.imgix.net/strains/reviews/photos/black-jack__primary_e20c.jpg?w=1200",
        "desc": "Fotografía macro de cogollo curado con glándulas de resina cristalinas, hojas de azúcar oscuras y pistilos anaranjados."
    },
    {
        "id": "ripper-kmintz",
        "name": "Kmintz",
        "bank": "Ripper Seeds",
        "url": "https://bucket.growdiaries.com/static/seed_item_photos/6966/kmintz.jpg",
        "desc": "Flor curada real con tonalidades violetas intensas, tricomas lechosos brillantes y pistilos cobrizos sobre fondo oscuro."
    },
    {
        "id": "sensi-sensi-amnesia",
        "name": "Sensi Amnesia",
        "bank": "Sensi Seeds",
        "url": "https://bucket.growdiaries.com/static/report/photo/328312/90bb0b5be71f1077315ddd62440a736d.webp",
        "desc": "Seguimiento real de cultivo en floración avanzada de Sensi Amnesia, gran cogollo central sativa con densos cálices verdes y resina."
    },
    {
        "id": "phil-lemon-og-candy",
        "name": "Lemon OG Candy",
        "bank": "Philosopher Seeds",
        "url": "https://www.cannaconnection.com/12830/lemon-og-candy.jpg",
        "desc": "Toma botánica de inflorescencia en floración sobre fondo natural oscuro, tricomas cargados y pistilos frescos."
    },
    {
        "id": "ihg-terple",
        "name": "Terple",
        "bank": "In-House Genetics",
        "url": "https://cdn.prod.website-files.com/65984dad3dc673726cd63bca/669165757a5711411936d057_map4.jpg",
        "desc": "Macro de dispensario de cogollo curado sobre losa oscura, intensa pigmentación púrpura y gruesa capa de tricomas plateados."
    },
    {
        "id": "raw-rainbow-studz",
        "name": "Rainbow Studz",
        "bank": "Raw Genetics",
        "url": "https://allbud.s3.amazonaws.com/media/images/strain/rainbow-chip/9oaTnkSy/imagejpg.jpg",
        "desc": "Fotografía óptica macro de cogollo curado con matices púrpuras y cálices resinosos en fondo de estudio gris neutro."
    }
]

print("=== INICIANDO DESCARGA Y PROCESAMIENTO BOTÁNICO (11 CEPAS) ===")
results = []

for item in STRAINS_DATA:
    sid = item["id"]
    url = item["url"]
    out_name = f"img/{sid}-bud-hd.jpg"
    print(f"\nProcesando [{sid}] desde:\n  {url}")
    
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = resp.read()
        
        im = Image.open(io.BytesIO(data)).convert("RGB")
        w, h = im.size
        print(f"  Descargado original: {w}x{h} px ({len(data)//1024} KB)")
        
        # Center crop 1:1
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        cropped = im.crop((left, top, left + min_dim, top + min_dim))
        
        # Ensure minimum 800x800 px
        final_w, final_h = cropped.size
        if final_w < 800 or final_h < 800:
            target_dim = 800
            cropped = cropped.resize((target_dim, target_dim), Image.Resampling.LANCZOS)
            print(f"  Reescalado Lanczos a: {cropped.size}")
        else:
            print(f"  Recorte 1:1 óptimo: {cropped.size}")
            
        cropped.save(out_name, format="JPEG", quality=95)
        file_sz = os.path.getsize(out_name)
        print(f"  Guardado en: {out_name} ({file_sz//1024} KB)")
        
        results.append({
            "id": sid,
            "name": item["name"],
            "url": url,
            "desc": item["desc"],
            "size": cropped.size,
            "status": "OK"
        })
    except Exception as e:
        print(f"  ERROR en {sid}: {e}")
        results.append({
            "id": sid,
            "name": item["name"],
            "url": url,
            "desc": item["desc"],
            "size": (0, 0),
            "status": f"FAIL: {e}"
        })

print("\n=== ACTUALIZANDO js/data.js ===")
with open("js/data.js", "r", encoding="utf-8") as f:
    data_js = f.read()

updated_count = 0
for item in STRAINS_DATA:
    sid = item["id"]
    new_img = f"img/{sid}-bud-hd.jpg"
    
    # Pattern to match this strain entry and update its image
    pattern = rf'(id:\s*["\']{re.escape(sid)}["\'].*?image:\s*["\'])([^"\']+)(["\'])'
    def replacer(m):
        global updated_count
        updated_count += 1
        return f"{m.group(1)}{new_img}{m.group(3)}"
    
    data_js = re.sub(pattern, replacer, data_js, count=1, flags=re.DOTALL)

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(data_js)

print(f"Actualizadas {updated_count} cepas en js/data.js.")
