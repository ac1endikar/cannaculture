import sys, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

new_strains = """,
  {
    id: "ths-bubblegum",
    image: "img/ths-bubblegum.jpg",
    name: "Bubblegum",
    aka: "Indiana Bubblegum",
    bank: "TH Seeds",
    species: "Hibrida",
    thc: 19, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 56, rating: 4.8, reviewsCount: 1800,
    genetics: "Indiana Bubblegum Selection",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, limonene: 25 },
    flavors: ["Chicle Rosa", "Fresa Dulce", "Golosina Afrutada"],
    effects: ["Euforia Dulce", "Relajación Corporal", "Bienestar Alegre"],
    activities: ["social", "music", "relax_sleep"],
    description: "Leyenda viva del cannabis galardonada con múltiples Cannabis Cups. Famosa por su inconfundible aroma y sabor a chicle de fresa dulce. Ofrece un colocón eufórico muy equilibrado que relaja el cuerpo manteniendo la mente alegre.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #F43F5E 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
    id: "ths-french-cookies",
    image: "img/ths-french-cookies.jpg",
    name: "French Cookies",
    aka: "Platinum Cookies Selection",
    bank: "TH Seeds",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 400, yieldOutdoor: 500,
    floweringDays: 63, rating: 4.7, reviewsCount: 920,
    genetics: "Platinum Cookies S1",
    origin: "Francia / Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, humulene: 25 },
    flavors: ["Galleta de Cacao", "Crema Dulce", "Menta Suave"],
    effects: ["Energía Creativa", "Euforia Elevada", "Claridad Mental"],
    activities: ["creativity", "social", "gaming"],
    description: "Una joya sative que destaca por sus tonos oscuros casi negros en floración y su densa capa de tricomas brillantes. Sabor dulce a galleta recién horneada con toques cremosos. Produce un subidón estimulante y altamente creativo.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #1E1B4B 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
    id: "ths-chocolate-chunk",
    image: "img/ths-chocolate-chunk.jpg",
    name: "Chocolate Chunk",
    aka: "100% Afghan Indica",
    bank: "TH Seeds",
    species: "Indica",
    thc: 20, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 500,
    floweringDays: 55, rating: 4.6, reviewsCount: 750,
    genetics: "Afghani Pure Inbred Line",
    origin: "Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Chocolate Negro", "Hachís Ancestral", "Tierra Dulce"],
    effects: ["Sedación Profunda", "Relax Físico", "Sueño Reparador"],
    activities: ["relax_sleep"],
    description: "100% Indica pura afgana con una estructura densa como un bloque de chocolate. Aromas profundos a hachís afgano clásico y notas de cacao amargo. Efecto narcótico devastador, ideal para combatir el insomnio y los dolores musculares.",
    visualColor: "linear-gradient(135deg, #78350F 0%, #27272A 100%)",
    bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  }
]"""

if "id: \"ths-bubblegum\"" not in text:
    target = text.rfind("];")
    if target != -1:
        updated = text[:target] + new_strains + text[target:]
        with open(data_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print("✅ Added Bubblegum, French Cookies, and Chocolate Chunk to data.js")
    else:
        print("❌ Could not find closing ]; in data.js")
else:
    print("ℹ️ Strains already present in data.js")
