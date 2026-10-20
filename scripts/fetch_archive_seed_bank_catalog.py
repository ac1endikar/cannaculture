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

ARCHIVE_SEED_BANK_CATALOG = [
    {
        "id": "arc-dosidos",
        "image": "img/arc-dosidos.jpg",
        "name": "Dosidos",
        "aka": "OGKB x Face Off OG BX1",
        "bank": "Archive Seed Bank",
        "species": "Indica",
        "thc": 28, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 4500,
        "genetics": "OGKB x Face Off OG BX1",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Menta Furia", "Pino OG", "Tierra Dulce"],
        "effects": ["Euforia Devastadora", "Relax Corporal Total", "Paz Mente"],
        "activities": ["relax_sleep", "music", "meditation"],
        "description": "La creación más célebre en la historia de Archive Seed Bank desarrollada por Fletcher (The Docta). Cruce de OGKB con Face Off OG BX1 que revolucionó el mercado cannábico mundial por su manto de tricomas diamantinos y aroma a menta OG extremadamente potente.",
        "visualColor": "linear-gradient(135deg, #15803D 0%, #166534 100%)",
        "bgPattern": "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)",
        "query": "Dosidos Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-rainbow-belts",
        "image": "img/arc-rainbow-belts.jpg",
        "name": "Rainbow Belts",
        "aka": "Zkittlez x Moonbow #75",
        "bank": "Archive Seed Bank",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 3600,
        "genetics": "Zkittlez x Moonbow #75",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "caryophyllene": 25, "linalool": 25 },
        "flavors": ["Gominola Arcoíris", "Cítrico Dulce", "Gasolina Kush"],
        "effects": ["Euforia Alegre", "Dicha Estallido", "Relax Placentero"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Ganadora de múltiples copas internacionales y aclamada como uno de los mejores híbridos Zkittlez jamás creados. Combina el sabor intenso a golosinas de frutas con el empuje terpénico diésel de Moonbow.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Rainbow Belts Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-moonbow",
        "image": "img/arc-moonbow.jpg",
        "name": "Moonbow",
        "aka": "Zkittlez x Face Off OG",
        "bank": "Archive Seed Bank",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 65, "rating": 4.9, "reviewsCount": 2800,
        "genetics": "Zkittlez x Face Off OG",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Caramelo de Frutas", "Gas Combustible", "Tierra Kush"],
        "effects": ["Euforia Radiante", "Relax Corporal Profundo", "Calma Mental"],
        "activities": ["social", "music", "meditation"],
        "description": "Una verdadera obra maestra moderna. Combina el perfil organoléptico dulcísimo a caramelos de Zkittlez con la fuerza pura y resina pesada del clon Face Off OG.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Moonbow Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-face-off-og",
        "image": "img/arc-face-off-og.jpg",
        "name": "Face Off OG",
        "aka": "Face Off OG IBL",
        "bank": "Archive Seed Bank",
        "species": "Indica",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 3100,
        "genetics": "707 OG Kush Selection",
        "origin": "California / Oregon, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "limonene": 20 },
        "flavors": ["Gasolina Diésel", "Pino Picante", "Tierra Húmeda"],
        "effects": ["Sedación Knockout", "Euforia Pesada", "Relajación Total"],
        "activities": ["relax_sleep", "meditation"],
        "description": "El clon pilar fundamental sobre el que se fundó Archive Seed Bank. Famoso por su efecto 'Face Off' tan potente que produce una sedación corporal aplastante y un aroma punzante a gasolina OG y pino.",
        "visualColor": "linear-gradient(135deg, #1E293B 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)",
        "query": "Face Off OG Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-rudeboi-og",
        "image": "img/arc-rudeboi-og.jpg",
        "name": "RudeBoi OG",
        "aka": "Irene OG x Face Off OG BX1",
        "bank": "Archive Seed Bank",
        "species": "Indica",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 65, "rating": 4.8, "reviewsCount": 1900,
        "genetics": "Irene OG x Face Off OG BX1",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "limonene": 20 },
        "flavors": ["Gasolina Kush", "Pimienta Negra", "Tierra de Bosque"],
        "effects": ["Efecto Corporal Pesado", "Calma Mente", "Sueño Placentero"],
        "activities": ["relax_sleep", "music"],
        "description": "Cruce de la legendaria Irene OG de Atlanta con Face Off OG BX1. Ofrece flores apretadas cargadas de cálices verde oscuro y resina con olor picante a gas pimienta y tierra de bosque.",
        "visualColor": "linear-gradient(135deg, #334155 0%, #1E293B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(51,65,85,0.2) 0%, transparent 70%)",
        "query": "RudeBoi OG Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-valley-girl",
        "image": "img/arc-valley-girl.jpg",
        "name": "Valley Girl",
        "aka": "SFV OG x Face Off OG BX1",
        "bank": "Archive Seed Bank",
        "species": "Indica",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1750,
        "genetics": "SFV OG x Face Off OG BX1",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 30, "caryophyllene": 25 },
        "flavors": ["Limón OG", "Pino Sol", "Tierra Húmeda"],
        "effects": ["Euforia Alegre", "Relax Físico Cálido", "Bienestar"],
        "activities": ["social", "relax_sleep"],
        "description": "Excelente cruce entre la clásica San Fernando Valley OG (SFV OG) y Face Off OG BX1. Brinda un perfume clásico a pino con limón fresco y una resina brillante muy viscosa.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #15803D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Valley Girl Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-dank-dough",
        "image": "img/arc-dank-dough.jpg",
        "name": "Dank Dough",
        "aka": "Gelato #41 x Moonbow #75",
        "bank": "Archive Seed Bank",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 1650,
        "genetics": "Gelato #41 x Moonbow #75",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "flavors": ["Masa de Galleta", "Gasolina Dulce", "Helado Creado"],
        "effects": ["Euforia Cerebral", "Relax Físico", "Dicha Risueña"],
        "activities": ["social", "music", "gaming"],
        "description": "Una delicia gastronómica que combina la potencia cremosa de Gelato #41 con la dulzura acaramelada y a gas de Moonbow #75. Cosechas cargadas de flores púrpura-plata.",
        "visualColor": "linear-gradient(135deg, #7C3AED 0%, #DB2777 100%)",
        "bgPattern": "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)",
        "query": "Dank Dough Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-double-cross",
        "image": "img/arc-double-cross.jpg",
        "name": "Double Cross",
        "aka": "Moonbow #73 x Face Off OG",
        "bank": "Archive Seed Bank",
        "species": "Indica",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1500,
        "genetics": "Moonbow #73 x Face Off OG",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Gas Combustible", "Caramelo de Uva", "Pino Kush"],
        "effects": ["Golpe Corporal Masivo", "Euforia Alegre", "Sueño Profundo"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Potente retrocruce entre Moonbow #73 y Face Off OG. Genera plantas con una cobertura de tricomas exagerada y un aroma denso a combustible diésel y fruta dulce.",
        "visualColor": "linear-gradient(135deg, #475569 0%, #1E1B4B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)",
        "query": "Double Cross Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-memory-loss",
        "image": "img/arc-memory-loss.jpg",
        "name": "Memory Loss",
        "aka": "Amnesia Haze x Face Off OG",
        "bank": "Archive Seed Bank",
        "species": "Sativa",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 70, "rating": 4.8, "reviewsCount": 1850,
        "genetics": "Amnesia Haze x Face Off OG",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "limonene": 30, "caryophyllene": 25 },
        "flavors": ["Limón Especiado", "Gasolina Haze", "Incienso Dulce"],
        "effects": ["Euforia Psicoactiva", "Energía Mental", "Desconexión Total"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Nombrada 'Memory Loss' por su deslumbrante efecto cerebral que hace olvidar las preocupaciones diarias. Une la mítica Amnesia Haze holandesa con la pegada diésel de Face Off OG.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Memory Loss Archive Seed Bank strain flower bud"
    },
    {
        "id": "arc-z-mints",
        "image": "img/arc-z-mints.jpg",
        "name": "Z-Mints",
        "aka": "Zkittlez x SinMint Cookies",
        "bank": "Archive Seed Bank",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1400,
        "genetics": "Zkittlez x SinMint Cookies",
        "origin": "Oregon, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "menthol": 25 },
        "flavors": ["Gominola de Menta", "Caramelo de Frutas", "Tierra Dulce"],
        "effects": ["Euforia Fresca", "Relax Físico", "Sensación Placentera"],
        "activities": ["social", "music", "nature_walk"],
        "description": "Híbrido de sabor súper refrescante que cruza Zkittlez con SinMint Cookies. Produce cogollos ultra duros con aroma a golosinas de fruta con toque de menta fría.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Z Mints Archive Seed Bank strain flower bud"
    }
]

print("Downloading authentic flower images for Archive Seed Bank catalog...")
for strain in ARCHIVE_SEED_BANK_CATALOG:
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

print("\nAll Archive Seed Bank photos ready.")
