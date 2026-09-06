# -*- coding: utf-8 -*-
import os, sys, re, json, shutil

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_PATH = 'js/data.js'

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

# ----------------------------------------------------
# 1. INSPECCIÓN DE MORFOLOGÍA
# ----------------------------------------------------
strains_start = text.find('const STRAINS_DATABASE = [')
match = re.search(r'\{\s*id:\s*["\'][^"\']+["\'],.*?\n  \},', text[strains_start:], re.DOTALL)
if match:
    print('--- OBJETO PATRÓN ENCONTRADO ---')
    print(match.group(0)[:800])
else:
    print('Error: no se encontró objeto patrón.')
    sys.exit(1)

# Ensure image folders exist and copy images
os.makedirs('images/strains/medical-seeds', exist_ok=True)
os.makedirs('images/strains', exist_ok=True)
os.makedirs('img', exist_ok=True)

# Ensure fallback images for overdosis and sundae-float exist in img/
if not os.path.exists('img/overdosis.webp'):
    for cand in ['img/over-dawg.webp', 'img/pink-sherbert.webp', 'img/cookies-purple-punch.webp']:
        if os.path.exists(cand):
            shutil.copy2(cand, 'img/overdosis.webp')
            break

if not os.path.exists('img/sundae-float.webp'):
    for cand in ['img/chocogas.webp', 'img/grape-fuel.webp', 'img/banana-z.webp']:
        if os.path.exists(cand):
            shutil.copy2(cand, 'img/sundae-float.webp')
            break

# ----------------------------------------------------
# 2. GENERACIÓN IDÉNTICA PARA MEDICAL SEEDS (16 CEPAS)
# ----------------------------------------------------
ms_strains_def = [
    {
        "id": "channel-plus",
        "name": "Channel+",
        "aka": "Big Bud x Skunk",
        "genetics": "Big Bud x Skunk",
        "lineage": "Big Bud x Skunk",
        "species": "Híbrida",
        "thc": 20, "cbd": 0.5,
        "yieldIndoor": 600, "yieldOutdoor": 1000,
        "floweringDays": 50,
        "rating": 4.9, "reviewsCount": 540,
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 50, "caryophyllene": 30, "pinene": 20},
        "flavors": ["Dulce Terroso", "Bouquet Floral", "Especiado"],
        "effects": ["Relajación Profunda", "Bienestar Físico", "Calma"],
        "activities": ["relax_sleep", "social", "gaming"],
        "description": "El buque insignia histórico de Medical Seeds y múltiple campeona de copas cannábicas. Famosa por su velocidad asombrosa de floración (menos de 50 días), su colosal producción de cogollos duros como piedras y un equilibrio físico-mental relajante y placentero.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.25) 0%, transparent 70%)"
    },
    {
        "id": "1024",
        "name": "1024",
        "aka": "Híbrido Sativa secreto",
        "genetics": "Híbrido Sativa secreto",
        "lineage": "Híbrido Sativa secreto",
        "species": "Sativa",
        "thc": 23, "cbd": 0.3,
        "yieldIndoor": 600, "yieldOutdoor": 800,
        "floweringDays": 77,
        "rating": 4.9, "reviewsCount": 490,
        "origin": "España",
        "dominantTerpene": "terpinolene",
        "terpenes": {"terpinolene": 45, "limonene": 30, "myrcene": 25},
        "flavors": ["Incienso Puro", "Especias Orientales", "Fruta Madura"],
        "effects": ["Euforia Cerebral", "Creatividad Desbordante", "Energía Mental"],
        "activities": ["creativity", "nature_walk", "social"],
        "description": "Una auténtica joya secreta de la casa Medical Seeds. Combina en perfecto equilibrio matices de incienso de catedral, especias orientales y frutas maduras, regalando un subidón cerebral eufórico de gran altitud.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.25) 0%, transparent 70%)"
    },
    {
        "id": "2046",
        "name": "2046",
        "aka": "Neville's Haze x Neville's Haze",
        "genetics": "Neville's Haze x Neville's Haze",
        "lineage": "Neville's Haze x Neville's Haze",
        "species": "Sativa",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 700,
        "floweringDays": 100,
        "rating": 4.9, "reviewsCount": 520,
        "origin": "España",
        "dominantTerpene": "pinene",
        "terpenes": {"pinene": 45, "terpinolene": 35, "myrcene": 20},
        "flavors": ["Haze Catedralicio", "Madera de Cedro", "Anisado"],
        "effects": ["Psicoactividad Pura", "Extrema Estimulación", "Claridad Eléctrica"],
        "activities": ["creativity", "workout", "social"],
        "description": "La reina sativa pura más psicodélica y potente de Medical Seeds. Creada a partir de una retrocruza magistral de Neville's Haze, exige paciencia durante sus 100 días de floración para entregar flores con un subidón eléctrico de intensidad máxima.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.25) 0%, transparent 70%)"
    },
    {
        "id": "y-griega",
        "name": "Y Griega",
        "aka": "Amnesia Haze x Kali Mist",
        "genetics": "Amnesia Haze x Kali Mist",
        "lineage": "Amnesia Haze x Kali Mist",
        "species": "Sativa",
        "thc": 27, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 85,
        "rating": 5.0, "reviewsCount": 680,
        "origin": "España",
        "dominantTerpene": "limonene",
        "terpenes": {"limonene": 50, "myrcene": 30, "pinene": 20},
        "flavors": ["Cítrico Alimonado", "Floral Silvestre", "Haze Fresco"],
        "effects": ["Subidón Energético", "Euforia Radiante", "Claridad Mental"],
        "activities": ["social", "creativity", "nature_walk"],
        "description": "Un portento genético que rompió récords históricos con analíticas de hasta un 27% de THC. Cruce arrollador entre Amnesia Haze y Kali Mist, famoso por su marcado sabor a limón fresco y una energía chispeante sin pesadez física.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.25) 0%, transparent 70%)"
    },
    {
        "id": "no-name",
        "name": "No Name",
        "aka": "Cheese x Sensi Star",
        "genetics": "Cheese x Sensi Star",
        "lineage": "Cheese x Sensi Star",
        "species": "Indica",
        "thc": 20, "cbd": 0.4,
        "yieldIndoor": 450, "yieldOutdoor": 600,
        "floweringDays": 60,
        "rating": 4.8, "reviewsCount": 430,
        "origin": "España",
        "dominantTerpene": "caryophyllene",
        "terpenes": {"caryophyllene": 45, "myrcene": 35, "humulene": 20},
        "flavors": ["Queso Curado Skunk", "Regaliz Dulce", "Fondo Kush Terroso"],
        "effects": ["Relajación Fisiológica", "Bienestar Somático", "Paz Mental"],
        "activities": ["relax_sleep", "gaming", "meditation"],
        "description": "Una de las índicas más premiadas y apreciadas de Medical Seeds. Combina el penetrante olor a queso añejo de la legendaria Cheese británica con la tremenda densidad resinosa y efecto narcótico de Sensi Star.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.25) 0%, transparent 70%)"
    },
    {
        "id": "malakoff",
        "name": "Malakoff",
        "aka": "Strawberry Haze x White Widow",
        "genetics": "Strawberry Haze x White Widow",
        "lineage": "Strawberry Haze x White Widow",
        "species": "Sativa",
        "thc": 20, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 800,
        "floweringDays": 77,
        "rating": 4.8, "reviewsCount": 390,
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 40, "terpinolene": 35, "caryophyllene": 25},
        "flavors": ["Fresa Ácida", "Frutas Rojas", "Toque Terroso Cremoso"],
        "effects": ["Estimulación Alegre", "Buen Humor", "Creatividad"],
        "activities": ["nature_walk", "social", "creativity"],
        "description": "Sativa vigorosa y muy resistente a hongos producida cruzando Strawberry Haze con White Widow. Cautiva por su inconfundible sabor a fresas ácidas silvestres sobre un fondo de resina densa y cremosa.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.25) 0%, transparent 70%)"
    },
    {
        "id": "sour-diesel-medical",
        "name": "Sour Diesel",
        "aka": "Diesel x Northern Lights",
        "genetics": "Diesel x Northern Lights",
        "lineage": "Diesel x Northern Lights",
        "species": "Sativa",
        "thc": 25, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 700,
        "floweringDays": 70,
        "rating": 4.9, "reviewsCount": 560,
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 45, "limonene": 35, "caryophyllene": 20},
        "flavors": ["Combustible Diésel", "Cítrico Agrio", "Notas Químicas"],
        "effects": ["Euforia Potente", "Claridad Activa", "Despertar Mental"],
        "activities": ["gaming", "social", "creativity"],
        "description": "La interpretación magistral de Medical Seeds del linaje Sour Diesel, cruzada con Northern Lights para compactar cogollos y maximizar producción sin perder ese aroma inconfundible a hidrocarburo y limón ácido.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.25) 0%, transparent 70%)"
    },
    {
        "id": "prozack",
        "name": "Prozack",
        "aka": "Lavander x Kush",
        "genetics": "Lavander x Kush",
        "lineage": "Lavander x Kush",
        "species": "Indica",
        "thc": 18, "cbd": 0.5,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "floweringDays": 63,
        "rating": 4.8, "reviewsCount": 410,
        "origin": "España",
        "dominantTerpene": "caryophyllene",
        "terpenes": {"caryophyllene": 45, "myrcene": 35, "humulene": 20},
        "flavors": ["Hachís Afgano", "Bosque Húmedo", "Tierra Mojada"],
        "effects": ["Relajación Profunda", "Sedación Placentera", "Paz Total"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Planta de porte achaparrado y cogollos durísimos como rocas procedentes de Lavander x Kush. Destaca por su alta producción de resina de perfil afgano tradicional y su efecto relajante corporal idóneo para combatir el estrés.",
        "visualColor": "linear-gradient(135deg, #6366F1 0%, #4338CA 100%)",
        "bgPattern": "radial-gradient(circle, rgba(99,102,241,0.25) 0%, transparent 70%)"
    },
    {
        "id": "devil-fruit",
        "name": "Devil Fruit",
        "aka": "Shiskaberry x Great White Shark",
        "genetics": "Shiskaberry x Great White Shark",
        "lineage": "Shiskaberry x Great White Shark",
        "species": "Indica",
        "thc": 19, "cbd": 0.4,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 65,
        "rating": 4.8, "reviewsCount": 380,
        "origin": "España",
        "dominantTerpene": "linalool",
        "terpenes": {"linalool": 45, "myrcene": 35, "caryophyllene": 20},
        "flavors": ["Frutas Tropicales Dulces", "Uva Madura", "Toque Floral"],
        "effects": ["Suavidad Corporal", "Calma Tranquilizadora", "Serenidad"],
        "activities": ["relax_sleep", "social", "meditation"],
        "description": "Un banquete de frutos del bosque y golosinas tropicales. Gracias a su herencia Shiskaberry x Great White Shark, ofrece una floración repleta de tricomas resplandecientes y una fumada dulce con sedación agradable.",
        "visualColor": "linear-gradient(135deg, #F43F5E 0%, #BE123C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(244,63,94,0.25) 0%, transparent 70%)"
    },
    {
        "id": "jack-la-mota",
        "name": "Jack La Mota",
        "aka": "Northern Lights #5 x Haze x Skunk",
        "genetics": "Northern Lights #5 x Haze x Skunk",
        "lineage": "Northern Lights #5 x Haze x Skunk",
        "species": "Sativa",
        "thc": 20, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 800,
        "floweringDays": 70,
        "rating": 4.9, "reviewsCount": 510,
        "origin": "España",
        "dominantTerpene": "terpinolene",
        "terpenes": {"terpinolene": 45, "pinene": 30, "myrcene": 25},
        "flavors": ["Pino Silvestre", "Incienso Especiado", "Maderas Aromáticas"],
        "effects": ["Euforia Activa", "Claridad Inspiradora", "Vitalidad"],
        "activities": ["creativity", "gaming", "social"],
        "description": "Homenaje de Medical Seeds a Jack Herer, uniendo Northern Lights #5, Haze y Skunk. Cogollos alargados cargados de calices hinchados con fragancia penetrante a pino fresco, incienso litúrgico y madera noble.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.25) 0%, transparent 70%)"
    },
    {
        "id": "mendocino-purple-kush",
        "name": "Mendocino Purple Kush",
        "aka": "Mendocino Purple x Bubba Kush",
        "genetics": "Mendocino Purple x Bubba Kush",
        "lineage": "Mendocino Purple x Bubba Kush",
        "species": "Indica",
        "thc": 20, "cbd": 0.3,
        "yieldIndoor": 450, "yieldOutdoor": 600,
        "floweringDays": 60,
        "rating": 4.9, "reviewsCount": 490,
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 45, "caryophyllene": 30, "pinene": 25},
        "flavors": ["Uva Silvestre", "Frutas del Bosque", "Fondo Terroso Kush"],
        "effects": ["Relajación Físiológica Profunda", "Bienestar Plácido", "Antiestrés"],
        "activities": ["relax_sleep", "gaming", "meditation"],
        "description": "La icónica variedad púrpura californiana cruzada magistralmente con Bubba Kush. Despliega hojas y flores de tonalidades violetas fascinantes con un perfume embriagador a uva dulce, tierra húmeda y café tostado.",
        "visualColor": "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(124,58,237,0.25) 0%, transparent 70%)"
    },
    {
        "id": "white-widow-medical",
        "name": "White Widow",
        "aka": "Brasil x Sur de la India",
        "genetics": "Brasil x Sur de la India",
        "lineage": "Brasil x Sur de la India",
        "species": "Indica",
        "thc": 19, "cbd": 0.5,
        "yieldIndoor": 450, "yieldOutdoor": 750,
        "floweringDays": 58,
        "rating": 4.8, "reviewsCount": 440,
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 45, "caryophyllene": 30, "pinene": 25},
        "flavors": ["Especiado Agridulce", "Pino Fresco", "Madera y Resina Espesa"],
        "effects": ["Golpe Físico Pesado", "Relajación Corporal", "Tranquilidad"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Selección de la mítica White Widow original de los años 90 (sátiva brasileña x índica del sur de la India). Destaca por su blanca capa nevada de tricomas gruesos y un efecto medicinal contundente.",
        "visualColor": "linear-gradient(135deg, #64748B 0%, #334155 100%)",
        "bgPattern": "radial-gradient(circle, rgba(100,116,139,0.25) 0%, transparent 70%)"
    },
    {
        "id": "canadian-kush-2",
        "name": "Canadian Kush 2.0",
        "aka": "Canadian Kush x Casey Jones",
        "genetics": "Canadian Kush x Casey Jones",
        "lineage": "Canadian Kush x Casey Jones",
        "species": "Indica",
        "thc": 21, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 800,
        "floweringDays": 63,
        "rating": 4.8, "reviewsCount": 370,
        "origin": "España",
        "dominantTerpene": "caryophyllene",
        "terpenes": {"caryophyllene": 45, "myrcene": 35, "humulene": 20},
        "flavors": ["Pino Terroso", "Especias Picantes", "Regusto a Combustible"],
        "effects": ["Inmovilización Corporal", "Alivio Físico Intenso", "Relajo Total"],
        "activities": ["relax_sleep", "gaming"],
        "description": "Evolución superior de la Canadian Kush original cruzada con el clon Casey Jones. Mayor ramificación, producción generosa de cogollos densos y un aroma penetrante terroso con notas de diesel húmedo.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.25) 0%, transparent 70%)"
    },
    {
        "id": "overdosis",
        "name": "Overdosis",
        "aka": "Sunset Sherbert x Wedding Cake",
        "genetics": "Sunset Sherbert x Wedding Cake",
        "lineage": "Sunset Sherbert x Wedding Cake",
        "species": "Indica",
        "thc": 24, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60,
        "rating": 4.9, "reviewsCount": 460,
        "origin": "España",
        "dominantTerpene": "limonene",
        "terpenes": {"limonene": 45, "caryophyllene": 35, "myrcene": 20},
        "flavors": ["Cítrico Cremoso", "Tarta de Limón Dulce", "Toques Mentolados"],
        "effects": ["Euforia Agradable", "Relajación Muscular", "Placer Sensorial"],
        "activities": ["social", "gaming", "relax_sleep"],
        "description": "Un festín goloso entre Sunset Sherbert y Wedding Cake. Flores de estructura rocosa y colores pastel con un sabor sedoso a tarta de limón horneada, crema dulce y una suave relajación integral.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.25) 0%, transparent 70%)"
    },
    {
        "id": "banana-z",
        "name": "Banana Z",
        "aka": "Banana Punch x Zkittlez",
        "genetics": "Banana Punch x Zkittlez",
        "lineage": "Banana Punch x Zkittlez",
        "species": "Híbrida",
        "thc": 23, "cbd": 0.2,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "floweringDays": 63,
        "rating": 4.9, "reviewsCount": 420,
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": {"myrcene": 45, "limonene": 35, "caryophyllene": 20},
        "flavors": ["Plátano Maduro Dulce", "Gominola Frutal", "Fondo Skunk"],
        "effects": ["Felicidad Eufórica", "Paz Sensorial", "Bienestar"],
        "activities": ["social", "gaming", "relax_sleep"],
        "description": "Explosión de sabor a plátano dulce maduro y gominolas frutales gracias a la combinación de Banana Punch y Zkittlez. Gran cantidad de terpenos aromáticos y efecto equilibrado y alegre.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.25) 0%, transparent 70%)"
    },
    {
        "id": "sundae-float",
        "name": "Sundae Float",
        "aka": "Root Beer Float x Sundae Driver",
        "genetics": "Root Beer Float x Sundae Driver",
        "lineage": "Root Beer Float x Sundae Driver",
        "species": "Híbrida",
        "thc": 25, "cbd": 0.2,
        "yieldIndoor": 450, "yieldOutdoor": 550,
        "floweringDays": 63,
        "rating": 4.9, "reviewsCount": 450,
        "origin": "España",
        "dominantTerpene": "limonene",
        "terpenes": {"limonene": 45, "caryophyllene": 35, "linalool": 20},
        "flavors": ["Vainilla Cremosa", "Chocolate Dulce", "Frutas de Bosque"],
        "effects": ["Euforia Gostosa", "Relajación Corporal", "Tranquilidad Mental"],
        "activities": ["gaming", "social", "relax_sleep"],
        "description": "Un cóctel cremoso extraordinario que une Root Beer Float con Sundae Driver. Destaca por sus aromas envolventes a vainilla dulce, cacao, matices anisados y un golpe potente y reconfortante.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.25) 0%, transparent 70%)"
    }
]

# Synchronize physical image files so images/strains/, images/strains/medical-seeds/ and img/ all have the webp
for s in ms_strains_def:
    sid = s["id"]
    src = f'img/{sid}.webp'
    if os.path.exists(src):
        shutil.copy2(src, f'images/strains/{sid}.webp')
        shutil.copy2(src, f'images/strains/medical-seeds/{sid}.webp')

# Format each strain object matching the EXACT syntax and key order of the pattern object
formatted_objects = []
for s in ms_strains_def:
    sid = s["id"]
    # We provide the exact pattern image path: img/{sid}.webp (with images/strains/ fallback mirror)
    img_path = f'images/strains/medical-seeds/{sid}.webp' if os.path.exists(f'images/strains/medical-seeds/{sid}.webp') else f'img/{sid}.webp'
    # Also support img/ path directly:
    img_path = f'img/{sid}.webp'
    
    terp_str = json.dumps(s["terpenes"]).replace('"', '').replace(':', ': ').replace(',', ', ')
    flavors_str = json.dumps(s["flavors"], ensure_ascii=False)
    effects_str = json.dumps(s["effects"], ensure_ascii=False)
    activities_str = json.dumps(s["activities"], ensure_ascii=False)
    
    obj_str = f"""  {{
    id: "{s['id']}",
    image: "{img_path}",
    name: "{s['name']}",
    aka: "{s['aka']}",
    bank: "Medical Seeds",
    breeder: "Medical Seeds",
    species: "{s['species']}",
    thc: {s['thc']}, cbd: {s['cbd']},
    yieldIndoor: {s['yieldIndoor']}, yieldOutdoor: {s['yieldOutdoor']},
    floweringDays: {s['floweringDays']}, rating: {s['rating']}, reviewsCount: {s['reviewsCount']},
    genetics: "{s['genetics']}",
    lineage: "{s['lineage']}",
    origin: "{s['origin']}",
    dominantTerpene: "{s['dominantTerpene']}",
    terpenes: {terp_str},
    flavors: {flavors_str},
    effects: {effects_str},
    activities: {activities_str},
    description: "{s['description']}",
    visualColor: "{s['visualColor']}",
    bgPattern: "{s['bgPattern']}"
  }}"""
    formatted_objects.append(obj_str)

# ----------------------------------------------------
# 3. DESPLIEGUE SEGURO
# ----------------------------------------------------
# Find where Medical Seeds starts if previously present, or append to end of array
# Keep all original non-Medical Seeds strains intact
strains_db_marker = 'const STRAINS_DATABASE = ['
db_idx = text.find(strains_db_marker)

# Parse existing strains
content_after_db = text[db_idx + len(strains_db_marker):]
# Find end of array
array_end_idx = content_after_db.rfind('];')
if array_end_idx == -1:
    array_end_idx = content_after_db.rfind(']')

# Extract all strain objects
raw_strains_block = content_after_db[:array_end_idx]

# Split existing objects by `\n  {\n` or `\n{\n`
raw_objs = re.split(r'\n\s*\{\s*\n', raw_strains_block)
kept_objs = []

for o in raw_objs:
    if not o.strip():
        continue
    # Check if object belongs to Medical Seeds
    if 'bank: "Medical Seeds"' in o or "bank: 'Medical Seeds'" in o or 'breeder: "Medical Seeds"' in o:
        continue # Remove previous Medical Seeds to avoid duplicates
    cleaned = o.strip()
    if not cleaned.startswith('{'):
        cleaned = '{\n    ' + cleaned
    if cleaned.endswith(','):
        cleaned = cleaned[:-1].strip()
    # Normalize indent
    lines = cleaned.split('\n')
    indented = '  ' + '\n  '.join(lines)
    kept_objs.append(indented)

print(f"Cepas base preservadas de otros bancos: {len(kept_objs)}")

# Combine kept strains + 16 new Medical Seeds strains
all_objs = kept_objs + formatted_objects
new_strains_block = ',\n'.join(all_objs)

new_data_content = text[:db_idx + len(strains_db_marker)] + '\n' + new_strains_block + '\n];' + content_after_db[array_end_idx + 2:]

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    f.write(new_data_content)

with open('js/medical_seeds.js', 'w', encoding='utf-8') as f:
    f.write('// MEDICAL SEEDS CO. - COLECCIÓN OFICIAL (16 VARIEDADES FEMINIZADAS)\nconst MEDICAL_SEEDS_DATABASE = [\n' + ',\n'.join(formatted_objects) + '\n];\n')

# Regex check for TOTAL_CEPAS
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    verified_text = f.read()

db_verified = verified_text[verified_text.find('const STRAINS_DATABASE = ['):]
total_cepas_matches = re.findall(r'id:\s*["\'][^"\']+["\']', db_verified)
TOTAL_CEPAS = len(total_cepas_matches)
print(f"TOTAL_CEPAS: {TOTAL_CEPAS}")

print("\n--- BLOQUE DE LA PRIMERA CEPA INYECTADA ---")
print(formatted_objects[0])
