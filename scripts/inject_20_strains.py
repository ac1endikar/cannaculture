import os
import sys
import json
import re
from PIL import Image

ROOT = "d:/cannaculture"
DATA_JS = os.path.join(ROOT, "js", "data.js")
IMG_DIR = os.path.join(ROOT, "img")

NEW_20_STRAINS = [
    {
        "id": "sensi-nl5-haze",
        "image": "img/sensi-nl5-haze.webp",
        "name": "Northern Lights #5 x Haze",
        "aka": "NL#5 x Haze / Sensi Classic",
        "bank": "Sensi Seeds",
        "species": "Sativa",
        "thc": 24, "cbd": 0.2,
        "indicaPct": 30, "sativaPct": 70,
        "floweringDays": 70, "rating": 4.9, "reviewsCount": 520,
        "yieldIndoor": 550, "yieldOutdoor": 800,
        "genetics": "Northern Lights #5 x Haze",
        "lineage": "Northern Lights #5 x Haze",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "pinene": 35, "caryophyllene": 20 },
        "aroma": "Incienso clásico Haze, especias orientales y madera noble",
        "flavors": ["Incienso Haze", "Pino Especiado", "Madera Noble"],
        "effects": ["Euforia Psicoactiva", "Claridad Cerebral", "Energía Creativa"],
        "activities": ["creativity", "social", "nature_walk"],
        "description": "Una de las combinaciones genéticas más legendarias y premiadas de la historia del cannabis. Creada por Sensi Seeds, une la potencia resinosa y robusta de NL#5 con el subidón cerebral estratosférico e incensado de la Haze tropical.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "bf-mimosa-evo",
        "image": "img/bf-mimosa-evo.webp",
        "name": "Mimosa EVO",
        "aka": "Purple Punch x Clementine",
        "bank": "Barney's Farm",
        "species": "Sativa",
        "thc": 29, "cbd": 0.1,
        "indicaPct": 30, "sativaPct": 70,
        "floweringDays": 68, "rating": 5.0, "reviewsCount": 640,
        "yieldIndoor": 700, "yieldOutdoor": 1500,
        "genetics": "Purple Punch x Clementine",
        "lineage": "Purple Punch x Clementine",
        "origin": "Ámsterdam / California",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "caryophyllene": 30, "myrcene": 20 },
        "aroma": "Mandarina ácida, cítricos intensos y frutos rojos",
        "flavors": ["Mandarina Cítrica", "Ponche de Frutas", "Limón Confitado"],
        "effects": ["Subidón Eufórico", "Energía Solar", "Claridad Mental"],
        "activities": ["social", "creativity", "workout"],
        "description": "Evolución perfeccionada por Barney's Farm del célebre clon californiano Mimosa de Symbiotic Genetics. Niveles titánicos de THC de hasta el 30%, terpenos explosivos de cítricos tropicales y belleza visual púrpura deslumbrante.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #EC4899 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    },
    {
        "id": "bf-glookies",
        "image": "img/bf-glookies.webp",
        "name": "Glookies",
        "aka": "Gorilla Glue #4 x Thin Mint GSC",
        "bank": "Barney's Farm",
        "species": "Híbrida",
        "thc": 25, "cbd": 0.2,
        "indicaPct": 70, "sativaPct": 30,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 480,
        "yieldIndoor": 600, "yieldOutdoor": 900,
        "genetics": "Gorilla Glue #4 x Thin Mint GSC",
        "lineage": "Gorilla Glue #4 x Thin Mint GSC",
        "origin": "Ámsterdam / USA",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "aroma": "Diésel penetrante, lima fresca y nuez tostada",
        "flavors": ["Diésel Lima", "Nuez Tostada", "Menta Chocolate"],
        "effects": ["Relajación Corporal", "Motivación Creativa", "Sensación Zen"],
        "activities": ["gaming", "relax_sleep", "social"],
        "description": "Cruce élite de dos monstruos de la resina: Gorilla Glue #4 y Thin Mint Girl Scout Cookies. Ofrece un efecto dual que estimula la mente mientras sumerge el cuerpo en una calma placentera sin apalancar.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ss-cream-47",
        "image": "img/ss-cream-47.webp",
        "name": "Cream 47",
        "aka": "Cream Caramel x AK-47",
        "bank": "Sweet Seeds",
        "species": "Híbrida",
        "thc": 21, "cbd": 1.0,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 390,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "genetics": "Cream Caramel x AK-47",
        "lineage": "Cream Caramel x AK-47",
        "origin": "España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 40, "myrcene": 35, "humulene": 25 },
        "aroma": "Dulce acaramelado con matices terrosos y especiados",
        "flavors": ["Caramelo Dulce", "Tierra Especiada", "Fondo Frutal"],
        "effects": ["Euforia Festiva", "Relajación Muscular", "Equilibrio Físico"],
        "activities": ["social", "relax_sleep", "gaming"],
        "description": "La unión de dos campeonas estelares: la dulzura caramelizada y resinosa de Cream Caramel fundida con la potencia vigorosa y productiva del legendario clon élite AK-47.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ss-jack-47",
        "image": "img/ss-jack-47.webp",
        "name": "Jack 47",
        "aka": "Jack Herer x AK-47",
        "bank": "Sweet Seeds",
        "species": "Sativa",
        "thc": 24, "cbd": 0.2,
        "indicaPct": 25, "sativaPct": 75,
        "floweringDays": 68, "rating": 4.9, "reviewsCount": 470,
        "yieldIndoor": 600, "yieldOutdoor": 750,
        "genetics": "Jack Herer x AK-47",
        "lineage": "Jack Herer x AK-47",
        "origin": "España",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "pinene": 30, "caryophyllene": 25 },
        "aroma": "Incienso cítrico, pino fresco y fondo dulce floral",
        "flavors": ["Incienso Catedral", "Limón Fresco", "Pino Silvestre"],
        "effects": ["Potencia Psicoactiva", "Claridad Mental", "Euforia Radiante"],
        "activities": ["creativity", "nature_walk", "workout"],
        "description": "Superhíbrido resultado de cruzar dos de las genéticas más laureadas y potentes del mundo. Crecimiento explosivo, cogollos de dureza marmórea y un viaje psicoactivo de pura lucidez y dinamismo.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #06B6D4 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "serious-seriosa",
        "image": "img/serious-seriosa.webp",
        "name": "Seriosa",
        "aka": "Mimosa x AK-47 Serious",
        "bank": "Serious Seeds",
        "species": "Híbrida",
        "thc": 24, "cbd": 0.1,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 58, "rating": 4.9, "reviewsCount": 310,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "genetics": "Mimosa x AK-47",
        "lineage": "Mimosa x AK-47",
        "origin": "Holanda",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 35, "linalool": 20 },
        "aroma": "Masa horneada, naranja dulce y toques lilas afrutados",
        "flavors": ["Pastel de Naranja", "Bayas Dulces", "Masa Horneada"],
        "effects": ["Felicidad Desbordante", "Calma Corporal", "Bienestar Holístico"],
        "activities": ["social", "relax_sleep", "creativity"],
        "description": "Obra maestra moderna de Serious Seeds. Une la legendaria estructura y fiabilidad de AK-47 con los colores púrpuras y el perfil aromático a pastelería cítrica de Mimosa.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
    },
    {
        "id": "serious-motavation",
        "image": "img/serious-motavation.webp",
        "name": "Motavation",
        "aka": "Sensi Star x Warlock",
        "bank": "Serious Seeds",
        "species": "Índica",
        "thc": 22, "cbd": 0.3,
        "indicaPct": 75, "sativaPct": 25,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 280,
        "yieldIndoor": 480, "yieldOutdoor": 600,
        "genetics": "Sensi Star x Warlock",
        "lineage": "Sensi Star x Warlock",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "humulene": 20 },
        "aroma": "Bosque húmedo, trementina, terroso y medicinal",
        "flavors": ["Trementina Dulce", "Musgo", "Pino Terroso"],
        "effects": ["Sedación Profunda", "Desconexión Muscular", "Alivio del Dolor"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Creada originariamente por Magus Genetics y adoptada por Serious Seeds. Cruce de dos Índicas legendarias que regala una capa descomunal de resina y un efecto calmante de cuerpo entero.",
        "visualColor": "linear-gradient(135deg, #059669 0%, #064E3B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ripper-fuel-og-official",
        "image": "img/ripper-fuel-og.webp",
        "name": "Fuel OG",
        "aka": "NYC Diesel x Fire OG",
        "bank": "Ripper Seeds",
        "species": "Híbrida",
        "thc": 24, "cbd": 0.2,
        "indicaPct": 60, "sativaPct": 40,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 410,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "NYC Diesel x Fire OG",
        "lineage": "NYC Diesel x Fire OG",
        "origin": "España / USA",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 35, "caryophyllene": 20 },
        "aroma": "Gasolina pura, queroseno y cítricos metálicos",
        "flavors": ["Combustible Diésel", "Pomelo Metálico", "Kush Terroso"],
        "effects": ["Golpe Cerebral Inmediato", "Energía Vibrante", "Relajación Corporal"],
        "activities": ["creativity", "gaming", "social"],
        "description": "Variedad insignia de Ripper Seeds que combina dos líneas míticas: el sabor cítrico-metálico a queroseno de New York City Diesel con la contundencia terrosa y devastadora de Fire OG.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ripper-badazz",
        "image": "img/ripper-badazz.webp",
        "name": "Badazz",
        "aka": "Original OG Badazz",
        "bank": "Ripper Seeds",
        "species": "Índica",
        "thc": 23, "cbd": 0.1,
        "indicaPct": 80, "sativaPct": 20,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 350,
        "yieldIndoor": 500, "yieldOutdoor": 700,
        "genetics": "Original OG Badazz (OG Kush x Afghan)",
        "lineage": "Original OG Badazz",
        "origin": "España / California",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "limonene": 20 },
        "aroma": "Kush clásico californiano, terroso húmedo y limón denso",
        "flavors": ["Kush Terroso", "Limón Agrio", "Madera Quemada"],
        "effects": ["Sedación Corporal", "Tranquilidad Mental", "Apetito y Sueño"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Genética traída de Los Ángeles nacida en 1998 en Austin (Texas). Perfil Kush auténtico, cogollos no excesivamente densos pero repletos de glándulas resinosas de primer nivel.",
        "visualColor": "linear-gradient(135deg, #047857 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ghs-chemical-bride",
        "image": "img/ghs-chemical-bride.webp",
        "name": "Chemical Bride",
        "aka": "Wedding Cake x Chemdawg",
        "bank": "Green House Seed Co.",
        "species": "Híbrida",
        "thc": 27, "cbd": 0.1,
        "indicaPct": 60, "sativaPct": 40,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 380,
        "yieldIndoor": 550, "yieldOutdoor": 700,
        "genetics": "Wedding Cake x Chemdawg",
        "lineage": "Wedding Cake x Chemdawg",
        "origin": "Holanda / USA",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 30, "limonene": 25 },
        "aroma": "Crema agria, combustible denso y notas terrosas punzantes",
        "flavors": ["Tarta Agria", "Químico Gaseoso", "Dulce Cremoso"],
        "effects": ["Potencia Pesada", "Relajación Muscular Total", "Euforia Contemplativa"],
        "activities": ["relax_sleep", "gaming"],
        "description": "Creación moderna de Green House Seed Co. que fusiona la cremosidad dulce de Wedding Cake con la agresividad diésel-química de la legendaria Chemdawg.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ghs-arjans-strawberry-haze",
        "image": "img/ghs-arjans-strawberry-haze.webp",
        "name": "Arjan's Strawberry Haze",
        "aka": "Swiss Sativa x NL#5 x Haze",
        "bank": "Green House Seed Co.",
        "species": "Sativa",
        "thc": 20, "cbd": 1.0,
        "indicaPct": 40, "sativaPct": 60,
        "floweringDays": 70, "rating": 4.8, "reviewsCount": 410,
        "yieldIndoor": 600, "yieldOutdoor": 800,
        "genetics": "Swiss Sativa x NL#5 Haze x Erdbeer",
        "lineage": "NL#5 x Haze x Erdbeer",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "pinene": 30, "terpinolene": 25 },
        "aroma": "Fresa silvestre dulce, fondo especiado Haze y madera",
        "flavors": ["Fresa Silvestre", "Especias Haze", "Dulce Herbal"],
        "effects": ["Estimulación Social", "Alegría Radiante", "Expansión Creativa"],
        "activities": ["social", "nature_walk", "creativity"],
        "description": "Clásico del catálogo de Green House creado por Arjan Roskam. Su aroma penetrante a fresa salvaje madura se entrelaza con el empuje activo y jovial de la Haze clásica.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ace-old-timers-haze",
        "image": "img/ace-old-timers-haze.webp",
        "name": "Old Timer's Haze",
        "aka": "A5 / Original 1970s Haze",
        "bank": "ACE Seeds",
        "species": "Sativa",
        "thc": 20, "cbd": 0.1,
        "indicaPct": 0, "sativaPct": 100,
        "floweringDays": 115, "rating": 5.0, "reviewsCount": 340,
        "yieldIndoor": 400, "yieldOutdoor": 650,
        "genetics": "Landrace Colombiana x Landrace Tailandesa",
        "lineage": "Landrace Colombiana x Landrace Tailandesa",
        "origin": "España / Colombia / Tailandia",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 50, "ocimene": 30, "pinene": 20 },
        "aroma": "Incienso eclesiástico, especias orientales y licor de fruta madura",
        "flavors": ["Incienso Puro", "Fruta Fermentada", "Madera Noble"],
        "effects": ["Psicodelia Eléctrica", "Claridad Mística", "Energía Ilimitada"],
        "activities": ["creativity", "nature_walk", "meditation"],
        "description": "Reliquia botánica preservada por ACE Seeds. Línea Haze 100% Sativa autóctona de los años 70 sin hibridar con Índica. Efecto introspectivo y psicoactivo inalcanzable para híbridos comerciales modernos.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    },
    {
        "id": "dp-euforia",
        "image": "img/dp-euforia.webp",
        "name": "Euforia",
        "aka": "Skunk #1 Selección 1996",
        "bank": "Dutch Passion",
        "species": "Sativa",
        "thc": 21, "cbd": 0.2,
        "indicaPct": 10, "sativaPct": 90,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 460,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "Skunk #1 Selección 1996",
        "lineage": "Skunk #1 Selección 1996",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "pinene": 25 },
        "aroma": "Skunk clásico, floral penetrante y notas dulces azucaradas",
        "flavors": ["Skunk Floral", "Almizcle Dulce", "Toque Cítrico"],
        "effects": ["Euforia Extrema", "Desinhibición", "Risas y Alegría"],
        "activities": ["social", "gaming", "creativity"],
        "description": "Variedad histórica galardonada de Dutch Passion seleccionada en 1996 durante un programa de crianza de Skunk #1. Famosa mundialmente por inducir un estado de risa y felicidad eufórica incontenible.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "dp-jorges-diamonds-1",
        "image": "img/dp-jorges-diamonds-1.webp",
        "name": "Jorge's Diamonds #1",
        "aka": "Jorge Cervantes Special Selection",
        "bank": "Dutch Passion",
        "species": "Híbrida",
        "thc": 20, "cbd": 0.2,
        "indicaPct": 60, "sativaPct": 40,
        "floweringDays": 60, "rating": 4.8, "reviewsCount": 330,
        "yieldIndoor": 500, "yieldOutdoor": 650,
        "genetics": "Genética Secreta x Índica Rara",
        "lineage": "Genética Secreta x Índica Rara",
        "origin": "Holanda",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 35, "linalool": 20 },
        "aroma": "Frambuesa salvaje, miel silvestre y fondo dulce afrutado",
        "flavors": ["Frambuesa Madura", "Miel Dulce", "Cerezas"],
        "effects": ["Relajación Aterciopelada", "Calma Mental", "Bienestar Prolongado"],
        "activities": ["relax_sleep", "nature_walk", "social"],
        "description": "Desarrollada en estrecha colaboración con el legendario gurú del cultivo cannábico Jorge Cervantes. Una joya dulce rebosante de tricomas aromáticos y sabor a frutos silvestres.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
    },
    {
        "id": "cg-jet-fuel-gelato",
        "image": "img/cg-jet-fuel-gelato.webp",
        "name": "Jet Fuel Gelato",
        "aka": "Gelato 45 x High Octane / Jet Fuel G6",
        "bank": "Compound Genetics",
        "species": "Híbrida",
        "thc": 28, "cbd": 0.1,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 62, "rating": 5.0, "reviewsCount": 580,
        "yieldIndoor": 600, "yieldOutdoor": 850,
        "genetics": "Gelato 45 x (High Octane x Jet Fuel G6)",
        "lineage": "Gelato 45 x High Octane",
        "origin": "California / USA",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "aroma": "Gasolina premium, combustible diésel denso, helado cremoso y cítricos",
        "flavors": ["Diésel Cremoso", "Helado de Vainilla y Gas", "Pino Cítrico"],
        "effects": ["Euforia Potente", "Energía Cerebral", "Relajación Muscular"],
        "activities": ["gaming", "social", "creativity"],
        "description": "El buque insignia y columna vertebral genética de Compound Genetics. Es la progenitora de éxitos planetarios como Gastro Pop, Apples & Bananas y La Bomba. Rendimiento resinoso descomunal.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "hsc-blueberry-cupcake",
        "image": "img/hsc-blueberry-cupcake.webp",
        "name": "Blueberry Cupcake",
        "aka": "Blueberry Muffin x Wedding Cake",
        "bank": "Humboldt Seed",
        "species": "Híbrida",
        "thc": 30, "cbd": 0.1,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 58, "rating": 5.0, "reviewsCount": 490,
        "yieldIndoor": 600, "yieldOutdoor": 900,
        "genetics": "Blueberry Muffin x Wedding Cake",
        "lineage": "Blueberry Muffin x Wedding Cake",
        "origin": "California / USA",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 35, "limonene": 20 },
        "aroma": "Bizcocho de arándanos recién horneado, glaseado dulce y diésel",
        "flavors": ["Magdalena de Arándanos", "Vainilla Glaseada", "Toque Diésel"],
        "effects": ["Euforia Deliciosa", "Paz Corporal", "Bienestar Radiante"],
        "activities": ["relax_sleep", "gaming", "social"],
        "description": "Fusión estelar de Humboldt Seed Company que eleva el aroma inconfundible a repostería de arándanos de Blueberry Muffin con la potencia extrema y densidad cristalina de Wedding Cake.",
        "visualColor": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
    },
    {
        "id": "hsc-poddy-mouth",
        "image": "img/hsc-poddy-mouth.webp",
        "name": "Poddy Mouth",
        "aka": "Humboldt Pound Cake x Mountaintop Mint",
        "bank": "Humboldt Seed",
        "species": "Híbrida",
        "thc": 28, "cbd": 0.1,
        "indicaPct": 50, "sativaPct": 50,
        "floweringDays": 55, "rating": 4.9, "reviewsCount": 380,
        "yieldIndoor": 550, "yieldOutdoor": 800,
        "genetics": "Humboldt Pound Cake x Mountaintop Mint",
        "lineage": "Humboldt Pound Cake x Mountaintop Mint",
        "origin": "California / USA",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 35, "pinene": 20 },
        "aroma": "Menta fresca, masa frita dulce y combustible terroso",
        "flavors": ["Menta Glacial", "Masa Dulce", "Gas Terroso"],
        "effects": ["Claridad Despejada", "Alivio de Tensión", "Motivación Serena"],
        "activities": ["nature_walk", "workout", "creativity"],
        "description": "Destacada variedad moderna criada en el condado de Humboldt con trichomas deslumbrantes en cabezas gigantes. Sabor refrescante mentolado con fondo terroso a repostería dulce.",
        "visualColor": "linear-gradient(135deg, #06B6D4 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
    },
    {
        "id": "ihg-flavors",
        "image": "img/ihg-flavors.webp",
        "name": "Flavors",
        "aka": "Slurricane #7 x Apple Fritter",
        "bank": "In-House Genetics",
        "species": "Híbrida",
        "thc": 28, "cbd": 0.1,
        "indicaPct": 60, "sativaPct": 40,
        "floweringDays": 62, "rating": 4.9, "reviewsCount": 420,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "Slurricane #7 x Apple Fritter",
        "lineage": "Slurricane #7 x Apple Fritter",
        "origin": "USA",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "aroma": "Tarta de manzana al horno, azúcar moreno y resina dulce",
        "flavors": ["Tarta de Manzana", "Azúcar Tostado", "Frutas Dulces"],
        "effects": ["Euforia Cálida", "Relajación Pesada", "Felicidad Profunda"],
        "activities": ["relax_sleep", "social", "gaming"],
        "description": "Creación de élite de In-House Genetics cruzando su insigne clon Slurricane #7 con Apple Fritter. Cobertura de tricomas blanco escarchado con un sabor gourmet irrepetible.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
    },
    {
        "id": "sjg-biscotti",
        "image": "img/sjg-biscotti.webp",
        "name": "Biscotti",
        "aka": "Gelato #25 x South Florida OG (Original Cut)",
        "bank": "Seed Junky Genetics",
        "species": "Índica",
        "thc": 27, "cbd": 0.1,
        "indicaPct": 80, "sativaPct": 20,
        "floweringDays": 64, "rating": 5.0, "reviewsCount": 610,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "genetics": "Gelato #25 x South Florida OG",
        "lineage": "Gelato #25 x South Florida OG",
        "origin": "California / USA",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "aroma": "Galleta tostada de mantequilla, especias dulces y combustible",
        "flavors": ["Galleta de Mantequilla", "Especias Dulces", "Diésel Suave"],
        "effects": ["Calma Cerebral Intensa", "Pesadez Corporal", "Relajación Nocturna"],
        "activities": ["relax_sleep", "gaming", "meditation"],
        "description": "La creación original e indiscutible del breeder JBeezy (Seed Junky Genetics) que conquistó la escena cannábica de California y el mundo entero. Flores densas y oscuras con pistilos anaranjados y resina extrema.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #4B5563 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
    },
    {
        "id": "dna-skywalker-kush",
        "image": "img/dna-skywalker-kush.webp",
        "name": "Skywalker Kush",
        "aka": "Skywalker x The OG #18",
        "bank": "DNA Genetics",
        "species": "Índica",
        "thc": 26, "cbd": 0.2,
        "indicaPct": 70, "sativaPct": 30,
        "floweringDays": 63, "rating": 5.0, "reviewsCount": 570,
        "yieldIndoor": 600, "yieldOutdoor": 800,
        "genetics": "Skywalker x The OG #18",
        "lineage": "Skywalker x The OG #18",
        "origin": "Ámsterdam / California",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "myrcene": 35, "limonene": 20 },
        "aroma": "Combustible Kush punzante, limón denso, notas terrosas y pino salvaje",
        "flavors": ["OG Kush Clásico", "Gasolina y Limón", "Tierra Húmeda"],
        "effects": ["Potencia Estelar", "Sedación Física Contundente", "Paz Mental"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Una de las variedades más laureadas de DNA Genetics y Reserva Privada. Cruce de la legendaria Skywalker con el clon élite The OG #18 que maximiza la producción de resina y proporciona un sabor a gasolina y cítrico inolvidable.",
        "visualColor": "linear-gradient(135deg, #059669 0%, #1F2937 100%)",
        "bgPattern": "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
    }
]

# Ensure each image exists in img/ directory
BANK_IMG_FALLBACK = {
    "sensi-nl5-haze": "sensi-jack-herer.webp",
    "bf-mimosa-evo": "barneys-mimosa-evo-bud-official.webp",
    "bf-glookies": "bf-dos-si-dos-33.webp",
    "ss-cream-47": "sweet-cream-caramel.webp",
    "ss-jack-47": "sweet-black-jack.webp",
    "serious-seriosa": "serious-ak-47.webp",
    "serious-motavation": "serious-sensi-star.webp",
    "ripper-fuel-og-official": "ripper-fuel-og.webp",
    "ripper-badazz": "ripper-zombie-kush.webp",
    "ghs-chemical-bride": "ghs-super-lemon-haze.webp",
    "ghs-arjans-strawberry-haze": "ghs-hawaiian-snow.webp",
    "ace-old-timers-haze": "aceseeds-panama.webp",
    "dp-euforia": "dp-powerplant.webp",
    "dp-jorges-diamonds-1": "dp-blueberry.webp",
    "cg-jet-fuel-gelato": "cpg-apples-and-bananas.webp",
    "hsc-blueberry-cupcake": "hso-blue-dream.webp",
    "hsc-poddy-mouth": "hso-trainwreck.webp",
    "ihg-flavors": "ihg-slurricane.webp",
    "sjg-biscotti": "sjg-kush-mints.webp",
    "dna-skywalker-kush": "dna-kosher-kush.webp"
}

for s in NEW_20_STRAINS:
    fname = os.path.basename(s["image"])
    target_path = os.path.join(IMG_DIR, fname)
    if not os.path.exists(target_path) or os.path.getsize(target_path) < 5000:
        # Fallback copy
        fallback_file = BANK_IMG_FALLBACK.get(s["id"])
        if fallback_file and os.path.exists(os.path.join(IMG_DIR, fallback_file)):
            src = os.path.join(IMG_DIR, fallback_file)
        else:
            # First available webp
            src = os.path.join(IMG_DIR, "bf-dos-si-dos-33.webp")
        try:
            im = Image.open(src).convert("RGB")
            im.save(target_path, "WEBP", quality=88)
            print(f"Prepared image for {s['id']} from {os.path.basename(src)}")
        except Exception as e:
            print(f"Error copying image for {s['id']}: {e}")

# Format new strains into JS code
js_blocks = []
key_order = [
    'id', 'image', 'name', 'aka', 'bank', 'species', 'thc', 'cbd',
    'indicaPct', 'sativaPct', 'floweringDays', 'rating', 'reviewsCount',
    'yieldIndoor', 'yieldOutdoor', 'genetics', 'lineage', 'origin',
    'dominantTerpene', 'terpenes', 'aroma', 'flavors', 'effects',
    'activities', 'description', 'visualColor', 'bgPattern'
]

for s in NEW_20_STRAINS:
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

# Find the closing of STRAINS_DATABASE array: last \n]; in file
pos = text.rfind('\n];')
if pos == -1:
    print("Error: Could not locate end of STRAINS_DATABASE in data.js")
    sys.exit(1)

new_text = text[:pos] + code_to_insert + text[pos:]

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Successfully inserted {len(NEW_20_STRAINS)} strains into {DATA_JS}")
