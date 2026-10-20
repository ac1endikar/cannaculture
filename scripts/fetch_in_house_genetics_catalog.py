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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (ioctl; Android) Chrome/120.0.0.0 Safari/537.36'
}

IN_HOUSE_GENETICS_CATALOG = [
    {
        "id": "ihg-slurricane",
        "image": "img/ihg-slurricane.jpg",
        "name": "Slurricane",
        "aka": "Do-Si-Dos x Purple Punch",
        "bank": "In-House Genetics",
        "species": "Indica",
        "thc": 28, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 4200,
        "genetics": "Do-Si-Dos x Purple Punch",
        "origin": "EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "limonene": 25 },
        "flavors": ["Baya Dulce", "Ponche de Uva", "Crema de Masa"],
        "effects": ["Sedación Placentera", "Euforia Cálida", "Relax Corporal Total"],
        "activities": ["relax_sleep", "music", "meditation"],
        "description": "La variedad insignia por excelencia de In-House Genetics. Cruce de Do-Si-Dos con Purple Punch que ha conquistado el mundo entero por sus cogollos bañados en resina escarchada, sabor a mermelada de bayas dulces y una potencia de 28% de THC.",
        "visualColor": "linear-gradient(135deg, #6B21A8 0%, #3B0764 100%)",
        "bgPattern": "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)",
        "query": "Slurricane In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-jelly-breath",
        "image": "img/ihg-jelly-breath.jpg",
        "name": "Jelly Breath",
        "aka": "Mendo Breath x Dosidos",
        "bank": "In-House Genetics",
        "species": "Indica",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 2600,
        "genetics": "Mendo Breath x Dosidos",
        "origin": "EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Mermelada de Bayas", "Vainilla Especiada", "Tierra Kush"],
        "effects": ["Relax Físico Intenso", "Euforia Alegre", "Calma Mental"],
        "activities": ["relax_sleep", "music"],
        "description": "Exquisita variedad rica en tricomas resinosos. Une Mendo Breath con Dosidos para ofrecer un aroma complejo a mermelada de bayas maduras con fondo de galleta de vainilla y especias dulces.",
        "visualColor": "linear-gradient(135deg, #9333EA 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(147,51,234,0.2) 0%, transparent 70%)",
        "query": "Jelly Breath In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-platinum-kush-breath",
        "image": "img/ihg-platinum-kush-breath.jpg",
        "name": "Platinum Kush Breath",
        "aka": "OG Kush Breath x Platinum",
        "bank": "In-House Genetics",
        "species": "Indica",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 2400,
        "genetics": "OG Kush Breath x Platinum",
        "origin": "EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "limonene": 25, "myrcene": 25 },
        "flavors": ["Gasolina OG", "Tierra Húmeda", "Mente Dulce"],
        "effects": ["Golpe Corporal", "Euforia Cerebral", "Descanso Profundo"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Una de las selecciones más potentes de la línea Platinum. Presenta flores densas de color plateado purpúreo cargadas de combustible diésel OG y tierra dulce.",
        "visualColor": "linear-gradient(135deg, #475569 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)",
        "query": "Platinum Kush Breath In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-sugar-cane",
        "image": "img/ihg-sugar-cane.jpg",
        "name": "Sugar Cane",
        "aka": "Platinum x Slurricane",
        "bank": "In-House Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 3100,
        "genetics": "Platinum x Slurricane",
        "origin": "EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 30, "caryophyllene": 25 },
        "flavors": ["Azúcar de Caña", "Uva Dulce", "Gasolina Suave"],
        "effects": ["Euforia Brillante", "Sensación Placentera", "Relax Físico"],
        "activities": ["creativity", "social", "music"],
        "description": "Famosa en redes sociales por producir uno de los retornos de resina más altos del mercado. Cruce directo de Platinum y Slurricane con flores completamente blancas sabor a azúcar dulce de caña y ponche de uva.",
        "visualColor": "linear-gradient(135deg, #E2E8F0 0%, #64748B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)",
        "query": "Sugar Cane In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-tart-pops",
        "image": "img/ihg-tart-pops.jpg",
        "name": "Tart Pops",
        "aka": "Sour Apple x Purple Punch",
        "bank": "In-House Genetics",
        "species": "Hibrida",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 1600,
        "genetics": "Sour Apple x Purple Punch",
        "origin": "EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 30, "caryophyllene": 25 },
        "flavors": ["Manzana Ácida", "Gominola de Uva", "Gas Dulce"],
        "effects": ["Euforia Feliz", "Sensación Placentera", "Relax Corporal"],
        "activities": ["social", "gaming", "music"],
        "description": "Híbrido súper apetecible de Sour Apple con Purple Punch. Desprende un aroma punzante a caramelos ácidos de manzana verde y tartas de mermelada de uva.",
        "visualColor": "linear-gradient(135deg, #84CC16 0%, #7E22CE 100%)",
        "bgPattern": "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)",
        "query": "Tart Pops In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-terple",
        "image": "img/ihg-terple.jpg",
        "name": "Terple",
        "aka": "Tropicana Cookies x Slurricane",
        "bank": "In-House Genetics",
        "species": "Hibrida",
        "thc": 24, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 1900,
        "genetics": "Tropicana Cookies x Slurricane",
        "origin": "EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "myrcene": 25, "caryophyllene": 25 },
        "flavors": ["Naranja Sangre", "Uva Dulce", "Masa de Galleta"],
        "effects": ["Euforia Creativa", "Energía Radiante", "Bienestar Físico"],
        "activities": ["social", "creativity", "nature_walk"],
        "description": "Obra de arte púrpura con aroma concentrado a zumo de naranja sangre recién exprimido mezclado con el dulzor berry de Slurricane. Espectacular perfil terpénico cítrico.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #9333EA 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Terple In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-black-cherry-pie",
        "image": "img/ihg-black-cherry-pie.jpg",
        "name": "Black Cherry Pie",
        "aka": "Blackberry x Cherry Pie",
        "bank": "In-House Genetics",
        "species": "Indica",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 1450,
        "genetics": "Blackberry x Cherry Pie",
        "origin": "EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "limonene": 25 },
        "flavors": ["Cereza Negra", "Pastel de Frutas", "Tierra Especiada"],
        "effects": ["Relax Corporal Suave", "Calma Mental", "Bienestar Placentero"],
        "activities": ["relax_sleep", "music"],
        "description": "Una delicia frutal caracterizada por sus cálices oscuros de tono cereza negra y un humo denso con aroma a tarta de cerezas recién horneada y frutos del bosque.",
        "visualColor": "linear-gradient(135deg, #991B1B 0%, #450A0A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(153,27,27,0.2) 0%, transparent 70%)",
        "query": "Black Cherry Pie In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-dolato",
        "image": "img/ihg-dolato.jpg",
        "name": "Dolato",
        "aka": "Do-Si-Dos x Gelato #33",
        "bank": "In-House Genetics",
        "species": "Indica",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2100,
        "genetics": "Do-Si-Dos x Gelato #33",
        "origin": "EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Helado Creado", "Pino Dulce", "Tierra Kush"],
        "effects": ["Sedación Corporal", "Paz Mental", "Descanso"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Matrimonio perfecto entre la potencia terrosa de Do-Si-Dos y el aroma a helado de Gelato #33. Cogollos apretados como diamantes con tricomas blancos y tonos verde menta.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Dolato In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-trichome-storm",
        "image": "img/ihg-trichome-storm.jpg",
        "name": "Trichome Storm",
        "aka": "Slurricane #7 x Platinum",
        "bank": "In-House Genetics",
        "species": "Indica",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 1700,
        "genetics": "Slurricane #7 x Platinum",
        "origin": "EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 30, "limonene": 25 },
        "flavors": ["Gasolina Dulce", "Uva Plata", "Kush Terroso"],
        "effects": ["Tormenta de Relax", "Euforia Placentera", "Sueño Profundo"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Nombrada 'Trichome Storm' por la avalancha imparable de resina que cubre sus flores de arriba a abajo. Aroma ultraintenso a diésel dulce, uvas congeladas y kush picante.",
        "visualColor": "linear-gradient(135deg, #38BDF8 0%, #1E293B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(56,189,248,0.2) 0%, transparent 70%)",
        "query": "Trichome Storm In-House Genetics strain flower bud"
    },
    {
        "id": "ihg-smackz",
        "image": "img/ihg-smackz.jpg",
        "name": "Smackz",
        "aka": "Runtz x Sol Sonic",
        "bank": "In-House Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1300,
        "genetics": "Runtz x Sol Sonic",
        "origin": "EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "flavors": ["Gominola Frutal", "Gas Combustible", "Cítrico Dulce"],
        "effects": ["Euforia Estallido", "Energía Social", "Relax Muscular"],
        "activities": ["social", "gaming", "music"],
        "description": "Potente híbrido goloso que une el perfil acaramelado de Runtz con la fuerza terpénica de Sol Sonic. Cogollos púrpura muy resinosos sabor a golosina de frutas y gas.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #A855F7 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Smackz In-House Genetics strain flower bud"
    }
]

print("Downloading authentic flower images for In-House Genetics catalog...")
for strain in IN_HOUSE_GENETICS_CATALOG:
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

print("\nAll In-House Genetics photos ready.")
