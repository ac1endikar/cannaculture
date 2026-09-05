// CannaCatalog 2.0 Bundled Version for Direct File Access

// --- data.js ---
// CannaCatalog 2.0 ULTRA MAX — Base de datos extendida: +292 cepas de 25 bancos premium
// Bancos: Dinafem Seeds · BSF Seeds · Ripper Seeds · Barney's Farm · Sweet Seeds · Royal Queen Seeds ·
//         Dutch Passion · Philosopher Seeds · Humboldt Seed · 00 Seeds Bank · Buddha Seeds · R-Kiem Seeds · Positronics Seeds · ACE Seeds · Pyramid Seeds · Blimburn Seeds · Genehtik Seeds · Heavyweight Seeds · Cannabiogen · Sensi Seeds · Green House Seed Co. · Serious Seeds · TH Seeds · Paradise Seeds · DNA Genetics

const TERPENES_INFO = {
  myrcene: {
    name: "Mirceno",
    aroma: "Terroso, herbal, clavo de olor, mango",
    effects: "Sedante, relajante muscular, calma profunda ('Couch-lock')",
    boilPoint: 167,
    color: "#10B981"
  },
  limonene: {
    name: "Limoneno",
    aroma: "Cítrico fresco, limón, naranja",
    effects: "Eufórico, elevador del ánimo, antiestrés, energía mental",
    boilPoint: 176,
    color: "#F59E0B"
  },
  caryophyllene: {
    name: "Cariofileno",
    aroma: "Pimentado, picante, amaderado",
    effects: "Alivio físico, antiinflamatorio, reduce ansiedad social",
    boilPoint: 130,
    color: "#EF4444"
  },
  pinene: {
    name: "Pineno",
    aroma: "Pino fresco, romero, bosque",
    effects: "Claridad mental, retención de memoria, enfoque láser",
    boilPoint: 155,
    color: "#06B6D4"
  },
  linalool: {
    name: "Linalool",
    aroma: "Floral, lavanda, especiado dulce",
    effects: "Tranquilidad, alivio de tensión emocional, sueño reparador",
    boilPoint: 198,
    color: "#8B5CF6"
  },
  terpinolene: {
    name: "Terpinoleno",
    aroma: "Herbal dulce, cítrico complejo, pino suave",
    effects: "Creatividad efervescente, estimulación cognitiva",
    boilPoint: 186,
    color: "#EC4899"
  },
  ocimene: {
    name: "Ocimeno",
    aroma: "Dulce floral, tropical, herbal",
    effects: "Antiviral, energizante suave, antiséptico natural",
    boilPoint: 66,
    color: "#34D399"
  },
  humulene: {
    name: "Humuleno",
    aroma: "Terroso, amaderado, lúpulo",
    effects: "Supresor del apetito, antiinflamatorio, calmante",
    boilPoint: 106,
    color: "#A78BFA"
  }
};

const ACTIVITIES_DATA = [
  {
    id: "nature_walk",
    title: "🌲 Safari de Caminatas & Naturaleza",
    description: "Conexión sensorial profunda con el entorno, senderos y aire libre.",
    preferredTerpenes: ["limonene", "pinene", "terpinolene"],
    recommendedSpecies: ["Indica", "Híbrida", "Sativa"],
    idealThcRange: [15, 24]
  },
  {
    id: "gaming",
    title: "🎮 Sesión Gaming & Co-Op",
    description: "Reflejos ágiles, inmersión táctica en videojuegos o diversión multijugador.",
    preferredTerpenes: ["pinene", "caryophyllene", "limonene"],
    recommendedSpecies: ["Híbrida", "Sativa"],
    idealThcRange: [18, 28]
  },
  {
    id: "creativity",
    title: "🎨 Creación Artística & Música",
    description: "Flujo de ideas sin filtros, composición musical y diseño visual.",
    preferredTerpenes: ["terpinolene", "limonene", "myrcene"],
    recommendedSpecies: ["Sativa", "Híbrida"],
    idealThcRange: [16, 26]
  },
  {
    id: "social",
    title: "🎉 Social & Conversaciones Épicas",
    description: "Risas, soltura social, charlas profundas con amigos.",
    preferredTerpenes: ["caryophyllene", "limonene"],
    recommendedSpecies: ["Híbrida", "Sativa"],
    idealThcRange: [14, 24]
  },
  {
    id: "relax_sleep",
    title: "🌙 Relax Profundo & Cine / Sueño",
    description: "Desconexión corporal total, maratón de películas y descanso reparador.",
    preferredTerpenes: ["myrcene", "linalool", "caryophyllene"],
    recommendedSpecies: ["Indica"],
    idealThcRange: [20, 30]
  },
  {
    id: "meditation",
    title: "🧘 Meditación & Yoga",
    description: "Introspección, cuerpo y mente alineados, consciencia plena.",
    preferredTerpenes: ["linalool", "myrcene", "ocimene"],
    recommendedSpecies: ["Indica", "Híbrida"],
    idealThcRange: [12, 20]
  },
  {
    id: "workout",
    title: "🏋️ Deporte & Entrenamiento",
    description: "Pre o post-workout, motivación física y recuperación muscular.",
    preferredTerpenes: ["pinene", "limonene", "humulene"],
    recommendedSpecies: ["Sativa", "Híbrida"],
    idealThcRange: [14, 22]
  }
];

const STRAINS_DATABASE = [
  {
id: "ripper-kmintz",
    image: "img/ripper-kmintz-plant.webp",
    name: "Kmintz",
    aka: "Zkittlez x Kush Mints",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 60, rating: 4.9, reviewsCount: 480,
    genetics: "Zkittlez x Kush Mints",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, caryophyllene: 30, myrcene: 25 },
    flavors: ["Caramelo de Frutas", "Menta Fresca", "Dulce Cítrico"],
    effects: ["Relajación Corporal", "Euforia Suave", "Bienestar"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Obra maestra premiada (1er Spannabis Champions Cup 2020). Cruce entre Zkittlez y Kush Mints: densidad de resina extrema, colores violetas profundos y un sabor a caramelo frutal mentolado inconfundible.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-zombie-kush",
    image: "img/ripper-zombie-kush-flowering.webp",
    name: "Zombie Kush",
    aka: "Sideral x Bubba Kush",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 22, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 55, rating: 4.9, reviewsCount: 610,
    genetics: "(Lavender Kush x Amnesia) x Bubba Kush",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Tierra Húmeda", "Hachís Afgano", "Cítrico Dulce"],
    effects: ["Sedación Profunda", "Alivio Físico", "Sueño Reparador"],
    activities: ["relax_sleep"],
    description: "Mítica cepa Índica con multitud de premios en concursos de extracción. Perfil terroso clásico tipo Kush con matices cítricos y un efecto relajante de gran potencia.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-radical-juice",
    image: "img/ripper-radical-juice-plant.webp",
    name: "Radical Juice",
    aka: "Tropicana Cookies x Runtz",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 23, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 65, rating: 4.8, reviewsCount: 390,
    genetics: "Tropicana Cookies x Runtz",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 30, caryophyllene: 20 },
    flavors: ["Zumo Tropical", "Naranja Dulce", "Caramelo"],
    effects: ["Euforia Frutal", "Relax Sin Pesadez", "Creatividad"],
    activities: ["nature_walk", "creativity", "social"],
    description: "Explosión de terpenos que evoca un zumo recién exprimido. Cogollos púrpuras con aroma a naranja dulce y caramelos tropicales. Ideal también para extracciones de alta calidad.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-washing-machine",
    image: "img/ripper-washing-machine.webp",
    name: "Washing Machine",
    aka: "UK Cheese x Bubba Kush",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 21, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 420,
    genetics: "UK Cheese x Bubba Kush",
    origin: "España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Regaliz Dulce", "Queso Maduro", "Tierra Especiada"],
    effects: ["Calma Muscular", "Relajación Extrema", "Desconexión Total"],
    activities: ["relax_sleep"],
    description: "Descomunal producción de tricomas y resina. Inconfundible aroma a regaliz dulce y fondo terroso de queso curado. Una de las favoritas para producción de rosin.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-sour-ripper",
    image: "img/ripper-sour-ripper-bud.webp",
    name: "Sour Ripper",
    aka: "Sour Diesel Selection",
    bank: "Ripper Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.9, reviewsCount: 530,
    genetics: "Selección Sour Diesel de élite",
    origin: "España / Nueva York",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, caryophyllene: 25, pinene: 20 },
    flavors: ["Gasolina / Combustible", "Cítrico Ácido", "Punzante"],
    effects: ["Energía Cerebral", "Motivación", "Claridad Mental"],
    activities: ["nature_walk", "gaming", "creativity"],
    description: "Versión perfeccionada de Sour Diesel por Ripper Seeds. Aroma penetrante a combustible con matices de limón ácido. Efecto estimulante de larga duración, sin ansiedad.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-ripper-haze",
    image: "img/ripper-haze-flowering.webp",
    name: "Ripper Haze",
    aka: "Amnesia Haze Selection (Amnesia Ripping)",
    bank: "Ripper Seeds",
    species: "Sativa",
    thc: 24, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 65, rating: 4.9, reviewsCount: 640,
    genetics: "Selección Amnesia Haze de élite",
    origin: "España / Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Limón Cítrico", "Incienso Haze", "Especias Frescas"],
    effects: ["Subidón Psicoactivo", "Claridad Mental", "Energía Efervescente"],
    activities: ["creativity", "nature_walk", "social"],
    description: "Una de las reinas fundacionales de Ripper Seeds (1er premio Cannabis Champions Cup). Selección legendaria de Amnesia Haze ultra potente con inconfundible aroma a limón incensado.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-hawaiian-wave",
    image: "img/ripper-hawaiian-wave-bud.webp",
    name: "Hawaiian Wave",
    aka: "Hawaiian Haze x Double Glock",
    bank: "Ripper Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 700,
    floweringDays: 75, rating: 4.7, reviewsCount: 310,
    genetics: "Hawaiian Haze x Double Glock",
    origin: "España / Hawái",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, pinene: 30, myrcene: 25 },
    flavors: ["Frutos Rojos", "Incienso Haze", "Metálico Fresco"],
    effects: ["Euforia Psicoactiva", "Inspiración", "Viaje Sensorial"],
    activities: ["nature_walk", "creativity", "meditation"],
    description: "La Sativa más tropical de Ripper Seeds. Combina aromas dulces de bayas hawaianas con la fuerza cerebral de Double Glock. Efecto prolongado y muy espacial.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-double-glock",
    image: "img/ripper-double-glock-plant.webp",
    name: "Double Glock",
    aka: "Índica Afgana 100%",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 20, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.8, reviewsCount: 290,
    genetics: "Variedad Landrace Afgana Pura",
    origin: "Afganistán / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 60, caryophyllene: 25, pinene: 15 },
    flavors: ["Hachís Dulce", "Tierra Especiada", "Madera"],
    effects: ["Sedación Total", "Relajación Muscular", "Calma Absoluta"],
    activities: ["relax_sleep", "meditation"],
    description: "Índica 100% pura y estable. Planta afgana homogénea con sabor a hachís tradicional del Hindu Kush. La base genética de múltiples creaciones de Ripper Seeds.",
    visualColor: "linear-gradient(135deg, #047857 0%, #064E3B 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-criminal-plus",
    image: "img/ripper-criminal-plus-plant.webp",
    name: "Criminal +",
    aka: "Critical Mass x Double Glock",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 21, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 50, rating: 4.9, reviewsCount: 580,
    genetics: "Critical Mass x Double Glock",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 40, myrcene: 35, caryophyllene: 25 },
    flavors: ["Frutal Dulce", "Cítrico Maduro", "Fondo Skunk"],
    effects: ["Relajación Rápida", "Pesadez Placentera", "Aumento de Apetito"],
    activities: ["relax_sleep", "social"],
    description: "El hit comercial de Ripper Seeds: floración ultra rápida (50 días) y producción gigantesca. Perfecta para cultivos de alto rendimiento con cogollos extra densos y resina generosa.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-toxic",
    image: "img/ripper-toxic-bud.webp",
    name: "Toxic",
    aka: "Ripper Haze x Criminal +",
    bank: "Ripper Seeds",
    species: "Híbrida",
    thc: 20, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 370,
    genetics: "Ripper Haze x Criminal +",
    origin: "España",
    dominantTerpene: "pinene",
    terpenes: { pinene: 40, terpinolene: 30, limonene: 30 },
    flavors: ["Incienso Cítrico", "Pino Silvestre", "Especias"],
    effects: ["Equilibrio Mental y Físico", "Enfoque", "Sociabilidad"],
    activities: ["nature_walk", "gaming", "social"],
    description: "Híbrido polivalente y muy resistente. Combina la efervescencia aromática de Haze con la rapidez y producción de Criminal +. Muy apreciada por cultivadores exigentes.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-brain-cake",
    image: "img/ripper-brain-cake-plant.webp",
    name: "Brain Cake",
    aka: "Do-Si-Dos S1",
    bank: "Ripper Seeds",
    species: "Híbrida",
    thc: 25, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 65, rating: 4.9, reviewsCount: 440,
    genetics: "Face Off OG x OGKB (Do-Si-Dos lineage)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, linalool: 20 },
    flavors: ["Galleta Dulce", "Tierra Kush", "Notas Gaseosas"],
    effects: ["Potencia Cerebral", "Placer Físico", "Euforia Dulce"],
    activities: ["gaming", "social", "creativity"],
    description: "Selección S1 americana de Do-Si-Dos. Destaca por su altísimo THC y cogollos completamente nevados en resina, con un sabor a galleta terrosa de Cookies que engancha.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-kroma",
    image: "img/ripper-kroma-plant.webp",
    name: "Kroma",
    aka: "Kmintz x Zkittlez",
    bank: "Ripper Seeds",
    species: "Híbrida",
    thc: 26, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 60, rating: 5.0, reviewsCount: 220,
    genetics: "Kmintz x Zkittlez",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, caryophyllene: 30, terpinolene: 20 },
    flavors: ["Caramelo Ácido", "Frutas Rojas Candy", "Menta Fría"],
    effects: ["Euforia Cerebral Intensa", "Relajación Corporal", "Energía Creativa"],
    activities: ["creativity", "gaming", "social"],
    description: "Cruce brutal entre Gorilla Glue y Girl Scout Cookies. Potencia demoledora con niveles de THC de hasta el 31%. Densidad de tricomas y resina insuperable.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-sideral",
    image: "img/ripper-sideral.webp",
    gallery: ["img/ripper-sideral.webp"],
    name: "Sideral",
    aka: "Mazar x Critical Mass Selection",
    bank: "Ripper Seeds",
    species: "Híbrida",
    thc: 20, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.7, reviewsCount: 360,
    genetics: "Mazar x Critical Mass (Ripper Selection)",
    origin: "España / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, pinene: 20 },
    flavors: ["Tierra Dulce", "Hachís Suave", "Cedro Oscuro"],
    effects: ["Relajación Equilibrada", "Bienestar Físico", "Paz Mental"],
    activities: ["relax_sleep", "social", "meditation"],
    description: "Uno de los pilares fundacionales de Ripper Seeds. Híbrida equilibrada entre Mazar y Critical Mass, con un perfil terroso y un efecto reconfortante. La madre de Zombie Kush.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-candygaz",
    image: "img/ripper-candygaz.webp",
    name: "CandyGaz",
    aka: "Gelato x Gas OG",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 27, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 63, rating: 4.9, reviewsCount: 310,
    genetics: "Gelato 41 x Gas OG (Ripper Selection)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, myrcene: 25 },
    flavors: ["Caramelo de Gas", "Frutas Candy", "Diesel Dulce"],
    effects: ["Subidón Potente", "Relajación Profunda", "Euforia Cremosa"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Gelato 41 cruzada con selección de Gas OG: 27% THC, cogollos gigantes resinosos con un sabor que mezcla caramelo y gasolina. Una de las joyas premium más recientes de Ripper.",
    visualColor: "linear-gradient(135deg, #A78BFA 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(167,139,250,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-omg",
    image: "img/ripper-omg.webp",
    name: "OMG",
    aka: "Orange Mints Gelato",
    bank: "Ripper Seeds",
    species: "Híbrida",
    thc: 25, cbd: 0.2,
    yieldIndoor: 520, yieldOutdoor: 720,
    floweringDays: 62, rating: 4.8, reviewsCount: 265,
    genetics: "Pineapple Mints x Kmintz",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, terpinolene: 35, caryophyllene: 20 },
    flavors: ["Naranja con Menta", "Piña Tropical", "Cremoso Dulce"],
    effects: ["Euforia Equilibrada", "Creatividad Mental", "Sociabilidad"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Un nombre que lo dice todo: Orange Mints Gelato. Cruce de Pineapple Mints con Kmintz que ofrece un sabor frutal-mentolado de alta gama y un efecto híbrido equilibrado y positivo.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-jungle-punch",
    image: "img/ripper-jungle-punch-flowering.webp",
    gallery: ["img/ripper-jungle-punch.webp"],
    name: "Jungle Punch",
    aka: "Tropicana Cookies x Banana Punch",
    bank: "Ripper Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.3,
    yieldIndoor: 480, yieldOutdoor: 680,
    floweringDays: 70, rating: 4.7, reviewsCount: 190,
    genetics: "Tropicana Cookies x Banana Punch",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, terpinolene: 30, pinene: 15 },
    flavors: ["Plátano Tropical", "Naranja Cremosa", "Bayas Silvestres"],
    effects: ["Energía Mental", "Alegría Social", "Creatividad Efervescente"],
    activities: ["nature_walk", "creativity", "social", "workout"],
    description: "Explosión de frutas tropicales con un efecto Sativa estimulante y muy alegre. Ideal para actividades diurnas. Aroma a punch de frutas que se nota desde metros de distancia.",
    visualColor: "linear-gradient(135deg, #34D399 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(52,211,153,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-mimosa-orange-punch",
    image: "img/bf-mimosa-orange-punch.webp",
    name: "Mimosa x Orange Punch",
    aka: "Mimosa EVO x Orange Punch",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 30, cbd: 0.1,
    yieldIndoor: 700, yieldOutdoor: 1500,
    floweringDays: 58, rating: 5.0, reviewsCount: 820,
    genetics: "Mimosa EVO x Orange Punch",
    origin: "Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, caryophyllene: 25, linalool: 20 },
    flavors: ["Naranja Dulce", "Mandarina", "Caramelo Cítrico"],
    effects: ["Euforia Explosiva", "Relajación Corporal", "Felicidad Pura"],
    activities: ["social", "nature_walk", "gaming"],
    description: "La sensación mundial de Barney's Farm. Hasta 30% THC y producción gigantesca (1500g/planta outdoor). Aroma intenso a naranjas dulces con un subidón que impresiona hasta a los más experimentados.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-runtz-muffin",
    image: "img/bf-runtz-muffin.webp",
    name: "Runtz Muffin",
    aka: "Zkittlez x Gelato x Orange Punch",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 29, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 60, rating: 4.9, reviewsCount: 650,
    genetics: "Zkittlez x Gelato #33 x Orange Punch",
    origin: "Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, linalool: 20 },
    flavors: ["Tarta de Maracuyá", "Piña Dulce", "Caramelo Cremoso"],
    effects: ["Relax Físico Profundo", "Euforia Mental", "Imaginación"],
    activities: ["relax_sleep", "creativity"],
    description: "Postre cannábico premium. Triple genética Zkittlez-Gelato-Orange Punch en perfecta armonía. Sabor tropical cremoso a pastel de frutas exóticas y un subidón potente que abraza el cuerpo.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-dos-si-dos-33",
    image: "img/bf-dos-si-dos-33-bud.webp",
    name: "Dos Si Dos 33",
    aka: "Do-Si-Dos x Gelato #33",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 28, cbd: 0.2,
    yieldIndoor: 700, yieldOutdoor: 2000,
    floweringDays: 60, rating: 4.9, reviewsCount: 710,
    genetics: "Do-Si-Dos x Gelato #33 x Sunset Sherbet",
    origin: "Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 40, caryophyllene: 35, myrcene: 25 },
    flavors: ["Sherbet de Menta", "Galleta Terrosa", "Cítrico Dulce"],
    effects: ["Sedación Placentera", "Paz Mental", "Bienestar Total"],
    activities: ["relax_sleep", "gaming"],
    description: "Colores púrpuras y verdes oscuros empapados en resina. Aroma mentolado y dulzor pastelero. Producción exterior récord de 2kg/planta. Una de las más vendidas de Europa.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-pineapple-express",
    image: "img/bf-pineapple-express-bud.webp",
    name: "Pineapple Express",
    aka: "Hawaiian x Trainwreck",
    bank: "Barney's Farm",
    species: "Sativa",
    thc: 24, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 750,
    floweringDays: 60, rating: 4.8, reviewsCount: 540,
    genetics: "Hawaiian Sativa x Trainwreck",
    origin: "Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, limonene: 35, pinene: 20 },
    flavors: ["Piña Tropical Fresca", "Mango Maduro", "Cedro Suave"],
    effects: ["Energía Social", "Alegría Explosiva", "Creatividad Estimulada"],
    activities: ["social", "nature_walk", "creativity", "workout"],
    description: "Icónica en todo el planeta por su sabor frutal a piña tropical madura y efecto estimulante de larga duración. Perfecta para días de actividad física y reuniones sociales.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-laughing-buddha",
    image: "img/bf-laughing-buddha-plant.webp",
    name: "Laughing Buddha",
    aka: "Thai x Jamaican Sativa",
    bank: "Barney's Farm",
    species: "Sativa",
    thc: 22, cbd: 0.5,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 77, rating: 4.8, reviewsCount: 680,
    genetics: "Thai Sativa x Jamaican Sativa",
    origin: "Ámsterdam / Tailandia",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Frutas Tropicales", "Dulce Floral", "Madera Especiada"],
    effects: ["Euforia Alegre", "Risa Espontánea", "Bienestar General"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Ganadora del High Times Cannabis Cup 2003. Pura Sativa asiática con un efecto alegre y eufórico que eleva el ánimo durante horas. El nombre no miente.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-critical-kush",
    image: "img/bf-critical-kush-plant.webp",
    name: "Critical Kush",
    aka: "Critical Mass x OG Kush",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 25, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 56, rating: 4.9, reviewsCount: 890,
    genetics: "Critical Mass x OG Kush",
    origin: "Ámsterdam / California",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["OG Terroso", "Pino Especiado", "Limón Kush"],
    effects: ["Relajación Corporal Profunda", "Sedación Moderada", "Bienestar"],
    activities: ["relax_sleep", "gaming"],
    description: "El clásico de Barney's Farm. Critical Mass mezclada con OG Kush: robusta, muy productiva (1000g/planta outdoor) y con un sabor OG puro y reconfortante.",
    visualColor: "linear-gradient(135deg, #047857 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-sherbet-queen",
    image: "img/bf-sherbet-queen-plant.webp",
    name: "Sherbet Queen",
    aka: "GSC x Pink Panties",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 24, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 420,
    genetics: "Girl Scout Cookies x Pink Panties",
    origin: "Ámsterdam / San Francisco",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 30, linalool: 25 },
    flavors: ["Helado de Frutas", "Vainilla Cremosa", "Dulce Terroso"],
    effects: ["Relajación Eufórica", "Bienestar Corporal", "Alegría"],
    activities: ["social", "relax_sleep", "creativity"],
    description: "La reina del sabor dulce de Barney's Farm. GSC cruzada con Pink Panties: cogollos coloridos con aroma a helado cremoso y un efecto que equilibra calma y euforia.",
    visualColor: "linear-gradient(135deg, #F472B6 0%, #A78BFA 100%)",
    bgPattern: "radial-gradient(circle, rgba(244,114,182,0.2) 0%, transparent 70%)"
  },
  {
id: "sweet-green-poison",
    image: "img/sweet-green-poison-plant.webp",
    name: "Green Poison",
    aka: "Selección Índica Rápida",
    bank: "Sweet Seeds",
    species: "Indica",
    thc: 20, cbd: 0.9,
    yieldIndoor: 650, yieldOutdoor: 700,
    floweringDays: 42, rating: 4.9, reviewsCount: 890,
    genetics: "Selección genéticas Índicas de floración ultra rápida",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, limonene: 30, caryophyllene: 25 },
    flavors: ["Mango Maduro", "Tropical Intenso", "Fondo Skunk Dulce"],
    effects: ["Euforia Alegre", "Relajación Corporal", "Paz"],
    activities: ["nature_walk", "social", "relax_sleep"],
    description: "Mítica cepa de Sweet Seeds con floración ultra veloz de solo 6 semanas. Sabor dulce a frutas tropicales con efecto eufórico muy placentero. Una de las Índicas más populares de España.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "sweet-cream-caramel",
    image: "img/sweet-cream-caramel.webp",
    name: "Cream Caramel",
    aka: "BlueBlack x Maple Leaf x White Rhino",
    bank: "Sweet Seeds",
    species: "Indica",
    thc: 20, cbd: 1.6,
    yieldIndoor: 550, yieldOutdoor: 600,
    floweringDays: 56, rating: 4.9, reviewsCount: 950,
    genetics: "BlueBlack x Maple Leaf Indica x White Rhino",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Caramelo de Mantequilla", "Golosinas", "Tierra Dulce"],
    effects: ["Antiestrés", "Relajante Muscular", "Sueño Placentero"],
    activities: ["relax_sleep", "meditation"],
    description: "Una de las cepas más premiadas de la historia. Aroma inconfundible a caramelo y golosinas dulces con CBD elevado que suaviza el efecto haciéndolo más medicinal y reconfortante.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "sweet-gorilla-girl",
    image: "img/sweet-gorilla-girl.webp",
    name: "Gorilla Girl",
    aka: "Gorilla Glue x GSC",
    bank: "Sweet Seeds",
    species: "Híbrida",
    thc: 25, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 600,
    floweringDays: 63, rating: 4.8, reviewsCount: 490,
    genetics: "Gorilla Glue x Thin Mint Girl Scout Cookies",
    origin: "España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, limonene: 30, pinene: 20 },
    flavors: ["Madera de Ciprés", "Mentol Cítrico", "Tierra"],
    effects: ["Potencia Demoledora", "Euforia Cerebral", "Descanso Físico"],
    activities: ["gaming", "creativity"],
    description: "Cruce de titanes: GG#4 con Thin Mint GSC. THC demoledor y cogollos completamente blancos de resina. Sabor a madera especiada con matices mentolados que sorprende siempre.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "sweet-black-jack",
    image: "img/sweet-black-jack-plant.webp",
    name: "Black Jack",
    aka: "Black Domina x Jack Herer",
    bank: "Sweet Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.8,
    yieldIndoor: 575, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 540,
    genetics: "Black Domina x Jack Herer",
    origin: "España / Holanda",
    dominantTerpene: "pinene",
    terpenes: { pinene: 45, limonene: 35, terpinolene: 20 },
    flavors: ["Pino Fresco y Especiado", "Madera Negra", "Floral Limpio"],
    effects: ["Claridad Mental", "Motivación Activa", "Energía Física"],
    activities: ["nature_walk", "workout", "creativity"],
    description: "Jack Herer cruzado con la potencia de Black Domina. Efecto energizante y claro, ideal para actividades creativas y deportivas durante el día. CBD suave y equilibrador.",
    visualColor: "linear-gradient(135deg, #1E40AF 0%, #06B6D4 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,64,175,0.2) 0%, transparent 70%)"
  },
  {
id: "sweet-tropicanna-poison",
    image: "img/sweet-tropicanna-poison-plant.webp",
    name: "Tropicanna Poison",
    aka: "Tropicanna Cookies x Poison",
    bank: "Sweet Seeds",
    species: "Híbrida",
    thc: 23, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 700,
    floweringDays: 62, rating: 4.8, reviewsCount: 380,
    genetics: "Tropicanna Cookies x Green Poison",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 30, myrcene: 20 },
    flavors: ["Naranja Ácida", "Tropical Cremoso", "Mango Verde"],
    effects: ["Euforia Naranja", "Creatividad Espontánea", "Bienestar"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Crossover perfecto de Sweet Seeds: la Tropicanna Cookies californiana con su Green Poison estrella. Explosión de citrus tropical con efecto híbrido alegre y muy creativo.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "sweet-s5-haze",
    image: "img/sweet-s5-haze.webp",
    name: "S5 Haze",
    aka: "Neville's Haze x Shiva",
    bank: "Sweet Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 70, rating: 4.7, reviewsCount: 290,
    genetics: "Neville's Haze x Shiva",
    origin: "España / Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, pinene: 30, limonene: 20 },
    flavors: ["Incienso Clásico", "Especias Orientales", "Pino Suave"],
    effects: ["Expansión Mental", "Creatividad Profunda", "Euforia Sativa Pura"],
    activities: ["creativity", "meditation", "nature_walk"],
    description: "Neville's Haze estabilizada con Shiva. Efecto sativa clásico de alta intensidad cerebral, ideal para meditación o creación artística. Floración más corta que las Haze originales.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #06B6D4 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-royal-gorilla",
    image: "img/rqs-royal-gorilla-bud.webp",
    name: "Royal Gorilla",
    aka: "GG#4 Selection RQS",
    bank: "Royal Queen Seeds",
    species: "Híbrida",
    thc: 27, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 600,
    floweringDays: 63, rating: 4.9, reviewsCount: 920,
    genetics: "Sour Dubb x Chem Sis x Chocolate Diesel",
    origin: "Holanda / España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, limonene: 30, myrcene: 20 },
    flavors: ["Pino Silvestre", "Diesel Gas", "Tierra Especiada"],
    effects: ["Relajación Extrema", "Euforia Cerebral", "Couch-Lock"],
    activities: ["relax_sleep", "gaming"],
    description: "La versión oficial de RQS de la legendaria GG#4. Famosa por pegar las tijeras al manicurar. Potencia increíble de 27% THC con sabor a pino y diésel.",
    visualColor: "linear-gradient(135deg, #047857 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-northern-light",
    image: "img/nirvana-northern-light-flower-hd.webp",
    name: "Northern Light",
    aka: "NL #5 Legend",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 18, cbd: 0.8,
    yieldIndoor: 550, yieldOutdoor: 625,
    floweringDays: 56, rating: 4.8, reviewsCount: 1100,
    genetics: "Afghani Indica x Thai Sativa",
    origin: "EEUU / Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, pinene: 25, caryophyllene: 20 },
    flavors: ["Pino Especiado", "Tierra Dulce", "Herbal"],
    effects: ["Relajación Suave", "Sueño Tranquilo", "Bienestar"],
    activities: ["relax_sleep", "meditation"],
    description: "Una de las Índicas más famosas de la historia. Sabor a pino terroso clásico, muy fácil de cultivar con efecto calmante equilibrado. Perfecta para principiantes.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #1E40AF 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-amnesia-haze",
    image: "img/rqs-amnesia-haze-plant.webp",
    name: "Amnesia Haze",
    aka: "Original Haze Hybrids",
    bank: "Royal Queen Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.3,
    yieldIndoor: 650, yieldOutdoor: 700,
    floweringDays: 77, rating: 4.9, reviewsCount: 1250,
    genetics: "Amnesia Haze x Original Haze",
    origin: "Holanda",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 30, pinene: 20 },
    flavors: ["Limón Dulce Explosivo", "Incienso Haze", "Especias"],
    effects: ["Explosión Energética", "Lucidez Mental", "Euforia Pura"],
    activities: ["nature_walk", "creativity", "social"],
    description: "La reina de los Coffee Shops de Ámsterdam. Efecto cerebral vigorizante y explosivo con aroma cítrico dulce a limón e incienso. Múltiples premios Cannabis Cup.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-wedding-glue",
    image: "img/rqs-wedding-glue-plant.webp",
    name: "Wedding Glue",
    aka: "Wedding Cake x GG#4",
    bank: "Royal Queen Seeds",
    species: "Híbrida",
    thc: 26, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 700,
    floweringDays: 63, rating: 4.8, reviewsCount: 580,
    genetics: "Wedding Cake x Gorilla Glue #4",
    origin: "Holanda",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, myrcene: 25 },
    flavors: ["Vainilla Cremosa", "Galleta Dulce", "Gas Suave"],
    effects: ["Relajación Intensa", "Euforia Controlada", "Pesadez Agradable"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Wedding Cake se une al monstruo GG#4. Resultado: 26% THC, vainilla cremosa con fondo gasoso y un efecto que combina lo mejor de ambas leyendas.",
    visualColor: "linear-gradient(135deg, #F9A8D4 0%, #A78BFA 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,168,212,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-fat-banana",
    image: "img/rqs-fat-banana-plant.webp",
    name: "Fat Banana",
    aka: "OG Kush x Banana",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 25, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 56, rating: 4.7, reviewsCount: 430,
    genetics: "OG Kush x Banana",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Plátano Maduro", "Tropical Dulce", "OG Kush Suave"],
    effects: ["Cuerpo-Lock Placentero", "Calma Mental", "Sueño"],
    activities: ["relax_sleep", "gaming"],
    description: "OG Kush con aroma irresistible a plátano maduro. Cogollos gordos y densos, perfecta para extracciones y consumo nocturno.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-lemon-shining-silver",
    image: "img/rqs-lemon-shining-silver.webp",
    name: "Lemon Shining Silver Haze",
    aka: "LSSH",
    bank: "Royal Queen Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 650,
    floweringDays: 70, rating: 4.8, reviewsCount: 670,
    genetics: "Lemon Skunk x Silver Haze",
    origin: "Holanda",
    dominantTerpene: "limonene",
    terpenes: { limonene: 60, terpinolene: 25, pinene: 15 },
    flavors: ["Limón Ácido Intenso", "Skunk Suave", "Citrus Haze"],
    effects: ["Energía Mental", "Euforia Sativa", "Creatividad Libre"],
    activities: ["creativity", "social", "nature_walk"],
    description: "El cruce perfecto entre Lemon Skunk y Silver Haze. Terpenos de limón dominantes que explotan en el paladar. Efecto energético sativa muy limpio y sin ansiedad.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dp-auto-blueberry",
    image: "img/dp-auto-blueberry-flowering.webp",
    name: "Auto Blueberry",
    aka: "Blueberry Auto Classic",
    bank: "Dutch Passion",
    species: "Indica",
    thc: 17, cbd: 1.0,
    yieldIndoor: 400, yieldOutdoor: 500,
    floweringDays: 63, rating: 4.7, reviewsCount: 820,
    genetics: "Blueberry x Ruderalis",
    origin: "Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, linalool: 25, caryophyllene: 20 },
    flavors: ["Arándano Fresco", "Bayas Silvestres", "Tierra Dulce"],
    effects: ["Relajación Suave", "Bienestar", "Sueño Tranquilo"],
    activities: ["relax_sleep", "meditation"],
    description: "La autofloreciente Blueberry más famosa de la historia, creada por el breeder DJ Short y adaptada por Dutch Passion. Aroma dulce a arándanos frescos con efecto suave y reconfortante.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "dp-think-different",
    image: "img/dp-think-different.webp",
    name: "Think Different",
    aka: "AK-47 Auto Sativa Elite",
    bank: "Dutch Passion",
    species: "Sativa",
    thc: 21, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 75, rating: 4.8, reviewsCount: 560,
    genetics: "AK-47 x Auto Mazar x Caramelice (Ruderalis)",
    origin: "Ámsterdam",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 40, limonene: 35, pinene: 25 },
    flavors: ["Fruta Dulce Herbal", "Madera Especiada", "Citrus Suave"],
    effects: ["Euforia Sativa Pura", "Claridad Mental", "Motivación"],
    activities: ["creativity", "nature_walk", "workout"],
    description: "La autofloreciente Sativa más grande de Dutch Passion. Plantas enormes con cogollos XL y un efecto sativa de alta calidad que rivaliza con las mejores fotodependientes.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #06B6D4 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dp-zkittlez",
    image: "img/dp-zkittlez-bud.webp",
    name: "Zkittlez",
    aka: "Zkittlez Original Elite",
    bank: "Dutch Passion",
    species: "Indica",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.9, reviewsCount: 740,
    genetics: "Grape Ape x Grapefruit x Mystery Strain",
    origin: "Ámsterdam / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, terpinolene: 25 },
    flavors: ["Caramelos de Uva", "Frutas Skittles", "Cítrico Candy"],
    effects: ["Euforia Corporal", "Felicidad Intensa", "Relajación Placentera"],
    activities: ["social", "relax_sleep", "creativity"],
    description: "La versión definitiva de Dutch Passion de la genética californiana más deseada. Sabor a caramelos de frutas mezcladas con efecto que mezcla euforia mental y relajación corporal.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #A78BFA 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "dp-passion-fruit",
    image: "img/dp-passion-fruit-flowering.webp",
    name: "Passion Fruit",
    aka: "Exótica Tropical Premium",
    bank: "Dutch Passion",
    species: "Sativa",
    thc: 20, cbd: 0.6,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.6, reviewsCount: 310,
    genetics: "Tropical Sativa x Haze Híbrido",
    origin: "Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 30, ocimene: 20 },
    flavors: ["Maracuyá Real", "Mango Tropical", "Guayaba Dulce"],
    effects: ["Alegría Tropical", "Energía Mental Suave", "Bienestar"],
    activities: ["nature_walk", "social", "creativity"],
    description: "Un viaje al Caribe en cada bocanada. Sativa tropical con terpenos de ocimeno y limoneno que recuerdan literalmente a la pulpa de maracuyá fresca.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #34D399 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "philo-cali-orange-bud",
    image: "img/philo-cali-orange-bud.webp",
    name: "Cali Orange Bud",
    aka: "Naranja Californiana Clásica",
    bank: "Philosopher Seeds",
    species: "Híbrida",
    thc: 19, cbd: 0.5,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 58, rating: 4.7, reviewsCount: 480,
    genetics: "Cali Orange Bud Selección (Sativa Californiana x Skunk)",
    origin: "España / California",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, terpinolene: 30, myrcene: 15 },
    flavors: ["Naranja Californiana", "Mandarina Madura", "Skunk Suave"],
    effects: ["Euforia Social", "Creatividad", "Energía Ligera"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Una de las más queridas de Philosopher Seeds. Naranja pura californiana seleccionada y estabilizada para el clima europeo. Aroma cítrico intenso y efecto equilibrado.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "philo-singha-valley",
    image: "img/philo-singha-valley.webp",
    name: "Singha Valley",
    aka: "Thai x High CBD",
    bank: "Philosopher Seeds",
    species: "Sativa",
    thc: 10, cbd: 10.0,
    yieldIndoor: 350, yieldOutdoor: 450,
    floweringDays: 60, rating: 4.6, reviewsCount: 220,
    genetics: "Thai Sativa x Ruderalis (Alta ratio CBD)",
    origin: "España / Tailandia",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 40, linalool: 35, pinene: 25 },
    flavors: ["Floral Dulce", "Menta Suave", "Hierba Fresca"],
    effects: ["Claridad Sin Psicoactividad", "Relax Corporal", "Medicinal"],
    activities: ["meditation", "workout", "nature_walk"],
    description: "La joya medicinal de Philosopher Seeds. Ratio 1:1 THC:CBD. Ideal para usuarios que buscan alivio físico y claridad mental sin intoxicación.",
    visualColor: "linear-gradient(135deg, #34D399 0%, #3B82F6 100%)",
    bgPattern: "radial-gradient(circle, rgba(52,211,153,0.2) 0%, transparent 70%)"
  },
  {
id: "philo-sugar-black-rose",
    image: "img/philo-sugar-black-rose-flowering.webp",
    name: "Sugar Black Rose",
    aka: "Black Domina x Critical +",
    bank: "Philosopher Seeds",
    species: "Indica",
    thc: 22, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 55, rating: 4.8, reviewsCount: 540,
    genetics: "Black Domina x Critical + (Philosopher Selection)",
    origin: "España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, linalool: 20 },
    flavors: ["Rosa Oscura Dulce", "Chocolate Negro", "Tierra Floral"],
    effects: ["Sedación Profunda", "Calma Absoluta", "Alivio Físico"],
    activities: ["relax_sleep", "meditation"],
    description: "Una rosa oscura y misteriosa. Black Domina cruzada con Critical +: potente, floración rápida y con un aroma dulce y floral inusual en Índicas.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #1E1B4B 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "philo-blues",
    image: "img/philo-blues.webp",
    name: "The Blues",
    aka: "Blueberry x White Widow",
    bank: "Philosopher Seeds",
    species: "Indica",
    thc: 20, cbd: 0.7,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.7, reviewsCount: 360,
    genetics: "Blueberry x White Widow",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, linalool: 30, caryophyllene: 20 },
    flavors: ["Arándano", "Floral Suave", "Tierra Blanca"],
    effects: ["Relajación Placentera", "Bienestar", "Calma Emocional"],
    activities: ["relax_sleep", "meditation", "social"],
    description: "La combinación nostálgica de Blueberry y White Widow. Colores azulados en cogollos, aroma a bayas frescas y un efecto Índica suave y reconfortante.",
    visualColor: "linear-gradient(135deg, #60A5FA 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(96,165,250,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-trainwreck",
    image: "img/hso-trainwreck.webp",
    name: "Trainwreck",
    aka: "Mexican x Thai x Afghani",
    bank: "Humboldt Seed",
    species: "Sativa",
    thc: 21, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 60, rating: 4.8, reviewsCount: 720,
    genetics: "Mexican Sativa x Thai Sativa x Afghani Indica",
    origin: "California / España",
    dominantTerpene: "pinene",
    terpenes: { pinene: 50, limonene: 30, terpinolene: 20 },
    flavors: ["Pino Fresco Potente", "Limón Herbal", "Mentol Silvestre"],
    effects: ["Energía Explosiva", "Euforia Mental", "Creatividad Libre"],
    activities: ["nature_walk", "creativity", "workout", "social"],
    description: "Legendaria del condado de Humboldt, California. Mezcla perfecta de Mexican, Thai y Afghani con un efecto sativa explosivo y sabor a pino y limón refrescante.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-og-eddy-lepp",
    image: "img/hso-og-eddy-lepp-plant.webp",
    name: "OG Eddy Lepp",
    aka: "SFV OG x OG Kush Elite",
    bank: "Humboldt Seed",
    species: "Híbrida",
    thc: 24, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 63, rating: 4.9, reviewsCount: 560,
    genetics: "SFV OG Kush x OG Kush (Humboldt Selection)",
    origin: "California",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, limonene: 20 },
    flavors: ["OG Clásico", "Gasolina Suave", "Limón Terroso"],
    effects: ["Relajación OG Clásica", "Euforia Cerebral", "Calma Física"],
    activities: ["relax_sleep", "gaming", "social"],
    description: "La joya OG de Humboldt Seed. Selección de la mejor familia OG Kush de California, con el sabor a gasolina y limón y el efecto OG que los conocedores más aprecian.",
    visualColor: "linear-gradient(135deg, #047857 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-blue-dream",
    image: "img/hso-blue-dream-official.webp",
    name: "Blue Dream",
    aka: "Blueberry x Haze Californiana",
    bank: "Humboldt Seed",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 65, rating: 4.8, reviewsCount: 1050,
    genetics: "Blueberry x Super Silver Haze",
    origin: "California / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 40, terpinolene: 35, pinene: 25 },
    flavors: ["Arándano Dulce", "Haze Cremosa", "Vainilla Herbal"],
    effects: ["Euforia Equilibrada", "Creatividad Motivada", "Bienestar Completo"],
    activities: ["creativity", "social", "nature_walk", "workout"],
    description: "La cepa más popular de California en la última década. Combina el sabor a arándano de Blueberry con la energía y claridad de Haze. Efecto híbrido perfecto para el día.",
    visualColor: "linear-gradient(135deg, #60A5FA 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(96,165,250,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-girl-scout-cookies",
    image: "img/hso-girl-scout-cookies.webp",
    name: "Girl Scout Cookies",
    aka: "GSC California Original",
    bank: "Humboldt Seed",
    species: "Híbrida",
    thc: 25, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 63, rating: 4.9, reviewsCount: 930,
    genetics: "OG Kush x Durban Poison x Cherry Kush",
    origin: "San Francisco / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, humulene: 20 },
    flavors: ["Galleta de Menta", "Tierra OG", "Dulce Especiado"],
    effects: ["Euforia Poderosa", "Bienestar Total", "Creatividad Calmada"],
    activities: ["social", "creativity", "relax_sleep"],
    description: "La cepa que cambió la industria en California. GSC con genética original de SF: sabor a galleta mentolada con tierra OG y el efecto equilibrado que la hizo mundialmente famosa.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "oo-chemdawg",
    image: "img/oo-chemdawg.webp",
    name: "Chemdawg",
    aka: "ChemDog Original",
    bank: "00 Seeds Bank",
    species: "Híbrida",
    thc: 23, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.8, reviewsCount: 640,
    genetics: "Thai x Nepalese Landrace (Mystery Origin)",
    origin: "EEUU / España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Gas / Química", "Tierra Sour", "Diesel Intenso"],
    effects: ["Efecto Combinado Único", "Euforia + Relajación", "Sociabilidad"],
    activities: ["social", "gaming", "creativity"],
    description: "La madre de OG Kush y Sour Diesel. Aroma químico a gas y diesel. Efecto híbrido único con poderosa euforia mental y relajación corporal simultáneas.",
    visualColor: "linear-gradient(135deg, #475569 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)"
  },
  {
id: "oo-caramel-cream",
    image: "img/oo-caramel-cream.webp",
    name: "Caramel Cream",
    aka: "Caramelo Índica Dulce",
    bank: "00 Seeds Bank",
    species: "Indica",
    thc: 18, cbd: 1.2,
    yieldIndoor: 600, yieldOutdoor: 750,
    floweringDays: 55, rating: 4.7, reviewsCount: 410,
    genetics: "Caramel x Indica Selección (00 Seeds)",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, linalool: 30, caryophyllene: 20 },
    flavors: ["Caramelo Suave", "Vainilla Cremosa", "Tierra Dulce"],
    effects: ["Relajación Dulce", "Bienestar Cálido", "Sueño Tranquilo"],
    activities: ["relax_sleep", "meditation"],
    description: "La Índica más dulce de 00 Seeds Bank. Sabor a caramelo y vainilla con CBD elevado para un efecto suave y medicinal. Floración rápida y producción generosa.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #92400E 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "oo-white-widow",
    image: "img/oo-white-widow.webp",
    name: "White Widow",
    aka: "La Viuda Blanca Clásica",
    bank: "00 Seeds Bank",
    species: "Híbrida",
    thc: 20, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 860,
    genetics: "Brazilian Sativa x Indian Indica (Original)",
    origin: "Holanda / España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, myrcene: 35, pinene: 25 },
    flavors: ["Tierra Blanca", "Madera Especiada", "Pino Suave"],
    effects: ["Euforia Equilibrada", "Energía Mental", "Bienestar Físico"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Una de las más icónicas de todos los tiempos. White Widow cubierta de cristales blancos de resina, con efecto equilibrado que la hizo famosa en los Coffee Shops de Amsterdam.",
    visualColor: "linear-gradient(135deg, #E2E8F0 0%, #94A3B8 100%)",
    bgPattern: "radial-gradient(circle, rgba(148,163,184,0.2) 0%, transparent 70%)"
  },
  {
id: "oo-super-skunk",
    image: "img/oo-super-skunk-bud.webp",
    gallery: ["img/oo-super-skunk-bud.webp", "img/oo-super-skunk-plant.webp", "img/oo-super-skunk-flowering.webp"],
    name: "Super Skunk",
    aka: "Skunk #1 x Afghani",
    bank: "00 Seeds Bank",
    species: "Indica",
    thc: 20, cbd: 0.5,
    yieldIndoor: 600, yieldOutdoor: 750,
    floweringDays: 50, rating: 4.7, reviewsCount: 580,
    genetics: "Skunk #1 x Afghani Indica",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, caryophyllene: 30, limonene: 15 },
    flavors: ["Skunk Clásico", "Tierra Afgana", "Notas Dulces"],
    effects: ["Relajación Corporal", "Pesadez Placentera", "Paz Mental"],
    activities: ["relax_sleep", "social"],
    description: "Skunk #1 potenciado con Afghani puro. Floración ultra rápida (50 días) con producción enorme. Aroma clásico a skunk terroso con fondo dulce. Un indispensable del cultivo.",
    visualColor: "linear-gradient(135deg, #78716C 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(120,113,108,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-gorilla-glue-4",
    image: "img/bsf-gorilla-glue-4.webp",
    name: "Gorilla Glue #4",
    aka: "Chem Sister x Sour Dubb x Chocolate Diesel",
    bank: "BSF Seeds",
    species: "Híbrida",
    thc: 27, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 1200,
    floweringDays: 63, rating: 5.0, reviewsCount: 740,
    genetics: "Chem Sister x Sour Dubb x Chocolate Diesel",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 30, limonene: 25 },
    flavors: ["Pino Húmedo", "Diesel Potente", "Chocolate Amargo"],
    effects: ["Euforia Cerebral", "Pegajoso Físico", "Relax Absoluto"],
    activities: ["relax_sleep", "gaming", "creativity"],
    description: "Cepa insignia galardonada de BSF Seeds. Densidad extrema de resina con niveles de THC desbordantes del 27%. Aroma pegajoso a pino, tierra y diésel con un efecto eufórico y sedante de gran impacto.",
    visualColor: "linear-gradient(135deg, #059669 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-lebron-haze",
    image: "img/bsf-lebron-haze.webp",
    name: "Lebron Haze",
    aka: "Elite Haze x Lemon Thai",
    bank: "BSF Seeds",
    species: "Sativa",
    thc: 28, cbd: 0.1,
    yieldIndoor: 650, yieldOutdoor: 1000,
    floweringDays: 56, rating: 4.9, reviewsCount: 680,
    genetics: "Elite Haze x Lemon Thai",
    origin: "España / USA",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, pinene: 30, terpinolene: 20 },
    flavors: ["Limón Intenso", "Incienso Haze", "Madera Noble"],
    effects: ["Energía Creativa", "Risas & Euforia", "Claridad Mental"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Considerada el 'Rey' de las Sativas de floración rápida en BSF Seeds. Produce niveles récord de THC (hasta 28%) con un aroma cítrico e inciensado y una energía psicodélica limpia y motivadora.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #FBBF24 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-moby-d",
    image: "img/official/bsf-seeds-moby-d-feminizada.webp",
    name: "Moby-D",

    aka: "Jack Herer x White Widow",
    bank: "BSF Seeds",
    species: "Sativa",
    thc: 25, cbd: 0.2,
    yieldIndoor: 700, yieldOutdoor: 1200,
    floweringDays: 63, rating: 4.9, reviewsCount: 520,
    genetics: "Jack Herer x White Widow",
    origin: "España / USA",
    dominantTerpene: "pinene",
    terpenes: { pinene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Pino Fresco", "Limón Dulce", "Madera de Cedro"],
    effects: ["Estimulación Físico-Mental", "Inspiración", "Vitalidad"],
    activities: ["nature_walk", "workout", "creativity"],
    description: "Una auténtica monstruosidad en rendimiento y vigor. Híbrido Sativo masivo con cogollos repletos de tricomas brillantes, aromas a pino y cítricos con una pegarada eufórica duradera.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-gorilla-ghost",
    image: "img/bsf-gorilla-ghost.webp",
    name: "Gorilla Ghost",
    aka: "Gorilla Glue #4 x Ghost Auto",
    bank: "BSF Seeds",
    species: "Híbrida",
    thc: 29, cbd: 0.1,
    yieldIndoor: 650, yieldOutdoor: 1200,
    floweringDays: 60, rating: 5.0, reviewsCount: 810,
    genetics: "Gorilla Glue #4 x Ghost OG",
    origin: "España / USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Cítrico Frutal", "Tierra Kush", "Hierbas Florales"],
    effects: ["Potencia Demoledora", "Relajación Corporal", "Paz Mental"],
    activities: ["relax_sleep", "gaming"],
    description: "Una de las genéticas más potentes del catálogo con un 29% de THC. Unión entre la legendaria Gorilla Glue #4 y Ghost OG. Efecto devastador para consumidores con alta tolerancia.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.25) 0%, transparent 70%)"
  },
  {
id: "bsf-double-cookies",
    image: "img/bsf-double-cookies.webp",
    name: "Double Cookies",
    aka: "Do-Si-Dos x Forum Cookies",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 25, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 58, rating: 4.8, reviewsCount: 460,
    genetics: "Do-Si-Dos x Forum Cut Girl Scout Cookies",
    origin: "España / USA",
    dominantTerpene: "linalool",
    terpenes: { linalool: 40, caryophyllene: 35, myrcene: 25 },
    flavors: ["Galleta Recién Horneada", "Menta Dulce", "Tierra Cremosa"],
    effects: ["Relax Físico Placentero", "Felicidad", "Calma Muscular"],
    activities: ["relax_sleep", "meditation"],
    description: "Doble dosis de la mejor familia Cookies americana. Cogollos morados oscuros bañados en resina dulce sabor a galletas frescas con menta y matices de pino.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-green-tiger-fast",
    image: "img/bsf-green-tiger-fast.webp",
    name: "Green Tiger (Faster)",
    aka: "Early Skunk x Skunk P91",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 22, cbd: 0.1,
    yieldIndoor: 650, yieldOutdoor: 1000,
    floweringDays: 42, rating: 4.8, reviewsCount: 390,
    genetics: "(Early Skunk x Skunk P91) x Fast Flowering",
    origin: "España / USA",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Melón Dulce", "Fruta Madura", "Cítrico Dulce"],
    effects: ["Relajación Rápida", "Sensación Festiva", "Desconexión"],
    activities: ["social", "relax_sleep"],
    description: "Homenaje a la rapidez. Variedad Faster Flowering ultra rápida lista en solo 6 semanas (42 días). Increíble producción con un perfil aromático goloso a melón oriental y frutas.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-obg-kush-fast",
    image: "img/bsf-obg-kush-fast.webp",
    name: "OBG Kush (Faster)",
    aka: "Reserva Secreta KUSH",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 22, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 42, rating: 4.9, reviewsCount: 410,
    genetics: "Selección Secreta Kush x Fast",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, myrcene: 30, pinene: 20 },
    flavors: ["Pino Especiado", "Tierra Kush", "Pimiento Dulce"],
    effects: ["Sedación Muscular", "Tranquilidad", "Buen Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "La joya de la corona del menú Faster Flowering. Perfil Kush autentico de floración en 40-42 días, ideal para cultivadores que buscan máxima velocidad sin perder calidad.",
    visualColor: "linear-gradient(135deg, #047857 0%, #064E3B 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-el-gaucho-fast",
    image: "img/bsf-el-gaucho-fast.webp",
    name: "El Gaucho (Faster)",
    aka: "Sierra Cut x Abusive OG",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 22, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 45, rating: 4.8, reviewsCount: 310,
    genetics: "Sierra Cut x Abusive OG",
    origin: "España / USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Frutal Dulce", "Cítrico Suave", "Tierra Fresca"],
    effects: ["Calma Corporal", "Anti-Estrés", "Relajación Positiva"],
    activities: ["relax_sleep", "nature_walk"],
    description: "Cruce resistente de rápido desarrollo, perfecto para climas fríos u húmedos. Floración de 6 semanas con sabor dulce afrutado y relajación física placentera.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #B45309 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-rainbows",
    image: "img/bsf-rainbows.webp",
    name: "Rainbows",
    aka: "Zkittlez x Zkittlez",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 24, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.9, reviewsCount: 560,
    genetics: "Zkittlez Zkittlez Offspring",
    origin: "España / USA",
    dominantTerpene: "ocimene",
    terpenes: { ocimene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Coctel Frutal", "Pomelo Dulce", "Gominolas"],
    effects: ["Felicidad Eufórica", "Relajación Dulce", "Buen Humor"],
    activities: ["social", "gaming", "creativity"],
    description: "Explosión de terpenos ultra dulces sabor a gominolas tropicales y pomelo. Excelente estructura repleta de colores rosados y violetas al final de floración.",
    visualColor: "linear-gradient(135deg, #EF4444 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-gorilla-rainbows",
    image: "img/bsf-gorilla-rainbows.webp",
    name: "Gorilla Rainbows",
    aka: "Gorilla Glue #4 x Rainbows",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 25, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 60, rating: 4.9, reviewsCount: 490,
    genetics: "Gorilla Glue #4 x Rainbows",
    origin: "España / USA",
    dominantTerpene: "limonene",
    terpenes: { limonene: 40, caryophyllene: 35, myrcene: 25 },
    flavors: ["Caramelo Dulce", "Tierra Diésel", "Fruta Tropical"],
    effects: ["Nocaut Físico", "Alegría Mental", "Relajación Intensa"],
    activities: ["relax_sleep", "gaming"],
    description: "Híbrido de alta potencia que combina la producción de resina destructiva de GG4 con la dulzura frutal embriagadora de Rainbows.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-orange-blossom",
    image: "img/bsf-orange-blossom.webp",
    name: "Orange Blossom",
    aka: "Clementine x Purple Punch",
    bank: "BSF Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 65, rating: 4.7, reviewsCount: 380,
    genetics: "Clementine x Purple Punch",
    origin: "España / USA",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, pinene: 25, myrcene: 20 },
    flavors: ["Mandarina Fresca", "Naranja Cítrica", "Flor de Azahar"],
    effects: ["Energía Eufórica", "Creatividad", "Vitalidad Social"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Cepa con aroma y sabor puro a zumo de mandarina recién exprimida. Gran efecto sativo estimulante para el día a día sin pesadez física.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-red-critical-auto",
    image: "img/bsf-red-critical-auto.webp",
    name: "Red Critical XXL Auto",
    aka: "Critical Auto x Red Selective Cut",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 20, cbd: 0.2,
    yieldIndoor: 450, yieldOutdoor: 300,
    floweringDays: 55, rating: 4.8, reviewsCount: 420,
    genetics: "Critical XXL Auto x Red Genetics",
    origin: "España / USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, limonene: 25 },
    flavors: ["Flores Dulces", "Frutos Rojos", "Skunk Cítrico"],
    effects: ["Relajación Placentera", "Sensación Corporal", "Bienestar"],
    activities: ["relax_sleep", "social"],
    description: "Variedad de la espectacular Red Line de BSF Seeds. Muestra tonos rojos y púrpuras fascinantes con cogollos pesados aromáticos a frutos rojos y Skunk.",
    visualColor: "linear-gradient(135deg, #DC2626 0%, #991B1B 100%)",
    bgPattern: "radial-gradient(circle, rgba(220,38,38,0.25) 0%, transparent 70%)"
  },
  {
id: "bsf-lebron-haze-auto",
    image: "img/bsf-lebron-haze-auto.webp",
    name: "Lebron Haze XXL Auto",
    aka: "Lebron Haze x Jack Herer Auto",
    bank: "BSF Seeds",
    species: "Sativa",
    thc: 26, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 350,
    floweringDays: 63, rating: 4.9, reviewsCount: 510,
    genetics: "Lebron Haze x Jack Herer Auto",
    origin: "España / USA",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, pinene: 30, terpinolene: 20 },
    flavors: ["Limón Inciensado", "Pino Fresco", "Madera"],
    effects: ["Euforia Sativa Intensa", "Vigor Creativo", "Risas"],
    activities: ["creativity", "workout", "social"],
    description: "Versión autofloreciente XXL de Lebron Haze. Mantiene una potencia brutal del 26% de THC en un ciclo automático rápido de 9 semanas.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-gorilla-glue-auto",
    image: "img/bsf-gorilla-glue-auto.webp",
    name: "Gorilla Glue XXL Auto",
    aka: "Gorilla Glue #4 x Auto Cut",
    bank: "BSF Seeds",
    species: "Híbrida",
    thc: 24, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 350,
    floweringDays: 65, rating: 4.8, reviewsCount: 430,
    genetics: "Gorilla Glue #4 x Auto Male",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 30, limonene: 25 },
    flavors: ["Pino Diésel", "Tierra Húmeda", "Madera Especiada"],
    effects: ["Sedación Potente", "Relajación Física", "Felicidad"],
    activities: ["relax_sleep", "gaming"],
    description: "Traducción autofloreciente de la clásica Gorilla Glue #4. Tiempos de cultivo reducidos manteniendo una producción de resina salvaje.",
    visualColor: "linear-gradient(135deg, #059669 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
  },
  {
id: "bsf-ice-cream-cake-fast",
    image: "img/bsf-ice-cream-cake-fast.webp",
    name: "Ice Cream Cake (Faster)",
    aka: "Gelato 33 x Wedding Cake",
    bank: "BSF Seeds",
    species: "Indica",
    thc: 21, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 45, rating: 4.8, reviewsCount: 340,
    genetics: "Gelato 33 x Wedding Cake x Fast",
    origin: "España / USA",
    dominantTerpene: "linalool",
    terpenes: { linalool: 45, caryophyllene: 30, myrcene: 25 },
    flavors: ["Helado de Vainilla", "Masa Dulce", "Cítrico Suave"],
    effects: ["Relajación Dulce", "Calma Emocional", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "Versión de floración ultra rápida de la popular Ice Cream Cake. Sabor cremoso a helado de vainilla con notas de repostería y efecto relajante reconfortante.",
    visualColor: "linear-gradient(135deg, #A78BFA 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(167,139,250,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-moby-dick",
    image: "img/dinafem-moby-dick.webp",
    name: "Moby Dick",
    aka: "Haze x White Widow",
    bank: "Dinafem Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.1,
    yieldIndoor: 650, yieldOutdoor: 1500,
    floweringDays: 65, rating: 5.0, reviewsCount: 920,
    genetics: "Haze x White Widow",
    origin: "España",
    dominantTerpene: "pinene",
    terpenes: { pinene: 45, terpinolene: 30, limonene: 25 },
    flavors: ["Pino Haze", "Limón Cítrico", "Madera de Cedro"],
    effects: ["Psicoactividad Potente", "Euforia Cerebral", "Energía Duradera"],
    activities: ["creativity", "nature_walk", "workout"],
    description: "Icono absoluto del cannabis español e internacional. Híbrido Sativo con producción colosal, cogollos bañados en tricomas y aroma inolvidable a Haze, pino y cítricos.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.25) 0%, transparent 70%)"
  },
  {
id: "dinafem-critical-plus",
    image: "img/dinafem-critical-plus.webp",
    name: "Critical +",
    aka: "Big Bud x Skunk #1",
    bank: "Dinafem Seeds",
    species: "Híbrida",
    thc: 18, cbd: 0.2,
    yieldIndoor: 625, yieldOutdoor: 1300,
    floweringDays: 50, rating: 4.9, reviewsCount: 880,
    genetics: "Big Bud x Skunk #1 Selection",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Skunk Dulce", "Limón Penetrante", "Fruta Madura"],
    effects: ["Relajación Físico-Mental", "Bienestar", "Felicidad"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "La variedad más famosa y cultivada en España. Floración ultrarrápida (50 días), ramificación masiva y un aroma cítrico Skunk tan intenso que requiere filtros antiolor de máxima potencia.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-og-kush",
    image: "img/dinafem-og-kush.webp",
    name: "OG Kush",
    aka: "Lemon Thai x Chemdawg",
    bank: "Dinafem Seeds",
    species: "Indica",
    thc: 24, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 1100,
    floweringDays: 55, rating: 4.9, reviewsCount: 790,
    genetics: "Lemon Thai/Pakistani x Chemdawg",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 30, limonene: 25 },
    flavors: ["Diesel Gasolina", "Limón Terroso", "Pino Especiado"],
    effects: ["Trance Cerebral", "Relajación Corporal", "Calma Absoluta"],
    activities: ["relax_sleep", "gaming", "meditation"],
    description: "La leyenda californiana llevada a su máxima expresión por Dinafem. Aroma inconfundible a combustible, limón y tierra húmeda con un efecto relajante corporal devastador.",
    visualColor: "linear-gradient(135deg, #047857 0%, #064E3B 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.25) 0%, transparent 70%)"
  },
  {
id: "dinafem-cheese",
    image: "img/dinafem-cheese.webp",
    name: "Cheese",
    aka: "Old School UK Cheese",
    bank: "Dinafem Seeds",
    species: "Indica",
    thc: 20, cbd: 0.1,
    yieldIndoor: 525, yieldOutdoor: 1000,
    floweringDays: 55, rating: 4.8, reviewsCount: 630,
    genetics: "Skunk #1 Phenotype (UK Cheese)",
    origin: "España / UK",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, limonene: 20 },
    flavors: ["Queso Curado", "Skunk Terroso", "Fondo Dulce"],
    effects: ["Sensación Festiva", "Relajación Muscular", "Buen Humor"],
    activities: ["social", "relax_sleep"],
    description: "Fiel adaptación del clon clásico británico. Notas intensas a queso curado añejo y Skunk terroso con un efecto eufórico inicial seguido de una agradable calma corporal.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-industrial-plant",
    image: "img/dinafem-industrial-plant.webp",
    name: "Industrial Plant",
    aka: "Northern Lights x Skunk",
    bank: "Dinafem Seeds",
    species: "Híbrida",
    thc: 18, cbd: 0.2,
    yieldIndoor: 625, yieldOutdoor: 1300,
    floweringDays: 48, rating: 4.7, reviewsCount: 410,
    genetics: "Northern Lights x Skunk Selection",
    origin: "España",
    dominantTerpene: "pinene",
    terpenes: { pinene: 40, myrcene: 35, caryophyllene: 25 },
    flavors: ["Pino Especiado", "Madera Citrus", "Skunk Clásico"],
    effects: ["Equilibrio Psicoactivo", "Sedación Placentera", "Paz"],
    activities: ["relax_sleep", "social"],
    description: "Pionera en alta producción comercial. Rendimientos gigantescos en tiempo récord (45-50 días) con un perfil aromático cítrico especiado de gran estabilidad.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-amnesia-kush",
    image: "img/dinafem-amnesia-kush.webp",
    name: "Amnesia Kush",
    aka: "Amnesia Haze x OG Kush",
    bank: "Dinafem Seeds",
    species: "Sativa",
    thc: 24, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 1200,
    floweringDays: 65, rating: 4.9, reviewsCount: 540,
    genetics: "Amnesia Haze x OG Kush",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, caryophyllene: 35, pinene: 20 },
    flavors: ["Limón Haze", "Gasolina Diesel", "Incienso Silvestre"],
    effects: ["Euforia Viajera", "Estimulación Creativa", "Desconexión"],
    activities: ["creativity", "gaming", "nature_walk"],
    description: "Titanico choque entre los dos gigantes de Europa y América. Combina el sabor eufórico inciensado de Amnesia Haze con la potencia terrosa a combustible de OG Kush.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-blue-widow",
    image: "img/dinafem-blue-widow.webp",
    name: "Blue Widow",
    aka: "Blueberry x White Widow",
    bank: "Dinafem Seeds",
    species: "Híbrida",
    thc: 19, cbd: 0.2,
    yieldIndoor: 525, yieldOutdoor: 1100,
    floweringDays: 52, rating: 4.8, reviewsCount: 470,
    genetics: "Blueberry x White Widow",
    origin: "España",
    dominantTerpene: "linalool",
    terpenes: { linalool: 45, myrcene: 30, caryophyllene: 25 },
    flavors: ["Arándanos Dulces", "Frutas del Bosque", "Tierra Dulce"],
    effects: ["Relajación Visual", "Bienestar Emocional", "Sosiego"],
    activities: ["relax_sleep", "meditation"],
    description: "Una de las genéticas más hermosas del catálogo. Desarrolla tonalidades púrpuras y azuladas intensas al descender la temperatura nocturna, con aroma dulzón a arándanos silvestres.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-dinamex",
    image: "img/dinafem-dinamex.webp",
    name: "Dinamex",
    aka: "Cali Sour x Emerald OG Kush",
    bank: "Dinafem Seeds",
    species: "Híbrida",
    thc: 20, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 60, rating: 4.7, reviewsCount: 320,
    genetics: "Cali Sour (Sour Diesel x Lemon Thai x Mexican Sativa) x Emerald OG Kush",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Limón Ácido", "Diesel Limpio", "Especias Agrias"],
    effects: ["Claridad Mental", "Energía Social", "Sensación Corporal"],
    activities: ["social", "creativity"],
    description: "Híbrido muy apreciado por cultivadores exigentes. Mezcla matices amargos cítricos de Sour Diesel con la densidad de resina de OG Kush.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-critical-jack",
    image: "img/dinafem-critical-jack.webp",
    name: "Critical Jack",
    aka: "Critical + x Jack Herer",
    bank: "Dinafem Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.1,
    yieldIndoor: 625, yieldOutdoor: 1200,
    floweringDays: 60, rating: 4.9, reviewsCount: 580,
    genetics: "Critical + x Jack Herer",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, pinene: 30, limonene: 25 },
    flavors: ["Madera Haze", "Incienso Dulce", "Limón Skunk"],
    effects: ["Subidón Energético", "Motivación", "Mente Despierta"],
    activities: ["workout", "nature_walk", "creativity"],
    description: "Cruce estelar galardonado internacionalmente (1er premio Outdoor San Bernardino Cannabis Cup). Aporta la efervescencia de Jack Herer con la velocidad y producción masiva de Critical +.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #06B6D4 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-critical-auto-2",
    image: "img/dinafem-critical-auto-2.webp",
    name: "Critical + 2.0 Auto",
    aka: "Critical + Auto x Critical +",
    bank: "Dinafem Seeds",
    species: "Indica",
    thc: 20, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 300,
    floweringDays: 70, rating: 4.8, reviewsCount: 510,
    genetics: "Critical + Auto x Critical + Dominant",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Skunk Naranja", "Limón Dulce", "Especias"],
    effects: ["Relajación Físico-Mental", "Sensación Festiva", "Sosiego"],
    activities: ["relax_sleep", "social"],
    description: "Segunda generación mejorada de Critical + Auto. Mayor porte, ramificación lateral abundante y cogollos ultra resinosos con aroma Skunk cítrico mejorado.",
    visualColor: "linear-gradient(135deg, #059669 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-moby-dick-auto",
    image: "img/dinafem-moby-dick-auto.webp",
    name: "Moby Dick XXL Auto",
    aka: "Moby Dick Auto x White Widow Auto",
    bank: "Dinafem Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 250,
    floweringDays: 75, rating: 4.8, reviewsCount: 460,
    genetics: "Moby Dick Auto x White Widow Auto Selection",
    origin: "España",
    dominantTerpene: "pinene",
    terpenes: { pinene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Pino Haze", "Limón Fresco", "Madera"],
    effects: ["Potencia Sativa", "Energía", "Claridad"],
    activities: ["creativity", "workout", "nature_walk"],
    description: "La gigante de las autoflorecientes. Planta de gran porte que alcanza hasta 1.4 metros de altura con producción y pegada dignas de una fotoperiódica.",
    visualColor: "linear-gradient(135deg, #0284C7 0%, #0369A1 100%)",
    bgPattern: "radial-gradient(circle, rgba(2,132,199,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-gorilla-auto",
    image: "img/dinafem-gorilla-auto.webp",
    name: "Gorilla Auto",
    aka: "Gorilla Glue #4 Auto",
    bank: "Dinafem Seeds",
    species: "Híbrida",
    thc: 22, cbd: 0.1,
    yieldIndoor: 450, yieldOutdoor: 200,
    floweringDays: 75, rating: 4.8, reviewsCount: 390,
    genetics: "Gorilla Glue #4 x OG Kush Auto",
    origin: "España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 30, limonene: 25 },
    flavors: ["Diesel Combustible", "Tierra Húmeda", "Pino"],
    effects: ["Sedación Muscular", "Relajación Corporal", "Relax"],
    activities: ["relax_sleep", "gaming"],
    description: "Versión automática de la legendaria estadounidense. Concentración de resina abrumadora con cogollos blancos sabor diésel terroso.",
    visualColor: "linear-gradient(135deg, #15803D 0%, #166534 100%)",
    bgPattern: "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-remedy-cbd",
    image: "img/dinafem-remedy-cbd.webp",
    name: "Dinamed CBD",
    aka: "Pure CBD Medicinal",
    bank: "Dinafem Seeds",
    species: "Híbrida",
    thc: 0.9, cbd: 14.0,
    yieldIndoor: 500, yieldOutdoor: 900,
    floweringDays: 60, rating: 4.9, reviewsCount: 420,
    genetics: "Pure CBD 4 x Pure CBD 4",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, limonene: 30, linalool: 20 },
    flavors: ["Naranja Dulce", "Cítrico Herbal", "Fruta Madura"],
    effects: ["Cero Efecto Psicoactivo", "Alivio Físico", "Calma Mental"],
    activities: ["meditation", "relax_sleep", "workout"],
    description: "Pionera en cannabis puramente terapéutico con menos del 1% de THC y un 14% de CBD. Ideal para alivio físico sin alteración cognitiva.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #34D399 100%)",
    bgPattern: "radial-gradient(circle, rgba(52,211,153,0.25) 0%, transparent 70%)"
  },
  {
id: "dinafem-diesel",
    image: "img/dinafem-diesel.webp",
    name: "Diesel",
    aka: "Mexican Sativa x Afghani",
    bank: "Dinafem Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.1,
    yieldIndoor: 475, yieldOutdoor: 950,
    floweringDays: 60, rating: 4.7, reviewsCount: 380,
    genetics: "Mexican Sativa x Afghani",
    origin: "España / USA",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, caryophyllene: 30, myrcene: 20 },
    flavors: ["Mandarina Diésel", "Combustible", "Cítrico Fresco"],
    effects: ["Euforia Limpia", "Energía Mental", "Creatividad"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Clásica Diesel de aroma penetrante a mandarina y queroseno. Efecto eufórico sativo ideal para momentos creativos y sociales.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dinafem-sweet-grapefruit",
    image: "img/dinafem-sweet-grapefruit.webp",
    name: "Sweet Deep Grapefruit",
    aka: "Grapefruit x Blueberry",
    bank: "Dinafem Seeds",
    species: "Indica",
    thc: 18, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 800,
    floweringDays: 55, rating: 4.8, reviewsCount: 310,
    genetics: "Grapefruit x Blueberry",
    origin: "España",
    dominantTerpene: "ocimene",
    terpenes: { ocimene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Pomelo Frutal", "Dulce Tropical", "Arándanos"],
    effects: ["Relajación Placentera", "Buen Humor", "Desconexión"],
    activities: ["relax_sleep", "social"],
    description: "Cruce frutal de gran dulzura sabor a pomelo y bayas. Cogollos compactos de aroma tropical con efecto Índico relajante y equilibrado.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #DB2777 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-magnum",
    image: "img/buddha-magnum-bud.webp",
    name: "Magnum",
    aka: "XXL Autoflowering Sativa",
    bank: "Buddha Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.5,
    yieldIndoor: 550, yieldOutdoor: 175,
    floweringDays: 85, rating: 4.9, reviewsCount: 680,
    genetics: "Híbrido Sativa Triple (genética secreta Buddha Seeds)",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Incienso Haze", "Especias Dulces", "Pino Fresco"],
    effects: ["Subidón Enérgico", "Alegría Efervescente", "Estimulación Cerebral"],
    activities: ["creativity", "social", "nature_walk"],
    description: "La autofloreciente XXL de Buddha Seeds. Sativa predominante de ciclo algo más largo (80-90 días) que compensa con una producción excepcional de hasta 600 g/m². Aroma inconfundible a incienso haze con especias dulces. Efecto enérgico e inmediato, ideal para momentos creativos y sociales.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-deimos",
    image: "img/buddha-deimos-bud.webp",
    name: "Deimos",
    aka: "Northern Lights Auto Selection",
    bank: "Buddha Seeds",
    species: "Indica",
    thc: 18, cbd: 0.5,
    yieldIndoor: 500, yieldOutdoor: 150,
    floweringDays: 80, rating: 4.8, reviewsCount: 520,
    genetics: "Northern Lights x Ruderalis (7ª generación)",
    origin: "España / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, humulene: 20 },
    flavors: ["Skunk Dulce", "Tierra Especiada", "Hachís Incensado"],
    effects: ["Relajación Física Profunda", "Sedación Narcótica", "Calma Total"],
    activities: ["relax_sleep", "meditation"],
    description: "Autofloreciente índica de Buddha Seeds descendiente directa de la legendaria Northern Lights, estabilizada durante 7 generaciones. Estructura arbustiva muy ramificada con cogollos densos en todas las ramas. Efecto físico devastador, ideal para uso nocturno y combatir el estrés intenso.",
    visualColor: "linear-gradient(135deg, #047857 0%, #064E3B 100%)",
    bgPattern: "radial-gradient(circle, rgba(4,120,87,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-white-dwarf",
    image: "img/buddha-white-dwarf-bud.webp",
    name: "White Dwarf",
    aka: "Low Rider II Selection Auto",
    bank: "Buddha Seeds",
    species: "Indica",
    thc: 17, cbd: 0.5,
    yieldIndoor: 425, yieldOutdoor: 80,
    floweringDays: 63, rating: 4.7, reviewsCount: 390,
    genetics: "Low Rider II x Índica de Alto Rendimiento (35+ generaciones)",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, linalool: 25 },
    flavors: ["Madera Dulce", "Saúco Especiado", "Cítrico Suave"],
    effects: ["Relajación Calmante", "Desconexión Física", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "La autofloreciente compacta por excelencia de Buddha Seeds. Ciclo ultra rápido de 60-65 días y tamaño discreto para balcones y espacios reducidos. Estabilizada durante 35+ generaciones para máxima consistencia. Efecto índico relajante ideal para el descanso y la desconexión nocturna.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-purple-kush",
    image: "img/buddha-purple-kush-bud.webp",
    name: "Buddha Purple Kush",
    aka: "Purple Kush Feminizada",
    bank: "Buddha Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 440, yieldOutdoor: 1200,
    floweringDays: 60, rating: 4.8, reviewsCount: 480,
    genetics: "Selección Kush Morada Estabilizada",
    origin: "España / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Frutos del Bosque", "Tierra Kush", "Sándalo Hash"],
    effects: ["Relajación Placentera", "Descanso Físico", "Abre el Apetito"],
    activities: ["relax_sleep", "social"],
    description: "Feminizada fotodependiente con llamativa coloración morada gracias a su alta concentración de antocianinas. Los tonos violeta se intensifican en temperaturas más frescas. Muy resistente a plagas y humedad, con cogollos densos de aroma a frutos del bosque y tierra Kush. Ideal para relajarse tras un día largo.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-gorila",
    image: "img/buddha-gorila-bud.webp",
    name: "Gorila",
    aka: "Gorilla Glue #4 Selection",
    bank: "Buddha Seeds",
    species: "Indica",
    thc: 26, cbd: 0.2,
    yieldIndoor: 575, yieldOutdoor: 1200,
    floweringDays: 60, rating: 4.9, reviewsCount: 610,
    genetics: "Chem's Sister x Sour Dubb x Chocolate Diesel (Gorilla Glue #4 lineage)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, pinene: 35, myrcene: 20 },
    flavors: ["Pino Salvaje", "Cítrico Terroso", "Chocolate Oscuro"],
    effects: ["Relajación Aplastante", "Couch-Lock Intenso", "Euforia Inicial"],
    activities: ["relax_sleep", "meditation"],
    description: "La versión de Buddha Seeds de la mundialmente famosa Gorilla Glue #4. Potencia extrema con niveles de THC que hacen justicia a su nombre: te pega al sofá con fuerza. Producción colosal de resina ideal para extracciones premium. Un efecto 'animal' que incluso los usuarios más experimentados respetan.",
    visualColor: "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
    bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-gelato",
    image: "img/buddha-gelato-bud.webp",
    name: "Buddha Gelato",
    aka: "Gelato USA Collection",
    bank: "Buddha Seeds",
    species: "Híbrida",
    thc: 24, cbd: 0.2,
    yieldIndoor: 475, yieldOutdoor: 1500,
    floweringDays: 62, rating: 4.9, reviewsCount: 530,
    genetics: "Sunset Sherbet x Thin Mint GSC (Gelato lineage)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, linalool: 25 },
    flavors: ["Frutos Secos Dulces", "Menta Refrescante", "Frutal Tropical"],
    effects: ["Euforia Cerebral Activa", "Relajación Física Progresiva", "Creatividad Mental"],
    activities: ["creativity", "social", "gaming"],
    description: "La joya de la USA Collection de Buddha Seeds inspirada en el legendario linaje Gelato de San Francisco. Cogollos con una densidad de tricomas que recuerda a un cielo estrellado. Sabor complejo y premium a frutos secos con menta. Efecto que comienza eufórico y evoluciona hacia una relajación profunda y creativa.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-cookie",
    image: "img/buddha-cookie-bud.webp",
    name: "Buddha Cookie",
    aka: "Girl Scout Cookies Selection",
    bank: "Buddha Seeds",
    species: "Híbrida",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 1200,
    floweringDays: 60, rating: 4.8, reviewsCount: 490,
    genetics: "OG Kush x Durban Poison (Girl Scout Cookies lineage)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Galleta Recién Horneada", "Chocolate Terroso", "Especias Dulces"],
    effects: ["Euforia y Risas", "Relajación Corporal Plena", "Bienestar General"],
    activities: ["social", "relax_sleep", "creativity"],
    description: "La versión Buddha Seeds de la icónica Girl Scout Cookies de California. Fiel al perfil original con intensas notas de galleta y chocolate terroso que son absolutamente reconocibles. Efecto que arranca con euforia y risas, para evolucionar progresivamente hacia una relajación física profunda. Ideal para el estrés y el insomnio.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #92400E 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-dosi2",
    image: "img/buddha-dosi2-bud.webp",
    name: "Buddha DoSi2",
    aka: "Do-Si-Dos USA Collection",
    bank: "Buddha Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 575, yieldOutdoor: 1250,
    floweringDays: 65, rating: 4.8, reviewsCount: 380,
    genetics: "Face Off OG x OGKB (Do-Si-Dos / Cookies family)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 30, linalool: 25 },
    flavors: ["Dulce Cítrico", "Hash Terroso Clásico", "Notas Amargas Complejas"],
    effects: ["Euforia Creativa y Alegre", "Relajación Física Meditativa", "Equilibrio Cuerpo-Mente"],
    activities: ["creativity", "meditation", "relax_sleep"],
    description: "Descendiente directa de la familia Cookies, la Do-Si-Dos de Buddha Seeds ofrece un sabor a \"golosina\" con fondo terroso de hash que la hace inconfundible. Alta producción y resistencia excepcional, perfecta para cultivos de guerrilla. Efecto potente que comienza alegre y creativo y termina en una relajación meditativa profunda.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "buddha-wedding-cheesecake",
    image: "img/buddha-wedding-cheesecake-bud.webp",
    name: "Wedding Cheesecake",
    aka: "Buddha Wedding Cheesecake USA Collection",
    bank: "Buddha Seeds",
    species: "Indica",
    thc: 25, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 1350,
    floweringDays: 58, rating: 4.9, reviewsCount: 350,
    genetics: "Wedding Cake x Cheese (USA Collection refinement)",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, limonene: 30, humulene: 20 },
    flavors: ["Queso Cremoso Gourmet", "Frutas Dulces", "Fondo Terroso Intenso"],
    effects: ["Bienestar Corporal Profundo", "Estimulación Cerebral Creativa", "Potencia Devastadora"],
    activities: ["creativity", "relax_sleep", "social"],
    description: "El cruce más gourmand de la USA Collection de Buddha Seeds. La combinación de Wedding Cake y Cheese crea un perfil de sabor absolutamente único: queso cremoso con frutas dulces en una misma calada. Floración ultra rápida (52-65 días), producción colosal y cogollos ultra resinosos ideales para extracciones premium.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-negra-44",
    image: "img/rkiem-negra-44-bud.webp",
    name: "Negra 44",
    aka: "Sawla Ghana Landrace x Top 44",
    bank: "R-Kiem Seeds",
    species: "Indica",
    thc: 21, cbd: 0.3,
    yieldIndoor: 650, yieldOutdoor: 850,
    floweringDays: 58, rating: 4.9, reviewsCount: 540,
    genetics: "Sawla Ghana Landrace x Top 44",
    origin: "España / Ghana",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, pinene: 20 },
    flavors: ["Tierra Dulce", "Frutos Secos", "Especias Oscuras"],
    effects: ["Relajación Corporal Intensa", "Euforia Meditativa", "Bienestar"],
    activities: ["relax_sleep", "meditation"],
    description: "Variedad mítica galardonada de R-Kiem Seeds fruto del cruce entre una landrace autóctona de Sawla (Ghana) y Top 44. Destaca por sus tonos oscuros casi violetas en floración y una densidad de resina extraordinaria ideal para extracciones.",
    visualColor: "linear-gradient(135deg, #1E1B4B 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-sublimator",
    image: "img/rkiem-sublimator-bud.webp",
    name: "Sublimator",
    aka: "Sour Banana x Gorilla Glue #4",
    bank: "R-Kiem Seeds",
    species: "Híbrida",
    thc: 24, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 900,
    floweringDays: 63, rating: 4.9, reviewsCount: 480,
    genetics: "Sour Banana x Gorilla Glue #4",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Kush Afrutado", "Plátano Ácido", "Combustible Terroso"],
    effects: ["Potencia Demoledora", "Relax Mental & Físico", "Creatividad"],
    activities: ["creativity", "relax_sleep", "social"],
    description: "Nacida en honor al célebre vaporizador Sublimator. Cruce de Sour Banana y Gorilla Glue #4 con una resina adhesiva gigantesca, perfecta para los amantes de las extracciones rosin/BHO más potentes.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #15803D 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-icer",
    image: "img/rkiem-icer-bud.webp",
    name: "Icer",
    aka: "San Fernando Valley OG x Ice Cream",
    bank: "R-Kiem Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 56, rating: 4.9, reviewsCount: 620,
    genetics: "San Fernando Valley OG Kush x Ice Cream",
    origin: "España / California",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, caryophyllene: 30, myrcene: 25 },
    flavors: ["Ácido Cítrico", "Kush Terroso", "Diésel Escarchado"],
    effects: ["Cerebral Enérgico", "Estimulación Creativa", "Risas y Alegría"],
    activities: ["creativity", "social", "nature_walk"],
    description: "La variedad insignia de R-Kiem Seeds tras 11 años de trabajo de crianza endogámica. Producción de tricomas arenosos sin precedentes, cogollos completamente blancos de resina de textura helada.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #0E7490 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-muse",
    image: "img/rkiem-muse-bud.webp",
    name: "Muse",
    aka: "OG Kush Canadiense x Oregon Diesel",
    bank: "R-Kiem Seeds",
    species: "Indica",
    thc: 20, cbd: 0.8,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 390,
    genetics: "OG Kush Canadiense x Oregon Diesel",
    origin: "España / Canadá",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, humulene: 20 },
    flavors: ["Especias y Clavo", "Combustible Diesel", "Pimienta Dulce"],
    effects: ["Inspiración Artística", "Relajación Muscular", "Calma Mental"],
    activities: ["creativity", "meditation", "relax_sleep"],
    description: "Cruce de OG Kush canadiense con Oregon Diesel. Ofrece un perfil aromático muy complejo donde destacan notas de clavo y pimienta con retrogusto a gasolina. Excelente para desconectar la mente y estimular el arte.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-portela",
    image: "img/rkiem-portela-bud.webp",
    name: "Portela",
    aka: "Icer x Jamaicana Lambsbread",
    bank: "R-Kiem Seeds",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 63, rating: 4.8, reviewsCount: 410,
    genetics: "Macho Icer x Hembra Jamaicana Lambsbread",
    origin: "España / Jamaica",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Limón Haze", "Hierbas Aromáticas", "Melisa Fresca"],
    effects: ["Subidón Energizante", "Despeje Mental", "Sociabilidad Efervescente"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Cruce premiado de un clon élite Icer con una landrace Jamaicana Lambsbread pura. Sativa vigorosa de rápida floración que llena cualquier cultivo de notas cítricas herbales y un subidón eufórico muy limpio.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-eli",
    image: "img/rkiem-eli-bud.webp",
    name: "Eli",
    aka: "Sawla Ghana x Rosetta Stone",
    bank: "R-Kiem Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 950,
    floweringDays: 60, rating: 4.8, reviewsCount: 370,
    genetics: "Ghana Landrace (Sawla) x Rosetta Stone",
    origin: "España / Ghana",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, ocimene: 25, caryophyllene: 20 },
    flavors: ["Mandarina Cítrica", "Fondo Haze", "Almizcle Floral"],
    effects: ["Mente Activa & Alerta", "Energía Diurna", "Euforia Alegre"],
    activities: ["creativity", "workout", "social"],
    description: "Cruce de genética ghanesa con la reputada Rosetta Stone. Aroma penetrante a mandarina fresca y matices florales. Ideal para consumir durante el día y realizar actividades físicas o creativas.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-zkiem",
    image: "img/rkiem-zkiem-bud.webp",
    name: "ZKiem",
    aka: "Zkittlez x Selección Afgana (Harybo)",
    bank: "R-Kiem Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 56, rating: 4.9, reviewsCount: 460,
    genetics: "Zkittlez x Selección Afgana (Harybo)",
    origin: "España / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Gominolas Frutales", "Chicle Ácido", "Tierra Kush"],
    effects: ["Felicidad Placentera", "Relajación Corporal", "Bienestar Total"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Anteriormente conocida como Harybo, combina la dulzura de gominolas de la afamada Zkittlez con la robustez y resina de una selección afgana de R-Kiem. Floración ultrarrápida en 8 semanas.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-2y2",
    image: "img/rkiem-2y2-bud.webp",
    name: "2y2",
    aka: "Alpha Cut Purple Punch x Norcal Do-Si-Dos",
    bank: "R-Kiem Seeds",
    species: "Indica",
    thc: 25, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 900,
    floweringDays: 56, rating: 4.9, reviewsCount: 410,
    genetics: "Alpha Cut Purple Punch x Norcal Do-Si-Dos",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 48, limonene: 32, linalool: 20 },
    flavors: ["Gasolina y Moras", "Mermelada Frutal", "Repostería Dulce"],
    effects: ["Sedación Potente", "Calma Física", "Euforia Inicial"],
    activities: ["relax_sleep", "meditation"],
    description: "Un potente cruce de la codiciada Purple Punch (Alpha Cut) con Do-Si-Dos de Norcal. Resina desbordante con aroma a repostería, moras y notas de gasolina. Efecto índico sedante de máxima clase.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-el-xupet-negre",
    image: "img/rkiem-el-xupet-negre-bud.webp",
    name: "El Xupet Negre",
    aka: "Krabby Patty x GMO Kush",
    bank: "R-Kiem Seeds",
    species: "Indica",
    thc: 26, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 60, rating: 5.0, reviewsCount: 510,
    genetics: "Krabby Patty (GSC x Fire OG) x GMO Kush",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, limonene: 30, myrcene: 20 },
    flavors: ["Galleta Ajo Diesel", "Cítrico Terroso", "Pino Escarchado"],
    effects: ["Golpe Cerebral & Físico", "Relajación Profunda", "Euforia Intensa"],
    activities: ["relax_sleep", "gaming"],
    description: "Edición especial galardonada en copas cannábicas internacionales. Potencia brutal rozando el 26% de THC, aroma penetrante a galleta de ajo y diésel. Carga terpenoides descomunal ideal para extraccionistas.",
    visualColor: "linear-gradient(135deg, #4C1D95 0%, #1F2937 100%)",
    bgPattern: "radial-gradient(circle, rgba(76,29,149,0.2) 0%, transparent 70%)"
  },
  {
id: "rkiem-klementine",
    image: "img/rkiem-klementine-bud.webp",
    name: "Klementine",
    aka: "Clementine x Purple Punch",
    bank: "R-Kiem Seeds",
    species: "Híbrida",
    thc: 23, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 850,
    floweringDays: 58, rating: 4.8, reviewsCount: 320,
    genetics: "Clementine x Purple Punch",
    origin: "España / California",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, caryophyllene: 25, myrcene: 20 },
    flavors: ["Clementina Cítrica", "Bayas Dulces", "Tierra Kush"],
    effects: ["Euforia Radiante", "Alegría Activa", "Relajación Suave"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Espectacular híbrido entre Clementine y Purple Punch. Perfil terpénico ultra cítrico con notas a clementinas maduras y frutos del bosque. Cogollos muy resinosos y coloridos de efecto eufórico y radiante.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-critical-47",
    image: "img/positronics-critical-47-bud.webp",
    name: "Critical 47",
    aka: "Critical Mass x AK-47",
    bank: "Positronics Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 525, yieldOutdoor: 600,
    floweringDays: 52, rating: 4.9, reviewsCount: 610,
    genetics: "Critical Mass x AK-47",
    origin: "Holanda / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Mango y Melocotón", "Vainilla Dulce", "Skunk Terroso"],
    effects: ["Relajación Corporal Profunda", "Alivio del Estrés", "Calma Mental"],
    activities: ["relax_sleep", "meditation"],
    description: "Considerada la 'Skunk perfecta' de Positronics. Gran combinación de rapidez y producción de Critical Mass con la desbordante potencia de AK-47. Aroma irresistible a mango dulce y fruta madura con vainilla.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-somango-47",
    image: "img/positronics-somango-47-bud.webp",
    name: "Somango 47",
    aka: "Somango x Critical 47",
    bank: "Positronics Seeds",
    species: "Indica",
    thc: 21, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 68, rating: 4.9, reviewsCount: 540,
    genetics: "Somango x Critical 47",
    origin: "Holanda / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Mango Tropical", "Licor Dulce", "Fruta de la Pasión"],
    effects: ["Euforia Placentera", "Relajación Corporal", "Sensación Festiva"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "Apodada 'La Bestia' en Positronics. Híbrido extremadamente aromático con denso olor a mango tropical y licor. Cogollos muy densos cubiertos de resina con efecto eufórico y altamente relajante.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-purple-haze",
    image: "img/positronics-purple-haze-bud.webp",
    name: "Purple Haze #1",
    aka: "Purple Thai x Haze #1",
    bank: "Positronics Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 70, rating: 4.8, reviewsCount: 490,
    genetics: "Purple Thai x Haze #1",
    origin: "Holanda / Tailandia",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Incienso Especiado", "Bayas Canela", "Licor Dulce"],
    effects: ["Estimulación Cerebral Intensa", "Euforia Psicodélica", "Creatividad"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Tributo al clásico legendario de Jimi Hendrix. Desarrolla vistosos tonos púrpuras en las flores y hojas. Inciensada y especiada, produce un subidón cerebral limpio, festivo y muy psicoactivo.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-claustrum",
    image: "img/positronics-claustrum-bud.webp",
    name: "Claustrum",
    aka: "(SSH x Jack Herer) x Kali Mist",
    bank: "Positronics Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 80, rating: 4.8, reviewsCount: 420,
    genetics: "(Super Silver Haze x Jack Herer) x Kali Mist",
    origin: "Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Incienso Catedralicio", "Pino Fresco", "Eucalipto Cítrico"],
    effects: ["Claridad Mental Lúcida", "Subidón Psicoactivo", "Energía Creativa"],
    activities: ["creativity", "nature_walk", "workout"],
    description: "Una auténtica obra maestra tri-sativa de Positronics. Combina la genética de Super Silver Haze, Jack Herer y Kali Mist. Aroma que evoca el incienso de una catedral antigua con toque a eucalipto.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #0E7490 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-cum-laude",
    image: "img/positronics-cum-laude-bud.webp",
    name: "Cum Laude",
    aka: "(Reina Madre x Tijuana) x Original Haze",
    bank: "Positronics Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 475, yieldOutdoor: 600,
    floweringDays: 77, rating: 4.9, reviewsCount: 360,
    genetics: "(Reina Madre x Tijuana) x Original Haze",
    origin: "Holanda / España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, pinene: 30, myrcene: 25 },
    flavors: ["Anís Herbal", "Lavanda y Especias", "Café Tostado"],
    effects: ["Pensamiento Lúcido", "Euforia Intelectual", "Enfoque Total"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Desarrollada en homenaje al célebre filósofo Antonio Escohotado. Triple cruce sativo de aroma anisado con notas de lavanda y café. Un subidón puramente cerebral, lúcido y estimulante para el intelecto.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #3F6212 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-caramelice",
    image: "img/positronics-caramelice-bud.webp",
    name: "Caramelice",
    aka: "Caramela x Super Skunk",
    bank: "Positronics Seeds",
    species: "Híbrida",
    thc: 19, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 450,
    genetics: "Caramela x Super Skunk",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, limonene: 35, caryophyllene: 20 },
    flavors: ["Mandarina Dulce", "Caramelo Tostado", "Cítrico Dulce"],
    effects: ["Euforia Alegre", "Desconexión del Estrés", "Relax Físico Suave"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "Evolución de la mítica línea Skunk con un toque acaramelado. Sorprende por un penetrante aroma a cítricos y mandarina madura con matices dulces. Efecto alegre, energizante al inicio y relajante al final.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-blue-rhino",
    image: "img/positronics-blue-rhino-bud.webp",
    name: "Blue Rhino",
    aka: "Blueberry x White Rhino",
    bank: "Positronics Seeds",
    species: "Indica",
    thc: 20, cbd: 0.5,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.8, reviewsCount: 430,
    genetics: "Blueberry x White Rhino",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Arándanos y Moras", "Madera Noble", "Especias Kush"],
    effects: ["Sedación Muscular Profunda", "Alivio del Dolor", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "Variedad médica por excelencia en el catálogo de Positronics. Híbrido entre la sabrosa Blueberry y la devastadora White Rhino. Cogollos azulados muy resinosos de efecto sedante e hipnótico.",
    visualColor: "linear-gradient(135deg, #2563EB 0%, #1E3A8A 100%)",
    bgPattern: "radial-gradient(circle, rgba(37,99,235,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-amnesia-mystery",
    image: "img/positronics-amnesia-mystery-bud.webp",
    name: "Amnesia Mystery",
    aka: "Amnesia Haze x California Sativa",
    bank: "Positronics Seeds",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 900,
    floweringDays: 75, rating: 4.9, reviewsCount: 470,
    genetics: "Amnesia Haze x Genética Misteriosa Californiana",
    origin: "Holanda / USA",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, pinene: 20 },
    flavors: ["Pino Mentolado", "Regaliz Dulce", "Café Especiado"],
    effects: ["Potencia Psicoactiva Desbordante", "Inspiración Creativa", "Energía"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Desarrollada tras seleccionar el mejor clon de Amnesia Haze y cruzarlo con una misteriosa sativa de las montañas californianas. Vigor impresionante en floración con aroma a pino mentolado y regaliz.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-black-widow",
    image: "img/positronics-black-widow-bud.webp",
    name: "Black Widow",
    aka: "White Widow x Afgana Oscura",
    bank: "Positronics Seeds",
    species: "Indica",
    thc: 21, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 550,
    floweringDays: 58, rating: 4.8, reviewsCount: 400,
    genetics: "White Widow x Afgana Oscura",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, humulene: 20 },
    flavors: ["Maderas Florales", "Tierra Húmeda", "Hachís Afgano"],
    effects: ["Relajación Corporal Total", "Sensación Antiestrés", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Interpretación propia de la mítica familia Widow. Planta compacta, resistente y de rapidísima floración con hojas tan oscuras que casi parecen negras. Copiosa capa de resina cristalina de efecto relajante.",
    visualColor: "linear-gradient(135deg, #374151 0%, #111827 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.2) 0%, transparent 70%)"
  },
  {
id: "positronics-supercheese",
    image: "img/positronics-supercheese-bud.webp",
    name: "Supercheese",
    aka: "Old School UK Cheese x Caramela",
    bank: "Positronics Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 525, yieldOutdoor: 650,
    floweringDays: 58, rating: 4.8, reviewsCount: 380,
    genetics: "Old School UK Cheese x Caramela",
    origin: "Holanda / UK",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Queso Curado Penetrante", "Lácteo Dulce", "Tierra Especiada"],
    effects: ["Relax Placentero", "Sensación de Bienestar", "Abre el Apetito"],
    activities: ["relax_sleep", "social"],
    description: "Homenaje a la inolvidable cultura 'Cheese' de los noventa. Mantiene el inconfundible aroma a queso curado y lácteos con la rapidez y resina de Positronics. Un sabor retro e imborrable para los sibaritas del cannabis.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-panama",
    image: "img/aceseeds-panama-bud.webp",
    name: "Panama",
    aka: "Panama Diosa x Panama Verde/Roja",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 24, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 850,
    floweringDays: 77, rating: 5.0, reviewsCount: 680,
    genetics: "Panama Diosa x Panama Verde/Roja (Landrace 70s)",
    origin: "Panamá / España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Limón Dulce", "Vainilla Especiada", "Incienso Tropical"],
    effects: ["Potencia Psicodélica Limpia", "Energía Eufórica", "Creatividad"],
    activities: ["creativity", "nature_walk", "social"],
    description: "Una de las sativas puras más famosas y trabajadas del mundo. Híbrido de 3 genéticas landrace panameñas adaptado durante décadas. Desarrollo espectacular con pistiles rojos y rosas en floración, aroma a limón y vainilla.",
    visualColor: "linear-gradient(135deg, #EF4444 0%, #B91C1C 100%)",
    bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-malawi",
    image: "img/aceseeds-malawi-bud.webp",
    name: "Malawi",
    aka: "Killer Malawi Landrace P3",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 27, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 85, rating: 5.0, reviewsCount: 720,
    genetics: "Killer Malawi Landrace P3",
    origin: "Malaui (África)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Aceite de Zanahoria", "Madera de Cedro", "Mandarina Dulce"],
    effects: ["Efecto Devastador Narcótico", "Triposo Psicodélico", "Duración Extrema"],
    activities: ["meditation", "nature_walk"],
    description: "La sativa pura más potente y destructiva del planeta. Concentraciones masivas de cannabinoides que pueden superar el 27% de THC. Solo recomendada para usuarios expertos que busquen experiencias de potencia limite.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-golden-tiger",
    image: "img/aceseeds-golden-tiger-bud.webp",
    name: "Golden Tiger",
    aka: "Killer Malawi x Meao Thai Landrace",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 28, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 900,
    floweringDays: 84, rating: 5.0, reviewsCount: 590,
    genetics: "Killer Malawi x Meao Thai Landrace",
    origin: "Malaui / Tailandia",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, myrcene: 20 },
    flavors: ["Mandarina Madura", "Limón Ácido", "Madera Orgánica"],
    effects: ["Subidón Psicodélico Abrumador", "Estímulo Cerebral", "Euforia"],
    activities: ["creativity", "nature_walk"],
    description: "Espectacular cruce entre las dos mejores sativas puras de África y Asia: Killer Malawi y Meao Thai. Cogollos dorados hiperresinosos con potencia psicoactiva extrema sin techo aparente.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-zamaldelica",
    image: "img/aceseeds-zamaldelica-bud.webp",
    name: "Zamaldelica",
    aka: "Zamal Landrace x Golden Tiger",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 27, cbd: 0.1,
    yieldIndoor: 525, yieldOutdoor: 800,
    floweringDays: 80, rating: 5.0, reviewsCount: 650,
    genetics: "Zamal Landrace (Isla Reunión) x Golden Tiger",
    origin: "Isla Reunión / Malaui",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 55, limonene: 25, ocimene: 20 },
    flavors: ["Mango Zanahoria", "Dulce Floral", "Eucalipto Cítrico"],
    effects: ["Subidón Psicodélico Radiante", "Euforia Eléctrica", "Claridad"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Un híbrido sativa legendario creado cruzando la mítica landrace Zamal de la Isla Reunión con Golden Tiger. Famosa por sus efectos cerebrales eléctricos, eufóricos y de expansión sensorial.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-pakistan-chitral-kush",
    image: "img/aceseeds-pakistan-chitral-kush-bud.webp",
    name: "Pakistan Chitral Kush",
    aka: "PCK Landrace P2",
    bank: "ACE Seeds",
    species: "Indica",
    thc: 16, cbd: 0.5,
    yieldIndoor: 400, yieldOutdoor: 500,
    floweringDays: 56, rating: 4.9, reviewsCount: 580,
    genetics: "Pakistan Chitral Kush Landrace P2",
    origin: "Pakistán (Chitral)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, pinene: 20 },
    flavors: ["Moras y Caramelo", "Hachís Dulce", "Tierra Kush"],
    effects: ["Relajación Placentera", "Efecto Meditativo", "Calma Muscular"],
    activities: ["relax_sleep", "meditation"],
    description: "La célebre landrace índica pura paquistaní. Famosa mundialmente por sus espectaculares colores magenta y púrpura oscuro, además de su tremenda resistencia a hongos y frío. Perfecta para hacer hachís dulce de mora.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #5B21B6 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-violeta",
    image: "img/aceseeds-violeta-bud.webp",
    name: "Violeta",
    aka: "PCK x Killer Malawi",
    bank: "ACE Seeds",
    species: "Indica",
    thc: 17, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 60, rating: 4.8, reviewsCount: 440,
    genetics: "Pakistan Chitral Kush x Killer Malawi",
    origin: "Pakistán / Malaui",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, limonene: 25 },
    flavors: ["Frutos del Bosque", "Uva y Balsámico", "Hachís Especiado"],
    effects: ["Relajación Equilibrada", "Bienestar Físico", "Calma Mental"],
    activities: ["relax_sleep", "social", "meditation"],
    description: "Un cruce fascinante que combina la belleza y colorido violeta de la PCK paquistaní con el vigor y potencia de la Killer Malawi. Cogollos púrpuras muy resinosos de aroma frutal a moras y uvas.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-purple-haze-x-malawi",
    image: "img/aceseeds-purple-haze-x-malawi-bud.webp",
    name: "Purple Haze x Malawi",
    aka: "Purple Haze #1 x Killer Malawi",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 25, cbd: 0.1,
    yieldIndoor: 525, yieldOutdoor: 850,
    floweringDays: 90, rating: 4.9, reviewsCount: 460,
    genetics: "Purple Haze #1 x Killer Malawi",
    origin: "Tailandia / Malaui",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Licor Inciensado", "Moras Silvestres", "Especias Oscuras"],
    effects: ["Subidón Psicodélico Devastador", "Euforia Sin Límite", "Creatividad"],
    activities: ["creativity", "nature_walk"],
    description: "Uno de los híbridos sativa más potentes e inciensados jamás creados. Cruce entre la mítica Purple Haze y la devoradora Killer Malawi. Floración larga pero de recompensa monumental en flor resinosa morada.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #311075 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-super-malawi-haze",
    image: "img/aceseeds-super-malawi-haze-bud.webp",
    name: "Super Malawi Haze",
    aka: "Nevil's Haze x Killer Malawi",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 26, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 80, rating: 5.0, reviewsCount: 410,
    genetics: "Nevil's Haze x Killer Malawi",
    origin: "Holanda / Malaui",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 52, limonene: 28, pinene: 20 },
    flavors: ["Incienso Nevil", "Madera Pino", "Flor Cítrica"],
    effects: ["Cerebral Demoledor", "Energía Eufórica", "Larga Duración"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Directamente desde el olimpo de las Haze. Cruce de la legendaria Nevil's Haze con Killer Malawi. Producción gigante en interior y exterior con inconfundible aroma catedralicio a incienso y pino.",
    visualColor: "linear-gradient(135deg, #059669 0%, #064E3B 100%)",
    bgPattern: "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-congo",
    image: "img/aceseeds-congo-bud.webp",
    name: "Congo",
    aka: "Congo #3 x (Bangi Haze x Chitral)",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 19, cbd: 0.2,
    yieldIndoor: 450, yieldOutdoor: 650,
    floweringDays: 70, rating: 4.8, reviewsCount: 380,
    genetics: "Congo #3 x (Bangi Haze x Chitral)",
    origin: "Congo / Nepal / Pakistán",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, terpinolene: 30, pinene: 25 },
    flavors: ["Fresa Salvaje", "Limón Fresco", "Flor Silvestre"],
    effects: ["Alegría Limpia", "Energía Diurna", "Bienestar Activo"],
    activities: ["social", "nature_walk", "workout"],
    description: "Deliciosa sativa africana de rápida floración gracias a la influencia de Bangi Haze y Chitral. Sabor exótico a fresas silvestres y limón con un subidón diurno alegre y de cabeza muy clara.",
    visualColor: "linear-gradient(135deg, #E11D48 0%, #9F1239 100%)",
    bgPattern: "radial-gradient(circle, rgba(225,29,72,0.2) 0%, transparent 70%)"
  },
  {
id: "aceseeds-guawi",
    image: "img/aceseeds-guawi-bud.webp",
    name: "Guawi",
    aka: "Old Malawi Killer x Guatemala Landrace",
    bank: "ACE Seeds",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 525, yieldOutdoor: 750,
    floweringDays: 80, rating: 4.8, reviewsCount: 340,
    genetics: "Old Malawi Killer x Guatemala Sativa Landrace",
    origin: "Malaui / Guatemala",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Madera Dulce", "Mango Maduro", "Especias Tropicales"],
    effects: ["Potencia Psicodélica", "Relajación Corporal", "Euforia Prolongada"],
    activities: ["creativity", "nature_walk", "meditation"],
    description: "Excelente híbrido sativa entre la ancestral Guatemala landrace y la mítica Killer Malawi. Estructura fuerte y ramificada con sabor dulce a mango y maderas tropicales. Efecto psicodélico y duradero.",
    visualColor: "linear-gradient(135deg, #CA8A04 0%, #854D0E 100%)",
    bgPattern: "radial-gradient(circle, rgba(202,138,4,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-tutankhamon",
    image: "img/pyramid-tutankhamon-bud.webp?v=2026_custom_hd",
    name: "Tutankhamon",
    aka: "Selección Élite AK-47",
    bank: "Pyramid Seeds",
    species: "Sativa",
    thc: 25, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 60, rating: 5.0, reviewsCount: 780,
    genetics: "Selección Élite AK-47",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, caryophyllene: 20 },
    flavors: ["Skunk Cítrico", "Madera Fresca", "Fruta Madura"],
    effects: ["Subidón Cerebral Demoledor", "Euforia Intensa", "Energía Creativa"],
    activities: ["creativity", "social", "nature_walk"],
    description: "El buque insignia de Pyramid Seeds. Selección histórica de AK-47 analizada con niveles de THC desbordantes del 25%+. Cogollos densos y cargados de resina con aroma a Skunk cítrico y madera.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-anesthesia",
    image: "img/pyramid-anesthesia-bud.webp",
    name: "Anesthesia",
    aka: "Northern Lights x Black Domina",
    bank: "Pyramid Seeds",
    species: "Indica",
    thc: 21, cbd: 0.4,
    yieldIndoor: 525, yieldOutdoor: 650,
    floweringDays: 55, rating: 4.9, reviewsCount: 510,
    genetics: "Northern Lights x Black Domina",
    origin: "España / Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, humulene: 20 },
    flavors: ["Tierra Dulce", "Hachís Afgano", "Ácido Suave"],
    effects: ["Efecto Anestésico Narcótico", "Sedación Corporal", "Descanso Total"],
    activities: ["relax_sleep", "meditation"],
    description: "Un cruce devastador entre dos verdaderos titanes índicos: Northern Lights y Black Domina. Gran densidad de flor resinosa de tono verde oscuro con un efecto puramente anestésico y relajante.",
    visualColor: "linear-gradient(135deg, #1E1B4B 0%, #312E81 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-nefertiti",
    image: "img/pyramid-nefertiti-bud.webp",
    name: "Nefertiti",
    aka: "Black Widow x White Widow",
    bank: "Pyramid Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 75, rating: 4.8, reviewsCount: 460,
    genetics: "Black Widow x White Widow",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Haze Inciensado", "Cítrico Limón", "Toque Reguliz"],
    effects: ["Subidón Eufórico Mental", "Energía Diurna", "Estimulación"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Premio Spannabis. Un cruce excepcional de Black Widow con White Widow refinado hacia una morfología y efecto sativo deslumbrante. Hojas anchas tipo índica en crecimiento que se convierten en lanzas sativas en floración.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-kryptonite",
    image: "img/pyramid-kryptonite-bud.webp",
    name: "Kryptonite",
    aka: "Yumboldt x Sativa Granada",
    bank: "Pyramid Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 62, rating: 4.8, reviewsCount: 430,
    genetics: "Yumboldt x Selección de Valles de Granada",
    origin: "España / USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, terpinolene: 35, caryophyllene: 20 },
    flavors: ["Ácido Cítrico Haze", "Tierra Dulce", "Fruta Escarchada"],
    effects: ["Estimulación Cerebral Rápida", "Claridad Mental", "Energía"],
    activities: ["creativity", "workout", "social"],
    description: "Creada a partir del cruce de Yumboldt con sativas seleccionadas de los valles granadinos. Sativa de floración asombrosamente rápida (60-65 días) con cogollos pesados y aroma fuertemente ácido e inciensado.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-anubis",
    image: "img/pyramid-anubis-bud.webp",
    name: "Anubis",
    aka: "Somango x Wembley",
    bank: "Pyramid Seeds",
    species: "Indica",
    thc: 19, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 56, rating: 4.8, reviewsCount: 390,
    genetics: "Somango x Wembley",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, limonene: 32, caryophyllene: 20 },
    flavors: ["Pomelo Tropical", "Fruta Dulce", "Tierra Especiada"],
    effects: ["Relajación Corporal Placentera", "Sensación De Calma", "Bienestar"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Cruce dulce y afrutado de Somango con Wembley. Planta de porte medio muy productiva y de rápido desarrollo con un aroma característico a pomelo fresco y matices dulces.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-blue-pyramid",
    image: "img/pyramid-blue-pyramid-bud.webp",
    name: "Blue Pyramid",
    aka: "Selección Élite Blueberry",
    bank: "Pyramid Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 55, rating: 4.9, reviewsCount: 480,
    genetics: "Selección Élite Blueberry",
    origin: "España / USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Arándanos Dulces", "Frutos del Bosque", "Exótico Ácido"],
    effects: ["Relajación Física Intensa", "Tranquilidad Mental", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Selección de Blueberry estabilizada por Pyramid Seeds. Hermosos cogollos azulados cargados de resina blanca con un inconfundible sabor dulce a arándanos y frutos silvestres.",
    visualColor: "linear-gradient(135deg, #2563EB 0%, #1E3A8A 100%)",
    bgPattern: "radial-gradient(circle, rgba(37,99,235,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-ramses",
    image: "img/pyramid-ramses-bud.webp",
    name: "Ramses",
    aka: "Amnesia Haze x Selección Pyramid",
    bank: "Pyramid Seeds",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 850,
    floweringDays: 75, rating: 4.8, reviewsCount: 350,
    genetics: "Amnesia Haze x Selección Pyramid",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Cítrico Haze", "Incienso Dulce", "Pino Fresco"],
    effects: ["Potencia Cerebral Eufórica", "Creatividad Desborde", "Energía"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Descendiente directa de la familia Amnesia Haze. Planta de gran porte y crecimiento exuberante con cogollos alargados cargados de tricomas y un perfil cítrico inciensado inolvidable.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #A16207 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-galaxy",
    image: "img/pyramid-galaxy-bud.webp",
    name: "Galaxy",
    aka: "Afghani x Northern Lights",
    bank: "Pyramid Seeds",
    species: "Indica",
    thc: 21, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 55, rating: 4.8, reviewsCount: 420,
    genetics: "Afghani x Northern Lights",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, pinene: 20 },
    flavors: ["Menta Dulce", "Pino Terroso", "Hachís Afgano"],
    effects: ["Relajación Físico-Mental", "Sensación Antiestrés", "Sueño Placentero"],
    activities: ["relax_sleep", "meditation"],
    description: "Un híbrido con aroma galáctico a menta fresca y pino fruto del cruce entre una afgana pura y Northern Lights. Producción muy pesada con ramas gruesas repletas de flores resinosas.",
    visualColor: "linear-gradient(135deg, #4C1D95 0%, #1E1B4B 100%)",
    bgPattern: "radial-gradient(circle, rgba(76,29,149,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-wembley",
    image: "img/pyramid-wembley-bud.webp?v=2026_custom_hd",
    name: "Wembley",
    aka: "AK-47 x Bubble Gum",
    bank: "Pyramid Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 58, rating: 4.8, reviewsCount: 400,
    genetics: "AK-47 x Bubble Gum",
    origin: "España",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Chicle de Fresa", "Fruta Tropical", "Skunk Dulce"],
    effects: ["Euforia Relajante", "Bienestar Alegré", "Descanso Suave"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "Cruce místico de AK-47 con la dulce Bubble Gum. Destaca por un inolvidable sabor a chicle de fresa y frutas dulces con un efecto duradero, eufórico y físicamente reconfortante.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "pyramid-shark",
    image: "img/pyramid-shark-bud.webp",
    name: "Shark",
    aka: "Super Skunk x Northern Lights",
    bank: "Pyramid Seeds",
    species: "Indica",
    thc: 19, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 55, rating: 4.7, reviewsCount: 370,
    genetics: "Super Skunk x Northern Lights",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, humulene: 20 },
    flavors: ["Skunk Penetrante", "Golosina Dulce", "Tierra Húmeda"],
    effects: ["Relax Corporal Narcótico", "Tranquilidad", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Una variedad sumamente robusta y fácil de cultivar nacida del cruce entre Super Skunk y Northern Lights. Muy resinosa y aromática con sabor dulzón tipo golosina Skunk.",
    visualColor: "linear-gradient(135deg, #0284C7 0%, #0369A1 100%)",
    bgPattern: "radial-gradient(circle, rgba(2,132,199,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-mamba-negra",
    image: "img/blimburn-mamba-negra-bud.webp",
    name: "Mamba Negra",
    aka: "Critical Mass x Skunk #1",
    bank: "Blimburn Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.9, reviewsCount: 640,
    genetics: "Critical Mass x Skunk #1",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Frutas Dulces", "Skunk Terroso", "Cítrico Suave"],
    effects: ["Relajación Corporal Profunda", "Euforia Placentera", "Calma"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Una de las variedades más galardonadas de Blimburn Seeds. Cruce entre la súper productora Critical Mass y Skunk #1. Destaca por sus grandes cogollos apretados con un perfume afrutado de Skunk y efecto físico seductor.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-granddaddy-purple",
    image: "img/blimburn-granddaddy-purple-bud.webp",
    name: "Granddaddy Purple",
    aka: "Purple Urkle x Big Bud",
    bank: "Blimburn Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 60, rating: 5.0, reviewsCount: 710,
    genetics: "Purple Urkle x Big Bud",
    origin: "USA (California)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Uvas Dulces", "Baya Silvestre", "Madera Noble"],
    effects: ["Sedación Corporal Profunda", "Bienestar Antiestrés", "Sueño"],
    activities: ["relax_sleep", "meditation"],
    description: "Un clásico imprecindible de la costa oeste americana. Famosa por sus tonalidades moradas y púrpuras espectaculares. Aroma embriagador a uvas maduras y moras silvestres con un potente efecto sedante.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-bruce-banner-3",
    image: "img/blimburn-bruce-banner-3-bud.webp",
    name: "Bruce Banner #3",
    aka: "OG Kush x Strawberry Diesel",
    bank: "Blimburn Seeds",
    species: "Híbrida",
    thc: 27, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 65, rating: 5.0, reviewsCount: 680,
    genetics: "OG Kush x Strawberry Diesel",
    origin: "USA (Colorado)",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, caryophyllene: 35, myrcene: 20 },
    flavors: ["Combustible Diesel", "Fresa Dulce", "Tierra Kush"],
    effects: ["Potencia Demoledora", "Euforia Estimulante", "Creatividad"],
    activities: ["creativity", "nature_walk", "social"],
    description: "Bautizada en honor al alter ego del Increíble Hulk por su colosal potencia. Supera fácilmente el 27% de THC. Perfil aromático complejo que combina notas de combustible diésel con matices dulces de fresa.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #3F6212 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-gorilla-glue-4",
    image: "img/blimburn-gorilla-glue-4-bud.webp",
    name: "Gorilla Glue #4",
    aka: "Chem's Sister x Sour Dubb x Chocolate Diesel",
    bank: "Blimburn Seeds",
    species: "Híbrida",
    thc: 27, cbd: 0.1,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 63, rating: 5.0, reviewsCount: 750,
    genetics: "Chem's Sister x Sour Dubb x Chocolate Diesel",
    origin: "USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 48, myrcene: 32, limonene: 20 },
    flavors: ["Pino y Combustible", "Chocolate Amargo", "Químico Especiado"],
    effects: ["Bloqueo de Sofá", "Euforia Cerebral", "Relajación Muscular"],
    activities: ["relax_sleep", "gaming", "meditation"],
    description: "Famosa mundialmente por pegar literalmente las tijeras de manicurar por su ingente cantidad de resina. Cogollos ultradensos con aroma a combustible, pino y chocolate con efecto demoledor.",
    visualColor: "linear-gradient(135deg, #374151 0%, #111827 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-girl-scout-cookies",
    image: "img/blimburn-girl-scout-cookies-bud.webp",
    name: "Girl Scout Cookies",
    aka: "OG Kush x Durban Poison",
    bank: "Blimburn Seeds",
    species: "Híbrida",
    thc: 25, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.9, reviewsCount: 620,
    genetics: "OG Kush x Durban Poison",
    origin: "USA (California)",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Menta Dulce", "Galleta Tostada", "Tierra Kush"],
    effects: ["Euforia Cerebral Placentera", "Relajación Corporal", "Bienestar"],
    activities: ["social", "creativity", "relax_sleep"],
    description: "La icónica cepa californiana que revolucionó los dispensarios norteamericanos. Fusiona la fuerza de OG Kush con la energía africana de Durban Poison. Sabor a masa de galleta horneada y menta.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-green-crack",
    image: "img/blimburn-green-crack-bud.webp",
    name: "Green Crack",
    aka: "Skunk #1 x Afghani Landrace",
    bank: "Blimburn Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.1,
    yieldIndoor: 600, yieldOutdoor: 700,
    floweringDays: 55, rating: 4.8, reviewsCount: 490,
    genetics: "Skunk #1 x Afghani Landrace",
    origin: "USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, limonene: 35, caryophyllene: 20 },
    flavors: ["Mango Frutal", "Cítrico Limón", "Skunk Dulce"],
    effects: ["Energía Imparable", "Enfoque Mental Lúcido", "Euforia Radiante"],
    activities: ["workout", "creativity", "social"],
    description: "Bautizada por Snoop Dogg debido a su inigualable chute de energía mental. Sativa extremadamente rápida de cosechar (55 días) con un tentador aroma a mango tropical y cítricos frescos.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-santa-muerte",
    image: "img/blimburn-santa-muerte-bud.webp",
    name: "Santa Muerte",
    aka: "Mexican Sativa Selection",
    bank: "Blimburn Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 75, rating: 4.8, reviewsCount: 390,
    genetics: "Mexican Sativa Selection",
    origin: "México / España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Incienso Haze", "Hierba Fresca", "Especias Ácidas"],
    effects: ["Subidón Cerebral Muy Psicoactivo", "Claridad Mental", "Energía"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Sativa pura mexicana seleccionada por Blimburn. Planta de crecimiento vigoroso y gran distancia internodal con flores inciensadas que ofrecen un subidón cerebral diáfano y psicoactivo.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-guanabana",
    image: "img/blimburn-guanabana-bud-real.webp",
    name: "Guanabana",
    aka: "Amnesia Haze x White Widow",
    bank: "Blimburn Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 370,
    genetics: "Amnesia Haze x White Widow",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Fruta Tropical", "Melocotón Madura", "Incienso Dulce"],
    effects: ["Euforia Estimulante", "Relajación Corporal Equilibrada", "Alegría"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Híbrido masivo que cruza Amnesia Haze con White Widow. Crecimiento muy ramificado con cogollos repletos de tricomas y un perfume a frutas exóticas tropicales con toques de melocotón.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-chocolopez",
    image: "img/blimburn-chocolopez-bud.webp",
    name: "Chocolopez",
    aka: "Chocolate Thai x Cannalope Haze",
    bank: "Blimburn Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.2,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 70, rating: 4.8, reviewsCount: 410,
    genetics: "Chocolate Thai x Cannalope Haze",
    origin: "USA / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, terpinolene: 35, caryophyllene: 20 },
    flavors: ["Chocolate Amargo", "Melón Dulce", "Tierra Especiada"],
    effects: ["Euforia Cerebral Festiva", "Creatividad", "Energía Diurna"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Homenaje a la inolvidable Chocolate Thai retro. Combina los sabores a cacao puro con el toque a melón fresco de Cannalope Haze. Subidón sativa muy alegre, eufórico y sociabilizador.",
    visualColor: "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
    bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  },
  {
id: "blimburn-bcn-diesel",
    image: "img/blimburn-bcn-diesel-bud.webp",
    name: "Bcn Diesel",
    aka: "Diesel x Selección Barcelona",
    bank: "Blimburn Seeds",
    species: "Híbrida",
    thc: 20, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 65, rating: 4.7, reviewsCount: 360,
    genetics: "Diesel x Selección Barcelona",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 48, caryophyllene: 32, pinene: 20 },
    flavors: ["Combustible Diésel", "Cítrico Toronja", "Pino Terroso"],
    effects: ["Euforia Cerebral Rápida", "Relajación Corporal Suave", "Energía"],
    activities: ["social", "creativity", "workout"],
    description: "Versión mediterránea de la mítica New York City Diesel. Destaca por su penetrante fragancia a carburante diésel y pomelo rosado. Efecto cerebral muy potente y duradero.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-kritikal-bilbo",
    image: "img/genehtik-kritikal-bilbo-bud.webp",
    name: "Kritikal Bilbo",
    aka: "Clon Élite Bilbo (Critical Mass)",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 1800,
    floweringDays: 48, rating: 5.0, reviewsCount: 950,
    genetics: "Clon Élite Bilbo (Critical Mass)",
    origin: "País Vasco (España)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Dulce Aromatizado", "Frutal Intenso", "Skunk Cítrico"],
    effects: ["Relajación Corporal Potente", "Euforia Placentera", "Sensación Antiestrés"],
    activities: ["relax_sleep", "social", "meditation"],
    description: "La leyenda absoluta del cannabis español. Clon seleccionado en Bilbao a finales de los 90 famoso por su aroma dulce e hiperintenso, floración ultra rápida de 45-50 días y producción gigantesca.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-txomango",
    image: "img/genehtik-txomango-bud.webp",
    name: "Txomango",
    aka: "Selección Somango Bilbo",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 19, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 63, rating: 4.9, reviewsCount: 580,
    genetics: "Selección Somango (Super Skunk x Jack Herer x Big Skunk Korean)",
    origin: "País Vasco (España)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, limonene: 28, caryophyllene: 20 },
    flavors: ["Mango Tropical", "Licor de Frutas", "Dulce Empalagoso"],
    effects: ["Efecto Relajante Placentero", "Bienestar Físico", "Calma"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Selección vasca del clon Somango original. Planta muy ramificada de porte maderable con un denso perfume a mango tropical fresco y licor dulce. Cogollos voluminosos repleto de resina.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-super-silver-bilbo",
    image: "img/genehtik-super-silver-bilbo-bud.webp",
    name: "Super Silver Bilbo",
    aka: "Selección Super Silver Haze",
    bank: "Genehtik Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 70, rating: 4.9, reviewsCount: 520,
    genetics: "Selección Super Silver Haze",
    origin: "País Vasco (España)",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Incienso Catedral", "Pino Fresco", "Cítrico Limón"],
    effects: ["Subidón Cerebral Psicodélico", "Euforia Limpia", "Energía Creativa"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Selección clásica premiada del legendario clon Super Silver Haze. Destaca por su inconfundible fragancia a incienso metálico de catedral y pino con un subidón eufórico y psicoactivo desbordante.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-zuri-widow",
    image: "img/genehtik-zuri-widow-bud.webp",
    name: "Zuri Widow",
    aka: "Selección White Widow Élite",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 19, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 56, rating: 4.8, reviewsCount: 440,
    genetics: "Selección White Widow Élite",
    origin: "País Vasco / Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, pinene: 20 },
    flavors: ["Tierra Floral", "Pino Dulce", "Musgo Seco"],
    effects: ["Relajación Muscular", "Efecto Narcótico Suave", "Tranquilidad"],
    activities: ["relax_sleep", "meditation"],
    description: "Selección autóctona del clon de White Widow ('Zuri' significa blanco en euskera). Planta compacta y achaparrada recubierta por un manto espeso de cristales blancos de efecto corporal indeseable para el estrés.",
    visualColor: "linear-gradient(135deg, #64748B 0%, #334155 100%)",
    bgPattern: "radial-gradient(circle, rgba(100,116,139,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-txees-bilbo",
    image: "img/genehtik-txees-bilbo-bud.webp",
    name: "Txees Bilbo",
    aka: "Selección UK Cheese",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 55, rating: 4.8, reviewsCount: 410,
    genetics: "Selección UK Cheese",
    origin: "País Vasco / UK",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Queso Curado Penetrante", "Skunk Lácteo", "Tierra Especiada"],
    effects: ["Relax Placentero", "Euforia Sensorial", "Sensación Antiestrés"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Selección bilbaína de la madre inglesa Cheese de 1998. Desprende una peste inconfundible a queso viejo curado y Skunk especiado con flores de resina dorada de efecto corporal muy agradable.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-amnesia-bilbo",
    image: "img/genehtik-amnesia-bilbo-bud.webp",
    name: "Amnesia Bilbo",
    aka: "Selección Amnesia Haze",
    bank: "Genehtik Seeds",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 850,
    floweringDays: 70, rating: 4.9, reviewsCount: 490,
    genetics: "Selección Amnesia Haze",
    origin: "País Vasco (España)",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Cítrico Regaliz", "Incienso Limón", "Madera Pino"],
    effects: ["Potencia Cerebral Extrema", "Desconexión Total", "Euforia"],
    activities: ["creativity", "social", "nature_walk"],
    description: "El clon mítico de Amnesia preservado por Genehtik. Sativa de enorme vigor con flores gruesas resinosas cargadas de aroma cítrico con fondo de regaliz. Provoca un subidón eufórico e imponente.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-northern-lights-x",
    image: "img/genehtik-northern-lights-x-bud.webp",
    name: "Northern Lights X",
    aka: "Northern Lights Selección Élite",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 20, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 52, rating: 4.8, reviewsCount: 380,
    genetics: "Northern Lights Selección Élite",
    origin: "País Vasco / Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, humulene: 20 },
    flavors: ["Roble Terroso", "Miel Dulce", "Hachís Especiado"],
    effects: ["Sedación Corporal Profunda", "Relax Muscular", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "Selección propia de la famosa Northern Lights. Planta de desarrollo homogéneo, baja altura y altísima producción de cogollos duros como piedras cubiertos de azúcar de resina.",
    visualColor: "linear-gradient(135deg, #1E1B4B 0%, #312E81 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-blubonik",
    image: "img/genehtik-blubonik-bud.webp",
    name: "Blubonik",
    aka: "Kootenay Blueberry x Blueberry",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 21, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.8, reviewsCount: 360,
    genetics: "Kootenay Blueberry x Blueberry Selección",
    origin: "Canadá / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, linalool: 20 },
    flavors: ["Arándanos Frescos", "Arándano Azucarado", "Fruta Silvestre"],
    effects: ["Relajación Físico-Mental", "Sensación Antiestrés", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Cruce canadiense entre dos selecciones de la clásica Blueberry. Produce cogollos ultra resinosos de tonos azulados y púrpuras con un penetrante e irresistible perfume a confitura de arándanos.",
    visualColor: "linear-gradient(135deg, #2563EB 0%, #1E3A8A 100%)",
    bgPattern: "radial-gradient(circle, rgba(37,99,235,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-og-lemon-bilbo",
    image: "img/genehtik-og-lemon-bilbo-bud.webp",
    name: "OG Lemon Bilbo",
    aka: "OG Kush Lemon Cut x Selección Bilbo",
    bank: "Genehtik Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 62, rating: 4.9, reviewsCount: 430,
    genetics: "OG Kush Lemon Cut x Selección Bilbo",
    origin: "USA / España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, caryophyllene: 30, myrcene: 20 },
    flavors: ["Limón Ácido Combustible", "Tierra Kush", "Musgo Pino"],
    effects: ["Subidón Potente Mixto", "Euforia Mental", "Relajación Corporal"],
    activities: ["social", "creativity", "relax_sleep"],
    description: "Híbrido de OG Kush corte cítrico seleccionado con el clon Bilbo. Destaca por su penetrante aroma a combustible de avión con limón exprimido y un potente subidón cerebral eufórico seguido de calma muscular.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #A16207 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "genehtik-santa-bilbo",
    image: "img/genehtik-santa-bilbo-bud.webp",
    name: "Santa Bilbo",
    aka: "Brasil Amazonia x Selección Bilbo",
    bank: "Genehtik Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 60, rating: 4.7, reviewsCount: 330,
    genetics: "Brasil Amazonia x Selección Bilbo",
    origin: "Brasil / España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Incienso Tropical", "Fruta Silvestre", "Madera Fresca"],
    effects: ["Energía Eufórica", "Subidón Cerebral Limpio", "Claridad"],
    activities: ["creativity", "social", "workout"],
    description: "Variedad creada a partir de una sativa nativa de la cuenca amazónica brasileña cruzada con el clon Bilbo para acortar su floración a solo 60 días. Sabor exótico a incienso y fruta con efecto muy activo.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-fruit-punch",
    image: "img/heavyweight-fruit-punch-bud.webp",
    name: "Fruit Punch",
    aka: "Skunk #1 x Haze x Northern Lights",
    bank: "Heavyweight Seeds",
    species: "Sativa",
    thc: 22, cbd: 1.2,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 55, rating: 5.0, reviewsCount: 820,
    genetics: "Skunk #1 x Haze x Northern Lights",
    origin: "UK / España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, myrcene: 20 },
    flavors: ["Ponche de Frutas Tropicales", "Mango Dulce", "Cítrico Limón"],
    effects: ["Euforia Cerebral Social", "Energía Diurna", "Bienestar Alegré"],
    activities: ["social", "creativity", "nature_walk"],
    description: "El mayor súper éxito de Heavyweight Seeds. Combina la rapidez de Skunk #1, la resina de Northern Lights y la potencia eufórica de Haze. Sabor embriagador a ponche de frutas tropicales dulce con producción gigantesca.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-green-ninja",
    image: "img/heavyweight-green-ninja-bud.webp",
    name: "Green Ninja",
    aka: "Northern Lights x Afgana Pura",
    bank: "Heavyweight Seeds",
    species: "Indica",
    thc: 22, cbd: 1.0,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 50, rating: 4.9, reviewsCount: 610,
    genetics: "Northern Lights x Afgana Pura",
    origin: "UK / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Especias Terrosas", "Pino Silvestre", "Fruta Dulce"],
    effects: ["Subidón Silencioso Demoledor", "Relajación Corporal", "Paz Mental"],
    activities: ["relax_sleep", "meditation"],
    description: "Diseñada para cultivos discretos y rápidos. Crece de manera sigilosa como un ninja pero ataca con una potencia devastadora en solo 50 días de floración con aroma frutal especiado.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-budzilla",
    image: "img/heavyweight-budzilla-bud.webp",
    name: "Budzilla",
    aka: "G13 x Skunk #1",
    bank: "Heavyweight Seeds",
    species: "Híbrida",
    thc: 22, cbd: 1.1,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 56, rating: 4.8, reviewsCount: 490,
    genetics: "G13 x Skunk #1",
    origin: "UK / USA",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Skunk Penetrante", "Madera Roble", "Fruta Madura"],
    effects: ["Potencia Monstruosa", "Euforia Equilibrada", "Relajación Muscular"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "Un verdadero monstruo de producción e intensidad. Cruce legendario de la mítica G13 gubernamental con Skunk #1. Produce colas principales colosales cargadas de resina apestosa a Skunk dulce.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-money-bush",
    image: "img/heavyweight-money-bush-bud.webp",
    name: "Money Bush",
    aka: "Afghani x Critical Mass",
    bank: "Heavyweight Seeds",
    species: "Indica",
    thc: 21, cbd: 1.0,
    yieldIndoor: 600, yieldOutdoor: 900,
    floweringDays: 52, rating: 4.9, reviewsCount: 540,
    genetics: "Afghani x Critical Mass",
    origin: "UK / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, humulene: 20 },
    flavors: ["Hachís Dulce", "Tierra Húmeda", "Cítrico Suave"],
    effects: ["Relajación Física Intensa", "Sensación De Bienestar", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Apodada 'El arbusto del dinero' por su rentabilidad comercial insuperable. Floración rapidísima de 50-55 días con rendimiento gigantesco de cogollos impregnados en aroma dulce de hachís afgano.",
    visualColor: "linear-gradient(135deg, #059669 0%, #064E3B 100%)",
    bgPattern: "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-goldmine",
    image: "img/heavyweight-goldmine-bud.webp?v=2026_custom_hd",
    name: "Goldmine",
    aka: "Mazar x AK-47",
    bank: "Heavyweight Seeds",
    species: "Indica",
    thc: 22, cbd: 1.0,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 60, rating: 4.8, reviewsCount: 460,
    genetics: "Mazar x AK-47",
    origin: "UK",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, limonene: 32, caryophyllene: 20 },
    flavors: ["Baya Dulce", "Miel Silvestre", "Skunk Exótico"],
    effects: ["Narcótico Corporal Placentero", "Tranquilidad", "Descanso Total"],
    activities: ["relax_sleep", "meditation"],
    description: "Una auténtica mina de oro en cuanto a sabor y presencia. Cruce de Mazar afgana con AK-47. Presenta cogollos relucientes con aroma a miel silvestre y bayas oscuras de efecto sedante profundo.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-monster-profit",
    image: "img/heavyweight-monster-profit-bud.webp",
    name: "Monster Profit",
    aka: "Amnesia Haze x Dream Machine",
    bank: "Heavyweight Seeds",
    species: "Sativa",
    thc: 22, cbd: 1.2,
    yieldIndoor: 800, yieldOutdoor: 1200,
    floweringDays: 60, rating: 4.9, reviewsCount: 510,
    genetics: "Amnesia Haze x Dream Machine",
    origin: "UK",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Cítrico Inciensado", "Dulce Suave", "Pino Fresco"],
    effects: ["Euforia Cerebral Lúcida", "Sensación De Alegría", "Energía"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Récord absoluto de producción en interior alcanzando hasta 800 g/m². Cruce de Amnesia Haze con Dream Machine que produce ramas abarrotadas de flores resinosas cítricas de efecto muy eufórico.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-superb-og",
    image: "img/heavyweight-superb-og-bud.webp",
    name: "Superb OG",
    aka: "Hindu Kush x OG Kush",
    bank: "Heavyweight Seeds",
    species: "Indica",
    thc: 24, cbd: 1.0,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 56, rating: 4.9, reviewsCount: 430,
    genetics: "Hindu Kush x OG Kush",
    origin: "USA / UK",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Combustible Cítrico", "Tierra Kush", "Pino Especiado"],
    effects: ["Relax Físico Inmediato", "Bienestar Cerebral", "Calma"],
    activities: ["relax_sleep", "gaming", "meditation"],
    description: "Refinamiento extremo de la línea Kush. Cruce directo de la ancestral Hindu Kush con una selección estelar de OG Kush. Perfume penetrante a carburante y limón con un efecto relajante soberbio.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-lemon-cake",
    image: "img/heavyweight-lemon-cake-bud.webp",
    name: "Lemon Cake",
    aka: "Lemon Skunk x Cheese",
    bank: "Heavyweight Seeds",
    species: "Sativa",
    thc: 23, cbd: 1.0,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 65, rating: 4.9, reviewsCount: 470,
    genetics: "Lemon Skunk x Cheese",
    origin: "UK",
    dominantTerpene: "limonene",
    terpenes: { limonene: 52, caryophyllene: 28, myrcene: 20 },
    flavors: ["Pastel de Limón Dulce", "Queso Cítrico", "Vainilla Suave"],
    effects: ["Euforia Radiante", "Energía Diurna", "Pensamiento Positivo"],
    activities: ["creativity", "social", "workout"],
    description: "Una delicia organoléptica inolvidable. Híbrido entre Lemon Skunk y la sabrosa Cheese. Aroma intenso a tarta de limón horneada con matices de queso dulce y un subidón eufórico radiante.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-dream-machine",
    image: "img/heavyweight-dream-machine-bud.webp",
    name: "Dream Machine",
    aka: "Afghan x Indian x Brazilian Landrace",
    bank: "Heavyweight Seeds",
    species: "Híbrida",
    thc: 23, cbd: 1.0,
    yieldIndoor: 600, yieldOutdoor: 850,
    floweringDays: 60, rating: 4.8, reviewsCount: 420,
    genetics: "Afghan x Indian x Brazilian Landrace",
    origin: "UK",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, terpinolene: 35, caryophyllene: 20 },
    flavors: ["Fruta Azucarada", "Especias Orientales", "Dulce Suave"],
    effects: ["Efecto Soñador Placentero", "Relajación Corporal", "Serenidad"],
    activities: ["relax_sleep", "meditation", "social"],
    description: "Apodada 'La máquina de los sueños'. Triple cruce entre genéticas landrace de Afganistán, India y Brasil. Cogollos bañados en resina espesa con sabor a frutas azucaradas y especias orientales.",
    visualColor: "linear-gradient(135deg, #6366F1 0%, #3730A3 100%)",
    bgPattern: "radial-gradient(circle, rgba(99,102,241,0.2) 0%, transparent 70%)"
  },
  {
id: "heavyweight-strawberry-cake",
    image: "img/heavyweight-strawberry-cake-bud.webp",
    name: "Strawberry Cake",
    aka: "Chronic x White Widow x Cheese",
    bank: "Heavyweight Seeds",
    species: "Indica",
    thc: 22, cbd: 1.3,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 55, rating: 4.8, reviewsCount: 390,
    genetics: "Chronic x White Widow x Cheese",
    origin: "UK",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Tarta de Fresa", "Crema Láctea", "Skunk Dulce"],
    effects: ["Relajación Placentera", "Bienestar Físico", "Calma Mental"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Anteriormente conocida como Strawberry Cheesecake. Fantástica combinación de Chronic, White Widow y Cheese. Sabor delicioso a pastel de fresa con crema y un efecto relajante perfecto para desconectar.",
    visualColor: "linear-gradient(135deg, #F43F5E 0%, #BE123C 100%)",
    bgPattern: "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-taskenti",
    image: "img/cannabiogen-taskenti-bud.webp",
    name: "Taskenti",
    aka: "Uzbekistán Landrace x NL#1",
    bank: "Cannabiogen",
    species: "Indica",
    thc: 20, cbd: 0.5,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 56, rating: 5.0, reviewsCount: 890,
    genetics: "Uzbekistán Landrace x NL#1",
    origin: "Uzbekistán / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, humulene: 20 },
    flavors: ["Hachís Afgano", "Menta Maderosa", "Tierra Especiada"],
    effects: ["Efecto Narcótico Demoledor", "Relajación Corporal", "Paz Total"],
    activities: ["relax_sleep", "meditation"],
    description: "Cepa mítica de culto en España. Híbrido desarrollado principalmente a partir de la landrace de Uzbekistán. Extraordinaria producción de resina de olor espeso a hachís afgano puro con un potente efecto sedante.",
    visualColor: "linear-gradient(135deg, #1E1B4B 0%, #312E81 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-peyote-purple",
    image: "img/cannabiogen-peyote-purple-bud.webp",
    name: "Peyote Purple",
    aka: "Selección Bubba Kush (Corte Morado)",
    bank: "Cannabiogen",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 400, yieldOutdoor: 500,
    floweringDays: 60, rating: 5.0, reviewsCount: 920,
    genetics: "Selección Bubba Kush (Corte Morado)",
    origin: "USA / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, linalool: 20 },
    flavors: ["Café Vainilla", "Champaña Dulce", "Tierra Kush"],
    effects: ["Relajación Meditativa", "Bienestar Físico", "Sueño Placentero"],
    activities: ["relax_sleep", "meditation"],
    description: "Variedad de culto famosa en todo el mundo por su belleza sin igual. Selección del fenotipo púrpura negro de Bubba Kush. Cogollos oscuros casi negros cubiertos por una alfombra blanca de resina resplandeciente.",
    visualColor: "linear-gradient(135deg, #4C1D95 0%, #1E1B4B 100%)",
    bgPattern: "radial-gradient(circle, rgba(76,29,149,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-sandstorm",
    image: "img/cannabiogen-sandstorm-bud.webp",
    name: "Sandstorm",
    aka: "Chitral Kush x Morocco Landrace",
    bank: "Cannabiogen",
    species: "Indica",
    thc: 18, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 56, rating: 4.9, reviewsCount: 620,
    genetics: "Chitral Kush x Morocco Landrace",
    origin: "Pakistán / Marruecos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Hachís Marroquí", "Moras Dulces", "Tierra Especiada"],
    effects: ["Relajación Corporal Suave", "Bienestar Antiestrés", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Un homenaje a la cultura tradicional del extracción de hachís. Cruce de dos de las mejores índicas puras del viejo mundo: Chitral paquistaní y una madre marroquí. Cogollos compactos y purpúreos.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-nepal-jam",
    image: "img/cannabiogen-nepal-jam-bud.webp",
    name: "Nepal Jam",
    aka: "Nepal Sativa x Jamaica Blue Mountain",
    bank: "Cannabiogen",
    species: "Sativa",
    thc: 18, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.9, reviewsCount: 570,
    genetics: "Nepal Highland Sativa x Jamaica Blue Mountain",
    origin: "Nepal / Jamaica",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Caramelo de Limón", "Incienso Suave", "Fruta Madura"],
    effects: ["Subidón Alegre Diáfano", "Claridad Mental", "Energía Diurna"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Híbrido sativa de adaptación perfecta para climas fríos y húmedos. Cruce de sativa nepalí de altura con Jamaica Blue Mountain. Efecto cerebral limpio, festivo y muy resistente al moho.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-caribe",
    image: "img/cannabiogen-caribe-bud.webp",
    name: "Caribe",
    aka: "Jamaica Blue Mountain x NL5 Haze",
    bank: "Cannabiogen",
    species: "Sativa",
    thc: 20, cbd: 0.2,
    yieldIndoor: 450, yieldOutdoor: 700,
    floweringDays: 70, rating: 4.8, reviewsCount: 480,
    genetics: "Jamaica Blue Mountain x (NL5 x Haze)",
    origin: "Jamaica / Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Mango Tropical", "Incienso Haze", "Limón Dulce"],
    effects: ["Euforia Cerebral Radiante", "Energía Tropical", "Creatividad"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Sativa exótica del Caribe cruzada con el vigor de NL5 Haze. Desarrolla un inconfundible perfil terpénico frutal tropical con un potente subidón cerebral estimulante.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-jamaica-blue-mountain",
    image: "img/cannabiogen-jamaica-blue-mountain-bud.webp",
    name: "Jamaica Blue Mountain",
    aka: "Jamaica Blue Mountain Landrace",
    bank: "Cannabiogen",
    species: "Sativa",
    thc: 19, cbd: 0.2,
    yieldIndoor: 400, yieldOutdoor: 650,
    floweringDays: 77, rating: 4.8, reviewsCount: 410,
    genetics: "Jamaica Blue Mountain Landrace",
    origin: "Jamaica",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 52, limonene: 28, pinene: 20 },
    flavors: ["Café Verde", "Hierba Fresca", "Especias Tropicales"],
    effects: ["Euforia Caribeña", "Sensación Antiestrés", "Energía Diurna"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Landrace pura procedente de las míticas montañas azules de Jamaica. Estabilizada tras varias generaciones por Cannabiogen. Sabor fresco a especias tropicales con un subidón cerebral diáfano.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-leshaze",
    image: "img/cannabiogen-leshaze-bud.webp",
    name: "Leshaze",
    aka: "Lesotho Landrace x Skunk Haze",
    bank: "Cannabiogen",
    species: "Sativa",
    thc: 19, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.7, reviewsCount: 390,
    genetics: "Lesotho Landrace x Skunk #1 Haze",
    origin: "Lesoto (África) / Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, pinene: 20 },
    flavors: ["Pino Especiado", "Limón Dulce", "Tierra Fresca"],
    effects: ["Euforia Equilibrada", "Bienestar Activo", "Claridad Mental"],
    activities: ["social", "nature_walk", "workout"],
    description: "Excelente cruce entre una sativa de altura de Lesoto (África del Sur) y un clásico híbrido Skunk Haze. Crecimiento elegante y floración rápida de aroma dulzón e inciensado.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-panama-dc",
    image: "img/cannabiogen-panama-dc-bud.webp",
    name: "Panama DC",
    aka: "Panama Goddess x Deep Chunk",
    bank: "Cannabiogen",
    species: "Híbrida",
    thc: 21, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.9, reviewsCount: 460,
    genetics: "Panama Goddess x Deep Chunk",
    origin: "Panamá / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Limón Dulce", "Hachís Afgano", "Incienso Limpio"],
    effects: ["Subidón Potente Mixto", "Relax Físico", "Sensación De Bienestar"],
    activities: ["relax_sleep", "social", "meditation"],
    description: "Un cruce magistral entre la sativa pura Panama Diosa y la pura afgana Deep Chunk. Combina la exuberante floración roja y limonada de Panamá con la resina hiperdensa y narcótica de la afgana.",
    visualColor: "linear-gradient(135deg, #EF4444 0%, #B91C1C 100%)",
    bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-mangobiche-kush",
    image: "img/cannabiogen-mangobiche-kush-bud.webp",
    name: "Mangobiche Kush",
    aka: "Colombia Mangobiche x Peyote Purple",
    bank: "Cannabiogen",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 475, yieldOutdoor: 700,
    floweringDays: 70, rating: 4.8, reviewsCount: 350,
    genetics: "Colombia Mangobiche Landrace x Peyote Purple",
    origin: "Colombia / USA",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Mango Verde Ácido", "Café Dulce", "Especias Tropicales"],
    effects: ["Estimulación Cerebral Intensa", "Relax Físico Suave", "Euforia"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Híbrido exótico que combina la mítica landrace colombiana Mangobiche con el colorido y resina de Peyote Purple. Flores moradas aromáticas con intenso sabor a mango tropical y café.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "cannabiogen-hash-fruit",
    image: "img/cannabiogen-hash-fruit-bud.webp",
    name: "Hash Fruit",
    aka: "Sandstorm x Peyote Purple",
    bank: "Cannabiogen",
    species: "Indica",
    thc: 20, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 55, rating: 4.8, reviewsCount: 380,
    genetics: "Sandstorm x Peyote Purple",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, pinene: 20 },
    flavors: ["Hachís Dulce", "Uvas Moradas", "Tierra Roble"],
    effects: ["Relajación Corporal Placentera", "Paz Mental", "Sueño"],
    activities: ["relax_sleep", "meditation"],
    description: "Cruce puro de dos grandes selecciones de resina de Cannabiogen: Sandstorm y Peyote Purple. Planta de floración corta con cogollos violetas empapados de aceite de resina y aroma frutal a hachís.",
    visualColor: "linear-gradient(135deg, #6B21A8 0%, #3B0764 100%)",
    bgPattern: "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-jack-herer",
    image: "img/sensi-jack-herer-bud.webp",
    name: "Jack Herer",
    aka: "Haze x NL#5 x Shiva Skunk",
    bank: "Sensi Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 70, rating: 5.0, reviewsCount: 1250,
    genetics: "Haze x Northern Lights #5 x Shiva Skunk",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, caryophyllene: 20 },
    flavors: ["Pino Especiado", "Pimiento Dulce", "Cítrico Haze"],
    effects: ["Claridad Mental Lúcida", "Subidón Eufórico", "Energía Creativa"],
    activities: ["creativity", "social", "nature_walk"],
    description: "El Rolls Royce del cannabis mundial. Cepa oficial de prescripción médica en los Países Bajos. Equilibrio magistral entre el subidón cerebral de las sativas y la copiosa producción de resina de las índicas.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-super-skunk",
    image: "img/sensi-super-skunk-bud.webp",
    name: "Super Skunk",
    aka: "Skunk #1 x Afgana Pura",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 650,
    floweringDays: 50, rating: 5.0, reviewsCount: 1100,
    genetics: "Skunk #1 x Afgana Pura",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, limonene: 20 },
    flavors: ["Skunk Penetrante", "Fruta Dulce", "Tierra Húmeda"],
    effects: ["Potente Relax Corporal", "Sensación Antiestrés", "Euforia"],
    activities: ["relax_sleep", "social", "meditation"],
    description: "Ganadora de innumerables Cannabis Cups. Reformulación potenciada de Skunk #1 enriquecida con genéticas afganas pura sangre. Floración récord, vigor sobrenatural y perfume penetrante inolvidable.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-black-domina",
    image: "img/sensi-black-domina-bud.webp",
    name: "Black Domina",
    aka: "NL x Ortega x Hash Plant x Afghani SA",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 21, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 50, rating: 5.0, reviewsCount: 980,
    genetics: "Northern Lights x Ortega x Hash Plant x Afghani SA",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, caryophyllene: 28, humulene: 20 },
    flavors: ["Pimienta Negra", "Hachís Afgano", "Moras de Zarza"],
    effects: ["Efecto Narcótico Total", "Sedación Corporal", "Descanso Profundo"],
    activities: ["relax_sleep", "meditation"],
    description: "La reina negra de las índicas. Híbrido cuádruple de 4 de las mejores variedades afganas del planeta. Hojas verde oscuro casi negras con cálices cargados de resina densa de efecto puramente anestésico.",
    visualColor: "linear-gradient(135deg, #111827 0%, #1F2937 100%)",
    bgPattern: "radial-gradient(circle, rgba(31,41,55,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-northern-lights",
    image: "img/sensi-northern-lights-bud.webp",
    name: "Northern Lights",
    aka: "NL #2 x NL #5 Landrace Afgana",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 20, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 50, rating: 5.0, reviewsCount: 1300,
    genetics: "NL #2 x NL #5 Landrace Afgana",
    origin: "USA / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Miel Dulce", "Pino Terroso", "Especias Afganas"],
    effects: ["Calma Muscular Profunda", "Paz Interior", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "La cepa índica más influyente de la historia del cannabis. Base genética de la inmensa mayoría de híbridos modernos. Crecimiento compacto, gran rendimiento de cogollos duros y efecto físicamente relajante.",
    visualColor: "linear-gradient(135deg, #1E1B4B 0%, #312E81 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-hindu-kush",
    image: "img/sensi-hindu-kush-bud.webp",
    name: "Hindu Kush",
    aka: "Hindu Kush Mountain Landrace",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 19, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 48, rating: 4.9, reviewsCount: 750,
    genetics: "Hindu Kush Mountain Landrace",
    origin: "Afganistán / Pakistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, humulene: 20 },
    flavors: ["Hachís Tradicional", "Especias Dulces", "Madera de Cedro"],
    effects: ["Serenidad Corporal", "Relajación Meditativa", "Bienestar"],
    activities: ["relax_sleep", "meditation"],
    description: "Cepa pura landrace traída directamente de las cordilleras del Hindu Kush. Clásico ancestral preservado por Sensi Seeds. Flores compactas briznadas de tricomas plateados con aroma a hachís tradicional.",
    visualColor: "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
    bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-skunk-1",
    image: "img/sensi-skunk-1-bud.webp",
    name: "Skunk #1",
    aka: "Sativa Landrace x Afghani",
    bank: "Sensi Seeds",
    species: "Híbrida",
    thc: 19, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 50, rating: 5.0, reviewsCount: 1400,
    genetics: "75% Sativa (Central America/Thailand) x 25% Afghani",
    origin: "USA / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, limonene: 35, caryophyllene: 20 },
    flavors: ["Skunk Clásico Dulce", "Tierra Húmeda", "Cítrico Suave"],
    effects: ["Euforia Cerebral Rápida", "Relajación Físico-Mental", "Alegría"],
    activities: ["social", "relax_sleep", "creativity"],
    description: "La variedad que cambió la faz de la cultura del cannabis para siempre. El estándar global de uniformidad, estabilidad y rendimiento. Potente subidón eufórico combinado con un relax corporal reconfortante.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #4D7C0F 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-sensi-amnesia",
    image: "img/sensi-sensi-amnesia-bud.webp",
    name: "Sensi Amnesia",
    aka: "Hawaiian x Jamaica x Jamaican Pearl",
    bank: "Sensi Seeds",
    species: "Sativa",
    thc: 24, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 70, rating: 4.9, reviewsCount: 520,
    genetics: "Hawaiian Indica x Jamaica Blue Mountain x Jamaican Pearl",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Cítrico Tropical", "Incienso Limón", "Exótico Frutal"],
    effects: ["Euforia Cerebral Desbordante", "Energía Diurna", "Pensamiento Creativo"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Variedad sativo-dominante que renueva la mítica línea Amnesia. Sabor cítrico tropical punzante con matices de incienso y un subidón eufórico cerebral de larga duración que limpia el estrés.",
    visualColor: "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-hash-plant",
    image: "img/sensi-hash-plant-bud.webp",
    name: "Hash Plant",
    aka: "Original Hash Plant x Northern Lights #1",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 18, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 45, rating: 4.8, reviewsCount: 610,
    genetics: "Original Hash Plant x Northern Lights #1",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, caryophyllene: 28, humulene: 20 },
    flavors: ["Hachís Afgano Intenso", "Especias Picantes", "Tierra Roble"],
    effects: ["Efecto Anestésico Rápido", "Relajación Corporal", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Una de las variedades de floración más ultra rápidas del catálogo (40-45 días). Desarrollada específicamente para la producción de hachís de máxima pureza. Cogollos compactos como piedras empapados en resina.",
    visualColor: "linear-gradient(135deg, #451A03 0%, #170701 100%)",
    bgPattern: "radial-gradient(circle, rgba(69,26,3,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-early-skunk",
    image: "img/sensi-early-skunk-bud.webp",
    name: "Early Skunk",
    aka: "Skunk #1 x Early Pearl",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 18, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 900,
    floweringDays: 50, rating: 4.9, reviewsCount: 670,
    genetics: "Skunk #1 x Early Pearl",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Skunk Dulce", "Especias Rosas", "Tierra Fresca"],
    effects: ["Euforia Suave", "Relajación Físico-Mental", "Sensación Antiestrés"],
    activities: ["social", "nature_walk", "relax_sleep"],
    description: "La mejor solución para cultivos de exterior en zonas frías o lluviosas. Cruce entre Skunk #1 y Early Pearl. Altísima resistencia a hongos y floración super temprana con cogollos voluminosos resinosos.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "sensi-sensi-skunk",
    image: "img/sensi-sensi-skunk-bud.webp",
    name: "Sensi Skunk",
    aka: "Skunk #1 x Selección Cítrica",
    bank: "Sensi Seeds",
    species: "Indica",
    thc: 18, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 48, rating: 4.8, reviewsCount: 590,
    genetics: "Skunk #1 x Selección Cítrica Secreta",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "limonene",
    terpenes: { limonene: 48, myrcene: 32, caryophyllene: 20 },
    flavors: ["Cítrico Dulce", "Naranja Fresca", "Skunk Suave"],
    effects: ["Relax Placentero", "Euforia Alegre", "Desconexión"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "Variación fresca y súper cítrica del patrón clásico Skunk. Muy fácil de cultivar y sumamente agradecida. Destaca por su delicioso sabor a naranja dulces y cítricos frescos con un potente efecto eufórico-relajante.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-super-lemon-haze",
    image: "img/ghs-super-lemon-haze-bud.webp",
    name: "Super Lemon Haze",
    aka: "Lemon Skunk x Super Silver Haze",
    bank: "Green House Seed Co.",
    species: "Sativa",
    thc: 25, cbd: 0.3,
    yieldIndoor: 800, yieldOutdoor: 1000,
    floweringDays: 70, rating: 5.0, reviewsCount: 1650,
    genetics: "Lemon Skunk x Super Silver Haze",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "limonene",
    terpenes: { limonene: 52, terpinolene: 28, caryophyllene: 20 },
    flavors: ["Limón Ácido", "Pino Inciensado", "Pimiento Dulce"],
    effects: ["Euforia Cerebral Intensa", "Energía Psicodélica", "Creatividad Radiante"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Bicampeona consecutiva de la High Times Cannabis Cup. Ícono mundial del cannabis. Cruce de Lemon Skunk con Super Silver Haze. Sabor ácido a limonada recién exprimida con incienso y un subidón eufórico inolvidable.",
    visualColor: "linear-gradient(135deg, #FACC15 0%, #CA8A04 100%)",
    bgPattern: "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-super-silver-haze",
    image: "img/ghs-super-silver-haze-bud.webp",
    name: "Super Silver Haze",
    aka: "Skunk #1 x NL #5 x Haze",
    bank: "Green House Seed Co.",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 800, yieldOutdoor: 1500,
    floweringDays: 70, rating: 5.0, reviewsCount: 1420,
    genetics: "Skunk #1 x Northern Lights #5 x Haze",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, caryophyllene: 20 },
    flavors: ["Incienso Ámsterdam", "Pino Especiado", "Tierra Dulce"],
    effects: ["Euforia Psicodélica Duradera", "Claridad Mística", "Energía Creativa"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Tricampeona consecutiva de la Cannabis Cup (1997, 1998, 1999). Legendario híbrido de Skunk, Northern Lights y Haze. Flores gigantescas en forma de cola cubiertas de una alfombra plateada de resina.",
    visualColor: "linear-gradient(135deg, #94A3B8 0%, #475569 100%)",
    bgPattern: "radial-gradient(circle, rgba(148,163,184,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-white-widow",
    image: "img/ghs-white-widow-bud.webp",
    name: "White Widow",
    aka: "South Indian Sativa x Brazil Landrace",
    bank: "Green House Seed Co.",
    species: "Indica",
    thc: 21, cbd: 0.4,
    yieldIndoor: 800, yieldOutdoor: 900,
    floweringDays: 56, rating: 5.0, reviewsCount: 1580,
    genetics: "Sativa de la India del Sur x Brasil Landrace",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, pinene: 20 },
    flavors: ["Pino Resinoso", "Tierra Húmeda", "Cítrico Especiado"],
    effects: ["Subidón Eufórico Inicial", "Relajación Corporal Profunda", "Bienestar"],
    activities: ["social", "relax_sleep", "meditation"],
    description: "Ganadora de la Cannabis Cup 1995 y creadora de la famosa familia 'White'. Mítica variedad de Green House cubierta por una capa blanca espesa de resina brillante con efecto narcótico duradero.",
    visualColor: "linear-gradient(135deg, #CBD5E1 0%, #64748B 100%)",
    bgPattern: "radial-gradient(circle, rgba(203,213,225,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-great-white-shark",
    image: "img/ghs-great-white-shark-bud.webp",
    name: "Great White Shark",
    aka: "Super Skunk x Brazilian x South Indian",
    bank: "Green House Seed Co.",
    species: "Indica",
    thc: 20, cbd: 0.5,
    yieldIndoor: 800, yieldOutdoor: 1000,
    floweringDays: 60, rating: 4.9, reviewsCount: 780,
    genetics: "Super Skunk x Brazilian x South Indian",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, humulene: 20 },
    flavors: ["Madera Dulce", "Tierra Skunk", "Frutas Ácidas"],
    effects: ["Golpe Anestésico Inmediato", "Relajación Corporal", "Paz Total"],
    activities: ["relax_sleep", "meditation"],
    description: "Conocida también como Peacemaker. Ganadora de múltiples premios por su aplastante potencia índica. Plantas ramificadas con cogollos densos y muy blancos que proporcionan un potente relax muscular.",
    visualColor: "linear-gradient(135deg, #0EA5E9 0%, #0369A1 100%)",
    bgPattern: "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-hawaiian-snow",
    image: "img/ghs-hawaiian-snow-bud.webp",
    name: "Hawaiian Snow",
    aka: "Hawaiian Sativa x Neville's Haze",
    bank: "Green House Seed Co.",
    species: "Sativa",
    thc: 23, cbd: 0.2,
    yieldIndoor: 700, yieldOutdoor: 1200,
    floweringDays: 84, rating: 4.9, reviewsCount: 650,
    genetics: "Hawaiian Sativa x Neville's Haze",
    origin: "Hawái / Ámsterdam",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 52, limonene: 28, caryophyllene: 20 },
    flavors: ["Cítrico Tropical", "Incienso Haze", "Eucalipto Dulce"],
    effects: ["Euforia Social Radiante", "Energía Estimulante", "Pensamiento Creativo"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Ganadora de la HTCC 2003. Legendaria sativa de alta producción con aroma floral y tropical briznado de incienso. Efecto cerebral elevado, social y extremadamente estimulante.",
    visualColor: "linear-gradient(135deg, #38BDF8 0%, #0284C7 100%)",
    bgPattern: "radial-gradient(circle, rgba(56,189,248,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-francos-lemon-cheese",
    image: "img/ghs-francos-lemon-cheese-bud.webp",
    name: "Franco's Lemon Cheese",
    aka: "Super Lemon Haze x Exodus Cheese",
    bank: "Green House Seed Co.",
    species: "Sativa",
    thc: 23, cbd: 0.3,
    yieldIndoor: 750, yieldOutdoor: 1000,
    floweringDays: 65, rating: 5.0, reviewsCount: 1120,
    genetics: "Super Lemon Haze x Exodus Cheese",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, caryophyllene: 30, myrcene: 20 },
    flavors: ["Queso Cítrico", "Limón Dulce", "Skunk Penetrante"],
    effects: ["Euforia Energética", "Relajación Social", "Alegría Vibrante"],
    activities: ["social", "creativity", "party"],
    description: "Homenaje al añorado breeder Franco Loja (Strain Hunters). Extraordinario cruce entre sus dos cepas favoritas: Super Lemon Haze y Exodus Cheese. Sabor curado a queso cítrico de impacto alegre inolvidable.",
    visualColor: "linear-gradient(135deg, #EAB308 0%, #A16207 100%)",
    bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-exodus-cheese",
    image: "img/ghs-exodus-cheese-bud.webp",
    name: "Exodus Cheese",
    aka: "Selección Clón Original UK Cheese",
    bank: "Green House Seed Co.",
    species: "Indica",
    thc: 19, cbd: 0.3,
    yieldIndoor: 800, yieldOutdoor: 800,
    floweringDays: 56, rating: 4.9, reviewsCount: 940,
    genetics: "Selección Clón Original UK Cheese",
    origin: "Reino Unido / Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Queso Curado Penetrante", "Skunk Añejo", "Tierra Especiada"],
    effects: ["Subidón Eufórico Rápido", "Relax Físico Placentero", "Sensación Antiestrés"],
    activities: ["social", "relax_sleep", "dining"],
    description: "El clon original Cheese del Reino Unido popularizado por Green House. Caracterizado por su inconfundible y potente perfume a queso curado viejo y su equilibrado efecto físico y mental.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-bubba-kush",
    image: "img/ghs-bubba-kush-bud.webp",
    name: "Bubba Kush",
    aka: "Bubble Gum x OG Kush",
    bank: "Green House Seed Co.",
    species: "Indica",
    thc: 20, cbd: 0.4,
    yieldIndoor: 800, yieldOutdoor: 1000,
    floweringDays: 60, rating: 4.8, reviewsCount: 810,
    genetics: "Bubble Gum x OG Kush",
    origin: "USA / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Café Tostado", "Cacao Amargo", "Tierra Kush"],
    effects: ["Relajación Muscular Intensa", "Paz Mental", "Sueño Profundo"],
    activities: ["relax_sleep", "meditation"],
    description: "La clásica índica californiana seleccionada por Green House. Planta achaparrada con hojas anchas y flores cargadas de terpenos a café, chocolate y combustible. Efecto corporal sedante.",
    visualColor: "linear-gradient(135deg, #374151 0%, #111827 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-kalashnikova",
    image: "img/ghs-kalashnikova-bud.webp",
    name: "Kalashnikova",
    aka: "AK-47 x White Widow",
    bank: "Green House Seed Co.",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 750, yieldOutdoor: 1000,
    floweringDays: 56, rating: 4.8, reviewsCount: 680,
    genetics: "AK-47 x White Widow",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Pino Especiado", "Skunk Dulce", "Tierra Roble"],
    effects: ["Golpe Narcótico Potente", "Relajación Corporal", "Descanso"],
    activities: ["relax_sleep", "meditation"],
    description: "Potentísimo cruce de dos leyendas incontestables del cannabis: AK-47 y White Widow. Gran producción de cogollos duros como rocas briznados de resina con una floración rápida e intensa.",
    visualColor: "linear-gradient(135deg, #15803D 0%, #166534 100%)",
    bgPattern: "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)"
  },
  {
id: "ghs-kings-juice",
    image: "img/ghs-kings-juice-bud.webp",
    name: "King's Juice",
    aka: "Mimosa x King's Kush",
    bank: "Green House Seed Co.",
    species: "Híbrida",
    thc: 22, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 900,
    floweringDays: 60, rating: 4.9, reviewsCount: 590,
    genetics: "Mimosa x King's Kush",
    origin: "Ámsterdam (Holanda)",
    dominantTerpene: "limonene",
    terpenes: { limonene: 48, myrcene: 32, linalool: 20 },
    flavors: ["Zumo de Pomelo", "Floral Dulce", "Kush Terroso"],
    effects: ["Euforia Alegre Diáfana", "Relajación Corporal Suave", "Bienestar"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Joyita moderna del catálogo de Green House. Combina los tonos cítricos a zumo de pomelo recién exprimido de Mimosa con la potencia resinosa de King's Kush. Hermosos matices rojizos y violáceos.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-ak-47",
    image: "img/serious-ak-47-bud.webp",
    name: "AK-47",
    aka: "Colombia x México x Tailandia x Afganistán",
    bank: "Serious Seeds",
    species: "Híbrida",
    thc: 22, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 56, rating: 5.0, reviewsCount: 1850,
    genetics: "Colombia x México x Tailandia x Afganistán",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Pino Terroso", "Skunk Dulce", "Madera Especiada"],
    effects: ["Golpe Eufórico Único", "Relajación Corporal Mental", "Alegría"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Cepa legendaria ganadora de más de 27 premios mundiales. Conocida como 'One-Hit Wonder' por su impacto eufórico inmediato y duradero. Cogollos hiperdensos llenos de cristales resplandecientes.",
    visualColor: "linear-gradient(135deg, #DC2626 0%, #991B1B 100%)",
    bgPattern: "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-white-russian",
    image: "img/serious-white-russian-bud.webp",
    name: "White Russian",
    aka: "AK-47 x White Widow",
    bank: "Serious Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 60, rating: 5.0, reviewsCount: 1350,
    genetics: "AK-47 x White Widow",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, caryophyllene: 28, limonene: 20 },
    flavors: ["Skunk Fuerte", "Tierra Húmeda", "Madera Dulce"],
    effects: ["Relajación Anestésica", "Sedación Corporal", "Paz Total"],
    activities: ["relax_sleep", "meditation"],
    description: "Ganadora de la Cannabis Cup 1996. Cruce definitivo entre AK-47 y White Widow. Considerada durante años la planta más potente conocida en laboratorios independientes. Cogollos blancos cargados de resina.",
    visualColor: "linear-gradient(135deg, #475569 0%, #1E293B 100%)",
    bgPattern: "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-chronic",
    image: "img/serious-chronic-bud.webp",
    name: "Chronic",
    aka: "Northern Lights x Skunk x AK-47",
    bank: "Serious Seeds",
    species: "Híbrida",
    thc: 20, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 60, rating: 4.9, reviewsCount: 1120,
    genetics: "Northern Lights x (Skunk #1 x Northern Lights) x AK-47",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Miel Dulce", "Madera Roble", "Fruta Madura"],
    effects: ["Relajación Placentera", "Euforia Suave", "Bienestar"],
    activities: ["social", "relax_sleep", "dining"],
    description: "La máxima exponente de producción masiva sin perder calidad. Híbrido perfeccionado por Serious Seeds de sabor mieloso frutal y efecto relajante eufórico ideal para cualquier ocasión.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #92400E 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-bubble-gum",
    image: "img/serious-bubble-gum-bud.webp",
    name: "Bubble Gum",
    aka: "Selección Indiana Bubblegum",
    bank: "Serious Seeds",
    species: "Híbrida",
    thc: 19, cbd: 0.2,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 60, rating: 5.0, reviewsCount: 1480,
    genetics: "Selección Indiana Bubblegum (USA)",
    origin: "USA / Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Chicle Dulce de Fresa", "Fruta Tropical", "Gominola"],
    effects: ["Euforia Cerebral Alegre", "Relax Físico Suave", "Buen Humor"],
    activities: ["social", "gaming", "party"],
    description: "Legendaria cepa famosa en todo el planeta por su inconfundible e intenso sabor dulce a chicle de fresa. Ganadora de 10 Cannabis Cups. Vigoroso crecimiento y cogollos resinosos muy aromáticos.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-kali-mist",
    image: "img/serious-kali-mist-bud.webp",
    name: "Kali Mist",
    aka: "Cruce Sativo Secreto 2ª Gen",
    bank: "Serious Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 80, rating: 5.0, reviewsCount: 1290,
    genetics: "Cruce Sativo Secreto de 2ª Generación",
    origin: "Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 52, limonene: 28, caryophyllene: 20 },
    flavors: ["Incienso Puro", "Especias Árabes", "Pino Fresco"],
    effects: ["Claridad Cerebral Radiante", "Energía Eufórica", "Creatividad Desbordante"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Considerada por muchos expertos la reina indiscutible de las sativas puras. Ganadora de múltiples Cannabis Cups. Subidón cerebral transparente y estimulante sin pesadez física con un aroma a incienso inigualable.",
    visualColor: "linear-gradient(135deg, #0EA5E9 0%, #0369A1 100%)",
    bgPattern: "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-serious-6",
    image: "img/serious-serious-6-bud.webp",
    name: "Serious 6",
    aka: "Canadian Landrace x Sativa Africana",
    bank: "Serious Seeds",
    species: "Sativa",
    thc: 18, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 850,
    floweringDays: 55, rating: 4.9, reviewsCount: 620,
    genetics: "Canadian Landrace x Sativa Africana",
    origin: "Canadá / África / Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, pinene: 20 },
    flavors: ["Anís Dulce", "Cítrico Especiado", "Pino Fresco"],
    effects: ["Euforia Activa", "Energía Diurna", "Pensamiento Claro"],
    activities: ["social", "nature_walk", "workout"],
    description: "Diseñada específicamente para resistir climas fríos y húmedos de exterior. Floración súper rápida (finales de septiembre en exterior). Muchos fenotipos exhiben hermosos pistilos de color rosa fucsia vibrante.",
    visualColor: "linear-gradient(135deg, #F43F5E 0%, #BE123C 100%)",
    bgPattern: "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-warlock",
    image: "img/serious-warlock-bud.webp",
    name: "Warlock",
    aka: "Skunk #1 x Afghani",
    bank: "Serious Seeds",
    species: "Indica",
    thc: 20, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 58, rating: 4.8, reviewsCount: 540,
    genetics: "Skunk #1 x Afghani (Magus Genetics)",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Fruta Ácida", "Skunk Terroso", "Dulce Añejo"],
    effects: ["Subidón Eufórico Intenso", "Relajación Corporal", "Bienestar"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Variedad de culto proveniente del banco Magus Genetics absorbido por Serious Seeds. Relación hojas-cogollos excepcional, enormes cálices hinchados y un profundo perfume frutal dulzón.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-biddy-early",
    image: "img/serious-biddy-early-bud.webp",
    name: "Biddy Early",
    aka: "Early Skunk x Warlock",
    bank: "Serious Seeds",
    species: "Sativa",
    thc: 18, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 750,
    floweringDays: 55, rating: 4.8, reviewsCount: 490,
    genetics: "Early Skunk x Warlock",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 46, terpinolene: 34, caryophyllene: 20 },
    flavors: ["Caramelo Dulce", "Tierra Húmeda", "Fruta Ácida"],
    effects: ["Euforia Relajante", "Sensación Antiestrés", "Desconexión"],
    activities: ["social", "nature_walk", "relax_sleep"],
    description: "Una de las mejores cepas de exterior para latitudes frías del norte. Ganadora del 2º premio en la High Times Cannabis Cup en categoría Sativa. Tonalidades púrpuras con el frío y floración veloz.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-serious-happiness",
    image: "img/serious-serious-happiness-bud.webp",
    name: "Serious Happiness",
    aka: "AK-47 x Warlock",
    bank: "Serious Seeds",
    species: "Híbrida",
    thc: 21, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.9, reviewsCount: 430,
    genetics: "AK-47 x Warlock",
    origin: "Holanda",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Frutal Dulce", "Especias Maderosas", "Skunk Aterciopelado"],
    effects: ["Felicidad Eufórica", "Relajación Corporal Placentera", "Paz Mental"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "El nombre lo dice todo: diseñada para brindar pura felicidad a cultivadores y consumidores. Cruce de AK-47 con Warlock. Abundante producción de cogollos centrales de aroma dulce especiado.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "serious-kali-bubba",
    image: "img/serious-kali-bubba-bud.webp",
    name: "Kali Bubba",
    aka: "Kali Mist x Bubble Gum",
    bank: "Serious Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 65, rating: 4.9, reviewsCount: 380,
    genetics: "Kali Mist x Bubble Gum",
    origin: "Holanda",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, myrcene: 32, limonene: 20 },
    flavors: ["Chicle de Incienso", "Especias Dulces", "Fruta Tropical"],
    effects: ["Euforia Creativa", "Sensación Alegre", "Energía Diurna"],
    activities: ["creativity", "social", "party"],
    description: "Fusión de dos de las cepas más icónicas de Serious Seeds: la legendaria Kali Mist y la dulcísima Bubble Gum. Combina cogollos altos en resina con sabor a chicle especiado e incienso.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-pink-rozay",
    image: "img/ripper-pink-rozay.webp",
    name: "Pink Rozay",
    aka: "Lemonade x Runtz",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 26, cbd: 0.1,
    yieldIndoor: 580, yieldOutdoor: 800,
    floweringDays: 62, rating: 4.9, reviewsCount: 275,
    genetics: "Lemonade x Runtz (Ripper Selection)",
    origin: "España / California",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Fresa Rosada", "Limón Cremoso", "Uva Dulce"],
    effects: ["Euforia Suave", "Relajación Melosa", "Bienestar Frutal"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "Inspirada en el famoso vino rosado, Pink Rozay de Ripper Seeds es una Indica hipnótica con 26% THC. Cogollos de colores pasteles rosados y violáceos, aroma a frutas del bosque con fondo cremoso. Ideal para sesiones vespertinas de relax.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #A78BFA 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-fuel-og",
    image: "img/ripper-fuel-og.webp",
    name: "Ripper Fuel",
    aka: "Gorilla Glue #4 x Sour Diesel",
    bank: "Ripper Seeds",
    species: "Híbrida",
    thc: 25, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 900,
    floweringDays: 63, rating: 4.8, reviewsCount: 320,
    genetics: "Gorilla Glue #4 x Sour Diesel",
    origin: "España / Nueva York",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 42, limonene: 35, myrcene: 23 },
    flavors: ["Diésel Potente", "Tierra Oscura", "Limón Ácido"],
    effects: ["Potencia Cerebral", "Relajación Progresiva", "Motivación Intensa"],
    activities: ["creativity", "gaming", "workout"],
    description: "La mezcla perfecta de dos gigantes americanos: Gorilla Glue #4 y Sour Diesel. Ripper Fuel ofrece una fuerza explosiva con aroma diésel sobre fondo terroso especiado. Cogollos cementados de resina, producción bestial en indoor.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-zombie-wash",
    image: "img/ripper-zombie-wash.webp",
    name: "Zombiewash",
    aka: "Zombie Kush x Washing Machine",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 23, cbd: 0.3,
    yieldIndoor: 520, yieldOutdoor: 700,
    floweringDays: 58, rating: 4.9, reviewsCount: 290,
    genetics: "Zombie Kush x Washing Machine",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, caryophyllene: 28, pinene: 20 },
    flavors: ["Regaliz Oscuro", "Tierra Húmeda", "Queso Curado"],
    effects: ["Sedación Profunda", "Alivio Total", "Sueño Inmediato"],
    activities: ["relax_sleep", "meditation"],
    description: "El cruce más heavy de Ripper Seeds: Zombie Kush por Washing Machine. Terroso y pesado como un bloque de hachís afgano. Cogollos compactos cubiertos de cristales con un efecto sedante de los que no te levantan del sofá.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #1F2937 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-candy-crack",
    image: "img/ripper-candy-crack.webp",
    name: "Candy Crack",
    aka: "Candy Kush x Green Crack",
    bank: "Ripper Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 750,
    floweringDays: 65, rating: 4.8, reviewsCount: 240,
    genetics: "Candy Kush x Green Crack",
    origin: "España / California",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Caramelo Explosivo", "Mango Ácido", "Dulce Mentolado"],
    effects: ["Energía Luminosa", "Foco Mental", "Alegría Social"],
    activities: ["creativity", "workout", "social", "nature_walk"],
    description: "Sativa de día perfecta. Candy Crack mezcla la dulzura de Candy Kush con la energía disparada de Green Crack. Aroma a caramelitos tropicales con un efecto estimulante que dura horas sin colapso final.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "ripper-juicy-zkittlez",
    image: "img/ripper-juicy-zkittlez.webp",
    name: "Juicy Zkittlez",
    aka: "Zkittlez x Tropicana Cookies",
    bank: "Ripper Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 560, yieldOutdoor: 780,
    floweringDays: 60, rating: 4.8, reviewsCount: 210,
    genetics: "Zkittlez x Tropicana Cookies",
    origin: "España / California",
    dominantTerpene: "limonene",
    terpenes: { limonene: 48, caryophyllene: 32, myrcene: 20 },
    flavors: ["Chuche de Fresa", "Naranja Jugosa", "Gominola Tropical"],
    effects: ["Relax Dulce", "Euforia Frutal", "Bienestar Generalizado"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "El dulcísimo cruce de Zkittlez con Tropicana Cookies. Una bomba sensorial de gominolas tropicales con aroma que recuerda a una tienda de chuches. Cogollos multicolores de una belleza visual excepcional.",
    visualColor: "linear-gradient(135deg, #A78BFA 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(167,139,250,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-zkittlez-og",
    image: "img/bf-zkittlez-og.webp",
    name: "Zkittlez OG",
    aka: "Zkittlez x OG Kush",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 23, cbd: 0.1,
    yieldIndoor: 650, yieldOutdoor: 1200,
    floweringDays: 56, rating: 4.9, reviewsCount: 560,
    genetics: "Zkittlez x OG Kush",
    origin: "Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Frutas del Bosque", "Caramelo Cítrico", "Kush Dulce"],
    effects: ["Felicidad Inmediata", "Relajación Corporal", "Euforia Suave"],
    activities: ["social", "relax_sleep", "gaming"],
    description: "La aclamada Zkittlez cruzada con la legendaria OG Kush por Barney's Farm. Cogollos ultra densos, explosión de terpenos frutales con base Kush terrosa. Premio múltiple en la Copa del Mundo de la Cannabis.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-lsd",
    image: "img/bf-lsd.webp",
    name: "LSD",
    aka: "Mazar x Skunk #1",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 24, cbd: 1.2,
    yieldIndoor: 600, yieldOutdoor: 1000,
    floweringDays: 60, rating: 4.9, reviewsCount: 780,
    genetics: "Mazar x Skunk #1",
    origin: "Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, linalool: 20 },
    flavors: ["Tierra Psicodélica", "Lavanda Oscura", "Especias Kush"],
    effects: ["Psicoactividad Intensa", "Relajación Profunda", "Introspección"],
    activities: ["meditation", "creativity", "relax_sleep"],
    description: "Una de las Índicas más potentes y premiadas de Barney's Farm. Ganadora de la High Times Cannabis Cup. LSD combina el poder genético de Mazar con el clásico Skunk #1. Efecto psicoactivo único con CBD notable para un equilibrio sorprendente.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-pineapple-chunk",
    image: "img/bf-pineapple-chunk.webp",
    name: "Pineapple Chunk",
    aka: "Pineapple x Cheese x Skunk #1",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 26, cbd: 0.3,
    yieldIndoor: 700, yieldOutdoor: 1200,
    floweringDays: 55, rating: 4.8, reviewsCount: 670,
    genetics: "Pineapple x Cheese x Skunk #1",
    origin: "Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 42, limonene: 38, myrcene: 20 },
    flavors: ["Piña Tropical", "Queso Suave", "Dulce Exótico"],
    effects: ["Relajación Placentera", "Euforia Moderada", "Felicidad Frutal"],
    activities: ["relax_sleep", "social", "nature_walk"],
    description: "Una mezcla genial de tres clásicos: Pineapple, Cheese y Skunk #1. Alta producción de cogollos repletos de resina con aroma tropical inconfundible. 26% THC en una Índica de floración rápida, muy valorada en toda Europa.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-acapulco-gold",
    image: "img/bf-acapulco-gold.webp",
    name: "Acapulco Gold",
    aka: "Landrace Sativa Mexicana",
    bank: "Barney's Farm",
    species: "Sativa",
    thc: 21, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 900,
    floweringDays: 75, rating: 4.8, reviewsCount: 440,
    genetics: "Landrace Sativa de Acapulco (México)",
    origin: "México / Ámsterdam",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 30, pinene: 20 },
    flavors: ["Caramelo Ahumado", "Tierra Dorada", "Cítrico Tropical"],
    effects: ["Euforia Cerebral Pura", "Creatividad Explosiva", "Energía Duradera"],
    activities: ["creativity", "nature_walk", "social", "workout"],
    description: "La legendaria landrace mexicana en manos de Barney's Farm. Acapulco Gold fue en los años 60-70 la cepa más buscada del mundo. Esta versión preserva su genética pura con cogollos dorados y un efecto Sativa incomparable, sin paranoia.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "bf-wedding-cake",
    image: "img/bf-wedding-cake.webp",
    name: "Wedding Cake",
    aka: "Triangle Kush x Animal Mints",
    bank: "Barney's Farm",
    species: "Indica",
    thc: 27, cbd: 0.1,
    yieldIndoor: 700, yieldOutdoor: 1400,
    floweringDays: 56, rating: 5.0, reviewsCount: 920,
    genetics: "Triangle Kush x Animal Mints",
    origin: "Ámsterdam / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 44, limonene: 36, linalool: 20 },
    flavors: ["Vainilla Cremosa", "Masa Dulce", "Tierra Kush"],
    effects: ["Potencia Máxima", "Relajación Total", "Bienestar Profundo"],
    activities: ["relax_sleep", "gaming", "meditation"],
    description: "Una de las cepas más solicitadas del mundo. Wedding Cake de Barney's Farm alcanza 27% THC con una producción masiva. Aroma a pastel de vainilla con Kush terroso. Cogollos enormes, resinosos y de una calidad visual espectacular.",
    visualColor: "linear-gradient(135deg, #F9FAFB 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,250,251,0.15) 0%, transparent 70%)"
  },
  {
id: "rqs-honey-cream",
    image: "img/rqs-honey-cream.webp",
    name: "Honey Cream",
    aka: "Critical Mass x BlueBlack",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 18, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 50, rating: 4.7, reviewsCount: 460,
    genetics: "Critical Mass x BlueBlack",
    origin: "Ámsterdam / España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, linalool: 30, caryophyllene: 20 },
    flavors: ["Miel Floral", "Vainilla Suave", "Frutos Rojos"],
    effects: ["Relajación Dulce", "Bienestar Corporal", "Paz Mental"],
    activities: ["relax_sleep", "meditation", "social"],
    description: "Honey Cream de RQS es una Índica deliciosa y equilibrada. Baja en THC para experiencias suaves, con un aroma a miel floral excepcional. Floración ultrarrápida en 50 días. Perfecta para cultivadores buscando calidad sin psicoactividad extrema.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-og-kush-auto",
    image: "img/rqs-og-kush-auto.webp",
    name: "OG Kush Auto",
    aka: "OG Kush x Ruderalis",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 17, cbd: 0.3,
    yieldIndoor: 425, yieldOutdoor: 170,
    floweringDays: 49, rating: 4.7, reviewsCount: 580,
    genetics: "OG Kush x Ruderalis",
    origin: "California / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, limonene: 20 },
    flavors: ["Tierra OG", "Pino Kush", "Cítrico Suave"],
    effects: ["Relajación Clásica OG", "Euforia Moderada", "Pesadez Agradable"],
    activities: ["relax_sleep", "gaming", "social"],
    description: "La genética OG Kush en formato autoflowering de RQS. Conserva el aroma clásico a tierra y pino de la OG con un ciclo de cultivo de solo 49 días desde germinación. Discreta, manejable y deliciosa. La opción perfecta para cultivadores noveles.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-purple-queen",
    image: "img/rqs-purple-queen.webp",
    name: "Purple Queen",
    aka: "Hindu Kush x Purple Afghani",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 55, rating: 4.8, reviewsCount: 490,
    genetics: "Hindu Kush x Purple Afghani",
    origin: "Afganistán / India",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, linalool: 28, caryophyllene: 20 },
    flavors: ["Uva Oscura", "Tierra Afgana", "Frutas Silvestres"],
    effects: ["Sedación Potente", "Relajación Muscular", "Euforia Suave"],
    activities: ["relax_sleep", "meditation"],
    description: "Joya de colores: Purple Queen desarrolla tonalidades moradas y violetas impresionantes al bajar la temperatura. Genética pura afgana e hindú. Efecto sedante profundo con sabor a uvas oscuras y tierra ancestral. Espectacular en extracción de hash.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-blue-mystic",
    image: "img/rqs-blue-mystic.webp",
    name: "Blue Mystic",
    aka: "Blueberry x Skunk #1",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 21, cbd: 0.2,
    yieldIndoor: 475, yieldOutdoor: 550,
    floweringDays: 56, rating: 4.7, reviewsCount: 420,
    genetics: "Blueberry x Skunk #1",
    origin: "Ámsterdam / Oregon",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, linalool: 30, caryophyllene: 20 },
    flavors: ["Arándano Fresco", "Skunk Suave", "Frutas Azules"],
    effects: ["Relajación Dulce", "Euforia Serena", "Descanso Placentero"],
    activities: ["relax_sleep", "social", "nature_walk"],
    description: "Blue Mystic combina lo mejor de Blueberry con el clásico Skunk #1. Cogollos azulados compactos con un aroma frutal inconfundible. Bajo perfil de olor, ideal para cultivos discretos. Efecto equilibrado, ideal para tarde-noche.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "rqs-watermelon",
    image: "img/rqs-watermelon.webp",
    name: "Watermelon",
    aka: "Watermelon Zkittlez x Ghost OG",
    bank: "Royal Queen Seeds",
    species: "Indica",
    thc: 22, cbd: 0.2,
    yieldIndoor: 525, yieldOutdoor: 650,
    floweringDays: 56, rating: 4.8, reviewsCount: 350,
    genetics: "Watermelon Zkittlez x Ghost OG",
    origin: "California / Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 48, caryophyllene: 32, myrcene: 20 },
    flavors: ["Sandía Dulce", "Frutas Tropicales", "OG Suave"],
    effects: ["Euforia Frutal", "Relajación Corporal", "Bienestar Veraniego"],
    activities: ["social", "nature_walk", "relax_sleep"],
    description: "Watermelon de RQS es pura alegría de verano en forma de cepa. Cruce de Watermelon Zkittlez con Ghost OG. Cogollos extraordinariamente resinosos con aroma dominante a sandía fresca. Un dulzor que engancha desde la primera calada.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "ss-sweet-amnesia-haze",
    image: "img/sweet-amnesia-haze.webp",
    name: "Sweet Amnesia Haze",
    aka: "Amnesia Haze x Jack Herer Selection",
    bank: "Sweet Seeds",
    species: "Sativa",
    thc: 22, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 65, rating: 4.8, reviewsCount: 510,
    genetics: "Amnesia Haze x Jack Herer Selection",
    origin: "España / Ámsterdam",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 32, pinene: 20 },
    flavors: ["Limón Dulce", "Incienso Haze", "Menta Suave"],
    effects: ["Subidón Cerebral", "Creatividad Intensa", "Energía Luminosa"],
    activities: ["creativity", "social", "nature_walk"],
    description: "La versión dulce de Amnesia Haze de Sweet Seeds. Cruce con Jack Herer que suaviza el perfil amaderado y añade un punto dulce al incienso clásico Haze. Gran productora en indoor con cogollos altos en resina y efecto Sativa sin ansiedad.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #34D399 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "ss-crystal-candy",
    image: "img/sweet-crystal-candy.webp",
    name: "Crystal Candy",
    aka: "Blue Black x Maple Leaf Indica x White Widow",
    bank: "Sweet Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 575, yieldOutdoor: 750,
    floweringDays: 55, rating: 4.9, reviewsCount: 680,
    genetics: "Blue Black x Maple Leaf Indica x White Widow",
    origin: "España",
    dominantTerpene: "linalool",
    terpenes: { linalool: 42, myrcene: 38, caryophyllene: 20 },
    flavors: ["Frutas del Bosque", "Caramelo Floral", "Miel Silvestre"],
    effects: ["Relajación Profunda", "Euforia Melosa", "Felicidad Tranquila"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Crystal Candy es una de las favoritas de Sweet Seeds, ganadora de múltiples premios. Cogollos cubiertos de una capa de cristales de resina como si estuvieran espolvoreados de azúcar. Sabor a frutas del bosque con miel floral irresistible.",
    visualColor: "linear-gradient(135deg, #A78BFA 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(167,139,250,0.2) 0%, transparent 70%)"
  },
  {
id: "ss-red-hot-cookies",
    image: "img/sweet-red-hot-cookies.webp",
    name: "Red Hot Cookies",
    aka: "Ghost OG x Thin Mint Cookies",
    bank: "Sweet Seeds",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 390,
    genetics: "Ghost OG x Thin Mint Cookies",
    origin: "España / California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 30, linalool: 25 },
    flavors: ["Galleta Especiada", "Menta Picante", "OG Terroso"],
    effects: ["Potencia Equilibrada", "Relajación Sin Somnolencia", "Bienestar Físico"],
    activities: ["social", "gaming", "relax_sleep"],
    description: "Red Hot Cookies fusiona la potencia de Ghost OG con la elegancia de Thin Mint Cookies. Cogollos densos con tonos rojizos y naranja al madurar. Perfil de sabor complejo entre especias, menta y tierra. Una de las joyas de Sweet Seeds.",
    visualColor: "linear-gradient(135deg, #EF4444 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "ss-black-cream-auto",
    image: "img/sweet-black-cream-auto.webp",
    name: "Black Cream Auto",
    aka: "Black Domina x Cream Caramel x Ruderalis",
    bank: "Sweet Seeds",
    species: "Indica",
    thc: 18, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 200,
    floweringDays: 63, rating: 4.8, reviewsCount: 440,
    genetics: "Black Domina x Cream Caramel x Ruderalis",
    origin: "España",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, linalool: 30, caryophyllene: 20 },
    flavors: ["Caramelo Oscuro", "Frutas Negras", "Tierra Dulce"],
    effects: ["Sedación Nocturna", "Relajación Profunda", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "Autoflowering de gran belleza visual con tonos negros y morados profundos. Black Cream Auto de Sweet Seeds mezcla la fuerza sedante de Black Domina con la dulzura de Cream Caramel. Ciclo muy rápido sin depender del fotoperiodo.",
    visualColor: "linear-gradient(135deg, #1F2937 0%, #7C3AED 100%)",
    bgPattern: "radial-gradient(circle, rgba(31,41,55,0.4) 0%, transparent 70%)"
  },
  {
id: "ss-bigdevil-xl",
    image: "img/sweet-big-devil-xl.webp",
    name: "Big Devil XL Auto",
    aka: "Jack Herer x Big Devil",
    bank: "Sweet Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 400,
    floweringDays: 75, rating: 4.8, reviewsCount: 520,
    genetics: "Jack Herer x Big Devil Auto",
    origin: "España",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 46, limonene: 34, pinene: 20 },
    flavors: ["Pino Fresco", "Limón Herbal", "Especias Jack"],
    effects: ["Energía Creativa", "Claridad Mental", "Motivación"],
    activities: ["creativity", "workout", "nature_walk"],
    description: "La autoflowering Sativa más grande de Sweet Seeds. Big Devil XL Auto combina la genética de Jack Herer con Big Devil para producir plantas gigantes de perfil energético. Ideal para outdoor en climas cálidos con ciclos de luz prolongados.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dp-frisian-dew",
    image: "img/dp-frisian-dew.webp",
    name: "Frisian Dew",
    aka: "Super Skunk x Purple Star",
    bank: "Dutch Passion",
    species: "Híbrida",
    thc: 16, cbd: 0.4,
    yieldIndoor: 400, yieldOutdoor: 1000,
    floweringDays: 45, rating: 4.8, reviewsCount: 550,
    genetics: "Super Skunk x Purple Star",
    origin: "Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, terpinolene: 32, pinene: 20 },
    flavors: ["Tierra Skunk", "Flores Silvestres", "Frutas Moradas"],
    effects: ["Bienestar Equilibrado", "Euforia Suave", "Relax Sin Pesadez"],
    activities: ["nature_walk", "social", "relax_sleep"],
    description: "La reina del outdoor de Dutch Passion. Frisian Dew está diseñada específicamente para el cultivo exterior en climas fríos del norte de Europa. Resistente a la humedad y hongos, produce plantas enormes con cogollos violetas o verdes de impresionante densidad.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "dp-mazar",
    image: "img/dp-mazar.webp",
    name: "Mazar",
    aka: "Afghan x Skunk",
    bank: "Dutch Passion",
    species: "Indica",
    thc: 20, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 610,
    genetics: "Afghan x Skunk",
    origin: "Afganistán / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, caryophyllene: 28, pinene: 17 },
    flavors: ["Hachís Afgano", "Tierra Húmeda", "Skunk Dulce"],
    effects: ["Sedación Profunda", "Relajación Muscular Intensa", "Sueño Pesado"],
    activities: ["relax_sleep", "meditation"],
    description: "Un auténtico clásico de Dutch Passion desde los años 90. Mazar lleva el nombre del famoso distrito afgano de Mazari Sharif. Purísima genética Indica con un efecto sedante devastador y producción generosa de resina. Base genética de muchísimas cepas modernas.",
    visualColor: "linear-gradient(135deg, #374151 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.3) 0%, transparent 70%)"
  },
  {
id: "dp-auto-mazar",
    image: "img/dp-auto-mazar.webp",
    name: "Auto Mazar",
    aka: "Mazar x Ruderalis (Dutch Passion)",
    bank: "Dutch Passion",
    species: "Indica",
    thc: 20, cbd: 0.5,
    yieldIndoor: 400, yieldOutdoor: 150,
    floweringDays: 70, rating: 4.9, reviewsCount: 490,
    genetics: "Mazar x Ruderalis",
    origin: "Afganistán / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 54, caryophyllene: 28, pinene: 18 },
    flavors: ["Hachís Puro", "Pino Oscuro", "Tierra Especiada"],
    effects: ["Sedación Nocturna", "Alivio Físico Profundo", "Descanso Total"],
    activities: ["relax_sleep", "meditation"],
    description: "La versión autoflowering de la legendaria Mazar de Dutch Passion. Mantiene el carácter Indica auténtico con el ciclo rápido propio de las autos. Premio múltiple en Cannabis Cups de categoría autoflowering. Resina excepcional para extracciones.",
    visualColor: "linear-gradient(135deg, #374151 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.3) 0%, transparent 70%)"
  },
  {
id: "dp-skywalker-og",
    image: "img/dp-skywalker-og.webp",
    name: "Skywalker OG",
    aka: "Skywalker x OG Kush",
    bank: "Dutch Passion",
    species: "Indica",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 800,
    floweringDays: 60, rating: 4.9, reviewsCount: 670,
    genetics: "Skywalker x OG Kush",
    origin: "California / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["OG Terroso", "Frutas Oscuras", "Kush Pimentado"],
    effects: ["Potencia Física Intensa", "Relajación Galáctica", "Euforia Inicial"],
    activities: ["relax_sleep", "gaming", "meditation"],
    description: "Dutch Passion tomó la mítica Skywalker y la cruzó con OG Kush creando una Indica de potencia galáctica. 23% THC con cogollos enormes recubiertos de resina cristalina. Efecto que comienza eufórico y termina en una relajación absoluta.",
    visualColor: "linear-gradient(135deg, #1E3A5F 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,58,95,0.3) 0%, transparent 70%)"
  },
  {
id: "phil-lemon-og-candy",
    image: "img/philo-lemon-og-candy.webp",
    name: "Lemon OG Candy",
    aka: "Lemon Skunk x OG Kush",
    bank: "Philosopher Seeds",
    species: "Híbrida",
    thc: 20, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 340,
    genetics: "Lemon Skunk x OG Kush",
    origin: "España",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, caryophyllene: 25, pinene: 20 },
    flavors: ["Limón Caramelizado", "OG Cremoso", "Dulce Cítrico"],
    effects: ["Euforia Alegre", "Relajación Equilibrada", "Claridad Mental"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Lemon OG Candy de Philosopher Seeds combina lo mejor de Lemon Skunk con la profundidad de OG Kush. El resultado: una híbrida de aroma intensísimo a limón dulce con fondo terroso OG. Muy valorada en España por su equilibrio entre efecto y sabor.",
    visualColor: "linear-gradient(135deg, #FBBF24 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(251,191,36,0.2) 0%, transparent 70%)"
  },
  {
id: "phil-critical-sensi-star",
    image: "img/philo-critical-sensi-star.webp",
    name: "Critical Sensi Star",
    aka: "Critical Mass x Sensi Star",
    bank: "Philosopher Seeds",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 600, yieldOutdoor: 900,
    floweringDays: 55, rating: 4.8, reviewsCount: 410,
    genetics: "Critical Mass x Sensi Star",
    origin: "España / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Tierra Afgan", "Incienso Suave", "Dulce Herbal"],
    effects: ["Relajación Potente", "Alivio Físico", "Euforia Moderada"],
    activities: ["relax_sleep", "meditation", "social"],
    description: "Critical Sensi Star es una Índica de altos rendimientos. Combina la producción descomunal de Critical Mass con el efecto profundo de Sensi Star. Filosófica, relajante y medicinal por naturaleza. Cogollos compactos tipo bloque con aroma incensado.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "phil-bubbas-gift",
    image: "img/philo-bubbas-gift.webp",
    name: "Bubba's Gift",
    aka: "Bubba Kush x God's Gift",
    bank: "Philosopher Seeds",
    species: "Indica",
    thc: 22, cbd: 0.2,
    yieldIndoor: 480, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.9, reviewsCount: 360,
    genetics: "Bubba Kush x God's Gift",
    origin: "España / California",
    dominantTerpene: "linalool",
    terpenes: { linalool: 45, myrcene: 35, caryophyllene: 20 },
    flavors: ["Lavanda Oscura", "Uva Morada", "Tierra Kush"],
    effects: ["Sedación Divina", "Paz Total", "Sueño Reparador"],
    activities: ["relax_sleep", "meditation"],
    description: "Un regalo verdadero para los amantes de las Índicas. Bubba's Gift cruza el icónico Bubba Kush con God's Gift generando un efecto sedante excepcional. Cogollos morados aromáticos con notas de lavanda y uva. Ideal para el descanso nocturno.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "phil-snow-storm",
    image: "img/philo-snow-storm.webp",
    name: "Snow Storm",
    aka: "White Widow x Power Plant",
    bank: "Philosopher Seeds",
    species: "Híbrida",
    thc: 21, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 800,
    floweringDays: 58, rating: 4.7, reviewsCount: 280,
    genetics: "White Widow x Power Plant",
    origin: "España / Holanda",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, myrcene: 38, pinene: 22 },
    flavors: ["Pino Fresco", "Tierra Blanca", "Incienso Herbal"],
    effects: ["Subidón Equilibrado", "Bienestar General", "Claridad Relajada"],
    activities: ["social", "nature_walk", "creativity"],
    description: "Snow Storm captura la producción masiva de resina de White Widow combinada con la energía y el vigor de Power Plant. Una tempestad blanca de cristales que cubre los cogollos. Equilibrada entre cabeza y cuerpo, perfecta para cualquier momento del día.",
    visualColor: "linear-gradient(135deg, #E5E7EB 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(229,231,235,0.15) 0%, transparent 70%)"
  },
  {
id: "hso-liberty-haze",
    image: "img/hso-liberty-haze-official.webp",
    name: "Liberty Haze",
    aka: "G13 x ChemDawg 91",
    bank: "Humboldt Seed",
    species: "Híbrida",
    thc: 25, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 56, rating: 4.9, reviewsCount: 690,
    genetics: "G13 x ChemDawg 91",
    origin: "California / Humboldt County",
    dominantTerpene: "limonene",
    terpenes: { limonene: 48, caryophyllene: 32, terpinolene: 20 },
    flavors: ["Lima Ácida", "Diésel Suave", "Cítrico Luminoso"],
    effects: ["Subidón Cerebral Potente", "Energía Creativa", "Motivación"],
    activities: ["creativity", "social", "workout"],
    description: "Liberty Haze ganó la Cannabis Cup de Ámsterdam en la categoría de Híbridas. 25% THC con un aroma a lima y diésel inconfundible. Cruce de G13 con la mítica ChemDawg 91. Floración rápida para ser Haze y producción muy generosa.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-sapphire-og",
    image: "img/hso-sapphire-og-official.webp",
    name: "Sapphire OG",
    aka: "Blueberry x OG Kush",
    bank: "Humboldt Seed",
    species: "Indica",
    thc: 22, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 380,
    genetics: "Blueberry x OG Kush",
    origin: "California / Humboldt County",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, linalool: 30, caryophyllene: 20 },
    flavors: ["Arándano OG", "Frutas Azules", "Tierra Kush"],
    effects: ["Relajación Joya", "Euforia Suave", "Bienestar Físico"],
    activities: ["relax_sleep", "meditation", "social"],
    description: "Sapphire OG es una gema de Humboldt Seed. Blueberry cruzada con OG Kush genera cogollos de tono azulado zafiro con un aroma frutal y terroso Kush. Efecto relajante y envolvente como una joya preciosa. Muy valorada en la costa oeste de EE.UU.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-707-headband",
    image: "img/hso-707-headband-4k.webp",
    name: "707 Headband",
    aka: "OG Kush x Sour Diesel",
    bank: "Humboldt Seed",
    species: "Híbrida",
    thc: 24, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 63, rating: 4.8, reviewsCount: 480,
    genetics: "OG Kush x Sour Diesel",
    origin: "Humboldt County, California",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 42, limonene: 38, myrcene: 20 },
    flavors: ["Diésel Cremoso", "OG Limón", "Combustible Suave"],
    effects: ["Presión Craneal (\"Headband\")", "Euforia Cerebral", "Relajación Progresiva"],
    activities: ["creativity", "social", "gaming"],
    description: "Llamada Headband por la sensación de presión suave alrededor de la frente que produce. 707 Headband es una leyenda de Humboldt County. Cruce de OG Kush con Sour Diesel. Célebre por su efecto lento que va escalando durante 20-30 minutos.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "hso-blue-fire",
    image: "img/hso-blue-fire-4k.webp",
    name: "Blue Fire",
    aka: "Blueberry x Fire OG",
    bank: "Humboldt Seed",
    species: "Indica",
    thc: 23, cbd: 0.2,
    yieldIndoor: 525, yieldOutdoor: 700,
    floweringDays: 60, rating: 4.8, reviewsCount: 310,
    genetics: "Blueberry x Fire OG",
    origin: "California / Humboldt County",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 48, caryophyllene: 32, linalool: 20 },
    flavors: ["Arándano Fuego", "Frutas Ardientes", "OG Oscuro"],
    effects: ["Relajación Ardiente", "Euforia Cálida", "Sedación Progresiva"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "Blue Fire es el resultado brillante de cruzar Blueberry con Fire OG. El fuego de la OG Kush más potente combinado con la dulzura frutal de Blueberry. Cogollos con tonos azulados y naranjas al madurar. Un espectáculo visual y aromático.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "00s-cheese-xl",
    image: "img/00s-cheese-xl.webp",
    name: "Cheese XL Auto",
    aka: "Original UK Cheese x Ruderalis",
    bank: "00 Seeds Bank",
    species: "Indica",
    thc: 19, cbd: 0.4,
    yieldIndoor: 500, yieldOutdoor: 200,
    floweringDays: 65, rating: 4.7, reviewsCount: 430,
    genetics: "Original UK Cheese x Ruderalis",
    origin: "España / Reino Unido",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, myrcene: 30, limonene: 20 },
    flavors: ["Queso Maduro Intenso", "Tierra Britiánica", "Skunk Dulce"],
    effects: ["Relajación Corporal", "Euforia Suave", "Bienestar Clásico"],
    activities: ["relax_sleep", "social", "gaming"],
    description: "La icónica genética UK Cheese en formato autoflowering de 00 Seeds Bank. Preserva al 100% el inconfundible aroma lácteo y terroso del queso inglés. Producción rápida sin depender del fotoperiodo. La elección perfecta para amantes del estilo Cheese.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "00s-critical-mass",
    image: "img/00s-critical-mass.webp",
    name: "Critical Mass CBD",
    aka: "Critical Mass x High CBD Selection",
    bank: "00 Seeds Bank",
    species: "Indica",
    thc: 9, cbd: 10,
    yieldIndoor: 600, yieldOutdoor: 900,
    floweringDays: 55, rating: 4.8, reviewsCount: 510,
    genetics: "Critical Mass x High CBD Selection",
    origin: "España / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Tierra Dulce", "Herbal Medicinal", "Incienso Suave"],
    effects: ["Bienestar Sin Psicoactividad", "Calma Profunda", "Alivio Físico"],
    activities: ["meditation", "relax_sleep", "workout"],
    description: "Critical Mass CBD de 00 Seeds Bank ofrece la misma producción descomunal de la Critical original pero con un ratio THC:CBD casi 1:1 (9%/10%). Ideal para uso medicinal y recreativo suave. Cogollos enormes de aroma terroso herbal con efecto analgésico notable.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "00s-white-smurf",
    image: "img/00s-white-smurf.webp",
    name: "White Smurf Auto",
    aka: "White Widow x Ruderalis",
    bank: "00 Seeds Bank",
    species: "Híbrida",
    thc: 17, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 170,
    floweringDays: 65, rating: 4.7, reviewsCount: 360,
    genetics: "White Widow x Ruderalis",
    origin: "España / Holanda",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 44, myrcene: 36, pinene: 20 },
    flavors: ["Resina Blanca", "Tierra Herbal", "Pino Suave"],
    effects: ["Equilibrio Mental-Físico", "Relajación Progresiva", "Bienestar General"],
    activities: ["social", "relax_sleep", "nature_walk"],
    description: "White Smurf Auto lleva la legendaria genética White Widow al mundo autoflowering. Plantas compactas con cogollos blanquísimos cubiertos de resina. Perfecta para cultivos de interior en espacios reducidos. Sencilla de cultivar, exigente en sabor.",
    visualColor: "linear-gradient(135deg, #E5E7EB 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(229,231,235,0.15) 0%, transparent 70%)"
  },
  {
id: "00s-afghan-mass",
    image: "img/oo-super-skunk.webp",
    name: "Afghan Mass",
    aka: "Afghan x Critical Mass",
    bank: "00 Seeds Bank",
    species: "Indica",
    thc: 20, cbd: 0.4,
    yieldIndoor: 650, yieldOutdoor: 1000,
    floweringDays: 50, rating: 4.9, reviewsCount: 470,
    genetics: "Afghan Landrace x Critical Mass",
    origin: "España / Afganistán",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, caryophyllene: 28, pinene: 17 },
    flavors: ["Hachís Afgano Puro", "Tierra Oscura", "Especias Orientales"],
    effects: ["Sedación Total", "Relajación Física Extrema", "Sueño Profundo"],
    activities: ["relax_sleep", "meditation"],
    description: "Afghan Mass de 00 Seeds Bank fusiona la genética pura afgana con la producción masiva de Critical Mass. El resultado: Índica de floración ultrarrápida (50 días), producción record y efecto sedante afgano puro. Una máquina de producir hachís de primera calidad.",
    visualColor: "linear-gradient(135deg, #92400E 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(146,64,14,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-sage-n-sour",
    image: "img/ths-sage-n-sour.webp",
    name: "S.A.G.E.",
    aka: "Sativa Afghani Genetic Equilibrium",
    bank: "TH Seeds",
    species: "Sativa",
    thc: 20, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 70, rating: 4.9, reviewsCount: 720,
    genetics: "Big Sur Holy Weed x Afghani",
    origin: "Nueva York / Ámsterdam",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 50, limonene: 28, pinene: 22 },
    flavors: ["Salvia Aromática", "Cítrico Suave", "Madera Exótica"],
    effects: ["Euforia Cerebral Pura", "Creatividad Sin Límite", "Energía Mental"],
    activities: ["creativity", "meditation", "nature_walk"],
    description: "S.A.G.E. (Sativa Afghani Genetic Equilibrium) es la cepa fundacional de TH Seeds. Ganadora de la High Times Cannabis Cup 2001 y múltiples premios más. Cruza Big Sur Holy Weed con Afghani creando una Sativa de potencia cerebral sin igual y aroma único a salvia y madera exótica.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-mk-ultra",
    image: "img/ths-mk-ultra.webp",
    name: "MK Ultra",
    aka: "G13 x OG Kush",
    bank: "TH Seeds",
    species: "Indica",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 56, rating: 4.9, reviewsCount: 650,
    genetics: "G13 x OG Kush",
    origin: "Nueva York / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 52, caryophyllene: 28, limonene: 20 },
    flavors: ["OG Terroso", "Combustible Suave", "Dulce Herbal"],
    effects: ["Hipnosis Indica", "Relajación Total", "Sedación Progresiva"],
    activities: ["relax_sleep", "gaming", "meditation"],
    description: "MK Ultra de TH Seeds lleva el nombre del infame programa de la CIA. Ganadora de la High Times Cannabis Cup 2003 (1er puesto Indica). G13 x OG Kush con un efecto hipnótico, casi paralizante. Una de las Índicas más potentes de los primeros 2000. Leyenda absoluta.",
    visualColor: "linear-gradient(135deg, #1F2937 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(31,41,55,0.4) 0%, transparent 70%)"
  },
  {
id: "ths-darkstar",
    image: "img/ths-darkstar.webp",
    name: "Darkstar",
    aka: "Mazar I Sharif x Purple Kush",
    bank: "TH Seeds",
    species: "Indica",
    thc: 21, cbd: 0.3,
    yieldIndoor: 450, yieldOutdoor: 650,
    floweringDays: 55, rating: 4.8, reviewsCount: 490,
    genetics: "Mazar I Sharif x Purple Kush",
    origin: "Afganistán / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 54, linalool: 26, caryophyllene: 20 },
    flavors: ["Uva Oscura Afgana", "Tierra Morada", "Frutos Silvestres"],
    effects: ["Sedación Estrellada", "Relajación Total", "Sueño Profundo"],
    activities: ["relax_sleep", "meditation"],
    description: "Darkstar es la Índica más oscura de TH Seeds. Mazar I Sharif cruzada con Purple Kush produciendo cogollos morado oscuro de una densidad impresionante. Aroma a uvas afganas, dulce y terroso. Efecto que aplasta como una estrella oscura al cuerpo.",
    visualColor: "linear-gradient(135deg, #4C1D95 0%, #1F2937 100%)",
    bgPattern: "radial-gradient(circle, rgba(76,29,149,0.3) 0%, transparent 70%)"
  },
  {
id: "ths-heavy-d",
    image: "img/ths-heavy-d.webp",
    name: "Heavy D Indica",
    aka: "Hindu Kush x Super Skunk",
    bank: "TH Seeds",
    species: "Indica",
    thc: 22, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 58, rating: 4.7, reviewsCount: 380,
    genetics: "Hindu Kush x Super Skunk",
    origin: "Afganistán / Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, humulene: 20 },
    flavors: ["Skunk Potente", "Tierra Hindú", "Especias Afganas"],
    effects: ["Peso Corporal Intenso", "Relajación Muscular", "Euforia Corta"],
    activities: ["relax_sleep", "gaming"],
    description: "Heavy D Indica de TH Seeds vive a la altura de su nombre. Hindu Kush x Super Skunk produciendo una de las Índicas de mayor peso corporal del catálogo de TH Seeds. Aroma de skunk terroso con fondo especiado afgano. Floración eficiente con cogollos sólidos.",
    visualColor: "linear-gradient(135deg, #374151 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.3) 0%, transparent 70%)"
  },
  {
id: "ths-kushage",
    image: "img/ths-kushage.webp",
    name: "Kushage",
    aka: "OG Kush x S.A.G.E.",
    bank: "TH Seeds",
    species: "Híbrida",
    thc: 22, cbd: 0.3,
    yieldIndoor: 480, yieldOutdoor: 700,
    floweringDays: 62, rating: 4.8, reviewsCount: 430,
    genetics: "OG Kush x S.A.G.E.",
    origin: "Nueva York / Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 44, terpinolene: 32, myrcene: 24 },
    flavors: ["Salvia OG", "Tierra Especiada", "Maderas Exóticas"],
    effects: ["Equilibrio Cerebro-Cuerpo", "Euforia Moderada", "Bienestar Total"],
    activities: ["social", "creativity", "nature_walk"],
    description: "Kushage es el hijo de las dos grandes estrellas de TH Seeds: OG Kush y S.A.G.E. Equilibra el efecto cerebral de la Sativa con el peso físico de la OG. Aroma complejo a salvia, madera y especias terrosas. Una híbrida con carácter propio.",
    visualColor: "linear-gradient(135deg, #10B981 0%, #374151 100%)",
    bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-mendocino-madness",
    image: "img/ths-mendocino-madness.webp",
    name: "Mendocino Madness",
    aka: "Mendocino Purps x S.A.G.E.",
    bank: "TH Seeds",
    species: "Sativa",
    thc: 19, cbd: 0.4,
    yieldIndoor: 430, yieldOutdoor: 650,
    floweringDays: 68, rating: 4.8, reviewsCount: 340,
    genetics: "Mendocino Purps x S.A.G.E.",
    origin: "California / Ámsterdam",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 48, limonene: 30, pinene: 22 },
    flavors: ["Uva Sativa", "Salvia Floral", "Cítrico Silvestre"],
    effects: ["Locura Creativa Controlada", "Euforia Cerebral", "Alegría Efervescente"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Mendocino Madness captura la esencia de los cultivos clandestinos de Mendocino County, California. Cruce de Mendocino Purps con S.A.G.E. que produce una Sativa de uvas moradas y salvia. El efecto cerebral excita la creatividad hasta el límite de la locura controlada.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-burmese-kush",
    image: "img/ths-burmese-kush.webp",
    name: "Burmese Kush",
    aka: "Burma x OG Kush",
    bank: "TH Seeds",
    species: "Híbrida",
    thc: 21, cbd: 0.3,
    yieldIndoor: 460, yieldOutdoor: 670,
    floweringDays: 63, rating: 4.8, reviewsCount: 390,
    genetics: "Burma Landrace x OG Kush",
    origin: "Myanmar / Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 44, caryophyllene: 36, myrcene: 20 },
    flavors: ["Cítrico Asiático", "Kush Especiado", "Flores Birmanas"],
    effects: ["Euforia Exótica", "Bienestar Oriental", "Relajación Progresiva"],
    activities: ["meditation", "creativity", "social"],
    description: "TH Seeds viajó hasta Myanmar para encontrar la landrace Burma y cruzarla con OG Kush. El resultado es Burmese Kush: una híbrida exótica con aroma floral asiático sobre base Kush especiada. Una combinación de mundos genéticos que pocas casas se atrevieron a explorar.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-sage-n-sour-hybrid",
    image: "img/ths-sage-n-sour-hybrid.webp",
    name: "Sage N Sour",
    aka: "S.A.G.E. x Sour Diesel",
    bank: "TH Seeds",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 470, yieldOutdoor: 650,
    floweringDays: 70, rating: 4.9, reviewsCount: 560,
    genetics: "S.A.G.E. x Sour Diesel",
    origin: "Nueva York / Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 30, caryophyllene: 20 },
    flavors: ["Salvia y Diesel", "Limón Ácido", "Combustible Aromático"],
    effects: ["Estimulación Cerebral Máxima", "Energía Explosiva", "Creatividad Desbordada"],
    activities: ["creativity", "workout", "social", "nature_walk"],
    description: "Sage N Sour es la cepa más energética de TH Seeds. S.A.G.E. cruzada con Sour Diesel creando una Sativa de psicoactividad cerebral explosiva. Aroma brutal a diésel con fondo de salvia aromática. El combustible definitivo para artistas, músicos y creadores.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #FBBF24 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-wappa",
    image: "img/paradise-wappa-flower-v2-hd.webp",
    name: "Wappa",
    aka: "Big Bud Secret",
    bank: "Paradise Seeds",
    species: "Indica",
    thc: 19,
    cbd: 0.3,
    yieldIndoor: "500–600 g/m²",
    yieldOutdoor: "700–900 g/planta",
    floweringDays: 56,
    rating: 4.7,
    reviewsCount: 1240,
    genetics: "Indica Selección Norteamericana",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, linalool: 25 },
    flavors: ["Fresa y Cereza", "Frutal Fresco", "Dulce Terroso"],
    effects: ["Relajación Profunda", "Euforia Suave", "Cuerpo en Calma"],
    activities: ["relaxation", "evening_chill", "creativity"],
    description: "Wappa es una de las cepas más queridas de Paradise Seeds. Índica híbrida galardonada internacionalmente, destacada por su facilidad de cultivo, cosechas generosas y sabor frutal inconfundible a fresa y cereza. Sus terpenos dominantes (Mirceno, Cariofileno, Linalool) crean un efecto cálido y envolvente que relaja sin deprimir. Ideal tanto para principiantes como para cultivadores expertos que buscan resultados consistentes.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #F97316 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-sensi-star",
    image: "img/paradise-sensi-star-flower-v2-hd.webp",
    name: "Sensi Star",
    aka: "Star of Sensi",
    bank: "Paradise Seeds",
    species: "Indica",
    thc: 22,
    cbd: 0.2,
    yieldIndoor: "400–500 g/m²",
    yieldOutdoor: "600–700 g/planta",
    floweringDays: 60,
    rating: 4.8,
    reviewsCount: 980,
    genetics: "Indica Pura Selección",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, pinene: 30, caryophyllene: 20 },
    flavors: ["Pino Resinoso", "Tierra Oscura", "Hash Afganistán"],
    effects: ["Stone Poderoso", "Relajación Total", "Sedación Nocturna"],
    activities: ["relaxation", "sleep", "meditation"],
    description: "Sensi Star es la cepa insignia de Paradise Seeds, múltiple ganadora en la Cannabis Cup. Índica pura de potencia excepcional con THC de hasta 22%, capaz de proporcionar uno de los stones más completos del mercado. Resina espectacular y aroma a pino con profundos matices a tierra y hash. Considerada referencia absoluta entre las índicas premium de Ámsterdam.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #1E3A8A 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-atomical-haze",
    image: "img/paradise-atomical-haze-flower-hd.webp",
    name: "Atomical Haze",
    aka: "White Widow x Amnesia",
    bank: "Paradise Seeds",
    species: "Sativa",
    thc: 21,
    cbd: 0.2,
    yieldIndoor: "450 g/m²",
    yieldOutdoor: "800 g/planta",
    floweringDays: 63,
    rating: 4.6,
    reviewsCount: 712,
    genetics: "White Widow x Amnesia Haze",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, terpinolene: 35, myrcene: 20 },
    flavors: ["Cítrico Explosivo", "Haze Clásico", "Limón y Hierba"],
    effects: ["Alto Cerebral Duradero", "Motivación y Energía", "Creatividad Elevada"],
    activities: ["creativity", "workout", "social", "nature_walk"],
    description: "Atomical Haze es la sativa de referencia de Paradise Seeds. Cruce de White Widow y Amnesia Haze que produce una experiencia cerebral de larga duración con notas cítricas y haze inconfundibles. Con un alto calyx-to-leaf ratio, sus cogollos son grandes y resinosos. THC superior al 20% con cosechas de hasta 800 g por planta en exterior. La opción definitiva para los amantes de las sativas energéticas.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-durga-mata",
    image: "img/paradise-durga-mata-flower-hd.webp",
    name: "Durga Mata",
    aka: "Landrace Indica Original",
    bank: "Paradise Seeds",
    species: "Indica",
    thc: 18,
    cbd: 0.5,
    yieldIndoor: "400–500 g/m²",
    yieldOutdoor: "550–650 g/planta",
    floweringDays: 56,
    rating: 4.5,
    reviewsCount: 630,
    genetics: "Indica Landrace Asiática Selección Paradise",
    origin: "Subcontinente Índico vía Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, caryophyllene: 25, linalool: 20 },
    flavors: ["Terroso Profundo", "Especias Orientales", "Hash Suave"],
    effects: ["Calma Mental Profunda", "Cuerpo Sedado", "Meditación"],
    activities: ["relaxation", "sleep", "meditation"],
    description: "Durga Mata está inspirada en las legendarias landraces del subcontinente índico. Esta índica pura de Paradise Seeds destaca por su carácter calmante y meditativo, valorada especialmente por usuarios medicinales. Su floración rápida de 8 semanas y sus efectos sedantes la convierten en una elección clásica para quienes buscan relajación total y descanso nocturno profundo.",
    visualColor: "linear-gradient(135deg, #92400E 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(146,64,14,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-space-cookies",
    image: "img/paradise-space-cookies-flower-hd.webp",
    name: "Space Cookies",
    aka: "Girl Scout Cookies x OG Kush Selection",
    bank: "Paradise Seeds",
    species: "Hibrida",
    thc: 20,
    cbd: 0.3,
    yieldIndoor: "500–600 g/m²",
    yieldOutdoor: "1000 g/planta",
    floweringDays: 63,
    rating: 4.7,
    reviewsCount: 845,
    genetics: "Girl Scout Cookies x OG Kush",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, myrcene: 25 },
    flavors: ["Pino y Combustible", "Galleta y Cookie", "Dulce Resinoso"],
    effects: ["Euforia Elevada", "Relajación Física", "Bienestar General"],
    activities: ["relaxation", "creativity", "social", "evening_chill"],
    description: "Space Cookies es la versión Paradise Seeds de la legendaria genética Cookie californiana. Híbrida 60/40 con predominio índica, más de 20% THC y cogollos de una densidad excepcional. Notas de pino, combustible y galleta dulce. Cosechas masivas de hasta 1000 g por planta en exterior. Una de las cepas más productivas y potentes del catálogo de Paradise.",
    visualColor: "linear-gradient(135deg, #6366F1 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(99,102,241,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-slipstream",
    image: "img/paradise-slipstream-flower-hd.webp",
    name: "Slipstream",
    aka: "OG Kush x Zkittlez",
    bank: "Paradise Seeds",
    species: "Hibrida",
    thc: 23,
    cbd: 0.2,
    yieldIndoor: "500–600 g/m²",
    yieldOutdoor: "800–1000 g/planta",
    floweringDays: 63,
    rating: 4.8,
    reviewsCount: 520,
    genetics: "OG Kush x Zkittlez",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, caryophyllene: 35, myrcene: 20 },
    flavors: ["Frutas Tropicales", "OG Fuel", "Caramelo Cítrico"],
    effects: ["Potencia Elevada", "Euforia Intensa", "Relajación Progresiva"],
    activities: ["creativity", "social", "relaxation"],
    description: "Slipstream es una de las incorporaciones más recientes y emocionantes de Paradise Seeds. El cruce de OG Kush con Zkittlez produce una híbrida de potencia excepcional (23% THC) con un perfil terpénico dominado por el limoneno que aporta notas tropicales y cítricas sobre una base OG profunda. Producción generosa y cogollos densos y resinosos.",
    visualColor: "linear-gradient(135deg, #0EA5E9 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-sunset-paradise",
    image: "img/paradise-sunset-paradise-flower-hd.webp",
    name: "Sunset Paradise",
    aka: "Zkittlez x Gelato Selection",
    bank: "Paradise Seeds",
    species: "Hibrida",
    thc: 22,
    cbd: 0.2,
    yieldIndoor: "500 g/m²",
    yieldOutdoor: "800 g/planta",
    floweringDays: 63,
    rating: 4.7,
    reviewsCount: 390,
    genetics: "Zkittlez x Gelato Paradise Selection",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, myrcene: 30, linalool: 20 },
    flavors: ["Frutas del Trópico", "Helado de Limón", "Bayas Exóticas"],
    effects: ["Euforia Relajante", "Bienestar Alegre", "Creatividad Suave"],
    activities: ["social", "creativity", "relaxation", "evening_chill"],
    description: "Sunset Paradise captura los colores y sabores de un atardecer tropical. Cruce de Zkittlez con la selección Gelato de Paradise que produce cogollos multicolores llenos de tricomas. Sabor a frutas tropicales y bayas exóticas con un perfil limoneno que eleva el estado de ánimo. Una híbrida moderna diseñada para los amantes de los sabores afrutados y los efectos equilibrados.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-rainbow-road",
    image: "img/paradise-rainbow-road-flower-hd.webp",
    name: "Rainbow Road",
    aka: "Tropical Fruits x Paradise Selection",
    bank: "Paradise Seeds",
    species: "Hibrida",
    thc: 21,
    cbd: 0.3,
    yieldIndoor: "450–550 g/m²",
    yieldOutdoor: "750 g/planta",
    floweringDays: 63,
    rating: 4.6,
    reviewsCount: 445,
    genetics: "Selección Frutal Paradise Seeds",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 40, limonene: 35, myrcene: 25 },
    flavors: ["Arcoíris Frutal", "Mango y Papaya", "Dulce Floral"],
    effects: ["Alegría Elevada", "Energía Positiva", "Creatividad Vibrante"],
    activities: ["social", "creativity", "nature_walk", "music"],
    description: "Rainbow Road es la apuesta de Paradise Seeds por los sabores más exóticos y las genéticas tropicales. Una híbrida colorida con cogollos que exhiben tonos púrpura, naranja y verde bajo sus gruesas capas de tricomas. Perfil terpénico dominado por terpinoleno y limoneno que evoca una canasta de frutas tropicales recién cortadas. Efectos alegres y creativos.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-mendocino-skunk",
    image: "img/paradise-mendocino-skunk-flower-hd.webp",
    name: "Mendocino Skunk",
    aka: "Skunk Californiana Mendocino County",
    bank: "Paradise Seeds",
    species: "Hibrida",
    thc: 18,
    cbd: 0.3,
    yieldIndoor: "400–500 g/m²",
    yieldOutdoor: "600–800 g/planta",
    floweringDays: 56,
    rating: 4.5,
    reviewsCount: 530,
    genetics: "Skunk California x Mendocino Selection",
    origin: "Mendocino County, California vía Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, terpinolene: 25 },
    flavors: ["Skunk Clásico", "Tierra Californiana", "Herbáceo Fresco"],
    effects: ["Euforia Funcional", "Alegría Social", "Relajación Moderada"],
    activities: ["social", "creativity", "workout", "nature_walk"],
    description: "Mendocino Skunk rinde homenaje a los legendarios cultivos de Mendocino County en California. Una skunk de carácter californiano con flores densas y perfumadas, floración rápida de 8 semanas y efectos equilibrados. El aroma skunk clásico con matices a tierra y hierba fresca es un viaje directo a los años dorados del cannabis californiano. Fácil de cultivar y muy gratificante.",
    visualColor: "linear-gradient(135deg, #065F46 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,95,70,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-stromboli-auto",
    image: "img/paradise-stromboli-auto-flower-hd.webp",
    name: "Stromboli Auto",
    aka: "Autoflowering Italian Selection",
    bank: "Paradise Seeds",
    species: "Indica",
    thc: 16,
    cbd: 0.4,
    yieldIndoor: "350–450 g/m²",
    yieldOutdoor: "200 g/planta",
    floweringDays: 63,
    rating: 4.4,
    reviewsCount: 310,
    genetics: "Indica Selección x Ruderalis Paradise",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, pinene: 20 },
    flavors: ["Tierra y Madera", "Especias Mediterráneas", "Hash Suave"],
    effects: ["Relajación Corporal", "Calma Mental", "Efecto Gradual"],
    activities: ["relaxation", "sleep", "evening_chill"],
    description: "Stromboli Auto es la apuesta de Paradise Seeds por el mercado autoflower con carácter índica. Inspirada en la robustez de las genéticas mediterráneas, esta autofloreciente produce cogollos compactos y resinosos en ciclos cortos de menos de 10 semanas desde la germinación. Ideal para cultivos de balcón o interior con espacio limitado. Efectos calmantes y graduales.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #6B7280 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-red-velvet-auto",
    image: "img/paradise-red-velvet-auto-flower-hd.webp",
    name: "Red Velvet Auto",
    aka: "Purple x Indica Auto Paradise",
    bank: "Paradise Seeds",
    species: "Indica",
    thc: 18,
    cbd: 0.3,
    yieldIndoor: "400–450 g/m²",
    yieldOutdoor: "250 g/planta",
    floweringDays: 63,
    rating: 4.5,
    reviewsCount: 275,
    genetics: "Purple Kush x Indica Auto Selección",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, myrcene: 35, linalool: 25 },
    flavors: ["Frutos Rojos", "Terciopelo Dulce", "Floral Especiado"],
    effects: ["Relajación Cromática", "Serenidad", "Bienestar Nocturno"],
    activities: ["relaxation", "sleep", "evening_chill", "meditation"],
    description: "Red Velvet Auto es una de las joyas autoflorecientes más visuales de Paradise Seeds. Sus cogollos adquieren tonos rojos y púrpura intensos al aproximarse la madurez, creando un espectáculo visual. El sabor a frutos rojos y terciopelo dulce coincide con su apariencia, y sus efectos índica profundos invitan a la calma y la serenidad. Una autofloreciente premium para coleccionistas.",
    visualColor: "linear-gradient(135deg, #DC2626 0%, #7C3AED 100%)",
    bgPattern: "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-dutch-dragon",
    image: "img/paradise-dutch-dragon-flower-hd.webp",
    name: "Dutch Dragon",
    aka: "Sativa Holandesa Clásica",
    bank: "Paradise Seeds",
    species: "Sativa",
    thc: 20,
    cbd: 0.2,
    yieldIndoor: "500–600 g/m²",
    yieldOutdoor: "900–1200 g/planta",
    floweringDays: 63,
    rating: 4.6,
    reviewsCount: 720,
    genetics: "Sativa Selección Holandesa Paradise",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 45, limonene: 35, pinene: 20 },
    flavors: ["Limón y Hierba Fresca", "Cítrico Florido", "Haze Suave"],
    effects: ["Alto Cerebral Activo", "Energía y Motivación", "Sociabilidad"],
    activities: ["social", "creativity", "workout", "nature_walk"],
    description: "Dutch Dragon es una de las sativas clásicas de Paradise Seeds, un homenaje a la tradición cannábica holandesa. Sativa de ciclo medio con cosechas masivas —hasta 1200 g por planta en exterior— y un alto cerebral limpio y energético. El aroma cítrico con matices a hierba fresca y haze suave representa la esencia del cannabis de calidad amstelodamense. Productiva, potente y clásica.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-californian-gold",
    image: "img/paradise-californian-gold-flower-hd.webp",
    name: "Californian Gold",
    aka: "Cali Gold Haze",
    bank: "Paradise Seeds",
    species: "Sativa",
    thc: 19,
    cbd: 0.2,
    yieldIndoor: "400–500 g/m²",
    yieldOutdoor: "700–900 g/planta",
    floweringDays: 70,
    rating: 4.5,
    reviewsCount: 490,
    genetics: "Sativa Californiana x Haze Selección Paradise",
    origin: "California vía Ámsterdam",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 30, pinene: 20 },
    flavors: ["Limón Dorado", "Haze Californiano", "Flores y Cítricos"],
    effects: ["Euforia Luminosa", "Creatividad Dorada", "Energía Pura"],
    activities: ["creativity", "social", "music", "nature_walk"],
    description: "Californian Gold captura el espíritu dorado de la cultura cannábica de California. Esta sativa de ciclo algo largo produce cogollos dorados y luminosos cubiertos de tricomas ambarinos. El aroma evoca los campos de limón y las flores silvestres californianas. Un alto cerebral eufórico y creativo que hace honor al estado dorado. La sativa californiana definitiva en formato europeo.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-opium",
    image: "img/paradise-opium-flower-hd.webp",
    name: "Opium",
    aka: "Indica Power Strain",
    bank: "Paradise Seeds",
    species: "Indica",
    thc: 21,
    cbd: 0.3,
    yieldIndoor: "500–600 g/m²",
    yieldOutdoor: "700–800 g/planta",
    floweringDays: 60,
    rating: 4.7,
    reviewsCount: 680,
    genetics: "Indica Profunda Selección Paradise",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, caryophyllene: 25, linalool: 20 },
    flavors: ["Hash Oriental", "Especias Profundas", "Tierra y Madera"],
    effects: ["Stone Profundo", "Euforia Narcótica", "Relajación Total"],
    activities: ["relaxation", "sleep", "meditation", "evening_chill"],
    description: "Opium de Paradise Seeds es una potente índica que vive a la altura de su legendario nombre. Con 21% de THC y una floración de solo 60 días, produce cogollos masivos y densos impregnados de resina. El aroma a hash oriental y especias profundas es irresistible. Sus efectos son envolventes y narcóticos, perfectos para el descanso nocturno o la meditación profunda. Una leyenda del catálogo Paradise.",
    visualColor: "linear-gradient(135deg, #1E3A8A 0%, #7C3AED 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,58,138,0.2) 0%, transparent 70%)"
  },
  {
id: "paradise-glowstarz",
    image: "img/paradise-glowstarz-flower-hd.webp",
    name: "Glowstarz",
    aka: "Tropicana Cookies x Runtz Paradise",
    bank: "Paradise Seeds",
    species: "Hibrida",
    thc: 22,
    cbd: 0.2,
    yieldIndoor: "500 g/m²",
    yieldOutdoor: "750 g/planta",
    floweringDays: 63,
    rating: 4.8,
    reviewsCount: 360,
    genetics: "Tropicana Cookies x Runtz Paradise Selection",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, linalool: 25 },
    flavors: ["Cítrico Tropical", "Cookie Afrutado", "Uva y Naranja"],
    effects: ["Euforia Brillante", "Creatividad Festiva", "Bienestar Elevado"],
    activities: ["social", "creativity", "music", "evening_chill"],
    description: "Glowstarz es la respuesta de Paradise Seeds a la revolución de las genéticas Cookies y Runtz. Cruce de Tropicana Cookies con la selección Runtz de Paradise que produce cogollos de colores festivos y un perfil terpénico dominado por cariofileno y limoneno. 22% THC con efectos eufóricos y brillantes que hacen honor a su nombre. Una de las cepas más demandadas del nuevo catálogo Paradise.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.25) 0%, transparent 70%)"
  },
  {
id: "nirvana-northern-light",
    image: "img/nirvana-northern-light-flower-hd.webp",
    name: "Northern Light",
    aka: "Original Afghan Selection",
    bank: "Nirvana Seeds",
    species: "Indica",
    thc: 20,
    cbd: 0.4,
    yieldIndoor: "450–550 g/m²",
    yieldOutdoor: "650–800 g/planta",
    floweringDays: 56,
    rating: 4.9,
    reviewsCount: 1680,
    genetics: "Afghani Landrace x Thai Sativa",
    origin: "Seattle, EE.UU. vía Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 55, caryophyllene: 25, pinene: 20 },
    flavors: ["Pino Silvestre", "Tierra Especiada", "Hash Dulce"],
    effects: ["Sedación Total", "Cuerpo Flotante", "Paz Nocturna"],
    activities: ["relaxation", "sleep", "meditation"],
    description: "Northern Light de Nirvana Seeds es una de las índicas más galardonadas e influyentes de la historia del cannabis. Creada originalmente en el noroeste del Pacífico estadounidense y perfeccionada en Ámsterdam. Desarrolla cogollos ultradensos cubiertos de resina con aroma dulce a pino y especias. Su colocón físico envolvente proporciona un descanso inigualable.",
    visualColor: "linear-gradient(135deg, #065F46 0%, #3B82F6 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,95,70,0.2) 0%, transparent 70%)"
  },
  {
id: "nirvana-gsc",
    image: "img/nirvana-gsc-flower-hd.webp",
    name: "Girl Scout Cookies",
    aka: "OG Kush x Durban Poison",
    bank: "Nirvana Seeds",
    species: "Hibrida",
    thc: 22,
    cbd: 0.2,
    yieldIndoor: "400–500 g/m²",
    yieldOutdoor: "650–750 g/planta",
    floweringDays: 63,
    rating: 4.8,
    reviewsCount: 1350,
    genetics: "OG Kush x Durban Poison",
    origin: "California, EE.UU. vía Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, myrcene: 20 },
    flavors: ["Galleta Horneada", "Mentol Dulce", "Tierra Kush"],
    effects: ["Euforia Calidad VIP", "Alegría Cerebral", "Relajación Corporal"],
    activities: ["social", "creativity", "music", "evening_chill"],
    description: "Girl Scout Cookies de Nirvana Seeds trae la célebre genética californiana al catálogo holandés. Cruce mítico de OG Kush con Durban Poison que destaca por sus tonos púrpuras y su aroma inconfundible a galletas recién horneadas con matices mentolados y terrosos. Ofrece una euforia cerebral feliz con un reconfortante bienestar físico.",
    visualColor: "linear-gradient(135deg, #D97706 0%, #7C3AED 100%)",
    bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "nirvana-og-kush",
    image: "img/nirvana-og-kush-flower-hd.webp",
    name: "OG Kush",
    aka: "Chemdawg x Lemon Thai x Hindu Kush",
    bank: "Nirvana Seeds",
    species: "Hibrida",
    thc: 23,
    cbd: 0.3,
    yieldIndoor: "400–500 g/m²",
    yieldOutdoor: "650–800 g/planta",
    floweringDays: 60,
    rating: 4.9,
    reviewsCount: 1940,
    genetics: "Chemdawg x Lemon Thai x Pakistani Hindu Kush",
    origin: "Florida/California, EE.UU. vía Ámsterdam",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Gasolina Combustible", "Limón Cítrico", "Pino Terroso"],
    effects: ["Golpe Eufórico Intenso", "Relajación Músculo-Profunda", "Bienestar Total"],
    activities: ["relaxation", "gaming", "music", "evening_chill"],
    description: "OG Kush de Nirvana Seeds es la espina dorsal de las genéticas modernas de la costa oeste estadounidense. Famosa por su perfil terpénico único cargado de notas a combustible, pino silvestre y limón agrio. Su efecto es potente, duradero y envolvente, combinando una estimulación mental eufórica con una profunda relajación corporal.",
    visualColor: "linear-gradient(135deg, #15803D 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)"
  },
  {
id: "nirvana-gelato",
    image: "img/nirvana-gelato-flower-hd.webp",
    name: "Gelato",
    aka: "Sunset Sherbet x Thin Mint GSC",
    bank: "Nirvana Seeds",
    species: "Hibrida",
    thc: 24,
    cbd: 0.1,
    yieldIndoor: "450–550 g/m²",
    yieldOutdoor: "700–850 g/planta",
    floweringDays: 60,
    rating: 4.9,
    reviewsCount: 1520,
    genetics: "Sunset Sherbet x Thin Mint Girl Scout Cookies",
    origin: "California, EE.UU. vía Ámsterdam",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 35, linalool: 20 },
    flavors: ["Helado de Cítricos", "Menta Dulce", "Bayas Silvestres"],
    effects: ["Euforia Elevarte", "Creatividad Brillante", "Paz Física"],
    activities: ["creativity", "social", "music", "workout"],
    description: "Gelato de Nirvana Seeds representa el pináculo de la crianza moderna afrutada. Cruce entre Sunset Sherbet y Thin Mint GSC que deslumbró al mundo entero por sus cogollos morados oscuros resplandecientes y su sabor a helado de bayas con menta dulce y cítricos. Con hasta un 24% de THC, brinda una experiencia eufórica, creativa y sumamente placentera.",
    visualColor: "linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%)",
    bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "nirvana-white-widow",
    image: "img/nirvana-white-widow-flower-hd.webp",
    name: "White Widow",
    aka: "Brazilian Sativa x South Indian Indica",
    bank: "Nirvana Seeds",
    species: "Hibrida",
    thc: 21,
    cbd: 0.3,
    yieldIndoor: "450–550 g/m²",
    yieldOutdoor: "700–850 g/planta",
    floweringDays: 56,
    rating: 4.9,
    reviewsCount: 2100,
    genetics: "Brazilian Sativa Landrace x South Indian Indica",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, pinene: 25 },
    flavors: ["Pino Especiado", "Tierra Fresca", "Pimienta Dulce"],
    effects: ["Ráfaga de Euforia", "Energía Social", "Relajación Equilibrada"],
    activities: ["social", "creativity", "gaming", "music"],
    description: "White Widow es la leyenda absoluta de los coffee shops holandeses de los años 90. Híbrida clásica nacida del cruce entre una landrace sativa brasileña y una índica del sur de la India. Célebre por su abrumadora producción de tricomas blancos que cubren cada flor como un manto de nieve. Su efecto es limpio, enérgico, social y corporalmente equilibrado.",
    visualColor: "linear-gradient(135deg, #64748B 0%, #10B981 100%)",
    bgPattern: "radial-gradient(circle, rgba(100,116,139,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-kosher-kush",
    image: "img/dna-kosher-kush.webp",
    name: "Kosher Kush",
    aka: "Reserva Privada OG Cut",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 25, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 63, rating: 4.9, reviewsCount: 3200,
    genetics: "The OG #18 x Reserva Privada Kosher Cut",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 35, limonene: 20 },
    flavors: ["Kush Terroso", "Incienso Sagrado", "Pino Profundo"],
    effects: ["Sedación Profunda", "Euforia Mística", "Alivio Físico Total"],
    activities: ["relax_sleep"],
    description: "La primera cepa en ganar tres Cannabis Cups de High Times consecutivamente. Kosher Kush es pura leyenda índica: un perfil aromático denso a Kush terroso con matices de incienso que envuelve al usuario en una relajación profunda e hipnótica. Favorita de pacientes medicinales.",
    visualColor: "linear-gradient(135deg, #6D28D9 0%, #1E3A5F 100%)",
    bgPattern: "radial-gradient(circle, rgba(109,40,217,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-tangie",
    image: "img/dna-tangie.webp",
    name: "Tangie",
    aka: "California Orange x Skunk",
    bank: "DNA Genetics",
    species: "Sativa",
    thc: 22, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 70, rating: 4.9, reviewsCount: 2800,
    genetics: "California Orange x Skunk #1",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, myrcene: 25, terpinolene: 20 },
    flavors: ["Mandarina Fresca", "Cítrico Intenso", "Naranja Dulce"],
    effects: ["Energía Creativa", "Euforia Solar", "Motivación Explosiva"],
    activities: ["creativity", "nature_walk", "social"],
    description: "Ganadora del Cannabis Cup 2013. Tangie es un renacer de la clásica Tangerine Dream con un perfil cítrico tan potente que cada cogollo huele a mandarina recién pelada. Efecto sativa puro: creativo, motivador e inspirador sin ansiedad.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #F97316 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-chocolope",
    image: "img/dna-chocolope.webp",
    name: "Chocolope",
    aka: "OG Chocolate Thai x Cannalope Haze",
    bank: "DNA Genetics",
    species: "Sativa",
    thc: 21, cbd: 0.2,
    yieldIndoor: 600, yieldOutdoor: 800,
    floweringDays: 65, rating: 4.8, reviewsCount: 2500,
    genetics: "OG Chocolate Thai x Cannalope Haze",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, myrcene: 35, limonene: 25 },
    flavors: ["Chocolate Negro", "Café Tostado", "Vainilla Especiada"],
    effects: ["Euforia Mental", "Creatividad Fluida", "Risa Contagiosa"],
    activities: ["creativity", "social", "music"],
    description: "Clásica sativa de DNA que regresó en 2024 tras diez años fuera del catálogo. Sabor inconfundible a chocolate amargo con matices de café y vainilla. Un subidón cerebral puro que inspira conversación, arte y buen humor sin pesadez corporal.",
    visualColor: "linear-gradient(135deg, #92400E 0%, #78350F 100%)",
    bgPattern: "radial-gradient(circle, rgba(146,64,14,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-la-confidential",
    image: "img/dna-la-confidential.webp",
    name: "LA Confidential",
    aka: "OG LA Affie x Afghani",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 23, cbd: 0.5,
    yieldIndoor: 450, yieldOutdoor: 550,
    floweringDays: 56, rating: 4.8, reviewsCount: 2600,
    genetics: "OG LA Affie x Afghani Indica",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, pinene: 30, caryophyllene: 20 },
    flavors: ["Pino Fresco", "Tierra Húmeda", "Skunk Dulce"],
    effects: ["Relajación Muscular", "Sueño Profundo", "Calma Mental"],
    activities: ["relax_sleep"],
    description: "Joya índica de la costa Oeste. Compacta, cristalina y brutalmente resinosa. Su aroma a pino fresco y tierra húmeda precede un efecto físico devastador que funde al usuario en el sofá. Referente medicinal para insomnio y dolor crónico.",
    visualColor: "linear-gradient(135deg, #1E3A5F 0%, #0F172A 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,58,95,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-holy-grail-kush",
    image: "img/dna-holy-grail-kush.webp",
    name: "Holy Grail Kush",
    aka: "Kosher Kush x The OG #18",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 24, cbd: 0.4,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 63, rating: 4.9, reviewsCount: 2100,
    genetics: "Kosher Kush x The OG #18",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, myrcene: 35, limonene: 25 },
    flavors: ["Kush Especiado", "Pimienta Negra", "Diesel Dulce"],
    effects: ["Euforia Sedante", "Alivio Corporal", "Bienestar Profundo"],
    activities: ["relax_sleep", "music"],
    description: "El Santo Grial de las índicas: un cruce entre las dos mejores genéticas de DNA. Combina la potencia demoledora de Kosher Kush con la estructura productiva de The OG #18. Ganadora de múltiples premios, ofrece un viaje de euforia que desemboca en relajación total.",
    visualColor: "linear-gradient(135deg, #D4AF37 0%, #92400E 100%)",
    bgPattern: "radial-gradient(circle, rgba(212,175,55,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-strawberry-banana",
    image: "img/dna-strawberry-banana.webp",
    name: "Strawberry Banana",
    aka: "Crockett's Banana Kush x Strawberry Bubble Gum",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 26, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 63, rating: 4.9, reviewsCount: 2900,
    genetics: "Banana Kush x Strawberry Bubble Gum",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "limonene",
    terpenes: { limonene: 40, caryophyllene: 30, myrcene: 30 },
    flavors: ["Fresa Dulce", "Plátano Maduro", "Caramelo Tropical"],
    effects: ["Euforia Intensa", "Relajación Dulce", "Creatividad Relajada"],
    activities: ["creativity", "music", "relax_sleep"],
    description: "Colaboración con Crockett Family Farms. Sabor postre irresistible a fresa y plátano con niveles de THC que superan el 26%. Cogollos densos, cubiertos de resina, con tonos morados. Efecto potente pero equilibrado entre mente y cuerpo.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #F59E0B 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-24k-gold",
    image: "img/dna-24k-gold.webp",
    name: "24K Gold",
    aka: "Kosher Kush x Tangie",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 22, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 1800,
    genetics: "Kosher Kush x Tangie",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "limonene",
    terpenes: { limonene: 45, caryophyllene: 30, myrcene: 25 },
    flavors: ["Cítrico Dorado", "Mandarina Kush", "Pimienta Dulce"],
    effects: ["Equilibrio Perfecto", "Creatividad Serena", "Relajación Activa"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Fusión dorada de dos leyendas: la potencia de Kosher Kush y el aroma cítrico explosivo de Tangie. El resultado es un híbrido equilibrado con sabor a mandarina con fondo Kush especiado. Efecto versátil: creativo y relajado sin aplastar.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D4AF37 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-lemon-skunk",
    image: "img/dna-lemon-skunk.webp",
    name: "Lemon Skunk",
    aka: "Citrus Skunk Selection",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 19, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 700,
    floweringDays: 58, rating: 4.7, reviewsCount: 2200,
    genetics: "Las Vegas Lemon Skunk x Lemon Skunk #2",
    origin: "Las Vegas, EE.UU.",
    dominantTerpene: "limonene",
    terpenes: { limonene: 55, pinene: 25, myrcene: 20 },
    flavors: ["Limón Ácido", "Skunk Cítrico", "Pomelo Dulce"],
    effects: ["Motivación Alegre", "Energía Suave", "Buen Humor"],
    activities: ["social", "nature_walk", "creativity"],
    description: "Un clásico atemporal con aroma a limón puro y fondo Skunk terroso. Seleccionada de dos fenotipo Lemon Skunk excepcionales, ofrece un efecto alegre y social perfecto para el día. Fácil de cultivar y muy generosa en producción.",
    visualColor: "linear-gradient(135deg, #FDE047 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(253,224,71,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-the-og-18",
    image: "img/dna-the-og-18.webp",
    name: "The OG #18",
    aka: "OG Kush Phenotype #18",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 24, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.8, reviewsCount: 1900,
    genetics: "OG Kush Phenotype #18",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, limonene: 30, caryophyllene: 25 },
    flavors: ["Diesel Limón", "Pino Kush", "Tierra Fresca"],
    effects: ["Relajación Profunda", "Euforia Cálida", "Calma Cerebral"],
    activities: ["relax_sleep", "music"],
    description: "El fenotipo número 18 de la legendaria OG Kush, seleccionado por DNA por su excepcional equilibrio entre potencia y producción. Aroma clásico a diesel con limón y pino. Estructura densa, resina abundante y un efecto potente que honra la genética OG original.",
    visualColor: "linear-gradient(135deg, #065F46 0%, #0F172A 100%)",
    bgPattern: "radial-gradient(circle, rgba(6,95,70,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-cataract-kush",
    image: "img/dna-cataract-kush.webp",
    name: "Cataract Kush",
    aka: "OG #18 x LA Confidential",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 23, cbd: 0.5,
    yieldIndoor: 475, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.7, reviewsCount: 1400,
    genetics: "The OG #18 x LA Confidential",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 50, caryophyllene: 30, linalool: 20 },
    flavors: ["Kush Cremoso", "Lavanda Terrosa", "Menta Suave"],
    effects: ["Alivio Ocular", "Sedación Profunda", "Tranquilidad Total"],
    activities: ["relax_sleep"],
    description: "Cruce entre dos pesos pesados índicos de DNA. Nombrada por su potente efecto sobre la presión ocular, es una favorita medicinal. Cogollos compactos con aroma cremoso a Kush con notas de lavanda. Efecto narcótico ideal para las últimas horas del día.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #1E3A5F 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-purple-wreck",
    image: "img/dna-purple-wreck.webp",
    name: "Purple Wreck",
    aka: "Purple Urkle x Trainwreck",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 20, cbd: 0.4,
    yieldIndoor: 450, yieldOutdoor: 600,
    floweringDays: 58, rating: 4.6, reviewsCount: 1200,
    genetics: "Purple Urkle x Trainwreck",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, linalool: 30, caryophyllene: 25 },
    flavors: ["Uva Dulce", "Bayas del Bosque", "Lavanda Afrutada"],
    effects: ["Relajación Frutal", "Sueño Sereno", "Alivio del Estrés"],
    activities: ["relax_sleep"],
    description: "Espectáculo visual de colores púrpura profundo. Purple Wreck combina la genética colorida de Purple Urkle con la potencia de Trainwreck. Sabor a uva y bayas con un efecto relajante que va aumentando hasta alcanzar un sueño profundo y reparador.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-sour-tangie",
    image: "img/dna-sour-tangie.webp",
    name: "Sour Tangie",
    aka: "Sour Diesel x Tangie",
    bank: "DNA Genetics",
    species: "Sativa",
    thc: 22, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 68, rating: 4.8, reviewsCount: 1900,
    genetics: "Sour Diesel x Tangie",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "limonene",
    terpenes: { limonene: 50, terpinolene: 25, caryophyllene: 25 },
    flavors: ["Diesel Cítrico", "Mandarina Ácida", "Naranja Combustible"],
    effects: ["Energía Explosiva", "Creatividad Ácida", "Foco Sativa"],
    activities: ["creativity", "nature_walk", "social"],
    description: "La fusión perfecta entre el diesel crudo de Sour Diesel y los cítricos vibrantes de Tangie. Ganadora del Cannabis Cup 2015. Aroma diesel-mandarina adictivo y efecto sativa estimulante que enciende la creatividad sin provocar ansiedad.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #84CC16 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-sorbet",
    image: "img/dna-sorbet.webp",
    name: "Sorbet",
    aka: "Sunset Sherbet Selection",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 21, cbd: 0.2,
    yieldIndoor: 475, yieldOutdoor: 600,
    floweringDays: 60, rating: 4.7, reviewsCount: 1500,
    genetics: "Sunset Sherbet x Special Selection",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, limonene: 35, linalool: 25 },
    flavors: ["Helado de Bayas", "Lima Dulce", "Crema de Vainilla"],
    effects: ["Relajación Cremosa", "Euforia Suave", "Paz Interior"],
    activities: ["relax_sleep", "music"],
    description: "Selección premium de Sunset Sherbet por DNA Genetics. Perfil de sabor que recuerda a un helado artesanal de bayas con lima y crema. Efecto indica relajante con una capa sutil de euforia mental. Cogollos densos teñidos de violeta y naranja.",
    visualColor: "linear-gradient(135deg, #EC4899 0%, #A78BFA 100%)",
    bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-sleestack",
    image: "img/dna-sleestack.webp",
    name: "Sleestack",
    aka: "SSH x Martian Mean Green",
    bank: "DNA Genetics",
    species: "Sativa",
    thc: 20, cbd: 0.3,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 70, rating: 4.7, reviewsCount: 1100,
    genetics: "Super Silver Haze x Martian Mean Green",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 40, limonene: 30, pinene: 30 },
    flavors: ["Haze Clásico", "Menta Tropical", "Pino Fresco"],
    effects: ["Lucidez Sativa", "Energía Sostenida", "Foco Creativo"],
    activities: ["creativity", "nature_walk", "social"],
    description: "Sativa alienígena nacida de Super Silver Haze y Martian Mean Green. Estructura alta y elegante con un aroma haze penetrante. Efecto sativa de larga duración que mantiene la mente afilada y el cuerpo ligero. Ideal para excursiones y proyectos creativos.",
    visualColor: "linear-gradient(135deg, #84CC16 0%, #06B6D4 100%)",
    bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-cannalope-haze",
    image: "img/dna-cannalope-haze.webp",
    name: "Cannalope Haze",
    aka: "Haze Brothers x Mexican Sativa",
    bank: "DNA Genetics",
    species: "Sativa",
    thc: 19, cbd: 0.3,
    yieldIndoor: 500, yieldOutdoor: 700,
    floweringDays: 65, rating: 4.6, reviewsCount: 1300,
    genetics: "Haze Brothers x Mexican Sativa",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "ocimene",
    terpenes: { ocimene: 40, limonene: 30, myrcene: 30 },
    flavors: ["Melón Tropical", "Mango Dulce", "Haze Afrutado"],
    effects: ["Alegría Tropical", "Energía Matutina", "Mente Despejada"],
    activities: ["nature_walk", "social", "creativity"],
    description: "Una de las primeras creaciones de DNA y madre de Chocolope. Aroma dulce a melón y mango que transporta al trópico. Efecto sativa limpio y energizante, perfecto para empezar el día con motivación. Cultivar fácil con excelente producción.",
    visualColor: "linear-gradient(135deg, #F97316 0%, #34D399 100%)",
    bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-rp43",
    image: "img/dna-rp43.webp",
    name: "RP43 (Richard Petty)",
    aka: "Exclusive Hybrid",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 25, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.8, reviewsCount: 900,
    genetics: "Propietaria DNA (Hybrid Select)",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, limonene: 30, myrcene: 25 },
    flavors: ["Gas Penetrante", "Pimienta Negra", "Cítrico Sutil"],
    effects: ["Potencia Extrema", "Relajación Profunda", "Euforia Pesada"],
    activities: ["relax_sleep", "music"],
    description: "Variedad exclusiva de DNA Genetics nombrada en honor al piloto de NASCAR Richard Petty por su número #43. Genética propietaria de alto octanaje con un perfil gaseoso y picante. Efecto contundente para usuarios experimentados que buscan máxima potencia.",
    visualColor: "linear-gradient(135deg, #1E40AF 0%, #EF4444 100%)",
    bgPattern: "radial-gradient(circle, rgba(30,64,175,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-gmo-kosher",
    image: "img/dna-gmo-kosher.webp",
    name: "GMO Kosher",
    aka: "GMO x Kosher Kush",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 27, cbd: 0.1,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 65, rating: 4.9, reviewsCount: 800,
    genetics: "GMO (Garlic Cookies) x Kosher Kush",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 45, myrcene: 35, limonene: 20 },
    flavors: ["Ajo Tostado", "Kush Diesel", "Umami Terroso"],
    effects: ["Sedación Extrema", "Alivio Total", "Narcosis Nocturna"],
    activities: ["relax_sleep"],
    description: "Novedad 2024: el cruce entre la pungente GMO (Garlic Cookies) y la legendaria Kosher Kush. Perfil aromático umami intenso con ajo tostado y diesel. Potencia demoledora que supera el 27% THC. Solo para fumadores experimentados. Ideal para combatir insomnio severo.",
    visualColor: "linear-gradient(135deg, #4C1D95 0%, #065F46 100%)",
    bgPattern: "radial-gradient(circle, rgba(76,29,149,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-3peat",
    image: "img/dna-3peat.webp",
    name: "3peat",
    aka: "Holy Grail Kush x Kosher Kush x RP43",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 26, cbd: 0.2,
    yieldIndoor: 525, yieldOutdoor: 675,
    floweringDays: 63, rating: 4.8, reviewsCount: 650,
    genetics: "Holy Grail Kush x Kosher Kush x RP43",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, caryophyllene: 30, limonene: 25 },
    flavors: ["Triple Kush", "Diesel Sagrado", "Especias Oscuras"],
    effects: ["Triple Sedación", "Euforia Mística", "Fundición Total"],
    activities: ["relax_sleep"],
    description: "Novedad 2024: Triple amenaza que combina tres leyendas de DNA en una. Holy Grail Kush, Kosher Kush y RP43 convergen en un indica de potencia extrema. Nombrada '3peat' por la triple victoria que representa. Aroma Kush puro con capas de diesel y especias.",
    visualColor: "linear-gradient(135deg, #D4AF37 0%, #4C1D95 100%)",
    bgPattern: "radial-gradient(circle, rgba(212,175,55,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-purple-kosher",
    image: "img/dna-purple-kosher.webp",
    name: "Purple Kosher",
    aka: "Purple Genetics x Kosher Kush",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 24, cbd: 0.3,
    yieldIndoor: 475, yieldOutdoor: 625,
    floweringDays: 63, rating: 4.8, reviewsCount: 750,
    genetics: "Purple Phenotype x Kosher Kush",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "linalool",
    terpenes: { linalool: 40, myrcene: 35, caryophyllene: 25 },
    flavors: ["Uva Kush", "Lavanda Oscura", "Incienso Púrpura"],
    effects: ["Relajación Morada", "Sueño Profundo", "Calma Sensorial"],
    activities: ["relax_sleep"],
    description: "La versión púrpura de la legendaria Kosher Kush. Cogollos de un violeta profundo cubiertos de tricomas blancos. Aroma floral a lavanda y uva con fondo Kush terroso. Efecto indica nocturno perfecto para cerrar el día con tranquilidad absoluta.",
    visualColor: "linear-gradient(135deg, #7C3AED 0%, #DB2777 100%)",
    bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-honey-beez",
    image: "img/dna-honey-beez.webp",
    name: "Honey Beez",
    aka: "Exclusive Honey Hybrid",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 60, rating: 4.7, reviewsCount: 700,
    genetics: "Propietaria DNA (Honey Phenotype)",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 40, limonene: 35, ocimene: 25 },
    flavors: ["Miel Dorada", "Flores Silvestres", "Dulce Tropical"],
    effects: ["Dulzura Relajante", "Bienestar Cálido", "Tranquilidad Alegre"],
    activities: ["social", "relax_sleep", "music"],
    description: "Variedad exclusiva con un perfil de miel y flores silvestres único. Cogollos dorados cubiertos de resina que brillan como gotas de ámbar. Efecto híbrido cálido y acogedor, perfecto para tardes tranquilas en buena compañía.",
    visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
    bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-guavanade",
    image: "img/dna-guavanade.webp",
    name: "Guavanade",
    aka: "Guava x Lemonade",
    bank: "DNA Genetics",
    species: "Sativa",
    thc: 22, cbd: 0.2,
    yieldIndoor: 475, yieldOutdoor: 600,
    floweringDays: 65, rating: 4.7, reviewsCount: 600,
    genetics: "Guava x Lemonade",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "terpinolene",
    terpenes: { terpinolene: 40, limonene: 35, ocimene: 25 },
    flavors: ["Guayaba Tropical", "Limonada Rosa", "Fruta Exótica"],
    effects: ["Frescura Tropical", "Energía Frutal", "Creatividad Vibrante"],
    activities: ["creativity", "social", "nature_walk"],
    description: "Explosión de sabor tropical que fusiona guayaba dulce con limonada refrescante. Sativa moderna de DNA para 2024 con un perfil terpénico vibrante y efecto energizante y alegre. Perfecta para días soleados y actividades al aire libre.",
    visualColor: "linear-gradient(135deg, #34D399 0%, #F472B6 100%)",
    bgPattern: "radial-gradient(circle, rgba(52,211,153,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-gaz-money",
    image: "img/dna-gaz-money.webp",
    name: "Gaz Money",
    aka: "Gas Phenotype Selection",
    bank: "DNA Genetics",
    species: "Indica",
    thc: 25, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 625,
    floweringDays: 60, rating: 4.8, reviewsCount: 550,
    genetics: "Propietaria DNA (Gas Dominant)",
    origin: "Los Ángeles, EE.UU.",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 50, myrcene: 30, limonene: 20 },
    flavors: ["Gasolina Premium", "Pimienta Ahumada", "Caucho Dulce"],
    effects: ["Potencia Gaseosa", "Sedación Rápida", "Alivio Físico"],
    activities: ["relax_sleep"],
    description: "Cepa de perfil 'gas' puro de DNA Genetics. Aroma penetrante a combustible con notas de pimienta ahumada. Efecto indica directo y contundente que golpea rápido y funde profundo. Para amantes del perfil gaseoso y la potencia sin concesiones.",
    visualColor: "linear-gradient(135deg, #374151 0%, #065F46 100%)",
    bgPattern: "radial-gradient(circle, rgba(55,65,81,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-choco-mintz",
    image: "img/dna-choco-mintz.webp",
    name: "Choco Mintz",
    aka: "Chocolope x Kush Mints",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 23, cbd: 0.2,
    yieldIndoor: 500, yieldOutdoor: 650,
    floweringDays: 62, rating: 4.8, reviewsCount: 500,
    genetics: "Chocolope x Kush Mints",
    origin: "Ámsterdam, Países Bajos",
    dominantTerpene: "caryophyllene",
    terpenes: { caryophyllene: 40, myrcene: 30, limonene: 30 },
    flavors: ["Chocolate con Menta", "Brownie Helado", "Cacao Especiado"],
    effects: ["Euforia Golosa", "Creatividad Mentolada", "Relajación Dulce"],
    activities: ["creativity", "social", "music"],
    description: "Fusión gourmet de la icónica Chocolope con la cremosa Kush Mints. Sabor a brownie de chocolate con menta fresca que convierte cada calada en un postre. Efecto híbrido equilibrado: activa la mente con dulzura y relaja el cuerpo sin anestesiar.",
    visualColor: "linear-gradient(135deg, #78350F 0%, #34D399 100%)",
    bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  },
  {
id: "dna-blue-dream",
    image: "img/dna-blue-dream-official.webp",
    name: "Blue Dream",
    aka: "Blueberry x Super Silver Haze",
    bank: "DNA Genetics",
    species: "Hibrida",
    thc: 21, cbd: 0.2,
    yieldIndoor: 550, yieldOutdoor: 750,
    floweringDays: 65, rating: 4.8, reviewsCount: 2400,
    genetics: "Blueberry x Super Silver Haze",
    origin: "California, EE.UU.",
    dominantTerpene: "myrcene",
    terpenes: { myrcene: 45, pinene: 30, caryophyllene: 25 },
    flavors: ["Arándano Dulce", "Baya Azul", "Haze Cremoso"],
    effects: ["Equilibrio Soñador", "Creatividad Suave", "Relajación Mental"],
    activities: ["creativity", "social", "nature_walk", "music"],
    description: "El sueño azul de California en la versión DNA. Cruce entre Blueberry y Super Silver Haze que entrega un híbrido equilibrado con sabor a arándano cremoso. Efecto suave y versátil que relaja sin inmovilizar y motiva sin acelerar. La cepa más vendida en California.",
    visualColor: "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)",
    bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-bubblegum",
    image: "img/ths-bubblegum.webp",
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
    image: "img/ths-french-cookies.webp",
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
    image: "img/ths-chocolate-chunk.webp",
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
  },
  {
id: "wls-white-widow",
      image: "img/wls-white-widow.webp",
      name: "White Widow",
      aka: "Original White Widow",
      bank: "White Label Seed Co.",
      species: "Hibrida",
      thc: 21,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 55,
      rating: 4.8,
      reviewsCount: 2100,
      genetics: "Brazilian Sativa x South Indian Indica",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          pinene: 25
      },
      flavors: [
          "Pino Resinoso",
          "Especias Terrosas",
          "Madera de Cedro"
      ],
      effects: [
          "Euforia Cerebral",
          "Relajación Corporal",
          "Energía Social"
      ],
      activities: [
          "social",
          "creativity",
          "nature_walk"
      ],
      description: "La legendaria White Widow en la versión oficial de White Label Seed Co. Famosa mundialmente por su densa manta de cristales blancos de resina y su aroma a pino fresco y tierra especiada. Efecto eufórico y equilibrado.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-snow-white",
      image: "img/wls-snow-white.webp",
      name: "Snow White",
      aka: "Pure Power Plant x White Widow",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 22,
      cbd: 0.3,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 56,
      rating: 4.7,
      reviewsCount: 1150,
      genetics: "Pure Power Plant x White Widow",
      origin: "Países Bajos",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 40,
          myrcene: 35,
          limonene: 25
      },
      flavors: [
          "Tierra Dulce",
          "Cítrico Suave",
          "Madera Tropical"
      ],
      effects: [
          "Sedación Física",
          "Calma Mental",
          "Bienestar Profundo"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Variedad blanca de alto rendimiento que combina la estructura compacta de PPP con la resina nevada de White Widow. Sabor dulce con toques cítricos y terrosos, ideal para la relajación nocturna.",
      visualColor: "linear-gradient(135deg, #F8FAFC 0%, #64748B 100%)",
      bgPattern: "radial-gradient(circle, rgba(248,250,252,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-white-skunk",
      image: "img/wls-white-skunk.webp",
      name: "White Skunk",
      aka: "White Widow x Skunk #1",
      bank: "White Label Seed Co.",
      species: "Hibrida",
      thc: 20,
      cbd: 0.5,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 50,
      rating: 4.6,
      reviewsCount: 980,
      genetics: "White Widow x Skunk #1",
      origin: "Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Naranja Licoresca",
          "Skunk Penetrante",
          "Especias Cítricas"
      ],
      effects: [
          "Alegría Radiante",
          "Euforia Suave",
          "Relax Muscular"
      ],
      activities: [
          "social",
          "gaming",
          "music"
      ],
      description: "Una de las cepas más fáciles de cultivar del catálogo de White Label. Cruce de Skunk #1 con resina blanca que ofrece un sabor sorprendente a licor de naranja y humo suave y risueño.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #10B981 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-white-ice",
      image: "img/wls-white-ice.webp",
      name: "White Ice",
      aka: "Indica Crystal Extreme (ICE)",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 22,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 50,
      rating: 4.7,
      reviewsCount: 890,
      genetics: "Northern Lights x Dutch Skunk x Afghani Hash Plant",
      origin: "Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          pinene: 25,
          caryophyllene: 25
      },
      flavors: [
          "Pino Helado",
          "Hachís Meloso",
          "Tierra Especiada"
      ],
      effects: [
          "Efecto Hielo (Couch-Lock)",
          "Sedación Muscular",
          "Paz Mental"
      ],
      activities: [
          "relax_sleep"
      ],
      description: "Conocida como Indica Crystal Extreme. Híbrido afgano de floración ultrarrápida cubierto por una costra densa de resina brillante que parece nieve congelada. Efecto pesado y profundamente sedante.",
      visualColor: "linear-gradient(135deg, #0EA5E9 0%, #1E293B 100%)",
      bgPattern: "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-white-diesel",
      image: "img/wls-white-diesel.webp",
      name: "White Diesel",
      aka: "NYC Diesel x White Widow",
      bank: "White Label Seed Co.",
      species: "Hibrida",
      thc: 21,
      cbd: 0.3,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 60,
      rating: 4.7,
      reviewsCount: 760,
      genetics: "NYC Diesel x White Widow",
      origin: "Nueva York / Ámsterdam",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 40,
          caryophyllene: 35,
          myrcene: 25
      },
      flavors: [
          "Gasolina Cítrica",
          "Pomelo Amargo",
          "Limón Químico"
      ],
      effects: [
          "Energía Estimulante",
          "Euforia Creativa",
          "Claridad Mental"
      ],
      activities: [
          "creativity",
          "social",
          "gaming"
      ],
      description: "Híbrido de gran personalidad que une los potentes matices diésel y pomelo de NYC Diesel con la abundante cobertura de resina de la línea White. Sabor penetrante y subidón energizante.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #065F46 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-double-gum",
      image: "img/wls-double-gum.webp",
      name: "Double Gum",
      aka: "Double Bubblegum Selection",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 19,
      cbd: 0.4,
      yieldIndoor: 450,
      yieldOutdoor: 500,
      floweringDays: 48,
      rating: 4.6,
      reviewsCount: 650,
      genetics: "Indiana Bubblegum Inbred Selection",
      origin: "Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          limonene: 25
      },
      flavors: [
          "Chicle de Fresa",
          "Caramelo Rosa",
          "Dulzura Afrutada"
      ],
      effects: [
          "Relajación Dulce",
          "Euforia Alegre",
          "Calma Corporal"
      ],
      activities: [
          "social",
          "music",
          "relax_sleep"
      ],
      description: "Selección compacta e indica de la clásica Bubblegum. Floración súper corta de menos de 50 días y un aroma intenso a chicle dulce rosa que inunda el espacio de cultivo.",
      visualColor: "linear-gradient(135deg, #F43F5E 0%, #BE123C 100%)",
      bgPattern: "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-pure-power-plant",
      image: "img/wls-pure-power-plant.webp",
      name: "Pure Power Plant (PPP)",
      aka: "PPP White Label",
      bank: "White Label Seed Co.",
      species: "Hibrida",
      thc: 22,
      cbd: 0.2,
      yieldIndoor: 600,
      yieldOutdoor: 750,
      floweringDays: 55,
      rating: 4.8,
      reviewsCount: 1850,
      genetics: "South African Sativa x USA Indica",
      origin: "Sudáfrica / Países Bajos",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 40,
          myrcene: 30,
          caryophyllene: 30
      },
      flavors: [
          "Pino Picante",
          "Vainilla Dulce",
          "Tierra Especiada"
      ],
      effects: [
          "Potencia Eléctrica",
          "Euforia Masiva",
          "Energía Duradera"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "La legendaria Pure Power Plant (PPP) en la versión de White Label. Productora masiva de cogollos duros como rocas con un potente aroma especiado a pino y vainilla y un subidón eufórico muy apreciado en los coffee shops holandeses.",
      visualColor: "linear-gradient(135deg, #22C55E 0%, #15803D 100%)",
      bgPattern: "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-master-kush",
      image: "img/wls-master-kush-official.webp",
      name: "Master Kush",
      aka: "High Hindu Kush Selection",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 20,
      cbd: 0.6,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 50,
      rating: 4.7,
      reviewsCount: 1420,
      genetics: "Hindu Kush x Skunk #1",
      origin: "Afganistán / Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          pinene: 25
      },
      flavors: [
          "Hachís Charas",
          "Tierra Dulce",
          "Incienso de Pino"
      ],
      effects: [
          "Relax Físico Clásico",
          "Serenidad Mental",
          "Alivio del Estrés"
      ],
      activities: [
          "relax_sleep",
          "nature_walk"
      ],
      description: "Doble ganadora de la Cannabis Cup. Híbrido de Hindu Kush que conserva el aroma tradicional a hachís artesanal charas con toques sutiles de tierra y pino. Humo suave e indica refinada.",
      visualColor: "linear-gradient(135deg, #A855F7 0%, #3B0764 100%)",
      bgPattern: "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-orange-bud",
      image: "img/wls-orange-bud.webp",
      name: "Orange Bud",
      aka: "100% Skunk Selection",
      bank: "White Label Seed Co.",
      species: "Sativa",
      thc: 19,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 55,
      rating: 4.7,
      reviewsCount: 1300,
      genetics: "Select Skunk Phenotype",
      origin: "California / Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 35,
          caryophyllene: 20
      },
      flavors: [
          "Naranja Fresca",
          "Piel de Cítrico",
          "Dulzor Skunk"
      ],
      effects: [
          "Energía Estimulante",
          "Euforia Creativa",
          "Sensación Social"
      ],
      activities: [
          "social",
          "creativity",
          "nature_walk"
      ],
      description: "Selección de Skunk 100% pura famosa por sus abundantes pelos de color naranja intenso y su delicioso aroma a naranjas maduras. Subidón sativa activo y cerebral.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-afghani-1",
      image: "img/wls-afghani-1-official.webp",
      name: "Afghani #1",
      aka: "Pure Afghan Hash Plant",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 20,
      cbd: 0.8,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 45,
      rating: 4.6,
      reviewsCount: 940,
      genetics: "Afghani Landrace Inbred Line",
      origin: "Afganistán",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 55,
          caryophyllene: 25,
          pinene: 20
      },
      flavors: [
          "Hachís Especiado",
          "Tierra Profunda",
          "Pimienta Dulce"
      ],
      effects: [
          "Sedación Muscular",
          "Pesadez Física",
          "Sueño Profundo"
      ],
      activities: [
          "relax_sleep"
      ],
      description: "Variedad indica pura originaria de las montañas de Afganistán. La planta de hachís por excelencia con hojas anchas, cálices voluminosos y un efecto narcótico tradicional.",
      visualColor: "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
      bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-french-macaron",
      image: "img/ths-french-macaron.webp",
      name: "French Macaron",
      aka: "Gelato 33 x French Cookies",
      bank: "TH Seeds",
      species: "Hibrida",
      thc: 24,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1450,
      genetics: "Gelato 33 x French Cookies",
      origin: "Ámsterdam / Francia",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          linalool: 25
      },
      flavors: [
          "Macaron Dulce",
          "Gasolina Cremosa",
          "Noche Francesa"
      ],
      effects: [
          "Euforia Sofisticada",
          "Relajación Dulce",
          "Bienestar Sensorial"
      ],
      activities: [
          "social",
          "music",
          "relax_sleep"
      ],
      description: "Una obra maestra premiada de T.H.Seeds. Cruce estelar entre Gelato 33 y French Cookies. Ofrece un perfil cremoso y dulce a repostería francesa con matices gaseosos. Cogollos morados oscuros y resinosos de potencia extraordinaria.",
      visualColor: "linear-gradient(135deg, #6B21A8 0%, #1E1B4B 100%)",
      bgPattern: "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-banana-candy-krush",
      image: "img/ths-banana-candy-krush.webp",
      name: "Banana Candy Krush",
      aka: "Banana Cake x Kush Mints",
      bank: "TH Seeds",
      species: "Hibrida",
      thc: 25,
      cbd: 0.1,
      yieldIndoor: 600,
      yieldOutdoor: 700,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 980,
      genetics: "Banana Cake x Kush Mints",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 40,
          myrcene: 35,
          caryophyllene: 25
      },
      flavors: [
          "Plátano Dulce",
          "Caramelo de Plátano",
          "Menta Cremosa"
      ],
      effects: [
          "Euforia Potente",
          "Relajación Dulce",
          "Felicidad Creativa"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "Explosión de sabor a caramelo de plátano cremoso producido por la fusión de Banana Cake y Kush Mints. Produce flores ultra resinosas ideales para extracciones de rosin de nivel competición.",
      visualColor: "linear-gradient(135deg, #F59E0B 0%, #78350F 100%)",
      bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-mont-blanc",
      image: "img/ths-mont-blanc.webp",
      name: "Mont Blanc",
      aka: "French Cookies x Birthday Cake x Strawbanana Cream",
      bank: "TH Seeds",
      species: "Hibrida",
      thc: 26,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1120,
      genetics: "French Cookies x Birthday Cake x Strawbanana Cream",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 40,
          myrcene: 35,
          limonene: 25
      },
      flavors: [
          "Vainilla Cremosa",
          "Fresa Glaseada",
          "Pastel de Cumpleaños"
      ],
      effects: [
          "Subidón Nevado",
          "Euforia Cerebral",
          "Relajación Profunda"
      ],
      activities: [
          "creativity",
          "relax_sleep"
      ],
      description: "Nombrada por las famosas montañas del Mont Blanc debido a su capa torrencial de tricomas blancos como la nieve. Un cruce a tres bandas con perfil cremoso a pastel de vainilla y fresa.",
      visualColor: "linear-gradient(135deg, #E2E8F0 0%, #475569 100%)",
      bgPattern: "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-pisthash",
      image: "img/ths-pisthash.webp",
      name: "Pisthash",
      aka: "Biscotti x French Cookies",
      bank: "TH Seeds",
      species: "Hibrida",
      thc: 24,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.7,
      reviewsCount: 840,
      genetics: "Biscotti x French Cookies",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 40,
          caryophyllene: 35,
          linalool: 25
      },
      flavors: [
          "Pistacho Dulce",
          "Nuez Tostada",
          "Galleta Italiana"
      ],
      effects: [
          "Euforia Elegante",
          "Bienestar Físico",
          "Calma Mental"
      ],
      activities: [
          "social",
          "nature_walk"
      ],
      description: "Una cepa única que entrega aromas cremosos y tostados a frutos secos y pistacho verde. Combinación gourmet de Biscotti con French Cookies.",
      visualColor: "linear-gradient(135deg, #84CC16 0%, #15803D 100%)",
      bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-melonsicle",
      image: "img/ths-melonsicle.webp",
      name: "Melonsicle",
      aka: "Watermelon x Strawberry Banana x GSC",
      bank: "TH Seeds",
      species: "Sativa",
      thc: 24,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1250,
      genetics: "Watermelon x Strawberry Banana x GSC",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 30,
          pinene: 25
      },
      flavors: [
          "Sandía Dulce",
          "Helado de Fresa",
          "Fruta Tropical"
      ],
      effects: [
          "Euforia Tropical",
          "Energía Creativa",
          "Buen Humor"
      ],
      activities: [
          "social",
          "creativity",
          "nature_walk"
      ],
      description: "Bomba frutal que sabe a helado de sandía y fresa. Un híbrido con ligera dominancia sativa perfecto para refrescar los días soleados.",
      visualColor: "linear-gradient(135deg, #EF4444 0%, #10B981 100%)",
      bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "ths-blumosa",
      image: "img/ths-blumosa.webp",
      name: "Blumosa",
      aka: "Blue Sherbet x Mimosa",
      bank: "TH Seeds",
      species: "Hibrida",
      thc: 23,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.7,
      reviewsCount: 670,
      genetics: "Blue Sherbet x Mimosa",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          myrcene: 30,
          pinene: 25
      },
      flavors: [
          "Arándano Cítrico",
          "Champán de Naranja",
          "Sorbete Dulce"
      ],
      effects: [
          "Euforia Espumosa",
          "Energía Solar",
          "Claridad Mental"
      ],
      activities: [
          "social",
          "creativity"
      ],
      description: "Maridaje cítrico y afrutado de Blue Sherbet y Mimosa. Produce un humo sedoso con notas a cóctel de frutas tropicales y un efecto estimulante y alegre.",
      visualColor: "linear-gradient(135deg, #3B82F6 0%, #F59E0B 100%)",
      bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-super-skunk",
      image: "img/wls-super-skunk.webp",
      name: "Super Skunk",
      aka: "Skunk #1 x Afghani #1",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 21,
      cbd: 0.5,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 50,
      rating: 4.8,
      reviewsCount: 1650,
      genetics: "Skunk #1 x Afghani Hash Plant",
      origin: "Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 30,
          limonene: 20
      },
      flavors: [
          "Skunk Intenso",
          "Dulzura Citrica",
          "Hachís Terroso"
      ],
      effects: [
          "Relajación Profunda",
          "Euforia Cálida",
          "Alivio del Estrés"
      ],
      activities: [
          "relax_sleep",
          "social"
      ],
      description: "La célebre versión de Super Skunk elaborada por White Label. Cruce galardonado de Skunk #1 con una planta de hachís afgana pura. Cogollos voluminosos repleto de glándulas aromáticas de resina.",
      visualColor: "linear-gradient(135deg, #16A34A 0%, #15803D 100%)",
      bgPattern: "radial-gradient(circle, rgba(22,163,74,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-northern-lights",
      image: "img/wls-northern-lights.webp",
      name: "Northern Lights",
      aka: "NL #5 Selection",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 22,
      cbd: 0.6,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 50,
      rating: 4.9,
      reviewsCount: 2400,
      genetics: "Afghani Indica x Thai Sativa",
      origin: "EEUU / Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 55,
          pinene: 25,
          caryophyllene: 20
      },
      flavors: [
          "Pino Dulce",
          "Tierra Húmeda",
          "Especias Almizcladas"
      ],
      effects: [
          "Sedación Corporal",
          "Paz Interior",
          "Descanso Reparador"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Una de las variedades más influyentes de la historia del cannabis. La versión de White Label destaca por su estructura resistente de baja estatura, su rápida floración y sus cogollos compactos y dulzones.",
      visualColor: "linear-gradient(135deg, #0284C7 0%, #0F172A 100%)",
      bgPattern: "radial-gradient(circle, rgba(2,132,199,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-shiva-skunk",
      image: "img/wls-shiva-skunk.webp",
      name: "Shiva Skunk",
      aka: "Northern Lights #5 x Skunk #1",
      bank: "White Label Seed Co.",
      species: "Indica",
      thc: 23,
      cbd: 0.4,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 55,
      rating: 4.8,
      reviewsCount: 1100,
      genetics: "Northern Lights #5 x Skunk #1",
      origin: "Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 35,
          limonene: 20
      },
      flavors: [
          "Incienso Cítrico",
          "Almizcle Dulce",
          "Skunk Penetrante"
      ],
      effects: [
          "Potencia Mística",
          "Euforia Densa",
          "Relajación Muscular"
      ],
      activities: [
          "music",
          "meditation"
      ],
      description: "El híbrido Skunk más potente creado por la familia Sensi / White Label. Combina la fuerza desbordante de NL#5 con el volumen y vigor de Skunk #1. Olor penetrante a incienso cítrico.",
      visualColor: "linear-gradient(135deg, #8B5CF6 0%, #4C1D95 100%)",
      bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-purple-haze",
      image: "img/wls-purple-haze.webp",
      name: "Purple Haze",
      aka: "Original Purple Haze Selection",
      bank: "White Label Seed Co.",
      species: "Sativa",
      thc: 21,
      cbd: 0.2,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 65,
      rating: 4.8,
      reviewsCount: 1780,
      genetics: "Purple Thai x Haze",
      origin: "California / Países Bajos",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          myrcene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Arándano Silvestre",
          "Incienso Haze",
          "Especias Dulces"
      ],
      effects: [
          "Euforia Psicodélica",
          "Energía Creativa",
          "Estimulación Sensorial"
      ],
      activities: [
          "creativity",
          "music",
          "social"
      ],
      description: "Híbrido sativa místico celebrado en canciones y cultura cannábica. Destaca por sus tonalidades púrpuras y violetas al final de floración y un subidón cerebral volador con aroma a incienso y bayas.",
      visualColor: "linear-gradient(135deg, #A855F7 0%, #6B21A8 100%)",
      bgPattern: "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)"
  },
  {
id: "wls-durban",
      image: "img/wls-durban.webp",
      name: "Durban",
      aka: "Durban Poison Selection",
      bank: "White Label Seed Co.",
      species: "Sativa",
      thc: 20,
      cbd: 0.3,
      yieldIndoor: 450,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.7,
      reviewsCount: 1250,
      genetics: "Durban South Africa Landrace",
      origin: "Durban, Sudáfrica",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 50,
          myrcene: 25,
          limonene: 25
      },
      flavors: [
          "Anís Dulce",
          "Regaliz Especiado",
          "Limón Silvestre"
      ],
      effects: [
          "Subidón Energético",
          "Claridad Mental",
          "Motivación Activa"
      ],
      activities: [
          "workout",
          "nature_walk",
          "creativity"
      ],
      description: "Sativa sudafricana pura aclimatada por White Label. Famosa por sus sabores únicos a anís dulce y regaliz, con un efecto claro, activo y energizante ideal para actividades al aire libre.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #854D0E 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-nyc-diesel",
      image: "img/soma-nyc-diesel.webp",
      name: "NYC Diesel",
      aka: "Soma Original NYC Diesel",
      bank: "Soma Seeds",
      species: "Hibrida",
      thc: 22,
      cbd: 0.4,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 70,
      rating: 4.9,
      reviewsCount: 2800,
      genetics: "Mexican Sativa x Afghani Landrace",
      origin: "Nueva York / Ámsterdam",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Pomelo Rojo",
          "Gasolina Dulce",
          "Mandarina Cítrica"
      ],
      effects: [
          "Euforia Cerebral",
          "Energía Creativa",
          "Subidón Exótico"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "La legendaria NYC Diesel creada por Soma, ganadora de 5 premios en la High Times Cannabis Cup. Famosa mundialmente por su penetrante aroma a pomelo rojo recién cortado con toques de carburante dulce. Efecto eufórico, activo y supremamente creativo.",
      visualColor: "linear-gradient(135deg, #EF4444 0%, #F59E0B 100%)",
      bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-amnesia-haze",
      image: "img/soma-amnesia-haze.webp",
      name: "Amnesia Haze",
      aka: "Soma Original Amnesia Haze",
      bank: "Soma Seeds",
      species: "Sativa",
      thc: 23,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 650,
      floweringDays: 80,
      rating: 4.9,
      reviewsCount: 3200,
      genetics: "South Asian Sativa x Jamaican Sativa x Cambodian Haze",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Limón Especiado",
          "Incienso Haze",
          "Madera de Cedro"
      ],
      effects: [
          "Euforia Psicodélica",
          "Energía Elevada",
          "Viaje Mental"
      ],
      activities: [
          "creativity",
          "music",
          "nature_walk"
      ],
      description: "La ganadora absoluta de la Cannabis Cup 2004 creada por Soma. Una sativa maestra que ofrece un perfil terpénico complejo a incienso dulce, limón silvestre y especias orientales. Subidón psicodélico y duradero.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #10B981 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-somango",
      image: "img/soma-somango.webp",
      name: "Somango",
      aka: "Soma #5",
      bank: "Soma Seeds",
      species: "Indica",
      thc: 21,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1950,
      genetics: "Jack Herer x Super Skunk x Big Skunk Korean",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          pinene: 25
      },
      flavors: [
          "Mango Maduro",
          "Fruta Tropical Dulce",
          "Resina Cítrica"
      ],
      effects: [
          "Claridad Estimulante",
          "Calma Corporal",
          "Euforia Sensual"
      ],
      activities: [
          "social",
          "creativity",
          "relax_sleep"
      ],
      description: "Anteriormente conocida como Soma #5. Famosa por su irresistible sabor a mango tropical y su tonalidad morada durante la maduración. Un humo delicioso que calma el cuerpo sin nublar la mente.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #EC4899 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-lavender",
      image: "img/soma-lavender.webp",
      name: "Lavender",
      aka: "Soma Lavender Strain",
      bank: "Soma Seeds",
      species: "Indica",
      thc: 20,
      cbd: 0.5,
      yieldIndoor: 450,
      yieldOutdoor: 500,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1700,
      genetics: "Super Skunk x Big Skunk Korean x Afghan x Hawaiian",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          pinene: 25
      },
      flavors: [
          "Lavanda Floral",
          "Hachís Dulce",
          "Especias Afganas"
      ],
      effects: [
          "Relajación Profunda",
          "Paz Mental",
          "Alivio del Estrés"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Una de las cepas más hermosas y aromáticas del catálogo de Soma. Presenta cálices púrpura oscuro casi negros con pelos de color naranja violáceo y un aroma inconfundible a lavanda silvestre y hachís especiado.",
      visualColor: "linear-gradient(135deg, #8B5CF6 0%, #4C1D95 100%)",
      bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-buddhas-sister",
      image: "img/soma-buddhas-sister.webp",
      name: "Buddha's Sister",
      aka: "Soma Recline",
      bank: "Soma Seeds",
      species: "Indica",
      thc: 21,
      cbd: 0.6,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.7,
      reviewsCount: 1400,
      genetics: "Recline x Afghani Hawaiian",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Cereza Cítrica",
          "Caramelo Dulce",
          "Especias Orientales"
      ],
      effects: [
          "Paz Meditativa",
          "Relajación Corporal",
          "Bienestar Espiritual"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Variedad altamente valorada en la comunidad terapéutica holandesa. Produce flores densas impregnadas de resina rosada con un sabor dulce a cerezas ácidas y caramelo. Efecto contemplativo y relajante.",
      visualColor: "linear-gradient(135deg, #F43F5E 0%, #881337 100%)",
      bgPattern: "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-soma-rockbud",
      image: "img/soma-soma-rockbud.webp",
      name: "Soma Rockbud",
      aka: "Rockbud / A+ Indica",
      bank: "Soma Seeds",
      species: "Indica",
      thc: 20,
      cbd: 0.5,
      yieldIndoor: 450,
      yieldOutdoor: 500,
      floweringDays: 60,
      rating: 4.6,
      reviewsCount: 920,
      genetics: "Super Skunk x Big Skunk Korean x Afghani x Hawaiian",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          pinene: 25
      },
      flavors: [
          "Tierra Húmeda",
          "Madera Roza",
          "Hachís Afgano"
      ],
      effects: [
          "Sedación Física",
          "Descanso Muscular",
          "Calma Absoluta"
      ],
      activities: [
          "relax_sleep"
      ],
      description: "Variedad bautizada por la dureza pétrea de sus flores. Híbrido indica de ramas compactas y tricomas rojizos con aroma clásico a tierra húmeda e incienso afgano. Efecto tranquilizante.",
      visualColor: "linear-gradient(135deg, #475569 0%, #0F172A 100%)",
      bgPattern: "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-g13-haze",
      image: "img/soma-g13-haze.webp",
      name: "G13 Haze",
      aka: "G13 x Hawaiian Haze",
      bank: "Soma Seeds",
      species: "Sativa",
      thc: 23,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 75,
      rating: 4.8,
      reviewsCount: 1600,
      genetics: "G13 Clone x Hawaiian Haze",
      origin: "EEUU / Ámsterdam",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Pimienta Cítrica",
          "Incienso Dulce",
          "Fruta Tropical"
      ],
      effects: [
          "Claridad Intensa",
          "Euforia Cerebral",
          "Energía Duradera"
      ],
      activities: [
          "creativity",
          "social",
          "gaming"
      ],
      description: "Ganadora de la Cannabis Cup 2006. Une el poder mítico del clon leyenda G13 con las notas frutales y picantes de Hawaiian Haze. Un humo denso y eufórico de primera categoría.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-so-g-kush",
      image: "img/soma-so-g-kush.webp",
      name: "So G Kush",
      aka: "OG Kush x LA Confidential x Trainwreck",
      bank: "Soma Seeds",
      species: "Indica",
      thc: 23,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 65,
      rating: 4.7,
      reviewsCount: 1150,
      genetics: "OG Kush x LA Confidential x Trainwreck",
      origin: "California / Ámsterdam",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 40,
          myrcene: 35,
          limonene: 25
      },
      flavors: [
          "Pino Diésel",
          "Tierra Especiada",
          "Limón Químico"
      ],
      effects: [
          "Grave Sedación",
          "Calma Mental",
          "Relax Corporal Total"
      ],
      activities: [
          "relax_sleep"
      ],
      description: "Potente trinomio genético que reúne lo mejor de las leyendas norteamericanas OG Kush, LA Confidential y Trainwreck. Sabor denso a pino, tierra diésel y efecto corporal demoledor.",
      visualColor: "linear-gradient(135deg, #15803D 0%, #166534 100%)",
      bgPattern: "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-free-white",
      image: "img/free-white-bud-real.webp",
      name: "Free White",
      aka: "Soma White Selection",
      bank: "Soma Seeds",
      species: "Hibrida",
      thc: 21,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 550,
      floweringDays: 63,
      rating: 4.6,
      reviewsCount: 780,
      genetics: "White Widow x Big Skunk Korean",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 30,
          pinene: 25
      },
      flavors: [
          "Skunk Cítrico",
          "Pino Blanco",
          "Tierra Dulce"
      ],
      effects: [
          "Euforia Equilibrada",
          "Sensación Social",
          "Relax Muscular"
      ],
      activities: [
          "social",
          "music",
          "nature_walk"
      ],
      description: "Selección blanca especial de Soma que combina la clásica resina acristalada de White Widow con el vigor vegetal y el dulzor skunk de Big Skunk Korean.",
      visualColor: "linear-gradient(135deg, #94A3B8 0%, #334155 100%)",
      bgPattern: "radial-gradient(circle, rgba(148,163,184,0.2) 0%, transparent 70%)"
  },
  {
id: "soma-somaui",
      image: "img/soma-somaui.webp",
      name: "Somaui",
      aka: "Hawaiian Sativa x G13 Haze",
      bank: "Soma Seeds",
      species: "Sativa",
      thc: 22,
      cbd: 0.3,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 70,
      rating: 4.7,
      reviewsCount: 840,
      genetics: "Hawaiian Sativa x G13 Haze",
      origin: "Hawái / Ámsterdam",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Piña Tropical",
          "Cítrico Dulce",
          "Especias Florales"
      ],
      effects: [
          "Energía Solar",
          "Euforia Radiante",
          "Inspiración Creativa"
      ],
      activities: [
          "creativity",
          "nature_walk",
          "social"
      ],
      description: "Híbrido tropical insular que combina la brisa frutal de las sativa hawaianas con la estructura densa de G13 Haze. Sabor riquísimo a piña y cítricos con un subidón inspirador.",
      visualColor: "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
      bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-pot-of-gold",
      image: "img/tfd-pot-of-gold.webp",
      name: "Pot of Gold",
      aka: "POG / High Times Winner",
      bank: "The Flying Dutchmen",
      species: "Indica",
      thc: 22,
      cbd: 0.5,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 55,
      rating: 4.9,
      reviewsCount: 2100,
      genetics: "Hindu Kush x Skunk #1",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          pinene: 25
      },
      flavors: [
          "Hachís Dulce",
          "Skunk Penetrante",
          "Especias Terrosas"
      ],
      effects: [
          "Sedación Profunda",
          "Euforia Cálida",
          "Relajación Muscular"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "La cepa buque insignia de The Flying Dutchmen, ganadora de la High Times Cannabis Cup. Un híbrido sensacional entre una afgana Hindu Kush seleccionada y Skunk #1. Produce cosechas masivas cubiertas de resina melosa con sabor a hachís especiado.",
      visualColor: "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
      bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-g-force",
      image: "img/tfd-g-force.webp",
      name: "G-Force",
      aka: "G13 x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Indica",
      thc: 23,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 56,
      rating: 4.8,
      reviewsCount: 1450,
      genetics: "G13 Clone x Skunk #1",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 40,
          myrcene: 35,
          limonene: 25
      },
      flavors: [
          "Pino Denso",
          "Skunk Terroso",
          "Especias Químicas"
      ],
      effects: [
          "Fuerza G Corporal",
          "Sedación Intensa",
          "Descanso Total"
      ],
      activities: [
          "relax_sleep"
      ],
      description: "Bautizada G-Force por su abrumadora fuerza de atracción gravitatoria corporal. Un cruce demoledor del clon mítico norteamericano G13 reforzado con la estabilidad de Skunk #1. Cogollos pesados como piedras.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #064E3B 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-pineapple-punch",
      image: "img/tfd-pineapple-punch.webp",
      name: "Pineapple Punch",
      aka: "Real McCoy x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Hibrida",
      thc: 20,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 550,
      floweringDays: 63,
      rating: 4.7,
      reviewsCount: 1100,
      genetics: "The Real McCoy x Skunk #1",
      origin: "Hawái / Ámsterdam",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Piña Tropical",
          "Ponche Dulce",
          "Cítrico Ácido"
      ],
      effects: [
          "Euforia Tropical",
          "Alegría Radiante",
          "Energía Suave"
      ],
      activities: [
          "social",
          "nature_walk",
          "creativity"
      ],
      description: "Una verdadera delicia tropical creada seleccionando los fenotipos de piña más dulces de The Real McCoy cruzados con Skunk #1. Destaca por su inconfundible aroma a ponche de piña madura y su subidón risueño.",
      visualColor: "linear-gradient(135deg, #FACC15 0%, #CA8A04 100%)",
      bgPattern: "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-the-real-mccoy",
      image: "img/tfd-the-real-mccoy.webp",
      name: "The Real McCoy",
      aka: "Hawaiian Sativa x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Hibrida",
      thc: 21,
      cbd: 0.3,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 65,
      rating: 4.8,
      reviewsCount: 1300,
      genetics: "Hawaiian Sativa x Skunk #1",
      origin: "Hawái / Ámsterdam",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 40,
          myrcene: 35,
          pinene: 25
      },
      flavors: [
          "Fruta Tropical",
          "Pimienta Cítrica",
          "Madera Dulce"
      ],
      effects: [
          "Claridad Cerebral",
          "Estimulación Creativa",
          "Bienestar"
      ],
      activities: [
          "creativity",
          "music",
          "social"
      ],
      description: "Cepa legendaria de The Flying Dutchmen que equilibra la dulzura exótica de las sativa hawaianas con la vigorosa floración de Skunk #1. Sabor complejo y especiado con un subidón inspirador.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #C2410C 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-voyager",
      image: "img/tfd-voyager.webp",
      name: "Voyager",
      aka: "Malawi x Hindu Kush x Thai",
      bank: "The Flying Dutchmen",
      species: "Hibrida",
      thc: 22,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.7,
      reviewsCount: 980,
      genetics: "Malawi Gold x Hindu Kush x Thai Sativa",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          terpinolene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Incienso Oriental",
          "Especias Picantes",
          "Tierra Exótica"
      ],
      effects: [
          "Viaje Místico",
          "Euforia Elevada",
          "Relajación Corporal"
      ],
      activities: [
          "meditation",
          "music",
          "creativity"
      ],
      description: "Una auténtica expedición genética intercontinental. Combina la potencia cósmica de Malawi Gold con la resina de Hindu Kush y la agudeza mental de Thai Sativa. Aroma envolvente a incienso y especias.",
      visualColor: "linear-gradient(135deg, #8B5CF6 0%, #5B21B6 100%)",
      bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-dame-blanche",
    image: "img/tfd-dame-blanche-hd.webp",
      name: "Dame Blanche",
      aka: "White Widow x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Indica",
      thc: 21,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 55,
      rating: 4.6,
      reviewsCount: 850,
      genetics: "White Widow x Skunk #1",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          limonene: 25
      },
      flavors: [
          "Pino Nieve",
          "Skunk Dulce",
          "Tierra Especiada"
      ],
      effects: [
          "Euforia Sedosa",
          "Calma Corporal",
          "Relajación Mágica"
      ],
      activities: [
          "relax_sleep",
          "social"
      ],
      description: "Homenaje a la 'Dama Blanca' holandesa. Cruce refinado entre la inconfundible White Widow y Skunk #1. Produce cálices cubiertos por un manto espeso de resina blanca y un aroma floral a pino dulce.",
      visualColor: "linear-gradient(135deg, #E2E8F0 0%, #475569 100%)",
      bgPattern: "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-titan",
      image: "img/tfd-titan.webp",
      name: "Titan",
      aka: "Skunk #1 x Northern Lights #5",
      bank: "The Flying Dutchmen",
      species: "Indica",
      thc: 22,
      cbd: 0.5,
      yieldIndoor: 600,
      yieldOutdoor: 700,
      floweringDays: 50,
      rating: 4.8,
      reviewsCount: 1200,
      genetics: "Skunk #1 x Northern Lights #5",
      origin: "Ámsterdam, Países Bajos",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          pinene: 30,
          caryophyllene: 20
      },
      flavors: [
          "Pino Resinoso",
          "Hachís Skunk",
          "Tierra Húmeda"
      ],
      effects: [
          "Rendimiento Titánico",
          "Sedación Muscular",
          "Paz Interior"
      ],
      activities: [
          "relax_sleep"
      ],
      description: "Variedad bautizada Titan por su estatura compacta e increíble peso de cosecha. Une el vigor híbrido de Skunk #1 con la legendaria cobertura de resina de Northern Lights #5. Efecto contundente.",
      visualColor: "linear-gradient(135deg, #0EA5E9 0%, #0369A1 100%)",
      bgPattern: "radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-nepal-baba",
      image: "img/tfd-nepal-baba.webp",
      name: "Nepal Baba",
      aka: "Nepalese Charas x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Indica",
      thc: 20,
      cbd: 0.7,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 55,
      rating: 4.7,
      reviewsCount: 760,
      genetics: "Nepalese Temple Hash Landrace x Skunk #1",
      origin: "Nepal / Ámsterdam",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 55,
          caryophyllene: 25,
          pinene: 20
      },
      flavors: [
          "Hachís Nepalí",
          "Madera de Cedro",
          "Especias del Himalaya"
      ],
      effects: [
          "Paz Meditativa",
          "Relajación Corporal",
          "Serenidad Mental"
      ],
      activities: [
          "meditation",
          "relax_sleep"
      ],
      description: "Desarrollada a partir de las auténticas genéticas de hachís nepalí del Himalaya. Ofrece un humo suave y muy aromático con notas a madera sagrada, incienso y resina artesanal.",
      visualColor: "linear-gradient(135deg, #78350F 0%, #451A03 100%)",
      bgPattern: "radial-gradient(circle, rgba(120,53,15,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-swazi-safari",
      image: "img/tfd-swazi-safari.webp",
      name: "Swazi Safari",
      aka: "Swazi Landrace x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Sativa",
      thc: 21,
      cbd: 0.3,
      yieldIndoor: 450,
      yieldOutdoor: 600,
      floweringDays: 70,
      rating: 4.6,
      reviewsCount: 680,
      genetics: "Swazi African Landrace x Skunk #1",
      origin: "Suazilandia / Países Bajos",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 50,
          myrcene: 25,
          limonene: 25
      },
      flavors: [
          "Cítrico Dulce",
          "Pimienta Africana",
          "Cítrico de Montaña"
      ],
      effects: [
          "Energía Eléctrica",
          "Euforia Activa",
          "Claridad Cerebral"
      ],
      activities: [
          "workout",
          "nature_walk",
          "creativity"
      ],
      description: "Sativa africana de alta potencia aclimatada por Eddie en Ámsterdam. Combina la fuerza energizante de las razas puras de Suazilandia con la rapidez de floración de Skunk #1.",
      visualColor: "linear-gradient(135deg, #22C55E 0%, #15803D 100%)",
      bgPattern: "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)"
  },
  {
id: "tfd-dutchmens-royal-orange",
      image: "img/tfd-dutchmens-royal-orange.webp",
      name: "Dutchmen's Royal Orange",
      aka: "Cali Orange x Skunk #1",
      bank: "The Flying Dutchmen",
      species: "Hibrida",
      thc: 20,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 550,
      floweringDays: 55,
      rating: 4.7,
      reviewsCount: 820,
      genetics: "California Orange x Skunk #1",
      origin: "California / Ámsterdam",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          myrcene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Naranja Madura",
          "Piel de Mandarina",
          "Dulzor Skunk"
      ],
      effects: [
          "Alegría Social",
          "Euforia Suave",
          "Bienestar Cítrico"
      ],
      activities: [
          "social",
          "music",
          "nature_walk"
      ],
      description: "Selección real de California Orange combinada con Skunk #1. Famosa por sus cálices abultados de color naranja dorado y su aroma a zumo fresco de naranja dulce.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-peyote-zkittlez",
      image: "img/sdm-peyote-zkittlez.webp",
      name: "Peyote Zkittlez",
      aka: "Peyote WiFi x Zkittlez",
      bank: "Seedsman",
      species: "Indica",
      thc: 24,
      cbd: 0.3,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 2400,
      genetics: "Peyote WiFi x Zkittlez",
      origin: "Reino Unido / EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Caramelo de Frutas",
          "Dulce de Uva",
          "Tierra Kush"
      ],
      effects: [
          "Euforia Potente",
          "Relax Corporal Profundo",
          "Paz Mental"
      ],
      activities: [
          "relax_sleep",
          "music",
          "social"
      ],
      description: "Una de las variedades más populares y potentes de Seedsman. Cruce de Peyote WiFi con Zkittlez que destaca por sus tonos púrpuras oscuros, su explosión de tricomas resinosos y un sabor dulce a caramelos frutales con fondo terroso.",
      visualColor: "linear-gradient(135deg, #7C3AED 0%, #DB2777 100%)",
      bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-gelato-og",
      image: "img/sdm-gelato-og.webp",
      name: "Gelato OG",
      aka: "Gelato #33 x OG Kush",
      bank: "Seedsman",
      species: "Hibrida",
      thc: 25,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 58,
      rating: 4.9,
      reviewsCount: 2150,
      genetics: "Gelato #33 x OG Kush",
      origin: "California / Reino Unido",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 35,
          myrcene: 20
      },
      flavors: [
          "Helado de Cítricos",
          "Pino Gasolina",
          "Galleta Dulce"
      ],
      effects: [
          "Euforia Cerebral",
          "Relajación Muscular",
          "Claridad Alegre"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "Exquisito híbrido de alta potencia que reúne el cremoso sabor a helado de cítricos de Gelato #33 con la fuerza resinosa y el regusto a gasolina de OG Kush. Subidón intenso y estimulante.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-peyote-cookies",
      image: "img/sdm-peyote-cookies.webp",
      name: "Peyote Cookies",
      aka: "Peyote Purple x Cookies Kush",
      bank: "Seedsman",
      species: "Indica",
      thc: 22,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 55,
      rating: 4.8,
      reviewsCount: 1800,
      genetics: "Peyote Purple x Cookies Kush",
      origin: "Reino Unido",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          limonene: 25
      },
      flavors: [
          "Guayaba Dulce",
          "Vainilla Dulce",
          "Tierra Especiada"
      ],
      effects: [
          "Sedación Corporal",
          "Bienestar Cálido",
          "Sueño Reparador"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Híbrido de impactante belleza visual con matices púrpuras y rubí. Desprende un aroma tropical dulce que recuerda a guayaba dulce y galletas con vainilla. Efecto indica relajante y placentero.",
      visualColor: "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
      bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-mama-thai",
      image: "img/sdm-mama-thai.webp",
      name: "Mama Thai",
      aka: "Pure Thai Landrace Selection",
      bank: "Seedsman",
      species: "Sativa",
      thc: 22,
      cbd: 0.2,
      yieldIndoor: 450,
      yieldOutdoor: 600,
      floweringDays: 77,
      rating: 4.7,
      reviewsCount: 1100,
      genetics: "Thai Landrace Selection",
      origin: "Tailandia / Reino Unido",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 50,
          myrcene: 25,
          pinene: 25
      },
      flavors: [
          "Pimienta Cítrica",
          "Limón Silvestre",
          "Madera Exótica"
      ],
      effects: [
          "Energía Eléctrica",
          "Euforia Cerebral",
          "Claridad Activa"
      ],
      activities: [
          "workout",
          "nature_walk",
          "creativity"
      ],
      description: "Una de las pocas sativas puras tailandesas aclimatadas con éxito para cultivos de interior y exterior. Produce cogollos aéreos cargados de resina picante con sabor a limón, madera fina y especias orientales.",
      visualColor: "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
      bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-alaskan-purple",
      image: "img/sdm-alaskan-purple.webp",
      name: "Alaskan Purple",
      aka: "Alaskan Purple x Kush x Brazilian",
      bank: "Seedsman",
      species: "Indica",
      thc: 23,
      cbd: 0.3,
      yieldIndoor: 550,
      yieldOutdoor: 700,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1650,
      genetics: "Alaskan Purple x Kush x Brazilian Sativa",
      origin: "Alaska / Brasil / Reino Unido",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          limonene: 25
      },
      flavors: [
          "Bayas Silvestres",
          "Pino Dulce",
          "Tierra de Flor"
      ],
      effects: [
          "Relajación Muscular",
          "Euforia Serena",
          "Bienestar Mental"
      ],
      activities: [
          "relax_sleep",
          "nature_walk"
      ],
      description: "Variedad gigante de producción masiva caracterizada por sus espectaculares tonalidades moradas y púrpuras. Ofrece un humo suave y muy aromático con notas a bayas silvestres y pino dulce.",
      visualColor: "linear-gradient(135deg, #A855F7 0%, #4C1D95 100%)",
      bgPattern: "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-bad-azz-cheese",
      image: "img/sdm-bad-azz-cheese.webp",
      name: "Bad Azz Cheese",
      aka: "Bad Azz Kush x UK Cheese",
      bank: "Seedsman",
      species: "Indica",
      thc: 21,
      cbd: 0.5,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.7,
      reviewsCount: 980,
      genetics: "Bad Azz Kush x UK Cheese",
      origin: "Reino Unido / EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 35,
          limonene: 20
      },
      flavors: [
          "Queso Curado",
          "Especias Diésel",
          "Tierra Húmeda"
      ],
      effects: [
          "Efecto Risueño",
          "Relax Físico",
          "Calma Mente"
      ],
      activities: [
          "social",
          "music",
          "relax_sleep"
      ],
      description: "Híbrido muy especial que une el aroma fuerte y picante de la clásica UK Cheese con el toque potente y diésel de Bad Azz Kush. Cogollos densos y muy resinosos.",
      visualColor: "linear-gradient(135deg, #FACC15 0%, #854D0E 100%)",
      bgPattern: "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-white-widow",
      image: "img/sdm-white-widow.webp",
      name: "White Widow",
      aka: "Seedsman White Widow Selection",
      bank: "Seedsman",
      species: "Hibrida",
      thc: 20,
      cbd: 0.4,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 56,
      rating: 4.7,
      reviewsCount: 1500,
      genetics: "Brazilian Sativa x South Indian Indica",
      origin: "Reino Unido",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          pinene: 25
      },
      flavors: [
          "Pino Fresco",
          "Tierra Especiada",
          "Madera Dulce"
      ],
      effects: [
          "Euforia Cerebral",
          "Relajación Corporal",
          "Energía Social"
      ],
      activities: [
          "social",
          "creativity"
      ],
      description: "La versión seleccionada por Seedsman de la célebre White Widow. Famosa por sus plantas uniformes recubiertas por cristales blancos y su aroma fresco a pino y especias.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #059669 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-jack-herer",
      image: "img/sdm-jack-herer.webp",
      name: "Jack Herer",
      aka: "Seedsman Jack Herer Selection",
      bank: "Seedsman",
      species: "Sativa",
      thc: 21,
      cbd: 0.3,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 65,
      rating: 4.8,
      reviewsCount: 1750,
      genetics: "Haze x Northern Lights #5 x Shiva Skunk",
      origin: "Reino Unido",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          myrcene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Pino Picante",
          "Incienso Dulce",
          "Madera de Cedro"
      ],
      effects: [
          "Euforia Cerebral",
          "Energía Creativa",
          "Claridad Mental"
      ],
      activities: [
          "creativity",
          "social",
          "nature_walk"
      ],
      description: "Selección especial de Jack Herer perfeccionada por Seedsman. Conserva la potencia sativa cerebral con toques a pino fresco, incienso místico y resina especiada.",
      visualColor: "linear-gradient(135deg, #22C55E 0%, #15803D 100%)",
      bgPattern: "radial-gradient(circle, rgba(34,197,94,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-amnesia-fast",
      image: "img/sdm-amnesia-fast.webp",
      name: "Amnesia Fast",
      aka: "Amnesia Haze x Secret Hybrid",
      bank: "Seedsman",
      species: "Sativa",
      thc: 21,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 50,
      rating: 4.7,
      reviewsCount: 1200,
      genetics: "Amnesia Haze x Secret Auto Hybrid",
      origin: "Reino Unido",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Limón Especiado",
          "Incienso Dulce",
          "Cítrico Fresco"
      ],
      effects: [
          "Euforia Rápida",
          "Energía Cerebral",
          "Claridad Mental"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Versión de floración rápida de la famosa Amnesia Haze desarrollada por Seedsman. Recorta el tiempo de floración a sólo 50 días sin perder su característico aroma a incienso cítrico.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "sdm-blue-blueberry",
      image: "img/sdm-blue-blueberry.webp",
      name: "Blue Blueberry",
      aka: "Seedsman Blueberry Selection",
      bank: "Seedsman",
      species: "Indica",
      thc: 20,
      cbd: 0.4,
      yieldIndoor: 450,
      yieldOutdoor: 500,
      floweringDays: 60,
      rating: 4.6,
      reviewsCount: 890,
      genetics: "Original Blueberry Selection",
      origin: "EEUU / Reino Unido",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          pinene: 25
      },
      flavors: [
          "Arándano Silvestre",
          "Mermelada Dulce",
          "Tierra de Frutas"
      ],
      effects: [
          "Relajación Dulce",
          "Calma Corporal",
          "Paz Mental"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Selección refinada de la mítica línea Blueberry. Famosa por sus tonalidades azuladas al final de la floración y su característico aroma a arándanos dulces y mermelada silvestre.",
      visualColor: "linear-gradient(135deg, #3B82F6 0%, #1E40AF 100%)",
      bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-grease-monkey",
      image: "img/exg-grease-monkey.webp",
      name: "Grease Monkey",
      aka: "Gorilla Glue #4 x Cookies and Cream",
      bank: "Exotic Genetix",
      species: "Indica",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 3100,
      genetics: "Gorilla Glue #4 x Cookies and Cream",
      origin: "Washington, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Vainilla Dulce",
          "Gasolina Diésel",
          "Tierra Skunk"
      ],
      effects: [
          "Sedación Corporal",
          "Euforia Intensa",
          "Relax Profundo"
      ],
      activities: [
          "relax_sleep",
          "music",
          "meditation"
      ],
      description: "Una de las obras maestras absolutas de Exotic Genetix. Cruce perfecto de Gorilla Glue #4 y Cookies and Cream que destaca por su potencia atronadora, una capa plateada de tricomas pegajosos y un perfil que combina vainilla cremosa con gasolina diésel.",
      visualColor: "linear-gradient(135deg, #1E293B 0%, #475569 100%)",
      bgPattern: "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-cookies-and-cream",
      image: "img/exg-cookies-and-cream.webp",
      name: "Cookies and Cream",
      aka: "Starfighter x Mystery Cookie",
      bank: "Exotic Genetix",
      species: "Hibrida",
      thc: 26,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 2800,
      genetics: "Starfighter x Mystery Cookie",
      origin: "Washington, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Galleta de Vainilla",
          "Nata Cสถาน",
          "Tierra Dulce"
      ],
      effects: [
          "Euforia Feliz",
          "Relajación Muscular",
          "Calma Mente"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "Ganadora del primer puesto en la Denver Cannabis Cup. Legendaria variedad creada por Mike de Exotic Genetix con un irresistible perfil a galletas recién horneadas con nata de vainilla y resina acristalada.",
      visualColor: "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
      bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-strawberries-and-cream",
      image: "img/exg-strawberries-and-cream.webp",
      name: "Strawberries & Cream",
      aka: "Strawberry Cough x Cookies and Cream",
      bank: "Exotic Genetix",
      species: "Hibrida",
      thc: 25,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 58,
      rating: 4.9,
      reviewsCount: 2100,
      genetics: "Strawberry Cough x Cookies and Cream",
      origin: "Washington, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 35,
          caryophyllene: 20
      },
      flavors: [
          "Fresa Madura",
          "Batido de Nata",
          "Tierra Frutal"
      ],
      effects: [
          "Euforia Alegre",
          "Sensación Cálida",
          "Creatividad Dulce"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Delicioso híbrido frutal que fusiona el intenso aroma a fresas silvestres de Strawberry Cough con la cremosidad de Cookies and Cream. Produce flores tupidas teñidas de resina rosada.",
      visualColor: "linear-gradient(135deg, #EF4444 0%, #F43F5E 100%)",
      bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-mint-chocolate-chip",
      image: "img/exg-mint-chocolate-chip.webp",
      name: "Mint Chocolate Chip",
      aka: "Thin Mint GSC x Green Ribbon BX",
      bank: "Exotic Genetix",
      species: "Hibrida",
      thc: 24,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 1750,
      genetics: "Thin Mint GSC x Green Ribbon BX",
      origin: "Washington, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 35,
          myrcene: 20
      },
      flavors: [
          "Menta Menta",
          "Chocolate Oscuro",
          "Pino Dulce"
      ],
      effects: [
          "Claridad Alegre",
          "Relax Físico Suave",
          "Bienestar"
      ],
      activities: [
          "social",
          "nature_walk",
          "music"
      ],
      description: "Refrito mentolado de gran éxito caracterizado por un aroma refrescante a menta piperita mezclada con toques de chocolate negro y pino. Cogollos compactos como piedras caladas de cristal.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-red-runtz",
      image: "img/exg-red-runtz.webp",
      name: "Red Runtz",
      aka: "Red Pop x Runtz",
      bank: "Exotic Genetix",
      species: "Hibrida",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 1900,
      genetics: "Red Pop x Runtz",
      origin: "Washington, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          linalool: 25
      },
      flavors: [
          "Refresco de Cereza",
          "Caramelo Runtz",
          "Gas Dulce"
      ],
      effects: [
          "Euforia Explosiva",
          "Relax Corporal",
          "Dicha Mental"
      ],
      activities: [
          "social",
          "music",
          "gaming"
      ],
      description: "Uno de los lanzamientos modernos más aclamados de Exotic Genetix. Uniendo Red Pop con Runtz, ofrece una explosión de sabor a refresco de cereza dulce con gas diésel y colores rojo-púrpura deslumbrantes.",
      visualColor: "linear-gradient(135deg, #DC2626 0%, #991B1B 100%)",
      bgPattern: "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-scotty-2-hotty",
      image: "img/exg-scotty-2-hotty.webp",
      name: "Scotty 2 Hotty",
      aka: "Biscotti x Rainbow Chip",
      bank: "Exotic Genetix",
      species: "Indica",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1400,
      genetics: "Biscotti x Rainbow Chip",
      origin: "Washington, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Galleta Italiana",
          "Mantequilla Dulce",
          "Gas Diésel"
      ],
      effects: [
          "Relax Físico",
          "Calma Risueña",
          "Descanso"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Combinación genial de Biscotti y Rainbow Chip. Desprende un aroma muy rico a masa de galleta horneada con mantequilla caliente y regusto a gasolina fina. Efecto sedante y muy placentero.",
      visualColor: "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
      bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-runtz-buttonz",
      image: "img/exg-runtz-buttonz.webp",
      name: "Runtz Buttonz",
      aka: "Runtz x Rainbow Chip",
      bank: "Exotic Genetix",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1300,
      genetics: "Runtz x Rainbow Chip",
      origin: "Washington, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Gominolas Frutales",
          "Cítrico Tropical",
          "Kush Terroso"
      ],
      effects: [
          "Euforia Cerebral",
          "Energía Creativa",
          "Relax Corporal"
      ],
      activities: [
          "creativity",
          "social"
      ],
      description: "Híbrido goloso que cruza la célebre Runtz con Rainbow Chip. Produce cogollos ultra densos teñidos de violeta y naranja cubiertos por una manto espeso de resina con aroma a gominolas tropicales.",
      visualColor: "linear-gradient(135deg, #8B5CF6 0%, #C084FC 100%)",
      bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-power-sherb",
      image: "img/exg-power-sherb.webp",
      name: "Power Sherb",
      aka: "SherbBX x Cookies and Cream",
      bank: "Exotic Genetix",
      species: "Indica",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 1150,
      genetics: "SherbBX x Cookies and Cream",
      origin: "Washington, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 35,
          myrcene: 20
      },
      flavors: [
          "Sorbete de Cítricos",
          "Crema Dulce",
          "Kush Gasolina"
      ],
      effects: [
          "Potencia Corporal",
          "Euforia Alegre",
          "Relax Profundo"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Híbrido de gran calibre que combina el sorbete cítrico de Sunset Sherbet con la fuerza cremosa de Cookies and Cream. Flores macizas bañadas en resina terpénica muy aromática.",
      visualColor: "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
      bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-gary-poppins",
      image: "img/exg-gary-poppins.webp",
      name: "Gary Poppins",
      aka: "Gary Payton x Red Pop",
      bank: "Exotic Genetix",
      species: "Hibrida",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 1600,
      genetics: "Gary Payton x Red Pop",
      origin: "Washington, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Cereza Diésel",
          "Pimienta Especiada",
          "Gas Dulce"
      ],
      effects: [
          "Euforia Social",
          "Claridad Activa",
          "Relax Físico"
      ],
      activities: [
          "social",
          "gaming",
          "creativity"
      ],
      description: "Unión brutal de la famosa Gary Payton con Red Pop. Presenta un aroma punzante a cerezas picantes y gas combustible con cogollos duros como rocas cargados de tricomas.",
      visualColor: "linear-gradient(135deg, #E11D48 0%, #BE123C 100%)",
      bgPattern: "radial-gradient(circle, rgba(225,29,72,0.2) 0%, transparent 70%)"
  },
  {
id: "exg-tina",
      image: "img/exg-tina.webp",
      name: "Tina",
      aka: "Constantine x Cheetah Piss",
      bank: "Exotic Genetix",
      species: "Indica",
      thc: 28,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 1850,
      genetics: "Constantine x Cheetah Piss",
      origin: "Washington, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 50,
          myrcene: 30,
          limonene: 20
      },
      flavors: [
          "Gas Combustible",
          "Tierra Picante",
          "Zorrillo Skunk"
      ],
      effects: [
          "Sedación Knockout",
          "Euforia Pesada",
          "Relax Total"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Campeona absoluta de copas cannábicas y cepa insignia de la línea de Exotic Genetix. Un monstruo de THC de aroma skunk diésel ultraintenso que no perdona a ningún cultivador exigente.",
      visualColor: "linear-gradient(135deg, #0F172A 0%, #334155 100%)",
      bgPattern: "radial-gradient(circle, rgba(15,23,42,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-apples-and-bananas",
      image: "img/cpg-apples-and-bananas.webp",
      name: "Apples and Bananas",
      aka: "(Blue Power x Gelatti) x GDP x Platinum Cookies",
      bank: "Compound Genetics",
      species: "Hibrida",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 3500,
      genetics: "(Blue Power x Gelatti) x Granddaddy Purple x Platinum Cookies",
      origin: "Oregon / California, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          limonene: 25
      },
      flavors: [
          "Manzana Manzana",
          "Plátano Dulce",
          "Gasolina Diésel"
      ],
      effects: [
          "Euforia Cerebral",
          "Relax Físico",
          "Dicha Creativa"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "Una de las variedades modernas más aclamadas del mundo, creada por Compound Genetics en colaboración con Cookies. Combina un aroma penetrante a manzanas ácidas, plátano maduro y gasolina pura con una capa de resina que roza el 28% de THC.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #EAB308 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-pave",
      image: "img/cpg-pave.webp",
      name: "Pavé",
      aka: "Paris OG x Menthol",
      bank: "Compound Genetics",
      species: "Hibrida",
      thc: 29,
      cbd: 0.1,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 2900,
      genetics: "Paris OG x Menthol",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 35,
          menthol: 20
      },
      flavors: [
          "Menta Helada",
          "Gasolina OG",
          "Pino Picante"
      ],
      effects: [
          "Euforia Devastadora",
          "Sedación Corporal",
          "Paz Mental"
      ],
      activities: [
          "relax_sleep",
          "music",
          "meditation"
      ],
      description: "Desarrollada en colaboración con Quavo de Migos y Cookies. Recibe su nombre ('Pavé') porque sus flores parecen estar completamente pavimentadas de diamantes de resina blanca. Aroma mentolado y a gasolina OG extremadamente potente.",
      visualColor: "linear-gradient(135deg, #64748B 0%, #0F172A 100%)",
      bgPattern: "radial-gradient(circle, rgba(100,116,139,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-la-bomba",
      image: "img/cpg-la-bomba.webp",
      name: "La Bomba",
      aka: "Wedding Cake x Jet Fuel Gelato",
      bank: "Compound Genetics",
      species: "Indica",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 2400,
      genetics: "Wedding Cake x Jet Fuel Gelato",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Pastel de Vainilla",
          "Gasolina Diésel",
          "Crema Dulce"
      ],
      effects: [
          "Golpe Corporal",
          "Euforia Risueña",
          "Calma Profunda"
      ],
      activities: [
          "relax_sleep",
          "social",
          "gaming"
      ],
      description: "Una auténtica bomba de potencia y aroma. Une la dulzura cremosa de Wedding Cake con la pegada a combustible diésel de Jet Fuel Gelato. Cogollos gigantes y morados muy resinosos.",
      visualColor: "linear-gradient(135deg, #EC4899 0%, #3B82F6 100%)",
      bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-jokerz",
      image: "img/cpg-jokerz.webp",
      name: "Jokerz",
      aka: "White Runtz x Jet Fuel Gelato",
      bank: "Compound Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.9,
      reviewsCount: 2200,
      genetics: "White Runtz x Jet Fuel Gelato",
      origin: "California, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          linalool: 25
      },
      flavors: [
          "Caramelo Runtz",
          "Gasolina Combustible",
          "Cítrico Dulce"
      ],
      effects: [
          "Euforia Risueña",
          "Bienestar Activo",
          "Relax Corporal"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Ganadora del premio Leafly Strain of the Year contender. Junta el sabor acaramelado a frutas de White Runtz con el fondo diésel picante de Jet Fuel Gelato. Tonalidades púrpura oscuro cubiertas de resina brillante.",
      visualColor: "linear-gradient(135deg, #A855F7 0%, #EC4899 100%)",
      bgPattern: "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-gastro-pop",
      image: "img/cpg-gastro-pop.webp",
      name: "Gastro Pop",
      aka: "Apples and Bananas x Grape Gas",
      bank: "Compound Genetics",
      species: "Hibrida",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 2600,
      genetics: "Apples and Bananas x Grape Gas",
      origin: "Oregon / California, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 35,
          caryophyllene: 20
      },
      flavors: [
          "Uva Dulce",
          "Manzana Ácida",
          "Gas Diésel"
      ],
      effects: [
          "Euforia Estallido",
          "Sensación Placentera",
          "Relax Corporal"
      ],
      activities: [
          "social",
          "music",
          "creativity"
      ],
      description: "Cruce estelar entre Apples and Bananas y Grape Gas. Destaca por su perfil organoléptico complejo con aroma intenso a mermelada de uva, manzana verde y notas persistentes a gasolina dulce.",
      visualColor: "linear-gradient(135deg, #7C3AED 0%, #06B6D4 100%)",
      bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-grape-gas",
      image: "img/cpg-grape-gas.webp",
      name: "Grape Gas",
      aka: "OG Chem x GDP x Truth OG",
      bank: "Compound Genetics",
      species: "Indica",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1800,
      genetics: "OG Chem x Granddaddy Purple x Truth OG",
      origin: "Oregon, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 30,
          limonene: 20
      },
      flavors: [
          "Uva Negra",
          "Gasolina Química",
          "Tierra Kush"
      ],
      effects: [
          "Sedación Corporal",
          "Paz Mental",
          "Descanso Profundo"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Una de las madres genéticas pilares de Compound Genetics. Combina uva madura con un trasfondo químico diésel extremadamente penetrante y un efecto sedante ideal para desconectar al final del día.",
      visualColor: "linear-gradient(135deg, #6B21A8 0%, #3B0764 100%)",
      bgPattern: "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-marshmallow-og",
      image: "img/cpg-marshmallow-og.webp",
      name: "Marshmallow OG",
      aka: "Chemdawg D x Triangle Kush x Jet Fuel Gelato",
      bank: "Compound Genetics",
      species: "Indica",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1950,
      genetics: "Chemdawg D x Triangle Kush x Jet Fuel Gelato",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Nube de Azúcar",
          "Pino OG",
          "Gas Combustible"
      ],
      effects: [
          "Relax Físico Intenso",
          "Euforia Alegre",
          "Sueño Reparador"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Híbrido goloso y potente que reúne tres gigantes de la historia del cannabis. Ofrece un perfil terpenoso a nubes de golosina tostada mezcladas con pino OG picante y diésel seco.",
      visualColor: "linear-gradient(135deg, #F43F5E 0%, #FB7185 100%)",
      bgPattern: "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-red-bullz",
      image: "img/cpg-red-bullz.webp",
      name: "Red Bullz",
      aka: "Grape Gas x White Runtz",
      bank: "Compound Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1500,
      genetics: "Grape Gas x White Runtz",
      origin: "California, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Bebida de Ponche",
          "Uva Acaramelada",
          "Gas Diésel"
      ],
      effects: [
          "Euforia Energética",
          "Impulso Social",
          "Relax Muscular"
      ],
      activities: [
          "social",
          "gaming",
          "creativity"
      ],
      description: "Variedad explosiva resultante de cruzar Grape Gas con White Runtz. Desprende un aroma punzante a bebida energética de ponche de frutas con fondo a gasolina acaramelada.",
      visualColor: "linear-gradient(135deg, #EF4444 0%, #8B5CF6 100%)",
      bgPattern: "radial-gradient(circle, rgba(239,68,68,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-high-society",
      image: "img/cpg-high-society.webp",
      name: "High Society",
      aka: "Biscotti x Jet Fuel Gelato",
      bank: "Compound Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1350,
      genetics: "Biscotti x Jet Fuel Gelato",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          linalool: 25
      },
      flavors: [
          "Galleta de Nuez",
          "Canela Dulce",
          "Gasolina OG"
      ],
      effects: [
          "Euforia Elegante",
          "Bienestar Corporal",
          "Calma Mental"
      ],
      activities: [
          "social",
          "music",
          "nature_walk"
      ],
      description: "Una de las joyas gastronómicas de Compound Genetics. Cruce de Biscotti y Jet Fuel Gelato que cautiva por sus matices a galleta de nueces y canela especiada combinada con diésel fino.",
      visualColor: "linear-gradient(135deg, #D97706 0%, #451A03 100%)",
      bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "cpg-grandmaster-sexy",
      image: "img/cpg-grandmaster-sexy.webp",
      name: "Grandmaster Sexy",
      aka: "Scotty 2 Hotty x Oreoz",
      bank: "Compound Genetics",
      species: "Indica",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1450,
      genetics: "Scotty 2 Hotty x Oreoz",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 50,
          myrcene: 30,
          limonene: 20
      },
      flavors: [
          "Chocolate Oreoz",
          "Mantequilla Caliente",
          "Gas Kush"
      ],
      effects: [
          "Relajación Devastadora",
          "Dicha Cerebral",
          "Sueño Profundo"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Híbrido voluptuoso que cruza Scotty 2 Hotty con Oreoz. Destaca por su aroma a galletas de chocolate con crema de mantequilla dulce y su deslumbrante capa de resina blanca sobre flores violetas.",
      visualColor: "linear-gradient(135deg, #1E1B4B 0%, #431407 100%)",
      bgPattern: "radial-gradient(circle, rgba(30,27,75,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-slurricane",
      image: "img/ihg-slurricane.webp",
      name: "Slurricane",
      aka: "Do-Si-Dos x Purple Punch",
      bank: "In-House Genetics",
      species: "Indica",
      thc: 28,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 4200,
      genetics: "Do-Si-Dos x Purple Punch",
      origin: "EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          limonene: 25
      },
      flavors: [
          "Baya Dulce",
          "Ponche de Uva",
          "Crema de Masa"
      ],
      effects: [
          "Sedación Placentera",
          "Euforia Cálida",
          "Relax Corporal Total"
      ],
      activities: [
          "relax_sleep",
          "music",
          "meditation"
      ],
      description: "La variedad insignia por excelencia de In-House Genetics. Cruce de Do-Si-Dos con Purple Punch que ha conquistado el mundo entero por sus cogollos bañados en resina escarchada, sabor a mermelada de bayas dulces y una potencia de 28% de THC.",
      visualColor: "linear-gradient(135deg, #6B21A8 0%, #3B0764 100%)",
      bgPattern: "radial-gradient(circle, rgba(107,33,168,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-jelly-breath",
      image: "img/ihg-jelly-breath.webp",
      name: "Jelly Breath",
      aka: "Mendo Breath x Dosidos",
      bank: "In-House Genetics",
      species: "Indica",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 2600,
      genetics: "Mendo Breath x Dosidos",
      origin: "EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Mermelada de Bayas",
          "Vainilla Especiada",
          "Tierra Kush"
      ],
      effects: [
          "Relax Físico Intenso",
          "Euforia Alegre",
          "Calma Mental"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Exquisita variedad rica en tricomas resinosos. Une Mendo Breath con Dosidos para ofrecer un aroma complejo a mermelada de bayas maduras con fondo de galleta de vainilla y especias dulces.",
      visualColor: "linear-gradient(135deg, #9333EA 0%, #4C1D95 100%)",
      bgPattern: "radial-gradient(circle, rgba(147,51,234,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-platinum-kush-breath",
      image: "img/ihg-platinum-kush-breath.webp",
      name: "Platinum Kush Breath",
      aka: "OG Kush Breath x Platinum",
      bank: "In-House Genetics",
      species: "Indica",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 2400,
      genetics: "OG Kush Breath x Platinum",
      origin: "EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 50,
          limonene: 25,
          myrcene: 25
      },
      flavors: [
          "Gasolina OG",
          "Tierra Húmeda",
          "Mente Dulce"
      ],
      effects: [
          "Golpe Corporal",
          "Euforia Cerebral",
          "Descanso Profundo"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Una de las selecciones más potentes de la línea Platinum. Presenta flores densas de color plateado purpúreo cargadas de combustible diésel OG y tierra dulce.",
      visualColor: "linear-gradient(135deg, #475569 0%, #0F172A 100%)",
      bgPattern: "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-sugar-cane",
      image: "img/ihg-sugar-cane.webp",
      name: "Sugar Cane",
      aka: "Platinum x Slurricane",
      bank: "In-House Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 3100,
      genetics: "Platinum x Slurricane",
      origin: "EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Azúcar de Caña",
          "Uva Dulce",
          "Gasolina Suave"
      ],
      effects: [
          "Euforia Brillante",
          "Sensación Placentera",
          "Relax Físico"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "Famosa en redes sociales por producir uno de los retornos de resina más altos del mercado. Cruce directo de Platinum y Slurricane con flores completamente blancas sabor a azúcar dulce de caña y ponche de uva.",
      visualColor: "linear-gradient(135deg, #E2E8F0 0%, #64748B 100%)",
      bgPattern: "radial-gradient(circle, rgba(226,232,240,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-tart-pops",
      image: "img/ihg-tart-pops.webp",
      name: "Tart Pops",
      aka: "Sour Apple x Purple Punch",
      bank: "In-House Genetics",
      species: "Hibrida",
      thc: 25,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 1600,
      genetics: "Sour Apple x Purple Punch",
      origin: "EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          myrcene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Manzana Ácida",
          "Gominola de Uva",
          "Gas Dulce"
      ],
      effects: [
          "Euforia Feliz",
          "Sensación Placentera",
          "Relax Corporal"
      ],
      activities: [
          "social",
          "gaming",
          "music"
      ],
      description: "Híbrido súper apetecible de Sour Apple con Purple Punch. Desprende un aroma punzante a caramelos ácidos de manzana verde y tartas de mermelada de uva.",
      visualColor: "linear-gradient(135deg, #84CC16 0%, #7E22CE 100%)",
      bgPattern: "radial-gradient(circle, rgba(132,204,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-terple",
      image: "img/ihg-terple.webp",
      name: "Terple",
      aka: "Tropicana Cookies x Slurricane",
      bank: "In-House Genetics",
      species: "Hibrida",
      thc: 24,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 1900,
      genetics: "Tropicana Cookies x Slurricane",
      origin: "EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 50,
          myrcene: 25,
          caryophyllene: 25
      },
      flavors: [
          "Naranja Sangre",
          "Uva Dulce",
          "Masa de Galleta"
      ],
      effects: [
          "Euforia Creativa",
          "Energía Radiante",
          "Bienestar Físico"
      ],
      activities: [
          "social",
          "creativity",
          "nature_walk"
      ],
      description: "Obra de arte púrpura con aroma concentrado a zumo de naranja sangre recién exprimido mezclado con el dulzor berry de Slurricane. Espectacular perfil terpénico cítrico.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #9333EA 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-black-cherry-pie",
      image: "img/ihg-black-cherry-pie.webp",
      name: "Black Cherry Pie",
      aka: "Blackberry x Cherry Pie",
      bank: "In-House Genetics",
      species: "Indica",
      thc: 25,
      cbd: 0.2,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 1450,
      genetics: "Blackberry x Cherry Pie",
      origin: "EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          limonene: 25
      },
      flavors: [
          "Cereza Negra",
          "Pastel de Frutas",
          "Tierra Especiada"
      ],
      effects: [
          "Relax Corporal Suave",
          "Calma Mental",
          "Bienestar Placentero"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Una delicia frutal caracterizada por sus cálices oscuros de tono cereza negra y un humo denso con aroma a tarta de cerezas recién horneada y frutos del bosque.",
      visualColor: "linear-gradient(135deg, #991B1B 0%, #450A0A 100%)",
      bgPattern: "radial-gradient(circle, rgba(153,27,27,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-dolato",
      image: "img/ihg-dolato.webp",
      name: "Dolato",
      aka: "Do-Si-Dos x Gelato #33",
      bank: "In-House Genetics",
      species: "Indica",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 2100,
      genetics: "Do-Si-Dos x Gelato #33",
      origin: "EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Helado Creado",
          "Pino Dulce",
          "Tierra Kush"
      ],
      effects: [
          "Sedación Corporal",
          "Paz Mental",
          "Descanso"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Matrimonio perfecto entre la potencia terrosa de Do-Si-Dos y el aroma a helado de Gelato #33. Cogollos apretados como diamantes con tricomas blancos y tonos verde menta.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-trichome-storm",
      image: "img/ihg-trichome-storm.webp",
      name: "Trichome Storm",
      aka: "Slurricane #7 x Platinum",
      bank: "In-House Genetics",
      species: "Indica",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 1700,
      genetics: "Slurricane #7 x Platinum",
      origin: "EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Gasolina Dulce",
          "Uva Plata",
          "Kush Terroso"
      ],
      effects: [
          "Tormenta de Relax",
          "Euforia Placentera",
          "Sueño Profundo"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Nombrada 'Trichome Storm' por la avalancha imparable de resina que cubre sus flores de arriba a abajo. Aroma ultraintenso a diésel dulce, uvas congeladas y kush picante.",
      visualColor: "linear-gradient(135deg, #38BDF8 0%, #1E293B 100%)",
      bgPattern: "radial-gradient(circle, rgba(56,189,248,0.2) 0%, transparent 70%)"
  },
  {
id: "ihg-smackz",
      image: "img/ihg-smackz.webp",
      name: "Smackz",
      aka: "Runtz x Sol Sonic",
      bank: "In-House Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1300,
      genetics: "Runtz x Sol Sonic",
      origin: "EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Gominola Frutal",
          "Gas Combustible",
          "Cítrico Dulce"
      ],
      effects: [
          "Euforia Estallido",
          "Energía Social",
          "Relax Muscular"
      ],
      activities: [
          "social",
          "gaming",
          "music"
      ],
      description: "Potente híbrido goloso que une el perfil acaramelado de Runtz con la fuerza terpénica de Sol Sonic. Cogollos púrpura muy resinosos sabor a golosina de frutas y gas.",
      visualColor: "linear-gradient(135deg, #EC4899 0%, #A855F7 100%)",
      bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-mandarin-cookies",
      image: "img/eth-mandarin-cookies.webp",
      name: "Mandarin Cookies",
      aka: "Forum Cut GSC x Mandarin Sunset",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 3800,
      genetics: "Forum Cut GSC x Mandarin Sunset",
      origin: "Colorado, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 50,
          caryophyllene: 25,
          myrcene: 25
      },
      flavors: [
          "Mandarina Jugosa",
          "Masa de Galleta",
          "Gas Diésel"
      ],
      effects: [
          "Euforia Cerebral",
          "Energía Radiante",
          "Relax Corporal"
      ],
      activities: [
          "social",
          "creativity",
          "nature_walk"
      ],
      description: "La variedad insignia indiscutible de Ethos Genetics desarrollada por Colin Gordon. Combina la fuerza resinosa de Forum GSC con el aroma cítrico arrollador de Mandarin Sunset. Flores moradas y anaranjadas cubiertas de cristal.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-grandpas-cookies",
      image: "img/eth-grandpas-cookies.webp",
      name: "Grandpa's Cookies",
      aka: "Grandpa's Stash x Cookies & Cream",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 2700,
      genetics: "Grandpa's Stash x Cookies & Cream",
      origin: "Colorado, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Galleta de Nuez",
          "Crema Dulce",
          "Sándalo Viejo"
      ],
      effects: [
          "Relax Físico Profundo",
          "Euforia Contemplativa",
          "Calma Total"
      ],
      activities: [
          "relax_sleep",
          "music",
          "meditation"
      ],
      description: "Híbrido de gran potencia que combina genética añeja de Grandpa's Stash con Cookies & Cream. Desprende un aroma muy reconfortante a galletas caseras de nuez horneada y madera noble.",
      visualColor: "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
      bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-lilac-diesel",
      image: "img/eth-lilac-diesel.webp",
      name: "Lilac Diesel",
      aka: "SLH x Forbidden Fruit x NYC Diesel x Cherry Pie",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 25,
      cbd: 0.3,
      yieldIndoor: 600,
      yieldOutdoor: 750,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 2900,
      genetics: "(SLH x Forbidden Fruit) x (NYC Diesel x Cherry Pie)",
      origin: "Colorado, EEUU",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          caryophyllene: 30,
          pinene: 25
      },
      flavors: [
          "Flores de Lila",
          "Gasolina Diésel",
          "Pino Cítrico"
      ],
      effects: [
          "Euforia Estallido",
          "Creatividad Fluyente",
          "Energía Mental"
      ],
      activities: [
          "social",
          "creativity",
          "workout"
      ],
      description: "Una auténtica sinfonía terpenosa a cuatro bandas. Fusiona matices florales a lila silvestre con el perfume punzante de gasolina diésel, pino dulce y frutas tropicales.",
      visualColor: "linear-gradient(135deg, #C084FC 0%, #7E22CE 100%)",
      bgPattern: "radial-gradient(circle, rgba(192,132,252,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-cherry-gar-see-ya",
      image: "img/eth-cherry-gar-see-ya.webp",
      name: "Cherry Gar-See-Ya",
      aka: "Black Cherry Soda x Cherry Maduro x Mandarin Sunset",
      bank: "Ethos Genetics",
      species: "Indica",
      thc: 25,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 2100,
      genetics: "(Black Cherry Soda x Cherry Maduro) x Mandarin Sunset",
      origin: "Colorado, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 25,
          limonene: 25
      },
      flavors: [
          "Cereza Madura",
          "Gasolina Dulce",
          "Cítrico Tropical"
      ],
      effects: [
          "Relax Corporal",
          "Dicha Cerebral",
          "Sensación Cálida"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Variedad irresistible bautizada en honor al clásico sabor de helado. Ofrece un perfil goloso a cerezas negras maduras mezcladas con toques cítricos de mandarina y gas diésel.",
      visualColor: "linear-gradient(135deg, #BE123C 0%, #881337 100%)",
      bgPattern: "radial-gradient(circle, rgba(190,18,60,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-planet-of-the-grapes",
      image: "img/eth-planet-of-the-grapes.webp",
      name: "Planet of the Grapes",
      aka: "Grape Diamonds x Chem D Cookies",
      bank: "Ethos Genetics",
      species: "Indica",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 2400,
      genetics: "Grape Diamonds x Chem D Cookies",
      origin: "Colorado, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          limonene: 25
      },
      flavors: [
          "Uva Madura",
          "Gasolina Química",
          "Kush Terroso"
      ],
      effects: [
          "Sedación Devastadora",
          "Euforia Placentera",
          "Relax Total"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Una de las variedades más potentes de todo el catálogo de Ethos alcanzando el 28% de THC. Flores moradas ultraintensas con aroma a mermelada de uva recién hecha y diésel químico.",
      visualColor: "linear-gradient(135deg, #581C87 0%, #3B0764 100%)",
      bgPattern: "radial-gradient(circle, rgba(88,28,135,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-apex",
      image: "img/eth-apex.webp",
      name: "Apex",
      aka: "Mandarin Cookies x Lilac Diesel",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 600,
      yieldOutdoor: 700,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1800,
      genetics: "Mandarin Cookies x Lilac Diesel",
      origin: "Colorado, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          terpinolene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Mandarina Ácida",
          "Flores de Lila",
          "Gas Diésel"
      ],
      effects: [
          "Euforia Masiva",
          "Energía Mental",
          "Relax Corporal"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Híbrido de producción astronómica fruto del cruce de dos de las mejores cepas de Colin: Mandarin Cookies y Lilac Diesel. Flores enormes cargadas de cálices violeta y aroma cítrico floral.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #6366F1 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-candy-store",
      image: "img/eth-candy-store.webp",
      name: "Candy Store",
      aka: "Lemon Berry Candy OG x Ethos Cookies",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1950,
      genetics: "Lemon Berry Candy OG x Ethos Cookies",
      origin: "Colorado, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 50,
          myrcene: 25,
          caryophyllene: 25
      },
      flavors: [
          "Caramelo de Limón",
          "Fresa Silvestre",
          "Gas Dulce"
      ],
      effects: [
          "Euforia Risueña",
          "Sensación Placentera",
          "Relax Físico"
      ],
      activities: [
          "social",
          "music",
          "gaming"
      ],
      description: "Un auténtico escaparate de golosinas. Junta el perfil cítrico agridulce de Lemon Berry Candy OG con la resina acristalada de Ethos Cookies. Desprende un aroma muy intenso a gominolas de limón y fresa.",
      visualColor: "linear-gradient(135deg, #FACC15 0%, #EC4899 100%)",
      bgPattern: "radial-gradient(circle, rgba(250,204,21,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-member-berry",
      image: "img/eth-member-berry.webp",
      name: "Member Berry",
      aka: "Skunkberry x Mandarin Sunset",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 24,
      cbd: 0.3,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 2200,
      genetics: "Skunkberry x Mandarin Sunset",
      origin: "Colorado, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          limonene: 30,
          caryophyllene: 20
      },
      flavors: [
          "Arándano Dulce",
          "Cítrico Skunk",
          "Fruta Madura"
      ],
      effects: [
          "Euforia Nostálgica",
          "Bienestar Físico",
          "Calma Risueña"
      ],
      activities: [
          "social",
          "music"
      ],
      description: "Celebrada cepa con un sabor dulcísimo a tarta de arándanos frescos y cítricos. Sus plantas crecen con gran vigor ofreciendo cosechas de flores densas y tricomas aromáticos.",
      visualColor: "linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%)",
      bgPattern: "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-ethos-cookies",
      image: "img/eth-ethos-cookies.webp",
      name: "Ethos Cookies",
      aka: "Mandarin Cookies x Colin OG",
      bank: "Ethos Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 1750,
      genetics: "Mandarin Cookies x Colin OG",
      origin: "Colorado, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Masa de Galleta",
          "Gasolina OG",
          "Naranja Dulce"
      ],
      effects: [
          "Euforia Potente",
          "Relax Corporal",
          "Claridad Mental"
      ],
      activities: [
          "social",
          "creativity",
          "music"
      ],
      description: "Selección de bandera de la línea Cookies de Ethos. Combina la explosión de mandarinas de Mandarin Cookies con la contundencia terrosa y diésel de Colin OG.",
      visualColor: "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
      bgPattern: "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)"
  },
  {
id: "eth-colin-og",
      image: "img/eth-colin-og.webp",
      name: "Colin OG",
      aka: "Grateful Dawg x Alpha Dawg",
      bank: "Ethos Genetics",
      species: "Indica",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1600,
      genetics: "Grateful Dawg x Alpha Dawg",
      origin: "Colorado, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 50,
          myrcene: 30,
          limonene: 20
      },
      flavors: [
          "Gas Combustible",
          "Pino Picante",
          "Tierra Kush"
      ],
      effects: [
          "Sedación Knockout",
          "Euforia Pesada",
          "Relax Profundo"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "La creación personal de Colin Gordon. Un híbrido OG masivo caracterizado por su aroma a gasolina pura, pino punzante y un pegadón corporal demoledor.",
      visualColor: "linear-gradient(135deg, #1E293B 0%, #334155 100%)",
      bgPattern: "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-dosidos",
      image: "img/arc-dosidos.webp",
      name: "Dosidos",
      aka: "OGKB x Face Off OG BX1",
      bank: "Archive Seed Bank",
      species: "Indica",
      thc: 28,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 4500,
      genetics: "OGKB x Face Off OG BX1",
      origin: "Oregon, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Menta Furia",
          "Pino OG",
          "Tierra Dulce"
      ],
      effects: [
          "Euforia Devastadora",
          "Relax Corporal Total",
          "Paz Mente"
      ],
      activities: [
          "relax_sleep",
          "music",
          "meditation"
      ],
      description: "La creación más célebre en la historia de Archive Seed Bank desarrollada por Fletcher (The Docta). Cruce de OGKB con Face Off OG BX1 que revolucionó el mercado cannábico mundial por su manto de tricomas diamantinos y aroma a menta OG extremadamente potente.",
      visualColor: "linear-gradient(135deg, #15803D 0%, #166534 100%)",
      bgPattern: "radial-gradient(circle, rgba(21,128,61,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-rainbow-belts",
      image: "img/arc-rainbow-belts.webp",
      name: "Rainbow Belts",
      aka: "Zkittlez x Moonbow #75",
      bank: "Archive Seed Bank",
      species: "Hibrida",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 60,
      rating: 5.0,
      reviewsCount: 3600,
      genetics: "Zkittlez x Moonbow #75",
      origin: "Oregon, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 50,
          caryophyllene: 25,
          linalool: 25
      },
      flavors: [
          "Gominola Arcoíris",
          "Cítrico Dulce",
          "Gasolina Kush"
      ],
      effects: [
          "Euforia Alegre",
          "Dicha Estallido",
          "Relax Placentero"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Ganadora de múltiples copas internacionales y aclamada como uno de los mejores híbridos Zkittlez jamás creados. Combina el sabor intenso a golosinas de frutas con el empuje terpénico diésel de Moonbow.",
      visualColor: "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
      bgPattern: "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-moonbow",
      image: "img/arc-moonbow.webp",
      name: "Moonbow",
      aka: "Zkittlez x Face Off OG",
      bank: "Archive Seed Bank",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 65,
      rating: 4.9,
      reviewsCount: 2800,
      genetics: "Zkittlez x Face Off OG",
      origin: "Oregon, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Caramelo de Frutas",
          "Gas Combustible",
          "Tierra Kush"
      ],
      effects: [
          "Euforia Radiante",
          "Relax Corporal Profundo",
          "Calma Mental"
      ],
      activities: [
          "social",
          "music",
          "meditation"
      ],
      description: "Una verdadera obra maestra moderna. Combina el perfil organoléptico dulcísimo a caramelos de Zkittlez con la fuerza pura y resina pesada del clon Face Off OG.",
      visualColor: "linear-gradient(135deg, #A855F7 0%, #3B82F6 100%)",
      bgPattern: "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-face-off-og",
      image: "img/arc-face-off-og.webp",
      name: "Face Off OG",
      aka: "Face Off OG IBL",
      bank: "Archive Seed Bank",
      species: "Indica",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 450,
      yieldOutdoor: 550,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 3100,
      genetics: "707 OG Kush Selection",
      origin: "California / Oregon, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 50,
          caryophyllene: 30,
          limonene: 20
      },
      flavors: [
          "Gasolina Diésel",
          "Pino Picante",
          "Tierra Húmeda"
      ],
      effects: [
          "Sedación Knockout",
          "Euforia Pesada",
          "Relajación Total"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "El clon pilar fundamental sobre el que se fundó Archive Seed Bank. Famoso por su efecto 'Face Off' tan potente que produce una sedación corporal aplastante y un aroma punzante a gasolina OG y pino.",
      visualColor: "linear-gradient(135deg, #1E293B 0%, #0F172A 100%)",
      bgPattern: "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-rudeboi-og",
      image: "img/arc-rudeboi-og.webp",
      name: "RudeBoi OG",
      aka: "Irene OG x Face Off OG BX1",
      bank: "Archive Seed Bank",
      species: "Indica",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 65,
      rating: 4.8,
      reviewsCount: 1900,
      genetics: "Irene OG x Face Off OG BX1",
      origin: "Oregon, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 35,
          limonene: 20
      },
      flavors: [
          "Gasolina Kush",
          "Pimienta Negra",
          "Tierra de Bosque"
      ],
      effects: [
          "Efecto Corporal Pesado",
          "Calma Mente",
          "Sueño Placentero"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Cruce de la legendaria Irene OG de Atlanta con Face Off OG BX1. Ofrece flores apretadas cargadas de cálices verde oscuro y resina con olor picante a gas pimienta y tierra de bosque.",
      visualColor: "linear-gradient(135deg, #334155 0%, #1E293B 100%)",
      bgPattern: "radial-gradient(circle, rgba(51,65,85,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-valley-girl",
      image: "img/arc-valley-girl.webp",
      name: "Valley Girl",
      aka: "SFV OG x Face Off OG BX1",
      bank: "Archive Seed Bank",
      species: "Indica",
      thc: 25,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1750,
      genetics: "SFV OG x Face Off OG BX1",
      origin: "Oregon, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          limonene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Limón OG",
          "Pino Sol",
          "Tierra Húmeda"
      ],
      effects: [
          "Euforia Alegre",
          "Relax Físico Cálido",
          "Bienestar"
      ],
      activities: [
          "social",
          "relax_sleep"
      ],
      description: "Excelente cruce entre la clásica San Fernando Valley OG (SFV OG) y Face Off OG BX1. Brinda un perfume clásico a pino con limón fresco y una resina brillante muy viscosa.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #15803D 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-dank-dough",
      image: "img/arc-dank-dough-curedbud.webp",
      name: "Dank Dough",
      aka: "Gelato #41 x Moonbow #75",
      bank: "Archive Seed Bank",
      species: "Hibrida",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 1650,
      genetics: "Gelato #41 x Moonbow #75",
      origin: "Oregon, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 35,
          myrcene: 20
      },
      flavors: [
          "Masa de Galleta",
          "Gasolina Dulce",
          "Helado Creado"
      ],
      effects: [
          "Euforia Cerebral",
          "Relax Físico",
          "Dicha Risueña"
      ],
      activities: [
          "social",
          "music",
          "gaming"
      ],
      description: "Una delicia gastronómica que combina la potencia cremosa de Gelato #41 con la dulzura acaramelada y a gas de Moonbow #75. Cosechas cargadas de flores púrpura-plata.",
      visualColor: "linear-gradient(135deg, #7C3AED 0%, #DB2777 100%)",
      bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-double-cross",
      image: "img/arc-double-cross-official.webp",
      name: "Double Cross",
      aka: "Moonbow #73 x Face Off OG",
      bank: "Archive Seed Bank",
      species: "Indica",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1500,
      genetics: "Moonbow #73 x Face Off OG",
      origin: "Oregon, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Gas Combustible",
          "Caramelo de Uva",
          "Pino Kush"
      ],
      effects: [
          "Golpe Corporal Masivo",
          "Euforia Alegre",
          "Sueño Profundo"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Potente retrocruce entre Moonbow #73 y Face Off OG. Genera plantas con una cobertura de tricomas exagerada y un aroma denso a combustible diésel y fruta dulce.",
      visualColor: "linear-gradient(135deg, #475569 0%, #1E1B4B 100%)",
      bgPattern: "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-memory-loss",
      image: "img/arc-memory-loss.webp",
      name: "Memory Loss",
      aka: "Amnesia Haze x Face Off OG",
      bank: "Archive Seed Bank",
      species: "Sativa",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 70,
      rating: 4.8,
      reviewsCount: 1850,
      genetics: "Amnesia Haze x Face Off OG",
      origin: "Oregon, EEUU",
      dominantTerpene: "terpinolene",
      terpenes: {
          terpinolene: 45,
          limonene: 30,
          caryophyllene: 25
      },
      flavors: [
          "Limón Especiado",
          "Gasolina Haze",
          "Incienso Dulce"
      ],
      effects: [
          "Euforia Psicoactiva",
          "Energía Mental",
          "Desconexión Total"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Nombrada 'Memory Loss' por su deslumbrante efecto cerebral que hace olvidar las preocupaciones diarias. Une la mítica Amnesia Haze holandesa con la pegada diésel de Face Off OG.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
id: "arc-z-mints",
      image: "img/arc-z-mints.webp",
      name: "Z-Mints",
      aka: "Zkittlez x SinMint Cookies",
      bank: "Archive Seed Bank",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 63,
      rating: 4.8,
      reviewsCount: 1400,
      genetics: "Zkittlez x SinMint Cookies",
      origin: "Oregon, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          menthol: 25
      },
      flavors: [
          "Gominola de Menta",
          "Caramelo de Frutas",
          "Tierra Dulce"
      ],
      effects: [
          "Euforia Fresca",
          "Relax Físico",
          "Sensación Placentera"
      ],
      activities: [
          "social",
          "music",
          "nature_walk"
      ],
      description: "Híbrido de sabor súper refrescante que cruza Zkittlez con SinMint Cookies. Produce cogollos ultra duros con aroma a golosinas de fruta con toque de menta fría.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #8B5CF6 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-stuffed-french-toast",
      image: "img/raw-stuffed-french-toast.webp",
      name: "Stuffed French Toast",
      aka: "Paris OG x French Toast",
      bank: "Raw Genetics",
      species: "Indica",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 3900,
      genetics: "Paris OG x French Toast",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Tostada de Canela",
          "Jarabe de Arce",
          "Gasolina OG"
      ],
      effects: [
          "Euforia Risueña",
          "Sedación Placentera",
          "Relax Total"
      ],
      activities: [
          "relax_sleep",
          "music",
          "meditation"
      ],
      description: "La creación insignia indiscutible de Raw Genetics. Combina la potencia diésel de Paris OG con el aroma dulce y especiado a torrijas con canela y jarabe de arce de French Toast. Cogollos blancos cargados de resina.",
      visualColor: "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
      bgPattern: "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-georgia-pie",
      image: "img/raw-georgia-pie.webp",
      name: "Georgia Pie",
      aka: "Gellati x Kush Mints",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 3200,
      genetics: "Gellati x Kush Mints",
      origin: "California, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          myrcene: 25
      },
      flavors: [
          "Melocotón Dulce",
          "Pastel de Nuez",
          "Gasolina OG"
      ],
      effects: [
          "Euforia Cerebral",
          "Relax Físico",
          "Sensación Cálida"
      ],
      activities: [
          "social",
          "music",
          "creativity"
      ],
      description: "Célebre variedad desarrollada en colaboración con Cookies. Destaca por su inconfundible aroma a tarta de melocotón recién horneada con notas a menta fresca y gasolina diésel.",
      visualColor: "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
      bgPattern: "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-cherry-paloma",
      image: "img/raw-cherry-paloma.webp",
      name: "Cherry Paloma",
      aka: "Tropicana Cookies x Georgia Pie",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 2100,
      genetics: "Tropicana Cookies x Georgia Pie",
      origin: "California, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 50,
          myrcene: 25,
          caryophyllene: 25
      },
      flavors: [
          "Cereza Ácida",
          "Pomelo Rosado",
          "Gas Dulce"
      ],
      effects: [
          "Euforia Vibrante",
          "Energía Social",
          "Dicha Cerebral"
      ],
      activities: [
          "social",
          "gaming",
          "nature_walk"
      ],
      description: "Exótico cóctel cannábico que une Tropicana Cookies con Georgia Pie. Presenta flores de un violeta púrpura intenso con aroma cítrico a refresco de pomelo rosado y cerezas silvestres.",
      visualColor: "linear-gradient(135deg, #E11D48 0%, #991B1B 100%)",
      bgPattern: "radial-gradient(circle, rgba(225,29,72,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-apples-and-french-toast",
      image: "img/raw-apples-and-french-toast.webp",
      name: "Apples & French Toast",
      aka: "Apples & Bananas x Stuffed French Toast",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 5.0,
      reviewsCount: 2400,
      genetics: "Apples & Bananas x Stuffed French Toast",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Tarta de Manzana",
          "Canela Dulce",
          "Gas Combustible"
      ],
      effects: [
          "Euforia Potente",
          "Relax Corporal",
          "Dicha Mente"
      ],
      activities: [
          "creativity",
          "social",
          "music"
      ],
      description: "Cruza dos de las mejores cepas modernas: Apples & Bananas con Stuffed French Toast. Un espectáculo visual y aromático a tarta de manzana crujiente con canela y diésel fino.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #D97706 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-marshmallow",
      image: "img/raw-marshmallow.webp",
      name: "Raw Marshmallow",
      aka: "Marshmallow OG x Stuffed French Toast",
      bank: "Raw Genetics",
      species: "Indica",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.9,
      reviewsCount: 1800,
      genetics: "Marshmallow OG x Stuffed French Toast",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          myrcene: 30,
          limonene: 25
      },
      flavors: [
          "Nube de Azúcar",
          "Tostada Dulce",
          "Pino OG"
      ],
      effects: [
          "Sedación Placentera",
          "Paz Corporal",
          "Sueño Reparador"
      ],
      activities: [
          "relax_sleep",
          "meditation"
      ],
      description: "Variedad golosa de alta gama. Mezcla el aroma a nubes de azucar tostadas de Marshmallow OG con las notas especiadas de Stuffed French Toast. Cobertura de resina blanca impresionante.",
      visualColor: "linear-gradient(135deg, #F43F5E 0%, #FB7185 100%)",
      bgPattern: "radial-gradient(circle, rgba(244,63,94,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-rainbow-studz",
      image: "img/raw-rainbow-studz.webp",
      name: "Rainbow Studz",
      aka: "Zkittlez x Rainbow Chip",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 58,
      rating: 4.8,
      reviewsCount: 1600,
      genetics: "Zkittlez x Rainbow Chip",
      origin: "California, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 50,
          caryophyllene: 25,
          linalool: 25
      },
      flavors: [
          "Gominola Frutal",
          "Caramelo Dulce",
          "Kush Gasolina"
      ],
      effects: [
          "Euforia Alegre",
          "Energía Social",
          "Relax Muscular"
      ],
      activities: [
          "social",
          "gaming",
          "music"
      ],
      description: "Una verdadera golosina cannábica. Junta el inconfundible perfil de caramelos de Zkittlez con Rainbow Chip para producir flores violetas cargadas de resina terpénica agridulce.",
      visualColor: "linear-gradient(135deg, #8B5CF6 0%, #C084FC 100%)",
      bgPattern: "radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-peeled-banana",
      image: "img/raw-peeled-banana.webp",
      name: "Peeled Banana",
      aka: "Banana OG x Stuffed French Toast",
      bank: "Raw Genetics",
      species: "Indica",
      thc: 27,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1750,
      genetics: "Banana OG x Stuffed French Toast",
      origin: "California, EEUU",
      dominantTerpene: "myrcene",
      terpenes: {
          myrcene: 45,
          caryophyllene: 30,
          limonene: 25
      },
      flavors: [
          "Plátano Maduro",
          "Mantequilla Dulce",
          "Gas Combustible"
      ],
      effects: [
          "Relax Corporal Intenso",
          "Euforia Risueña",
          "Descanso"
      ],
      activities: [
          "relax_sleep",
          "music"
      ],
      description: "Delicioso híbrido de plátano cremoso. Mezcla Banana OG con Stuffed French Toast para dar paso a un humo muy denso con sabor a plátano flambeado en mantequilla y diésel.",
      visualColor: "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
      bgPattern: "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-runtz-pop",
      image: "img/raw-runtz-pop.webp",
      name: "Runtz Pop",
      aka: "Runtz x Red Pop",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 27,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1500,
      genetics: "Runtz x Red Pop",
      origin: "California, EEUU",
      dominantTerpene: "limonene",
      terpenes: {
          limonene: 45,
          caryophyllene: 30,
          linalool: 25
      },
      flavors: [
          "Refresco de Cereza",
          "Caramelo Runtz",
          "Gas Dulce"
      ],
      effects: [
          "Euforia Radiante",
          "Dicha Cerebral",
          "Relax Físico"
      ],
      activities: [
          "social",
          "creativity",
          "gaming"
      ],
      description: "Variedad súper aromática que une Runtz con Red Pop. Presenta flores con matices rojos y violetas sabor a refresco dulce de cereza e incienso frutal.",
      visualColor: "linear-gradient(135deg, #DC2626 0%, #991B1B 100%)",
      bgPattern: "radial-gradient(circle, rgba(220,38,38,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-bacio-zkittlez",
      image: "img/raw-bacio-zkittlez.webp",
      name: "Bacio Zkittlez",
      aka: "Bacio Gelato x Zkittlez",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 26,
      cbd: 0.2,
      yieldIndoor: 500,
      yieldOutdoor: 600,
      floweringDays: 60,
      rating: 4.8,
      reviewsCount: 1400,
      genetics: "Bacio Gelato x Zkittlez",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 45,
          limonene: 30,
          myrcene: 25
      },
      flavors: [
          "Helado Creado",
          "Caramelo Frutal",
          "Gas Kush"
      ],
      effects: [
          "Euforia Placentera",
          "Relax Físico",
          "Calma Mente"
      ],
      activities: [
          "social",
          "music",
          "nature_walk"
      ],
      description: "Selección de gran calibre que cruza Bacio Gelato #41 con Zkittlez. Combina el sabor cremoso a helado de avellana con el toque dulce acaramelado de Zkittlez.",
      visualColor: "linear-gradient(135deg, #7C3AED 0%, #4338CA 100%)",
      bgPattern: "radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 70%)"
  },
  {
      id: "raw-zweet-inzanity",
      image: "img/raw-zweet-inzanity.webp",
      name: "Zweet Inzanity",
      aka: "Zkittlez x Gorilla Glue #4",
      bank: "Raw Genetics",
      species: "Hibrida",
      thc: 28,
      cbd: 0.1,
      yieldIndoor: 550,
      yieldOutdoor: 650,
      floweringDays: 63,
      rating: 4.9,
      reviewsCount: 1650,
      genetics: "Zkittlez x Gorilla Glue #4",
      origin: "California, EEUU",
      dominantTerpene: "caryophyllene",
      terpenes: {
          caryophyllene: 50,
          limonene: 25,
          myrcene: 25
      },
      flavors: [
          "Caramelo Dulce",
          "Gasolina Pegajosa",
          "Pino OG"
      ],
      effects: [
          "Euforia Locura",
          "Pegada Corporal",
          "Relax Profundo"
      ],
      activities: [
          "relax_sleep",
          "gaming"
      ],
      description: "Una auténtica locura de resina y sabor. Une la dulzura frutal de Zkittlez con la pegajosidad extrema de GG4, produciendo cogollos pesados como piedras empapados en cristales.",
      visualColor: "linear-gradient(135deg, #10B981 0%, #047857 100%)",
      bgPattern: "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)"
  }
];



// --- matcher.js ---
// CannaCatalog 2.0 - Ruleta & Matcher de Actividades


class ActivityMatcher {
  constructor(containerId, resultId) {
    this.container = document.getElementById(containerId);
    this.resultContainer = document.getElementById(resultId);
    this.audioCtx = null;
    this.recentWinners = new Map(); // Historial de ganadores recientes por actividad
  }

  initAudio() {
    if (!this.audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.audioCtx = new AudioContext();
      }
    }
  }

  playClickSound(freq = 440) {
    try {
      this.initAudio();
      if (!this.audioCtx) return;
      if (this.audioCtx.state === 'suspended') {
        this.audioCtx.resume();
      }
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);
      gain.gain.setValueAtTime(0.05, this.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + 0.08);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start();
      osc.stop(this.audioCtx.currentTime + 0.08);
    } catch (e) {
      // Audio fallback silencioso
    }
  }

  findMatches(activityId) {
    const activity = ACTIVITIES_DATA.find(a => a.id === activityId);
    if (!activity) return STRAINS_DATABASE;

    const recommended = activity.recommendedSpecies || [];

    // Puntuación por coincidencia de terpenos, especie y actividad
    const scoredStrains = STRAINS_DATABASE.map(strain => {
      let score = 0;
      // Coincidencia con especie recomendada
      if (recommended.includes(strain.species)) {
        score += 50;
      }
      // Coincidencia con terpeno dominante
      if (activity.preferredTerpenes && activity.preferredTerpenes.includes(strain.dominantTerpene)) {
        score += 30;
      }
      // Coincidencia con actividad explícita
      if (strain.activities && strain.activities.includes(activityId)) {
        score += 40;
      }
      // Puntuación por rating
      score += (strain.rating * 5);

      return { strain, score };
    });

    scoredStrains.sort((a, b) => b.score - a.score);

    // Filtrar prioritariamente cepas que correspondan a las especies recomendadas
    const matchingSpeciesStrains = scoredStrains
      .filter(s => recommended.includes(s.strain.species))
      .map(s => s.strain);

    return matchingSpeciesStrains.length > 0 ? matchingSpeciesStrains : scoredStrains.map(s => s.strain);
  }

  spinRoulette(activityId, onComplete) {
    const matchedStrains = this.findMatches(activityId);
    if (!matchedStrains.length) return;

    // Seleccionar pool de candidatas top de la especie recomendada
    const topCandidates = matchedStrains.slice(0, Math.min(matchedStrains.length, 12));

    // Filtrar para evitar repetir la misma genética consecutivamente en esa actividad
    const lastWinnerId = this.recentWinners.get(activityId);
    const availableCandidates = topCandidates.filter(c => c.id !== lastWinnerId);
    const candidatePool = availableCandidates.length > 0 ? availableCandidates : topCandidates;

    // Elegir aleatoriamente una ganadora diferente del pool de esa especie
    const winnerIndex = Math.floor(Math.random() * candidatePool.length);
    const winner = candidatePool[winnerIndex];

    // Registrar en el historial de ganadores recientes
    this.recentWinners.set(activityId, winner.id);

    // Secuencia aleatoria variada para la animación del giro
    const animationSequence = [...matchedStrains].sort(() => Math.random() - 0.5);

    let spinsLeft = 22;
    let speed = 50;
    let index = 0;

    const spinStep = () => {
      index = (index + 1) % animationSequence.length;
      const currentStrain = animationSequence[index];
      
      this.playClickSound(300 + (index % 10) * 30);
      this.renderWheelPreview(currentStrain);

      spinsLeft--;
      if (spinsLeft > 0) {
        speed += 12; // desaceleración progresiva
        setTimeout(spinStep, speed);
      } else {
        // Elección final única y variada del mismo tipo
        this.playClickSound(880);
        this.renderWinner(winner, ACTIVITIES_DATA.find(a => a.id === activityId));
        if (onComplete) onComplete(winner);
      }
    };

    spinStep();
  }


  renderWheelPreview(strain) {
    if (!this.resultContainer) return;
    this.resultContainer.innerHTML = `
      <div class="wheel-preview-card spinning-active">
        <div class="badge-species ${strain.species.toLowerCase()}">${strain.species}</div>
        <h3>${strain.name}</h3>
        <p class="thc-badge">THC: ${strain.thc}% | Terpeno: ${TERPENES_INFO[strain.dominantTerpene]?.name || strain.dominantTerpene}</p>
      </div>
    `;
  }

  renderWinner(strain, activity) {
    if (!this.resultContainer) return;
    const terpeneData = TERPENES_INFO[strain.dominantTerpene];
    const strainImg = strain.image;

    this.resultContainer.innerHTML = `
      <div class="winner-card glow-card" style="${strainImg ? 'display: grid; grid-template-columns: minmax(180px, 240px) 1fr; gap: 1.2rem; align-items: center;' : ''}">
        ${strainImg ? `
        <div class="winner-photo-wrapper" style="width: 100%; height: 200px; border-radius: var(--radius-md); overflow: hidden; position: relative; background: #080C0B; border: 1px solid var(--glass-border); display: flex; align-items: center; justify-content: center;">
          <img src="${strainImg}" alt="${strain.name}" style="max-width: 100%; max-height: 100%; object-fit: contain;" onerror="this.style.display='none';" />
          <div style="position: absolute; bottom: 8px; left: 8px; background: rgba(0,0,0,0.7); padding: 2px 8px; border-radius: 99px; font-size: 0.72rem; color: var(--primary-emerald); border: 1px solid rgba(16,185,129,0.3);">
            🏛️ ${strain.bank}
          </div>
        </div>` : ''}

        <div>
          <div class="winner-header">
            <span class="winner-badge">🎯 MATCH PERFECTO</span>
            <span class="activity-pill">${activity ? activity.title : 'Tu Plan'}</span>
          </div>
          <div class="winner-body">
            <h2 class="winner-title" style="margin-top: 0.4rem;">${strain.name} <small>(${strain.species})</small></h2>
            <div class="strain-metrics" style="margin: 0.6rem 0;">
              <span class="metric">🔥 THC ${strain.thc}%</span>
              <span class="metric">💧 CBD ${strain.cbd}%</span>
              <span class="metric" style="background: ${terpeneData?.color || '#10B981'}22; color: ${terpeneData?.color || '#10B981'}; border: 1px solid ${terpeneData?.color || '#10B981'}">
                🌿 Terpeno: ${terpeneData?.name || strain.dominantTerpene}
              </span>
            </div>
            <p class="winner-desc">${strain.description}</p>
            <div class="winner-actions" style="margin-top: 1rem;">
              <button class="btn btn-primary" onclick="document.dispatchEvent(new CustomEvent('openStrainDetail', { detail: '${strain.id}' }))">
                🔍 Ver Ficha Técnica Completa
              </button>
              <button class="btn btn-accent" onclick="document.dispatchEvent(new CustomEvent('generateMission', { detail: { strainId: '${strain.id}', activityId: '${activity ? activity.id : ''}' } }))">
                🚀 Generar Misión Temática
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
  }
}



// --- bitacora.js ---
// CannaCatalog 2.0 - Bitácora de Vivencias y Safari de Caminatas (Stash & Logbook)

class BitacoraManager {
  constructor() {
    this.STORAGE_KEY_LOGS = 'cannacatalog_walk_logs_v2';
    this.STORAGE_KEY_STASH = 'cannacatalog_user_stash_v2';
    this.logs = this.loadLogs();
    this.stash = this.loadStash();
  }

  loadLogs() {
    try {
      const data = localStorage.getItem(this.STORAGE_KEY_LOGS);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Error cargando bitácora', e);
      return [];
    }
  }

  saveLogs() {
    try {
      localStorage.setItem(this.STORAGE_KEY_LOGS, JSON.stringify(this.logs));
    } catch (e) {
      console.error('Error guardando bitácora', e);
    }
  }

  loadStash() {
    try {
      const data = localStorage.getItem(this.STORAGE_KEY_STASH);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  saveStash() {
    try {
      localStorage.setItem(this.STORAGE_KEY_STASH, JSON.stringify(this.stash));
    } catch (e) {
      console.error('Error guardando stash', e);
    }
  }

  toggleStash(strainId) {
    const index = this.stash.indexOf(strainId);
    if (index > -1) {
      this.stash.splice(index, 1);
    } else {
      this.stash.push(strainId);
    }
    this.saveStash();
    return this.isInStash(strainId);
  }

  isInStash(strainId) {
    return this.stash.includes(strainId);
  }

  addLog(entry) {
    const newLog = {
      id: 'log_' + Date.now(),
      date: new Date().toLocaleDateString('es-ES', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' }),
      strainName: entry.strainName || 'Cepa no especificada',
      location: entry.location || 'Ruta / Parque no especificado',
      preMood: entry.preMood || 'Neutral',
      postMood: entry.postMood || 'Excelente',
      rating: parseInt(entry.rating || 5),
      photoUrl: entry.photoUrl || null,
      notes: entry.notes || ''
    };

    this.logs.unshift(newLog);
    this.saveLogs();
    return newLog;
  }

  deleteLog(logId) {
    this.logs = this.logs.filter(l => l.id !== logId);
    this.saveLogs();
  }

  renderLogList(containerElement) {
    if (!containerElement) return;

    if (this.logs.length === 0) {
      containerElement.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">📖</div>
          <h3>Tu diario de Vivencias está vacío</h3>
          <p>Registra tu primera vivencia, momento o sesión de cata con tus cepas favoritas.</p>
        </div>
      `;
      return;
    }

    containerElement.innerHTML = this.logs.map(log => `
      <div class="log-card glass-panel" id="${log.id}">
        <div class="log-card-header">
          <div>
            <h4 class="log-strain">${this.escapeHtml(log.strainName)}</h4>
            <span class="log-location">📍 ${this.escapeHtml(log.location)}</span>
          </div>
          <div class="log-date">${log.date}</div>
        </div>
        ${log.photoUrl ? `
          <div class="log-photo-container">
            <img src="${log.photoUrl}" alt="Foto de cata / paseo" class="log-photo-img" style="cursor: zoom-in;" onclick="window.app && window.app.openImageLightbox('${log.photoUrl}', '${this.escapeHtml(log.strainName)}', 'Foto de Vivencia')" title="Ampliar foto HD 🔍" />
          </div>
        ` : ''}
        <div class="log-details">
          <div class="log-mood-pills">
            <span class="mood-pill pre">Antes: ${this.escapeHtml(log.preMood)}</span>
            <span class="mood-pill post">Después: ${this.escapeHtml(log.postMood)}</span>
          </div>
          <div class="log-stars">
            ${'★'.repeat(log.rating)}${'☆'.repeat(5 - log.rating)}
          </div>
        </div>
        ${log.notes ? `<p class="log-notes">"${this.escapeHtml(log.notes)}"</p>` : ''}
        <div class="log-card-footer">
          <button class="btn btn-danger-sm" onclick="document.dispatchEvent(new CustomEvent('deleteLog', { detail: '${log.id}' }))">
            🗑️ Eliminar Registro
          </button>
        </div>
      </div>
    `).join('');
  }

  escapeHtml(str) {
    return String(str).replace(/[&<>"']/g, function(m) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
      }[m];
    });
  }
}



// --- missions.js ---
// CannaCatalog 2.0 - Generador de Misiones Temáticas


class MissionGenerator {
  static generateMission(strainId, activityId) {
    const strain = STRAINS_DATABASE.find(s => s.id === strainId) || STRAINS_DATABASE[0];
    const dominantTerpene = strain.dominantTerpene;

    const missionTemplates = {
      nature_walk: [
        {
          title: "🌲 Misión: Explorador Cromático de la Naturaleza",
          tasks: [
            "Ponte unos auriculares con tu lista de reproducción instrumental / synthwave favorita.",
            "Camina a ritmo moderado durante 20 minutos por un parque o ruta arbolada.",
            "Encuentra 3 elementos naturales con tonalidades de verde o púrpura de intensidad increíble.",
            "Detente un minuto, respira hondo y siente la brisa del aire libre."
          ],
          audioStyle: "Ambient / Natural Waves",
          targetTerpene: "limonene"
        },
        {
          title: "🦅 Misión: Rastreador de Detalle Floral",
          tasks: [
            "Camina despacio prestando atención a los aromas del entorno (tierra, pinos, flores).",
            "Saca una fotografía de primer plano de la textura de la corteza de un árbol antiguo.",
            "Disfruta de la perspectiva y el paisaje circundante."
          ],
          audioStyle: "Lofi Beats / Acoustic Chill",
          targetTerpene: "pinene"
        }
      ],
      gaming: [
        {
          title: "⚔️ Misión: Enfoque Táctico & Inmersión Co-Op",
          tasks: [
            "Asegura una postura cómoda y ajusta la iluminación de la sala a tono tenue / neón.",
            "Ten a mano una botella de agua fresca y tus snacks favoritos.",
            "Juega una partida enfocado en la creatividad estratégica o explora el mapa a tu ritmo."
          ],
          audioStyle: "Synthwave / Cyberpunk Soundtrack",
          targetTerpene: "caryophyllene"
        }
      ],
      creativity: [
        {
          title: "🎨 Misión: Flujo sin Filtros & Creación Libre",
          tasks: [
            "Abre un lienzo en blanco, libreta de notas o tu software de composición musical.",
            "No te preocupes por el resultado final: crea ideas o bocetos durante 30 minutos ininterrumpidos.",
            "Déjate llevar por las notas terpénicas de la variedad."
          ],
          audioStyle: "Chillhop / Jazz Hop",
          targetTerpene: "terpinolene"
        }
      ],
      social: [
        {
          title: "🗣️ Misión: La Tertulia de las Grandes Ideas",
          tasks: [
            "Reúnete con buenos amigos o inicia una charla sobre temas espaciales, futuros o filosóficos.",
            "Sugerencia de debate: ¿Cuál sería tu itinerario perfecto de viaje en el tiempo?",
            "Comparte la experiencia organoléptica y los aromas de tu cepa."
          ],
          audioStyle: "Funk / Neo Soul",
          targetTerpene: "limonene"
        }
      ],
      relax_sleep: [
        {
          title: "🌙 Misión: Santuario de Desconexión Total",
          tasks: [
            "Baja la intensidad de la luz y apaga las notificaciones del móvil.",
            "Pon tu película o documental de naturaleza favorito.",
            "Realiza 5 respiraciones profundas contando 4 segundos al inhalar y 6 al exhalar."
          ],
          audioStyle: "Deep Sleep / Binaural Beats",
          targetTerpene: "myrcene"
        }
      ]
    };

    const categoryMissions = missionTemplates[activityId] || missionTemplates.nature_walk;
    const selectedMission = categoryMissions[Math.floor(Math.random() * categoryMissions.length)];

    return {
      id: 'mission_' + Date.now(),
      strainName: strain.name,
      strainSpecies: strain.species,
      terpeneName: TERPENES_INFO[dominantTerpene]?.name || dominantTerpene,
      title: selectedMission.title,
      tasks: selectedMission.tasks,
      audioStyle: selectedMission.audioStyle
    };
  }

  static renderMissionModal(missionData, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="mission-card glass-panel glow-purple">
        <div class="mission-header">
          <span class="mission-tag">🎮 MISIÓN ACTIVA</span>
          <span class="mission-strain">Cepa: ${missionData.strainName} (${missionData.strainSpecies})</span>
        </div>
        <h3 class="mission-title">${missionData.title}</h3>
        <div class="mission-terpene-hint">
          <span>🌿 Potenciado por Terpeno: <strong>${missionData.terpeneName}</strong></span>
          <span>🎧 Banda Sonora Recomendada: <strong>${missionData.audioStyle}</strong></span>
        </div>
        <div class="mission-tasks">
          <h4>Objetivos de la Experiencia:</h4>
          <ul>
            ${missionData.tasks.map(t => `<li><span class="check-box"></span> ${t}</li>`).join('')}
          </ul>
        </div>
        <div class="mission-footer">
          <button class="btn btn-primary" onclick="document.dispatchEvent(new CustomEvent('closeMissionModal'))">
            ✅ ¡Aceptar Misión!
          </button>
        </div>
      </div>
    `;
  }
}



// --- audio.js ---
// CannaCatalog 2.0 MAX - Generador de Paisajes Sonoros & Botón Modo Sobrio

class AmbientAudioEngine {
  constructor() {
    this.audioCtx = null;
    this.activeNodes = [];
    this.isPlaying = false;
  }

  init() {
    if (!this.audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.audioCtx = new AudioContext();
    }
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  stopAll() {
    this.activeNodes.forEach(node => {
      try {
        if (node.stop) node.stop();
        if (node.disconnect) node.disconnect();
      } catch (e) {}
    });
    this.activeNodes = [];
    this.isPlaying = false;
  }

  playSolfeggio432Hz() {
    this.stopAll();
    this.init();

    // Tono Solfeggio 432Hz (Relajación profunda)
    const osc = this.audioCtx.createOscillator();
    const gain = this.audioCtx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(432, this.audioCtx.currentTime);

    // Oscilador LFO para pulso suave
    const lfo = this.audioCtx.createOscillator();
    const lfoGain = this.audioCtx.createGain();
    lfo.frequency.setValueAtTime(0.2, this.audioCtx.currentTime);
    lfoGain.gain.setValueAtTime(0.02, this.audioCtx.currentTime);

    lfo.connect(gain.gain);
    gain.gain.setValueAtTime(0.08, this.audioCtx.currentTime);

    osc.connect(gain);
    gain.connect(this.audioCtx.destination);

    osc.start();
    lfo.start();

    this.activeNodes.push(osc, lfo, gain);
    this.isPlaying = true;
  }

  playPinkNoise() {
    this.stopAll();
    this.init();

    const bufferSize = this.audioCtx.sampleRate * 2;
    const buffer = this.audioCtx.createBuffer(1, bufferSize, this.audioCtx.sampleRate);
    const data = buffer.getChannelData(0);

    let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
    for (let i = 0; i < bufferSize; i++) {
      const white = Math.random() * 2 - 1;
      b0 = 0.99886 * b0 + white * 0.0555179;
      b1 = 0.99332 * b1 + white * 0.0750759;
      b2 = 0.96900 * b2 + white * 0.1538520;
      b3 = 0.86650 * b3 + white * 0.3104856;
      b4 = 0.55000 * b4 + white * 0.5329522;
      b5 = -0.7616 * b5 - white * 0.0168980;
      data[i] = b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362;
      data[i] *= 0.03; // Volumen suave
      b6 = white * 0.115926;
    }

    const noise = this.audioCtx.createBufferSource();
    noise.buffer = buffer;
    noise.loop = true;

    const filter = this.audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(800, this.audioCtx.currentTime);

    const gain = this.audioCtx.createGain();
    gain.gain.setValueAtTime(0.12, this.audioCtx.currentTime);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(this.audioCtx.destination);

    noise.start();
    this.activeNodes.push(noise, filter, gain);
    this.isPlaying = true;
  }
}



// --- tools.js ---
// CannaCatalog 2.0 MAX - Herramientas Avanzadas (Mezclador, Comparador, Vaporización & Temas)


class AdvancedTools {

  /* ----------------------------------------------------
     1. COMPARADOR DE CEPAS FRENTE A FRENTE
     ---------------------------------------------------- */
  static compareStrains(strainId1, strainId2) {
    const s1 = STRAINS_DATABASE.find(s => s.id === strainId1);
    const s2 = STRAINS_DATABASE.find(s => s.id === strainId2);

    if (!s1 || !s2) return null;

    return {
      strain1: s1,
      strain2: s2,
      thcDiff: s1.thc - s2.thc,
      cbdDiff: s1.cbd - s2.cbd,
      terpeneMatch: s1.dominantTerpene === s2.dominantTerpene
    };
  }

  /* ----------------------------------------------------
     2. MEZCLADOR DE CEPAS (SALAD BOWL BLENDER)
     ---------------------------------------------------- */
  static blendStrains(strainId1, strainId2, ratio1 = 50) {
    const s1 = STRAINS_DATABASE.find(s => s.id === strainId1) || STRAINS_DATABASE[0];
    const s2 = STRAINS_DATABASE.find(s => s.id === strainId2) || STRAINS_DATABASE[1];

    const r1 = ratio1 / 100;
    const r2 = 1 - r1;

    const blendedThc = (s1.thc * r1 + s2.thc * r2).toFixed(1);
    const blendedCbd = (s1.cbd * r1 + s2.cbd * r2).toFixed(1);

    return {
      name: `Blend Custom (${s1.name} + ${s2.name})`,
      ratioText: `${ratio1}% ${s1.name} / ${100 - ratio1}% ${s2.name}`,
      thc: blendedThc,
      cbd: blendedCbd,
      combinedEffects: Array.from(new Set([...s1.effects, ...s2.effects])),
      combinedFlavors: Array.from(new Set([...s1.flavors, ...s2.flavors])),
      dominantTerpenes: [s1.dominantTerpene, s2.dominantTerpene]
    };
  }

  /* ----------------------------------------------------
     3. TABLA DE TEMPERATURAS DE VAPORIZACIÓN
     ---------------------------------------------------- */
  static getVapeTemps() {
    return [
      { terpene: "Cariofileno", tempC: 130, tempF: 266, effect: "Alivio físico & Anti-ansiedad", color: "#EF4444" },
      { terpene: "Humuleno",    tempC: 106, tempF: 223, effect: "Supresor apetito & Calmante",  color: "#A78BFA" },
      { terpene: "Pineno",      tempC: 155, tempF: 311, effect: "Claridad mental & Enfoque láser", color: "#06B6D4" },
      { terpene: "Mirceno",     tempC: 167, tempF: 333, effect: "Relajación muscular & Calma profunda", color: "#10B981" },
      { terpene: "Limoneno",    tempC: 176, tempF: 349, effect: "Euforia & Elevación del ánimo", color: "#F59E0B" },
      { terpene: "Terpinoleno", tempC: 186, tempF: 367, effect: "Creatividad & Estimulación cognitiva", color: "#EC4899" },
      { terpene: "Linalool",    tempC: 198, tempF: 388, effect: "Sueño reparador & Paz emocional", color: "#8B5CF6" },
      { terpene: "Ocimeno",     tempC: 66,  tempF: 151, effect: "Antiviral & Energía suave tropical", color: "#34D399" }
    ];
  }

  /* ----------------------------------------------------
     4b. ESTADÍSTICAS DEL CATÁLOGO
     ---------------------------------------------------- */
  static getCatalogStats(strains) {
    if (!strains || strains.length === 0) return null;
    const parseYield = y => typeof y === 'number' ? y : (parseInt(y) || 0);
    const banks = [...new Set(strains.map(s => s.bank))].length;
    const indicas = strains.filter(s => s.species === 'Indica').length;
    const sativas = strains.filter(s => s.species === 'Sativa').length;
    const hibridas = strains.filter(s => s.species === 'Híbrida' || s.species === 'Hibrida').length;
    const avgThc = (strains.reduce((sum, s) => sum + (typeof s.thc === 'number' ? s.thc : parseFloat(s.thc) || 0), 0) / strains.length).toFixed(1);
    const maxYieldIndoor = Math.max(...strains.map(s => parseYield(s.yieldIndoor)));
    const maxYieldOutdoor = Math.max(...strains.map(s => parseYield(s.yieldOutdoor)));
    const topRated = strains.slice().sort((a,b) => b.rating - a.rating)[0];
    return { total: strains.length, banks, indicas, sativas, hibridas, avgThc, maxYieldIndoor, maxYieldOutdoor, topRated };
  }

  /* ----------------------------------------------------
     4. GESTOR DE TEMAS DE COLOR (THEME ENGINE)
     ---------------------------------------------------- */
  static setTheme(themeName) {
    const root = document.documentElement;

    const themes = {
      emerald: {
        '--primary-emerald': '#10B981',
        '--primary-emerald-hover': '#059669',
        '--accent-purple': '#8B5CF6'
      },
      cyberpurple: {
        '--primary-emerald': '#8B5CF6',
        '--primary-emerald-hover': '#7C3AED',
        '--accent-purple': '#EC4899'
      },
      sunsetgold: {
        '--primary-emerald': '#F59E0B',
        '--primary-emerald-hover': '#D97706',
        '--accent-purple': '#EF4444'
      },
      obsidian: {
        '--primary-emerald': '#06B6D4',
        '--primary-emerald-hover': '#0891B2',
        '--accent-purple': '#10B981'
      }
    };

    const targetTheme = themes[themeName] || themes.emerald;
    Object.entries(targetTheme).forEach(([varName, val]) => {
      root.style.setProperty(varName, val);
    });

    localStorage.setItem('cannacatalog_theme', themeName);
  }
}



// --- ai-sommelier.js ---
// CannaCatalog 2.0 - Agente IA Sommelier Humano (Con Motor de Razonamiento Lógico Neuro-Terpénico)

class AISommelierAgent {
  constructor(appController) {
    this.app = appController;
    this.history = [];
    this.apiKey = localStorage.getItem('gemini_api_key') || null;
    this.initUI();
  }

  initUI() {
    this.triggerBtn = document.getElementById('ai-chat-trigger');
    this.chatWindow = document.getElementById('ai-chat-window');
    this.closeBtn = document.getElementById('ai-chat-close');
    this.messagesContainers = [
      document.getElementById('ai-chat-messages'),
      document.getElementById('ai-chat-messages-inline')
    ].filter(Boolean);

    this.inputFloating = document.getElementById('ai-chat-input');
    this.inputInline = document.getElementById('ai-chat-input-inline');
    this.sendBtnFloating = document.getElementById('ai-chat-send');
    this.sendBtnInline = document.getElementById('ai-chat-send-inline');
    this.quickPills = document.querySelectorAll('.ai-suggest-pill');

    // Toggle Floating Chat
    this.triggerBtn?.addEventListener('click', () => {
      const isVisible = this.chatWindow.style.display === 'flex';
      this.chatWindow.style.display = isVisible ? 'none' : 'flex';
      if (!isVisible && this.inputFloating) {
        this.inputFloating.focus();
      }
    });

    this.closeBtn?.addEventListener('click', () => {
      if (this.chatWindow) this.chatWindow.style.display = 'none';
    });

    // Send Message Events
    const handleSendFloating = () => {
      const text = this.inputFloating?.value?.trim();
      if (!text) return;
      this.inputFloating.value = '';
      this.userSay(text);
      this.processQuery(text);
    };

    const handleSendInline = () => {
      const text = this.inputInline?.value?.trim();
      if (!text) return;
      this.inputInline.value = '';
      this.userSay(text);
      this.processQuery(text);
    };

    this.sendBtnFloating?.addEventListener('click', handleSendFloating);
    this.inputFloating?.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') handleSendFloating();
    });

    this.sendBtnInline?.addEventListener('click', handleSendInline);
    this.inputInline?.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') handleSendInline();
    });

    // Quick Suggest Pills
    this.quickPills.forEach(pill => {
      pill.addEventListener('click', () => {
        const text = pill.getAttribute('data-prompt') || pill.textContent.trim();
        this.userSay(text);
        this.processQuery(text);
      });
    });

    // Saludo inicial con razomamiento activo
    const greeting = '¡Hola! Soy <strong>Mateo</strong>, tu master sumiller en CannaCatalog. 🌿 Cuento con un <strong>motor de razonamiento neuro-terpénico</strong> para analizar tus gustos o tu actividad objetivo y argumentar de forma lógica la recomendación perfecta.<br/><br/>👅 <em>¿Qué actividad vas a realizar o qué perfil de aromas te atraen más? (🍋 Cítricos, 🍓 Frutales Dulces, 🌲 Pino Haze, ⛽ Diésel, 🍪 Galleta/Vainilla o 🧀 Queso)</em>';
    this.botSay(greeting);
  }

  userSay(text) {
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const msgEl = document.createElement('div');
      msgEl.className = 'ai-msg user-msg';
      msgEl.textContent = text;
      container.appendChild(msgEl);
    });
    this.scrollToBottom();
  }

  botSay(htmlContent) {
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const msgEl = document.createElement('div');
      msgEl.className = 'ai-msg bot-msg';
      msgEl.innerHTML = htmlContent;
      container.appendChild(msgEl);

      // Re-bind strain link clicks
      msgEl.querySelectorAll('.ai-strain-link').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const strainId = link.getAttribute('data-strain-id');
          if (strainId) {
            document.dispatchEvent(new CustomEvent('openStrainDetail', { detail: strainId }));
          }
        });
      });
    });
    this.scrollToBottom();
  }

  showTyping() {
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const typing = document.createElement('div');
      typing.className = 'ai-msg bot-msg typing-msg ai-typing-indicator-node';
      typing.innerHTML = '<span>🧠 Mateo procesando razonamiento terpénico & maridaje...</span>';
      container.appendChild(typing);
    });
    this.scrollToBottom();
  }

  hideTyping() {
    document.querySelectorAll('.ai-typing-indicator-node').forEach(n => n.remove());
  }

  scrollToBottom() {
    this.messagesContainers.forEach(container => {
      if (container) container.scrollTop = container.scrollHeight;
    });
  }

  // Generador visual del Bloque de Razonamiento
  buildReasoningBox(step1Need, step2Terpenes, step3Selection) {
    return `
      <div class="sommelier-reasoning-box">
        <div class="reasoning-header">
          <span class="reasoning-brain-icon">🧠</span>
          <span class="reasoning-title">RAZONAMIENTO DEL SOMMELIER</span>
          <span class="reasoning-badge">Análisis Neuro-Terpénico</span>
        </div>
        <div class="reasoning-steps">
          <div class="reasoning-step">
            <span class="step-num">1</span>
            <div><strong>Diagnóstico de Necesidad:</strong> ${step1Need}</div>
          </div>
          <div class="reasoning-step">
            <span class="step-num">2</span>
            <div><strong>Análisis Terpénico & Séquito:</strong> ${step2Terpenes}</div>
          </div>
          <div class="reasoning-step">
            <span class="step-num">3</span>
            <div><strong>Cribado del Catálogo:</strong> ${step3Selection}</div>
          </div>
        </div>
      </div>
    `;
  }

  // Algoritmo del Activity Matcher para puntuar cepas según la actividad objetivo
  getActivityMatch(activityId) {
    const activity = ACTIVITIES_DATA.find(a => a.id === activityId);
    if (!activity) return null;

    const scoredStrains = STRAINS_DATABASE.map(strain => {
      let score = 0;
      if (activity.preferredTerpenes.includes(strain.dominantTerpene)) score += 40;
      if (activity.recommendedSpecies.includes(strain.species)) score += 30;
      if (strain.activities && strain.activities.includes(activityId)) score += 50;
      score += (strain.rating * 5);

      return { strain, score };
    });

    scoredStrains.sort((a, b) => b.score - a.score);
    return {
      activity,
      topStrains: scoredStrains.slice(0, 3).map(s => s.strain)
    };
  }

  async processQuery(userQuery) {
    this.showTyping();

    if (this.apiKey) {
      try {
        const cloudResponse = await this.callGeminiAPI(userQuery);
        this.hideTyping();
        this.botSay(cloudResponse);
        return;
      } catch (err) {
        console.warn('Error en Gemini API, usando motor Sommelier local:', err);
      }
    }

    setTimeout(() => {
      this.hideTyping();
      const response = this.generateHumanResponse(userQuery.toLowerCase());
      this.botSay(response);
    }, 450);
  }

  async callGeminiAPI(userQuery) {
    const catalogContext = STRAINS_DATABASE.map(s => 
      `- ${s.name} (Especie: ${s.species}, Banco: ${s.bank}): THC ${s.thc}%, CBD ${s.cbd}%, Terpeno: ${s.dominantTerpene}, Sabores: ${s.flavors.join('/')}, Efectos: ${s.effects.join('/')}, ID: ${s.id}`
    ).join('\n');

    const systemPrompt = `Eres Mateo, un master sumiller de cannabis en CannaCatalog dotado de razonamiento estructurado.
SIEMPRE debes empezar tu respuesta incluyendo el bloque HTML de razonamiento exacto:
<div class="sommelier-reasoning-box">
  <div class="reasoning-header">
    <span class="reasoning-brain-icon">🧠</span>
    <span class="reasoning-title">RAZONAMIENTO DEL SOMMELIER</span>
    <span class="reasoning-badge">Análisis Neuro-Terpénico</span>
  </div>
  <div class="reasoning-steps">
    <div class="reasoning-step">
      <span class="step-num">1</span>
      <div><strong>Diagnóstico de Necesidad:</strong> [Describe brevemente qué busca el usuario]</div>
    </div>
    <div class="reasoning-step">
      <span class="step-num">2</span>
      <div><strong>Análisis Terpénico & Séquito:</strong> [Explica qué terpenos y cannabinoides favorecen este estado]</div>
    </div>
    <div class="reasoning-step">
      <span class="step-num">3</span>
      <div><strong>Cribado del Catálogo:</strong> [Explica cómo se filtraron las mejores cepas]</div>
    </div>
  </div>
</div>

A continuación del bloque de razonamiento, ofrece tu recomendación final fundamentada.
Cuando menciones una cepa, usa exactamente el formato de enlace: <a href="#" class="ai-strain-link" data-strain-id="ID_DE_LA_CEPA">Nombre Cepa</a>.

Catálogo de cepas disponible:
${catalogContext}`;

    const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${this.apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [
          { role: 'user', parts: [{ text: `${systemPrompt}\n\nConsulta del cliente: ${userQuery}` }] }
        ]
      })
    });

    const data = await res.json();
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
    if (text) {
      return text.replace(/\n/g, '<br/>');
    }
    throw new Error('Respuesta vacía de la API');
  }

  generateHumanResponse(rawQuery) {
    const query = rawQuery.toLowerCase();

    // 1. EVALUACIÓN DE SABORES
    // A) CÍTRICOS / LIMÓN / MANDARINA / NARANJA
    if (query.includes('citric') || query.includes('cítric') || query.includes('limon') || query.includes('limón') || query.includes('mandarina') || query.includes('naranja')) {
      const matches = STRAINS_DATABASE.filter(s => 
        s.flavors.some(f => f.toLowerCase().includes('limón') || f.toLowerCase().includes('cítrico') || f.toLowerCase().includes('mandarina') || f.toLowerCase().includes('naranja') || f.toLowerCase().includes('citrus')) ||
        s.dominantTerpene === 'limonene'
      ).sort((a, b) => b.rating - a.rating).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'El usuario busca una experiencia estimulante con frescor cítrico en paladar.',
        'Priorizo cepas con dominancia en <strong>Limoneno</strong>, responsable de la elevación del ánimo y la estimulación de dopamina.',
        'Filtradas 267 cepas del catálogo seleccionando las 3 mejor puntuadas con notas a limón exprimido y mandarina.'
      );

      return `
        ${reasoning}
        🍋 <strong>Recomendación Fundamentada — Perfil Cítrico & Refrescante:</strong>
        <br/><br/>
        En base al análisis terpénico, estas cepas combinan notas cítricas con un efecto alegre y despejado:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(245,158,11,0.25); color:#FCD34D; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | 🌿 Terpeno: ${TERPENES_INFO[s.dominantTerpene]?.name || s.dominantTerpene}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Para qué actividad te gustaría maridar esta selección cítrica? (Gaming, Creatividad, Paseo o Deporte)</em>
      `;
    }

    // B) FRUTAL / DULCE / ARÁNDANOS / CARAMELO / FRESA / BAYAS
    if (query.includes('frutal') || query.includes('fruta') || query.includes('frutas') || query.includes('dulce') || query.includes('arándano') || query.includes('bayas') || query.includes('caramelo') || query.includes('fresa') || query.includes('uva') || query.includes('tropica')) {
      const matches = STRAINS_DATABASE.filter(s => 
        s.flavors.some(f => f.toLowerCase().includes('dulce') || f.toLowerCase().includes('fruta') || f.toLowerCase().includes('arándano') || f.toLowerCase().includes('caramelo') || f.toLowerCase().includes('bayas') || f.toLowerCase().includes('tropical')) ||
        s.dominantTerpene === 'ocimene' || s.dominantTerpene === 'terpinolene'
      ).sort((a, b) => b.rating - a.rating).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Búsqueda de perfil organoléptico frutal, dulce y goloso.',
        'Análisis de sinergia entre <strong>Mirceno, Terpinoleno y Ocimeno</strong>, potenciadores de aromas a bayas silvestres y frutas de hueso.',
        'Seleccionadas 3 variedades top ventas con perfiles afrutados de alta densidad resinosa.'
      );

      return `
        ${reasoning}
        🍓 <strong>Recomendación Fundamentada — Perfil Frutal Dulce & Goloso:</strong>
        <br/><br/>
        Genéticas maridadas por su alta concentración de esteres aromáticos y terpenos dulces:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(236,72,153,0.25); color:#F472B6; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | ✨ ${s.effects.slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Prefieres una genética más relajante (Índica) o eufórica (Sativa) con este sabor?</em>
      `;
    }

    // C) PINO / BOSQUE / MADERA / INCIENSO HAZE / CEDRO
    if (query.includes('pino') || query.includes('bosque') || query.includes('madera') || query.includes('incienso') || query.includes('haze') || query.includes('cedro')) {
      const matches = STRAINS_DATABASE.filter(s => 
        s.flavors.some(f => f.toLowerCase().includes('pino') || f.toLowerCase().includes('madera') || f.toLowerCase().includes('incienso') || f.toLowerCase().includes('haze') || f.toLowerCase().includes('cedro')) ||
        s.dominantTerpene === 'pinene'
      ).sort((a, b) => b.rating - a.rating).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Preferencia por matices amaderados, inciensados y resinosos de estilo Haze silvestre.',
        'Enfoque en <strong>Alfa y Beta Pineno</strong>, terpenos neuroprotectores que favorecen la retención de memoria y la claridad focal.',
        'Cribadas cepas legendarias Haze y forestales con retrogusto a madera de cedro e incienso.'
      );

      return `
        ${reasoning}
        🌲 <strong>Recomendación Fundamentada — Perfil Pino, Bosque & Haze:</strong>
        <br/><br/>
        Variedades seleccionadas por su aroma a sotobosque y su potente claridad cognitiva:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(6,182,212,0.25); color:#67E8F9; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | 🧠 Claridad Láser</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Te gustaría maridar esta cepa con naturaleza, senderismo o creación artística?</em>
      `;
    }

    // D) DIÉSEL / GASOLINA / COMBUSTIBLE / GAS
    if (query.includes('diesel') || query.includes('diésel') || query.includes('gasolina') || query.includes('combustible') || query.includes('gas')) {
      const matches = STRAINS_DATABASE.filter(s => 
        s.flavors.some(f => f.toLowerCase().includes('diésel') || f.toLowerCase().includes('diesel') || f.toLowerCase().includes('gasolina') || f.toLowerCase().includes('combustible'))
      ).sort((a, b) => b.thc - a.thc).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'El cliente busca un aroma penetrante a combustible con pegada de alta intensidad.',
        'Selección de cepas ricas en <strong>Cariofileno y Limoneno</strong> con alto THC (>20%), responsables del buqué a queroseno.',
        'Filtradas las cepas más potentes de la familia Sour Diesel y OG Kush del catálogo.'
      );

      return `
        ${reasoning}
        ⛽ <strong>Recomendación Fundamentada — Perfil Diésel & Gasolina:</strong>
        <br/><br/>
        Selección de máxima intensidad terpénica con bouquet a queroseno y pegada eufórica:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(16,185,129,0.25); color:#6EE7B7; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | ⚡ ${s.effects.slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // E) GALLETA / COOKIES / VAINILLA / REPOSTERÍA / HELADO / CREMA
    if (query.includes('galleta') || query.includes('cookie') || query.includes('cookies') || query.includes('vainilla') || query.includes('reposteria') || query.includes('repostería') || query.includes('helado') || query.includes('crema')) {
      const matches = STRAINS_DATABASE.filter(s => 
        s.flavors.some(f => f.toLowerCase().includes('galleta') || f.toLowerCase().includes('cookie') || f.toLowerCase().includes('vainilla') || f.toLowerCase().includes('helado') || f.toLowerCase().includes('crema') || f.toLowerCase().includes('masa'))
      ).sort((a, b) => b.rating - a.rating).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Preferencia por matices de repostería artesanal, vainilla y notas de crema pastelera.',
        'Identificado perfil de <strong>Linalool y Beta-Cariofileno</strong> que aportan textura de humo denso y retrogusto a mantequilla dulce.',
        'Seleccionadas cepas de la familia Cookies, Cake y Gelato con mejores puntuaciones organolépticas.'
      );

      return `
        ${reasoning}
        🍪 <strong>Recomendación Fundamentada — Perfil Galleta & Repostería:</strong>
        <br/><br/>
        Genéticas seleccionadas por su densidad de humo cremoso y matices a postre horneado:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(139,92,246,0.25); color:#C084FC; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | 😌 ${s.effects.slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // F) QUESO / CHEESE / SKUNK
    if (query.includes('queso') || query.includes('cheese') || query.includes('skunk')) {
      const matches = STRAINS_DATABASE.filter(s => 
        s.flavors.some(f => f.toLowerCase().includes('queso') || f.toLowerCase().includes('cheese') || f.toLowerCase().includes('skunk'))
      ).sort((a, b) => b.rating - a.rating).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Búsqueda de aromas Old School profundos a lácteo maduro y fondo Skunk.',
        'Análisis de compuesos de azufre orgánico y <strong>Mirceno potente</strong> característicos de las genéticas UK Cheese.',
        'Filtradas las variedades con buqué más añejo y bouquet terroso de Skunk tradicional.'
      );

      return `
        ${reasoning}
        🧀 <strong>Recomendación Fundamentada — Perfil Queso Curado & Skunk:</strong>
        <br/><br/>
        Variedades con buqué añejo y personalidad única para paladares exigentes:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(234,179,8,0.25); color:#FDE047; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | 🥳 ${s.effects.slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // 2. MAPEO DIRECTO CON ACTIVIDADES DEL ACTIVITY MATCHER
    let matchedActivityId = null;
    if (query.includes('caminar') || query.includes('pasear') || query.includes('caminata') || query.includes('paseo') || query.includes('senderismo') || query.includes('andar') || query.includes('naturaleza') || query.includes('bosque')) {
      matchedActivityId = 'nature_walk';
    } else if (query.includes('juego') || query.includes('gaming') || query.includes('consola') || query.includes('play') || query.includes('xbox') || query.includes('gamer')) {
      matchedActivityId = 'gaming';
    } else if (query.includes('crear') || query.includes('pintar') || query.includes('música') || query.includes('musica') || query.includes('arte') || query.includes('creatividad') || query.includes('escribir')) {
      matchedActivityId = 'creativity';
    } else if (query.includes('social') || query.includes('amigos') || query.includes('fiesta') || query.includes('charlar') || query.includes('risas') || query.includes('reunión')) {
      matchedActivityId = 'social';
    } else if (query.includes('dormir') || query.includes('relax') || query.includes('cine') || query.includes('película') || query.includes('peli') || query.includes('sofá') || query.includes('sofa') || query.includes('descansar') || query.includes('insomnio')) {
      matchedActivityId = 'relax_sleep';
    } else if (query.includes('meditar') || query.includes('meditacion') || query.includes('yoga') || query.includes('introspección') || query.includes('paz mental')) {
      matchedActivityId = 'meditation';
    } else if (query.includes('gimnasio') || query.includes('deporte') || query.includes('entrenar') || query.includes('ejercicio') || query.includes('gym') || query.includes('fitness') || query.includes('workout')) {
      matchedActivityId = 'workout';
    }

    if (matchedActivityId) {
      const matchResult = this.getActivityMatch(matchedActivityId);
      if (matchResult) {
        const { activity, topStrains } = matchResult;
        const terpeneNames = activity.preferredTerpenes.map(t => TERPENES_INFO[t]?.name || t).join(', ');

        const reasoning = this.buildReasoningBox(
          `Optimización para la actividad objetivo: <strong>${activity.title}</strong>.`,
          `Mapeo de terpenos sinérgicos (<strong>${terpeneNames}</strong>) y equilibrio cannabinode para evitar ansiedad o fatiga prematura.`,
          `Cruce de variables con el motor Activity Matcher puntuando especie (${activity.recommendedSpecies.join('/')}) y afinidad de actividad.`
        );

        return `
          ${reasoning}
          🎲 <strong>Recomendación Fundamentada para: ${activity.title}</strong>
          <br/><br/>
          <em>${activity.description}</em>
          <br/><br/>
          🏆 <strong>Top 3 cepas ganadoras según el razonamiento lógico:</strong>
          <br/><br/>
          ${topStrains.map((s, idx) => `
            ${idx === 0 ? '🥇' : idx === 1 ? '🥈' : '🥉'} <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(16,185,129,0.2); color:#6EE7B7; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
            &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 🌿 Terpeno: ${TERPENES_INFO[s.dominantTerpene]?.name || s.dominantTerpene} | 👅 Sabores: ${s.flavors.join(', ')}</small>
          `).join('<br/><br/>')}
          <br/><br/>
          💬 <em>¿Qué perfil de sabor prefieres para esta actividad? (🍋 Cítricos, 🍓 Frutal Dulce, 🌲 Pino Haze, ⛽ Diésel o 🍪 Galleta)</em>
        `;
      }
    }

    const hasIndica = query.includes('indica') || query.includes('índica') || query.includes('indicas') || query.includes('índicas');
    const hasSativa = query.includes('sativa') || query.includes('sativas') || query.includes('satva');
    const hasDifference = query.includes('diferencia') || query.includes('vs') || query.includes('comparar');

    // COMPARATIVA AMBAS
    if ((hasIndica && hasSativa) || hasDifference) {
      const topIndica = STRAINS_DATABASE.find(s => s.species.toLowerCase().includes('indica'));
      const topSativa = STRAINS_DATABASE.find(s => s.species.toLowerCase().includes('sativa'));

      const reasoning = this.buildReasoningBox(
        'El usuario solicita una comparativa entre el quimiotipo Índica y Sativa.',
        'Análisis de la interacción de terpenos miorrelajantes (Mirceno) frente a estimulantes cerebrales (Limoneno/Terpinoleno).',
        'Seleccionadas las dos cepas de referencia más galardonadas de cada quimiotipo.'
      );

      return `
        ${reasoning}
        ⚖️ <strong>Análisis Comparativo Fundamentado:</strong>
        <br/><br/>
        🟣 <strong>INDICA (Relajación Corporal):</strong><br/>
        Predominio de <strong>Mirceno</strong>. Sensación de descanso físico y desconexión.<br/>
        • <em>Recomendación estrella:</em> <a href="#" class="ai-strain-link" data-strain-id="${topIndica.id}"><strong>${topIndica.name}</strong></a> (${topIndica.bank}) — THC ${topIndica.thc}%.
        <br/><br/>
        🟡 <strong>SATIVA (Estimulación Cerebral):</strong><br/>
        Predominio de <strong>Limoneno y Terpinoleno</strong>. Impulso alegre y creativo.<br/>
        • <em>Recomendación estrella:</em> <a href="#" class="ai-strain-link" data-strain-id="${topSativa.id}"><strong>${topSativa.name}</strong></a> (${topSativa.bank}) — THC ${topSativa.thc}%.
        <br/><br/>
        💬 <em>¿Qué efecto se ajusta mejor a lo que buscas experimentar hoy?</em>
      `;
    }

    // PETICIÓN EXPLICITA DE INDICA
    if (hasIndica || query.includes('no quiero sativa') || query.includes('sin sativa')) {
      const indicaStrains = STRAINS_DATABASE.filter(s => s.species.toLowerCase().includes('indica'));
      const topIndicas = indicaStrains.sort((a, b) => b.thc - a.thc).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Búsqueda de quimiotipo Índica para relajación corporal o sedación nocturna.',
        'Selección basada en <strong>Mirceno y Linalool</strong> para maximizar el efecto de calma muscular y paz mental.',
        'Filtradas las cepas Índica pura con mayor concentración de resina y mejor valoración.'
      );

      return `
        ${reasoning}
        🟣 <strong>Recomendación Fundamentada — Genéticas INDICA:</strong>
        <br/><br/>
        Selección de cepas miorrelajantes ideales para descansar y desconectar:
        <br/><br/>
        ${topIndicas.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(139,92,246,0.25); color:#C084FC; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${s.flavors.join(', ')} | ⚡ ${s.effects.join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Prefieres tu Índica con sabor a Queso 🧀, Galletas/Vainilla 🍪 o Frutas Dulces 🍓?</em>
      `;
    }

    // PETICIÓN EXPLICITA DE SATIVA
    if (hasSativa || query.includes('no quiero indica') || query.includes('sin indica')) {
      const sativaStrains = STRAINS_DATABASE.filter(s => s.species.toLowerCase().includes('sativa'));
      const topSativas = sativaStrains.sort((a, b) => b.thc - a.thc).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Búsqueda de quimiotipo Sativa para estimulación cerebral y energía.',
        'Foco en <strong>Limoneno, Pineno y Terpinoleno</strong> para elevar la motivación sin provocar confusión mental.',
        'Cribadas las cepas Sativa dominantes con mayor THC y mejor respuesta eufórica.'
      );

      return `
        ${reasoning}
        🟡 <strong>Recomendación Fundamentada — Genéticas SATIVA:</strong>
        <br/><br/>
        Selección de cepas eufóricas y alegres diseñadas para estar activo:
        <br/><br/>
        ${topSativas.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(245,158,11,0.25); color:#FCD34D; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">⚡ THC: ${s.thc}% | 👅 Sabores: ${s.flavors.join(', ')} | ✨ ${s.effects.join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Te llama más la atención el sabor Cítrico 🍋, Pino/Haze 🌲 o Diésel ⛽?</em>
      `;
    }

    // POTENCIA ALTA
    if (query.includes('thc') || query.includes('potente') || query.includes('fuerte')) {
      const topThc = [...STRAINS_DATABASE].sort((a, b) => b.thc - a.thc).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'El usuario exige la máxima concentración de cannabinoides (THC elevado).',
        'Evaluación de sinergia entre THC >22% y terpenos fijadores (Cariofileno y Mirceno) que prolongan la duración de los receptores.',
        'Filtradas las 3 variedades con mayor porcentaje de THC de todo el catálogo.'
      );

      return `
        ${reasoning}
        🔥 <strong>Recomendación Fundamentada — Máxima Potencia THC:</strong>
        <br/><br/>
        ${topThc.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> (${s.species}) — <strong>${s.thc}% THC</strong> (<em>${s.bank}</em>)<br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">👅 Sabores: ${s.flavors.join(', ')} | ⚡ ${s.effects.join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Qué matiz aromático buscas en tu cepa potente?</em>
      `;
    }

    // BÚSQUEDA GENERAL POR PALABRA CLAVE
    const searchMatches = STRAINS_DATABASE.filter(s => 
      s.name.toLowerCase().includes(query) ||
      s.flavors.some(f => f.toLowerCase().includes(query)) ||
      s.effects.some(e => e.toLowerCase().includes(query)) ||
      s.dominantTerpene.toLowerCase().includes(query)
    ).slice(0, 3);

    if (searchMatches.length > 0) {
      const reasoning = this.buildReasoningBox(
        `Búsqueda personalizada para el término: <strong>"${rawQuery}"</strong>.`,
        'Filtrado terpénico y organoléptico por coincidencia semántica de aromas y efectos.',
        'Coincidencias óptimas encontradas en el catálogo de 267 cepas.'
      );

      return `
        ${reasoning}
        🔍 <strong>Recomendación Fundamentada para "${rawQuery}":</strong>
        <br/><br/>
        ${searchMatches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> (${s.species}) — <em>${s.bank}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 Sabores: ${s.flavors.join(', ')} | ⚡ ${s.effects.join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // FALLBACK INTERACTIVO CON PREGUNTA DE SABORES
    const randomPick = STRAINS_DATABASE[Math.floor(Math.random() * STRAINS_DATABASE.length)];
    const reasoning = this.buildReasoningBox(
      'Consulta general o abierta recibida.',
      'Analizando cepa aleatoria de alta puntuación para abrir el maridaje terpénico.',
      'Sugerencia directa para encauzar la búsqueda hacia tu perfil de sabor o actividad ideal.'
    );

    return `
      ${reasoning}
      🌟 <strong>Sugerencia del Sumiller:</strong><br/><br/>
      Prueba la cepa destacada de hoy: <a href="#" class="ai-strain-link" data-strain-id="${randomPick.id}"><strong>${randomPick.name}</strong></a> (${randomPick.species} de <em>${randomPick.bank}</em>)<br/>
      &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${randomPick.thc}% | 👅 Sabores: ${randomPick.flavors.join(', ')}</small>
      <br/><br/>
      💬 <strong>¿Qué tipo de sabores prefieres más?</strong><br/>
      Dime si buscas sabores 🍋 <em>Cítricos</em>, 🍓 <em>Frutales Dulces</em>, 🌲 <em>Pino Haze</em>, ⛽ <em>Diésel</em>, 🍪 <em>Galleta/Vainilla</em> o 🧀 <em>Queso</em> y te haré la recomendación exacta con mi análisis de razonamiento.
    `;
  }
}





// --- app.js ---
// CannaCatalog 2.0 MAX - Controlador Principal (Blindado y Defensivo)


class CannaAppMAX {
  constructor() {
    this.selectedActivity = 'nature_walk';
    this.currentStrains = Array.isArray(STRAINS_DATABASE) ? [...STRAINS_DATABASE] : [];

    try {
      const savedCompared = JSON.parse(localStorage.getItem('cannacatalog_compared') || '[]');
      this.comparedStrains = Array.isArray(savedCompared) ? savedCompared.slice(0, 3) : [];
    } catch (e) {
      this.comparedStrains = [];
    }

    const safeRun = (fn, name) => {
      try {
        if (typeof fn === 'function') fn.call(this);
      } catch (err) {
        console.warn(`[CannaApp] error in ${name}:`, err);
      }
    };

    safeRun(this.initDOM, 'initDOM');
    safeRun(this.initAgeGate, 'initAgeGate');

    try { this.matcher = new ActivityMatcher('matcher-container', 'matcher-result-area'); } catch (e) { console.warn(e); }
    try { this.bitacora = new BitacoraManager(); } catch (e) { console.warn(e); }
    try { this.audioEngine = new AmbientAudioEngine(); window.audioEngine = this.audioEngine; } catch (e) { console.warn(e); }
    try { this.aiAgent = new AISommelierAgent(this); } catch (e) { console.warn(e); }

    safeRun(this.initNavigation, 'initNavigation');
    safeRun(this.initCatalog, 'initCatalog');
    safeRun(this.initStatsBar, 'initStatsBar');
    safeRun(this.initMatcherEvents, 'initMatcherEvents');
    safeRun(this.initBitacoraEvents, 'initBitacoraEvents');
    safeRun(this.initBlenderAndCompare, 'initBlenderAndCompare');
    safeRun(this.initTerpeneSection, 'initTerpeneSection');
    safeRun(this.initSobrioMode, 'initSobrioMode');
    safeRun(this.initThemeEngine, 'initThemeEngine');
    safeRun(this.initAuth, 'initAuth');
    safeRun(this.initCustomEventListeners, 'initCustomEventListeners');
    safeRun(this.initImageLightboxEngine, 'initImageLightboxEngine');
    safeRun(this.updateStashCounter, 'updateStashCounter');
    safeRun(this.initCaraACaraComparator, 'initCaraACaraComparator');
  }

  initDOM() {
    this.ageModal = document.getElementById('age-modal');
    this.strainsGrid = document.getElementById('strains-grid');
    this.searchInput = document.getElementById('search-input');
    this.filterBank = document.getElementById('filter-bank');
    this.filterSpecies = document.getElementById('filter-species');
    this.filterTerpene = document.getElementById('filter-terpene');
    this.sortBy = document.getElementById('sort-by');
    this.catalogCount = document.getElementById('catalog-count');
    this.strainDetailModal = document.getElementById('strain-detail-modal');
    this.strainDetailContent = document.getElementById('strain-detail-content');
    this.addLogModal = document.getElementById('add-log-modal');
    this.addLogForm = document.getElementById('add-log-form');
    this.missionModal = document.getElementById('mission-modal');
    this.missionModalContent = document.getElementById('mission-modal-content');
    this.stashCounter = document.getElementById('stash-counter');
    this.sobrioModal = document.getElementById('sobrio-modal');
    this.imageLightboxModal = document.getElementById('image-lightbox-modal');
    this.lightboxImg = document.getElementById('lightbox-img');
    this.lightboxTitle = document.getElementById('lightbox-title');
    this.lightboxSubtitle = document.getElementById('lightbox-subtitle');
    this.compareDock = document.getElementById('compare-floating-dock');
    this.compareDockSlots = document.getElementById('compare-dock-slots');
    this.compareDockCounter = document.getElementById('compare-dock-counter');
    this.compareModal = document.getElementById('compare-modal');
    this.compareModalContent = document.getElementById('compare-modal-content');
    this.btnOpenCompareModal = document.getElementById('btn-open-compare-modal');
    this.btnClearCompare = document.getElementById('btn-clear-compare');
  }

  /* 1. VERIFICACIÓN DE EDAD DEFENSIVA (+18) */
  initAgeGate() {
    const ageModal    = document.getElementById('age-modal');
    const stepVerify  = document.getElementById('age-step-verify');
    const stepDenied  = document.getElementById('age-step-denied');
    const btnConfirm  = document.getElementById('btn-age-confirm');
    const btnReject   = document.getElementById('btn-age-reject');
    const btnRetry    = document.getElementById('btn-age-retry');
    const btnStatus   = document.getElementById('btn-age-status');
    const statusText  = document.getElementById('age-status-text');
    const lockStyle   = document.getElementById('age-lock-style');
    const mainApp     = document.getElementById('main-app');
    const mainHeader  = document.querySelector('.main-header');

    /* ── Helpers de estado ─────────────────────────────────── */
    const setPill = (verified) => {
      if (!statusText || !btnStatus) return;
      if (verified) {
        statusText.textContent = '+18 Verificado';
        btnStatus.style.borderColor = 'rgba(16,185,129,0.4)';
        btnStatus.style.color = 'var(--primary-emerald)';
      } else {
        statusText.textContent = '🔞 Sin Verificar';
        btnStatus.style.borderColor = 'rgba(239,68,68,0.5)';
        btnStatus.style.color = '#FCA5A5';
      }
    };

    /* ── Desbloquear contenido ─────────────────────────────── */
    const unlockContent = () => {
      // Eliminar la barrera CSS que oculta header + main
      if (lockStyle) lockStyle.remove();
      // Revelar explícitamente los elementos
      if (mainApp)    mainApp.style.display    = '';
      if (mainHeader) mainHeader.style.display = '';
      document.body.classList.remove('age-locked');
      if (ageModal && ageModal.open) ageModal.close();
      setPill(true);
    };

    /* ── Bloquear contenido (Mantener visible el catálogo) ─── */
    const lockContent = () => {
      document.body.classList.add('age-locked');
      if (stepVerify) stepVerify.style.display = 'block';
      if (stepDenied) stepDenied.style.display = 'none';
      if (ageModal && typeof ageModal.showModal === 'function') {
        try {
          if (!ageModal.open) ageModal.showModal();
        } catch (_) {}
      }
      setPill(false);
    };

    /* ── Verificar estado (Por defecto auto-verificado para acceso directo) ─── */
    let isVerified = true;
    try {
      localStorage.setItem('cannacatalog_age_verified', 'true');
      localStorage.setItem('canna_age_verified', 'true');
    } catch (_) {}

    unlockContent();

    /* ── Confirmar edad (+18) ──────────────────────────────── */
    btnConfirm?.addEventListener('click', () => {
      try {
        localStorage.setItem('cannacatalog_age_verified', 'true');
        localStorage.setItem('canna_age_verified', 'true');
      } catch (_) {}
      unlockContent();
      this.showToast('✅ Acceso concedido (+18). ¡Bienvenido a CannaCatalog 2.0 MAX!');
    });

    /* ── Rechazar (<18) → redirigir a Google ───────────────── */
    btnReject?.addEventListener('click', () => {
      if (stepVerify) stepVerify.style.display = 'none';
      if (stepDenied) stepDenied.style.display = 'block';
      // Redirigir a Google tras la pantalla de denegación
      this._denyTimer = setTimeout(() => {
        window.location.href = 'https://www.google.com';
      }, 1500);
    });

    /* ── Volver a intentar verificación ───────────────────── */
    btnRetry?.addEventListener('click', () => {
      clearTimeout(this._denyTimer);
      if (stepDenied) stepDenied.style.display = 'none';
      if (stepVerify) stepVerify.style.display = 'block';
    });

    /* ── Botón de estado en cabecera ───────────────────────── */
    btnStatus?.addEventListener('click', () => {
      const v = localStorage.getItem('cannacatalog_age_verified') === 'true' ||
                localStorage.getItem('canna_age_verified') === 'true';
      if (v) {
        if (confirm('🛡️ Estado: Verificado (+18).\n¿Deseas reiniciar tu verificación de edad?')) {
          try {
            localStorage.removeItem('cannacatalog_age_verified');
            localStorage.removeItem('canna_age_verified');
          } catch (_) {}
          lockContent();
        }
      } else {
        lockContent();
      }
    });
  }


  /* 2. NAVEGACIÓN SPA */
  initNavigation() {
    const navButtons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.app-section');

    navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-target');
        if (!targetId) return;

        navButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        sections.forEach(sec => {
          if (sec.id === targetId) {
            sec.classList.add('active-section');
          } else {
            sec.classList.remove('active-section');
          }
        });

        if (targetId === 'section-bitacora') {
          this.bitacora.renderLogList(document.getElementById('bitacora-list'));
        }
      });
    });

    document.getElementById('open-stash-btn')?.addEventListener('click', () => {
      this.filterByStash();
    });
  }

  /* 2b. STATS BAR DEL CATÁLOGO */
  initStatsBar() {
    const stats = AdvancedTools.getCatalogStats(STRAINS_DATABASE);
    if (!stats) return;

    const animateNumber = (el, target) => {
      let start = 0;
      const duration = 1200;
      const step = (timestamp) => {
        if (!start) start = timestamp;
        const progress = Math.min((timestamp - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target);
        if (progress < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    const set = (id, val) => {
      const el = document.getElementById(id);
      if (!el) return;
      if (typeof val === 'number') animateNumber(el, val);
      else el.textContent = val;
    };

    set('stat-total',   stats.total);
    set('stat-banks',   stats.banks);
    set('stat-indicas', stats.indicas);
    set('stat-sativas', stats.sativas);
    set('stat-hibridas', stats.hibridas);
    set('stat-avg-thc', parseFloat(stats.avgThc));
    if (stats.topRated) {
      const topEl = document.getElementById('stat-top-rated');
      if (topEl) topEl.textContent = stats.topRated.name;
    }
  }

  /* SISTEMA DE AUTENTICACIÓN Y CONTROL DE USUARIOS VIP */
  initAuth() {
    this.authModal = document.getElementById('auth-modal');
    this.btnUserAuth = document.getElementById('btn-user-auth');
    this.authBtnText = document.getElementById('auth-btn-text');
    
    this.authFormsWrapper = document.getElementById('auth-forms-wrapper');
    this.authProfileWrapper = document.getElementById('auth-profile-wrapper');
    
    this.tabLoginBtn = document.getElementById('tab-login-btn');
    this.tabRegisterBtn = document.getElementById('tab-register-btn');
    this.authLoginForm = document.getElementById('auth-login-form');
    this.authRegisterForm = document.getElementById('auth-register-form');
    this.btnLogout = document.getElementById('btn-logout');

    this.updateUserSessionUI();

    // Backdrop click listener to close auth modal
    this.authModal?.addEventListener('click', (e) => {
      const rect = this.authModal.getBoundingClientRect();
      const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
      if (!isInDialog) {
        this.authModal.close();
      }
    });

    // Abrir Modal de Sesión / Registro
    this.btnUserAuth?.addEventListener('click', () => {
      const session = this.getUserSession();
      if (session) {
        // Mostrar perfil
        if (this.authFormsWrapper) this.authFormsWrapper.style.display = 'none';
        if (this.authProfileWrapper) this.authProfileWrapper.style.display = 'block';
        
        const profileName = document.getElementById('profile-user-name');
        const profileEmail = document.getElementById('profile-user-email');
        const profileStatsLogs = document.getElementById('profile-stats-logs');
        
        if (profileName) profileName.textContent = session.name || 'Usuario VIP';
        if (profileEmail) profileEmail.textContent = session.email || 'usuario@cannacatalog.com';
        if (profileStatsLogs) profileStatsLogs.textContent = this.bitacora?.logs?.length || 0;
      } else {
        // Mostrar login/registro
        if (this.authFormsWrapper) this.authFormsWrapper.style.display = 'block';
        if (this.authProfileWrapper) this.authProfileWrapper.style.display = 'none';
        this.switchAuthTab('login');
      }
      this.authModal?.showModal();
    });

    // Eventos de Pestañas (Login / Registro)
    this.tabLoginBtn?.addEventListener('click', () => this.switchAuthTab('login'));
    this.tabRegisterBtn?.addEventListener('click', () => this.switchAuthTab('register'));

    // Submit Form Login
    this.authLoginForm?.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('login-email')?.value?.trim();
      const password = document.getElementById('login-password')?.value;

      if (!email || !password) return;

      const userName = email.split('@')[0];
      const sessionData = {
        name: userName.charAt(0).toUpperCase() + userName.slice(1),
        email: email.includes('@') ? email : `${email}@cannacatalog.com`,
        joinedDate: new Date().toLocaleDateString()
      };

      localStorage.setItem('cannacatalog_user_session', JSON.stringify(sessionData));
      this.updateUserSessionUI();
      this.authModal?.close();
      this.showToast(`✨ ¡Bienvenido de nuevo, ${sessionData.name}!`);
    });

    // Submit Form Registro
    this.authRegisterForm?.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('reg-name')?.value?.trim();
      const email = document.getElementById('reg-email')?.value?.trim();
      const pass = document.getElementById('reg-password')?.value;
      const confirmPass = document.getElementById('reg-confirm-password')?.value;

      if (pass !== confirmPass) {
        alert('⚠️ Las contraseñas no coinciden. Por favor verifícalas.');
        return;
      }

      const sessionData = {
        name: name || 'Usuario VIP',
        email: email,
        joinedDate: new Date().toLocaleDateString()
      };

      localStorage.setItem('cannacatalog_user_session', JSON.stringify(sessionData));
      this.updateUserSessionUI();
      this.authModal?.close();
      this.showToast(`🚀 ¡Registro completado con éxito! Bienvenido ${sessionData.name}.`);
    });

    // Cerrar Sesión
    this.btnLogout?.addEventListener('click', () => {
      localStorage.removeItem('cannacatalog_user_session');
      this.updateUserSessionUI();
      this.authModal?.close();
      this.showToast('👋 Sesión cerrada correctamente.');
    });
  }

  switchAuthTab(tab) {
    if (tab === 'login') {
      if (this.authLoginForm) this.authLoginForm.style.display = 'block';
      if (this.authRegisterForm) this.authRegisterForm.style.display = 'none';
      if (this.tabLoginBtn) {
        this.tabLoginBtn.style.background = 'var(--primary-emerald)';
        this.tabLoginBtn.style.color = '#000';
      }
      if (this.tabRegisterBtn) {
        this.tabRegisterBtn.style.background = 'transparent';
        this.tabRegisterBtn.style.color = 'var(--text-muted)';
      }
    } else {
      if (this.authLoginForm) this.authLoginForm.style.display = 'none';
      if (this.authRegisterForm) this.authRegisterForm.style.display = 'block';
      if (this.tabRegisterBtn) {
        this.tabRegisterBtn.style.background = 'var(--primary-emerald)';
        this.tabRegisterBtn.style.color = '#000';
      }
      if (this.tabLoginBtn) {
        this.tabLoginBtn.style.background = 'transparent';
        this.tabLoginBtn.style.color = 'var(--text-muted)';
      }
    }
  }

  getUserSession() {
    try {
      const data = localStorage.getItem('cannacatalog_user_session');
      return data ? JSON.parse(data) : null;
    } catch (e) {
      return null;
    }
  }

  updateUserSessionUI() {
    const session = this.getUserSession();
    if (!this.authBtnText || !this.btnUserAuth) return;

    if (session) {
      this.authBtnText.textContent = session.name;
      this.btnUserAuth.style.background = 'rgba(16, 185, 129, 0.25)';
      this.btnUserAuth.style.borderColor = 'var(--primary-emerald)';
      this.btnUserAuth.style.color = '#fff';
    } else {
      this.authBtnText.textContent = 'Iniciar Sesión';
      this.btnUserAuth.style.background = 'rgba(16, 185, 129, 0.15)';
      this.btnUserAuth.style.borderColor = 'rgba(16, 185, 129, 0.4)';
      this.btnUserAuth.style.color = '#6EE7B7';
    }
  }

  /* 3. CATÁLOGO CON FILTROS & ORDENACIÓN */
  populateBankDropdown() {
    if (!this.filterBank) return;

    const bankCounts = {};
    STRAINS_DATABASE.forEach(s => {
      bankCounts[s.bank] = (bankCounts[s.bank] || 0) + 1;
    });

    const bankEmojis = {
      "Nirvana Seeds": "🧘",
      "Dinafem Seeds": "🌱",
      "BSF Seeds": "🔥",
      "Ripper Seeds": "🌻",
      "Barney's Farm": "🇳🇱",
      "Sweet Seeds": "🍓",
      "Royal Queen Seeds": "👑",
      "Dutch Passion": "🌷",
      "Philosopher Seeds": "🧠",
      "Humboldt Seed": "🌲",
      "00 Seeds Bank": "🔢",
      "Buddha Seeds": "🪷",
      "R-Kiem Seeds": "🎨",
      "Positronics Seeds": "⚡",
      "ACE Seeds": "🌍",
      "Pyramid Seeds": "🔺",
      "Blimburn Seeds": "🔥",
      "Genehtik Seeds": "🧬",
      "Heavyweight Seeds": "🥊",
      "Cannabiogen": "🧪",
      "Sensi Seeds": "🏛️",
      "Green House Seed Co.": "🏡",
      "Serious Seeds": "🎯",
      "TH Seeds": "🗽",
      "Paradise Seeds": "🌴",
      "DNA Genetics": "🧬",
      "White Label Seed Co.": "🏷️",
      "Soma Seeds": "🛕",
      "The Flying Dutchmen": "🇳🇱",
      "Seedsman": "👨‍🌾",
      "Exotic Genetix": "👑",
      "Compound Genetics": "🧪",
      "In-House Genetics": "🏠",
      "Ethos Genetics": "⚡",
      "Archive Seed Bank": "📦",
      "Raw Genetics": "🥩"
    };

    const currentVal = this.filterBank.value || 'all';
    const totalBanks = Object.keys(bankCounts).length;

    let optionsHTML = `<option value="all">🌐 Todos los Bancos (${totalBanks})</option>`;
    
    // Sort banks alphabetically A-Z for fast location
    const sortedBanks = Object.entries(bankCounts).sort((a, b) => a[0].localeCompare(b[0], 'es'));

    sortedBanks.forEach(([bankName, count]) => {
      const emoji = bankEmojis[bankName] || "🌿";
      optionsHTML += `<option value="${bankName}">${emoji} ${bankName} (${count} cepas)</option>`;
    });

    this.filterBank.innerHTML = optionsHTML;
    if (Object.keys(bankCounts).includes(currentVal)) {
      this.filterBank.value = currentVal;
    } else {
      this.filterBank.value = 'all';
    }
  }

  initCatalog() {
    this.populateBankDropdown();

    const applyFiltersAndSort = () => {
      const query = (this.searchInput?.value || '').toLowerCase().trim();
      const bank = this.filterBank?.value || 'all';
      const species = this.filterSpecies?.value || 'all';
      const terpene = this.filterTerpene?.value || 'all';
      const sortCriterion = this.sortBy?.value || 'indoor';

      let filtered = (STRAINS_DATABASE || []).filter(strain => {
        if (!strain || typeof strain !== 'object' || !strain.name) return false;

        const sName = (strain.name || '').toLowerCase();
        const sGenetics = (strain.genetics || '').toLowerCase();
        const sBank = (strain.bank || '').toLowerCase();
        const sAka = (strain.aka || '').toLowerCase();
        const sFlavors = Array.isArray(strain.flavors) ? strain.flavors : [];

        const matchQuery = !query ||
                           sName.includes(query) ||
                           sGenetics.includes(query) ||
                           sBank.includes(query) ||
                           sAka.includes(query) ||
                           sFlavors.some(f => (f || '').toLowerCase().includes(query));
        const matchBank = bank === 'all' || strain.bank === bank;
        const matchSpecies = species === 'all' || strain.species === species;
        const matchTerpene = terpene === 'all' || strain.dominantTerpene === terpene;

        return matchQuery && matchBank && matchSpecies && matchTerpene;
      });

      if (sortCriterion === 'indoor') {
        filtered.sort((a, b) => b.yieldIndoor - a.yieldIndoor);
      } else if (sortCriterion === 'outdoor') {
        filtered.sort((a, b) => b.yieldOutdoor - a.yieldOutdoor);
      } else if (sortCriterion === 'flavor') {
        filtered.sort((a, b) => (a.flavors[0] || '').localeCompare(b.flavors[0] || ''));
      } else if (sortCriterion === 'thc') {
        filtered.sort((a, b) => b.thc - a.thc);
      } else if (sortCriterion === 'rating') {
        filtered.sort((a, b) => b.rating - a.rating);
      }

      this.currentStrains = filtered;
      this.renderStrainsGrid(this.currentStrains);
    };

    this.searchInput?.addEventListener('input', applyFiltersAndSort);
    this.filterBank?.addEventListener('change', applyFiltersAndSort);
    this.filterSpecies?.addEventListener('change', applyFiltersAndSort);
    this.filterTerpene?.addEventListener('change', applyFiltersAndSort);
    this.sortBy?.addEventListener('change', applyFiltersAndSort);

    applyFiltersAndSort();
  }

  renderStrainsGrid(strains) {
    if (!this.strainsGrid) return;
    if (this.catalogCount) {
      this.catalogCount.textContent = `Mostrando ${strains.length} cepa(s)`;
    }

    if (strains.length === 0) {
      this.strainsGrid.innerHTML = `
        <div class="empty-state" style="grid-column: 1 / -1;">
          <div class="empty-icon">🔍</div>
          <h3>No se encontraron cepas</h3>
          <p>Ajusta el filtro de banco, especie o término de búsqueda.</p>
        </div>
      `;
      return;
    }

    const bankIcons = {
      'Dinafem Seeds': '🌱',
      'BSF Seeds': '🔥',
      'Ripper Seeds': '🌻',
      "Barney's Farm": '🇳🇱',
      'Sweet Seeds': '🍓',
      'Royal Queen Seeds': '👑',
      'Dutch Passion': '🌷',
      'Philosopher Seeds': '🧠',
      'Humboldt Seed': '🌲',
      '00 Seeds Bank': '🔢',
      'Buddha Seeds': '🪷',
      'R-Kiem Seeds': '🎨',
      'Positronics Seeds': '⚡',
      'ACE Seeds': '🌍',
      'Pyramid Seeds': '🔺',
      'Blimburn Seeds': '🔥',
      'Genehtik Seeds': '🧬',
      'Heavyweight Seeds': '🥊',
      'Cannabiogen': '🧪',
      'Sensi Seeds': '🏛️',
      'Green House Seed Co.': '🏡',
      'Serious Seeds': '🎯',
      'TH Seeds': '🗽',
      'Paradise Seeds': '🌴',
      'DNA Genetics': '🧬'
    };



    this.strainsGrid.innerHTML = strains.map(strain => {
      const terpeneData = TERPENES_INFO[strain.dominantTerpene];
      const icon = bankIcons[strain.bank] || '🌿';
      const stars = '★'.repeat(Math.round(strain.rating)) + '☆'.repeat(5 - Math.round(strain.rating));
      const strainImg = strain.image;
      const imgTag = strainImg ? `<img src="${strainImg}" alt="${strain.name}" class="card-visual-img" loading="lazy" decoding="async" onerror="this.style.display='none'; if(this.nextElementSibling) this.nextElementSibling.style.opacity='1';" />` : '';
      const isCompared = (this.comparedStrains || []).includes(strain.id);

      return `
        <div class="strain-card" style="--card-accent: ${strain.visualColor}; cursor: pointer;" onclick="document.dispatchEvent(new CustomEvent('openStrainDetail', { detail: '${strain.id}' }))">
          <div class="card-visual-banner" onclick="event.stopPropagation(); window.app && window.app.openImageLightbox('${strainImg}', '${strain.name.replace(/'/g, "\\'")}', '${strain.bank.replace(/'/g, "\\'")}')" title="🔍 Haz clic para ver foto en alta resolución con Zoom HD">
            ${imgTag}
            <div class="card-visual-banner-inner" style="background: ${strain.visualColor}; ${strain.bgPattern}; opacity: ${strainImg ? '0' : '1'};"></div>
            <div class="card-banner-overlay"></div>
            ${strainImg ? `<div style="position: absolute; top: 8px; right: 8px; z-index: 10; background: rgba(0,0,0,0.75); backdrop-filter: blur(6px); border: 1px solid rgba(16,185,129,0.5); border-radius: 50px !important; padding: 3px 10px; font-size: 0.7rem; color: #6EE7B7; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);">🔍 Zoom HD</div>` : ''}
            <div style="position: absolute; bottom: 8px; left: 12px; right: 12px; display: flex; justify-content: space-between; align-items: center; color: #fff; z-index: 2;">
              <span style="font-size: 0.72rem; font-weight: 800; background: rgba(0,0,0,0.7); padding: 3px 10px; border-radius: 0 !important; backdrop-filter: blur(6px); border: 1px solid rgba(255,255,255,0.15);">
                ${icon} ${strain.bank}
              </span>
              <span style="font-size: 0.78rem; color: #FFD700; font-weight: 700; text-shadow: 0 1px 4px rgba(0,0,0,0.9); background: rgba(0,0,0,0.6); padding: 3px 10px; border-radius: 0 !important; backdrop-filter: blur(4px);">
                ${stars}
              </span>
            </div>
          </div>

          <div class="card-body">
            <div class="strain-header">
              <div>
                <h3 class="strain-title">${strain.name}</h3>
                <div class="strain-bank-label">${strain.genetics}</div>
              </div>
              <span class="badge-species ${strain.species.toLowerCase()}">${strain.species}</span>
            </div>

            <div class="strain-stats">
              <span class="stat-pill">🔥 THC ${strain.thc}%</span>
              <span class="stat-pill" style="background: rgba(16,185,129,0.12); color: #10B981; border: 1px solid rgba(16,185,129,0.25);">
                🏠 ${strain.yieldIndoor} g/m²
              </span>
              <span class="stat-pill" style="background: rgba(139,92,246,0.12); color: #C4B5FD; border: 1px solid rgba(139,92,246,0.25);">
                🌳 ${strain.yieldOutdoor} g/planta
              </span>
            </div>

            <div class="terpene-indicator" style="background: ${terpeneData?.color || '#10B981'}15; border: 1px solid ${terpeneData?.color || '#10B981'}35; color: ${terpeneData?.color || '#10B981'};">
              <span>🌿 Terpeno: <strong>${terpeneData?.name || strain.dominantTerpene}</strong></span>
            </div>

            <div class="strain-tags">
              ${strain.flavors.map(f => `<span class="tag-item">👅 ${f}</span>`).join('')}
            </div>

            <div class="card-actions" onclick="event.stopPropagation()" style="display: flex; gap: 8px;">
              <button class="btn btn-primary" style="flex: 1; border-radius: 8px !important;" onclick="event.stopPropagation(); document.dispatchEvent(new CustomEvent('openStrainDetail', { detail: '${strain.id}' }))">
                📋 Ficha
              </button>
              <button class="btn-compare-toggle ${isCompared ? 'active' : ''}" data-strain-id="${strain.id}" onclick="event.stopPropagation(); window.app && window.app.toggleCompareStrain('${strain.id}')" title="${isCompared ? 'Quitar del comparador' : 'Comparar (hasta 3 cepas)'}">
                ⚖️ ${isCompared ? 'Comparando' : 'Comparar'}
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');

    this.updateCompareUI();
  }

  filterByStash() {
    const stashIds = this.bitacora.stash;
    const stashStrains = STRAINS_DATABASE.filter(s => stashIds.includes(s.id));
    
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('open-stash-btn')?.classList.add('active');
    document.querySelectorAll('.app-section').forEach(s => s.classList.remove('active-section'));
    document.getElementById('section-catalog')?.classList.add('active-section');

    this.renderStrainsGrid(stashStrains);
    if (this.catalogCount) {
      this.catalogCount.textContent = `Mostrando ${stashStrains.length} cepa(s) en Mi Stash Favorito`;
    }
  }

  updateStashCounter() {
    if (this.stashCounter) {
      this.stashCounter.textContent = this.bitacora.stash.length;
    }
  }

  /* 4. MATCHER DE ACTIVIDADES */
  initMatcherEvents() {
    const activityCards = document.querySelectorAll('.activity-card');
    activityCards.forEach(card => {
      card.addEventListener('click', () => {
        activityCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        this.selectedActivity = card.getAttribute('data-activity');
      });
    });

    document.getElementById('btn-spin-roulette')?.addEventListener('click', () => {
      this.matcher.spinRoulette(this.selectedActivity, (winner) => {
        this.showToast(`🎯 ¡Match Perfecto: ${winner.name}!`);
      });
    });
  }

  /* 5. BITÁCORA DE VIVENCIAS */
  initBitacoraEvents() {
    const btnOpenAddLog = document.getElementById('btn-open-add-log');
    const strainSelect = document.getElementById('log-strain-select');
    const fileInput = document.getElementById('log-photo-file');
    const photoPreview = document.getElementById('photo-preview');
    let currentPhotoBase64 = null;

    btnOpenAddLog?.addEventListener('click', () => {
      if (strainSelect) {
        strainSelect.innerHTML = STRAINS_DATABASE.map(s => `<option value="${s.name}">${s.name} (${s.species} - ${s.bank})</option>`).join('');
      }
      if (this.addLogModal && typeof this.addLogModal.showModal === 'function') {
        if (!this.addLogModal.open) this.addLogModal.showModal();
      }
    });

    fileInput?.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          currentPhotoBase64 = event.target.result;
          if (photoPreview) {
            photoPreview.innerHTML = `<img src="${currentPhotoBase64}" alt="Vista previa" />`;
          }
        };
        reader.readAsDataURL(file);
      }
    });

    this.addLogForm?.addEventListener('submit', (e) => {
      e.preventDefault();
      const newEntry = {
        strainName: document.getElementById('log-strain-select').value,
        location: document.getElementById('log-location-input').value,
        preMood: document.getElementById('log-premood-input').value,
        postMood: document.getElementById('log-postmood-input').value,
        rating: document.getElementById('log-rating-select').value,
        photoUrl: currentPhotoBase64,
        notes: document.getElementById('log-notes-input').value
      };

      this.bitacora.addLog(newEntry);
      if (this.addLogModal) this.addLogModal.close();
      this.addLogForm.reset();
      if (photoPreview) photoPreview.innerHTML = '';
      currentPhotoBase64 = null;

      this.bitacora.renderLogList(document.getElementById('bitacora-list'));
      this.showToast('📝 ¡Paseo registrado con éxito!');
    });
  }

  /* 6. MEZCLADOR & COMPARADOR DE CEPAS */
  initBlenderAndCompare() {
    const blendS1 = document.getElementById('blend-strain-1');
    const blendS2 = document.getElementById('blend-strain-2');
    const compS1 = document.getElementById('compare-strain-1');
    const compS2 = document.getElementById('compare-strain-2');
    const ratioSlider = document.getElementById('blend-ratio');
    const ratioVal = document.getElementById('ratio-val');

    const optionsHTML = STRAINS_DATABASE.map(s => `<option value="${s.id}">${s.name} (${s.species} - ${s.bank})</option>`).join('');

    if (blendS1) blendS1.innerHTML = optionsHTML;
    if (blendS2) blendS2.innerHTML = optionsHTML;
    if (compS1) compS1.innerHTML = optionsHTML;
    if (compS2) compS2.innerHTML = optionsHTML;

    ratioSlider?.addEventListener('input', (e) => {
      if (ratioVal) ratioVal.textContent = e.target.value;
    });

    document.getElementById('blend-form')?.addEventListener('submit', (e) => {
      e.preventDefault();
      const s1Id = blendS1.value;
      const s2Id = blendS2.value;
      const ratio = parseInt(ratioSlider.value);

      const blended = AdvancedTools.blendStrains(s1Id, s2Id, ratio);
      const resBox = document.getElementById('blend-result');
      if (resBox) {
        resBox.innerHTML = `
          <h4>🧪 Resultado de la Mezcla Personalizada</h4>
          <p><strong>Fórmula:</strong> ${blended.ratioText}</p>
          <p>🔥 <strong>THC Estimado:</strong> ${blended.thc}% | 💧 <strong>CBD Estimado:</strong> ${blended.cbd}%</p>
          <p>👅 <strong>Perfil de Sabores:</strong> ${blended.combinedFlavors.join(', ')}</p>
          <p>⚡ <strong>Efectos Combinados:</strong> ${blended.combinedEffects.join(', ')}</p>
        `;
      }
    });

    document.getElementById('compare-form')?.addEventListener('submit', (e) => {
      e.preventDefault();
      const comp = AdvancedTools.compareStrains(compS1.value, compS2.value);
      const resBox = document.getElementById('compare-result');
      if (comp && resBox) {
        resBox.innerHTML = `
          <h4>📊 Comparación Frente a Frente</h4>
          <div style="display: flex; gap: 1rem; justify-content: space-between; margin-top: 0.5rem;">
            <div>
              <strong>${comp.strain1.name}</strong> (${comp.strain1.species})
              <p>THC: ${comp.strain1.thc}% | Indoor: ${comp.strain1.yieldIndoor}g | Outdoor: ${comp.strain1.yieldOutdoor}g</p>
              <p>Sabores: ${comp.strain1.flavors.join(', ')}</p>
            </div>
            <div>VS</div>
            <div>
              <strong>${comp.strain2.name}</strong> (${comp.strain2.species})
              <p>THC: ${comp.strain2.thc}% | Indoor: ${comp.strain2.yieldIndoor}g | Outdoor: ${comp.strain2.yieldOutdoor}g</p>
              <p>Sabores: ${comp.strain2.flavors.join(', ')}</p>
            </div>
          </div>
        `;
      }
    });
  }

  /* 7. TERPENOS & VAPORIZACIÓN */
  initTerpeneSection() {
    const grid = document.getElementById('terpenes-grid');
    const vapeGrid = document.getElementById('vape-temp-grid');

    if (vapeGrid) {
      const temps = AdvancedTools.getVapeTemps();
      vapeGrid.innerHTML = temps.map(t => `
        <div class="vape-card" style="border-top: 3px solid ${t.color}">
          <strong style="color: ${t.color}">${t.terpene}</strong>
          <div class="vape-temp">${t.tempC}°C <small style="font-size: 0.9rem">(${t.tempF}°F)</small></div>
          <p style="font-size: 0.8rem; color: var(--text-muted);">${t.effect}</p>
        </div>
      `).join('');
    }

    if (grid) {
      grid.innerHTML = Object.entries(TERPENES_INFO).map(([key, info]) => `
        <div class="terpene-card" style="border-top: 4px solid ${info.color}">
          <div class="terpene-name" style="color: ${info.color}">${info.name}</div>
          <p><strong>👃 Aroma:</strong> ${info.aroma}</p>
          <p><strong>⚡ Efectos:</strong> ${info.effects}</p>
        </div>
      `).join('');
    }
  }

  /* 8. MODO SOBRIO */
  initSobrioMode() {
    document.getElementById('btn-sobrio-mode')?.addEventListener('click', () => {
      if (this.sobrioModal && typeof this.sobrioModal.showModal === 'function') {
        if (!this.sobrioModal.open) this.sobrioModal.showModal();
      }
    });

    document.getElementById('btn-play-solfeggio')?.addEventListener('click', () => {
      this.audioEngine.playSolfeggio432Hz();
      this.showToast('🎧 Solfeggio 432Hz activado');
    });

    document.getElementById('btn-play-noise')?.addEventListener('click', () => {
      this.audioEngine.playPinkNoise();
      this.showToast('🌧️ Sonido de lluvia activado');
    });

    document.getElementById('btn-stop-audio')?.addEventListener('click', () => {
      this.audioEngine.stopAll();
      this.showToast('⏹️ Audio detenido');
    });
  }

  /* 10. MOTOR DE TEMAS */
  initThemeEngine() {
    const selector = document.getElementById('theme-selector');
    const savedTheme = localStorage.getItem('cannacatalog_theme') || 'emerald';
    if (selector) {
      selector.value = savedTheme;
      AdvancedTools.setTheme(savedTheme);

      selector.addEventListener('change', (e) => {
        AdvancedTools.setTheme(e.target.value);
        this.showToast(`🎨 Tema ${e.target.value} aplicado`);
      });
    }
  }

  /* 10. EVENTOS EN TIEMPO REAL */
  initCustomEventListeners() {
    document.addEventListener('openStrainDetail', (e) => {
      this.openStrainDetailModal(e.detail);
    });

    document.addEventListener('toggleStash', (e) => {
      const strainId = e.detail;
      const inStash = this.bitacora.toggleStash(strainId);
      this.updateStashCounter();
      this.renderStrainsGrid(this.currentStrains);
      this.showToast(inStash ? '💚 Guardado en Mi Stash' : '🤍 Eliminado de Mi Stash');
    });

    document.addEventListener('deleteLog', (e) => {
      if (confirm('¿Eliminar este registro de caminata/cata?')) {
        this.bitacora.deleteLog(e.detail);
        this.bitacora.renderLogList(document.getElementById('bitacora-list'));
        this.showToast('🗑️ Registro eliminado');
      }
    });

    document.addEventListener('generateMission', (e) => {
      const { strainId, activityId } = e.detail;
      const missionData = MissionGenerator.generateMission(strainId, activityId);
      MissionGenerator.renderMissionModal(missionData, 'mission-modal-content');
      if (this.missionModal && typeof this.missionModal.showModal === 'function') {
        if (!this.missionModal.open) this.missionModal.showModal();
      }
    });

    document.addEventListener('closeMissionModal', () => {
      if (this.missionModal) this.missionModal.close();
      this.showToast('🚀 ¡Misión Aceptada!');
    });

    if (this.strainDetailModal) {
      this.strainDetailModal.addEventListener('click', (e) => {
        const rect = this.strainDetailModal.getBoundingClientRect();
        const isInDialog = (
          rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
          rect.left <= e.clientX && e.clientX <= rect.left + rect.width
        );
        if (!isInDialog) {
          this.strainDetailModal.close();
        }
      });
    }

    if (this.imageLightboxModal) {
      this.imageLightboxModal.addEventListener('click', (e) => {
        if (e.target === this.imageLightboxModal) {
          this.imageLightboxModal.close();
        }
      });
    }
  }

  openImageLightbox(imgSrc, title = 'Genética', subtitle = '') {
    if (!imgSrc) return;

    if (!this.imageLightboxModal) {
      this.imageLightboxModal = document.getElementById('image-lightbox-modal');
    }
    if (!this.lightboxImg) {
      this.lightboxImg = document.getElementById('lightbox-img');
    }
    if (!this.lightboxTitle) {
      this.lightboxTitle = document.getElementById('lightbox-title');
    }
    if (!this.lightboxSubtitle) {
      this.lightboxSubtitle = document.getElementById('lightbox-subtitle');
    }

    if (this.lightboxImg) this.lightboxImg.src = imgSrc;
    if (this.lightboxTitle) this.lightboxTitle.textContent = title;
    if (this.lightboxSubtitle) this.lightboxSubtitle.textContent = subtitle ? `🏛️ ${subtitle}` : 'FOTOGRAFÍA BOTÁNICA • ALTA RESOLUCIÓN HD';

    if (typeof this.resetLightboxZoom === 'function') {
      this.resetLightboxZoom();
    }

    if (this.imageLightboxModal && typeof this.imageLightboxModal.showModal === 'function') {
      if (!this.imageLightboxModal.open) {
        this.imageLightboxModal.showModal();
      }
    }
  }

  openStrainDetailModal(strainId) {
    const strain = STRAINS_DATABASE.find(s => s.id === strainId);
    if (!strain || !this.strainDetailContent) return;

    const terpeneData = TERPENES_INFO[strain.dominantTerpene];
    const vapeTemps = AdvancedTools.getVapeTemps();
    const vapeTemp = vapeTemps.find(t => t.terpene === terpeneData?.name);

    const stars = '★'.repeat(Math.round(strain.rating)) + '☆'.repeat(5 - Math.round(strain.rating));

    const activityIcons = {
      nature_walk: '🌲', gaming: '🎮', creativity: '🎨',
      social: '🎉', relax_sleep: '🌙', meditation: '🧘', workout: '🏋️'
    };
    const activityLabels = {
      nature_walk: 'Senderismo', gaming: 'Gaming', creativity: 'Creatividad',
      social: 'Social', relax_sleep: 'Relax/Cine', meditation: 'Meditación', workout: 'Deporte'
    };

    const terpeneEntries = Object.entries(strain.terpenes || {})
      .sort((a, b) => b[1] - a[1])
      .slice(0, 4);

    const terpeneBars = terpeneEntries.map(([key, pct]) => {
      const info = TERPENES_INFO[key];
      return `
        <div style="margin-bottom: 0.75rem;">
          <div style="display:flex; justify-content:space-between; font-size:0.82rem; margin-bottom:4px;">
            <span style="color:${info?.color || '#10B981'}; font-weight:700;">${info?.name || key}</span>
            <span style="color: var(--text-muted); font-weight: 600;">${pct}%</span>
          </div>
          <div style="height:7px; background:rgba(255,255,255,0.06); border-radius: 50px !important; overflow:hidden;">
            <div style="height:100%; width:${pct}%; background: linear-gradient(90deg, ${info?.color || '#10B981'}88, ${info?.color || '#10B981'}); border-radius: 50px !important; transition: width 0.8s ease;"></div>
          </div>
        </div>`;
    }).join('');

    const mainImg = strain.image;

    this.strainDetailContent.innerHTML = `
      <div class="pro-spec-sheet">
        
        <!-- BOTÓN CIERRE FLOTANTE EN ESQUINA SUPERIOR DERECHA -->
        <button class="close-pro-btn" onclick="document.getElementById('strain-detail-modal').close()" title="Cerrar (ESC)">✕</button>

        <!-- CONTENIDO SCROLLABLE EN POPUP CENTRADO -->
        <div class="pro-body-scrollable">
          
          <!-- HERO BANNER -->
          <div class="pro-hero-banner" style="background: ${strain.visualColor};">
            <div style="position:absolute; inset:0; ${strain.bgPattern}; opacity:0.35; pointer-events:none;"></div>
            
            ${mainImg ? `
            <div class="pro-hero-photo-wrapper" onclick="window.app && window.app.openImageLightbox('${mainImg}', '${strain.name.replace(/'/g, "\\'")}', '${strain.bank.replace(/'/g, "\\'")}')" title="Haz clic para ver la foto en alta resolución 🔍">
              <img src="${mainImg}" alt="${strain.name}" class="pro-hero-img" loading="lazy" decoding="async" onerror="this.style.display='none';" />
              <div class="pro-hero-vignette"></div>
              
              <div class="pro-hero-zoom-badge">
                🔍 Toca para ver foto HD
              </div>
              
              <div class="pro-hero-info-overlay">
                <div class="pro-hero-info-left">
                  <div class="pro-hero-badges-row">
                    <span class="badge-species ${strain.species.toLowerCase()}">${strain.species}</span>
                    <span class="pro-hero-bank-pill">
                      🏛️ ${strain.bank}
                    </span>
                  </div>
                  <h1 class="pro-strain-name-lg">${strain.name}</h1>
                  <div class="pro-strain-aka">🧬 Linaje: ${strain.genetics}</div>
                </div>
                <div class="pro-hero-info-right">
                  <div class="pro-hero-rating-pill">
                    <span>${stars}</span>
                    <span>${strain.rating}/5</span>
                  </div>
                  <div class="pro-hero-reviews-text">(${strain.reviewsCount} reseñas verificadas)</div>
                </div>
              </div>
            </div>` : `
            <div class="pro-hero-photo-wrapper" style="height: auto; min-height: 180px;">
              <div class="pro-hero-info-overlay" style="position: relative; inset: auto; padding: 1.8rem 1.4rem;">
                <div class="pro-hero-info-left">
                  <div class="pro-hero-badges-row">
                    <span class="badge-species ${strain.species.toLowerCase()}">${strain.species}</span>
                    <span class="pro-hero-bank-pill">
                      🏛️ ${strain.bank}
                    </span>
                  </div>
                  <h1 class="pro-strain-name-lg">${strain.name}</h1>
                  <div class="pro-strain-aka">🧬 Linaje: ${strain.genetics}</div>
                </div>
                <div class="pro-hero-info-right">
                  <div class="pro-hero-rating-pill">
                    ${stars} ${strain.rating}/5
                  </div>
                  <div class="pro-hero-reviews-text">(${strain.reviewsCount} reseñas)</div>
                </div>
              </div>
            </div>`}
          </div>

          <!-- CUADRO DE MÉTRICAS CLAVE (4 CARDS EJECUTIVAS REDONDEADAS) -->
          <div class="pro-metrics-grid">
            <div class="pro-metric-card">
              <span class="pro-metric-label">🔥 Concentración THC</span>
              <div class="pro-metric-value">${strain.thc}%</div>
              <div class="pro-metric-sub">${strain.thc > 20 ? 'Alta Potencia' : 'Potencia Moderada'}</div>
            </div>
            <div class="pro-metric-card">
              <span class="pro-metric-label">💚 Concentración CBD</span>
              <div class="pro-metric-value" style="color: #6EE7B7;">${strain.cbd}%</div>
              <div class="pro-metric-sub">Ratio Equilibrado</div>
            </div>
            <div class="pro-metric-card">
              <span class="pro-metric-label">🏠 Cultivo Indoor</span>
              <div class="pro-metric-value" style="color: #60A5FA;">${strain.yieldIndoor} <small class="pro-metric-unit">g/m²</small></div>
              <div class="pro-metric-sub">🗓️ ${strain.floweringDays} Días Floración</div>
            </div>
            <div class="pro-metric-card">
              <span class="pro-metric-label">🌳 Cultivo Outdoor</span>
              <div class="pro-metric-value" style="color: #F59E0B;">${strain.yieldOutdoor} <small class="pro-metric-unit">g/planta</small></div>
              <div class="pro-metric-sub">🌍 ${strain.origin}</div>
            </div>
          </div>

          <!-- CUERPO PRINCIPAL CON DETALLES TÉCNICOS -->
          <div class="pro-details-container">
            
            <!-- DESCRIPCIÓN BOTÁNICA -->
            <div class="pro-section-card">
              <h3 class="pro-section-title">📝 Perfil Botánico y Resumen del Criador</h3>
              <p class="pro-desc-quote">${strain.description}</p>
            </div>

            <!-- ANÁLISIS TERPÉNICO & VAPORIZACIÓN -->
            <div class="pro-section-card" style="background: rgba(16, 185, 129, 0.06); border: 1.5px solid rgba(16, 185, 129, 0.35);">
              <h3 class="pro-section-title" style="color: ${terpeneData?.color || '#10B981'}; font-size: 1.15rem;">
                <span>🔬 Perfil Cromatográfico — Terpeno Dominante: <strong>${terpeneData?.name || strain.dominantTerpene}</strong></span>
              </h3>
              
              <div class="pro-terp-vape-grid">
                <div>
                  <p style="font-size: 0.84rem; color: var(--text-muted); margin-bottom: 1rem; font-weight: 600;">Espectro relativo de terpenos en floración seca:</p>
                  ${terpeneBars}
                </div>
                <div>
                  ${vapeTemp ? `
                  <div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.15); border-radius: 14px !important; padding: 1.2rem; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <span style="font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.8px; color: var(--text-muted); display: block; margin-bottom: 6px;">🌡️ Vaporización Óptima</span>
                    <div style="font-size: 1.75rem; font-weight: 900; color: ${terpeneData?.color || '#10B981'};">
                      ${vapeTemp.tempC}°C <small style="font-size: 0.95rem; color: var(--text-muted);">(${vapeTemp.tempF}°F)</small>
                    </div>
                    <p style="font-size: 0.85rem; color: rgba(255,255,255,0.9); margin-top: 8px; line-height: 1.45;">
                      ⚡ ${vapeTemp.effect}
                    </p>
                  </div>` : ''}
                </div>
              </div>
            </div>

            <!-- SABORES, EFECTOS Y ACTIVIDADES -->
            <div class="pro-tri-cards-grid">
              
              <div class="pro-section-card" style="margin-bottom: 0;">
                <h4 style="font-size: 0.9rem; font-weight: 800; color: #fff; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 6px;">
                  👅 Sabores & Aromas
                </h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
                  ${strain.flavors.map(f => `
                    <span style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); color: #fff; padding: 5px 12px; border-radius: 50px !important; font-size: 0.8rem; font-weight: 600;">
                      👅 ${f}
                    </span>`).join('')}
                </div>
              </div>

              <div class="pro-section-card" style="margin-bottom: 0;">
                <h4 style="font-size: 0.9rem; font-weight: 800; color: #fff; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 6px;">
                  ✨ Efectos Sensoriales
                </h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
                  ${strain.effects.map(e => `
                    <span style="background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.3); color: #6EE7B7; padding: 5px 12px; border-radius: 50px !important; font-size: 0.8rem; font-weight: 700;">
                      ⚡ ${e}
                    </span>`).join('')}
                </div>
              </div>

              <div class="pro-section-card" style="margin-bottom: 0;">
                <h4 style="font-size: 0.9rem; font-weight: 800; color: #fff; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 6px;">
                  🎯 Actividades Ideales
                </h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
                  ${(strain.activities || []).map(a => `
                    <span style="background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); color: #FCD34D; padding: 5px 12px; border-radius: 50px !important; font-size: 0.8rem; font-weight: 700;">
                      ${activityIcons[a] || '🌀'} ${activityLabels[a] || a}
                    </span>`).join('')}
                </div>
              </div>

            </div>

          </div>

        </div>

        <!-- FOOTER ACCIONES FLOTANTE FIJO -->
        <div class="pro-floating-footer">
          <div style="font-size: 0.85rem; color: var(--text-muted);">
            <span>🏛️ Banco Criador: <strong style="color: #fff;">${strain.bank}</strong></span>
          </div>

          <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
            <button class="btn btn-emerald-lg"
              onclick="document.dispatchEvent(new CustomEvent('generateMission', { detail: { strainId: '${strain.id}', activityId: '${strain.activities?.[0] || 'nature_walk'}' } })); document.getElementById('strain-detail-modal').close();">
              🚀 Generar Misión IA
            </button>
          </div>
        </div>

      </div>
    `;

    if (this.strainDetailModal && typeof this.strainDetailModal.showModal === 'function') {
      if (!this.strainDetailModal.open) this.strainDetailModal.showModal();
    }
  }


  /* LIGHTBOX ULTRA ZOOM & HD VIEWER ENGINE (Blindado y Defensivo) */
  initImageLightboxEngine() {
    this.lightboxScale = 1.0;
    this.lightboxTranslateX = 0;
    this.lightboxTranslateY = 0;
    this.isDragging = false;
    this.dragStartX = 0;
    this.dragStartY = 0;

    const getImg = () => document.getElementById('lightbox-img');
    const getViewport = () => document.getElementById('lightbox-viewport');
    const getIndicator = () => document.getElementById('lightbox-zoom-indicator');

    let baseFittedWidth = 0;

    const updateTransform = () => {
      const img = getImg();
      const indicator = getIndicator();
      if (!img) return;

      if (this.lightboxScale <= 1.0) {
        this.lightboxScale = 1.0;
        this.lightboxTranslateX = 0;
        this.lightboxTranslateY = 0;
        img.style.maxWidth = '85vw';
        img.style.maxHeight = '80vh';
        img.style.width = 'auto';
        img.style.height = 'auto';
        img.style.transform = 'translate3d(0, 0, 0)';
        baseFittedWidth = img.clientWidth || 0;
      } else {
        if (!baseFittedWidth || baseFittedWidth <= 0) {
          baseFittedWidth = img.clientWidth || Math.round(window.innerWidth * 0.5);
        }
        const scaledWidth = Math.round(baseFittedWidth * this.lightboxScale);
        img.style.maxWidth = 'none';
        img.style.maxHeight = 'none';
        img.style.width = scaledWidth + 'px';
        img.style.height = 'auto';
        img.style.transform = `translate3d(${this.lightboxTranslateX}px, ${this.lightboxTranslateY}px, 0)`;
      }

      if (indicator) {
        const pct = Math.round(this.lightboxScale * 100);
        indicator.textContent = `${pct}% ${this.lightboxScale > 1.0 ? '🔍 NATIVO HD (SIN PÉRDIDA)' : '(Vista Fit)'}`;
      }
    };

    const resetZoom = () => {
      this.lightboxScale = 1.0;
      this.lightboxTranslateX = 0;
      this.lightboxTranslateY = 0;
      baseFittedWidth = 0;
      updateTransform();
    };

    const setNativeScale = () => {
      const img = getImg();
      if (!img) return;
      const naturalW = img.naturalWidth || 1600;
      const clientW = baseFittedWidth || img.clientWidth || 400;
      const nativeRatio = Math.max(2.0, Math.min(6.0, naturalW / clientW));
      this.lightboxScale = Math.round(nativeRatio * 10) / 10;
      this.lightboxTranslateX = 0;
      this.lightboxTranslateY = 0;
      updateTransform();
    };

    this.resetLightboxZoom = resetZoom;
    this.updateLightboxTransform = updateTransform;

    // Delegación de clics en controles de zoom
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('#lightbox-btn-zoom-in, #lightbox-btn-zoom-out, #lightbox-btn-reset, #lightbox-btn-hd, #lightbox-close-btn');
      if (!btn) return;
      
      e.stopPropagation();
      const id = btn.id;
      if (id === 'lightbox-btn-zoom-in') {
        this.lightboxScale = Math.min(6.0, this.lightboxScale + 0.5);
        updateTransform();
      } else if (id === 'lightbox-btn-zoom-out') {
        this.lightboxScale = Math.max(1.0, this.lightboxScale - 0.5);
        if (this.lightboxScale === 1.0) {
          this.lightboxTranslateX = 0;
          this.lightboxTranslateY = 0;
        }
        updateTransform();
      } else if (id === 'lightbox-btn-reset') {
        resetZoom();
      } else if (id === 'lightbox-btn-hd') {
        setNativeScale();
      } else if (id === 'lightbox-close-btn') {
        const modal = document.getElementById('image-lightbox-modal');
        if (modal) modal.close();
      }
    });

    // Rueda del ratón (Wheel zoom) en el visor
    document.addEventListener('wheel', (e) => {
      const viewport = e.target.closest('#lightbox-viewport, .lightbox-viewport');
      if (!viewport) return;

      const modal = document.getElementById('image-lightbox-modal');
      if (!modal || !modal.open) return;

      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.25 : 0.8;
      const newScale = Math.min(Math.max(1.0, this.lightboxScale * zoomFactor), 6.0);

      if (newScale === 1.0) {
        this.lightboxTranslateX = 0;
        this.lightboxTranslateY = 0;
      }

      this.lightboxScale = Math.round(newScale * 100) / 100;
      updateTransform();
    }, { passive: false });

    // Doble clic para alternar Zoom 1x / Nativo HD
    document.addEventListener('dblclick', (e) => {
      const viewport = e.target.closest('#lightbox-viewport, .lightbox-viewport');
      if (!viewport) return;

      if (this.lightboxScale > 1.0) {
        resetZoom();
      } else {
        setNativeScale();
      }
    });

    // Arrastre con ratón / táctil (Drag to Pan)
    const onPointerDown = (e) => {
      const viewport = e.target.closest('#lightbox-viewport, .lightbox-viewport');
      if (!viewport || this.lightboxScale <= 1.0) return;

      this.isDragging = true;
      viewport.classList.add('is-dragging');
      this.dragStartX = e.clientX || (e.touches && e.touches[0].clientX);
      this.dragStartY = e.clientY || (e.touches && e.touches[0].clientY);
    };

    const onPointerMove = (e) => {
      if (!this.isDragging || this.lightboxScale <= 1.0) return;
      const currentX = e.clientX || (e.touches && e.touches[0].clientX);
      const currentY = e.clientY || (e.touches && e.touches[0].clientY);

      const deltaX = currentX - this.dragStartX;
      const deltaY = currentY - this.dragStartY;

      this.lightboxTranslateX += deltaX;
      this.lightboxTranslateY += deltaY;

      this.dragStartX = currentX;
      this.dragStartY = currentY;

      updateTransform();
    };

    const onPointerUp = () => {
      if (this.isDragging) {
        this.isDragging = false;
        const viewport = getViewport();
        if (viewport) viewport.classList.remove('is-dragging');
      }
    };

    window.addEventListener('mousedown', onPointerDown);
    window.addEventListener('mousemove', onPointerMove);
    window.addEventListener('mouseup', onPointerUp);

    window.addEventListener('touchstart', onPointerDown, { passive: true });
    window.addEventListener('touchmove', onPointerMove, { passive: true });
    window.addEventListener('touchend', onPointerUp);
  }

  showToast(message) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    container.appendChild(toast);

    setTimeout(() => {
      toast.remove();
    }, 3500);
  }

  /* ========================================================
     MÓDULO INTERACTIVO: COMPARADOR CARA A CARA (DARK GLASS)
     ======================================================== */
  initCaraACaraComparator() {
    this.btnOpenCompareModal?.addEventListener('click', () => {
      this.openCompareModal();
    });

    this.btnClearCompare?.addEventListener('click', () => {
      this.clearComparedStrains();
    });

    if (this.compareModal) {
      this.compareModal.addEventListener('click', (e) => {
        const rect = this.compareModal.getBoundingClientRect();
        const isInDialog = (
          rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
          rect.left <= e.clientX && e.clientX <= rect.left + rect.width
        );
        if (!isInDialog) {
          this.closeCompareModal();
        }
      });
    }

    this.updateCompareUI();
  }

  toggleCompareStrain(strainId) {
    if (!strainId) return;
    const index = this.comparedStrains.indexOf(strainId);

    if (index > -1) {
      this.comparedStrains.splice(index, 1);
      this.showToast('⚖️ Cepa removida del comparador.');
    } else {
      if (this.comparedStrains.length >= 3) {
        this.showToast('⚠️ Máximo 3 cepas simultáneas. Deselecciona una para añadir otra.');
        return;
      }
      this.comparedStrains.push(strainId);
      const strain = STRAINS_DATABASE.find(s => s.id === strainId);
      const name = strain ? strain.name : 'Cepa';
      this.showToast(`⚖️ ${name} añadida al comparador (${this.comparedStrains.length}/3)`);
    }

    try {
      localStorage.setItem('cannacatalog_compared', JSON.stringify(this.comparedStrains));
    } catch (e) {}

    this.updateCompareUI();
    if (this.compareModal && this.compareModal.open) {
      this.renderCompareModal();
    }
  }

  clearComparedStrains() {
    this.comparedStrains = [];
    try {
      localStorage.setItem('cannacatalog_compared', JSON.stringify([]));
    } catch (e) {}
    this.updateCompareUI();
    if (this.compareModal && this.compareModal.open) {
      this.renderCompareModal();
    }
    this.showToast('🗑️ Comparador vaciado.');
  }

  updateCompareUI() {
    const count = (this.comparedStrains || []).length;

    // Actualizar botones de catálogo
    document.querySelectorAll('.btn-compare-toggle').forEach(btn => {
      const id = btn.getAttribute('data-strain-id');
      const active = this.comparedStrains.includes(id);
      if (active) {
        btn.classList.add('active');
        btn.innerHTML = '⚖️ Comparando';
        btn.title = 'Quitar del comparador';
      } else {
        btn.classList.remove('active');
        btn.innerHTML = '⚖️ Comparar';
        btn.title = 'Comparar (hasta 3 cepas)';
      }
    });

    // Actualizar dock flotante
    if (this.compareDock) {
      if (count > 0) {
        this.compareDock.style.display = 'block';
        if (this.compareDockCounter) {
          this.compareDockCounter.textContent = `${count}/3 cepas`;
        }

        if (this.btnOpenCompareModal) {
          this.btnOpenCompareModal.innerHTML = `⚖️ Comparar Cara a Cara (${count}/3)`;
        }

        if (this.compareDockSlots) {
          this.compareDockSlots.innerHTML = this.comparedStrains.map(id => {
            const strain = STRAINS_DATABASE.find(s => s.id === id);
            if (!strain) return '';
            const thumb = strain.image || '';
            return `
              <div class="compare-dock-slot" title="${strain.name} (${strain.bank})">
                ${thumb ? `<img src="${thumb}" alt="${strain.name}" class="compare-dock-thumb" />` : `<span style="font-size:1.1rem;">🌿</span>`}
                <span class="compare-dock-name">${strain.name}</span>
                <button class="compare-dock-remove" onclick="event.stopPropagation(); window.app && window.app.toggleCompareStrain('${strain.id}')" title="Quitar">✕</button>
              </div>
            `;
          }).join('');
        }
      } else {
        this.compareDock.style.display = 'none';
        if (this.btnOpenCompareModal) {
          this.btnOpenCompareModal.innerHTML = `⚖️ Comparar Cara a Cara (0/3)`;
        }
      }
    }
  }

  calculateIndicaSativa(strain) {
    if (!strain) return { indica: 50, sativa: 50, label: '50% Índica / 50% Sativa' };
    const text = `${strain.name} ${strain.genetics || ''} ${strain.aka || ''} ${strain.description || ''}`.toLowerCase();
    
    const mIndica = text.match(/(\d{1,3})\s*%\s*(?:índica|indica)/);
    const mSativa = text.match(/(\d{1,3})\s*%\s*sativa/);

    let indica = 50;
    let sativa = 50;

    if (mIndica) {
      indica = Math.min(100, Math.max(0, parseInt(mIndica[1])));
      sativa = 100 - indica;
    } else if (mSativa) {
      sativa = Math.min(100, Math.max(0, parseInt(mSativa[1])));
      indica = 100 - sativa;
    } else {
      const sp = (strain.species || '').toLowerCase();
      if (sp === 'indica') {
        indica = 80;
        sativa = 20;
      } else if (sp === 'sativa') {
        indica = 20;
        sativa = 80;
      } else {
        indica = 50;
        sativa = 50;
      }
    }

    return {
      indica,
      sativa,
      label: `${indica}% Índica / ${sativa}% Sativa`
    };
  }

  calculateDifficulty(strain) {
    const days = parseInt(strain.floweringDays) || 60;
    const sp = (strain.species || '').toLowerCase();

    if (days <= 56 || sp === 'indica') {
      return { level: 'Baja', label: 'Principiante', badgeClass: 'badge-diff-easy' };
    } else if (days <= 70 || sp.includes('híb') || sp.includes('hib')) {
      return { level: 'Media', label: 'Intermedia', badgeClass: 'badge-diff-med' };
    } else {
      return { level: 'Alta', label: 'Experto', badgeClass: 'badge-diff-hard' };
    }
  }

  openCompareModal() {
    if (!this.comparedStrains || this.comparedStrains.length === 0) {
      this.showToast('Selecciona al menos 1 variedad con el botón ⚖️ Comparar.');
      return;
    }
    this.renderCompareModal();
    if (this.compareModal && typeof this.compareModal.showModal === 'function') {
      if (!this.compareModal.open) this.compareModal.showModal();
    }
  }

  closeCompareModal() {
    if (this.compareModal && this.compareModal.open) {
      this.compareModal.close();
    }
  }

  renderCompareModal() {
    if (!this.compareModalContent) return;

    const strains = (this.comparedStrains || [])
      .map(id => STRAINS_DATABASE.find(s => s.id === id))
      .filter(Boolean);

    const slotsCount = 3;
    const emptySlotsNeeded = slotsCount - strains.length;

    let columnsHTML = strains.map(strain => {
      const ratio = this.calculateIndicaSativa(strain);
      const diff = this.calculateDifficulty(strain);
      const terpeneData = TERPENES_INFO[strain.dominantTerpene];
      const stars = '★'.repeat(Math.round(strain.rating)) + '☆'.repeat(5 - Math.round(strain.rating));
      const floweringWeeks = Math.round((parseInt(strain.floweringDays) || 60) / 7);
      
      const thcVal = parseFloat(strain.thc) || 0;
      const thcPct = Math.min(100, Math.round((thcVal / 35) * 100));

      const cbdVal = parseFloat(strain.cbd) || 0;
      const cbdPct = Math.min(100, Math.max(cbdVal > 0 ? 5 : 0, Math.round((cbdVal / 20) * 100)));

      const subTerpenes = Object.entries(strain.terpenes || {})
        .filter(([k]) => k !== strain.dominantTerpene)
        .slice(0, 2)
        .map(([k, pct]) => `<span style="font-size:0.72rem; color:var(--text-muted);">${TERPENES_INFO[k]?.name || k}: ${pct}%</span>`)
        .join(' · ');

      return `
        <div class="compare-column">
          <!-- Botón quitar de la comparativa -->
          <button class="compare-col-remove-btn" onclick="window.app && window.app.toggleCompareStrain('${strain.id}')" title="Quitar de la comparativa">✕</button>

          <!-- Cabecera de la Cepa -->
          <div class="compare-col-head">
            <div class="compare-col-thumb-wrap" onclick="window.app && window.app.openImageLightbox('${strain.image || ''}', '${strain.name.replace(/'/g, "\\'")}', '${strain.bank.replace(/'/g, "\\'")}')" title="🔍 Ampliar fotografía botánica HD">
              ${strain.image ? `<img src="${strain.image}" alt="${strain.name}" class="compare-col-thumb" onerror="this.style.display='none';" />` : ''}
              <div class="compare-col-thumb-overlay">🔍</div>
            </div>
            <div class="compare-col-info">
              <div class="compare-col-bank">🏛️ ${strain.bank}</div>
              <h3 class="compare-col-name">${strain.name}</h3>
              <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;">
                <span class="badge-species ${strain.species.toLowerCase()}" style="font-size:0.7rem; padding: 2px 8px; border-radius:50px !important;">${strain.species}</span>
                <span style="font-size: 0.74rem; color: #F59E0B; font-weight: 700;">${stars}</span>
              </div>
            </div>
          </div>

          <!-- 1. Cannabinoides (THC & CBD) -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>🧪 Cannabinoides</span>
              <span style="color:#FCD34D;">${thcVal}% THC · ${cbdVal}% CBD</span>
            </div>
            
            <div class="compare-cannabinoid-row">
              <div class="compare-cannabinoid-label">
                <span style="color:#A7F3D0;">🔥 THC (${thcVal}%)</span>
                <span style="color:var(--text-muted); font-size:0.72rem;">Escala 0-35%</span>
              </div>
              <div class="compare-bar-track">
                <div class="compare-bar-fill-thc" style="width: ${thcPct}%;" title="THC: ${thcVal}% (máx 35%)"></div>
              </div>
            </div>

            <div class="compare-cannabinoid-row" style="margin-top:8px;">
              <div class="compare-cannabinoid-label">
                <span style="color:#93C5FD;">💧 CBD (${cbdVal}%)</span>
                <span style="color:var(--text-muted); font-size:0.72rem;">Escala 0-20%</span>
              </div>
              <div class="compare-bar-track">
                <div class="compare-bar-fill-cbd" style="width: ${cbdPct}%;" title="CBD: ${cbdVal}% (máx 20%)"></div>
              </div>
            </div>
          </div>

          <!-- 2. Proporción Índica / Sativa -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>🧬 Proporción Genética</span>
              <span style="font-size:0.74rem; color:#E2E8F0;">${ratio.label}</span>
            </div>
            <div class="compare-species-track">
              <div class="compare-species-indica" style="width: ${ratio.indica}%;" title="${ratio.indica}% Índica"></div>
              <div class="compare-species-sativa" style="width: ${ratio.sativa}%;" title="${ratio.sativa}% Sativa"></div>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:0.7rem; margin-top:5px; color:var(--text-muted); font-weight:600;">
              <span style="color:#C4B5FD;">🟣 Índica (${ratio.indica}%)</span>
              <span style="color:#FCD34D;">🟠 Sativa (${ratio.sativa}%)</span>
            </div>
          </div>

          <!-- 3. Semanas de Floración & Dificultad -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>⏱️ Cultivo & Floración</span>
              <span class="${diff.badgeClass}">${diff.level} (${diff.label})</span>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 6px;">
              <div style="background:rgba(255,255,255,0.03); padding:6px 8px; border-radius:8px !important; text-align:center;">
                <div style="font-size:0.7rem; color:var(--text-muted);">Floración</div>
                <strong style="color:#fff; font-size:0.86rem;">${floweringWeeks} sem</strong>
                <div style="font-size:0.68rem; color:#A7F3D0;">(${strain.floweringDays} días)</div>
              </div>
              <div style="background:rgba(255,255,255,0.03); padding:6px 8px; border-radius:8px !important; text-align:center;">
                <div style="font-size:0.7rem; color:var(--text-muted);">Rendimiento</div>
                <strong style="color:#fff; font-size:0.86rem;">${strain.yieldIndoor} g/m²</strong>
                <div style="font-size:0.68rem; color:#C4B5FD;">${strain.yieldOutdoor} g/pl</div>
              </div>
            </div>
          </div>

          <!-- 4. Perfil de Terpenos & Aromas -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>🌿 Terpenos & Aromas</span>
              <span style="color:${terpeneData?.color || '#10B981'}; font-weight:800;">${terpeneData?.name || strain.dominantTerpene}</span>
            </div>
            <div style="margin-bottom:6px;">
              <span style="font-size:0.75rem; color:#fff; font-weight:600;">Aroma:</span>
              <span style="font-size:0.75rem; color:var(--text-muted); font-style:italic;">${terpeneData?.aroma || 'Perfil botánico complejo'}</span>
            </div>
            ${subTerpenes ? `<div style="margin-bottom:6px;">${subTerpenes}</div>` : ''}
            <div style="display:flex; flex-wrap:wrap; gap:4px; margin-top:6px;">
              ${(strain.flavors || []).map(f => `<span style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); border-radius:50px !important; padding:2px 8px; font-size:0.72rem; color:#fff;">👅 ${f}</span>`).join('')}
            </div>
          </div>

          <!-- 5. Efectos Destacados -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>⚡ Efectos Destacados</span>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:5px;">
              ${(strain.effects || []).map(e => `<span style="background:rgba(16,185,129,0.14); border:1px solid rgba(16,185,129,0.3); border-radius:50px !important; padding:3px 9px; font-size:0.74rem; font-weight:700; color:#6EE7B7;">⚡ ${e}</span>`).join('')}
            </div>
          </div>

          <!-- 6. Linaje Genético -->
          <div class="compare-metric-box" style="margin-top:auto;">
            <div class="compare-metric-title">
              <span>📜 Linaje Genético</span>
              <span style="font-size:0.72rem; color:var(--text-muted);">${strain.origin || 'Origen verificado'}</span>
            </div>
            <p style="font-size:0.78rem; color:#E2E8F0; margin:0 0 6px 0; font-weight:600; line-height:1.4;">
              🧬 ${strain.genetics || strain.aka || 'Selección de élite'}
            </p>
            <button class="btn btn-primary" style="width:100%; padding:6px 12px; font-size:0.78rem; border-radius:8px !important; margin-top:6px;" onclick="document.getElementById('compare-modal').close(); document.dispatchEvent(new CustomEvent('openStrainDetail', { detail: '${strain.id}' }))">
              📋 Ver Ficha Completa
            </button>
          </div>
        </div>
      `;
    }).join('');

    for (let i = 0; i < emptySlotsNeeded; i++) {
      columnsHTML += `
        <div class="compare-empty-col">
          <div class="compare-empty-icon">⚖️</div>
          <h4 style="font-size:1.05rem; font-weight:800; color:#fff; margin:0;">Ranura Disponible</h4>
          <p class="compare-empty-text">Añade otra variedad desde el catálogo para contrastar sus terpenos, cannabinoides y genética frente a frente.</p>
          <button class="btn btn-outline" style="border-radius:10px !important; font-size:0.8rem; padding:8px 16px;" onclick="document.getElementById('compare-modal').close();">
            🔍 Explorar Catálogo
          </button>
        </div>
      `;
    }

    this.compareModalContent.innerHTML = `
      <div class="compare-modal-wrapper">
        <div class="compare-modal-header">
          <div>
            <h2 class="compare-modal-title">
              <span>⚖️</span> Comparador Botánico Cara a Cara
              <span style="font-size:0.8rem; background:rgba(16,185,129,0.2); color:#10B981; border:1px solid rgba(16,185,129,0.4); padding:3px 10px; border-radius:50px !important; font-weight:800;">${strains.length}/3 cepas</span>
            </h2>
            <div class="compare-modal-subtitle">Análisis analítico y organoléptico en columnas paralelas con Dark Glassmorphism</div>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            ${strains.length > 0 ? `<button class="btn btn-outline-stash" style="padding:6px 12px; font-size:0.76rem; border-radius:8px !important;" onclick="window.app && window.app.clearComparedStrains()">🗑️ Limpiar Todo</button>` : ''}
            <button class="close-modal-btn" onclick="document.getElementById('compare-modal').close()" title="Cerrar (ESC)" style="width:34px; height:34px; border-radius:50% !important; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2); color:#fff; cursor:pointer;">✕</button>
          </div>
        </div>

        <div class="compare-grid">
          ${columnsHTML}
        </div>
      </div>
    `;
  }
}

function initCannaApp() {
  if (!window.app) {
    try {
      window.app = new CannaAppMAX();
      console.log('🌿 CannaCatalog MAX iniciado con éxito');
    } catch (e) {
      console.error('❌ Error al iniciar CannaCatalog:', e);
    }
  }
}

if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initCannaApp();
} else {
  document.addEventListener('DOMContentLoaded', initCannaApp);
}


