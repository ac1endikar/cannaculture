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

COMPOUND_GENETICS_CATALOG = [
    {
        "id": "cpg-apples-and-bananas",
        "image": "img/cpg-apples-and-bananas.jpg",
        "name": "Apples and Bananas",
        "aka": "(Blue Power x Gelatti) x GDP x Platinum Cookies",
        "bank": "Compound Genetics",
        "species": "Hibrida",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 3500,
        "genetics": "(Blue Power x Gelatti) x Granddaddy Purple x Platinum Cookies",
        "origin": "Oregon / California, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "limonene": 25 },
        "flavors": ["Manzana Manzana", "Plátano Dulce", "Gasolina Diésel"],
        "effects": ["Euforia Cerebral", "Relax Físico", "Dicha Creativa"],
        "activities": ["creativity", "social", "music"],
        "description": "Una de las variedades modernas más aclamadas del mundo, creada por Compound Genetics en colaboración con Cookies. Combina un aroma penetrante a manzanas ácidas, plátano maduro y gasolina pura con una capa de resina que roza el 28% de THC.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #EAB308 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Apples and Bananas Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-pave",
        "image": "img/cpg-pave.jpg",
        "name": "Pavé",
        "aka": "Paris OG x Menthol",
        "bank": "Compound Genetics",
        "species": "Hibrida",
        "thc": 29, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2900,
        "genetics": "Paris OG x Menthol",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "menthol": 20 },
        "flavors": ["Menta Helada", "Gasolina OG", "Pino Picante"],
        "effects": ["Euforia Devastadora", "Sedación Corporal", "Paz Mental"],
        "activities": ["relax_sleep", "music", "meditation"],
        "description": "Desarrollada en colaboración con Quavo de Migos y Cookies. Recibe su nombre ('Pavé') porque sus flores parecen estar completamente pavimentadas de diamantes de resina blanca. Aroma mentolado y a gasolina OG extremadamente potente.",
        "visualColor": "linear-gradient(135deg, #64748B 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(100,116,139,0.2) 0%, transparent 70%)",
        "query": "Pave Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-la-bomba",
        "image": "img/cpg-la-bomba.jpg",
        "name": "La Bomba",
        "aka": "Wedding Cake x Jet Fuel Gelato",
        "bank": "Compound Genetics",
        "species": "Indica",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2400,
        "genetics": "Wedding Cake x Jet Fuel Gelato",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Pastel de Vainilla", "Gasolina Diésel", "Crema Dulce"],
        "effects": ["Golpe Corporal", "Euforia Risueña", "Calma Profunda"],
        "activities": ["relax_sleep", "social", "gaming"],
        "description": "Una auténtica bomba de potencia y aroma. Une la dulzura cremosa de Wedding Cake con la pegada a combustible diésel de Jet Fuel Gelato. Cogollos gigantes y morados muy resinosos.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "La Bomba Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-jokerz",
        "image": "img/cpg-jokerz.jpg",
        "name": "Jokerz",
        "aka": "White Runtz x Jet Fuel Gelato",
        "bank": "Compound Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.9, "reviewsCount": 2200,
        "genetics": "White Runtz x Jet Fuel Gelato",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "linalool": 25 },
        "flavors": ["Caramelo Runtz", "Gasolina Combustible", "Cítrico Dulce"],
        "effects": ["Euforia Risueña", "Bienestar Activo", "Relax Corporal"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Ganadora del premio Leafly Strain of the Year contender. Junta el sabor acaramelado a frutas de White Runtz con el fondo diésel picante de Jet Fuel Gelato. Tonalidades púrpura oscuro cubiertas de resina brillante.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #EC4899 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Jokerz Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-gastro-pop",
        "image": "img/cpg-gastro-pop.jpg",
        "name": "Gastro Pop",
        "aka": "Apples and Bananas x Grape Gas",
        "bank": "Compound Genetics",
        "species": "Hibrida",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 2600,
        "genetics": "Apples and Bananas x Grape Gas",
        "origin": "Oregon / California, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 35, "caryophyllene": 20 },
        "flavors": ["Uva Dulce", "Manzana Ácida", "Gas Diésel"],
        "effects": ["Euforia Estallido", "Sensación Placentera", "Relax Corporal"],
        "activities": ["social", "music", "creativity"],
        "description": "Cruce estelar entre Apples and Bananas y Grape Gas. Destaca por su perfil organoléptico complejo con aroma intenso a mermelada de uva, manzana verde y notas persistentes a gasolina dulce.",
        "visualColor": "linear-gradient(135deg, #7C3AED 0%, #06B6D4 100%)",
        "bgPattern": "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)",
        "query": "Gastro Pop Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-grape-gas",
        "image": "img/cpg-grape-gas.jpg",
        "name": "Grape Gas",
        "aka": "OG Chem x GDP x Truth OG",
        "bank": "Compound Genetics",
        "species": "Indica",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1800,
        "genetics": "OG Chem x Granddaddy Purple x Truth OG",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "limonene": 20 },
        "flavors": ["Uva Negra", "Gasolina Química", "Tierra Kush"],
        "effects": ["Sedación Corporal", "Paz Mental", "Descanso Profundo"],
        "activities": ["relax_sleep", "music"],
        "description": "Una de las madres genéticas pilares de Compound Genetics. Combina uva madura con un trasfondo químico diésel extremadamente penetrante y un efecto sedante ideal para desconectar al final del día.",
        "visualColor": "linear-gradient(135deg, #6B21A8 0%, #3B0764 100%)",
        "bgPattern": "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)",
        "query": "Grape Gas Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-marshmallow-og",
        "image": "img/cpg-marshmallow-og.jpg",
        "name": "Marshmallow OG",
        "aka": "Chemdawg D x Triangle Kush x Jet Fuel Gelato",
        "bank": "Compound Genetics",
        "species": "Indica",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1950,
        "genetics": "Chemdawg D x Triangle Kush x Jet Fuel Gelato",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Nube de Azúcar", "Pino OG", "Gas Combustible"],
        "effects": ["Relax Físico Intenso", "Euforia Alegre", "Sueño Reparador"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Híbrido goloso y potente que reúne tres gigantes de la historia del cannabis. Ofrece un perfil terpenoso a nubes de golosina tostada mezcladas con pino OG picante y diésel seco.",
        "visualColor": "linear-gradient(135deg, #F43F5E 0%, #FB7185 100%)",
        "bgPattern": "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)",
        "query": "Marshmallow OG Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-red-bullz",
        "image": "img/cpg-red-bullz.jpg",
        "name": "Red Bullz",
        "aka": "Grape Gas x White Runtz",
        "bank": "Compound Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1500,
        "genetics": "Grape Gas x White Runtz",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Bebida de Ponche", "Uva Acaramelada", "Gas Diésel"],
        "effects": ["Euforia Energética", "Impulso Social", "Relax Muscular"],
        "activities": ["social", "gaming", "creativity"],
        "description": "Variedad explosiva resultante de cruzar Grape Gas con White Runtz. Desprende un aroma punzante a bebida energética de ponche de frutas con fondo a gasolina acaramelada.",
        "visualColor": "linear-gradient(135deg, #EF4444 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)",
        "query": "Red Bullz Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-high-society",
        "image": "img/cpg-high-society.jpg",
        "name": "High Society",
        "aka": "Biscotti x Jet Fuel Gelato",
        "bank": "Compound Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1350,
        "genetics": "Biscotti x Jet Fuel Gelato",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "linalool": 25 },
        "flavors": ["Galleta de Nuez", "Canela Dulce", "Gasolina OG"],
        "effects": ["Euforia Elegante", "Bienestar Corporal", "Calma Mental"],
        "activities": ["social", "music", "nature_walk"],
        "description": "Una de las joyas gastronómicas de Compound Genetics. Cruce de Biscotti y Jet Fuel Gelato que cautiva por sus matices a galleta de nueces y canela especiada combinada con diésel fino.",
        "visualColor": "linear-gradient(135deg, #D97706 0%, #451A03 100%)",
        "bgPattern": "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)",
        "query": "High Society Compound Genetics strain flower bud"
    },
    {
        "id": "cpg-grandmaster-sexy",
        "image": "img/cpg-grandmaster-sexy.jpg",
        "name": "Grandmaster Sexy",
        "aka": "Scotty 2 Hotty x Oreoz",
        "bank": "Compound Genetics",
        "species": "Indica",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1450,
        "genetics": "Scotty 2 Hotty x Oreoz",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "myrcene": 30, "limonene": 20 },
        "flavors": ["Chocolate Oreoz", "Mantequilla Caliente", "Gas Kush"],
        "effects": ["Relajación Devastadora", "Dicha Cerebral", "Sueño Profundo"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Híbrido voluptuoso que cruza Scotty 2 Hotty con Oreoz. Destaca por su aroma a galletas de chocolate con crema de mantequilla dulce y su deslumbrante capa de resina blanca sobre flores violetas.",
        "visualColor": "linear-gradient(135deg, #1E1B4B 0%, #431407 100%)",
        "bgPattern": "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)",
        "query": "Grandmaster Sexy Compound Genetics strain flower bud"
    }
]

print("Downloading authentic flower images for Compound Genetics catalog...")
for strain in COMPOUND_GENETICS_CATALOG:
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

print("\nAll Compound Genetics photos ready.")
