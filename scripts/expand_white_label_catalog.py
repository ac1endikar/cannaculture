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

FULL_WLS_CATALOG = [
    {
        "id": "wls-white-widow",
        "image": "img/wls-white-widow.jpg",
        "name": "White Widow",
        "aka": "Original White Widow",
        "bank": "White Label Seed Co.",
        "species": "Hibrida",
        "thc": 21, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 55, "rating": 4.8, "reviewsCount": 2100,
        "genetics": "Brazilian Sativa x South Indian Indica",
        "origin": "Ámsterdam, Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "pinene": 25 },
        "flavors": ["Pino Resinoso", "Especias Terrosas", "Madera de Cedro"],
        "effects": ["Euforia Cerebral", "Relajación Corporal", "Energía Social"],
        "activities": ["social", "creativity", "nature_walk"],
        "description": "La legendaria White Widow en la versión oficial de White Label Seed Co. Famosa mundialmente por su densa manta de cristales blancos de resina y su aroma a pino fresco y tierra especiada. Efecto eufórico y equilibrado.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "White Widow White Label Seed Co strain flower"
    },
    {
        "id": "wls-snow-white",
        "image": "img/wls-snow-white.jpg",
        "name": "Snow White",
        "aka": "Pure Power Plant x White Widow",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 22, "cbd": 0.3,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 56, "rating": 4.7, "reviewsCount": 1150,
        "genetics": "Pure Power Plant x White Widow",
        "origin": "Países Bajos",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 40, "myrcene": 35, "limonene": 25 },
        "flavors": ["Tierra Dulce", "Cítrico Suave", "Madera Tropical"],
        "effects": ["Sedación Física", "Calma Mental", "Bienestar Profundo"],
        "activities": ["relax_sleep", "music"],
        "description": "Variedad blanca de alto rendimiento que combina la estructura compacta de PPP con la resina nevada de White Widow. Sabor dulce con toques cítricos y terrosos, ideal para la relajación nocturna.",
        "visualColor": "linear-gradient(135deg, #F8FAFC 0%, #64748B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(248,250,252,0.2) 0%, transparent 70%)",
        "query": "Snow White White Label Seed Co strain bud"
    },
    {
        "id": "wls-white-skunk",
        "image": "img/wls-white-skunk.jpg",
        "name": "White Skunk",
        "aka": "White Widow x Skunk #1",
        "bank": "White Label Seed Co.",
        "species": "Hibrida",
        "thc": 20, "cbd": 0.5,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 50, "rating": 4.6, "reviewsCount": 980,
        "genetics": "White Widow x Skunk #1",
        "origin": "Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 30, "caryophyllene": 25 },
        "flavors": ["Naranja Licoresca", "Skunk Penetrante", "Especias Cítricas"],
        "effects": ["Alegría Radiante", "Euforia Suave", "Relax Muscular"],
        "activities": ["social", "gaming", "music"],
        "description": "Una de las cepas más fáciles de cultivar del catálogo de White Label. Cruce de Skunk #1 con resina blanca que ofrece un sabor sorprendente a licor de naranja y humo suave y risueño.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "White Skunk White Label Seed Co strain bud"
    },
    {
        "id": "wls-white-ice",
        "image": "img/wls-white-ice.jpg",
        "name": "White Ice",
        "aka": "Indica Crystal Extreme (ICE)",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 22, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 50, "rating": 4.7, "reviewsCount": 890,
        "genetics": "Northern Lights x Dutch Skunk x Afghani Hash Plant",
        "origin": "Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "pinene": 25, "caryophyllene": 25 },
        "flavors": ["Pino Helado", "Hachís Meloso", "Tierra Especiada"],
        "effects": ["Efecto Hielo (Couch-Lock)", "Sedación Muscular", "Paz Mental"],
        "activities": ["relax_sleep"],
        "description": "Conocida como Indica Crystal Extreme. Híbrido afgano de floración ultrarrápida cubierto por una costra densa de resina brillante que parece nieve congelada. Efecto pesado y profundamente sedante.",
        "visualColor": "linear-gradient(135deg, #0EA5E9 0%, #1E293B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)",
        "query": "White Ice White Label Seed Co strain bud"
    },
    {
        "id": "wls-white-diesel",
        "image": "img/wls-white-diesel.jpg",
        "name": "White Diesel",
        "aka": "NYC Diesel x White Widow",
        "bank": "White Label Seed Co.",
        "species": "Hibrida",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 60, "rating": 4.7, "reviewsCount": 760,
        "genetics": "NYC Diesel x White Widow",
        "origin": "Nueva York / Ámsterdam",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 40, "caryophyllene": 35, "myrcene": 25 },
        "flavors": ["Gasolina Cítrica", "Pomelo Amargo", "Limón Químico"],
        "effects": ["Energía Estimulante", "Euforia Creativa", "Claridad Mental"],
        "activities": ["creativity", "social", "gaming"],
        "description": "Híbrido de gran personalidad que une los potentes matices diésel y pomelo de NYC Diesel con la abundante cobertura de resina de la línea White. Sabor penetrante y subidón energizante.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #065F46 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "White Diesel White Label Seed Co strain bud"
    },
    {
        "id": "wls-double-gum",
        "image": "img/wls-double-gum.jpg",
        "name": "Double Gum",
        "aka": "Double Bubblegum Selection",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 19, "cbd": 0.4,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "floweringDays": 48, "rating": 4.6, "reviewsCount": 650,
        "genetics": "Indiana Bubblegum Inbred Selection",
        "origin": "Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "limonene": 25 },
        "flavors": ["Chicle de Fresa", "Caramelo Rosa", "Dulzura Afrutada"],
        "effects": ["Relajación Dulce", "Euforia Alegre", "Calma Corporal"],
        "activities": ["social", "music", "relax_sleep"],
        "description": "Selección compacta e indica de la clásica Bubblegum. Floración súper corta de menos de 50 días y un aroma intenso a chicle dulce rosa que inunda el espacio de cultivo.",
        "visualColor": "linear-gradient(135deg, #F43F5E 0%, #BE123C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)",
        "query": "Double Gum White Label Seed Co strain bud"
    },
    {
        "id": "wls-pure-power-plant",
        "image": "img/wls-pure-power-plant.jpg",
        "name": "Pure Power Plant (PPP)",
        "aka": "PPP White Label",
        "bank": "White Label Seed Co.",
        "species": "Hibrida",
        "thc": 22, "cbd": 0.2,
        "yieldIndoor": 600, "yieldOutdoor": 750,
        "floweringDays": 55, "rating": 4.8, "reviewsCount": 1850,
        "genetics": "South African Sativa x USA Indica",
        "origin": "Sudáfrica / Países Bajos",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 40, "myrcene": 30, "caryophyllene": 30 },
        "flavors": ["Pino Picante", "Vainilla Dulce", "Tierra Especiada"],
        "effects": ["Potencia Eléctrica", "Euforia Masiva", "Energía Duradera"],
        "activities": ["social", "creativity", "gaming"],
        "description": "La legendaria Pure Power Plant (PPP) en la versión de White Label. Productora masiva de cogollos duros como rocas con un potente aroma especiado a pino y vainilla y un subidón eufórico muy apreciado en los coffee shops holandeses.",
        "visualColor": "linear-gradient(135deg, #22C55E 0%, #15803D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)",
        "query": "Pure Power Plant White Label Seed Co strain bud"
    },
    {
        "id": "wls-master-kush",
        "image": "img/wls-master-kush-official.jpg",
        "name": "Master Kush",
        "aka": "High Hindu Kush Selection",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 20, "cbd": 0.6,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 50, "rating": 4.7, "reviewsCount": 1420,
        "genetics": "Hindu Kush x Skunk #1",
        "origin": "Afganistán / Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "pinene": 25 },
        "flavors": ["Hachís Charas", "Tierra Dulce", "Incienso de Pino"],
        "effects": ["Relax Físico Clásico", "Serenidad Mental", "Alivio del Estrés"],
        "activities": ["relax_sleep", "nature_walk"],
        "description": "Doble ganadora de la Cannabis Cup. Híbrido de Hindu Kush que conserva el aroma tradicional a hachís artesanal charas con toques sutiles de tierra y pino. Humo suave e indica refinada.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #3B0764 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Master Kush White Label Seed Co strain bud"
    },
    {
        "id": "wls-orange-bud",
        "image": "img/wls-orange-bud.jpg",
        "name": "Orange Bud",
        "aka": "100% Skunk Selection",
        "bank": "White Label Seed Co.",
        "species": "Sativa",
        "thc": 19, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 55, "rating": 4.7, "reviewsCount": 1300,
        "genetics": "Select Skunk Phenotype",
        "origin": "California / Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 35, "caryophyllene": 20 },
        "flavors": ["Naranja Fresca", "Piel de Cítrico", "Dulzor Skunk"],
        "effects": ["Energía Estimulante", "Euforia Creativa", "Sensación Social"],
        "activities": ["social", "creativity", "nature_walk"],
        "description": "Selección de Skunk 100% pura famosa por sus abundantes pelos de color naranja intenso y su delicioso aroma a naranjas maduras. Subidón sativa activo y cerebral.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Orange Bud White Label Seed Co strain bud"
    },
    {
        "id": "wls-afghani-1",
        "image": "img/wls-afghani-1-official.jpg",
        "name": "Afghani #1",
        "aka": "Pure Afghan Hash Plant",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 20, "cbd": 0.8,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 45, "rating": 4.6, "reviewsCount": 940,
        "genetics": "Afghani Landrace Inbred Line",
        "origin": "Afganistán",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 55, "caryophyllene": 25, "pinene": 20 },
        "flavors": ["Hachís Especiado", "Tierra Profunda", "Pimienta Dulce"],
        "effects": ["Sedación Muscular", "Pesadez Física", "Sueño Profundo"],
        "activities": ["relax_sleep"],
        "description": "Variedad indica pura originaria de las montañas de Afganistán. La planta de hachís por excelencia con hojas anchas, cálices voluminosos y un efecto narcótico tradicional.",
        "visualColor": "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
        "bgPattern": "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)",
        "query": "Afghani 1 White Label Seed Co strain bud"
    },
    {
        "id": "wls-super-skunk",
        "image": "img/wls-super-skunk.jpg",
        "name": "Super Skunk",
        "aka": "Skunk #1 x Afghani #1",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 21, "cbd": 0.5,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 50, "rating": 4.8, "reviewsCount": 1650,
        "genetics": "Skunk #1 x Afghani Hash Plant",
        "origin": "Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "limonene": 20 },
        "flavors": ["Skunk Intenso", "Dulzura Citrica", "Hachís Terroso"],
        "effects": ["Relajación Profunda", "Euforia Cálida", "Alivio del Estrés"],
        "activities": ["relax_sleep", "social"],
        "description": "La célebre versión de Super Skunk elaborada por White Label. Cruce galardonado de Skunk #1 con una planta de hachís afgana pura. Cogollos voluminosos repleto de glándulas aromáticas de resina.",
        "visualColor": "linear-gradient(135deg, #16A34A 0%, #15803D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(22,163,74,0.2) 0%, transparent 70%)",
        "query": "Super Skunk White Label Seed Co strain bud"
    },
    {
        "id": "wls-northern-lights",
        "image": "img/wls-northern-lights.jpg",
        "name": "Northern Lights",
        "aka": "NL #5 Selection",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 22, "cbd": 0.6,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 50, "rating": 4.9, "reviewsCount": 2400,
        "genetics": "Afghani Indica x Thai Sativa",
        "origin": "EEUU / Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 55, "pinene": 25, "caryophyllene": 20 },
        "flavors": ["Pino Dulce", "Tierra Húmeda", "Especias Almizcladas"],
        "effects": ["Sedación Corporal", "Paz Interior", "Descanso Reparador"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Una de las variedades más influyentes de la historia del cannabis. La versión de White Label destaca por su estructura resistente de baja estatura, su rápida floración y sus cogollos compactos y dulzones.",
        "visualColor": "linear-gradient(135deg, #0284C7 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(2,132,199,0.2) 0%, transparent 70%)",
        "query": "Northern Lights White Label Seed Co strain bud"
    },
    {
        "id": "wls-shiva-skunk",
        "image": "img/wls-shiva-skunk.jpg",
        "name": "Shiva Skunk",
        "aka": "Northern Lights #5 x Skunk #1",
        "bank": "White Label Seed Co.",
        "species": "Indica",
        "thc": 23, "cbd": 0.4,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 55, "rating": 4.8, "reviewsCount": 1100,
        "genetics": "Northern Lights #5 x Skunk #1",
        "origin": "Países Bajos",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 35, "limonene": 20 },
        "flavors": ["Incienso Cítrico", "Almizcle Dulce", "Skunk Penetrante"],
        "effects": ["Potencia Mística", "Euforia Densa", "Relajación Muscular"],
        "activities": ["music", "meditation"],
        "description": "El híbrido Skunk más potente creado por la familia Sensi / White Label. Combina la fuerza desbordante de NL#5 con el volumen y vigor de Skunk #1. Olor penetrante a incienso cítrico.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)",
        "query": "Shiva Skunk White Label Seed Co strain bud"
    },
    {
        "id": "wls-purple-haze",
        "image": "img/wls-purple-haze.jpg",
        "name": "Purple Haze",
        "aka": "Original Purple Haze Selection",
        "bank": "White Label Seed Co.",
        "species": "Sativa",
        "thc": 21, "cbd": 0.2,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 65, "rating": 4.8, "reviewsCount": 1780,
        "genetics": "Purple Thai x Haze",
        "origin": "California / Países Bajos",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "myrcene": 30, "caryophyllene": 25 },
        "flavors": ["Arándano Silvestre", "Incienso Haze", "Especias Dulces"],
        "effects": ["Euforia Psicodélica", "Energía Creativa", "Estimulación Sensorial"],
        "activities": ["creativity", "music", "social"],
        "description": "Híbrido sativa místico celebrado en canciones y cultura cannábica. Destaca por sus tonalidades púrpuras y violetas al final de floración y un subidón cerebral volador con aroma a incienso y bayas.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #6B21A8 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Purple Haze White Label Seed Co strain bud"
    },
    {
        "id": "wls-durban",
        "image": "img/wls-durban.jpg",
        "name": "Durban",
        "aka": "Durban Poison Selection",
        "bank": "White Label Seed Co.",
        "species": "Sativa",
        "thc": 20, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.7, "reviewsCount": 1250,
        "genetics": "Durban South Africa Landrace",
        "origin": "Durban, Sudáfrica",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 50, "myrcene": 25, "limonene": 25 },
        "flavors": ["Anís Dulce", "Regaliz Especiado", "Limón Silvestre"],
        "effects": ["Subidón Energético", "Claridad Mental", "Motivación Activa"],
        "activities": ["workout", "nature_walk", "creativity"],
        "description": "Sativa sudafricana pura aclimatada por White Label. Famosa por sus sabores únicos a anís dulce y regaliz, con un efecto claro, activo y energizante ideal para actividades al aire libre.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #854D0E 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Durban White Label Seed Co strain bud"
    }
]

print("Downloading authentic images for expanded White Label Seed Co. catalog...")
for strain in FULL_WLS_CATALOG:
    s_id = strain["id"]
    query = strain["query"]
    out_file = os.path.join(IMG_DIR, f"{s_id}.jpg")
    
    if os.path.exists(out_file) and os.path.getsize(out_file) > 15000 and "official" not in strain["image"]:
        print(f"  Existing image OK for {s_id}")
        continue
    if "official" in strain["image"]:
        print(f"  Official custom image preserved for {s_id}")
        continue
        
    print(f"\nDownloading photo for {s_id} ({query})...")
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
    except Exception as e:
        print(f"  Error: {e}")

print("\nAll White Label photos ready.")
