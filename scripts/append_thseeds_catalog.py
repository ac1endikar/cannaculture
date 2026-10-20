import sys, os, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

new_strains = [
  {
    "id": "ths-french-macaron",
    "image": "img/ths-french-macaron.jpg",
    "name": "French Macaron",
    "aka": "Gelato 33 x French Cookies",
    "bank": "TH Seeds",
    "species": "Hibrida",
    "thc": 24, "cbd": 0.2,
    "yieldIndoor": 550, "yieldOutdoor": 650,
    "floweringDays": 63, "rating": 4.9, "reviewsCount": 1450,
    "genetics": "Gelato 33 x French Cookies",
    "origin": "Ámsterdam / Francia",
    "dominantTerpene": "caryophyllene",
    "terpenes": { "caryophyllene": 45, "limonene": 30, "linalool": 25 },
    "flavors": ["Macaron Dulce", "Gasolina Cremosa", "Noche Francesa"],
    "effects": ["Euforia Sofisticada", "Relajación Dulce", "Bienestar Sensorial"],
    "activities": ["social", "music", "relax_sleep"],
    "description": "Una obra maestra premiada de T.H.Seeds. Cruce estelar entre Gelato 33 y French Cookies. Ofrece un perfil cremoso y dulce a repostería francesa con matices gaseosos. Cogollos morados oscuros y resinosos de potencia extraordinaria.",
    "visualColor": "linear-gradient(135deg, #6B21A8 0%, #1E1B4B 100%)",
    "bgPattern": "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)"
  },
  {
    "id": "ths-banana-candy-krush",
    "image": "img/ths-banana-candy-krush.jpg",
    "name": "Banana Candy Krush",
    "aka": "Banana Cake x Kush Mints",
    "bank": "TH Seeds",
    "species": "Hibrida",
    "thc": 25, "cbd": 0.1,
    "yieldIndoor": 600, "yieldOutdoor": 700,
    "floweringDays": 60, "rating": 4.8, "reviewsCount": 980,
    "genetics": "Banana Cake x Kush Mints",
    "origin": "Ámsterdam, Países Bajos",
    "dominantTerpene": "limonene",
    "terpenes": { "limonene": 40, "myrcene": 35, "caryophyllene": 25 },
    "flavors": ["Plátano Dulce", "Caramelo de Plátano", "Menta Cremosa"],
    "effects": ["Euforia Potente", "Relajación Dulce", "Felicidad Creativa"],
    "activities": ["creativity", "social", "music"],
    "description": "Explosión de sabor a caramelo de plátano cremoso producido por la fusión de Banana Cake y Kush Mints. Produce flores ultra resinosas ideales para extracciones de rosin de nivel competición.",
    "visualColor": "linear-gradient(135deg, #F59E0B 0%, #78350F 100%)",
    "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
    "id": "ths-mont-blanc",
    "image": "img/ths-mont-blanc.jpg",
    "name": "Mont Blanc",
    "aka": "French Cookies x Birthday Cake x Strawbanana Cream",
    "bank": "TH Seeds",
    "species": "Hibrida",
    "thc": 26, "cbd": 0.1,
    "yieldIndoor": 550, "yieldOutdoor": 650,
    "floweringDays": 63, "rating": 4.9, "reviewsCount": 1120,
    "genetics": "French Cookies x Birthday Cake x Strawbanana Cream",
    "origin": "Ámsterdam, Países Bajos",
    "dominantTerpene": "caryophyllene",
    "terpenes": { "caryophyllene": 40, "myrcene": 35, "limonene": 25 },
    "flavors": ["Vainilla Cremosa", "Fresa Glaseada", "Pastel de Cumpleaños"],
    "effects": ["Subidón Nevado", "Euforia Cerebral", "Relajación Profunda"],
    "activities": ["creativity", "relax_sleep"],
    "description": "Nombrada por las famosas montañas del Mont Blanc debido a su capa torrencial de tricomas blancos como la nieve. Un cruce a tres bandas con perfil cremoso a pastel de vainilla y fresa.",
    "visualColor": "linear-gradient(135deg, #E2E8F0 0%, #475569 100%)",
    "bgPattern": "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)"
  },
  {
    "id": "ths-pisthash",
    "image": "img/ths-pisthash.jpg",
    "name": "Pisthash",
    "aka": "Biscotti x French Cookies",
    "bank": "TH Seeds",
    "species": "Hibrida",
    "thc": 24, "cbd": 0.2,
    "yieldIndoor": 500, "yieldOutdoor": 600,
    "floweringDays": 60, "rating": 4.7, "reviewsCount": 840,
    "genetics": "Biscotti x French Cookies",
    "origin": "Ámsterdam, Países Bajos",
    "dominantTerpene": "limonene",
    "terpenes": { "limonene": 40, "caryophyllene": 35, "linalool": 25 },
    "flavors": ["Pistacho Dulce", "Nuez Tostada", "Galleta Italiana"],
    "effects": ["Euforia Elegante", "Bienestar Físico", "Calma Mental"],
    "activities": ["social", "nature_walk"],
    "description": "Una cepa única que entrega aromas cremosos y tostados a frutos secos y pistacho verde. Combinación gourmet de Biscotti con French Cookies.",
    "visualColor": "linear-gradient(135deg, #84CC16 0%, #15803D 100%)",
    "bgPattern": "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
    "id": "ths-melonsicle",
    "image": "img/ths-melonsicle.jpg",
    "name": "Melonsicle",
    "aka": "Watermelon x Strawberry Banana x GSC",
    "bank": "TH Seeds",
    "species": "Sativa",
    "thc": 24, "cbd": 0.1,
    "yieldIndoor": 550, "yieldOutdoor": 650,
    "floweringDays": 63, "rating": 4.8, "reviewsCount": 1250,
    "genetics": "Watermelon x Strawberry Banana x GSC",
    "origin": "Ámsterdam, Países Bajos",
    "dominantTerpene": "myrcene",
    "terpenes": { "myrcene": 45, "limonene": 30, "pinene": 25 },
    "flavors": ["Sandía Dulce", "Helado de Fresa", "Fruta Tropical"],
    "effects": ["Euforia Tropical", "Energía Creativa", "Buen Humor"],
    "activities": ["social", "creativity", "nature_walk"],
    "description": "Bomba frutal que sabe a helado de sandía y fresa. Un híbrido con ligera dominancia sativa perfecto para refrescar los días soleados.",
    "visualColor": "linear-gradient(135deg, #EF4444 0%, #10B981 100%)",
    "bgPattern": "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
    "id": "ths-blumosa",
    "image": "img/ths-blumosa.jpg",
    "name": "Blumosa",
    "aka": "Blue Sherbet x Mimosa",
    "bank": "TH Seeds",
    "species": "Hibrida",
    "thc": 23, "cbd": 0.2,
    "yieldIndoor": 500, "yieldOutdoor": 600,
    "floweringDays": 60, "rating": 4.7, "reviewsCount": 670,
    "genetics": "Blue Sherbet x Mimosa",
    "origin": "Ámsterdam, Países Bajos",
    "dominantTerpene": "limonene",
    "terpenes": { "limonene": 45, "myrcene": 30, "pinene": 25 },
    "flavors": ["Arándano Cítrico", "Champán de Naranja", "Sorbete Dulce"],
    "effects": ["Euforia Espumosa", "Energía Solar", "Claridad Mental"],
    "activities": ["social", "creativity"],
    "description": "Maridaje cítrico y afrutado de Blue Sherbet y Mimosa. Produce un humo sedoso con notas a cóctel de frutas tropicales y un efecto estimulante y alegre.",
    "visualColor": "linear-gradient(135deg, #3B82F6 0%, #F59E0B 100%)",
    "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  }
]

added_count = 0
for strain in new_strains:
    s_id = strain["id"]
    if f'id: "{s_id}"' not in text:
        formatted = ",\n  " + json.dumps(strain, indent=4, ensure_ascii=False).replace('\n', '\n  ')
        target = text.rfind("];")
        if target != -1:
            text = text[:target] + formatted + "\n" + text[target:]
            added_count += 1
            print(f"✅ Added {s_id} ({strain['name']}) to data.js")

if added_count > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"\nSaved {added_count} new T.H.Seeds strains to data.js")
