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

FLYING_DUTCHMEN_CATALOG = [
    {
        "id": "tfd-pot-of-gold",
        "image": "img/tfd-pot-of-gold.jpg",
        "name": "Pot of Gold",
        "aka": "POG / High Times Winner",
        "bank": "The Flying Dutchmen",
        "species": "Indica",
        "thc": 22, "cbd": 0.5,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 55, "rating": 4.9, "reviewsCount": 2100,
        "genetics": "Hindu Kush x Skunk #1",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "pinene": 25 },
        "flavors": ["Hachís Dulce", "Skunk Penetrante", "Especias Terrosas"],
        "effects": ["Sedación Profunda", "Euforia Cálida", "Relajación Muscular"],
        "activities": ["relax_sleep", "music"],
        "description": "La cepa buque insignia de The Flying Dutchmen, ganadora de la High Times Cannabis Cup. Un híbrido sensacional entre una afgana Hindu Kush seleccionada y Skunk #1. Produce cosechas masivas cubiertas de resina melosa con sabor a hachís especiado.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Pot of Gold Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-g-force",
        "image": "img/tfd-g-force.jpg",
        "name": "G-Force",
        "aka": "G13 x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Indica",
        "thc": 23, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 56, "rating": 4.8, "reviewsCount": 1450,
        "genetics": "G13 Clone x Skunk #1",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 40, "myrcene": 35, "limonene": 25 },
        "flavors": ["Pino Denso", "Skunk Terroso", "Especias Químicas"],
        "effects": ["Fuerza G Corporal", "Sedación Intensa", "Descanso Total"],
        "activities": ["relax_sleep"],
        "description": "Bautizada G-Force por su abrumadora fuerza de atracción gravitatoria corporal. Un cruce demoledor del clon mítico norteamericano G13 reforzado con la estabilidad de Skunk #1. Cogollos pesados como piedras.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #064E3B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "G Force Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-pineapple-punch",
        "image": "img/tfd-pineapple-punch.jpg",
        "name": "Pineapple Punch",
        "aka": "Real McCoy x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Hibrida",
        "thc": 20, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 63, "rating": 4.7, "reviewsCount": 1100,
        "genetics": "The Real McCoy x Skunk #1",
        "origin": "Hawái / Ámsterdam",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Piña Tropical", "Ponche Dulce", "Cítrico Ácido"],
        "effects": ["Euforia Tropical", "Alegría Radiante", "Energía Suave"],
        "activities": ["social", "nature_walk", "creativity"],
        "description": "Una verdadera delicia tropical creada seleccionando los fenotipos de piña más dulces de The Real McCoy cruzados con Skunk #1. Destaca por su inconfundible aroma a ponche de piña madura y su subidón risueño.",
        "visualColor": "linear-gradient(135deg, #FACC15 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)",
        "query": "Pineapple Punch Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-the-real-mccoy",
        "image": "img/tfd-the-real-mccoy.jpg",
        "name": "The Real McCoy",
        "aka": "Hawaiian Sativa x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Hibrida",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 65, "rating": 4.8, "reviewsCount": 1300,
        "genetics": "Hawaiian Sativa x Skunk #1",
        "origin": "Hawái / Ámsterdam",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 40, "myrcene": 35, "pinene": 25 },
        "flavors": ["Fruta Tropical", "Pimienta Cítrica", "Madera Dulce"],
        "effects": ["Claridad Cerebral", "Estimulación Creativa", "Bienestar"],
        "activities": ["creativity", "music", "social"],
        "description": "Cepa legendaria de The Flying Dutchmen que equilibra la dulzura exótica de las sativa hawaianas con la vigorosa floración de Skunk #1. Sabor complejo y especiado con un subidón inspirador.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "The Real McCoy Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-voyager",
        "image": "img/tfd-voyager.jpg",
        "name": "Voyager",
        "aka": "Malawi x Hindu Kush x Thai",
        "bank": "The Flying Dutchmen",
        "species": "Hibrida",
        "thc": 22, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.7, "reviewsCount": 980,
        "genetics": "Malawi Gold x Hindu Kush x Thai Sativa",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "terpinolene": 30, "caryophyllene": 25 },
        "flavors": ["Incienso Oriental", "Especias Picantes", "Tierra Exótica"],
        "effects": ["Viaje Místico", "Euforia Elevada", "Relajación Corporal"],
        "activities": ["meditation", "music", "creativity"],
        "description": "Una auténtica expedición genética intercontinental. Combina la potencia cósmica de Malawi Gold con la resina de Hindu Kush y la agudeza mental de Thai Sativa. Aroma envolvente a incienso y especias.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #5B21B6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)",
        "query": "Voyager Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-dame-blanche",
        "image": "img/tfd-dame-blanche.jpg",
        "name": "Dame Blanche",
        "aka": "White Widow x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Indica",
        "thc": 21, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 55, "rating": 4.6, "reviewsCount": 850,
        "genetics": "White Widow x Skunk #1",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "limonene": 25 },
        "flavors": ["Pino Nieve", "Skunk Dulce", "Tierra Especiada"],
        "effects": ["Euforia Sedosa", "Calma Corporal", "Relajación Mágica"],
        "activities": ["relax_sleep", "social"],
        "description": "Homenaje a la 'Dama Blanca' holandesa. Cruce refinado entre la inconfundible White Widow y Skunk #1. Produce cálices cubiertos por un manto espeso de resina blanca y un aroma floral a pino dulce.",
        "visualColor": "linear-gradient(135deg, #E2E8F0 0%, #475569 100%)",
        "bgPattern": "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)",
        "query": "Dame Blanche Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-titan",
        "image": "img/tfd-titan.jpg",
        "name": "Titan",
        "aka": "Skunk #1 x Northern Lights #5",
        "bank": "The Flying Dutchmen",
        "species": "Indica",
        "thc": 22, "cbd": 0.5,
        "yieldIndoor": 600, "yieldOutdoor": 700,
        "floweringDays": 50, "rating": 4.8, "reviewsCount": 1200,
        "genetics": "Skunk #1 x Northern Lights #5",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "pinene": 30, "caryophyllene": 20 },
        "flavors": ["Pino Resinoso", "Hachís Skunk", "Tierra Húmeda"],
        "effects": ["Rendimiento Titánico", "Sedación Muscular", "Paz Interior"],
        "activities": ["relax_sleep"],
        "description": "Variedad bautizada Titan por su estatura compacta e increíble peso de cosecha. Une el vigor híbrido de Skunk #1 con la legendaria cobertura de resina de Northern Lights #5. Efecto contundente.",
        "visualColor": "linear-gradient(135deg, #0EA5E9 0%, #0369A1 100%)",
        "bgPattern": "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)",
        "query": "Titan Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-nepal-baba",
        "image": "img/tfd-nepal-baba.jpg",
        "name": "Nepal Baba",
        "aka": "Nepalese Charas x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Indica",
        "thc": 20, "cbd": 0.7,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 55, "rating": 4.7, "reviewsCount": 760,
        "genetics": "Nepalese Temple Hash Landrace x Skunk #1",
        "origin": "Nepal / Ámsterdam",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 55, "caryophyllene": 25, "pinene": 20 },
        "flavors": ["Hachís Nepalí", "Madera de Cedro", "Especias del Himalaya"],
        "effects": ["Paz Meditativa", "Relajación Corporal", "Serenidad Mental"],
        "activities": ["meditation", "relax_sleep"],
        "description": "Desarrollada a partir de las auténticas genéticas de hachís nepalí del Himalaya. Ofrece un humo suave y muy aromático con notas a madera sagrada, incienso y resina artesanal.",
        "visualColor": "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
        "bgPattern": "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)",
        "query": "Nepal Baba Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-swazi-safari",
        "image": "img/tfd-swazi-safari.jpg",
        "name": "Swazi Safari",
        "aka": "Swazi Landrace x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Sativa",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 600,
        "floweringDays": 70, "rating": 4.6, "reviewsCount": 680,
        "genetics": "Swazi African Landrace x Skunk #1",
        "origin": "Suazilandia / Países Bajos",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 50, "myrcene": 25, "limonene": 25 },
        "flavors": ["Cítrico Dulce", "Pimienta Africana", "Cítrico de Montaña"],
        "effects": ["Energía Eléctrica", "Euforia Activa", "Claridad Cerebral"],
        "activities": ["workout", "nature_walk", "creativity"],
        "description": "Sativa africana de alta potencia aclimatada por Eddie en Ámsterdam. Combina la fuerza energizante de las razas puras de Suazilandia con la rapidez de floración de Skunk #1.",
        "visualColor": "linear-gradient(135deg, #22C55E 0%, #15803D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)",
        "query": "Swazi Safari Flying Dutchmen strain flower bud"
    },
    {
        "id": "tfd-dutchmens-royal-orange",
        "image": "img/tfd-dutchmens-royal-orange.jpg",
        "name": "Dutchmen's Royal Orange",
        "aka": "Cali Orange x Skunk #1",
        "bank": "The Flying Dutchmen",
        "species": "Hibrida",
        "thc": 20, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 55, "rating": 4.7, "reviewsCount": 820,
        "genetics": "California Orange x Skunk #1",
        "origin": "California / Ámsterdam",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 30, "caryophyllene": 25 },
        "flavors": ["Naranja Madura", "Piel de Mandarina", "Dulzor Skunk"],
        "effects": ["Alegría Social", "Euforia Suave", "Bienestar Cítrico"],
        "activities": ["social", "music", "nature_walk"],
        "description": "Selección real de California Orange combinada con Skunk #1. Famosa por sus cálices abultados de color naranja dorado y su aroma a zumo fresco de naranja dulce.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Dutchmens Royal Orange Flying Dutchmen strain flower bud"
    }
]

print("Downloading authentic flower images for The Flying Dutchmen...")
for strain in FLYING_DUTCHMEN_CATALOG:
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

print("\nAll The Flying Dutchmen photos ready.")
