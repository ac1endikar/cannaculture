import os
import sys
import json
import re

ROOT = "d:/cannaculture"
DATA_JS = os.path.join(ROOT, "js", "data.js")

NEW_12_STRAINS = [
    # 1. TGA Subcool Seeds - Jack the Ripper
    {
        "id": "tga-jack-the-ripper",
        "image": "img/tga-jack-the-ripper.webp",
        "name": "Jack the Ripper",
        "aka": "JTR / Killer Lemon Haze",
        "bank": "TGA Subcool Seeds",
        "species": "Sativa",
        "thc": 22, "cbd": 0.2,
        "indicaPct": 30, "sativaPct": 70,
        "floweringDays": 58, "rating": 4.9, "reviewsCount": 430,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "Pluton x Jack's Cleaner x Space Queen",
        "lineage": "Pluton x Jack's Cleaner x Space Queen",
        "origin": "USA / Costa Oeste",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 50, "pinene": 30, "myrcene": 20 },
        "aroma": "Limón ácido penetrante, mango verde y pino silvestre",
        "flavors": ["Limón Ácido", "Mango Verde", "Pino Silvestre"],
        "effects": ["Euforia Triposa", "Estimulación Creativa", "Claridad Mental"],
        "activities": ["creativity", "social", "nature_walk"],
        "description": "La creación insigne del legendario criador Subcool. Conocida por su velocidad de floración inusual para una sativa dominante y su devastador perfil cítrico cargado de terpinoleno y THCV. Produce un efecto cerebral inmediato, energético y profundamente estimulante.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
    },
    # 2. TGA Subcool Seeds - Vortex
    {
        "id": "tga-vortex",
        "image": "img/tga-vortex.webp",
        "name": "Vortex",
        "aka": "Apollo 13 x Space Queen",
        "bank": "TGA Subcool Seeds",
        "species": "Sativa",
        "thc": 23, "cbd": 0.1,
        "indicaPct": 20, "sativaPct": 80,
        "floweringDays": 58, "rating": 4.9, "reviewsCount": 380,
        "yieldIndoor": 500, "yieldOutdoor": 700,
        "genetics": "Apollo 13 x Space Queen",
        "lineage": "Apollo 13 x Space Queen",
        "origin": "USA / Costa Oeste",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 35, "caryophyllene": 20 },
        "aroma": "Fruta tropical madura, manzana ácida y cítricos dulces",
        "flavors": ["Fruta Tropical", "Manzana Ácida", "Cítrico Dulce"],
        "effects": ["Vértigo Cerebral Eufórico", "Energía Motivadora", "Risa Contagiosa"],
        "activities": ["social", "music_party", "creativity"],
        "description": "Ganadora de la High Times Cannabis Cup como Mejor Sativa. Desarrollada por Subcool cruzando Genius/Apollo 13 con Space Queen (Romulan x Cindy 99). Ofrece una aceleración mental vertiginosa con un buqué embriagador a piña confitada, sidra de manzana y mango.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    },
    # 3. Sagarmatha Seeds - Yumboldt
    {
        "id": "sagarmatha-yumboldt",
        "image": "img/sagarmatha-yumboldt.webp",
        "name": "Yumboldt",
        "aka": "Humboldt Amsterdam Selection",
        "bank": "Sagarmatha Seeds",
        "species": "Índica",
        "thc": 21, "cbd": 1.0,
        "indicaPct": 80, "sativaPct": 20,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 350,
        "yieldIndoor": 550, "yieldOutdoor": 800,
        "genetics": "Humboldt County Landrace selección Ámsterdam",
        "lineage": "Humboldt County Landrace selección Ámsterdam",
        "origin": "Humboldt County / Ámsterdam",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "pinene": 35, "humulene": 20 },
        "aroma": "Pino dulce, madera noble y fondo terroso de bosque",
        "flavors": ["Pino Dulce", "Madera Noble", "Bosque Húmedo"],
        "effects": ["Relajación Profunda", "Sedación Plácida", "Alivio Físico"],
        "activities": ["relax_sleep", "meditation", "reading"],
        "description": "Una de las primeras exportaciones californianas llevadas a Holanda a finales de los 90 y galardonada en la High Times Cup 2001. Sagarmatha preservó esta línea índica originaria del condado de Humboldt, famosa por sus cálices cristalizados y sabor dulce a bosque montañoso.",
        "visualColor": "linear-gradient(135deg, #059669 0%, #1E3A8A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
    },
    # 4. Sagarmatha Seeds - Slyder
    {
        "id": "sagarmatha-slyder",
        "image": "img/sagarmatha-slyder.webp",
        "name": "Slyder",
        "aka": "NL x Afghan Landrace",
        "bank": "Sagarmatha Seeds",
        "species": "Índica",
        "thc": 21, "cbd": 0.3,
        "indicaPct": 100, "sativaPct": 0,
        "floweringDays": 53, "rating": 4.8, "reviewsCount": 290,
        "yieldIndoor": 500, "yieldOutdoor": 650,
        "genetics": "Northern Lights x Afghan Landrace",
        "lineage": "Northern Lights x Afghan Landrace",
        "origin": "Afganistán / Ámsterdam",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "linalool": 20 },
        "aroma": "Hachís afgano tradicional, tierra húmeda y almizcle denso",
        "flavors": ["Hachís Afgano", "Tierra Húmeda", "Almizcle Especiado"],
        "effects": ["Efecto Narcótico Clásico", "Relajación Muscular Total", "Pesadez Corporal"],
        "activities": ["relax_sleep", "movie_couch", "meditation"],
        "description": "Índica pura de la vieja escuela amsterdamesa. Cruce directo de la clásica Northern Lights con una selección autóctona afgana. Variedad ultracompacta y de cogollos pétreos que induce una relajación física incondicional, ideal para desconectar el cuerpo por completo.",
        "visualColor": "linear-gradient(135deg, #475569 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)"
    },
    # 5. Chimera Seeds - Fighting Buddha
    {
        "id": "chimera-fighting-buddha",
        "image": "img/chimera-fighting-buddha.webp",
        "name": "Fighting Buddha",
        "aka": "Burmese x Blueberry 1998",
        "bank": "Chimera Seeds",
        "species": "Sativa",
        "thc": 22, "cbd": 0.2,
        "indicaPct": 30, "sativaPct": 70,
        "floweringDays": 68, "rating": 4.9, "reviewsCount": 310,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "Burmese Sativa Landrace x Blueberry 1998",
        "lineage": "Burmese Sativa Landrace x Blueberry 1998",
        "origin": "Canadá / Birmania",
        "dominantTerpene": "pinene",
        "terpenes": { "pinene": 45, "caryophyllene": 30, "myrcene": 25 },
        "aroma": "Especias orientales, arándanos silvestres y sándalo",
        "flavors": ["Especias Orientales", "Arándano Silvestre", "Madera de Sándalo"],
        "effects": ["Enfoque Zen Despierto", "Claridad Meditativa", "Vitalidad Sativa"],
        "activities": ["yoga", "meditation", "creativity"],
        "description": "Obra maestra del criador científico canadiense Chimera. Fusión de una genética autóctona birmana (Burmese Sativa) de las montañas con el clásico parental macho Blueberry de DJ Short de finales de los 90. Un colocón lúcido y contemplativo con un aroma amaderado y afrutado único.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
    },
    # 6. Chimera Seeds - Frost Bite
    {
        "id": "chimera-frost-bite",
        "image": "img/chimera-frost-bite.webp",
        "name": "Frost Bite",
        "aka": "Sweet Skunk x Blueberry",
        "bank": "Chimera Seeds",
        "species": "Híbrida",
        "thc": 23, "cbd": 0.2,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 270,
        "yieldIndoor": 550, "yieldOutdoor": 700,
        "genetics": "Sweet Skunk x Blueberry",
        "lineage": "Sweet Skunk x Blueberry",
        "origin": "Canadá",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 40, "myrcene": 35, "limonene": 25 },
        "aroma": "Skunk dulce, frutos del bosque maduros y cobertura de resina densa",
        "flavors": ["Skunk Dulce", "Frutos del Bosque", "Resina Cristalina"],
        "effects": ["Equilibrio Psicoactivo", "Euforia Placentera", "Bienestar Integral"],
        "activities": ["social", "gaming", "relaxation"],
        "description": "Híbrido legendario canadiense que une el clon Sweet Skunk de British Columbia con el linaje Blueberry original. Su nombre proviene de la capa invernal de tricomas glandulares que recubre cada cáliz y hoja, desprendiendo un perfume agridulce que enamoró a varias generaciones.",
        "visualColor": "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
    },
    # 7. Aficionado French Connection - Pianono
    {
        "id": "afc-pianono",
        "image": "img/afc-pianono.webp",
        "name": "Pianono",
        "aka": "Key Lime Pie x Sorbetto",
        "bank": "Aficionado French Connection",
        "species": "Híbrida",
        "thc": 27, "cbd": 0.1,
        "indicaPct": 60, "sativaPct": 40,
        "floweringDays": 62, "rating": 5.0, "reviewsCount": 420,
        "yieldIndoor": 600, "yieldOutdoor": 900,
        "genetics": "Key Lime Pie x Sorbetto",
        "lineage": "Key Lime Pie x Sorbetto",
        "origin": "Mendocino / París",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 35, "linalool": 20 },
        "aroma": "Masa hojaldrada, crema de lima ácida y azúcar glas",
        "flavors": ["Pastelería Fina", "Crema de Lima", "Azúcar Glas"],
        "effects": ["Éxtasis Sensorial", "Placer Gourmet", "Relajación Aterciopelada"],
        "activities": ["fine_dining", "relaxation", "social"],
        "description": "Auténtica alta costura cannábica nacida de la sinergia entre Leo Stone (Mendocino) y Frenchy Cannoli. Un cruce de Key Lime Pie con Sorbetto que rinde homenaje al dulce tradicional granadino. Flores densas y aromáticas como un postre de pastelería con una potencia abrumadora.",
        "visualColor": "linear-gradient(135deg, #84CC16 0%, #EAB308 100%)",
        "bgPattern": "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
    },
    # 8. Aficionado French Connection - Rosso Corsa
    {
        "id": "afc-rosso-corsa",
        "image": "img/afc-rosso-corsa.webp",
        "name": "Rosso Corsa",
        "aka": "SFV OG x French Gelato #33",
        "bank": "Aficionado French Connection",
        "species": "Índica",
        "thc": 28, "cbd": 0.1,
        "indicaPct": 75, "sativaPct": 25,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 390,
        "yieldIndoor": 550, "yieldOutdoor": 850,
        "genetics": "SFV OG x Gelato #33 selección francesa",
        "lineage": "SFV OG x Gelato #33 selección francesa",
        "origin": "California / Francia",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "humulene": 20 },
        "aroma": "Combustible denso, cereza oscura confitada y tierra mojada",
        "flavors": ["Queroseno OG", "Cereza Negra", "Tierra Húmeda"],
        "effects": ["Pegada Contundente", "Inmersión Física Profunda", "Paz Mental Lúcida"],
        "activities": ["night_walk", "relax_sleep", "music_listening"],
        "description": "Inspirada en el legendario rojo de las carreras italianas, esta joya de edición limitada cruza la legendaria San Fernando Valley OG Kush con un fenotipo ultra-resinoso de Gelato #33 adaptado al clima europeo. Potencia de élite con notas intensas de queroseno y frutas oscuras maduras.",
        "visualColor": "linear-gradient(135deg, #DC2626 0%, #1F2937 100%)",
        "bgPattern": "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)"
    },
    # 9. Exotic Seed - Spicy Bitch
    {
        "id": "exotic-spicy-bitch",
        "image": "img/exotic-spicy-bitch.webp",
        "name": "Spicy Bitch",
        "aka": "Reina Madre x AK-47",
        "bank": "Exotic Seed",
        "species": "Sativa",
        "thc": 22, "cbd": 0.2,
        "indicaPct": 20, "sativaPct": 80,
        "floweringDays": 66, "rating": 4.9, "reviewsCount": 460,
        "yieldIndoor": 550, "yieldOutdoor": 800,
        "genetics": "Queen Mother (Reina Madre) x AK-47",
        "lineage": "Queen Mother (Reina Madre) x AK-47",
        "origin": "Madrid / Ámsterdam",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "caryophyllene": 30, "pinene": 25 },
        "aroma": "Pimienta negra, especias picantes, madera y fondo floral",
        "flavors": ["Pimienta Negra", "Especias Picantes", "Madera Noble"],
        "effects": ["Energía Eléctrica", "Risa y Desparpajo", "Euforia Estimulante"],
        "activities": ["workout", "social", "party"],
        "description": "Una de las sativas más galardonadas del banco hispano-holandés Exotic Seed. Cruza la mítica Reina Madre (Queen Mother) de Mario Bellandi con el clon AK-47 pre-2000. Regala un efecto vivaz, electrizante y festivo acompañado de un perfil de terpenos especiado y picante sin parangón.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
    },
    # 10. Exotic Seed - Malasaña Gelato
    {
        "id": "exotic-malasana-gelato",
        "image": "img/exotic-malasana-gelato.webp",
        "name": "Malasaña Gelato",
        "aka": "Gelato #33 x Exotic Selection",
        "bank": "Exotic Seed",
        "species": "Híbrida",
        "thc": 26, "cbd": 0.1,
        "indicaPct": 60, "sativaPct": 40,
        "floweringDays": 62, "rating": 4.9, "reviewsCount": 510,
        "yieldIndoor": 600, "yieldOutdoor": 850,
        "genetics": "Gelato #33 x selección secreta Exotic Seed",
        "lineage": "Gelato #33 x selección secreta Exotic Seed",
        "origin": "Madrid / California",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "humulene": 20 },
        "aroma": "Repostería cremosa dulce, notas terrosas y cítricos suaves",
        "flavors": ["Helado Cremoso", "Galleta Terrosa", "Cítrico Suave"],
        "effects": ["Bienestar Alegre", "Relajación Corpórea", "Placer Gourmet"],
        "activities": ["social", "gastronomy", "relaxation"],
        "description": "Homenaje al bohemio barrio madrileño de Malasaña y a la cultura cannábica urbana. Exotic Seed combinó el clon californiano Larry Bird (Gelato #33) con una selección propia secreta, potenciando la densidad de flor y logrando una resina cargada de notas cremosas a repostería.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #6366F1 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
    },
    # 11. Exotic Seed - Gypsy Widow
    {
        "id": "exotic-gypsy-widow",
        "image": "img/exotic-gypsy-widow.webp",
        "name": "Gypsy Widow",
        "aka": "White Widow Selection A x B",
        "bank": "Exotic Seed",
        "species": "Híbrida",
        "thc": 23, "cbd": 0.2,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 380,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "White Widow Selección x Original White Widow",
        "lineage": "White Widow Selección x Original White Widow",
        "origin": "España / Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 40, "pinene": 35, "caryophyllene": 25 },
        "aroma": "Resina clásica de la vieja escuela, pino y toques florales frescos",
        "flavors": ["Resina Old School", "Pino Fresco", "Flores Blancas"],
        "effects": ["Potencia Clásica Holandesa", "Claridad Mental Balanceada", "Relajo Físico"],
        "activities": ["social", "nature", "reading"],
        "description": "Perfeccionamiento botánico de la legendaria White Widow. Exotic Seed cruzó dos fenotipos selectos preservados desde la década de los noventa para reforzar la producción de resina cristalina y el vigor híbrido, manteniendo intacto el sabor penetrante de la vieja escuela.",
        "visualColor": "linear-gradient(135deg, #64748B 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(100,116,139,0.2) 0%, transparent 70%)"
    },
    # 12. Exotic Seed - Herz OG
    {
        "id": "exotic-herz-og",
        "image": "img/exotic-herz-og.webp",
        "name": "Herz OG",
        "aka": "Larry OG x Kosher Kush Herzog",
        "bank": "Exotic Seed",
        "species": "Índica",
        "thc": 26, "cbd": 0.1,
        "indicaPct": 80, "sativaPct": 20,
        "floweringDays": 62, "rating": 4.9, "reviewsCount": 440,
        "yieldIndoor": 550, "yieldOutdoor": 800,
        "genetics": "Larry OG x Kosher Kush (colaboración German Rapper Herzog)",
        "lineage": "Larry OG x Kosher Kush (colaboración German Rapper Herzog)",
        "origin": "Madrid / Alemania / California",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "limonene": 20 },
        "aroma": "Pino intenso, petróleo crudo y limón dulce penetrante",
        "flavors": ["Pino Kush", "Petróleo Crudo", "Limón Confitado"],
        "effects": ["Knockout Índico Potente", "Euforia Inicial Densa", "Relajación Profunda"],
        "activities": ["relax_sleep", "music_listening", "meditation"],
        "description": "Desarrollada en estrecha colaboración con el rapero alemán Herzog. Combina los mejores atributos de Larry OG y la campeona Kosher Kush. Un misil de resina kush con un perfil demoledor a hidrocarburos y cítricos secos, que ha acumulado numerosos premios en copas europeas.",
        "visualColor": "linear-gradient(135deg, #15803D 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)"
    }
]

# Format strains into JS code
js_blocks = []
key_order = [
    'id', 'image', 'name', 'aka', 'bank', 'species', 'thc', 'cbd',
    'indicaPct', 'sativaPct', 'floweringDays', 'rating', 'reviewsCount',
    'yieldIndoor', 'yieldOutdoor', 'genetics', 'lineage', 'origin',
    'dominantTerpene', 'terpenes', 'aroma', 'flavors', 'effects',
    'activities', 'description', 'visualColor', 'bgPattern'
]

for s in NEW_12_STRAINS:
    lines = ["  {"]
    for k in key_order:
        if k not in s:
            continue
        v = s[k]
        if isinstance(v, str):
            val_str = json.dumps(v, ensure_ascii=False)
            lines.append(f'        {k}: {val_str},')
        elif isinstance(v, (int, float)):
            lines.append(f'        {k}: {v},')
        elif isinstance(v, dict):
            inner = ", ".join(f"{tk}: {tv}" for tk, tv in v.items())
            lines.append(f'        {k}: {{ {inner} }},')
        elif isinstance(v, list):
            val_str = json.dumps(v, ensure_ascii=False)
            lines.append(f'        {k}: {val_str},')
    if lines[-1].endswith(','):
        lines[-1] = lines[-1][:-1]
    lines.append("      }")
    js_blocks.append("\n".join(lines))

code_to_insert = ",\n" + ",\n".join(js_blocks)

with open(DATA_JS, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.rfind('\n];')
if pos == -1:
    print("Error: Could not locate end of STRAINS_DATABASE in data.js")
    sys.exit(1)

new_text = text[:pos] + code_to_insert + text[pos:]

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Successfully inserted {len(NEW_12_STRAINS)} strains into {DATA_JS}")
