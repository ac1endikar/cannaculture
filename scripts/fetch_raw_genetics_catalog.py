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

RAW_GENETICS_CATALOG = [
    {
        "id": "raw-stuffed-french-toast",
        "image": "img/raw-stuffed-french-toast.jpg",
        "name": "Stuffed French Toast",
        "aka": "Paris OG x French Toast",
        "bank": "Raw Genetics",
        "species": "Indica",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 3900,
        "genetics": "Paris OG x French Toast",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Tostada de Canela", "Jarabe de Arce", "Gasolina OG"],
        "effects": ["Euforia Risueña", "Sedación Placentera", "Relax Total"],
        "activities": ["relax_sleep", "music", "meditation"],
        "description": "La creación insignia indiscutible de Raw Genetics. Combina la potencia diésel de Paris OG con el aroma dulce y especiado a torrijas con canela y jarabe de arce de French Toast. Cogollos blancos cargados de resina.",
        "visualColor": "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
        "bgPattern": "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)",
        "query": "Stuffed French Toast Raw Genetics strain flower bud"
    },
    {
        "id": "raw-georgia-pie",
        "image": "img/raw-georgia-pie.jpg",
        "name": "Georgia Pie",
        "aka": "Gellati x Kush Mints",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 3200,
        "genetics": "Gellati x Kush Mints",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Melocotón Dulce", "Pastel de Nuez", "Gasolina OG"],
        "effects": ["Euforia Cerebral", "Relax Físico", "Sensación Cálida"],
        "activities": ["social", "music", "creativity"],
        "description": "Célebre variedad desarrollada en colaboración con Cookies. Destaca por su inconfundible aroma a tarta de melocotón recién horneada con notas a menta fresca y gasolina diésel.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Georgia Pie Raw Genetics strain flower bud"
    },
    {
        "id": "raw-cherry-paloma",
        "image": "img/raw-cherry-paloma.jpg",
        "name": "Cherry Paloma",
        "aka": "Tropicana Cookies x Georgia Pie",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 2100,
        "genetics": "Tropicana Cookies x Georgia Pie",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "myrcene": 25, "caryophyllene": 25 },
        "flavors": ["Cereza Ácida", "Pomelo Rosado", "Gas Dulce"],
        "effects": ["Euforia Vibrante", "Energía Social", "Dicha Cerebral"],
        "activities": ["social", "gaming", "nature_walk"],
        "description": "Exótico cóctel cannábico que une Tropicana Cookies con Georgia Pie. Presenta flores de un violeta púrpura intenso con aroma cítrico a refresco de pomelo rosado y cerezas silvestres.",
        "visualColor": "linear-gradient(135deg, #E11D48 0%, #991B1B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(225,29,72,0.2) 0%, transparent 70%)",
        "query": "Cherry Paloma Raw Genetics strain flower bud"
    },
    {
        "id": "raw-apples-and-french-toast",
        "image": "img/raw-apples-and-french-toast.jpg",
        "name": "Apples & French Toast",
        "aka": "Apples & Bananas x Stuffed French Toast",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 2400,
        "genetics": "Apples & Bananas x Stuffed French Toast",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Tarta de Manzana", "Canela Dulce", "Gas Combustible"],
        "effects": ["Euforia Potente", "Relax Corporal", "Dicha Mente"],
        "activities": ["creativity", "social", "music"],
        "description": "Cruza dos de las mejores cepas modernas: Apples & Bananas con Stuffed French Toast. Un espectáculo visual y aromático a tarta de manzana crujiente con canela y diésel fino.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Apples and French Toast Raw Genetics strain flower bud"
    },
    {
        "id": "raw-marshmallow",
        "image": "img/raw-marshmallow.jpg",
        "name": "Raw Marshmallow",
        "aka": "Marshmallow OG x Stuffed French Toast",
        "bank": "Raw Genetics",
        "species": "Indica",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 1800,
        "genetics": "Marshmallow OG x Stuffed French Toast",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Nube de Azúcar", "Tostada Dulce", "Pino OG"],
        "effects": ["Sedación Placentera", "Paz Corporal", "Sueño Reparador"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Variedad golosa de alta gama. Mezcla el aroma a nubes de azucar tostadas de Marshmallow OG con las notas especiadas de Stuffed French Toast. Cobertura de resina blanca impresionante.",
        "visualColor": "linear-gradient(135deg, #F43F5E 0%, #FB7185 100%)",
        "bgPattern": "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)",
        "query": "Raw Marshmallow strain flower bud"
    },
    {
        "id": "raw-rainbow-studz",
        "image": "img/raw-rainbow-studz.jpg",
        "name": "Rainbow Studz",
        "aka": "Zkittlez x Rainbow Chip",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 1600,
        "genetics": "Zkittlez x Rainbow Chip",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "caryophyllene": 25, "linalool": 25 },
        "flavors": ["Gominola Frutal", "Caramelo Dulce", "Kush Gasolina"],
        "effects": ["Euforia Alegre", "Energía Social", "Relax Muscular"],
        "activities": ["social", "gaming", "music"],
        "description": "Una verdadera golosina cannábica. Junta el inconfundible perfil de caramelos de Zkittlez con Rainbow Chip para producir flores violetas cargadas de resina terpénica agridulce.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #C084FC 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)",
        "query": "Rainbow Studz Raw Genetics strain flower bud"
    },
    {
        "id": "raw-peeled-banana",
        "image": "img/raw-peeled-banana.jpg",
        "name": "Peeled Banana",
        "aka": "Banana OG x Stuffed French Toast",
        "bank": "Raw Genetics",
        "species": "Indica",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1750,
        "genetics": "Banana OG x Stuffed French Toast",
        "origin": "California, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "limonene": 25 },
        "flavors": ["Plátano Maduro", "Mantequilla Dulce", "Gas Combustible"],
        "effects": ["Relax Corporal Intenso", "Euforia Risueña", "Descanso"],
        "activities": ["relax_sleep", "music"],
        "description": "Delicioso híbrido de plátano cremoso. Mezcla Banana OG con Stuffed French Toast para dar paso a un humo muy denso con sabor a plátano flambeado en mantequilla y diésel.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Peeled Banana Raw Genetics strain flower bud"
    },
    {
        "id": "raw-runtz-pop",
        "image": "img/raw-runtz-pop.jpg",
        "name": "Runtz Pop",
        "aka": "Runtz x Red Pop",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1500,
        "genetics": "Runtz x Red Pop",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "linalool": 25 },
        "flavors": ["Refresco de Cereza", "Caramelo Runtz", "Gas Dulce"],
        "effects": ["Euforia Radiante", "Dicha Cerebral", "Relax Físico"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Variedad súper aromática que une Runtz con Red Pop. Presenta flores con matices rojos y violetas sabor a refresco dulce de cereza e incienso frutal.",
        "visualColor": "linear-gradient(135deg, #DC2626 0%, #991B1B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)",
        "query": "Runtz Pop Raw Genetics strain flower bud"
    },
    {
        "id": "raw-bacio-zkittlez",
        "image": "img/raw-bacio-zkittlez.jpg",
        "name": "Bacio Zkittlez",
        "aka": "Bacio Gelato x Zkittlez",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1400,
        "genetics": "Bacio Gelato x Zkittlez",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Helado Creado", "Caramelo Frutal", "Gas Kush"],
        "effects": ["Euforia Placentera", "Relax Físico", "Calma Mente"],
        "activities": ["social", "music", "nature_walk"],
        "description": "Selección de gran calibre que cruza Bacio Gelato #41 con Zkittlez. Combina el sabor cremoso a helado de avellana con el toque dulce acaramelado de Zkittlez.",
        "visualColor": "linear-gradient(135deg, #7C3AED 0%, #4338CA 100%)",
        "bgPattern": "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)",
        "query": "Bacio Zkittlez Raw Genetics strain flower bud"
    },
    {
        "id": "raw-zweet-inzanity",
        "image": "img/raw-zweet-inzanity.jpg",
        "name": "Zweet Inzanity",
        "aka": "Zkittlez x Gorilla Glue #4",
        "bank": "Raw Genetics",
        "species": "Hibrida",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1650,
        "genetics": "Zkittlez x Gorilla Glue #4",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "limonene": 25, "myrcene": 25 },
        "flavors": ["Caramelo Dulce", "Gasolina Pegajosa", "Pino OG"],
        "effects": ["Euforia Locura", "Pegada Corporal", "Relax Profundo"],
        "activities": ["relax_sleep", "gaming"],
        "description": "Una auténtica locura de resina y sabor. Une la dulzura frutal de Zkittlez con la pegajosidad extrema de GG4, produciendo cogollos pesados como piedras empapados en cristales.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Zweet Inzanity Raw Genetics strain flower bud"
    }
]

print("Downloading authentic flower images for Raw Genetics catalog...")
for strain in RAW_GENETICS_CATALOG:
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

print("\nAll Raw Genetics photos ready.")
