import os
import sys
import re

DATA_PATH = "d:/cannaculture/js/data.js"
BACKUP_PATH = "d:/cannaculture/js/data.js.bak_before_auto_purge"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    original_content = f.read()

# Make backup
with open(BACKUP_PATH, "w", encoding="utf-8") as f:
    f.write(original_content)

print(f"Created backup at {BACKUP_PATH}")

# Define the 6 replacements
replacements = {
    "00s-cheese-xl": """  {
        id: "00s-00-skunk",
        image: "img/00s-cheese-xl.webp",
        name: "00 Skunk",
        aka: "Skunk #1 Selection",
        bank: "00 Seeds Bank",
        species: "Híbrida",
        thc: 20, cbd: 0.1,
        floweringDays: 55, rating: 4.8, reviewsCount: 310,
        yieldIndoor: 550, yieldOutdoor: 700,
        genetics: "Skunk #1 x Skunk #1",
        origin: "España",
        dominantTerpene: "myrcene",
        terpenes: { myrcene: 45, caryophyllene: 30, pinene: 25 },
        aroma: "Aroma cítrico penetrante, matices almizclados y fondo dulce skunk clásico",
        flavors: ["Cítrico Skunk", "Almizcle", "Dulce Herbal"],
        effects: ["Euforia Cerebral", "Relajación Corporal", "Antiestrés"],
        activities: ["social", "gaming", "creativity"],
        description: "Selección pura de Skunk #1 de floración rápida y generosa resina aromática. Floración vigorosa con el aroma dulce y especiado característico de las mejores selecciones clásicas.",
        visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
      }""",

    "00s-white-smurf": """  {
        id: "00s-northern-lights",
        image: "img/00s-white-smurf.webp",
        name: "Northern Lights (00 Seeds)",
        aka: "NL Selection",
        bank: "00 Seeds Bank",
        species: "Índica",
        thc: 21, cbd: 0.2,
        floweringDays: 50, rating: 4.8, reviewsCount: 290,
        yieldIndoor: 500, yieldOutdoor: 650,
        genetics: "Northern Lights Selection",
        origin: "España",
        dominantTerpene: "myrcene",
        terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
        aroma: "Aroma dulce terroso, madera de pino y especias balsámicas",
        flavors: ["Terroso Dulce", "Pino", "Especias"],
        effects: ["Relajación Muscular", "Calma Mental", "Sedación Nocturna"],
        activities: ["relax_sleep", "meditation"],
        description: "Clásica selección Índica afgana afamada por su estructura compacta, nula exigencia en cultivo y cogollos nevados en resina de potencia sedante.",
        visualColor: "linear-gradient(135deg, #059669 0%, #047857 100%)",
        bgPattern: "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
      }""",

    "paradise-red-velvet-auto": """  {
        id: "paradise-all-kush",
        image: "img/paradise-red-velvet-auto.webp",
        name: "All-Kush",
        aka: "Sheetara / Afghan Kush",
        bank: "Paradise Seeds",
        species: "Índica",
        thc: 22, cbd: 0.3,
        floweringDays: 60, rating: 4.8, reviewsCount: 380,
        yieldIndoor: 450, yieldOutdoor: 600,
        genetics: "Kush x Hollandsche Hoop",
        origin: "Holanda",
        dominantTerpene: "myrcene",
        terpenes: { myrcene: 45, caryophyllene: 35, linalool: 20 },
        aroma: "Aroma balsámico oriental, almizcle Kush dulce y toques terrosos",
        flavors: ["Kush Especiado", "Hachís Dulce", "Herbal"],
        effects: ["Sedación Corporal", "Alivio Físico", "Paz Profunda"],
        activities: ["relax_sleep", "meditation"],
        description: "Premiada variedad de Paradise Seeds con profunda ascendencia Kush afgana. Produce cogollos densos bañados en cristales resinosos con sabor suave a hachís y un efecto de relajación corporal contundente.",
        visualColor: "linear-gradient(135deg, #047857 0%, #064E3B 100%)",
        bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
      }""",

    "paradise-stromboli-auto": """  {
        id: "paradise-nebula",
        image: "img/paradise-stromboli-auto.webp",
        name: "Nebula",
        aka: "Starcloud / Haze x Master Widow",
        bank: "Paradise Seeds",
        species: "Híbrida",
        thc: 23, cbd: 0.2,
        floweringDays: 63, rating: 4.9, reviewsCount: 440,
        yieldIndoor: 500, yieldOutdoor: 700,
        genetics: "US Haze x Master Widow",
        origin: "Holanda",
        dominantTerpene: "terpinolene",
        terpenes: { terpinolene: 40, limonene: 35, caryophyllene: 25 },
        aroma: "Aroma dulce afrutado, toques de miel silvestre y matices Haze frescos",
        flavors: ["Miel Dulce", "Frutas Maduras", "Toque Haze"],
        effects: ["Euforia Psicoactiva", "Creatividad Luminosa", "Energía Social"],
        activities: ["creativity", "social", "gaming"],
        description: "La legendaria 'Nube de Estrellas' de Paradise Seeds, multicampeona en varias ediciones de la High Times Cannabis Cup. Resina brillante como un manto estelar y efecto eufórico trascendental.",
        visualColor: "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
        bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
      }""",

    "ss-bigdevil-xl": """  {
        id: "ss-sweet-cheese",
        image: "img/ss-bigdevil-xl.webp",
        name: "Sweet Cheese",
        aka: "Cheese x Black Jack",
        bank: "Sweet Seeds",
        species: "Sativa",
        thc: 22, cbd: 0.2,
        floweringDays: 63, rating: 4.8, reviewsCount: 410,
        yieldIndoor: 550, yieldOutdoor: 600,
        genetics: "Cheese x Black Jack",
        origin: "España",
        dominantTerpene: "caryophyllene",
        terpenes: { caryophyllene: 40, myrcene: 35, limonene: 25 },
        aroma: "Queso curado maduro con fondo dulce especiado tipo Black Jack",
        flavors: ["Queso Curado", "Incienso Dulce", "Especias"],
        effects: ["Claridad Mental", "Euforia Dinámica", "Bienestar"],
        activities: ["social", "creativity", "workout"],
        description: "Fusión magistral entre el clon élite Cheese y Black Jack. Combina el sabor intenso a queso curado con los matices de incienso dulce, ofreciendo una producción descomunal y vigor extraordinario.",
        visualColor: "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
        bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
      }""",

    "ss-black-cream-auto": """  {
        id: "ss-mohan-ram",
        image: "img/ss-black-cream-auto.webp",
        name: "Mohan Ram",
        aka: "Sweet Afgani Delicious x White Widow",
        bank: "Sweet Seeds",
        species: "Índica",
        thc: 22, cbd: 0.3,
        floweringDays: 56, rating: 4.9, reviewsCount: 460,
        yieldIndoor: 500, yieldOutdoor: 550,
        genetics: "S.A.D. S1 x White Widow",
        origin: "España",
        dominantTerpene: "myrcene",
        terpenes: { myrcene: 45, pinene: 30, caryophyllene: 25 },
        aroma: "Aroma dulce y almizclado clásico de White Widow con matices florales frescos",
        flavors: ["Almizcle Floral", "Dulce Afgano", "Toque Frutal"],
        effects: ["Relajación Corporal", "Calma Mental", "Paz Serena"],
        activities: ["relax_sleep", "meditation"],
        description: "Homenaje botánico a Mohan Ram. Hibridación de la dulce y resinosa S.A.D. con un clon élite seleccionado de White Widow. Espectacular producción de tricomas y aroma floral exquisito.",
        visualColor: "linear-gradient(135deg, #059669 0%, #047857 100%)",
        bgPattern: "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
      }"""
}

# The 9 ids to purge
purge_ids = [
    "bsf-gorilla-glue-auto",
    "bsf-lebron-haze-auto",
    "bsf-red-critical-auto",
    "dinafem-critical-auto-2",
    "dinafem-moby-dick-auto",
    "dinafem-gorilla-auto",
    "dp-auto-blueberry",
    "dp-auto-mazar",
    "rqs-og-kush-auto"
]

content = original_content

# 1. Apply replacements
for target_id, new_block in replacements.items():
    # Regex to find object with target_id
    pattern = rf'(\s*\{{\s*id:\s*["\']{re.escape(target_id)}["\'].*?\n\s*\}})'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        content = content[:m.start()] + "\n" + new_block + content[m.end():]
        print(f"Replaced {target_id}")
    else:
        print(f"Warning: could not find {target_id} for replacement")

# 2. Purge the 9 auto entries
for p_id in purge_ids:
    # Match object with trailing comma and whitespace or preceding comma
    # Pattern: \s*\{\s*id:\s*["']p_id["'].*?\n\s*\},?
    pattern = rf'(\n\s*\{{\s*id:\s*["\']{re.escape(p_id)}["\'].*?\n\s*\}},?)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        content = content[:m.start()] + content[m.end():]
        print(f"Purged {p_id}")
    else:
        print(f"Warning: could not find {p_id} for purge")

# Clean any double commas or syntax imperfections
content = re.sub(r',\s*,', ',', content)
content = re.sub(r',\s*\];', '\n];', content)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Saved updated {DATA_PATH}")
