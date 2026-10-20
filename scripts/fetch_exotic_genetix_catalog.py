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

EXOTIC_GENETIX_CATALOG = [
    {
        "id": "exg-grease-monkey",
        "image": "img/exg-grease-monkey.jpg",
        "name": "Grease Monkey",
        "aka": "Gorilla Glue #4 x Cookies and Cream",
        "bank": "Exotic Genetix",
        "species": "Indica",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 3100,
        "genetics": "Gorilla Glue #4 x Cookies and Cream",
        "origin": "Washington, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Vainilla Dulce", "Gasolina Diésel", "Tierra Skunk"],
        "effects": ["Sedación Corporal", "Euforia Intensa", "Relax Profundo"],
        "activities": ["relax_sleep", "music", "meditation"],
        "description": "Una de las obras maestras absolutas de Exotic Genetix. Cruce perfecto de Gorilla Glue #4 y Cookies and Cream que destaca por su potencia atronadora, una capa plateada de tricomas pegajosos y un perfil que combina vainilla cremosa con gasolina diésel.",
        "visualColor": "linear-gradient(135deg, #1E293B 0%, #475569 100%)",
        "bgPattern": "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)",
        "query": "Grease Monkey Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-cookies-and-cream",
        "image": "img/exg-cookies-and-cream.jpg",
        "name": "Cookies and Cream",
        "aka": "Starfighter x Mystery Cookie",
        "bank": "Exotic Genetix",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 2800,
        "genetics": "Starfighter x Mystery Cookie",
        "origin": "Washington, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Galleta de Vainilla", "Nata Cสถาน", "Tierra Dulce"],
        "effects": ["Euforia Feliz", "Relajación Muscular", "Calma Mente"],
        "activities": ["creativity", "social", "music"],
        "description": "Ganadora del primer puesto en la Denver Cannabis Cup. Legendaria variedad creada por Mike de Exotic Genetix con un irresistible perfil a galletas recién horneadas con nata de vainilla y resina acristalada.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Cookies and Cream Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-strawberries-and-cream",
        "image": "img/exg-strawberries-and-cream.jpg",
        "name": "Strawberries & Cream",
        "aka": "Strawberry Cough x Cookies and Cream",
        "bank": "Exotic Genetix",
        "species": "Hibrida",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 58, "rating": 4.9, "reviewsCount": 2100,
        "genetics": "Strawberry Cough x Cookies and Cream",
        "origin": "Washington, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 35, "caryophyllene": 20 },
        "flavors": ["Fresa Madura", "Batido de Nata", "Tierra Frutal"],
        "effects": ["Euforia Alegre", "Sensación Cálida", "Creatividad Dulce"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Delicioso híbrido frutal que fusiona el intenso aroma a fresas silvestres de Strawberry Cough con la cremosidad de Cookies and Cream. Produce flores tupidas teñidas de resina rosada.",
        "visualColor": "linear-gradient(135deg, #EF4444 0%, #F43F5E 100%)",
        "bgPattern": "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)",
        "query": "Strawberries and Cream Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-mint-chocolate-chip",
        "image": "img/exg-mint-chocolate-chip.jpg",
        "name": "Mint Chocolate Chip",
        "aka": "Thin Mint GSC x Green Ribbon BX",
        "bank": "Exotic Genetix",
        "species": "Hibrida",
        "thc": 24, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 1750,
        "genetics": "Thin Mint GSC x Green Ribbon BX",
        "origin": "Washington, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 35, "myrcene": 20 },
        "flavors": ["Menta Menta", "Chocolate Oscuro", "Pino Dulce"],
        "effects": ["Claridad Alegre", "Relax Físico Suave", "Bienestar"],
        "activities": ["social", "nature_walk", "music"],
        "description": "Refrito mentolado de gran éxito caracterizado por un aroma refrescante a menta piperita mezclada con toques de chocolate negro y pino. Cogollos compactos como piedras caladas de cristal.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Mint Chocolate Chip Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-red-runtz",
        "image": "img/exg-red-runtz.jpg",
        "name": "Red Runtz",
        "aka": "Red Pop x Runtz",
        "bank": "Exotic Genetix",
        "species": "Hibrida",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 1900,
        "genetics": "Red Pop x Runtz",
        "origin": "Washington, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "linalool": 25 },
        "flavors": ["Refresco de Cereza", "Caramelo Runtz", "Gas Dulce"],
        "effects": ["Euforia Explosiva", "Relax Corporal", "Dicha Mental"],
        "activities": ["social", "music", "gaming"],
        "description": "Uno de los lanzamientos modernos más aclamados de Exotic Genetix. Uniendo Red Pop con Runtz, ofrece una explosión de sabor a refresco de cereza dulce con gas diésel y colores rojo-púrpura deslumbrantes.",
        "visualColor": "linear-gradient(135deg, #DC2626 0%, #991B1B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)",
        "query": "Red Runtz Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-scotty-2-hotty",
        "image": "img/exg-scotty-2-hotty.jpg",
        "name": "Scotty 2 Hotty",
        "aka": "Biscotti x Rainbow Chip",
        "bank": "Exotic Genetix",
        "species": "Indica",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1400,
        "genetics": "Biscotti x Rainbow Chip",
        "origin": "Washington, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Galleta Italiana", "Mantequilla Dulce", "Gas Diésel"],
        "effects": ["Relax Físico", "Calma Risueña", "Descanso"],
        "activities": ["relax_sleep", "music"],
        "description": "Combinación genial de Biscotti y Rainbow Chip. Desprende un aroma muy rico a masa de galleta horneada con mantequilla caliente y regusto a gasolina fina. Efecto sedante y muy placentero.",
        "visualColor": "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
        "bgPattern": "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)",
        "query": "Scotty 2 Hotty Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-runtz-buttonz",
        "image": "img/exg-runtz-buttonz.jpg",
        "name": "Runtz Buttonz",
        "aka": "Runtz x Rainbow Chip",
        "bank": "Exotic Genetix",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1300,
        "genetics": "Runtz x Rainbow Chip",
        "origin": "Washington, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Gominolas Frutales", "Cítrico Tropical", "Kush Terroso"],
        "effects": ["Euforia Cerebral", "Energía Creativa", "Relax Corporal"],
        "activities": ["creativity", "social"],
        "description": "Híbrido goloso que cruza la célebre Runtz con Rainbow Chip. Produce cogollos ultra densos teñidos de violeta y naranja cubiertos por una manto espeso de resina con aroma a gominolas tropicales.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #C084FC 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)",
        "query": "Runtz Buttonz Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-power-sherb",
        "image": "img/exg-power-sherb.jpg",
        "name": "Power Sherb",
        "aka": "SherbBX x Cookies and Cream",
        "bank": "Exotic Genetix",
        "species": "Indica",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 1150,
        "genetics": "SherbBX x Cookies and Cream",
        "origin": "Washington, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "flavors": ["Sorbete de Cítricos", "Crema Dulce", "Kush Gasolina"],
        "effects": ["Potencia Corporal", "Euforia Alegre", "Relax Profundo"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Híbrido de gran calibre que combina el sorbete cítrico de Sunset Sherbet con la fuerza cremosa de Cookies and Cream. Flores macizas bañadas en resina terpénica muy aromática.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Power Sherb Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-gary-poppins",
        "image": "img/exg-gary-poppins.jpg",
        "name": "Gary Poppins",
        "aka": "Gary Payton x Red Pop",
        "bank": "Exotic Genetix",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 1600,
        "genetics": "Gary Payton x Red Pop",
        "origin": "Washington, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Cereza Diésel", "Pimienta Especiada", "Gas Dulce"],
        "effects": ["Euforia Social", "Claridad Activa", "Relax Físico"],
        "activities": ["social", "gaming", "creativity"],
        "description": "Unión brutal de la famosa Gary Payton con Red Pop. Presenta un aroma punzante a cerezas picantes y gas combustible con cogollos duros como rocas cargados de tricomas.",
        "visualColor": "linear-gradient(135deg, #E11D48 0%, #BE123C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(225,29,72,0.2) 0%, transparent 70%)",
        "query": "Gary Poppins Exotic Genetix strain flower bud"
    },
    {
        "id": "exg-tina",
        "image": "img/exg-tina.jpg",
        "name": "Tina",
        "aka": "Constantine x Cheetah Piss",
        "bank": "Exotic Genetix",
        "species": "Indica",
        "thc": 28, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 1850,
        "genetics": "Constantine x Cheetah Piss",
        "origin": "Washington, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "myrcene": 30, "limonene": 20 },
        "flavors": ["Gas Combustible", "Tierra Picante", "Zorrillo Skunk"],
        "effects": ["Sedación Knockout", "Euforia Pesada", "Relax Total"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Campeona absoluta de copas cannábicas y cepa insignia de la línea de Exotic Genetix. Un monstruo de THC de aroma skunk diésel ultraintenso que no perdona a ningún cultivador exigente.",
        "visualColor": "linear-gradient(135deg, #0F172A 0%, #334155 100%)",
        "bgPattern": "radial-gradient(circle, rgba(15,23,42,0.2) 0%, transparent 70%)",
        "query": "Tina Exotic Genetix strain flower bud"
    }
]

print("Downloading authentic flower images for Exotic Genetix catalog...")
for strain in EXOTIC_GENETIX_CATALOG:
    s_id = strain["id"]
    query = strain["query"]
    out_file = os.path.join(IMG_DIR, f"{s_id}.jpg")
    print(f"\nSearching photo for {s_id} ({query})...")
    
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'illustration', 'vector', 'ai', 'midjourney'])]
        
        saved = False
        for img_url in valid[:5]:
            try:
                r = urllib.request.Request(img_url, headers=HEADERS)
                with urllib.request.urlopen(r, timeout=10) as res:
                    data = res.read()
                if len(data) > 15000:
                    im = Image.open(io.BytesIO(data))
                    if im.width >= 400 and im.height >= 400:
                        im = im.convert('RGB')
                        im.save(out_file, 'JPEG', quality=95)
                        print(f"  ✅ Saved: {im.width}x{im.height} -> {out_file} ({len(data):,} bytes)")
                        saved = True
                        break
            except Exception as e:
                pass
        if not saved:
            print(f"  ⚠️ Could not download image for {s_id}")
    except Exception as e:
        print(f"  Error: {e}")

print("\nAll Exotic Genetix photos ready.")
