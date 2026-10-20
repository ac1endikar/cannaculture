import os, sys, re, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

eva_strains = [
  {
    "id": "jamaican-dream",
    "image": "img/jamaican-dream.webp",
    "name": "Jamaican Dream",
    "aka": "Landrace Jamaica pura",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Sativa",
    "thc": 21, "cbd": 0.1,
    "yieldIndoor": 550, "yieldOutdoor": 800,
    "floweringDays": 44, "rating": 4.9, "reviewsCount": 480,
    "genetics": "Landrace Jamaica pura",
    "lineage": "Landrace Jamaica pura",
    "origin": "Jamaica / España",
    "dominantTerpene": "limonene",
    "terpenes": {"limonene": 45, "myrcene": 30, "caryophyllene": 25},
    "flavors": ["Cítrico Dulce", "Frutas Tropicales", "Toque Azucarado"],
    "effects": ["Euforia Activa", "Creatividad Luminosa", "Energía Social"],
    "activities": ["creativity", "social", "nature_walk"],
    "description": "La joya más icónica de Eva Seeds y una de las sativas puras más rápidas del planeta (42-45 días). Procedente de una cuidada selección de landraces jamaiquinas, regala cogollos densos cubiertos de resina con aroma dulce y cítrico y un efecto eufórico, alegre y muy limpio.",
    "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.25) 0%, transparent 70%)"
  },
  {
    "id": "monster",
    "image": "img/monster.webp",
    "name": "Monster",
    "aka": "G13 Hash Plant x Híbrido Sudamericano",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Híbrida",
    "thc": 20, "cbd": 0.2,
    "yieldIndoor": 600, "yieldOutdoor": 1200,
    "floweringDays": 58, "rating": 4.8, "reviewsCount": 390,
    "genetics": "G13 Hash Plant x Híbrido Sudamericano",
    "lineage": "G13 Hash Plant x Híbrido Sudamericano",
    "origin": "España",
    "dominantTerpene": "myrcene",
    "terpenes": {"myrcene": 45, "caryophyllene": 35, "pinene": 20},
    "flavors": ["Fruta Madura", "Madera Noble", "Especias"],
    "effects": ["Relajación Corporal", "Paz Sensorial", "Bienestar Duradero"],
    "activities": ["relax_sleep", "music", "gaming"],
    "description": "Variedad de porte colosal y producción gigantesca que cruza la legendaria G13 Hash Plant con un selecto híbrido sudamericano. Sus cogollos son densos, resinosos y desprenden un perfume embriagador a fruta madura, maderas nobles y especias orientales.",
    "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.25) 0%, transparent 70%)"
  },
  {
    "id": "veneno",
    "image": "img/veneno.webp",
    "name": "Veneno",
    "aka": "Monster x Papa's Candy",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Indica",
    "thc": 20, "cbd": 0.3,
    "yieldIndoor": 550, "yieldOutdoor": 900,
    "floweringDays": 58, "rating": 4.9, "reviewsCount": 410,
    "genetics": "Monster x Papa's Candy",
    "lineage": "Monster x Papa's Candy",
    "origin": "España",
    "dominantTerpene": "myrcene",
    "terpenes": {"myrcene": 50, "caryophyllene": 30, "linalool": 20},
    "flavors": ["Fresas Dulces", "Especias Orientales", "Fondo Amaderado"],
    "effects": ["Sedación Placentera", "Paz Mental", "Relajación Muscular"],
    "activities": ["relax_sleep", "meditation", "music"],
    "description": "Cruce demoledor entre la productiva Monster y la golosa Papa's Candy. Ofrece una abrumadora capa de tricomas sobre flores que desprenden aroma a fresas silvestres maduras aderezadas con especias. Efecto índico profundo, narcótico y sumamente relajante.",
    "visualColor": "linear-gradient(135deg, #EF4444 0%, #991B1B 100%)",
    "bgPattern": "radial-gradient(circle, rgba(239,68,68,0.25) 0%, transparent 70%)"
  },
  {
    "id": "papas-candy",
    "image": "img/papas-candy.webp",
    "name": "Papa's Candy",
    "aka": "Laos x Pakistán",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Indica",
    "thc": 20, "cbd": 0.4,
    "yieldIndoor": 550, "yieldOutdoor": 800,
    "floweringDays": 50, "rating": 4.9, "reviewsCount": 430,
    "genetics": "Laos x Pakistán",
    "lineage": "Laos x Pakistán",
    "origin": "España",
    "dominantTerpene": "caryophyllene",
    "terpenes": {"caryophyllene": 45, "myrcene": 35, "limonene": 20},
    "flavors": ["Caramelo Dulce", "Anís", "Toque Terroso"],
    "effects": ["Calma Absoluta", "Bienestar Físico", "Serenidad"],
    "activities": ["relax_sleep", "meditation", "gaming"],
    "description": "Auténtico deleite para el paladar ganador de múltiples copas. Cruza una exótica sativa de Laos con una robusta kush pakistaní, resultando en una planta compacta repleta de cogollos brillantes como diamantes, aroma a caramelo dulce de anís y un efecto medicinal balsámico.",
    "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%)",
    "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.25) 0%, transparent 70%)"
  },
  {
    "id": "high-level",
    "image": "img/high-level.webp",
    "name": "High Level",
    "aka": "Lesotho x Skunk/Haze",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Sativa",
    "thc": 19, "cbd": 0.2,
    "yieldIndoor": 500, "yieldOutdoor": 750,
    "floweringDays": 58, "rating": 4.8, "reviewsCount": 370,
    "genetics": "Lesotho x Skunk/Haze",
    "lineage": "Lesotho x Skunk/Haze",
    "origin": "España",
    "dominantTerpene": "terpinolene",
    "terpenes": {"terpinolene": 45, "pinene": 30, "myrcene": 25},
    "flavors": ["Dulce Afrutado", "Pimienta Picante", "Notas Haze"],
    "effects": ["Claridad Mental", "Euforia Estimulante", "Creatividad Total"],
    "activities": ["creativity", "social", "nature_walk"],
    "description": "Una sativa 100% pura nacida del cruce entre una landrace de Lesotho (Sudáfrica) y un cruce Skunk/Haze. Estructura espigada con largas colas repletas de resina, aroma dulce afrutado con un picante fondo especiado y un viaje cerebral eufórico de larga duración.",
    "visualColor": "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
    "bgPattern": "radial-gradient(circle, rgba(6,182,212,0.25) 0%, transparent 70%)"
  },
  {
    "id": "black-dream",
    "image": "img/black-dream.webp",
    "name": "Black Dream",
    "aka": "Jamaican Dream x Black Domina",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Híbrida",
    "thc": 21, "cbd": 0.2,
    "yieldIndoor": 550, "yieldOutdoor": 900,
    "floweringDays": 48, "rating": 4.9, "reviewsCount": 460,
    "genetics": "Jamaican Dream x Black Domina",
    "lineage": "Jamaican Dream x Black Domina",
    "origin": "España",
    "dominantTerpene": "caryophyllene",
    "terpenes": {"caryophyllene": 40, "limonene": 35, "myrcene": 25},
    "flavors": ["Frutas Dulces", "Pimienta Negra", "Toque Roble"],
    "effects": ["Equilibrio Mental-Físico", "Dicha Eufórica", "Relajación Corporal"],
    "activities": ["social", "gaming", "music"],
    "description": "Híbrido magistral que fusiona la rapidez y energía de Jamaican Dream con la contundencia afgana de Black Domina. Florece en tan solo 45-50 días produciendo densas piñas resinosas con un aroma delicioso afrutado y picante, brindando un efecto balanceado, lúcido y reconfortante.",
    "visualColor": "linear-gradient(135deg, #6366F1 0%, #4338CA 100%)",
    "bgPattern": "radial-gradient(circle, rgba(99,102,241,0.25) 0%, transparent 70%)"
  },
  {
    "id": "furious-candy",
    "image": "img/furious-candy.webp",
    "name": "Furious Candy",
    "aka": "Papa's Candy x Great White Shark",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Indica",
    "thc": 20, "cbd": 0.3,
    "yieldIndoor": 500, "yieldOutdoor": 800,
    "floweringDays": 48, "rating": 4.8, "reviewsCount": 380,
    "genetics": "Papa's Candy x Great White Shark",
    "lineage": "Papa's Candy x Great White Shark",
    "origin": "España",
    "dominantTerpene": "myrcene",
    "terpenes": {"myrcene": 45, "limonene": 30, "caryophyllene": 25},
    "flavors": ["Chicle de Fresa", "Fruta Dulce", "Golosinas"],
    "effects": ["Relajación Dulce", "Buen Humor", "Desconexión"],
    "activities": ["relax_sleep", "gaming", "social"],
    "description": "Variedad super dulce nacida del cruce entre la azucarada Papa's Candy y la mítica productora de resina Great White Shark. Es famosa por su inconfundible aroma a chicle de fresa y golosinas ácidas con un efecto relajante, alegre y muy placentero.",
    "visualColor": "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
    "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.25) 0%, transparent 70%)"
  },
  {
    "id": "missing-in-barcelona",
    "image": "img/missing-in-barcelona.webp",
    "name": "Missing In Barcelona",
    "aka": "High Level x Blueberry",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Híbrida",
    "thc": 20, "cbd": 0.2,
    "yieldIndoor": 550, "yieldOutdoor": 900,
    "floweringDays": 58, "rating": 4.9, "reviewsCount": 440,
    "genetics": "High Level x Blueberry",
    "lineage": "High Level x Blueberry",
    "origin": "España",
    "dominantTerpene": "terpinolene",
    "terpenes": {"terpinolene": 40, "myrcene": 35, "limonene": 25},
    "flavors": ["Frutos del Bosque", "Naranja Ácida", "Arándano Dulce"],
    "effects": ["Subidón Cerebral Estimulante", "Risas", "Dicha Creativa"],
    "activities": ["creativity", "social", "music"],
    "description": "Un híbrido legendario que une la potencia sativa de High Level con el sabor afrutado de Blueberry. Desarrolla cogollos resinosos teñidos de púrpura con aroma a frutos del bosque y naranja ácida. Su efecto es muy potente, risueño y altamente creativo.",
    "visualColor": "linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%)",
    "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.25) 0%, transparent 70%)"
  },
  {
    "id": "tnt-kush",
    "image": "img/tnt-kush.webp",
    "name": "TNT Kush",
    "aka": "Pakistan Chitral Kush",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Indica",
    "thc": 22, "cbd": 0.5,
    "yieldIndoor": 500, "yieldOutdoor": 750,
    "floweringDays": 58, "rating": 4.9, "reviewsCount": 470,
    "genetics": "Pakistan Chitral Kush",
    "lineage": "Pakistan Chitral Kush",
    "origin": "Pakistán / España",
    "dominantTerpene": "myrcene",
    "terpenes": {"myrcene": 50, "caryophyllene": 30, "humulene": 20},
    "flavors": ["Frutos Secos", "Cereza Madura", "Madera de Nogal"],
    "effects": ["Efecto Narcótico Potente", "Relajación Muscular Total", "Paz Zen"],
    "activities": ["relax_sleep", "meditation"],
    "description": "Una índica pura 100% originaria de las montañas de Chitral en Pakistán. Produce flores extraordinariamente compactas con una deslumbrante capa de resina afgana, aroma a frutos secos, cerezas y madera de nogal y una pegada demoledora perfecta para el insomnio y la desconexión.",
    "visualColor": "linear-gradient(135deg, #14B8A6 0%, #0F766E 100%)",
    "bgPattern": "radial-gradient(circle, rgba(20,184,166,0.25) 0%, transparent 70%)"
  },
  {
    "id": "gipsy-haze",
    "image": "img/gipsy-haze.webp",
    "name": "Gipsy Haze",
    "aka": "Jack Herer x Black Domina x Space Bomb",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Sativa",
    "thc": 22, "cbd": 0.2,
    "yieldIndoor": 600, "yieldOutdoor": 1000,
    "floweringDays": 63, "rating": 4.9, "reviewsCount": 450,
    "genetics": "Jack Herer x Black Domina x Space Bomb",
    "lineage": "Jack Herer x Black Domina x Space Bomb",
    "origin": "España",
    "dominantTerpene": "limonene",
    "terpenes": {"limonene": 45, "terpinolene": 35, "pinene": 20},
    "flavors": ["Incienso Alimonado", "Mango Maduro", "Toque Haze Cítrico"],
    "effects": ["Euforia Enérgica", "Inspiración Creativa", "Risas y Vitalidad"],
    "activities": ["creativity", "social", "nature_walk"],
    "description": "Espectacular cruce a tres bandas entre Jack Herer, Black Domina y Space Bomb. Esta sativa de floración rápida destaca por su aroma intenso a incienso alimonado con matices a mango y lima, regalando un subidón eufórico muy limpio y alegre.",
    "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
    "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.25) 0%, transparent 70%)"
  },
  {
    "id": "lemon-king",
    "image": "img/lemon-king.webp",
    "name": "Lemon King",
    "aka": "Space Bomb x Critical Swiss",
    "bank": "Eva Seeds",
    "breeder": "Eva Seeds",
    "species": "Sativa",
    "thc": 23, "cbd": 0.1,
    "yieldIndoor": 550, "yieldOutdoor": 900,
    "floweringDays": 52, "rating": 4.9, "reviewsCount": 460,
    "genetics": "Space Bomb x Critical Swiss",
    "lineage": "Space Bomb x Critical Swiss",
    "origin": "España",
    "dominantTerpene": "limonene",
    "terpenes": {"limonene": 50, "caryophyllene": 30, "myrcene": 20},
    "flavors": ["Limón Maduro", "Incienso Fino", "Cítrico Dulce"],
    "effects": ["Euforia Activa", "Dicha Cerebral", "Energía Positiva"],
    "activities": ["social", "creativity", "nature_walk"],
    "description": "Poderoso híbrido predominantemente sativo fruto de la unión entre Space Bomb y Critical Swiss. Espectacular perfil de terpenos con notas marcadas de limón maduro madurado al sol e incienso eclesiástico, con un efecto despierto, activo y altamente social.",
    "visualColor": "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    "bgPattern": "radial-gradient(circle, rgba(132,204,22,0.25) 0%, transparent 70%)"
  }
]

def format_strain_js(s):
    # Format with clean indentation matching data.js
    terps_str = "{ " + ", ".join([f"{k}: {v}" for k, v in s['terpenes'].items()]) + " }"
    flavs_str = json.dumps(s['flavors'], ensure_ascii=False)
    effs_str = json.dumps(s['effects'], ensure_ascii=False)
    acts_str = json.dumps(s['activities'], ensure_ascii=False)
    desc_str = json.dumps(s['description'], ensure_ascii=False)
    
    js = f"""  {{
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
    return js

# Also create js/eva_seeds.js
eva_file_content = "// EVA SEEDS - CATÁLOGO FOTOPERIÓDICO THC OFICIAL (11 VARIEDADES)\nconst EVA_SEEDS_DATABASE = [\n"
eva_file_content += ",\n".join([format_strain_js(s) for s in eva_strains])
eva_file_content += "\n];\n"

with open('d:/cannaculture/js/eva_seeds.js', 'w', encoding='utf-8') as f:
    f.write(eva_file_content)
print(f"✅ Generated d:/cannaculture/js/eva_seeds.js ({len(eva_strains)} strains)")

# Now append to js/data.js safely
data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    data_content = f.read()

# Backup
with open('d:/cannaculture/js/data.js.bak_before_eva_seeds', 'w', encoding='utf-8') as f:
    f.write(data_content)

# Count existing strains in STRAINS_DATABASE
db_idx = data_content.find('const STRAINS_DATABASE')
if db_idx == -1:
    print("❌ ERROR: const STRAINS_DATABASE not found in data.js")
    sys.exit(1)

pre_matches = re.findall(r'\bid:\s*["\']([^"\']+)["\']', data_content[db_idx:])
count_before = len(pre_matches)
print(f"📊 Strains in STRAINS_DATABASE before insertion: {count_before}")

# Find the end of STRAINS_DATABASE: usually ends with "];\n" or "];"
last_bracket_idx = data_content.rfind('];')
if last_bracket_idx == -1:
    print("❌ ERROR: Closing bracket '];' not found in data.js")
    sys.exit(1)

# Check if there is a comma before the closing bracket
before_bracket = data_content[:last_bracket_idx].rstrip()
needs_comma = not before_bracket.endswith(',')

new_strains_code = ",\n".join([format_strain_js(s) for s in eva_strains])

if needs_comma:
    new_data_content = before_bracket + ",\n" + new_strains_code + "\n];\n" + data_content[last_bracket_idx+2:]
else:
    new_data_content = before_bracket + "\n" + new_strains_code + "\n];\n" + data_content[last_bracket_idx+2:]

# Write updated data.js
with open(data_path, 'w', encoding='utf-8') as f:
    f.write(new_data_content)

# Verify count after insertion
post_matches = re.findall(r'\bid:\s*["\']([^"\']+)["\']', new_data_content[db_idx:])
count_after = len(post_matches)
print(f"📊 Strains in STRAINS_DATABASE after insertion: {count_after}")
print(f"✅ Delta: +{count_after - count_before} strains (Target: +11)")

if count_after == count_before + 11:
    print("🎉 SUCCESS: All 11 Eva Seeds strains appended safely!")
else:
    print("⚠️ WARNING: Count mismatch!")
