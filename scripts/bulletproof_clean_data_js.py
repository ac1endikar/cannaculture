import sys, os, re, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

terpenes_part = text[:text.find("export const STRAINS_DATABASE = [")]

# Append White Label strains if missing
white_label_strains = [
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
    "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(248,250,252,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
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
    "bgPattern": "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  }
]

# Parse existing strains cleanly
strains_part = text[text.find("export const STRAINS_DATABASE = ["):]
raw_blocks = strains_part.split('\n  {\n    id:')

strains_map = {}

# Re-read existing strains in text
for block in text.split('\n  {\n'):
    if 'id:' in block or 'name:' in block:
        # Extract id
        m_id = re.search(r'id:\s*["\']([^"\']+)["\']', block)
        if m_id:
            s_id = m_id.group(1)
            # Reconstruct JS object text cleanly
            clean_block = "  {\n" + block.strip().rstrip(',').rstrip('];')
            strains_map[s_id] = clean_block

print(f"Existing strains mapped: {len(strains_map)}")

# Add or update White Label strains
for w_strain in white_label_strains:
    s_id = w_strain["id"]
    formatted_str = "  " + json.dumps(w_strain, indent=4, ensure_ascii=False).replace('\n', '\n  ')
    formatted_str = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', formatted_str)
    strains_map[s_id] = formatted_str
    print(f"✅ Embedded {s_id} ({w_strain['name']})")

print(f"Total strains after embedding: {len(strains_map)}")

# Rebuild STRAINS_DATABASE array string
all_objects = list(strains_map.values())
formatted_db = "export const STRAINS_DATABASE = [\n" + ",\n".join(all_objects) + "\n];\n"

final_code = terpenes_part.strip() + "\n\n" + formatted_db

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(final_code)

print(f"✅ Bulletproof update complete: {len(strains_map)} strains written to data.js")
