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

SEEDSMAN_CATALOG = [
    {
        "id": "sdm-peyote-zkittlez",
        "image": "img/sdm-peyote-zkittlez.jpg",
        "name": "Peyote Zkittlez",
        "aka": "Peyote WiFi x Zkittlez",
        "bank": "Seedsman",
        "species": "Indica",
        "thc": 24, "cbd": 0.3,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2400,
        "genetics": "Peyote WiFi x Zkittlez",
        "origin": "Reino Unido / EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Caramelo de Frutas", "Dulce de Uva", "Tierra Kush"],
        "effects": ["Euforia Potente", "Relax Corporal Profundo", "Paz Mental"],
        "activities": ["relax_sleep", "music", "social"],
        "description": "Una de las variedades más populares y potentes de Seedsman. Cruce de Peyote WiFi con Zkittlez que destaca por sus tonos púrpuras oscuros, su explosión de tricomas resinosos y un sabor dulce a caramelos frutales con fondo terroso.",
        "visualColor": "linear-gradient(135deg, #7C3AED 0%, #DB2777 100%)",
        "bgPattern": "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)",
        "query": "Peyote Zkittlez Seedsman strain flower bud"
    },
    {
        "id": "sdm-gelato-og",
        "image": "img/sdm-gelato-og.jpg",
        "name": "Gelato OG",
        "aka": "Gelato #33 x OG Kush",
        "bank": "Seedsman",
        "species": "Hibrida",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 58, "rating": 4.9, "reviewsCount": 2150,
        "genetics": "Gelato #33 x OG Kush",
        "origin": "California / Reino Unido",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "flavors": ["Helado de Cítricos", "Pino Gasolina", "Galleta Dulce"],
        "effects": ["Euforia Cerebral", "Relajación Muscular", "Claridad Alegre"],
        "activities": ["creativity", "social", "music"],
        "description": "Exquisito híbrido de alta potencia que reúne el cremoso sabor a helado de cítricos de Gelato #33 con la fuerza resinosa y el regusto a gasolina de OG Kush. Subidón intenso y estimulante.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Gelato OG Seedsman strain flower bud"
    },
    {
        "id": "sdm-peyote-cookies",
        "image": "img/sdm-peyote-cookies.jpg",
        "name": "Peyote Cookies",
        "aka": "Peyote Purple x Cookies Kush",
        "bank": "Seedsman",
        "species": "Indica",
        "thc": 22, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 55, "rating": 4.8, "reviewsCount": 1800,
        "genetics": "Peyote Purple x Cookies Kush",
        "origin": "Reino Unido",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "limonene": 25 },
        "flavors": ["Guayaba Dulce", "Vainilla Dulce", "Tierra Especiada"],
        "effects": ["Sedación Corporal", "Bienestar Cálido", "Sueño Reparador"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Híbrido de impactante belleza visual con matices púrpuras y rubí. Desprende un aroma tropical dulce que recuerda a guayaba dulce y galletas con vainilla. Efecto indica relajante y placentero.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Peyote Cookies Seedsman strain flower bud"
    },
    {
        "id": "sdm-mama-thai",
        "image": "img/sdm-mama-thai.jpg",
        "name": "Mama Thai",
        "aka": "Pure Thai Landrace Selection",
        "bank": "Seedsman",
        "species": "Sativa",
        "thc": 22, "cbd": 0.2,
        "yieldIndoor": 450, "yieldOutdoor": 600,
        "floweringDays": 77, "rating": 4.7, "reviewsCount": 1100,
        "genetics": "Thai Landrace Selection",
        "origin": "Tailandia / Reino Unido",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 50, "myrcene": 25, "pinene": 25 },
        "flavors": ["Pimienta Cítrica", "Limón Silvestre", "Madera Exótica"],
        "effects": ["Energía Eléctrica", "Euforia Cerebral", "Claridad Activa"],
        "activities": ["workout", "nature_walk", "creativity"],
        "description": "Una de las pocas sativas puras tailandesas aclimatadas con éxito para cultivos de interior y exterior. Produce cogollos aéreos cargados de resina picante con sabor a limón, madera fina y especias orientales.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Mama Thai Seedsman strain flower bud"
    },
    {
        "id": "sdm-alaskan-purple",
        "image": "img/sdm-alaskan-purple.jpg",
        "name": "Alaskan Purple",
        "aka": "Alaskan Purple x Kush x Brazilian",
        "bank": "Seedsman",
        "species": "Indica",
        "thc": 23, "cbd": 0.3,
        "yieldIndoor": 550, "yieldOutdoor": 700,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1650,
        "genetics": "Alaskan Purple x Kush x Brazilian Sativa",
        "origin": "Alaska / Brasil / Reino Unido",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "limonene": 25 },
        "flavors": ["Bayas Silvestres", "Pino Dulce", "Tierra de Flor"],
        "effects": ["Relajación Muscular", "Euforia Serena", "Bienestar Mental"],
        "activities": ["relax_sleep", "nature_walk"],
        "description": "Variedad gigante de producción masiva caracterizada por sus espectaculares tonalidades moradas y púrpuras. Ofrece un humo suave y muy aromático con notas a bayas silvestres y pino dulce.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Alaskan Purple Seedsman strain flower bud"
    },
    {
        "id": "sdm-bad-azz-cheese",
        "image": "img/sdm-bad-azz-cheese.jpg",
        "name": "Bad Azz Cheese",
        "aka": "Bad Azz Kush x UK Cheese",
        "bank": "Seedsman",
        "species": "Indica",
        "thc": 21, "cbd": 0.5,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.7, "reviewsCount": 980,
        "genetics": "Bad Azz Kush x UK Cheese",
        "origin": "Reino Unido / EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "limonene": 20 },
        "flavors": ["Queso Curado", "Especias Diésel", "Tierra Húmeda"],
        "effects": ["Efecto Risueño", "Relax Físico", "Calma Mente"],
        "activities": ["social", "music", "relax_sleep"],
        "description": "Híbrido muy especial que une el aroma fuerte y picante de la clásica UK Cheese con el toque potente y diésel de Bad Azz Kush. Cogollos densos y muy resinosos.",
        "visualColor": "linear-gradient(135deg, #FACC15 0%, #854D0E 100%)",
        "bgPattern": "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)",
        "query": "Bad Azz Cheese Seedsman strain flower bud"
    },
    {
        "id": "sdm-white-widow",
        "image": "img/sdm-white-widow.jpg",
        "name": "White Widow",
        "aka": "Seedsman White Widow Selection",
        "bank": "Seedsman",
        "species": "Hibrida",
        "thc": 20, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 56, "rating": 4.7, "reviewsCount": 1500,
        "genetics": "Brazilian Sativa x South Indian Indica",
        "origin": "Reino Unido",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "pinene": 25 },
        "flavors": ["Pino Fresco", "Tierra Especiada", "Madera Dulce"],
        "effects": ["Euforia Cerebral", "Relajación Corporal", "Energía Social"],
        "activities": ["social", "creativity"],
        "description": "La versión seleccionada por Seedsman de la célebre White Widow. Famosa por sus plantas uniformes recubiertas por cristales blancos y su aroma fresco a pino y especias.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "White Widow Seedsman strain flower bud"
    },
    {
        "id": "sdm-jack-herer",
        "image": "img/sdm-jack-herer.jpg",
        "name": "Jack Herer",
        "aka": "Seedsman Jack Herer Selection",
        "bank": "Seedsman",
        "species": "Sativa",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 65, "rating": 4.8, "reviewsCount": 1750,
        "genetics": "Haze x Northern Lights #5 x Shiva Skunk",
        "origin": "Reino Unido",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "myrcene": 30, "caryophyllene": 25 },
        "flavors": ["Pino Picante", "Incienso Dulce", "Madera de Cedro"],
        "effects": ["Euforia Cerebral", "Energía Creativa", "Claridad Mental"],
        "activities": ["creativity", "social", "nature_walk"],
        "description": "Selección especial de Jack Herer perfeccionada por Seedsman. Conserva la potencia sativa cerebral con toques a pino fresco, incienso místico y resina especiada.",
        "visualColor": "linear-gradient(135deg, #22C55E 0%, #15803D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)",
        "query": "Jack Herer Seedsman strain flower bud"
    },
    {
        "id": "sdm-amnesia-fast",
        "image": "img/sdm-amnesia-fast.jpg",
        "name": "Amnesia Fast",
        "aka": "Amnesia Haze x Secret Hybrid",
        "bank": "Seedsman",
        "species": "Sativa",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 50, "rating": 4.7, "reviewsCount": 1200,
        "genetics": "Amnesia Haze x Secret Auto Hybrid",
        "origin": "Reino Unido",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Limón Especiado", "Incienso Dulce", "Cítrico Fresco"],
        "effects": ["Euforia Rápida", "Energía Cerebral", "Claridad Mental"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Versión de floración rápida de la famosa Amnesia Haze desarrollada por Seedsman. Recorta el tiempo de floración a sólo 50 días sin perder su característico aroma a incienso cítrico.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Amnesia Fast Seedsman strain flower bud"
    },
    {
        "id": "sdm-blue-blueberry",
        "image": "img/sdm-blue-blueberry.jpg",
        "name": "Blue Blueberry",
        "aka": "Seedsman Blueberry Selection",
        "bank": "Seedsman",
        "species": "Indica",
        "thc": 20, "cbd": 0.4,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "floweringDays": 60, "rating": 4.6, "reviewsCount": 890,
        "genetics": "Original Blueberry Selection",
        "origin": "EEUU / Reino Unido",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "pinene": 25 },
        "flavors": ["Arándano Silvestre", "Mermelada Dulce", "Tierra de Frutas"],
        "effects": ["Relajación Dulce", "Calma Corporal", "Paz Mental"],
        "activities": ["relax_sleep", "music"],
        "description": "Selección refinada de la mítica línea Blueberry. Famosa por sus tonalidades azuladas al final de la floración y su característico aroma a arándanos dulces y mermelada silvestre.",
        "visualColor": "linear-gradient(135deg, #3B82F6 0%, #1E40AF 100%)",
        "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)",
        "query": "Blueberry Seedsman strain flower bud"
    }
]

print("Downloading authentic flower images for Seedsman catalog...")
for strain in SEEDSMAN_CATALOG:
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

print("\nAll Seedsman photos ready.")
