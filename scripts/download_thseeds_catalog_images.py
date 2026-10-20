import urllib.request
import urllib.parse
import json
import re
import os
import sys
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

IMG_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "img"))
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# List of T.H.Seeds strains to detail and fetch from official website / high quality sources
TH_SEEDS_CATALOG = [
    {
        "id": "ths-french-macaron",
        "name": "French Macaron",
        "aka": "Gelato 33 x French Cookies",
        "species": "Hibrida",
        "thc": 24, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays: 63": 63,
        "genetics": "Gelato 33 x French Cookies",
        "dominantTerpene": "caryophyllene",
        "terpenes": {"caryophyllene": 45, "limonene": 30, "linalool": 25},
        "flavors": ["Macaron Dulce", "Gasolina Cremosa", "Noche Francesa"],
        "effects": ["Euforia Sofisticada", "Relajación Dulce", "Bienestar Sensorial"],
        "activities": ["social", "music", "relax_sleep"],
        "description": "Una obra maestra premiada de T.H.Seeds. Cruce estelar entre la legendaria Gelato 33 y French Cookies. Ofrece un perfil cremoso y dulce a repostería francesa con matices gaseosos. Cogollos morados oscuros y resinosos de potencia extraordinaria.",
        "visualColor": "linear-gradient(135deg, #6B21A8 0%, #1E1B4B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)",
        "query": "TH Seeds French Macaron strain bud"
    },
    {
        "id": "ths-banana-candy-krush",
        "name": "Banana Candy Krush",
        "aka": "Banana Cake x Kush Mints",
        "species": "Hibrida",
        "thc": 25, "cbd": 0.1,
        "yieldIndoor": 600, "yieldOutdoor": 700,
        "floweringDays": 60,
        "genetics": "Banana Cake x Kush Mints",
        "dominantTerpene": "limonene",
        "terpenes": {"limonene": 40, "myrcene": 35, "caryophyllene": 25},
        "flavors": ["Plátano Dulce", "Caramelo de Plátano", "Menta Cremosa"],
        "effects": ["Euforia Potente", "Relajación Dulce", "Felicidad Creativa"],
        "activities": ["creativity", "social", "music"],
        "description": "Explosión de sabor a caramelo de plátano cremoso producido por la fusión de Banana Cake y Kush Mints. Produce flores ultra resinosas ideales para extracciones de rosin de nivel competición.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #78350F 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "TH Seeds Banana Candy Krush strain bud"
    },
    {
        "id": "ths-mont-blanc",
        "name": "Mont Blanc",
        "aka": "French Cookies x Birthday Cake x Strawbanana Cream",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63,
        "genetics": "French Cookies x Birthday Cake x Strawbanana Cream",
        "dominantTerpene": "caryophyllene",
        "terpenes": {"caryophyllene": 40, "myrcene": 35, "limonene": 25},
        "flavors": ["Vainilla Cremosa", "Fresa Glaseada", "Pastel de Cumpleaños"],
        "effects": ["Subidón Nevado", "Euforia Cerebral", "Relajación Profunda"],
        "activities": ["creativity", "relax_sleep"],
        "description": "Nombrada por las famosas montañas del Mont Blanc debido a su capa torrencial de tricomas blancos como la nieve. Un cruce a tres bandas con perfil cremoso a pastel de vainilla y fresa.",
        "visualColor": "linear-gradient(135deg, #E2E8F0 0%, #475569 100%)",
        "bgPattern": "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)",
        "query": "TH Seeds Mont Blanc strain bud"
    },
    {
        "id": "ths-pisthash",
        "name": "Pisthash",
        "aka": "Biscotti x French Cookies",
        "species": "Hibrida",
        "thc": 24, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60,
        "genetics": "Biscotti x French Cookies",
        "dominantTerpene": "limonene",
        "terpenes": {"limonene": 40, "caryophyllene": 35, "linalool": 25},
        "flavors": ["Pistacho Dulce", "NuezTostada", "Galleta Italiana"],
        "effects": ["Euforia Elegante", "Bienestar Físico", "Calma Mental"],
        "activities": ["social", "nature_walk"],
        "description": "Una cepa única que entrega aromas cremosos y tostados a frutos secos y pistacho verde. Combinación gourmet de Biscotti con French Cookies.",
        "visualColor": "linear-gradient(135deg, #84CC16 0%, #15803D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)",
        "query": "TH Seeds Pisthash strain bud"
    },
    {
        "id": "ths-melonsicle",
        "name": "Melonsicle",
        "aka": "Watermelon x Strawberry Banana x Girl Scout Cookies",
        "species": "Sativa",
        "thc": 24, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63,
        "genetics": "Watermelon x Strawberry Banana x GSC",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 45, "limonene": 30, "pinene": 25},
        "flavors": ["Sandía Dulce", "Helado de Fresa", "Fruta Tropical"],
        "effects": ["Euforia Tropical", "Energía Creativa", "Buen Humor"],
        "activities": ["social", "creativity", "nature_walk"],
        "description": "Bomba frutal que sabe a helado de sandía y fresa. Un híbrido con ligera dominancia sativa perfecto para refrescar los días soleados.",
        "visualColor": "linear-gradient(135deg, #EF4444 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)",
        "query": "TH Seeds Melonsicle strain bud"
    },
    {
        "id": "ths-blumosa",
        "name": "Blumosa",
        "aka": "Blue Sherbet x Mimosa",
        "species": "Hibrida",
        "thc": 23, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60,
        "genetics": "Blue Sherbet x Mimosa",
        "dominantTerpene": "limonene",
        "terpenes": {"limonene": 45, "myrcene": 30, "pinene": 25},
        "flavors": ["Arándano Cítrico", "Champán de Naranja", "Sorbete Dulce"],
        "effects": ["Euforia Espumosa", "Energía Solar", "Claridad Mental"],
        "activities": ["social", "creativity"],
        "description": "Maridaje cítrico y afrutado de Blue Sherbet y Mimosa. Produce un humo sedoso con notas a cóctel de frutas tropicales y un efecto estimulante y alegre.",
        "visualColor": "linear-gradient(135deg, #3B82F6 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)",
        "query": "TH Seeds Blumosa strain bud"
    }
]

print("Fetching high-res images for new T.H.Seeds strains...")
for s in TH_SEEDS_CATALOG:
    s_id = s["id"]
    query = s["query"]
    out_file = os.path.join(IMG_DIR, f"{s_id}.jpg")
    print(f"\nSearching image for {s_id} ({query})...")
    
    # Try Bing image search
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'vector'])]
        if valid:
            for img_url in valid[:3]:
                try:
                    r = urllib.request.Request(img_url, headers=HEADERS)
                    with urllib.request.urlopen(r, timeout=10) as res:
                        data = res.read()
                    if len(data) > 10000:
                        im = Image.open(io.BytesIO(data))
                        if im.width >= 400 and im.height >= 400:
                            im = im.convert('RGB')
                            im.save(out_file, 'JPEG', quality=95)
                            print(f"  ✅ Saved: {im.width}x{im.height} -> {out_file} ({len(data):,} bytes)")
                            break
                except Exception as e:
                    pass
    except Exception as e:
        print(f"  Error searching for {s_id}: {e}")
