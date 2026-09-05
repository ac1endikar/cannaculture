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

SOMA_SEEDS_CATALOG = [
    {
        "id": "soma-nyc-diesel",
        "image": "img/soma-nyc-diesel.jpg",
        "name": "NYC Diesel",
        "aka": "Soma Original NYC Diesel",
        "bank": "Soma Seeds",
        "species": "Hibrida",
        "thc": 22, "cbd": 0.4,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 70, "rating": 4.9, "reviewsCount": 2800,
        "genetics": "Mexican Sativa x Afghani Landrace",
        "origin": "Nueva York / Ámsterdam",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Pomelo Rojo", "Gasolina Dulce", "Mandarina Cítrica"],
        "effects": ["Euforia Cerebral", "Energía Creativa", "Subidón Exótico"],
        "activities": ["creativity", "social", "music"],
        "description": "La legendaria NYC Diesel creada por Soma, ganadora de 5 premios en la High Times Cannabis Cup. Famosa mundialmente por su penetrante aroma a pomelo rojo recién cortado con toques de carburante dulce. Efecto eufórico, activo y supremamente creativo.",
        "visualColor": "linear-gradient(135deg, #EF4444 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)",
        "query": "NYC Diesel Soma Seeds strain flower bud"
    },
    {
        "id": "soma-amnesia-haze",
        "image": "img/soma-amnesia-haze.jpg",
        "name": "Amnesia Haze",
        "aka": "Soma Original Amnesia Haze",
        "bank": "Soma Seeds",
        "species": "Sativa",
        "thc": 23, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 650,
        "floweringDays": 80, "rating": 4.9, "reviewsCount": 3200,
        "genetics": "South Asian Sativa x Jamaican Sativa x Cambodian Haze",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Limón Especiado", "Incienso Haze", "Madera de Cedro"],
        "effects": ["Euforia Psicodélica", "Energía Elevada", "Viaje Mental"],
        "activities": ["creativity", "music", "nature_walk"],
        "description": "La ganadora absoluta de la Cannabis Cup 2004 creada por Soma. Una sativa maestra que ofrece un perfil terpénico complejo a incienso dulce, limón silvestre y especias orientales. Subidón psicodélico y duradero.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Amnesia Haze Soma Seeds strain flower bud"
    },
    {
        "id": "soma-somango",
        "image": "img/soma-somango.jpg",
        "name": "Somango",
        "aka": "Soma #5",
        "bank": "Soma Seeds",
        "species": "Indica",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1950,
        "genetics": "Jack Herer x Super Skunk x Big Skunk Korean",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "pinene": 25 },
        "flavors": ["Mango Maduro", "Fruta Tropical Dulce", "Resina Cítrica"],
        "effects": ["Claridad Estimulante", "Calma Corporal", "Euforia Sensual"],
        "activities": ["social", "creativity", "relax_sleep"],
        "description": "Anteriormente conocida como Soma #5. Famosa por su irresistible sabor a mango tropical y su tonalidad morada durante la maduración. Un humo delicioso que calma el cuerpo sin nublar la mente.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #EC4899 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Somango Soma Seeds strain flower bud"
    },
    {
        "id": "soma-lavender",
        "image": "img/soma-lavender.jpg",
        "name": "Lavender",
        "aka": "Soma Lavender Strain",
        "bank": "Soma Seeds",
        "species": "Indica",
        "thc": 20, "cbd": 0.5,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1700,
        "genetics": "Super Skunk x Big Skunk Korean x Afghan x Hawaiian",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "pinene": 25 },
        "flavors": ["Lavanda Floral", "Hachís Dulce", "Especias Afganas"],
        "effects": ["Relajación Profunda", "Paz Mental", "Alivio del Estrés"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Una de las cepas más hermosas y aromáticas del catálogo de Soma. Presenta cálices púrpura oscuro casi negros con pelos de color naranja violáceo y un aroma inconfundible a lavanda silvestre y hachís especiado.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)",
        "query": "Lavender Soma Seeds strain flower bud"
    },
    {
        "id": "soma-buddhas-sister",
        "image": "img/soma-buddhas-sister.jpg",
        "name": "Buddha's Sister",
        "aka": "Soma Recline",
        "bank": "Soma Seeds",
        "species": "Indica",
        "thc": 21, "cbd": 0.6,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 4.7, "reviewsCount": 1400,
        "genetics": "Recline x Afghani Hawaiian",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 30, "caryophyllene": 25 },
        "flavors": ["Cereza Cítrica", "Caramelo Dulce", "Especias Orientales"],
        "effects": ["Paz Meditativa", "Relajación Corporal", "Bienestar Espiritual"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Variedad altamente valorada en la comunidad terapéutica holandesa. Produce flores densas impregnadas de resina rosada con un sabor dulce a cerezas ácidas y caramelo. Efecto contemplativo y relajante.",
        "visualColor": "linear-gradient(135deg, #F43F5E 0%, #881337 100%)",
        "bgPattern": "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)",
        "query": "Buddhas Sister Soma Seeds strain flower bud"
    },
    {
        "id": "soma-soma-rockbud",
        "image": "img/soma-soma-rockbud.jpg",
        "name": "Soma Rockbud",
        "aka": "Rockbud / A+ Indica",
        "bank": "Soma Seeds",
        "species": "Indica",
        "thc": 20, "cbd": 0.5,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "floweringDays": 60, "rating": 4.6, "reviewsCount": 920,
        "genetics": "Super Skunk x Big Skunk Korean x Afghani x Hawaiian",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "pinene": 25 },
        "flavors": ["Tierra Húmeda", "Madera Roza", "Hachís Afgano"],
        "effects": ["Sedación Física", "Descanso Muscular", "Calma Absoluta"],
        "activities": ["relax_sleep"],
        "description": "Variedad bautizada por la dureza pétrea de sus flores. Híbrido indica de ramas compactas y tricomas rojizos con aroma clásico a tierra húmeda e incienso afgano. Efecto tranquilizante.",
        "visualColor": "linear-gradient(135deg, #475569 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)",
        "query": "Rockbud Soma Seeds strain flower bud"
    },
    {
        "id": "soma-g13-haze",
        "image": "img/soma-g13-haze.jpg",
        "name": "G13 Haze",
        "aka": "G13 x Hawaiian Haze",
        "bank": "Soma Seeds",
        "species": "Sativa",
        "thc": 23, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 75, "rating": 4.8, "reviewsCount": 1600,
        "genetics": "G13 Clone x Hawaiian Haze",
        "origin": "EEUU / Ámsterdam",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Pimienta Cítrica", "Incienso Dulce", "Fruta Tropical"],
        "effects": ["Claridad Intensa", "Euforia Cerebral", "Energía Duradera"],
        "activities": ["creativity", "social", "gaming"],
        "description": "Ganadora de la Cannabis Cup 2006. Une el poder mítico del clon leyenda G13 con las notas frutales y picantes de Hawaiian Haze. Un humo denso y eufórico de primera categoría.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "G13 Haze Soma Seeds strain flower bud"
    },
    {
        "id": "soma-so-g-kush",
        "image": "img/soma-so-g-kush.jpg",
        "name": "So G Kush",
        "aka": "OG Kush x LA Confidential x Trainwreck",
        "bank": "Soma Seeds",
        "species": "Indica",
        "thc": 23, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 65, "rating": 4.7, "reviewsCount": 1150,
        "genetics": "OG Kush x LA Confidential x Trainwreck",
        "origin": "California / Ámsterdam",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 40, "myrcene": 35, "limonene": 25 },
        "flavors": ["Pino Diésel", "Tierra Especiada", "Limón Químico"],
        "effects": ["Grave Sedación", "Calma Mental", "Relax Corporal Total"],
        "activities": ["relax_sleep"],
        "description": "Potente trinomio genético que reúne lo mejor de las leyendas norteamericanas OG Kush, LA Confidential y Trainwreck. Sabor denso a pino, tierra diésel y efecto corporal demoledor.",
        "visualColor": "linear-gradient(135deg, #15803D 0%, #166534 100%)",
        "bgPattern": "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)",
        "query": "So G Kush Soma Seeds strain flower bud"
    },
    {
        "id": "soma-free-white",
        "image": "img/soma-free-white.jpg",
        "name": "Free White",
        "aka": "Soma White Selection",
        "bank": "Soma Seeds",
        "species": "Hibrida",
        "thc": 21, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 63, "rating": 4.6, "reviewsCount": 780,
        "genetics": "White Widow x Big Skunk Korean",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 30, "pinene": 25 },
        "flavors": ["Skunk Cítrico", "Pino Blanco", "Tierra Dulce"],
        "effects": ["Euforia Equilibrada", "Sensación Social", "Relax Muscular"],
        "activities": ["social", "music", "nature_walk"],
        "description": "Selección blanca especial de Soma que combina la clásica resina acristalada de White Widow con el vigor vegetal y el dulzor skunk de Big Skunk Korean.",
        "visualColor": "linear-gradient(135deg, #94A3B8 0%, #334155 100%)",
        "bgPattern": "radial-gradient(circle, rgba(148,163,184,0.2) 0%, transparent 70%)",
        "query": "Free White Soma Seeds strain flower bud"
    },
    {
        "id": "soma-somaui",
        "image": "img/soma-somaui.jpg",
        "name": "Somaui",
        "aka": "Hawaiian Sativa x G13 Haze",
        "bank": "Soma Seeds",
        "species": "Sativa",
        "thc": 22, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 70, "rating": 4.7, "reviewsCount": 840,
        "genetics": "Hawaiian Sativa x G13 Haze",
        "origin": "Hawái / Ámsterdam",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Piña Tropical", "Cítrico Dulce", "Especias Florales"],
        "effects": ["Energía Solar", "Euforia Radiante", "Inspiración Creativa"],
        "activities": ["creativity", "nature_walk", "social"],
        "description": "Híbrido tropical insular que combina la brisa frutal de las sativa hawaianas con la estructura densa de G13 Haze. Sabor riquísimo a piña y cítricos con un subidón inspirador.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Somaui Soma Seeds strain flower bud"
    }
]

print("Downloading authentic flower images for Soma Seeds...")
for strain in SOMA_SEEDS_CATALOG:
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

print("\nAll Soma Seeds photos ready.")
