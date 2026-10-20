import re, os, sys, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

strains_to_add = [
    {
        "id": "00-kush",
        "name": "00 Kush",
        "aka": "Selección OG Kush",
        "bank": "00 Seeds Bank",
        "breeder": "00 Seeds Bank",
        "species": "Indica",
        "thc": 22, "cbd": 0.3,
        "indicaPct": 80, "sativaPct": 20,
        "floweringDays": 55, "rating": 4.8, "reviewsCount": 380,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "genetics": "Selección OG Kush",
        "lineage": "Selección OG Kush",
        "origin": "España / EE. UU.",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "pinene": 20 },
        "aroma": "Cítrico, terroso con matices a pino",
        "flavors": ["Cítrico Madurado", "Tierra Húmeda", "Pino Fresco"],
        "effects": ["Relajación Muscular", "Calma Profunda", "Alivio Físico"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Selección de OG Kush rápida, compacta y extremadamente resinosa. Aromas cítricos y terrosos con marcados matices a pino y un efecto relajante corporal potente y duradero.",
        "image": "images/strains/00-kush.jpg",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "chocolate-skunk",
        "name": "Chocolate Skunk",
        "aka": "Skunk Mass x Secreta",
        "bank": "00 Seeds Bank",
        "breeder": "00 Seeds Bank",
        "species": "Híbrida",
        "thc": 20, "cbd": 0.4,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 52, "rating": 4.7, "reviewsCount": 420,
        "yieldIndoor": 550, "yieldOutdoor": 700,
        "genetics": "Skunk Mass x Genética Secreta",
        "lineage": "Skunk Mass x Genética Secreta",
        "origin": "España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "limonene": 20 },
        "aroma": "Dulce chocolate, notas a café y fondo skunk",
        "flavors": ["Chocolate Dulce", "Café Tostado", "Skunk Clásico"],
        "effects": ["Euforia Risueña", "Relajación Equilibrada", "Bienestar"],
        "activities": ["social", "gaming", "creativity"],
        "description": "Híbrido de altísima producción y floración ultrarrápida. Desprende un aroma dulce a chocolate con fondo a café tostado y matices skunk penetrantes de gran personalidad.",
        "image": "images/strains/chocolate-skunk.jpg",
        "visualColor": "linear-gradient(135deg, #6D28D9 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
    },
    {
        "id": "gorilla-00",
        "name": "Gorilla",
        "aka": "Gorilla Glue #4 Selection",
        "bank": "00 Seeds Bank",
        "breeder": "00 Seeds Bank",
        "species": "Híbrida",
        "thc": 25, "cbd": 0.2,
        "indicaPct": 55, "sativaPct": 45,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 510,
        "yieldIndoor": 600, "yieldOutdoor": 800,
        "genetics": "Chem Sister x Sour Dubb x Chocolate Diesel",
        "lineage": "Chem Sister x Sour Dubb x Chocolate Diesel",
        "origin": "EE. UU. / España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "limonene": 30, "myrcene": 20 },
        "aroma": "Pino intenso, terroso y combustible diésel",
        "flavors": ["Pino Intenso", "Diésel Combustible", "Tierra Húmeda"],
        "effects": ["Pegada Demoledora", "Euforia Inicial", "Sedación Placentera"],
        "activities": ["relax_sleep", "gaming"],
        "description": "Versión de la mítica Gorilla Glue por 00 Seeds Bank. Concentración de resina salvaje, aromas terrosos y a combustible diésel con un porcentaje demoledor de THC del 25%.",
        "image": "images/strains/gorilla-00.jpg",
        "visualColor": "linear-gradient(135deg, #059669 0%, #064E3B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
    },
    {
        "id": "california-kush",
        "name": "California Kush",
        "aka": "California Indica x Kush",
        "bank": "00 Seeds Bank",
        "breeder": "00 Seeds Bank",
        "species": "Indica",
        "thc": 20, "cbd": 0.3,
        "indicaPct": 75, "sativaPct": 25,
        "floweringDays": 58, "rating": 4.7, "reviewsCount": 360,
        "yieldIndoor": 500, "yieldOutdoor": 650,
        "genetics": "California Indica x Kush",
        "lineage": "California Indica x Kush",
        "origin": "EE. UU. / España",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 30, "myrcene": 25 },
        "aroma": "Cítrico maduro y combustible terroso",
        "flavors": ["Cítrico Maduro", "Combustible Terroso", "Especias"],
        "effects": ["Relajación Corporal", "Tranquilidad Mental", "Sosiego"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Cruce de genética californiana clásica con una robusta índica Kush. Destaca por su aroma a limón dulce madurado al sol y una pegada física reconfortante.",
        "image": "images/strains/california-kush.jpg",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    },
    {
        "id": "sweet-soma",
        "name": "Sweet Soma",
        "aka": "Somango x Indica Selection",
        "bank": "00 Seeds Bank",
        "breeder": "00 Seeds Bank",
        "species": "Indica",
        "thc": 22, "cbd": 0.3,
        "indicaPct": 80, "sativaPct": 20,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 340,
        "yieldIndoor": 450, "yieldOutdoor": 600,
        "genetics": "Somango x Selección Índica",
        "lineage": "Somango x Selección Índica",
        "origin": "España",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "limonene": 30, "caryophyllene": 20 },
        "aroma": "Dulce afrutado, golosinas y frutas de bosque",
        "flavors": ["Frutas del Bosque", "Mango Dulce", "Golosinas"],
        "effects": ["Sedación Dulce", "Desconexión Total", "Paz Física"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Variedad índica compacta y aromática derivada de Somango. Floración dulce y afrutada que recuerda a caramelos de fruta madura con un efecto balsámico corporal.",
        "image": "images/strains/sweet-soma.jpg",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
    },
    {
        "id": "gorilla-girl",
        "name": "Gorilla Girl",
        "aka": "Gorilla Glue x Girl Scout Cookies",
        "bank": "Sweet Seeds",
        "breeder": "Sweet Seeds",
        "species": "Híbrida",
        "thc": 25, "cbd": 0.1,
        "indicaPct": 40, "sativaPct": 60,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 580,
        "yieldIndoor": 550, "yieldOutdoor": 600,
        "genetics": "Gorilla Glue x Girl Scout Cookies",
        "lineage": "Gorilla Glue x Girl Scout Cookies",
        "origin": "España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "limonene": 30, "pinene": 20 },
        "aroma": "Ciprés, madera noble, cítrico terroso",
        "flavors": ["Ciprés Fresco", "Madera Noble", "Cítrico Terroso"],
        "effects": ["Euforia Cerebral", "Potencia Brutal", "Estimulación Creativa"],
        "activities": ["gaming", "creativity", "social"],
        "description": "La célebre creación de Sweet Seeds: cruce demoledor de Gorilla Glue x Girl Scout Cookies con niveles de THC que alcanzan el 25%. Resina exuberante y aroma a ciprés y maderas nobles.",
        "image": "images/strains/gorilla-girl.jpg",
        "visualColor": "linear-gradient(135deg, #06B6D4 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
    },
    {
        "id": "san-fernando-lemon-kush",
        "name": "San Fernando Lemon Kush",
        "aka": "SFV OG Kush x Kosher Kush",
        "bank": "Sweet Seeds",
        "breeder": "Sweet Seeds",
        "species": "Híbrida",
        "thc": 21, "cbd": 0.2,
        "indicaPct": 35, "sativaPct": 65,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 460,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "genetics": "San Fernando Valley OG Kush x Kosher Kush",
        "lineage": "San Fernando Valley OG Kush x Kosher Kush",
        "origin": "España / EE. UU.",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "caryophyllene": 30, "myrcene": 20 },
        "aroma": "Limón ácido, especias y solvente disolvente",
        "flavors": ["Limón Ácido", "Disolvente Cítrico", "Especias Kush"],
        "effects": ["Claridad Mental", "Euforia Motivadora", "Relax Progresivo"],
        "activities": ["creativity", "social", "nature_walk"],
        "description": "Excepcional híbrido de genética americana que cruza dos de las mejores líneas Kush de California. Exquisito aroma a limón ácido con matices de disolvente y fondo especiado OG.",
        "image": "images/strains/san-fernando-lemon-kush.jpg",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
    },
    {
        "id": "black-jack",
        "name": "Black Jack",
        "aka": "Black Domina x Jack Herer",
        "bank": "Sweet Seeds",
        "breeder": "Sweet Seeds",
        "species": "Híbrida",
        "thc": 21, "cbd": 0.6,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 620,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "genetics": "Black Domina x Jack Herer",
        "lineage": "Black Domina x Jack Herer",
        "origin": "España",
        "dominantTerpene": "terpinoleno",
        "terpenes": { "terpinolene": 45, "limonene": 30, "pinene": 25 },
        "aroma": "Incienso catedralicio, especias dulces y fondo terroso",
        "flavors": ["Incienso Catedral", "Especias Dulces", "Tierra Boscosa"],
        "effects": ["Equilibrio Perfecto", "Inspiración Creativa", "Alivio Físico"],
        "activities": ["creativity", "nature_walk", "workout"],
        "description": "Un clásico eterno de Sweet Seeds. Fusión perfecta de la resina índica de Black Domina con la euforia y el perfil a incienso dulce catedralicio de Jack Herer.",
        "image": "images/strains/black-jack.jpg",
        "visualColor": "linear-gradient(135deg, #1E40AF 0%, #06B6D4 100%)",
        "bgPattern": "radial-gradient(circle, rgba(30,64,175,0.2) 0%, transparent 70%)"
    },
    {
        "id": "sweet-tai",
        "name": "Sweet Tai",
        "aka": "Super Tai x Early Skunk",
        "bank": "Sweet Seeds",
        "breeder": "Sweet Seeds",
        "species": "Sativa",
        "thc": 20, "cbd": 0.4,
        "indicaPct": 30, "sativaPct": 70,
        "floweringDays": 70, "rating": 4.7, "reviewsCount": 390,
        "yieldIndoor": 450, "yieldOutdoor": 500,
        "genetics": "Super Tai x Early Skunk",
        "lineage": "Super Tai x Early Skunk",
        "origin": "España / Tailandia",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "terpinolene": 35, "pinene": 20 },
        "aroma": "Frutas exóticas asiáticas, nuez moscada y fondo picante",
        "flavors": ["Frutas Asiáticas", "Nuez Moscada", "Especias Exóticas"],
        "effects": ["Euforia Dinámica", "Lucidez Mental", "Energía Social"],
        "activities": ["social", "nature_walk", "workout"],
        "description": "Cruce exótico entre la histórica Super Tai y Early Skunk. Aporta vigor sativa con aromas especiados asiáticos y notas de nuez moscada, con una energía despierta y positiva.",
        "image": "images/strains/sweet-tai.jpg",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    }
]

def format_strain_js(s):
    terps_str = "{ " + ", ".join([f"{k}: {v}" for k, v in s['terpenes'].items()]) + " }"
    flavs_str = json.dumps(s['flavors'], ensure_ascii=False)
    effs_str = json.dumps(s['effects'], ensure_ascii=False)
    acts_str = json.dumps(s['activities'], ensure_ascii=False)
    desc_str = json.dumps(s['description'], ensure_ascii=False)
    
    return f"""  {{
    id: "{s['id']}",
    image: "{s['image']}",
    name: "{s['name']}",
    aka: "{s['aka']}",
    bank: "{s['bank']}",
    breeder: "{s['breeder']}",
    species: "{s['species']}",
    thc: {s['thc']}, cbd: {s['cbd']},
    yieldIndoor: {s['yieldIndoor']}, yieldOutdoor: {s['yieldOutdoor']},
    floweringDays: {s['floweringDays']}, rating: {s['rating']}, reviewsCount: {s['reviewsCount']},
    genetics: "{s['genetics']}",
    lineage: "{s['lineage']}",
    origin: "{s['origin']}",
    dominantTerpene: "{s['dominantTerpene']}",
    terpenes: {terps_str},
    flavors: {flavs_str},
    effects: {effs_str},
    activities: {acts_str},
    description: {desc_str},
    visualColor: "{s['visualColor']}",
    bgPattern: "{s['bgPattern']}"
  }}"""

data_path = 'js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
with open('js/data.js.bak_before_spain_expansion', 'w', encoding='utf-8') as f:
    f.write(content)

# Find all existing ids in STRAINS_DATABASE
db_match = re.search(r'export const STRAINS_DATABASE = \[(.*?)\];\s*(?:export const|$)', content, re.DOTALL)
if not db_match:
    print("❌ Could not find STRAINS_DATABASE array!")
    sys.exit(1)

existing_ids = set(re.findall(r'\bid:\s*["\']([^"\']+)["\']', db_match.group(1)))
print(f"Existing strain IDs in STRAINS_DATABASE: {len(existing_ids)}")

to_insert = []
for s in strains_to_add:
    if s['id'] not in existing_ids:
        to_insert.append(s)
        print(f"➕ Will insert: {s['id']} ({s['name']} - {s['bank']})")
    else:
        print(f"⏭️ Skipping already existing ID: {s['id']}")

if not to_insert:
    print("ℹ️ No new strains to insert!")
    sys.exit(0)

# Locate end of STRAINS_DATABASE
# We look for the closing ]; of STRAINS_DATABASE
# Find index where STRAINS_DATABASE starts
start_idx = content.find('export const STRAINS_DATABASE = [')
bracket_end_idx = content.find('];', start_idx)
if bracket_end_idx == -1:
    print("❌ Could not find closing bracket for STRAINS_DATABASE")
    sys.exit(1)

before_bracket = content[:bracket_end_idx].rstrip()
needs_comma = not before_bracket.endswith(',')
new_code = ",\n".join([format_strain_js(s) for s in to_insert])

if needs_comma:
    updated_content = before_bracket + ",\n" + new_code + "\n];" + content[bracket_end_idx+2:]
else:
    updated_content = before_bracket + "\n" + new_code + "\n];" + content[bracket_end_idx+2:]

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)

# Verify
new_db_match = re.search(r'export const STRAINS_DATABASE = \[(.*?)\];\s*(?:export const|$)', updated_content, re.DOTALL)
new_ids = re.findall(r'\bid:\s*["\']([^"\']+)["\']', new_db_match.group(1))
print(f"\n✅ Total strains in STRAINS_DATABASE after insertion: {len(new_ids)}")
print(f"✅ Successfully inserted {len(to_insert)} strains!")
