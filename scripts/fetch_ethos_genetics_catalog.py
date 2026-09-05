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

ETHOS_GENETICS_CATALOG = [
    {
        "id": "eth-mandarin-cookies",
        "image": "img/eth-mandarin-cookies.jpg",
        "name": "Mandarin Cookies",
        "aka": "Forum Cut GSC x Mandarin Sunset",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 3800,
        "genetics": "Forum Cut GSC x Mandarin Sunset",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "caryophyllene": 25, "myrcene": 25 },
        "flavors": ["Mandarina Jugosa", "Masa de Galleta", "Gas Diésel"],
        "effects": ["Euforia Cerebral", "Energía Radiante", "Relax Corporal"],
        "activities": ["social", "creativity", "nature_walk"],
        "description": "La variedad insignia indiscutible de Ethos Genetics desarrollada por Colin Gordon. Combina la fuerza resinosa de Forum GSC con el aroma cítrico arrollador de Mandarin Sunset. Flores moradas y anaranjadas cubiertas de cristal.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Mandarin Cookies Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-grandpas-cookies",
        "image": "img/eth-grandpas-cookies.jpg",
        "name": "Grandpa's Cookies",
        "aka": "Grandpa's Stash x Cookies & Cream",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2700,
        "genetics": "Grandpa's Stash x Cookies & Cream",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Galleta de Nuez", "Crema Dulce", "Sándalo Viejo"],
        "effects": ["Relax Físico Profundo", "Euforia Contemplativa", "Calma Total"],
        "activities": ["relax_sleep", "music", "meditation"],
        "description": "Híbrido de gran potencia que combina genética añeja de Grandpa's Stash con Cookies & Cream. Desprende un aroma muy reconfortante a galletas caseras de nuez horneada y madera noble.",
        "visualColor": "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
        "bgPattern": "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)",
        "query": "Grandpas Cookies Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-lilac-diesel",
        "image": "img/eth-lilac-diesel.jpg",
        "name": "Lilac Diesel",
        "aka": "SLH x Forbidden Fruit x NYC Diesel x Cherry Pie",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 25, "cbd": 0.3,
        "yieldIndoor": 600, "yieldOutdoor": 750,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 2900,
        "genetics": "(SLH x Forbidden Fruit) x (NYC Diesel x Cherry Pie)",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "caryophyllene": 30, "pinene": 25 },
        "flavors": ["Flores de Lila", "Gasolina Diésel", "Pino Cítrico"],
        "effects": ["Euforia Estallido", "Creatividad Fluyente", "Energía Mental"],
        "activities": ["social", "creativity", "workout"],
        "description": "Una auténtica sinfonía terpenosa a cuatro bandas. Fusiona matices florales a lila silvestre con el perfume punzante de gasolina diésel, pino dulce y frutas tropicales.",
        "visualColor": "linear-gradient(135deg, #C084FC 0%, #7E22CE 100%)",
        "bgPattern": "radial-gradient(circle, rgba(192,132,252,0.2) 0%, transparent 70%)",
        "query": "Lilac Diesel Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-cherry-gar-see-ya",
        "image": "img/eth-cherry-gar-see-ya.jpg",
        "name": "Cherry Gar-See-Ya",
        "aka": "Black Cherry Soda x Cherry Maduro x Mandarin Sunset",
        "bank": "Ethos Genetics",
        "species": "Indica",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 2100,
        "genetics": "(Black Cherry Soda x Cherry Maduro) x Mandarin Sunset",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 25, "limonene": 25 },
        "flavors": ["Cereza Madura", "Gasolina Dulce", "Cítrico Tropical"],
        "effects": ["Relax Corporal", "Dicha Cerebral", "Sensación Cálida"],
        "activities": ["relax_sleep", "music"],
        "description": "Variedad irresistible bautizada en honor al clásico sabor de helado. Ofrece un perfil goloso a cerezas negras maduras mezcladas con toques cítricos de mandarina y gas diésel.",
        "visualColor": "linear-gradient(135deg, #BE123C 0%, #881337 100%)",
        "bgPattern": "radial-gradient(circle, rgba(190,18,60,0.2) 0%, transparent 70%)",
        "query": "Cherry Gar See Ya Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-planet-of-the-grapes",
        "image": "img/eth-planet-of-the-grapes.jpg",
        "name": "Planet of the Grapes",
        "aka": "Grape Diamonds x Chem D Cookies",
        "bank": "Ethos Genetics",
        "species": "Indica",
        "thc": 28, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 5.0, "reviewsCount": 2400,
        "genetics": "Grape Diamonds x Chem D Cookies",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "limonene": 25 },
        "flavors": ["Uva Madura", "Gasolina Química", "Kush Terroso"],
        "effects": ["Sedación Devastadora", "Euforia Placentera", "Relax Total"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Una de las variedades más potentes de todo el catálogo de Ethos alcanzando el 28% de THC. Flores moradas ultraintensas con aroma a mermelada de uva recién hecha y diésel químico.",
        "visualColor": "linear-gradient(135deg, #581C87 0%, #3B0764 100%)",
        "bgPattern": "radial-gradient(circle, rgba(88,28,135,0.2) 0%, transparent 70%)",
        "query": "Planet of the Grapes Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-apex",
        "image": "img/eth-apex.jpg",
        "name": "Apex",
        "aka": "Mandarin Cookies x Lilac Diesel",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 27, "cbd": 0.2,
        "yieldIndoor": 600, "yieldOutdoor": 700,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1800,
        "genetics": "Mandarin Cookies x Lilac Diesel",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "terpinolene": 30, "caryophyllene": 25 },
        "flavors": ["Mandarina Ácida", "Flores de Lila", "Gas Diésel"],
        "effects": ["Euforia Masiva", "Energía Mental", "Relax Corporal"],
        "activities": ["social", "creativity", "gaming"],
        "description": "Híbrido de producción astronómica fruto del cruce de dos de las mejores cepas de Colin: Mandarin Cookies y Lilac Diesel. Flores enormes cargadas de cálices violeta y aroma cítrico floral.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #6366F1 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Apex Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-candy-store",
        "image": "img/eth-candy-store.jpg",
        "name": "Candy Store",
        "aka": "Lemon Berry Candy OG x Ethos Cookies",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 1950,
        "genetics": "Lemon Berry Candy OG x Ethos Cookies",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "myrcene": 25, "caryophyllene": 25 },
        "flavors": ["Caramelo de Limón", "Fresa Silvestre", "Gas Dulce"],
        "effects": ["Euforia Risueña", "Sensación Placentera", "Relax Físico"],
        "activities": ["social", "music", "gaming"],
        "description": "Un auténtico escaparate de golosinas. Junta el perfil cítrico agridulce de Lemon Berry Candy OG con la resina acristalada de Ethos Cookies. Desprende un aroma muy intenso a gominolas de limón y fresa.",
        "visualColor": "linear-gradient(135deg, #FACC15 0%, #EC4899 100%)",
        "bgPattern": "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)",
        "query": "Candy Store Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-member-berry",
        "image": "img/eth-member-berry.jpg",
        "name": "Member Berry",
        "aka": "Skunkberry x Mandarin Sunset",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 24, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 2200,
        "genetics": "Skunkberry x Mandarin Sunset",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "limonene": 30, "caryophyllene": 20 },
        "flavors": ["Arándano Dulce", "Cítrico Skunk", "Fruta Madura"],
        "effects": ["Euforia Nostálgica", "Bienestar Físico", "Calma Risueña"],
        "activities": ["social", "music"],
        "description": "Celebrada cepa con un sabor dulcísimo a tarta de arándanos frescos y cítricos. Sus plantas crecen con gran vigor ofreciendo cosechas de flores densas y tricomas aromáticos.",
        "visualColor": "linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%)",
        "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)",
        "query": "Member Berry Ethos Genetics strain flower bud"
    },
    {
        "id": "eth-ethos-cookies",
        "image": "img/eth-ethos-cookies.jpg",
        "name": "Ethos Cookies",
        "aka": "Mandarin Cookies x Colin OG",
        "bank": "Ethos Genetics",
        "species": "Hibrida",
        "thc": 26, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 1750,
        "genetics": "Mandarin Cookies x Colin OG",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Masa de Galleta", "Gasolina OG", "Naranja Dulce"],
        "effects": ["Euforia Potente", "Relax Corporal", "Claridad Mental"],
        "activities": ["social", "creativity", "music"],
        "description": "Selección de bandera de la línea Cookies de Ethos. Combina la explosión de mandarinas de Mandarin Cookies con la contundencia terrosa y diésel de Colin OG.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Ethos Cookies strain flower bud"
    },
    {
        "id": "eth-colin-og",
        "image": "img/eth-colin-og.jpg",
        "name": "Colin OG",
        "aka": "Grateful Dawg x Alpha Dawg",
        "bank": "Ethos Genetics",
        "species": "Indica",
        "thc": 27, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1600,
        "genetics": "Grateful Dawg x Alpha Dawg",
        "origin": "Colorado, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "myrcene": 30, "limonene": 20 },
        "flavors": ["Gas Combustible", "Pino Picante", "Tierra Kush"],
        "effects": ["Sedación Knockout", "Euforia Pesada", "Relax Profundo"],
        "activities": ["relax_sleep", "meditation"],
        "description": "La creación personal de Colin Gordon. Un híbrido OG masivo caracterizado por su aroma a gasolina pura, pino punzante y un pegadón corporal demoledor.",
        "visualColor": "linear-gradient(135deg, #1E293B 0%, #334155 100%)",
        "bgPattern": "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)",
        "query": "Colin OG Ethos Genetics strain flower bud"
    }
]

print("Downloading authentic flower images for Ethos Genetics catalog...")
for strain in ETHOS_GENETICS_CATALOG:
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

print("\nAll Ethos Genetics photos ready.")
