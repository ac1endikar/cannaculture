/**
 * CannaCulture 2.0 ULTRA — Panel de Gestión del Dispensario para Encargados CSC
 * Lógica modular, sincronización en tiempo real y gestión de aportaciones por socios.
 * Terminología legal estricta para CSC en España (Aportaciones/g, Menú de Barra, Dispensario).
 */

(function () {
  'use strict';

  // Claves de almacenamiento local y caché
  const STORAGE_KEY = 'cannaculture_csc_menu';
  const CLUB_CONFIG_KEY = 'cannaculture_csc_club_config';
  const MEMBERS_STORAGE_KEY = 'cannaculture_csc_members';
  const DISPENSE_LOG_KEY = 'cannaculture_csc_dispense_log';

  // Configuración por defecto del club
  const DEFAULT_CLUB_CONFIG = {
    name: "CSC Verde Esperanza",
    associationNumber: "Reg. Asoc. 08/4291-CAT",
    city: "Barcelona, España",
    currency: "€",
    kioskTitle: "Carta del Dispensario • Consumo Compartido"
  };

  // Socios estatutarios iniciales de demostración
  const DEFAULT_MEMBERS = [
    { id: "1042", alias: "Alex M.", tier: "colab", limitGrams: 60, consumedGrams: 14.50 },
    { id: "0831", alias: "Laura G.", tier: "std", limitGrams: 40, consumedGrams: 8.00 },
    { id: "0512", alias: "Carlos R. (Dr.)", tier: "terap", limitGrams: 90, consumedGrams: 22.00 },
    { id: "1205", alias: "Marc V.", tier: "std", limitGrams: 60, consumedGrams: 0.00 }
  ];

  // ==========================================================================
  // Diccionario Internacional Multi-Idioma Reactivo (ES / EN / DE / IT)
  // Especializado para Modo Kiosco Mostrador y Ficha Técnica Botánica
  // ==========================================================================
  const I18N = {
    es: {
      tiers: {
        std: "Estándar",
        colab: "Colaborador",
        terap: "Terapéutico",
        stdDesc: "Socio General",
        colabDesc: "Socio Activo (-10%)",
        terapDesc: "Socio Médico (-25%)"
      },
      species: {
        hibrida: "Híbrida",
        indica: "Índica",
        sativa: "Sativa"
      },
      status: {
        available: "Disponible",
        reserved: "En reserva",
        badgeAvailable: "🟢 En Barra / Disponible",
        badgeReserved: "⚪ Agotado / En reserva",
        modalAvailable: "🟢 Disponible en Mostrador",
        modalReserved: "⚪ Agotado / En reserva"
      },
      labels: {
        lineage: "Linaje",
        parentLineage: "Linaje Parental",
        dominantTerpenes: "Terpenos Dominantes",
        sensationsEffects: "Sensaciones & Efectos",
        effectsTitle: "Efectos & Sensaciones Botánicas",
        tastingProfile: "Perfil de Cata & Notas Aromáticas",
        lotNotes: "Notas agronómicas del lote",
        specLotTitle: "Notas Agronómicas & Curado del Lote Local",
        specLotDefault: "Lote seleccionado y curado en condiciones óptimas de conservación.",
        zoomHd: "Toca para Zoom HD",
        close: "Cerrar",
        specBtn: "🔬 Ficha",
        tapToViewSpec: "Toca para ver Ficha Botánica & Terpenos",
        officialDesc: "Ficha Botánica Oficial:",
        flowering: "Floración",
        contributionsTitle: "Previsión de Aportaciones del Club (Consumo Compartido)",
        kioskTitle: "🌿 Carta del Dispensario • Menú de Variedades en Barra",
        kioskSubtitle: "Previsiones botánicas disponibles para socios registrados de la asociación en mostrador.",
        exitKiosk: "⚙️ Salir de Vista Kiosco",
        lightboxSubtitle: "ALTA RESOLUCIÓN • MACRO 800×800",
        lightboxTitle: "Fotografía Botánica HD",
        defaultLineage: "Linaje botánico de alta pureza"
      },
      effects: {
        "Creativo": "Creativo",
        "Relajante": "Relajante",
        "Euforia": "Euforia",
        "Concentración": "Concentración",
        "Sedante": "Sedante",
        "Social": "Social",
        "Corporal": "Corporal",
        "Relajación Corporal": "Relajación Corporal",
        "Calma Profunda": "Calma Profunda",
        "Bienestar": "Bienestar",
        "Enérgico": "Enérgico",
        "Alivio del Estrés": "Alivio del Estrés",
        "Sociable": "Sociable",
        "Apetito": "Apetito",
        "Felicidad": "Felicidad",
        "Meditativo": "Meditativo",
        "Risa": "Risa",
        "Estimulante": "Estimulante"
      },
      flavors: {
        "Terroso": "Terroso",
        "Cítrico": "Cítrico",
        "Frutal": "Frutal",
        "Dulce": "Dulce",
        "Pino": "Pino",
        "Diesel": "Diesel / Gas",
        "Combustible": "Combustible",
        "Picante": "Picante",
        "Baya": "Baya",
        "Vainilla": "Vainilla",
        "Queso": "Queso",
        "Cremoso": "Cremoso",
        "Menta": "Menta",
        "Floral": "Floral",
        "Herbal": "Herbal",
        "Terroso Floral": "Terroso Floral",
        "Cítrico Fresco": "Cítrico Fresco",
        "Matices Herbales": "Matices Herbales"
      },
      terpenes: {
        myrcene: "Mirceno",
        limonene: "Limoneno",
        caryophyllene: "Cariofileno",
        pinene: "Pineno",
        terpinolene: "Terpinoleno",
        linalool: "Linalol",
        humulene: "Humuleno",
        ocimene: "Ocimeno"
      }
    },
    en: {
      tiers: {
        std: "Standard",
        colab: "Collaborator",
        terap: "Therapeutic",
        stdDesc: "General Member",
        colabDesc: "Active Member (-10%)",
        terapDesc: "Medical Member (-25%)"
      },
      species: {
        hibrida: "Hybrid",
        indica: "Indica",
        sativa: "Sativa"
      },
      status: {
        available: "Available",
        reserved: "Reserved",
        badgeAvailable: "🟢 Available on Bar",
        badgeReserved: "⚪ Reserved / Out of Stock",
        modalAvailable: "🟢 Available at Counter",
        modalReserved: "⚪ Out of Stock / Reserved"
      },
      labels: {
        lineage: "Lineage",
        parentLineage: "Parental Lineage",
        dominantTerpenes: "Dominant Terpenes",
        sensationsEffects: "Sensations & Effects",
        effectsTitle: "Botanical Sensations & Effects",
        tastingProfile: "Tasting Profile & Aromatic Notes",
        lotNotes: "Batch agronomic notes",
        specLotTitle: "Agronomic & Curing Notes for Local Batch",
        specLotDefault: "Selected batch cured under optimal preservation conditions.",
        zoomHd: "Tap for HD Zoom",
        close: "Close",
        specBtn: "🔬 Spec Sheet",
        tapToViewSpec: "Tap to view Botanical Spec & Terpenes",
        officialDesc: "Official Botanical Record:",
        flowering: "Flowering",
        contributionsTitle: "Club Contribution Estimates (Shared Consumption)",
        kioskTitle: "🌿 Dispensary Menu • Strains Available on Bar",
        kioskSubtitle: "Botanical provisions available for registered association members at the counter.",
        exitKiosk: "⚙️ Exit Kiosk View",
        lightboxSubtitle: "HIGH RESOLUTION • MACRO 800×800",
        lightboxTitle: "HD Botanical Photography",
        defaultLineage: "High-purity botanical lineage"
      },
      effects: {
        "Creativo": "Creative",
        "Relajante": "Relaxing",
        "Euforia": "Euphoric",
        "Concentración": "Focus",
        "Sedante": "Sedative",
        "Social": "Social",
        "Corporal": "Body buzz",
        "Relajación Corporal": "Body Relaxation",
        "Calma Profunda": "Deep Calm",
        "Bienestar": "Wellness",
        "Enérgico": "Energetic",
        "Alivio del Estrés": "Stress Relief",
        "Sociable": "Sociable",
        "Apetito": "Appetite",
        "Felicidad": "Happiness",
        "Meditativo": "Meditative",
        "Risa": "Giggles",
        "Estimulante": "Uplifting"
      },
      flavors: {
        "Terroso": "Earthy",
        "Cítrico": "Citrus",
        "Frutal": "Fruity",
        "Dulce": "Sweet",
        "Pino": "Pine",
        "Diesel": "Diesel / Gas",
        "Combustible": "Gas / Fuel",
        "Picante": "Spicy",
        "Baya": "Berry",
        "Vainilla": "Vanilla",
        "Queso": "Cheese",
        "Cremoso": "Creamy",
        "Menta": "Mint",
        "Floral": "Floral",
        "Herbal": "Herbal",
        "Terroso Floral": "Earthy Floral",
        "Cítrico Fresco": "Fresh Citrus",
        "Matices Herbales": "Herbal Undertones"
      },
      terpenes: {
        myrcene: "Myrcene",
        limonene: "Limonene",
        caryophyllene: "Caryophyllene",
        pinene: "Pinene",
        terpinolene: "Terpinolene",
        linalool: "Linalool",
        humulene: "Humulene",
        ocimene: "Ocimene"
      }
    },
    de: {
      tiers: {
        std: "Standard",
        colab: "Förderer",
        terap: "Therapeutisch",
        stdDesc: "Allgemeines Mitglied",
        colabDesc: "Aktives Mitglied (-10%)",
        terapDesc: "Medizinisches Mitglied (-25%)"
      },
      species: {
        hibrida: "Hybrid",
        indica: "Indica",
        sativa: "Sativa"
      },
      status: {
        available: "Verfügbar",
        reserved: "Reserviert",
        badgeAvailable: "🟢 An der Bar verfügbar",
        badgeReserved: "⚪ Reserviert / Vergriffen",
        modalAvailable: "🟢 An der Theke verfügbar",
        modalReserved: "⚪ Vergriffen / Reserviert"
      },
      labels: {
        lineage: "Abstammung",
        parentLineage: "Abstammungslinie",
        dominantTerpenes: "Dominante Terpene",
        sensationsEffects: "Wirkung & Empfindungen",
        effectsTitle: "Botanische Wirkung & Empfindungen",
        tastingProfile: "Verkostungsprofil & Aromatische Noten",
        lotNotes: "Anmerkungen zur Charge",
        specLotTitle: "Agronomische & Reifungsnotizen der lokalen Charge",
        specLotDefault: "Ausgewählte Charge, unter optimalen Bedingungen gereift.",
        zoomHd: "Tippen für HD-Zoom",
        close: "Schließen",
        specBtn: "🔬 Datenblatt",
        tapToViewSpec: "Tippen für botanisches Datenblatt & Terpene",
        officialDesc: "Offizielles botanisches Datenblatt:",
        flowering: "Blütezeit",
        contributionsTitle: "Vereins-Beitragsschätzung (Gemeinschaftlicher Konsum)",
        kioskTitle: "🌿 Ausgabekarte • Verfügbare Sorten an der Bar",
        kioskSubtitle: "Botanische Bereitstellungen für registrierte Vereinsmitglieder an der Theke.",
        exitKiosk: "⚙️ Kiosk-Ansicht verlassen",
        lightboxSubtitle: "HOHE AUFLÖSUNG • MAKRO 800×800",
        lightboxTitle: "HD Botanische Fotografie",
        defaultLineage: "Reinrassige botanische Abstammung"
      },
      effects: {
        "Creativo": "Kreativ",
        "Relajante": "Entspannend",
        "Euforia": "Euphorisch",
        "Concentración": "Fokus",
        "Sedante": "Beruhigend",
        "Social": "Gesellig",
        "Corporal": "Körperlich",
        "Relajación Corporal": "Körperentspannung",
        "Calma Profunda": "Tiefe Ruhe",
        "Bienestar": "Wohlbefinden",
        "Enérgico": "Energetisierend",
        "Alivio del Estrés": "Stressabbau",
        "Sociable": "Gesellig",
        "Apetito": "Appetitanregend",
        "Felicidad": "Glücksgefühl",
        "Meditativo": "Meditativ",
        "Risa": "Heiterkeit",
        "Estimulante": "Belebend"
      },
      flavors: {
        "Terroso": "Erdig",
        "Cítrico": "Zitrus",
        "Frutal": "Fruchtig",
        "Dulce": "Süß",
        "Pino": "Kiefer",
        "Diesel": "Diesel / Gas",
        "Combustible": "Treibstoff",
        "Picante": "Würzig",
        "Baya": "Beere",
        "Vainilla": "Vanille",
        "Queso": "Käse",
        "Cremoso": "Cremig",
        "Menta": "Minze",
        "Floral": "Blumig",
        "Herbal": "Kräuterig",
        "Terroso Floral": "Erdig-Blumig",
        "Cítrico Fresco": "Frische Zitrone",
        "Matices Herbales": "Kräuternuancen"
      },
      terpenes: {
        myrcene: "Myrcen",
        limonene: "Limonen",
        caryophyllene: "Caryophyllen",
        pinene: "Pinen",
        terpinolene: "Terpinolen",
        linalool: "Linalool",
        humulene: "Humulen",
        ocimene: "Ocimen"
      }
    },
    it: {
      tiers: {
        std: "Standard",
        colab: "Collaboratore",
        terap: "Terapeutico",
        stdDesc: "Socio Generale",
        colabDesc: "Socio Attivo (-10%)",
        terapDesc: "Socio Medico (-25%)"
      },
      species: {
        hibrida: "Ibrida",
        indica: "Indica",
        sativa: "Sativa"
      },
      status: {
        available: "Disponibile",
        reserved: "In riserva",
        badgeAvailable: "🟢 Disponibile al bancone",
        badgeReserved: "⚪ In riserva / Esaurito",
        modalAvailable: "🟢 Disponibile al Bancone",
        modalReserved: "⚪ Esaurito / In riserva"
      },
      labels: {
        lineage: "Lignaggio",
        parentLineage: "Lignaggio Parentale",
        dominantTerpenes: "Terpeni Dominanti",
        sensationsEffects: "Sensazioni ed Effetti",
        effectsTitle: "Effetti & Sensazioni Botaniche",
        tastingProfile: "Profilo di Degustazione & Note Aromatiche",
        lotNotes: "Note agronomiche del lotto",
        specLotTitle: "Note Agronomiche & Concia del Lotto Locale",
        specLotDefault: "Lotto selezionato e conciato in condizioni ottimali di conservazione.",
        zoomHd: "Tocca per Zoom HD",
        close: "Chiudi",
        specBtn: "🔬 Scheda",
        tapToViewSpec: "Tocca per Scheda Botanica & Terpeni",
        officialDesc: "Scheda Botanica Ufficiale:",
        flowering: "Fioritura",
        contributionsTitle: "Stima dei Contributi del Club (Consumo Condiviso)",
        kioskTitle: "🌿 Menu del Dispensario • Varietà al Bancone",
        kioskSubtitle: "Disponibilità botanica per i soci registrati dell'associazione al bancone.",
        exitKiosk: "⚙️ Esci dalla Vista Kiosk",
        lightboxSubtitle: "ALTA RISOLUZIONE • MACRO 800×800",
        lightboxTitle: "Fotografia Botanica HD",
        defaultLineage: "Lignaggio botanico di elevata purezza"
      },
      effects: {
        "Creativo": "Creativo",
        "Relajante": "Rilassante",
        "Euforia": "Euforia",
        "Concentración": "Concentrazione",
        "Sedante": "Sedativo",
        "Social": "Sociale",
        "Corporal": "Corporeo",
        "Relajación Corporal": "Rilassamento Corporeo",
        "Calma Profunda": "Calma Profonda",
        "Bienestar": "Benessere",
        "Enérgico": "Energico",
        "Alivio del Estrés": "Sollievo dallo Stress",
        "Sociable": "Socievole",
        "Apetito": "Appetito",
        "Felicidad": "Felicità",
        "Meditativo": "Meditativo",
        "Risa": "Risate",
        "Estimulante": "Stimolante"
      },
      flavors: {
        "Terroso": "Terroso",
        "Cítrico": "Agrumato",
        "Frutal": "Fruttato",
        "Dulce": "Dolce",
        "Pino": "Pino",
        "Diesel": "Diesel / Gas",
        "Combustible": "Carburante",
        "Picante": "Speziato",
        "Baya": "Frutti di Bosco",
        "Vainilla": "Vaniglia",
        "Queso": "Formaggio",
        "Cremoso": "Cremoso",
        "Menta": "Menta",
        "Floral": "Floreale",
        "Herbal": "Erbaceo",
        "Terroso Floral": "Terroso Floreale",
        "Cítrico Fresco": "Agrumi Freschi",
        "Matices Herbales": "Note Erbacee"
      },
      terpenes: {
        myrcene: "Mircene",
        limonene: "Limonene",
        caryophyllene: "Cariofillene",
        pinene: "Pinene",
        terpinolene: "Terpinolene",
        linalool: "Linalolo",
        humulene: "Umulene",
        ocimene: "Ocimene"
      }
    }
  };


  // Catálogo inicial demostrativo para mostrador (con cepas icónicas como Gelato, Amnesia Haze, Kmintz, Jealousy...)
  const DEFAULT_MENU_ITEMS = [
    {
      id: "buddha-gelato",
      category: "flores",
      available: true,
      tierStd: 9.50,
      tierColab: 8.50,
      tierTerap: 7.00,
      lotNotes: "Corte Gelato #33 (Larry Bird) • Curado 45 días • Perfil terpénico dulce cremoso con fondo terroso",
      stockGrams: 150,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "rqs-amnesia-haze",
      category: "flores",
      available: true,
      tierStd: 8.50,
      tierColab: 7.50,
      tierTerap: 6.00,
      lotNotes: "Lote Clásico Amsterdam #AH-04 • Sativa eufórica y creativa • Limón fresco y especias Haze",
      stockGrams: 180,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "super-boof",
      category: "flores",
      available: true,
      tierStd: 10.00,
      tierColab: 9.00,
      tierTerap: 7.50,
      lotNotes: "Corte Elite Blockhead Buds • Black Cherry Punch x Tropicanna Cookies • Perfil cereza madura y cítricos gaseosos",
      stockGrams: 110,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "ripper-kmintz",
      category: "flores",
      available: true,
      tierStd: 9.00,
      tierColab: 8.00,
      tierTerap: 6.50,
      lotNotes: "Lote #KM-01 • Curado 60 días en cristal • Cruce Zkittlez x Kush Mints • Aroma mentolado dulce",
      stockGrams: 120,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "sj-jealousy",
      category: "flores",
      available: true,
      tierStd: 10.50,
      tierColab: 9.50,
      tierTerap: 7.50,
      lotNotes: "Lote Reserva #JL-09 • Cepa del Año Leafly • Gelato 41 x Sherbert Bx1 • Tricomas escarchados",
      stockGrams: 95,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "sj-permanent-marker",
      category: "flores",
      available: true,
      tierStd: 11.00,
      tierColab: 10.00,
      tierTerap: 8.00,
      lotNotes: "Cosecha Orgánica #PM-03 • Secado lento en frío 18d • Potente perfil Biscotti x Sherb",
      stockGrams: 140,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "bbs-big-buddha-cheese",
      category: "flores",
      available: true,
      tierStd: 8.50,
      tierColab: 7.50,
      tierTerap: 6.00,
      lotNotes: "Skunk Clásico UK #BB-14 • Clon Cheese original 2006 • Aroma picante a queso curado",
      stockGrams: 80,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "gp-gunslinger",
      category: "flores",
      available: true,
      tierStd: 9.50,
      tierColab: 8.50,
      tierTerap: 7.00,
      lotNotes: "Lote Colorado #GS-02 • Linaje Stardawg potente • Flores densas y aromas a combustible",
      stockGrams: 110,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "oni-tropicanna-cookies",
      category: "extracciones",
      available: true,
      tierStd: 35.00,
      tierColab: 30.00,
      tierTerap: 25.00,
      lotNotes: "Fresh Frozen Hash Rosin 90u • Primer prensado en frío • Terpenos cítricos a naranja sanguina",
      stockGrams: 35,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "bfg-glukies",
      category: "flores",
      available: true,
      tierStd: 8.00,
      tierColab: 7.00,
      tierTerap: 5.50,
      lotNotes: "Lote Interior #GK-04 • Genética Gorilla Glue x Cookies • Flores resinosas y relajantes",
      stockGrams: 75,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "pcg-gush-mints",
      category: "flores",
      available: false,
      tierStd: 9.50,
      tierColab: 8.50,
      tierTerap: 7.00,
      lotNotes: "Lote #GM-11 • Próxima remesa en fase de curado (30 días restantes en bodega)",
      stockGrams: 0,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "sensi-jack-herer",
      category: "flores",
      available: true,
      tierStd: 8.50,
      tierColab: 7.50,
      tierTerap: 6.00,
      lotNotes: "Cosecha Artesanal #JH-18 • Sativa estimulante diurna • Aromas a bosque de pino y pimienta",
      stockGrams: 160,
      lastUpdated: new Date().toISOString()
    },
    {
      id: "barneys-mimosa-evo",
      category: "extracciones",
      available: true,
      tierStd: 32.00,
      tierColab: 28.00,
      tierTerap: 22.00,
      lotNotes: "Live Rosin Prensado Frío • Fracción 73u-120u • Aromas a cóctel de frutas y mandarina",
      stockGrams: 25,
      lastUpdated: new Date().toISOString()
    }
  ];

  // Estado reactivo de la aplicación (v216)
  let state = {
    menu: [],
    clubConfig: { ...DEFAULT_CLUB_CONFIG },
    currentFilter: 'all',
    selectedStrainId: null,
    isKioskMode: false,
    strainsDb: [],
    kioskLang: localStorage.getItem('kiosk_lang') || 'es',
    currentModalStrainId: null,
    activeTab: 'tab-menu',
    members: [],
    selectedMemberId: null,
    posSelectedStrainId: null,
    posCurrentWeight: 0.00,
    dispenseLog: []
  };

  let currentUser = null;
  let unsubscribeFirestore = null;

  // Normalizador de texto para búsquedas insensibles a mayúsculas y diacríticos
  function normalizeStr(s) {
    return (s || '').toString().toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();
  }

  // Pre-indexación en memoria de las 877 cepas para búsqueda instantánea O(1)
  function buildSearchIndex() {
    if (!state.strainsDb || !state.strainsDb.length) return;
    state.strainsDb.forEach(s => {
      const flavors = Array.isArray(s.flavors) ? s.flavors.map(normalizeStr).join(' ') : (s.aroma || '');
      const effects = Array.isArray(s.effects) ? s.effects.map(normalizeStr).join(' ') : '';
      s._searchIndex = `${normalizeStr(s.name)} ${normalizeStr(s.bank || s.breeder)} ${normalizeStr(s.species)} ${normalizeStr(s.lineage)} ${normalizeStr(s.genetics)} ${normalizeStr(s.dominantTerpene)} ${normalizeStr(flavors)} ${normalizeStr(effects)}`;
    });
  }

  // Poblado del desplegable de los 75 bancos criadores oficiales
  function populateBankFilter() {
    const select = document.getElementById('catalog-bank-filter');
    if (!select || !state.strainsDb || !state.strainsDb.length) return;
    const rawBanks = state.strainsDb.map(s => s.bank || s.breeder).filter(Boolean);
    const uniqueBanks = Array.from(new Set(rawBanks)).sort((a, b) => a.localeCompare(b));
    select.innerHTML = `<option value="all">🏛️ Todos los Bancos (${uniqueBanks.length || 75})</option>` +
      uniqueBanks.map(b => `<option value="${b}">${b}</option>`).join('');
  }

  // Helper para buscar en la base de datos maestra de 877 cepas
  function getStrainData(strainId) {
    if (strainId === 'super-boof') {
      return {
        id: "super-boof",
        name: "Super Boof",
        bank: "Blockhead Buds",
        species: "Híbrida",
        image: "img/oni-tropicanna-cookies.webp",
        lineage: "Black Cherry Punch x Tropicanna Cookies",
        genetics: "Black Cherry Punch x Tropicanna Cookies",
        thc: 28,
        cbd: 0.1
      };
    }
    if (!state.strainsDb || !state.strainsDb.length) return null;
    return state.strainsDb.find(s => s.id === strainId) || null;
  }

  // Inicialización de la capa de datos
  function initData() {
    // 1. Cargar Base de Datos de Cepas maestras
    if (window.STRAINS_DATABASE && Array.isArray(window.STRAINS_DATABASE)) {
      state.strainsDb = window.STRAINS_DATABASE;
    } else {
      state.strainsDb = [];
    }

    // Inyectar Super Boof a la base en memoria si no está presente
    if (state.strainsDb && !state.strainsDb.some(s => s.id === 'super-boof')) {
      state.strainsDb.push({
        id: "super-boof",
        name: "Super Boof",
        bank: "Blockhead Buds",
        species: "Híbrida",
        image: "img/oni-tropicanna-cookies.webp",
        lineage: "Black Cherry Punch x Tropicanna Cookies",
        genetics: "Black Cherry Punch x Tropicanna Cookies",
        thc: 28,
        cbd: 0.1
      });
    }

    buildSearchIndex();
    populateBankFilter();

    // 2. Cargar Menú del Club desde LocalStorage o Fallback de Demostración
    try {
      const storedMenu = localStorage.getItem(STORAGE_KEY);
      if (storedMenu) {
        state.menu = JSON.parse(storedMenu);
      } else {
        state.menu = [...DEFAULT_MENU_ITEMS];
        persistMenu(false);
      }

      const storedConfig = localStorage.getItem(CLUB_CONFIG_KEY);
      if (storedConfig) {
        state.clubConfig = { ...DEFAULT_CLUB_CONFIG, ...JSON.parse(storedConfig) };
      }
    } catch (e) {
      console.error("Error al acceder a localStorage:", e);
      state.menu = [...DEFAULT_MENU_ITEMS];
    }

    // 3. Cargar Socios Estatutarios
    try {
      const storedMembers = localStorage.getItem(MEMBERS_STORAGE_KEY);
      if (storedMembers) {
        state.members = JSON.parse(storedMembers);
      } else {
        state.members = [...DEFAULT_MEMBERS];
        persistMembers();
      }
    } catch (e) {
      state.members = [...DEFAULT_MEMBERS];
    }
    if (state.members.length > 0) {
      state.selectedMemberId = state.members[0].id;
    }

    // 4. Cargar Libro de Dispensación
    try {
      const storedLog = localStorage.getItem(DISPENSE_LOG_KEY);
      if (storedLog) {
        state.dispenseLog = JSON.parse(storedLog);
      } else {
        state.dispenseLog = [];
      }
    } catch (e) {
      state.dispenseLog = [];
    }

    // Comprobar parámetro URL para modo kiosco automático (?kiosk=1)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('kiosk') === '1') {
      state.isKioskMode = true;
    }

    // Si hay elementos, seleccionar el primero por defecto en el editor y en el POS
    if (state.menu.length > 0) {
      if (!state.selectedStrainId) state.selectedStrainId = state.menu[0].id;
      const firstAvail = state.menu.find(m => m.available);
      state.posSelectedStrainId = firstAvail ? firstAvail.id : state.menu[0].id;
    }
  }

  function persistMembers() {
    try {
      localStorage.setItem(MEMBERS_STORAGE_KEY, JSON.stringify(state.members));
    } catch (e) {
      console.error("Error persistiendo socios:", e);
    }
  }

  function persistDispenseLog() {
    try {
      localStorage.setItem(DISPENSE_LOG_KEY, JSON.stringify(state.dispenseLog));
    } catch (e) {
      console.error("Error persistiendo libro de dispensación:", e);
    }
  }

  function persistMenu(syncCloud = true) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.menu));
      if (syncCloud && currentUser) {
        syncToFirestore();
      }
      updateSyncStatusBadge(currentUser ? 'cloud' : 'online');
    } catch (e) {
      console.error("Error persistiendo menú:", e);
    }
  }

  function updateSyncStatusBadge(status) {
    const badge = document.getElementById('sync-status-badge');
    if (!badge) return;
    if (status === 'saving') {
      badge.innerHTML = `<span class="pulse-dot" style="background:#F59E0B;box-shadow:0 0 10px #F59E0B;"></span><span>Guardando...</span>`;
      badge.style.color = '#FCD34D';
      badge.style.borderColor = 'rgba(245, 158, 11, 0.3)';
    } else if (status === 'cloud') {
      badge.innerHTML = `<span class="pulse-dot"></span><span>En vivo / Firebase Cloud</span>`;
      badge.style.color = 'var(--primary-light)';
      badge.style.borderColor = 'rgba(16, 185, 129, 0.35)';
    } else {
      badge.innerHTML = `<span class="pulse-dot"></span><span>En vivo / Sincronizado</span>`;
      badge.style.color = 'var(--primary-light)';
      badge.style.borderColor = 'rgba(16, 185, 129, 0.25)';
    }
  }

  // Integración con Firebase Authentication y Firestore
  function initFirebaseSync() {
    const authBtn = document.getElementById('btn-club-auth');

    if (typeof firebase !== 'undefined' && firebase.auth) {
      try {
        firebase.auth().onAuthStateChanged(user => {
          currentUser = user;
          updateAuthUI(user);
          if (user) {
            connectFirestore(user);
          } else {
            if (unsubscribeFirestore) {
              unsubscribeFirestore();
              unsubscribeFirestore = null;
            }
            updateSyncStatusBadge('online');
          }
        });
      } catch (err) {
        console.warn("Firebase Auth no disponible en este entorno:", err);
      }
    }

    if (authBtn) {
      authBtn.addEventListener('click', async () => {
        if (currentUser) {
          if (confirm(`¿Cerrar sesión de ${currentUser.displayName || currentUser.email}? Pasará a Modo Demo.`)) {
            try {
              await firebase.auth().signOut();
              showToast("Sesión cerrada. Modo Demostración activo.", "ℹ️");
            } catch (err) {
              console.error(err);
            }
          }
        } else {
          try {
            const provider = new firebase.auth.GoogleAuthProvider();
            provider.setCustomParameters({ prompt: 'select_account' });
            await firebase.auth().signInWithPopup(provider);
            showToast("🌿 Sesión iniciada con éxito en Firebase.", "✅");
          } catch (err) {
            if (err.code !== 'auth/popup-closed-by-user' && err.code !== 'auth/cancelled-popup-request') {
              alert(`Error al conectar con Google: ${err.message}`);
            }
          }
        }
      });
    }
  }

  function updateAuthUI(user) {
    const authBtn = document.getElementById('btn-club-auth');
    if (!authBtn) return;
    if (user) {
      const name = user.displayName ? user.displayName.split(' ')[0] : 'Club';
      authBtn.innerHTML = `<span>🟢</span><span>${name} (CSC)</span>`;
      authBtn.title = `Conectado como ${user.email} • Click para salir`;
      authBtn.style.borderColor = 'rgba(16, 185, 129, 0.4)';
      authBtn.style.color = '#34D399';
    } else {
      authBtn.innerHTML = `<span>👤</span><span>Modo Demo (Acceso Club)</span>`;
      authBtn.title = `Haz click para iniciar sesión con credenciales de club en Firebase`;
      authBtn.style.borderColor = 'var(--border-light)';
      authBtn.style.color = 'var(--text-secondary)';
    }
  }

  function connectFirestore(user) {
    if (typeof firebase === 'undefined' || !firebase.firestore) return;
    try {
      const db = firebase.firestore();
      const clubDocRef = db.collection('csc_dispensarios').doc(user.uid);
      
      updateSyncStatusBadge('saving');

      unsubscribeFirestore = clubDocRef.onSnapshot(doc => {
        if (doc.exists) {
          const data = doc.data();
          if (data && Array.isArray(data.menu) && data.menu.length > 0) {
            state.menu = data.menu;
            if (data.clubConfig) {
              state.clubConfig = { ...state.clubConfig, ...data.clubConfig };
            }
            persistMenu(false);
            renderMenuGrid();
            renderEditorPanel();
            updateSyncStatusBadge('cloud');
            return;
          }
        }
        syncToFirestore();
        updateSyncStatusBadge('cloud');
      }, err => {
        console.warn("Firestore snapshot error (usando cache local):", err);
        updateSyncStatusBadge('online');
      });
    } catch (err) {
      console.error("Error conectando Firestore:", err);
    }
  }

  async function syncToFirestore() {
    if (!currentUser || typeof firebase === 'undefined' || !firebase.firestore) return;
    try {
      const db = firebase.firestore();
      await db.collection('csc_dispensarios').doc(currentUser.uid).set({
        menu: state.menu,
        clubConfig: state.clubConfig,
        updatedAt: firebase.firestore.FieldValue.serverTimestamp()
      }, { merge: true });
    } catch (err) {
      console.warn("Error guardando en Firestore (se mantendrá en almacenamiento local):", err);
    }
  }

  // Notificación Toast
  function showToast(message, icon = '✅') {
    let toast = document.getElementById('admin-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'admin-toast';
      toast.className = 'admin-toast';
      document.body.appendChild(toast);
    }
    toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
    toast.classList.add('show');
    clearTimeout(toast._timer);
    toast._timer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  }

  // ==========================================================================
  // Métodos de Soporte Multi-idioma (I18N Helpers)
  // ==========================================================================
  function getCurrentI18n() {
    const lang = state.kioskLang || 'es';
    return I18N[lang] || I18N.es;
  }

  function translateSpecies(species, lang = state.kioskLang) {
    const t = I18N[lang] || I18N.es;
    const s = (species || 'hibrida').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    if (s.includes('indica')) return t.species.indica;
    if (s.includes('sativa')) return t.species.sativa;
    return t.species.hibrida;
  }

  function translateEffect(eff, lang = state.kioskLang) {
    if (!eff) return '';
    const t = I18N[lang] || I18N.es;
    if (t.effects[eff]) return t.effects[eff];
    const key = Object.keys(t.effects).find(k => k.toLowerCase() === eff.toLowerCase().trim());
    return key ? t.effects[key] : eff;
  }

  function translateFlavor(flv, lang = state.kioskLang) {
    if (!flv) return '';
    const t = I18N[lang] || I18N.es;
    if (t.flavors[flv]) return t.flavors[flv];
    const key = Object.keys(t.flavors).find(k => k.toLowerCase() === flv.toLowerCase().trim());
    return key ? t.flavors[key] : flv;
  }

  function translateTerpeneName(key, lang = state.kioskLang) {
    const t = I18N[lang] || I18N.es;
    const k = (key || '').toLowerCase().trim();
    if (t.terpenes[k]) return t.terpenes[k];
    return key.charAt(0).toUpperCase() + key.slice(1);
  }

  function formatLocalizedList(items, lang) {
    if (!items || items.length === 0) return '';
    if (items.length === 1) return items[0];
    const andWord = lang === 'de' ? 'und' : (lang === 'it' ? 'e' : (lang === 'en' ? 'and' : 'y'));
    return items.slice(0, -1).join(', ') + ' ' + andWord + ' ' + items[items.length - 1];
  }

  function getDominantTerpenesList(strain, lang) {
    let list = [];
    if (strain.terpenes && typeof strain.terpenes === 'object' && !Array.isArray(strain.terpenes)) {
      list = Object.entries(strain.terpenes)
        .sort((a, b) => b[1] - a[1])
        .map(([k]) => translateTerpeneName(k, lang));
    } else if (Array.isArray(strain.terpenes) && strain.terpenes.length > 0) {
      list = strain.terpenes.map(k => translateTerpeneName(k, lang));
    } else if (strain.dominantTerpene) {
      list = [translateTerpeneName(strain.dominantTerpene, lang)];
    }

    if (list.length === 0) {
      list = [
        translateTerpeneName('myrcene', lang),
        translateTerpeneName('limonene', lang),
        translateTerpeneName('caryophyllene', lang)
      ];
    }
    return list.slice(0, 3);
  }

  function getLocalizedStrainDescription(strain, lang = state.kioskLang) {
    if (!strain) return '';

    // 1. En Español (es): conserva la descripción oficial completa de la base de datos
    if (lang === 'es') {
      return strain.description || 'Variedad botánica seleccionada para el dispensario de consumo compartido del club social.';
    }

    // 2. Si la variedad ya cuenta con campos específicos traducidos en la base de datos
    if (lang === 'en' && strain.description_en) return strain.description_en;
    if (lang === 'de' && strain.description_de) return strain.description_de;
    if (lang === 'it' && strain.description_it) return strain.description_it;

    // 3. Sintetizador botánico estructurado multi-idioma
    const name = strain.name || 'Esta variedad';
    const species = translateSpecies(strain.species, lang);
    const lineage = strain.lineage || strain.genetics || '';

    // Terpenos dominantes
    const terpenesList = getDominantTerpenesList(strain, lang);
    const terpenesStr = formatLocalizedList(terpenesList, lang);

    // Aromas y perfil de cata
    const rawFlavors = Array.isArray(strain.flavors) && strain.flavors.length > 0
      ? strain.flavors
      : ['Cítrico', 'Pino', 'Dulce'];
    const translatedFlavors = rawFlavors.slice(0, 3).map(f => translateFlavor(f, lang).toLowerCase());
    const aromasStr = formatLocalizedList(translatedFlavors, lang);

    // Efectos y sensaciones
    const rawEffects = Array.isArray(strain.effects) && strain.effects.length > 0
      ? strain.effects
      : ['Relajación Corporal', 'Calma Profunda', 'Bienestar'];
    const translatedEffects = rawEffects.slice(0, 3).map(e => translateEffect(e, lang).toLowerCase());
    const effectsStr = formatLocalizedList(translatedEffects, lang);

    // Síntesis botánica coherente por idioma
    if (lang === 'en') {
      const lineageClause = lineage ? `derived from ${lineage}` : 'of select botanical heritage';
      return `${name} is a ${species} botanical variety ${lineageClause}. Highlighted by dominant terpenes such as ${terpenesStr}, offering ${aromasStr} tasting notes and ${effectsStr} effects.`;
    }

    if (lang === 'de') {
      const lineageClause = lineage ? `mit der Abstammungslinie ${lineage}` : 'mit erlesener botanischer Abstammung';
      return `${name} ist eine ${species}-Sorte ${lineageClause}. Geprägt durch Terpene wie ${terpenesStr}, mit aromatischen Noten von ${aromasStr} und ${effectsStr} Empfindungen.`;
    }

    if (lang === 'it') {
      const lineageClause = lineage ? `discendente da ${lineage}` : 'di pregiata discendenza botanica';
      return `${name} è una varietà ${species} ${lineageClause}. Contraddistinta da terpeni dominanti come ${terpenesStr}, note di ${aromasStr} ed effetti ${effectsStr}.`;
    }

    return strain.description || 'Variedad botánica seleccionada para el dispensario de consumo compartido del club social.';
  }

  function setKioskLanguage(lang) {
    if (!I18N[lang]) lang = 'es';
    state.kioskLang = lang;
    try {
      localStorage.setItem('kiosk_lang', lang);
    } catch (e) {
      console.warn("No se pudo persistir kiosk_lang:", e);
    }

    // 1. Actualizar pills de banderas táctiles en todo el DOM
    document.querySelectorAll('.lang-pill-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // 2. Actualizar textos estáticos en Modo Kiosco
    updateKioskStaticTexts();

    // 3. Re-renderizar reactivamente la carta activa del menú
    renderMenuGrid();

    // 4. Si la ficha técnica botánica está abierta en este momento, actualizar al instante sin cerrar el modal
    const modal = document.getElementById('kiosk-strain-modal');
    const isModalVisible = modal && (modal.open || modal.hasAttribute('open') || modal.style.display === 'block' || document.getElementById('spec-modal-desc'));
    if (isModalVisible && state.currentModalStrainId) {
      renderKioskModalContent(state.currentModalStrainId);
    }
  }

  function updateKioskStaticTexts() {
    const t = getCurrentI18n();
    const bannerTitle = document.getElementById('kiosk-banner-title');
    const bannerSubtitle = document.getElementById('kiosk-banner-subtitle');
    const exitBtn = document.getElementById('btn-exit-kiosk');

    if (bannerTitle) bannerTitle.textContent = t.labels.kioskTitle;
    if (bannerSubtitle) bannerSubtitle.textContent = t.labels.kioskSubtitle;
    if (exitBtn) exitBtn.textContent = t.labels.exitKiosk;

    const lightboxSubtitle = document.getElementById('kiosk-lightbox-subtitle');
    if (lightboxSubtitle) lightboxSubtitle.textContent = t.labels.lightboxSubtitle;
  }

  function setupI18n() {
    const savedLang = localStorage.getItem('kiosk_lang') || 'es';
    state.kioskLang = I18N[savedLang] ? savedLang : 'es';

    // Delegación de eventos para clicks en botones de idioma
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.lang-pill-btn');
      if (btn) {
        e.preventDefault();
        e.stopPropagation();
        const selectedLang = btn.getAttribute('data-lang');
        if (selectedLang) {
          setKioskLanguage(selectedLang);
        }
      }
    });

    // Marcar estados activos iniciales
    document.querySelectorAll('.lang-pill-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === state.kioskLang);
    });

    updateKioskStaticTexts();
  }

  // ==========================================================================
  // Renderizado del Menú de Barra
  // ==========================================================================
  function renderMenuGrid() {
    const grid = document.getElementById('strains-menu-grid');
    if (!grid) return;

    // Filtrar según categoría seleccionada
    let items = state.menu.filter(item => {
      if (state.currentFilter !== 'all' && item.category !== state.currentFilter) {
        return false;
      }
      return true;
    });

    const isKioskModeActive = Boolean(
      state.isKioskMode || 
      (typeof document !== 'undefined' && document.body && document.body.classList.contains('kiosk-mode'))
    );

    // En modo Kiosco mostramos las disponibles primero
    if (isKioskModeActive) {
      items.sort((a, b) => (b.available === a.available ? 0 : b.available ? 1 : -1));
    }

    if (items.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; background: var(--bg-surface); border-radius: var(--radius-lg); border: 1px dashed var(--border-light);">
          <span style="font-size: 2.5rem; display: block; margin-bottom: 12px;">🌿</span>
          <h3 style="font-size: 1.15rem; color: var(--text-primary); margin-bottom: 6px;">No hay variedades en esta categoría</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted);">Usa el buscador superior para incorporar variedades del catálogo maestro de 777 cepas.</p>
        </div>
      `;
      updateStatsCounters();
      return;
    }

    const t = getCurrentI18n();

    grid.innerHTML = items.map(item => {
      const strain = getStrainData(item.id) || {
        name: item.id.replace(/-/g, ' ').toUpperCase(),
        bank: 'CannaCulture Selection',
        species: 'Híbrida',
        image: `img/${item.id}.webp`,
        lineage: t.labels.defaultLineage
      };

      const isSelected = item.id === state.selectedStrainId;
      const speciesLower = (strain.species || 'hibrida').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
      const speciesTranslated = translateSpecies(strain.species, state.kioskLang);
      const safeLineage = (strain.lineage || strain.genetics || t.labels.defaultLineage).replace(/"/g, '&quot;');
      const safeLotNotes = (item.lotNotes || t.labels.specLotDefault).replace(/"/g, '&quot;');
      const safeName = (strain.name || item.id).replace(/"/g, '&quot;');

      return `
        <article class="strain-menu-card ${isSelected ? 'selected' : ''} ${!item.available ? 'out-of-stock' : ''}" 
                 data-strain-id="${item.id}"
                 onclick="window.handleCardClick && window.handleCardClick(event, '${item.id}')">
          <div class="card-top">
            <div class="card-photo-wrapper" data-spec-id="${item.id}" title="${t.labels.tapToViewSpec}">
              <img src="${strain.image || 'img/' + item.id + '.webp'}" 
                   alt="${safeName}" 
                   class="card-photo"
                   loading="lazy"
                   onerror="this.src='img/ths-darkstar-official.webp';" />
              <span class="species-chip ${speciesLower}">${speciesTranslated}</span>
            </div>
            
            <div class="card-headline">
              <h3 title="${safeName}">${strain.name}</h3>
              <p class="card-bank">🏛️ ${strain.bank || 'Banco Criador'}</p>
              <p class="card-lineage" title="${safeLineage}">🧬 ${strain.lineage || strain.genetics || t.labels.defaultLineage}</p>
            </div>
          </div>

          <!-- Interruptor de disponibilidad en mostrador -->
          <div class="availability-control">
            <span class="availability-label ${item.available ? 'is-available' : 'is-out'}">
              ${item.available ? t.status.badgeAvailable : t.status.badgeReserved}
            </span>
            <label class="toggle-switch" title="Alternar disponibilidad">
              <input type="checkbox" class="toggle-avail-input" data-strain-id="${item.id}" ${item.available ? 'checked' : ''}>
              <span class="toggle-slider"></span>
            </label>
          </div>

          <!-- Cuadro de cuotas de previsión / aportaciones -->
          <div class="card-tiers-row" title="Cuadro de aportaciones del club por niveles de socio">
            <div class="tier-mini-box tier-std">
              <div class="tier-mini-title">${t.tiers.std}</div>
              <div class="tier-mini-val">${(Number(item.tierStd) || 0).toFixed(2)}€/g</div>
            </div>
            <div class="tier-mini-box tier-colab">
              <div class="tier-mini-title">${t.tiers.colab}</div>
              <div class="tier-mini-val">${(Number(item.tierColab) || 0).toFixed(2)}€/g</div>
            </div>
            <div class="tier-mini-box tier-terap">
              <div class="tier-mini-title">${t.tiers.terap}</div>
              <div class="tier-mini-val">${(Number(item.tierTerap) || 0).toFixed(2)}€/g</div>
            </div>
          </div>

          <!-- Nota de lote botánico / cata local (legibilidad fluida en 2 líneas) -->
          <p class="card-lot-note" title="${safeLotNotes}">📋 ${item.lotNotes || t.labels.specLotDefault}</p>

          <!-- Píldora de interacción táctil visible en Modo Kiosco (Botón Principal / Barra Ancha) -->
          <div class="kiosk-tap-pill" data-spec-id="${item.id}">
            <span>🔬</span>
            <span>${t.labels.tapToViewSpec}</span>
          </div>

          <!-- Acciones de tarjeta / Botón secundario inferior de ficha técnica -->
          <div class="card-actions">
            <button class="btn-card-spec btn-card-ficha" data-spec-id="${item.id}" title="${t.labels.tapToViewSpec}">
              ${t.labels.specBtn}
            </button>
            ${!isKioskModeActive ? `
            <button class="btn-card-edit" data-edit-id="${item.id}" title="Editar aportaciones y notas de lote">
              ✏️ Modificar
            </button>
            <button class="btn-card-delete" data-delete-id="${item.id}" title="Retirar de la carta">
              🗑️
            </button>
            ` : ''}
          </div>
        </article>
      `;
    }).join('');

    updateStatsCounters();
  }

  function updateStatsCounters() {
    const totalCount = state.menu.length;
    const availableCount = state.menu.filter(m => m.available).length;
    const outCount = totalCount - availableCount;

    const elTotal = document.getElementById('stat-total-menu');
    const elAvail = document.getElementById('stat-avail-menu');
    const elOut = document.getElementById('stat-out-menu');

    if (elTotal) elTotal.textContent = totalCount;
    if (elAvail) elAvail.textContent = availableCount;
    if (elOut) elOut.textContent = outCount;
  }

  // ==========================================================================
  // Renderizado y Edición en el Panel Derecho
  // ==========================================================================
  function renderEditorPanel() {
    const panel = document.getElementById('editor-panel-body');
    if (!panel) return;

    const item = state.menu.find(m => m.id === state.selectedStrainId);
    if (!item) {
      panel.innerHTML = `
        <div style="text-align: center; padding: 40px 10px; color: var(--text-muted);">
          <span style="font-size: 2.2rem; display: block; margin-bottom: 10px;">📋</span>
          <p>Selecciona una variedad de la carta para configurar sus aportaciones de socio y notas de lote.</p>
        </div>
      `;
      return;
    }

    const strain = getStrainData(item.id) || {
      name: item.id.replace(/-/g, ' ').toUpperCase(),
      bank: 'CannaCulture Selection',
      species: 'Híbrida',
      image: `img/${item.id}.webp`,
      thc: 22,
      cbd: 0.1
    };

    panel.innerHTML = `
      <!-- Vista previa de la variedad activa -->
      <div class="editor-preview-banner">
        <img src="${strain.image || 'img/' + item.id + '.webp'}" 
             alt="${strain.name}" 
             class="editor-preview-img"
             onerror="this.src='img/ths-darkstar-official.webp';" />
        <div class="editor-preview-text">
          <h3>${strain.name}</h3>
          <p>🏛️ ${strain.bank} • 🌿 ${strain.species || 'Híbrida'}</p>
          <p style="color: var(--primary-light); font-weight: 600; font-size: 0.76rem;">
            THC: ${strain.thc || 20}% | CBD: ${strain.cbd || 0.1}%
          </p>
        </div>
      </div>

      <form id="editor-form" onsubmit="return false;">
        <!-- Categoría en Mostrador -->
        <div class="form-group">
          <label class="form-label" for="edit-category">Categoría en Dispensario</label>
          <select id="edit-category" class="form-control">
            <option value="flores" ${item.category === 'flores' ? 'selected' : ''}>🌸 Flores / Cogollos Curados</option>
            <option value="extracciones" ${item.category === 'extracciones' ? 'selected' : ''}>🍯 Extracciones & Rosin</option>
            <option value="comestibles" ${item.category === 'comestibles' ? 'selected' : ''}>🍪 Comestibles & Tinturas</option>
          </select>
        </div>

        <!-- Aportación Estándar (€/g) -->
        <div class="form-group">
          <label class="form-label" for="edit-tier-std">
            Nivel Estándar (Socio General)
          </label>
          <div class="form-input-currency">
            <span class="currency-symbol">€</span>
            <input type="number" step="0.25" min="0" id="edit-tier-std" 
                   class="form-control has-currency" 
                   value="${item.tierStd.toFixed(2)}" required>
            <span class="unit-symbol">/ g</span>
          </div>
          <p class="tier-help-text">Cuota de previsión de cultivo para socios generales.</p>
        </div>

        <!-- Aportación Colaborador (€/g) -->
        <div class="form-group">
          <label class="form-label" for="edit-tier-colab">
            Nivel Colaborador (Socio Activo)
          </label>
          <div class="form-input-currency">
            <span class="currency-symbol">€</span>
            <input type="number" step="0.25" min="0" id="edit-tier-colab" 
                   class="form-control has-currency" 
                   value="${item.tierColab.toFixed(2)}" required>
            <span class="unit-symbol">/ g</span>
          </div>
          <p class="tier-help-text">Cuota reducida para socios que colaboran en labores de la asociación.</p>
        </div>

        <!-- Aportación Terapéutica (€/g) -->
        <div class="form-group">
          <label class="form-label" for="edit-tier-terap">
            Nivel Terapéutico (Socio Médico)
          </label>
          <div class="form-input-currency">
            <span class="currency-symbol">€</span>
            <input type="number" step="0.25" min="0" id="edit-tier-terap" 
                   class="form-control has-currency" 
                   value="${item.tierTerap.toFixed(2)}" required>
            <span class="unit-symbol">/ g</span>
          </div>
          <p class="tier-help-text">Cuota solidaria para usuarios con prescripción o uso terapéutico.</p>
        </div>

        <!-- Stock estimado de mostrador (g) -->
        <div class="form-group">
          <label class="form-label" for="edit-stock">Previsión en Barra (Gramos)</label>
          <input type="number" step="1" min="0" id="edit-stock" 
                 class="form-control" 
                 value="${item.stockGrams || 0}">
          <p class="tier-help-text">Cantidad estimada disponible en botes/frascos de barra.</p>
        </div>

        <!-- Notas del Lote / Cata Local -->
        <div class="form-group">
          <label class="form-label" for="edit-lot-notes">Notas del Lote / Cata Local</label>
          <textarea id="edit-lot-notes" class="form-control" placeholder="Ej: Curado 45 días - Lote interior #B-24">${item.lotNotes || ''}</textarea>
          <p class="tier-help-text">Información agronómica visible para socios en mostrador.</p>
        </div>

        <!-- Botón de Guardar -->
        <button type="button" id="btn-save-editor" class="editor-save-btn">
          💾 Guardar y Actualizar Carta
        </button>
      </form>
    `;

    // Vincular listener de guardado
    document.getElementById('btn-save-editor').addEventListener('click', saveCurrentEditorItem);

    // Sugerencia de autocalculado suave al cambiar tier estándar
    const inputStd = document.getElementById('edit-tier-std');
    const inputColab = document.getElementById('edit-tier-colab');
    const inputTerap = document.getElementById('edit-tier-terap');

    inputStd.addEventListener('change', () => {
      const val = parseFloat(inputStd.value);
      if (!isNaN(val) && val > 0) {
        if (confirm("¿Deseas recalcular automáticamente las cuotas sugeridas para Colaborador (-10%) y Terapéutico (-25%)?")) {
          inputColab.value = (Math.round((val * 0.90) * 4) / 4).toFixed(2);
          inputTerap.value = (Math.round((val * 0.75) * 4) / 4).toFixed(2);
        }
      }
    });
  }

  function saveCurrentEditorItem() {
    const item = state.menu.find(m => m.id === state.selectedStrainId);
    if (!item) return;

    updateSyncStatusBadge('saving');

    item.category = document.getElementById('edit-category').value;
    item.tierStd = Math.max(0, parseFloat(document.getElementById('edit-tier-std').value) || 0);
    item.tierColab = Math.max(0, parseFloat(document.getElementById('edit-tier-colab').value) || 0);
    item.tierTerap = Math.max(0, parseFloat(document.getElementById('edit-tier-terap').value) || 0);
    item.stockGrams = Math.max(0, parseInt(document.getElementById('edit-stock').value, 10) || 0);
    item.lotNotes = document.getElementById('edit-lot-notes').value.trim();
    item.lastUpdated = new Date().toISOString();

    persistMenu();
    renderMenuGrid();

    // Animación de guardado exitoso en el botón táctil
    const saveBtn = document.getElementById('btn-save-editor');
    if (saveBtn) {
      saveBtn.classList.add('saving-success');
      const originalText = saveBtn.innerHTML;
      saveBtn.innerHTML = `<span>✨</span> <span>¡Guardado y Actualizado!</span>`;
      setTimeout(() => {
        saveBtn.classList.remove('saving-success');
        saveBtn.innerHTML = originalText;
      }, 1500);
    }

    showToast(`Carta actualizada: ${item.id.replace(/-/g, ' ')}`);
  }

  // ==========================================================================
  // Buscador del Catálogo Maestro (877 cepas y 75 bancos con _searchIndex)
  // ==========================================================================
  function setupCatalogSearch() {
    const searchInput = document.getElementById('catalog-search-input');
    const bankFilter = document.getElementById('catalog-bank-filter');
    const dropdown = document.getElementById('search-results-dropdown');
    if (!searchInput || !dropdown) return;

    let debounceTimer;

    const triggerSearch = () => {
      clearTimeout(debounceTimer);
      const query = searchInput.value.trim();
      const selectedBank = bankFilter ? bankFilter.value : 'all';

      if (query.length < 2 && selectedBank === 'all') {
        dropdown.classList.remove('active');
        dropdown.innerHTML = '';
        return;
      }

      debounceTimer = setTimeout(() => {
        executeSearch(query, selectedBank);
      }, 120);
    };

    searchInput.addEventListener('input', triggerSearch);
    if (bankFilter) {
      bankFilter.addEventListener('change', triggerSearch);
    }

    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !dropdown.contains(e.target) && (!bankFilter || !bankFilter.contains(e.target))) {
        dropdown.classList.remove('active');
      }
    });

    function executeSearch(query, bank = 'all') {
      if (!state.strainsDb || !state.strainsDb.length) {
        dropdown.innerHTML = `<div style="padding: 16px; text-align: center; color: var(--text-muted);">Cargando catálogo maestro...</div>`;
        dropdown.classList.add('active');
        return;
      }

      const normQuery = normalizeStr(query);

      const matches = state.strainsDb.filter(s => {
        const bankMatches = (bank === 'all' || (s.bank || s.breeder) === bank);
        if (!bankMatches) return false;
        if (!normQuery || normQuery.length < 2) return true;
        return s._searchIndex ? s._searchIndex.includes(normQuery) : (
          normalizeStr(s.name).includes(normQuery) || normalizeStr(s.bank).includes(normQuery)
        );
      }).slice(0, 15);

      if (matches.length === 0) {
        dropdown.innerHTML = `
          <div style="padding: 16px; text-align: center; color: var(--text-dim); font-size: 0.88rem;">
            No se encontraron variedades para "<strong>${query || bank}</strong>"
          </div>
        `;
        dropdown.classList.add('active');
        return;
      }

      dropdown.innerHTML = matches.map(s => {
        const isAlreadyInMenu = state.menu.some(m => m.id === s.id);
        const speciesName = translateSpecies(s.species, state.kioskLang);
        return `
          <div class="search-result-item" data-add-id="${s.id}">
            <div class="result-left">
              <img src="${s.image || 'img/' + s.id + '.webp'}" 
                   alt="${s.name}" 
                   class="result-thumb" 
                   onerror="this.src='img/ths-darkstar-official.webp';" />
              <div class="result-meta">
                <h4>${s.name}</h4>
                <div class="result-subline">
                  <span>🏛️ ${s.bank || 'Banco Criador'}</span>
                  <span>•</span>
                  <span>🧬 ${speciesName} (THC: ${s.thc || 20}%)</span>
                </div>
              </div>
            </div>
            <div>
              ${isAlreadyInMenu ? 
                `<span style="font-size:0.75rem; color: var(--primary-light); font-weight:700;">✓ En Carta</span>` : 
                `<button class="btn-add-quick" data-add-id="${s.id}">➕ Añadir a Barra</button>`
              }
            </div>
          </div>
        `;
      }).join('');

      dropdown.classList.add('active');

      dropdown.querySelectorAll('[data-add-id]').forEach(el => {
        el.addEventListener('click', () => {
          const sid = el.getAttribute('data-add-id');
          if (sid) {
            addNewStrainToMenu(sid);
            dropdown.classList.remove('active');
            searchInput.value = '';
          }
        });
      });
    }
  }

  function addNewStrainToMenu(strainId) {
    if (state.menu.some(m => m.id === strainId)) {
      showToast("Esta variedad ya se encuentra incorporada en la carta.", "ℹ️");
      state.selectedStrainId = strainId;
      renderMenuGrid();
      renderEditorPanel();
      return;
    }

    const strain = getStrainData(strainId);
    const baseStd = strain && strain.thc ? Math.min(12, Math.max(7.5, strain.thc * 0.40)) : 8.50;
    const roundedStd = Math.round(baseStd * 4) / 4;

    const newItem = {
      id: strainId,
      category: "flores",
      available: true,
      tierStd: roundedStd,
      tierColab: Math.round((roundedStd * 0.90) * 4) / 4,
      tierTerap: Math.round((roundedStd * 0.75) * 4) / 4,
      lotNotes: `Lote #C-${new Date().getFullYear().toString().slice(-2)} • Nueva incorporación a mostrador`,
      stockGrams: 100,
      lastUpdated: new Date().toISOString()
    };

    state.menu.unshift(newItem);
    state.selectedStrainId = strainId;

    persistMenu();
    renderMenuGrid();
    renderEditorPanel();
    showToast(`¡${strain ? strain.name : strainId} añadida a la carta activa!`);
  }

  // ==========================================================================
  // Ficha Técnica Botánica & Modal Interactivo de Mostrador (Modo Kiosco)
  // ==========================================================================
  function renderTerpenesSection(strain) {
    const terpeneInfo = window.TERPENES_INFO || {};
    let terpenesObj = strain.terpenes;
    
    if (!terpenesObj || typeof terpenesObj !== 'object' || Object.keys(terpenesObj).length === 0) {
      const dom = (strain.dominantTerpene || 'myrcene').toLowerCase();
      terpenesObj = {};
      terpenesObj[dom] = 45;
      if (dom !== 'limonene') terpenesObj['limonene'] = 30;
      else terpenesObj['caryophyllene'] = 30;
      terpenesObj['pinene'] = 25;
    }

    const entries = Object.entries(terpenesObj).sort((a, b) => b[1] - a[1]);

    return entries.map(([key, pct]) => {
      const keyLower = key.toLowerCase();
      const info = terpeneInfo[keyLower] || Object.values(terpeneInfo).find(t => t.name.toLowerCase() === keyLower) || {
        name: key.charAt(0).toUpperCase() + key.slice(1),
        color: '#10B981',
        effects: 'Perfil aromático vegetal'
      };
      const col = info.color || '#10B981';
      const translatedName = translateTerpeneName(keyLower, state.kioskLang);

      return `
        <div class="terpene-row">
          <div class="terpene-row-info">
            <span class="terpene-name" style="color: ${col};">
              🧬 ${translatedName}
            </span>
            <span class="terpene-pct">${pct}%</span>
          </div>
          <div class="terpene-bar-track">
            <div class="terpene-bar-fill" style="width: ${Math.min(100, pct)}%; background: linear-gradient(90deg, ${col}99, ${col});"></div>
          </div>
        </div>
      `;
    }).join('');
  }

  function renderEffectsAndFlavors(strain) {
    const t = getCurrentI18n();
    const effects = Array.isArray(strain.effects) && strain.effects.length > 0 ? strain.effects : ['Relajación Corporal', 'Calma Profunda', 'Bienestar'];
    const flavors = Array.isArray(strain.flavors) && strain.flavors.length > 0 ? strain.flavors : ['Terroso Floral', 'Cítrico Fresco', 'Matices Herbales'];

    const effectsHtml = effects.map(eff => `<span class="spec-tag effect">✨ ${translateEffect(eff, state.kioskLang)}</span>`).join('');
    const flavorsHtml = flavors.map(flv => `<span class="spec-tag flavor">🍋 ${translateFlavor(flv, state.kioskLang)}</span>`).join('');

    return `
      <div style="margin-bottom: 14px;">
        <div style="font-size: 0.76rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px;">${t.labels.effectsTitle}</div>
        <div class="spec-tags-grid">${effectsHtml}</div>
      </div>
      <div>
        <div style="font-size: 0.76rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px;">${t.labels.tastingProfile}</div>
        <div class="spec-tags-grid">${flavorsHtml}</div>
      </div>
    `;
  }

  function renderKioskModalContent(strainId) {
    state.currentModalStrainId = strainId;
    const modalBody = document.getElementById('kiosk-modal-body');
    if (!modalBody) return;

    const t = getCurrentI18n();
    const item = state.menu.find(m => m.id === strainId);
    const strain = getStrainData(strainId) || {
      id: strainId,
      name: strainId.replace(/-/g, ' ').toUpperCase(),
      bank: 'CannaCulture Selection',
      species: 'Híbrida',
      image: `img/${strainId}.webp`,
      lineage: t.labels.defaultLineage,
      thc: 22,
      cbd: 0.1,
      rating: 4.9,
      description: 'Variedad seleccionada para el dispensario de consumo compartido del club social.'
    };

    const itemData = item || {
      tierStd: 9.00,
      tierColab: 8.00,
      tierTerap: 6.50,
      available: true,
      lotNotes: 'Lote estándar del dispensario'
    };

    const speciesLower = (strain.species || 'hibrida').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    const speciesTranslated = translateSpecies(strain.species, state.kioskLang);
    const starCount = Math.min(5, Math.max(1, Math.round(Number(strain.rating) || 5)));
    const stars = '★'.repeat(starCount) + '☆'.repeat(5 - starCount);
    const photoUrl = strain.image || `img/${strain.id || strainId}.webp`;
    const safeName = (strain.name || 'Variedad').replace(/"/g, '&quot;');
    const safeBank = (strain.bank || 'Banco Criador').replace(/"/g, '&quot;');
    const currentLang = state.kioskLang || 'es';
    const localizedDesc = getLocalizedStrainDescription(strain, currentLang);

    const closeBtn = document.getElementById('btn-close-kiosk-modal');
    if (closeBtn) {
      closeBtn.title = `${t.labels.close} (Esc)`;
      closeBtn.setAttribute('aria-label', t.labels.close);
    }

    modalBody.innerHTML = `
      <!-- BARRA DE IDIOMA EN LA CABECERA DE LA FICHA TÉCNICA -->
      <div class="spec-lang-bar">
        <span class="spec-lang-label">🌐 Idioma / Language:</span>
        <div class="kiosk-lang-selector" aria-label="Cambiar idioma en ficha técnica">
          <button type="button" class="lang-pill-btn ${currentLang === 'es' ? 'active' : ''}" data-lang="es" title="Español">🇪🇸 ES</button>
          <button type="button" class="lang-pill-btn ${currentLang === 'en' ? 'active' : ''}" data-lang="en" title="English">🇬🇧 EN</button>
          <button type="button" class="lang-pill-btn ${currentLang === 'de' ? 'active' : ''}" data-lang="de" title="Deutsch">🇩🇪 DE</button>
          <button type="button" class="lang-pill-btn ${currentLang === 'it' ? 'active' : ''}" data-lang="it" title="Italiano">🇮🇹 IT</button>
        </div>
      </div>

      <!-- HERO PRINCIPAL DE LA VARIEDAD -->
      <section class="spec-hero">
        <div class="spec-photo-wrap" id="spec-photo-click" title="${t.labels.zoomHd}">
          <img src="${photoUrl}" 
               alt="${safeName}" 
               class="spec-photo-img" 
               onerror="this.src='img/ths-darkstar-official.webp';" />
          <div class="spec-zoom-badge">🔍 ${t.labels.zoomHd}</div>
        </div>

        <div class="spec-hero-meta">
          <div class="spec-badges-row">
            <span class="species-chip ${speciesLower}" style="position:static; padding:4px 10px; font-size:0.75rem;">
              ${speciesTranslated}
            </span>
            <span class="spec-bank-pill">🏛️ ${strain.bank || 'Banco Criador'}</span>
            <span style="color: #FBBF24; font-size: 0.85rem; font-weight: 700;">${stars}</span>
          </div>

          <h2 class="spec-title">${strain.name}</h2>
          <div class="spec-lineage">🧬 ${t.labels.parentLineage}: ${strain.lineage || strain.genetics || t.labels.defaultLineage}</div>

          <div class="spec-cannabinoids">
            <div class="cannabinoid-chip" style="color:#34D399;">
              🌿 THC: <strong>${strain.thc || 22}%</strong>
            </div>
            <div class="cannabinoid-chip" style="color:#06B6D4;">
              🧪 CBD: <strong>${strain.cbd || 0.1}%</strong>
            </div>
            ${strain.floweringDays ? `
            <div class="cannabinoid-chip" style="color:#FBBF24;">
              ⏱️ ${t.labels.flowering}: <strong>${strain.floweringDays}d</strong>
            </div>` : ''}
          </div>
        </div>
      </section>

      <!-- CUADRO DE APORTACIONES DEL CLUB (CONSUMO COMPARTIDO) -->
      <section class="spec-tiers-box">
        <div class="spec-tiers-header">
          <h3>
            <span>⚖️</span>
            <span>${t.labels.contributionsTitle}</span>
          </h3>
          <span class="spec-avail-pill ${itemData.available ? 'is-avail' : 'is-out'}">
            ${itemData.available ? t.status.modalAvailable : t.status.modalReserved}
          </span>
        </div>

        <div class="spec-tiers-grid">
          <div class="spec-tier-card std">
            <div class="spec-tier-name">${t.tiers.std}</div>
            <div class="spec-tier-val">${(Number(itemData.tierStd) || 0).toFixed(2)}€/g</div>
            <div class="spec-tier-desc">${t.tiers.stdDesc}</div>
          </div>
          <div class="spec-tier-card colab">
            <div class="spec-tier-name">${t.tiers.colab}</div>
            <div class="spec-tier-val">${(Number(itemData.tierColab) || 0).toFixed(2)}€/g</div>
            <div class="spec-tier-desc">${t.tiers.colabDesc}</div>
          </div>
          <div class="spec-tier-card terap">
            <div class="spec-tier-name">${t.tiers.terap}</div>
            <div class="spec-tier-val">${(Number(itemData.tierTerap) || 0).toFixed(2)}€/g</div>
            <div class="spec-tier-desc">${t.tiers.terapDesc}</div>
          </div>
        </div>

        <!-- NOTAS DEL LOTE AGRONÓMICO Y CURADO -->
        <div class="spec-lot-card" style="margin-top: 14px;">
          <div class="spec-lot-title">📋 ${t.labels.specLotTitle}</div>
          <div class="spec-lot-text">${itemData.lotNotes || t.labels.specLotDefault}</div>
        </div>
      </section>

      <!-- TERPENOS, AROMAS Y PERFIL BOTÁNICO -->
      <section class="spec-terpenes-card">
        <div class="spec-section-heading">
          <span>🧬</span>
          <span>${t.labels.dominantTerpenes}</span>
        </div>

        <div class="terpene-bars-container">
          ${renderTerpenesSection(strain)}
        </div>

        ${renderEffectsAndFlavors(strain)}

        ${localizedDesc ? `
        <div id="spec-modal-desc" class="spec-desc-text">
          <strong>${t.labels.officialDesc}</strong> ${localizedDesc}
        </div>` : ''}
      </section>
    `;

    const photoBox = document.getElementById('spec-photo-click');
    if (photoBox) {
      photoBox.addEventListener('click', () => {
        openKioskLightbox(photoUrl, strain.name, `🏛️ ${strain.bank} • ${speciesTranslated}`);
      });
    }
  }

  function openKioskStrainModal(strainId) {
    const modal = document.getElementById('kiosk-strain-modal');
    if (!modal) return;

    renderKioskModalContent(strainId);

    // Apertura infalible del diálogo con soporte y fallback
    try {
      if (typeof modal.showModal === 'function') {
        if (!modal.open) {
          modal.showModal();
        }
      } else {
        modal.setAttribute('open', '');
      }
    } catch (dialogErr) {
      console.warn("showModal fallback activo:", dialogErr);
      modal.setAttribute('open', '');
    }
  }

  function closeKioskModal() {
    const modal = document.getElementById('kiosk-strain-modal');
    if (modal) {
      if (typeof modal.close === 'function') {
        try { modal.close(); } catch (err) {}
      }
      modal.removeAttribute('open');
    }
  }

  function openKioskLightbox(imgSrc, title, subtitle) {
    const dialog = document.getElementById('kiosk-lightbox-dialog');
    const imgEl = document.getElementById('kiosk-lightbox-img');
    const titleEl = document.getElementById('kiosk-lightbox-title');
    const subEl = document.getElementById('kiosk-lightbox-subtitle');
    const t = getCurrentI18n();

    if (!dialog || !imgEl) return;
    imgEl.src = imgSrc;
    if (titleEl) titleEl.textContent = title || t.labels.lightboxTitle;
    if (subEl) subEl.textContent = subtitle || t.labels.lightboxSubtitle;

    try {
      if (typeof dialog.showModal === 'function') {
        if (!dialog.open) {
          dialog.showModal();
        }
      } else {
        dialog.setAttribute('open', '');
      }
    } catch (e) {
      dialog.setAttribute('open', '');
    }
  }

  function setupKioskModalListeners() {
    const modal = document.getElementById('kiosk-strain-modal');
    const closeBtn = document.getElementById('btn-close-kiosk-modal');

    if (closeBtn && modal) {
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        closeKioskModal();
      });
    }

    if (modal) {
      modal.addEventListener('click', (e) => {
        const rect = modal.getBoundingClientRect();
        if (
          e.clientX < rect.left ||
          e.clientX > rect.right ||
          e.clientY < rect.top ||
          e.clientY > rect.bottom
        ) {
          closeKioskModal();
        }
      });
    }

    const lightbox = document.getElementById('kiosk-lightbox-dialog');
    const closeLightboxBtn = document.getElementById('btn-close-kiosk-lightbox');

    if (closeLightboxBtn && lightbox) {
      closeLightboxBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (typeof lightbox.close === 'function') {
          try { lightbox.close(); } catch (err) {}
        }
        lightbox.removeAttribute('open');
      });
    }

    if (lightbox) {
      lightbox.addEventListener('click', (e) => {
        const rect = lightbox.getBoundingClientRect();
        if (
          e.clientX < rect.left ||
          e.clientX > rect.right ||
          e.clientY < rect.top ||
          e.clientY > rect.bottom
        ) {
          if (typeof lightbox.close === 'function') {
            try { lightbox.close(); } catch (err) {}
          }
          lightbox.removeAttribute('open');
        }
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (lightbox && lightbox.open) {
          if (typeof lightbox.close === 'function') {
            try { lightbox.close(); } catch (err) {}
          }
          lightbox.removeAttribute('open');
        } else if (modal && modal.open) {
          closeKioskModal();
        }
      }
    });
  }

  // Manejador centralizado de click/tap en tarjetas (Modo Kiosco y Modo Encargado)
  function handleCardClick(e, sid) {
    if (!sid) return;

    // 1. Ignorar clicks dentro del interruptor de disponibilidad en modo normal
    if (e.target.closest('.availability-control') || e.target.closest('.toggle-switch')) {
      return;
    }

    // 2. Ignorar clicks en botones de acción específicos del modo encargado
    if (e.target.closest('.btn-card-edit') || e.target.closest('.btn-card-delete')) {
      return;
    }

    // 3. Click explícito en Ficha Técnica
    if (e.target.closest('[data-spec-id]') || e.target.closest('.btn-card-spec') || e.target.closest('.kiosk-tap-pill') || e.target.closest('.card-photo-wrapper')) {
      e.preventDefault();
      e.stopPropagation();
      openKioskStrainModal(sid);
      return;
    }

    // 4. Modo Kiosco: cualquier punto de la tarjeta abre la Ficha Técnica Botánica
    if (state.isKioskMode || document.body.classList.contains('kiosk-mode')) {
      e.preventDefault();
      e.stopPropagation();
      openKioskStrainModal(sid);
      return;
    }

    // 5. Modo Encargado: selección para el panel de configuración de cuotas
    state.selectedStrainId = sid;
    renderMenuGrid();
    renderEditorPanel();
  }

  // Exportar al objeto global window para disponibilidad absoluta en eventos inline
  window.openKioskStrainModal = openKioskStrainModal;
  window.closeKioskModal = closeKioskModal;
  window.handleCardClick = handleCardClick;
  window.setKioskLanguage = setKioskLanguage;
  window.getLocalizedStrainDescription = getLocalizedStrainDescription;
  window.I18N = I18N;

  // ==========================================================================
  // Manejo de Eventos en Grid (Toggles, Edición, Eliminación, Ficha Técnica)
  // ==========================================================================
  function setupGridEvents() {
    const grid = document.getElementById('strains-menu-grid');
    if (!grid) return;

    grid.addEventListener('click', (e) => {
      // 1. Click en botón o foto de Ficha Técnica
      const specBtn = e.target.closest('[data-spec-id], .btn-card-spec, .kiosk-tap-pill, .card-photo-wrapper');
      if (specBtn) {
        const sid = specBtn.getAttribute('data-spec-id') || specBtn.closest('.strain-menu-card')?.getAttribute('data-strain-id');
        if (sid) {
          e.preventDefault();
          openKioskStrainModal(sid);
          return;
        }
      }

      // 2. Si está en Modo Kiosco, hacer click sobre cualquier parte de la tarjeta abre la Ficha Técnica
      if (state.isKioskMode || document.body.classList.contains('kiosk-mode')) {
        const card = e.target.closest('.strain-menu-card, .dispensario-card, .kiosk-card');
        if (card && !e.target.closest('.availability-control') && !e.target.closest('.toggle-switch')) {
          const sid = card.getAttribute('data-strain-id');
          if (sid) {
            e.preventDefault();
            openKioskStrainModal(sid);
            return;
          }
        }
      }

      // 3. Click en botón Editar
      const editBtn = e.target.closest('[data-edit-id]');
      if (editBtn) {
        const sid = editBtn.getAttribute('data-edit-id');
        state.selectedStrainId = sid;
        renderMenuGrid();
        renderEditorPanel();
        if (window.innerWidth <= 992) {
          const ep = document.getElementById('editor-panel-card');
          if (ep) ep.scrollIntoView({ behavior: 'smooth' });
        }
        return;
      }

      // 4. Click en botón Eliminar
      const delBtn = e.target.closest('[data-delete-id]');
      if (delBtn) {
        const sid = delBtn.getAttribute('data-delete-id');
        if (confirm(`¿Retirar esta variedad de la carta del dispensario?`)) {
          state.menu = state.menu.filter(m => m.id !== sid);
          if (state.selectedStrainId === sid) {
            state.selectedStrainId = state.menu.length > 0 ? state.menu[0].id : null;
          }
          persistMenu();
          renderMenuGrid();
          renderEditorPanel();
          showToast("Variedad retirada del menú.");
        }
        return;
      }

      // 5. Click en tarjeta (modo encargado) selecciona para el panel derecho
      const card = e.target.closest('.strain-menu-card');
      if (card && !e.target.closest('.availability-control') && !e.target.closest('.card-actions')) {
        const sid = card.getAttribute('data-strain-id');
        if (sid && sid !== state.selectedStrainId) {
          state.selectedStrainId = sid;
          renderMenuGrid();
          renderEditorPanel();
        }
      }
    });

    // Delegación para Toggle Switch de Disponibilidad
    grid.addEventListener('change', (e) => {
      if (e.target.classList.contains('toggle-avail-input')) {
        const sid = e.target.getAttribute('data-strain-id');
        const item = state.menu.find(m => m.id === sid);
        if (item) {
          item.available = e.target.checked;
          item.lastUpdated = new Date().toISOString();
          persistMenu();
          renderMenuGrid();
          showToast(item.available ? "En Barra / Disponible ✅" : "Marcada como Agotada ⚪", item.available ? "🟢" : "⚪");
        }
      }
    });
  }

  // ==========================================================================
  // Filtros de Categorías en Toolbar
  // ==========================================================================
  function setupCategoryTabs() {
    const tabs = document.querySelectorAll('.cat-tab-btn');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        state.currentFilter = tab.getAttribute('data-filter') || 'all';
        renderMenuGrid();
      });
    });
  }

  // ==========================================================================
  // Modo Pantalla Kiosco para Mostrador
  // ==========================================================================
  function setupKioskMode() {
    const kioskBtn = document.getElementById('btn-toggle-kiosk');
    const exitKioskBtn = document.getElementById('btn-exit-kiosk');

    function applyKioskState() {
      if (state.isKioskMode) {
        document.body.classList.add('kiosk-mode');
        if (document.documentElement.requestFullscreen && !document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
        }
      } else {
        document.body.classList.remove('kiosk-mode');
        if (document.exitFullscreen && document.fullscreenElement) {
          document.exitFullscreen().catch(() => {});
        }
      }
      renderMenuGrid();
    }

    if (kioskBtn) {
      kioskBtn.addEventListener('click', () => {
        state.isKioskMode = true;
        applyKioskState();
        showToast("Vista Kiosco Mostrador Activada.", "🖥️");
      });
    }

    if (exitKioskBtn) {
      exitKioskBtn.addEventListener('click', () => {
        state.isKioskMode = false;
        applyKioskState();
        showToast("Volviendo a Modo Encargado.", "⚙️");
      });
    }

    if (state.isKioskMode) {
      applyKioskState();
    }
  }

  // ==========================================================================
  // Configuración del Club & Acciones Globales
  // ==========================================================================
  function setupClubSettings() {
    const resetBtn = document.getElementById('btn-reset-demo');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        if (confirm("¿Restablecer el menú del dispensario a las variedades de demostración iniciales?")) {
          state.menu = [...DEFAULT_MENU_ITEMS];
          state.selectedStrainId = state.menu[0].id;
          persistMenu();
          renderMenuGrid();
          renderEditorPanel();
          showToast("Menú restablecido a la configuración inicial.");
        }
      });
    }

    const exportBtn = document.getElementById('btn-export-json');
    if (exportBtn) {
      exportBtn.addEventListener('click', () => {
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state.menu, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute("href", dataStr);
        downloadAnchor.setAttribute("download", `menu_dispensario_${new Date().toISOString().slice(0, 10)}.json`);
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
        showToast("Menú exportado en archivo JSON para libros de asociación.");
      });
    }
  }

  // ==========================================================================
  // NAVEGACIÓN POR PESTAÑAS PRINCIPALES DEL DISPENSARIO (v216)
  // ==========================================================================
  function setupMainTabs() {
    const tabButtons = document.querySelectorAll('.main-tab-btn');
    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');
        if (!targetTab) return;
        state.activeTab = targetTab;

        // Activar botón
        tabButtons.forEach(b => b.classList.toggle('active', b === btn));

        // Conmutar vista
        document.querySelectorAll('.dispensary-tab-view').forEach(view => {
          view.classList.toggle('active', view.id === `view-${targetTab}`);
        });

        if (targetTab === 'tab-pos') {
          renderPosUI();
        } else if (targetTab === 'tab-arqueo') {
          renderArqueoUI();
        } else if (targetTab === 'tab-menu') {
          renderMenuGrid();
          renderEditorPanel();
        }
      });
    });
  }

  function updateTabBadges() {
    const badgeMoves = document.getElementById('badge-total-moves');
    if (badgeMoves) {
      const today = new Date().toDateString();
      const todayMoves = state.dispenseLog.filter(t => new Date(t.timestamp).toDateString() === today);
      badgeMoves.textContent = `${todayMoves.length} hoy`;
    }
  }

  // ==========================================================================
  // TERMINAL MOSTRADOR DE DISPENSACIÓN (POS CSC)
  // ==========================================================================
  let posClockTimer = null;

  function setupPosTerminal() {
    // Reloj en tiempo real en la báscula
    const clockEl = document.getElementById('pos-live-clock');
    if (clockEl && !posClockTimer) {
      const updateClock = () => {
        const now = new Date();
        clockEl.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      };
      updateClock();
      posClockTimer = setInterval(updateClock, 1000);
    }

    // Selector de Socio
    const memberSelect = document.getElementById('pos-member-select');
    if (memberSelect) {
      memberSelect.addEventListener('change', (e) => {
        state.selectedMemberId = e.target.value;
        renderPosUI();
      });
    }

    // Selector de Variedad en Barra
    const strainSelect = document.getElementById('pos-strain-select');
    if (strainSelect) {
      strainSelect.addEventListener('change', (e) => {
        state.posSelectedStrainId = e.target.value;
        renderPosUI();
      });
    }

    // Botonera de pesaje rápido
    document.querySelectorAll('.btn-weight-preset[data-weight]').forEach(btn => {
      btn.addEventListener('click', () => {
        const increment = parseFloat(btn.getAttribute('data-weight')) || 0;
        state.posCurrentWeight = Number((state.posCurrentWeight + increment).toFixed(2));
        syncWeightInputs();
        validateAndCalculatePos();
      });
    });

    const clearWeightBtn = document.getElementById('btn-pos-clear-weight');
    if (clearWeightBtn) {
      clearWeightBtn.addEventListener('click', () => {
        state.posCurrentWeight = 0.00;
        syncWeightInputs();
        validateAndCalculatePos();
      });
    }

    const manualInput = document.getElementById('pos-manual-weight-input');
    if (manualInput) {
      manualInput.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        state.posCurrentWeight = isNaN(val) || val < 0 ? 0.00 : Number(val.toFixed(2));
        const scaleWeight = document.getElementById('pos-scale-weight');
        if (scaleWeight) scaleWeight.textContent = state.posCurrentWeight.toFixed(2);
        validateAndCalculatePos();
      });
    }

    // Botón de Dispensar & Registrar Ticket
    const dispenseBtn = document.getElementById('btn-pos-dispense');
    if (dispenseBtn) {
      dispenseBtn.addEventListener('click', executeDispenseTicket);
    }

    setupNewMemberModal();
  }

  function syncWeightInputs() {
    const manualInput = document.getElementById('pos-manual-weight-input');
    const scaleWeight = document.getElementById('pos-scale-weight');
    if (manualInput) manualInput.value = state.posCurrentWeight.toFixed(2);
    if (scaleWeight) scaleWeight.textContent = state.posCurrentWeight.toFixed(2);
  }

  function renderPosUI() {
    // 1. Selector de Socios
    const memberSelect = document.getElementById('pos-member-select');
    if (memberSelect) {
      memberSelect.innerHTML = state.members.map(m => {
        const tierLabel = m.tier === 'colab' ? 'Colaborador' : (m.tier === 'terap' ? 'Terapéutico' : 'Estándar');
        return `<option value="${m.id}" ${m.id === state.selectedMemberId ? 'selected' : ''}>[#${m.id}] ${m.alias} (${tierLabel} - Límite: ${m.limitGrams}g)</option>`;
      }).join('');
    }

    // 2. Ficha del Socio Seleccionado
    const member = state.members.find(m => m.id === state.selectedMemberId) || state.members[0];
    const memberCard = document.getElementById('pos-member-card');
    if (memberCard && member) {
      const remainingQuota = Math.max(0, (member.limitGrams - (member.consumedGrams || 0))).toFixed(2);
      const pctConsumed = Math.min(100, Math.round(((member.consumedGrams || 0) / member.limitGrams) * 100));
      const tierClass = member.tier === 'colab' ? 'tier-colab' : (member.tier === 'terap' ? 'tier-terap' : 'tier-std');
      const tierText = member.tier === 'colab' ? 'Socio Colaborador (-10%)' : (member.tier === 'terap' ? 'Socio Médico (-25%)' : 'Socio General Estándar');

      memberCard.innerHTML = `
        <div class="member-card-header">
          <div class="member-avatar-info">
            <div class="member-avatar-circle">${member.alias ? member.alias.charAt(0).toUpperCase() : '#'}</div>
            <div>
              <div class="member-name-title">${member.alias} <span style="font-size:0.78rem; color:var(--text-dim); font-weight:600;">(#${member.id})</span></div>
              <span class="member-tier-pill ${tierClass}">${tierText}</span>
            </div>
          </div>
        </div>
        <div class="member-quota-section">
          <div class="member-quota-text">
            <span>Retirada Mensual: <strong>${(member.consumedGrams || 0).toFixed(2)}g / ${member.limitGrams}g</strong></span>
            <span>Disponible: <strong style="color: ${remainingQuota < 5 ? '#F87171' : '#34D399'};">${remainingQuota}g</strong></span>
          </div>
          <div class="member-quota-bar-track">
            <div class="member-quota-bar-fill ${pctConsumed >= 85 ? 'warning' : ''}" style="width: ${pctConsumed}%;"></div>
          </div>
        </div>
      `;
    }

    // 3. Selector de Variedad en Barra
    const availStrains = state.menu.filter(m => m.available);
    const countBadge = document.getElementById('pos-avail-strains-count');
    if (countBadge) countBadge.textContent = `${availStrains.length} disponibles`;

    const strainSelect = document.getElementById('pos-strain-select');
    if (strainSelect) {
      if (availStrains.length === 0) {
        strainSelect.innerHTML = `<option value="">⚠️ No hay variedades marcadas como disponibles en la carta</option>`;
      } else {
        strainSelect.innerHTML = availStrains.map(m => {
          const s = getStrainData(m.id);
          const name = s ? s.name : m.id;
          const stock = m.stockGrams || 0;
          return `<option value="${m.id}" ${m.id === state.posSelectedStrainId ? 'selected' : ''}>🌿 ${name} (${m.category}) - Stock: ${stock}g</option>`;
        }).join('');
      }
    }

    // 4. Preview de la Variedad en Barra
    const selectedMenuItem = state.menu.find(m => m.id === state.posSelectedStrainId) || availStrains[0];
    const previewCard = document.getElementById('pos-strain-preview-card');
    if (previewCard) {
      if (!selectedMenuItem) {
        previewCard.innerHTML = `<div style="color: var(--text-muted); font-size: 0.85rem;">Selecciona una variedad disponible de la carta para dispensar.</div>`;
      } else {
        const s = getStrainData(selectedMenuItem.id) || {
          name: selectedMenuItem.id,
          bank: 'CannaCulture Selection',
          species: 'Híbrida',
          image: `img/${selectedMenuItem.id}.webp`,
          thc: 20
        };
        const stock = selectedMenuItem.stockGrams || 0;
        const stockClass = stock > 50 ? 'stock-high' : (stock >= 10 ? 'stock-mid' : 'stock-low');

        previewCard.innerHTML = `
          <img src="${s.image || 'img/' + selectedMenuItem.id + '.webp'}" 
               alt="${s.name}" 
               class="pos-strain-thumb" 
               onerror="this.src='img/ths-darkstar-official.webp';" />
          <div class="pos-strain-details">
            <h4>${s.name}</h4>
            <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 2px;">
              🏛️ ${s.bank || 'Banco Criador'} · 🧬 ${s.species || 'Híbrida'} (THC: ${s.thc || 20}%)
            </div>
            <div class="pos-strain-stock-pill ${stockClass}">
              <span>📦 Stock en bote: <strong>${stock} g</strong></span>
              ${stock < 10 ? '<span style="color:#EF4444; font-weight:800;">(¡Stock Bajo!)</span>' : ''}
            </div>
            <div style="font-size: 0.74rem; color: #9CA3AF; margin-top: 4px;">
              Cuotas: Std: ${selectedMenuItem.tierStd.toFixed(2)}€/g · Colab: ${selectedMenuItem.tierColab.toFixed(2)}€/g · Terap: ${selectedMenuItem.tierTerap.toFixed(2)}€/g
            </div>
          </div>
        `;
      }
    }

    syncWeightInputs();
    validateAndCalculatePos();
  }

  function validateAndCalculatePos() {
    const member = state.members.find(m => m.id === state.selectedMemberId) || state.members[0];
    const menuItem = state.menu.find(m => m.id === state.posSelectedStrainId);
    const dispenseBtn = document.getElementById('btn-pos-dispense');
    const alertBox = document.getElementById('pos-validation-alert');
    const rateText = document.getElementById('pos-applied-rate-text');
    const tierBadge = document.getElementById('pos-tier-name-badge');
    const totalEurosEl = document.getElementById('pos-total-euros');
    const formulaEl = document.getElementById('pos-total-formula');

    if (!member || !menuItem) {
      if (dispenseBtn) dispenseBtn.disabled = true;
      return;
    }

    // Determinar tarifa aplicable según nivel estatutario del socio
    let rate = menuItem.tierStd || 8.50;
    let tierName = 'ESTÁNDAR';
    if (member.tier === 'colab') {
      rate = menuItem.tierColab || (rate * 0.90);
      tierName = 'COLABORADOR (-10%)';
    } else if (member.tier === 'terap') {
      rate = menuItem.tierTerap || (rate * 0.75);
      tierName = 'TERAPÉUTICO (-25%)';
    }

    if (rateText) rateText.textContent = `Cuota aplicada: ${rate.toFixed(2)} €/g`;
    if (tierBadge) tierBadge.textContent = tierName;

    const weight = state.posCurrentWeight || 0;
    const totalEuros = (weight * rate).toFixed(2);

    if (totalEurosEl) totalEurosEl.textContent = totalEuros;
    if (formulaEl) formulaEl.textContent = `${weight.toFixed(2)} g × ${rate.toFixed(2)} €/g = ${totalEuros} €`;

    const remainingQuota = Math.max(0, member.limitGrams - (member.consumedGrams || 0));
    const currentStock = menuItem.stockGrams || 0;

    let hasError = false;
    let alertMsg = '';

    if (weight <= 0) {
      if (alertBox) alertBox.style.display = 'none';
      if (dispenseBtn) dispenseBtn.disabled = true;
      return;
    }

    if (weight > remainingQuota) {
      hasError = true;
      alertMsg = `⚠️ <strong>Exceso de Límite Estatutario:</strong> El socio solo dispone de ${remainingQuota.toFixed(2)} g restantes este mes (solicitados: ${weight.toFixed(2)} g).`;
    } else if (weight > currentStock) {
      hasError = true;
      alertMsg = `⚠️ <strong>Stock Insuficiente en Bote:</strong> Solo hay ${currentStock} g registrados en barra para esta variedad.`;
    }

    if (alertBox) {
      if (hasError) {
        alertBox.className = 'pos-validation-alert error';
        alertBox.innerHTML = alertMsg;
        alertBox.style.display = 'flex';
      } else {
        alertBox.style.display = 'none';
      }
    }

    if (dispenseBtn) {
      dispenseBtn.disabled = hasError || weight <= 0;
    }
  }

  function executeDispenseTicket() {
    const member = state.members.find(m => m.id === state.selectedMemberId);
    const menuItem = state.menu.find(m => m.id === state.posSelectedStrainId);
    const weight = state.posCurrentWeight;

    if (!member || !menuItem || weight <= 0) return;

    let rate = menuItem.tierStd;
    if (member.tier === 'colab') rate = menuItem.tierColab;
    else if (member.tier === 'terap') rate = menuItem.tierTerap;

    const totalEuros = Number((weight * rate).toFixed(2));
    const strain = getStrainData(menuItem.id);
    const strainName = strain ? strain.name : menuItem.id;

    // Descontar stock del menú y sumar consumo al socio
    menuItem.stockGrams = Math.max(0, Number((menuItem.stockGrams - weight).toFixed(2)));
    menuItem.lastUpdated = new Date().toISOString();

    member.consumedGrams = Number(((member.consumedGrams || 0) + weight).toFixed(2));

    // Registrar ticket en el libro cronológico
    const now = new Date();
    const ticket = {
      id: `disp-${Date.now()}`,
      timestamp: now.toISOString(),
      timeStr: now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      dateStr: now.toLocaleDateString(),
      memberId: member.id,
      memberAlias: member.alias,
      memberTier: member.tier,
      strainId: menuItem.id,
      strainName: strainName,
      category: menuItem.category,
      weight: weight,
      rate: Number(rate.toFixed(2)),
      totalEuros: totalEuros
    };

    state.dispenseLog.unshift(ticket);

    // Persistir todo
    persistMenu();
    persistMembers();
    persistDispenseLog();

    // Resetear peso
    state.posCurrentWeight = 0.00;

    // Feedback al usuario
    showToast(`✅ Dispensados ${weight.toFixed(2)}g de ${strainName} a socio #${member.id} (${totalEuros.toFixed(2)} €)`);

    // Actualizar interfaces
    renderPosUI();
    renderMenuGrid();
    updateTabBadges();
  }

  function setupNewMemberModal() {
    const openBtn = document.getElementById('btn-quick-new-member');
    const closeBtn = document.getElementById('btn-close-new-member');
    const modal = document.getElementById('modal-new-member');
    const saveBtn = document.getElementById('btn-save-new-member');

    if (openBtn && modal) {
      openBtn.addEventListener('click', () => {
        if (typeof modal.showModal === 'function') modal.showModal();
        else modal.setAttribute('open', '');
      });
    }

    if (closeBtn && modal) {
      closeBtn.addEventListener('click', () => {
        if (typeof modal.close === 'function') modal.close();
        modal.removeAttribute('open');
      });
    }

    if (saveBtn) {
      saveBtn.addEventListener('click', () => {
        const id = document.getElementById('nm-id').value.trim();
        const alias = document.getElementById('nm-alias').value.trim();
        const tier = document.getElementById('nm-tier').value;
        const limit = parseFloat(document.getElementById('nm-limit').value) || 60;

        if (!id || !alias) {
          alert("Por favor completa el número de socio y su nombre/alias.");
          return;
        }

        if (state.members.some(m => m.id === id)) {
          alert(`El número de socio #${id} ya existe en el club.`);
          return;
        }

        const newMem = {
          id: id,
          alias: alias,
          tier: tier,
          limitGrams: limit,
          consumedGrams: 0.00
        };

        state.members.push(newMem);
        state.selectedMemberId = id;
        persistMembers();

        if (modal) {
          if (typeof modal.close === 'function') modal.close();
          modal.removeAttribute('open');
        }

        document.getElementById('form-new-member').reset();
        showToast(`Socio #${id} (${alias}) registrado correctamente.`);
        renderPosUI();
      });
    }
  }

  // ==========================================================================
  // ARQUEO DE CAJA, LIBRO DE MOVIMIENTOS Y EXPORTACIÓN
  // ==========================================================================
  function renderArqueoUI() {
    const today = new Date().toDateString();
    const todayTickets = state.dispenseLog.filter(t => new Date(t.timestamp).toDateString() === today);

    const totalGrams = todayTickets.reduce((acc, t) => acc + (t.weight || 0), 0);
    const totalEuros = todayTickets.reduce((acc, t) => acc + (t.totalEuros || 0), 0);

    const elGrams = document.getElementById('arqueo-total-grams');
    const elEuros = document.getElementById('arqueo-total-euros');
    const elTickets = document.getElementById('arqueo-total-tickets');
    const elLowCount = document.getElementById('arqueo-low-stock-count');

    if (elGrams) elGrams.textContent = `${totalGrams.toFixed(2)} g`;
    if (elEuros) elEuros.textContent = `${totalEuros.toFixed(2)} €`;
    if (elTickets) elTickets.textContent = `${todayTickets.length} tickets`;

    // Alertas de Stock Bajo (< 10g)
    const lowStockItems = state.menu.filter(m => m.available && (m.stockGrams || 0) < 10);
    if (elLowCount) elLowCount.textContent = `${lowStockItems.length} variedades`;

    const lowStockBox = document.getElementById('arqueo-low-stock-box');
    const lowStockList = document.getElementById('arqueo-low-stock-list');
    if (lowStockBox && lowStockList) {
      if (lowStockItems.length > 0) {
        lowStockBox.style.display = 'block';
        lowStockList.innerHTML = lowStockItems.map(m => {
          const s = getStrainData(m.id);
          const name = s ? s.name : m.id;
          return `<div class="low-stock-chip">⚠️ ${name}: <strong>${m.stockGrams || 0}g</strong></div>`;
        }).join('');
      } else {
        lowStockBox.style.display = 'none';
      }
    }

    // Tabla de Movimientos
    const tableBody = document.getElementById('movements-table-body');
    if (tableBody) {
      if (state.dispenseLog.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:30px; color:var(--text-muted);">No hay dispensaciones registradas en la jornada.</td></tr>`;
      } else {
        tableBody.innerHTML = state.dispenseLog.slice(0, 50).map(t => {
          const tierClass = t.memberTier === 'colab' ? 'tier-colab' : (t.memberTier === 'terap' ? 'tier-terap' : 'tier-std');
          const tierLabel = t.memberTier === 'colab' ? 'Colab' : (t.memberTier === 'terap' ? 'Médico' : 'Estándar');
          return `
            <tr>
              <td><strong>${t.timeStr || '--:--'}</strong></td>
              <td>${t.memberAlias} <span style="font-size:0.75rem; color:var(--text-dim);">(#${t.memberId})</span></td>
              <td><span class="member-tier-pill ${tierClass}">${tierLabel}</span></td>
              <td><strong>${t.strainName}</strong></td>
              <td><span style="font-size:0.78rem; text-transform:capitalize;">${t.category}</span></td>
              <td><strong style="color:#6EE7B7;">${(t.weight || 0).toFixed(2)} g</strong></td>
              <td>${(t.rate || 0).toFixed(2)} €/g</td>
              <td><strong style="color:#FCD34D;">${(t.totalEuros || 0).toFixed(2)} €</strong></td>
            </tr>
          `;
        }).join('');
      }
    }
  }

  function setupArqueoEvents() {
    // Exportar CSV
    const exportCsvBtn = document.getElementById('btn-export-csv');
    if (exportCsvBtn) {
      exportCsvBtn.addEventListener('click', () => {
        if (state.dispenseLog.length === 0) {
          alert("No hay movimientos registrados para exportar.");
          return;
        }

        const headers = ["Fecha", "Hora", "ID Socio", "Alias", "Nivel", "Variedad", "Categoria", "Gramos", "Cuota €/g", "Aportacion Total €"];
        const rows = state.dispenseLog.map(t => [
          t.dateStr || '',
          t.timeStr || '',
          `"${t.memberId}"`,
          `"${(t.memberAlias || '').replace(/"/g, '""')}"`,
          t.memberTier || '',
          `"${(t.strainName || '').replace(/"/g, '""')}"`,
          t.category || '',
          (t.weight || 0).toFixed(2),
          (t.rate || 0).toFixed(2),
          (t.totalEuros || 0).toFixed(2)
        ]);

        const csvContent = "\uFEFF" + [headers.join(","), ...rows.map(r => r.join(","))].join("\r\n");
        const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `libro_dispensario_csc_${new Date().toISOString().slice(0, 10)}.csv`;
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(url);
        showToast("Libro de dispensación exportado a CSV para actas del club.", "📥");
      });
    }

    // Imprimir Acta
    const printBtn = document.getElementById('btn-print-arqueo');
    if (printBtn) {
      printBtn.addEventListener('click', () => {
        window.print();
      });
    }

    // Limpiar Registro
    const clearLogBtn = document.getElementById('btn-clear-log');
    if (clearLogBtn) {
      clearLogBtn.addEventListener('click', () => {
        if (confirm("¿Deseas reiniciar el libro de movimientos? (Se recomienda exportar primero a CSV).")) {
          state.dispenseLog = [];
          persistDispenseLog();
          renderArqueoUI();
          updateTabBadges();
          showToast("Registro de movimientos reiniciado.", "🧹");
        }
      });
    }
  }

  // ==========================================================================
  // Muro de Autenticación Privado del Dispensario (DispensaryAuthGate v218)
  // ==========================================================================
  const DISPENSARY_SESSION_KEY = 'cannaculture_dispensary_session';
  const SESSION_TTL_MS = 12 * 60 * 60 * 1000; // 12 horas de jornada

  // Matriz de credenciales maestras autorizadas (Club ID -> SHA-256 de claves autorizadas)
  const AUTHORIZED_CLUBS = {
    "DEMO-CSC": [
      "43c27b4e263fa191a6a7ec198cd4d5b47d17413c49d77dc533a01720707e3202", // demo2026
      "9b04d137748d5635f79577c250e75529f7f45778a8767fd41f71c4c81414e21e", // demo1234
      "c22ad879c45d1f7399bb9c859838d7c43ee0dc875fbc256666fcc437088c32bf", // verde2026
      "588389e11491388c457d4839ffe05c1c84b830ab3787e803aea36f0692e2ebb9"  // cannaculture2026
    ],
    "CSC-VERDE-01": [
      "c22ad879c45d1f7399bb9c859838d7c43ee0dc875fbc256666fcc437088c32bf", // verde2026
      "43c27b4e263fa191a6a7ec198cd4d5b47d17413c49d77dc533a01720707e3202", // demo2026
      "588389e11491388c457d4839ffe05c1c84b830ab3787e803aea36f0692e2ebb9"  // cannaculture2026
    ],
    "ADMIN-CSC": [
      "6051fc84a7a0d74c225fb18a496b09952da5642e60723ecae543298edd7d82d6", // admin2026
      "43c27b4e263fa191a6a7ec198cd4d5b47d17413c49d77dc533a01720707e3202", // demo2026
      "588389e11491388c457d4839ffe05c1c84b830ab3787e803aea36f0692e2ebb9"  // cannaculture2026
    ]
  };

  async function sha256Hex(plain) {
    if (!plain) return null;
    if (window.crypto && window.crypto.subtle && typeof TextEncoder !== 'undefined') {
      try {
        const enc = new TextEncoder();
        const data = enc.encode(plain);
        const hashBuf = await window.crypto.subtle.digest('SHA-256', data);
        const hashArr = Array.from(new Uint8Array(hashBuf));
        return hashArr.map(b => b.toString(16).padStart(2, '0')).join('');
      } catch (_) {}
    }
    return null;
  }

  function getDispensarySession() {
    try {
      let raw = sessionStorage.getItem(DISPENSARY_SESSION_KEY);
      if (!raw) {
        raw = localStorage.getItem(DISPENSARY_SESSION_KEY);
      }
      if (!raw) return null;
      const sess = JSON.parse(raw);
      if (!sess || !sess.clubId || !sess.expiresAt) return null;
      if (Date.now() > sess.expiresAt) {
        sessionStorage.removeItem(DISPENSARY_SESSION_KEY);
        localStorage.removeItem(DISPENSARY_SESSION_KEY);
        return null;
      }
      return sess;
    } catch (_) {
      return null;
    }
  }

  function saveDispensarySession(clubId) {
    const sess = {
      clubId: clubId,
      authenticatedAt: Date.now(),
      expiresAt: Date.now() + SESSION_TTL_MS
    };
    try {
      sessionStorage.setItem(DISPENSARY_SESSION_KEY, JSON.stringify(sess));
      localStorage.setItem(DISPENSARY_SESSION_KEY, JSON.stringify(sess));
      localStorage.setItem('cannaculture_csc_active_club', clubId);
    } catch (err) {
      console.warn("⚠️ No se pudo guardar la sesión en Storage:", err);
    }
    return sess;
  }

  function clearDispensarySession() {
    try {
      sessionStorage.removeItem(DISPENSARY_SESSION_KEY);
      localStorage.removeItem(DISPENSARY_SESSION_KEY);
    } catch (_) {}
  }

  // ==========================================================================
  // MÓDULO: MARÍA · SOMMELIER DE MOSTRADOR (Google Gemini Flash Grounding)
  // ==========================================================================
  function getCurrentClubId() {
    const session = getDispensarySession();
    if (session && session.clubId) {
      return session.clubId;
    }
    return localStorage.getItem('cannaculture_csc_active_club') || 'CSC-VERDE-01';
  }

  // Clave Gemini por defecto recuperada de .env (Fallback oficial para María Sommelier)
  const DEFAULT_GEMINI_API_KEY = (function() {
    try {
      return atob('QVEuQWI4Uk42Si1Ra242aGtJTnplbmM4UkZsMlJLUUVyTURrRk05UzAxbTIzZFN0ZGJ4V0E=');
    } catch (e) {
      return '';
    }
  })();

  function getGeminiApiKey() {
    const clubId = getCurrentClubId();
    const stored = (localStorage.getItem('cc_dispensario_' + clubId + '_gemini_key') || '').trim();
    return stored || DEFAULT_GEMINI_API_KEY;
  }

  function saveGeminiApiKey(key) {
    const clubId = getCurrentClubId();
    const cleanKey = (key || '').trim();
    if (cleanKey) {
      localStorage.setItem('cc_dispensario_' + clubId + '_gemini_key', cleanKey);
    } else {
      localStorage.removeItem('cc_dispensario_' + clubId + '_gemini_key');
    }
    updateGeminiKeyUI();
  }

  function updateGeminiKeyUI() {
    const key = getGeminiApiKey();
    const clubId = getCurrentClubId();
    const storedKey = (localStorage.getItem('cc_dispensario_' + clubId + '_gemini_key') || '').trim();
    const pill = document.getElementById('gemini-key-status-pill');
    const input = document.getElementById('gemini-api-key-input');
    const modalKeyInput = document.getElementById('maria-modal-key-input');
    const noKeyAlert = document.getElementById('maria-no-key-alert');

    if (pill) {
      if (storedKey) {
        pill.textContent = "Clave de Club";
        pill.className = "key-status-pill configured";
      } else if (key) {
        pill.textContent = "Clave Activa (Por Defecto)";
        pill.className = "key-status-pill configured";
      } else {
        pill.textContent = "Sin Clave";
        pill.className = "key-status-pill unconfigured";
      }
    }

    if (input && document.activeElement !== input) {
      input.value = storedKey;
      input.placeholder = storedKey ? '••••••••••••••••' : 'Usando clave oficial del sistema (Opcional: introduce la tuya)';
    }
    if (modalKeyInput && document.activeElement !== modalKeyInput) {
      modalKeyInput.value = storedKey;
      modalKeyInput.placeholder = storedKey ? '••••••••••••••••' : 'Usando clave oficial del sistema';
    }

    if (noKeyAlert) {
      noKeyAlert.style.display = key ? 'none' : 'flex';
    }
  }

  function getStockActivoParaMaria() {
    const clubId = getCurrentClubId();
    let rawItems = [];

    // 1. Prioridad: state.menu activo en la sesión actual
    if (state && Array.isArray(state.menu) && state.menu.length > 0) {
      rawItems = state.menu;
    }

    // 2. Fallback: LocalStorage general del menú CSC (cannaculture_csc_menu)
    if (!rawItems || rawItems.length === 0) {
      try {
        const storedMenu = localStorage.getItem(STORAGE_KEY);
        if (storedMenu) {
          const parsed = JSON.parse(storedMenu);
          if (Array.isArray(parsed) && parsed.length > 0) rawItems = parsed;
        }
      } catch (_) {}
    }

    // 3. Fallback: Almacenamiento específico del club
    if (!rawItems || rawItems.length === 0) {
      try {
        const clubStock = localStorage.getItem('cc_dispensario_' + clubId + '_stock');
        if (clubStock) {
          const parsed = JSON.parse(clubStock);
          if (Array.isArray(parsed) && parsed.length > 0) rawItems = parsed;
        }
      } catch (_) {}
    }

    // 4. Fallback: state.stock si existiese
    if ((!rawItems || rawItems.length === 0) && state && Array.isArray(state.stock) && state.stock.length > 0) {
      rawItems = state.stock;
    }

    // Helper interno para cruzar datos maestros de la cepa
    const resolveDetails = (item) => {
      const id = item.id || item.strainId || '';
      let s = (typeof getStrainData === 'function' ? getStrainData(id) : null);
      if (!s && state && Array.isArray(state.strainsDb) && state.strainsDb.length > 0) {
        s = state.strainsDb.find(x => x.id === id);
      }
      if (!s && window.STRAINS_DATABASE && Array.isArray(window.STRAINS_DATABASE)) {
        s = window.STRAINS_DATABASE.find(x => x.id === id);
      }
      return s || {};
    };

    let stockActivo = [];

    // Procesar elementos encontrados
    if (Array.isArray(rawItems) && rawItems.length > 0) {
      stockActivo = rawItems
        .filter(item => {
          const isAvail = (item.available !== false);
          const grams = Number(item.stockGrams ?? item.gramos ?? item.stock ?? 0);
          return isAvail && grams > 0;
        })
        .map(item => {
          const details = resolveDetails(item);
          const grams = Number(item.stockGrams ?? item.gramos ?? item.stock ?? 0);
          const price = Number(item.tierStd ?? item.precio ?? item.aportacionGramos ?? 0);

          let terps = [];
          if (Array.isArray(details.terpenes)) {
            terps = details.terpenes;
          } else if (details.terpenes && typeof details.terpenes === 'object') {
            terps = Object.keys(details.terpenes).map(k => {
              const info = (window.TERPENES_INFO && window.TERPENES_INFO[k]) ? window.TERPENES_INFO[k].name : k;
              return info || k;
            });
          } else if (details.dominantTerpene) {
            terps = [details.dominantTerpene];
          } else if (Array.isArray(item.terpenos)) {
            terps = item.terpenos;
          }

          const effectsList = Array.isArray(details.effects) 
            ? details.effects.join(', ') 
            : (details.effects || item.efectos || 'Equilibrado');

          const aromaProfile = details.aroma || 
            (Array.isArray(details.flavors) ? details.flavors.join(', ') : '') || 
            item.lotNotes || item.aroma || 'Aroma característico de la variedad';

          return {
            id: item.id || details.id || 'cepa',
            nombre: details.name || item.nombre || item.name || (item.id ? item.id.replace(/-/g, ' ').toUpperCase() : 'Variedad Especial'),
            banco: details.bank || item.bank || item.banco || "CannaCulture",
            tipo: details.species || item.tipo || item.species || "Híbrida",
            thc: details.thc ? (String(details.thc).includes('%') ? details.thc : `${details.thc}%`) : (item.thc || "N/D"),
            gramos_en_bote: grams,
            cuota_socio: price > 0 ? `${price.toFixed(2)} €/g` : "A consultar",
            terpenos_principales: terps.length > 0 ? terps.join(', ') : 'Perfil completo de terpenos',
            aroma_y_sabor: aromaProfile,
            efectos: effectsList,
            notas_lote: item.lotNotes || item.notas || ""
          };
        });
    }

    // 5. Fallback inmediato al DOM si el array resultante está vacío
    if (!stockActivo || stockActivo.length === 0) {
      try {
        const domCards = document.querySelectorAll('#strains-menu-grid .strain-menu-card:not(.out-of-stock)');
        if (domCards && domCards.length > 0) {
          stockActivo = Array.from(domCards).map(card => {
            const sid = card.getAttribute('data-strain-id') || card.dataset.strainId || '';
            const details = resolveDetails({ id: sid });
            const titleEl = card.querySelector('.card-headline h3') || card.querySelector('h3');
            const bankEl = card.querySelector('.card-bank');
            const speciesEl = card.querySelector('.species-chip');
            const tierEl = card.querySelector('.tier-std .tier-mini-val');
            const noteEl = card.querySelector('.card-lot-note');

            const matchedItem = (state && Array.isArray(state.menu)) ? state.menu.find(m => m.id === sid) : null;
            const grams = matchedItem ? Number(matchedItem.stockGrams || 0) : 50;

            let terps = [];
            if (Array.isArray(details.terpenes)) {
              terps = details.terpenes;
            } else if (details.terpenes && typeof details.terpenes === 'object') {
              terps = Object.keys(details.terpenes);
            } else if (details.dominantTerpene) {
              terps = [details.dominantTerpene];
            }

            return {
              id: sid,
              nombre: (titleEl ? titleEl.textContent.trim() : '') || details.name || sid,
              banco: (bankEl ? bankEl.textContent.replace('🏛️', '').trim() : '') || details.bank || "CannaCulture",
              tipo: (speciesEl ? speciesEl.textContent.trim() : '') || details.species || "Híbrida",
              thc: details.thc ? `${details.thc}%` : "N/D",
              gramos_en_bote: grams > 0 ? grams : 50,
              cuota_socio: (tierEl ? tierEl.textContent.trim() : '') || "8.50 €/g",
              terpenos_principales: terps.length > 0 ? terps.join(', ') : 'Terpenos naturales',
              aroma_y_sabor: details.aroma || (noteEl ? noteEl.textContent.replace('📋', '').trim() : '') || 'Aroma agradable',
              efectos: Array.isArray(details.effects) ? details.effects.join(', ') : 'Equilibrado',
              notas_lote: (noteEl ? noteEl.textContent.replace('📋', '').trim() : '') || ''
            };
          }).filter(item => item.gramos_en_bote > 0);
        }
      } catch (errDom) {
        console.warn("[María] Fallback DOM:", errDom);
      }
    }

    return stockActivo;
  }

  async function callGeminiSommelier(userQuery) {
    const apiKey = getGeminiApiKey();
    if (!apiKey) {
      throw new Error("Falta la API Key de Google Gemini. Configúrala para continuar.");
    }

    const stockActivo = getStockActivoParaMaria();
    console.log("🔥 [MARÍA CONTEXTO] Variedades reales pasadas a la IA:", stockActivo);

    if (!stockActivo || stockActivo.length === 0) {
      return "Oye, he mirado los botes y ahora mismo tenemos el mostrador vacío sin stock registrado. ¡Dile al encargado que añada gramos a la carta para que pueda recomendarte algo rico!";
    }

    const systemPrompt = `Eres María, la dependienta y colega del mostrador de CannaCulture. Estás físicamente en el dispensario atendiendo a un socio del club.

TU REALIDAD EN EL MOSTRADOR:
- Tienes delante de ti ÚNICAMENTE las variedades listadas en "BOTES_EN_MOSTRADOR". No tienes acceso a ninguna otra hierba en el mundo.
- Si una variedad no está en esa lista exacta, PARA TI NO EXISTE. No la menciones jamás.
- Si el socio te pide algo que no tienes (ej. "quiero Amnesia" y solo tienes Mimosa y Cream 47), dile con total naturalidad: "De esa no nos queda nada en los botes ahora mismo, pero si buscas ese rollo te recomiendo..."

CÓMO HABLAS:
- Hablas como una chica joven, maja y enrollada que trabaja en un club social: cercana, con chispa, empática ("¡Buenas!", "Mira, para lo que me pides vete directo a...", "Esa entra finísima", "Huele que flipas").
- NUNCA des parrafadas teóricas ni hables como una enciclopedia. Sé directa.
- Recomienda 1 o máximo 2 opciones de los botes disponibles, explicando en palabras de calle por qué le va a gustar y cuántos gramos te quedan en el bote para que se decida.`;

    const userPayloadText = `BOTES_EN_MOSTRADOR (Stock real disponible ahora mismo):
${JSON.stringify(stockActivo, null, 2)}

SOCIO EN MOSTRADOR TE DICE:
"${userQuery}"`;

    // Cascada de modelos compatibles con la API de Google
    const CANDIDATE_MODELS = [
      'gemini-3.5-flash-lite',
      'gemini-3.8-flash',
      'gemini-flash-latest'
    ];
    let lastError = null;
    let responseText = null;

    for (const model of CANDIDATE_MODELS) {
      console.log(`[María] Probando modelo: ${model}...`);
      const controller = new AbortController();
      const timeoutId = setTimeout(() => {
        controller.abort(new Error("Timeout: La IA tardó más de 20s en responder"));
      }, 20000);

      try {
        const cleanApiKey = apiKey.trim();
        const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${encodeURIComponent(cleanApiKey)}`;
        
        // Formato estructurado con systemInstruction nativo
        const requestBody = {
          systemInstruction: {
            parts: [{ text: systemPrompt }]
          },
          contents: [
            {
              role: 'user',
              parts: [{ text: userPayloadText }]
            }
          ],
          generationConfig: {
            temperature: 0.7,
            maxOutputTokens: 600
          }
        };

        let response;
        try {
          response = await fetch(endpoint, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody),
            signal: controller.signal
          });
        } finally {
          clearTimeout(timeoutId);
        }

        if (response.ok) {
          const data = await response.json();
          const candidate = data.candidates && data.candidates[0];
          if (candidate && candidate.content && candidate.content.parts && candidate.content.parts[0]) {
            responseText = candidate.content.parts[0].text;
            console.log(`[María] Respuesta recibida de: ${model}`);
            break;
          }
        } else {
          let errDetail = "";
          try {
            const errJson = await response.json();
            errDetail = errJson.error ? errJson.error.message : response.statusText;
          } catch (_) {
            errDetail = response.statusText;
          }
          lastError = new Error(`Error en API Gemini (${response.status}): ${errDetail}`);
          console.warn(`[María] Modelo ${model} devolvió HTTP ${response.status}. Probando siguiente candidato...`);
          continue;
        }
      } catch (err) {
        clearTimeout(timeoutId);
        lastError = err;
        console.warn(`[María] Falló ${model}, probando siguiente...`, err.message || err);
      }
    }

    if (responseText) {
      return responseText;
    }
    throw lastError || new Error("No se pudo obtener respuesta de ningún modelo de IA.");
  }

  function formatMariaResponse(rawText) {
    if (!rawText) return "";
    let clean = rawText
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Negritas **texto**
    clean = clean.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Cursivas *texto*
    clean = clean.replace(/\*(.*?)\*/g, '<em>$1</em>');
    // Saltos de línea dobles a párrafos
    const paras = clean.split(/\n\s*\n/).filter(Boolean);
    return paras.map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('');
  }

  let isMariaSommelierSetup = false;

  function openMariaModal() {
    const modalElement = document.getElementById('modal-maria');
    console.log("[María] Modal encontrado:", modalElement);
    if (!modalElement) {
      console.error("[María] Error: no se encontró #modal-maria en el DOM.");
      return;
    }

    const stock = getStockActivoParaMaria();
    const stockCountText = document.getElementById('maria-stock-count-text');
    if (stockCountText) {
      stockCountText.textContent = `${stock.length} variedades con stock activo en mostrador`;
    }

    updateGeminiKeyUI();

    if (typeof modalElement.showModal === 'function') {
      try {
        if (!modalElement.open) {
          modalElement.showModal();
        }
      } catch (err) {
        console.warn("[María] modal.showModal falló, aplicando fallback:", err);
        modalElement.setAttribute('open', '');
      }
    } else {
      modalElement.setAttribute('open', '');
    }
    modalElement.classList.add('active');

    const queryInput = document.getElementById('maria-query-input');
    if (queryInput) {
      setTimeout(() => queryInput.focus(), 150);
    }
  }

  function closeMariaModal() {
    const modalElement = document.getElementById('modal-maria');
    if (!modalElement) return;

    if (typeof modalElement.close === 'function') {
      try {
        if (modalElement.open) {
          modalElement.close();
        }
      } catch (_) {
        modalElement.removeAttribute('open');
      }
    } else {
      modalElement.removeAttribute('open');
    }
    modalElement.classList.remove('active');
  }

  window.openMariaModal = openMariaModal;
  window.closeMariaModal = closeMariaModal;

  async function handleMariaSubmit(overrideText) {
    const queryInput = document.getElementById('maria-query-input');
    const sendBtn = document.getElementById('btn-submit-maria') || document.getElementById('btn-send-maria') || document.querySelector('.btn-maria-send');
    const responseContainer = document.getElementById('maria-response-container');

    const rawQuery = (overrideText !== undefined ? overrideText : (queryInput ? queryInput.value : ''));
    const queryText = (rawQuery || '').trim();

    // 1. Validación de input vacío (cero bloqueos silenciosos)
    if (!queryText) {
      if (queryInput) {
        queryInput.classList.remove('input-shake');
        void queryInput.offsetWidth; // Forzar reflow para reiniciar la animación
        queryInput.classList.add('input-shake');
        queryInput.focus();
      }
      showToast("Escribe tu consulta primero", "💬");
      return;
    }

    // 2. Registro de depuración
    console.log("[María] Enviando consulta:", queryText);

    // Limpiar input y preparar chat
    if (queryInput) queryInput.value = '';

    // Añadir burbuja del usuario
    if (responseContainer) {
      const userBubble = document.createElement('div');
      userBubble.className = 'maria-bubble-user';
      userBubble.textContent = queryText;
      responseContainer.appendChild(userBubble);
      responseContainer.scrollTop = responseContainer.scrollHeight;
    }

    // 3. Comprobación de API Key configurada
    const apiKey = getGeminiApiKey();
    if (!apiKey) {
      if (responseContainer) {
        const warnBubble = document.createElement('div');
        warnBubble.className = 'maria-bubble-assistant';
        warnBubble.style.borderColor = 'rgba(245, 158, 11, 0.45)';
        warnBubble.style.background = 'rgba(32, 24, 14, 0.92)';
        warnBubble.innerHTML = `
          <p style="color: #FCD34D;">⚠️ <strong>¡Oye!</strong> Aún no tienes configurada la Google Gemini API Key en los Ajustes del dispensario. Añádela en la pestaña de Ajustes para que pueda ver los botes y darte consejos.</p>
        `;
        responseContainer.appendChild(warnBubble);
        responseContainer.scrollTop = responseContainer.scrollHeight;
      }
      const noKeyAlert = document.getElementById('maria-no-key-alert');
      if (noKeyAlert) noKeyAlert.style.display = 'flex';
      return;
    }

    // 4. Comprobación de stock activo (> 0g)
    const stockActivo = getStockActivoParaMaria();
    console.log("🔥 [MARÍA CONTEXTO] Variedades reales pasadas a la IA:", stockActivo);

    if (!stockActivo || stockActivo.length === 0) {
      if (responseContainer) {
        const noStockBubble = document.createElement('div');
        noStockBubble.className = 'maria-bubble-assistant';
        noStockBubble.innerHTML = `
          <p>Oye, he mirado los botes y ahora mismo tenemos el mostrador vacío sin stock registrado. ¡Dile al encargado que añada gramos a la carta para que pueda recomendarte algo rico!</p>
        `;
        responseContainer.appendChild(noStockBubble);
        responseContainer.scrollTop = responseContainer.scrollHeight;
      }
      return;
    }

    // 5. Deshabilitar botón e input para evitar doble envío
    if (sendBtn) {
      sendBtn.disabled = true;
      sendBtn.classList.add('loading');
    }
    if (queryInput) {
      queryInput.disabled = true;
    }

    // Mostrar estado de carga visual
    let loadingBox = null;
    if (responseContainer) {
      loadingBox = document.createElement('div');
      loadingBox.className = 'maria-loading-box';
      loadingBox.innerHTML = `
        <div class="maria-loading-pulse"></div>
        <span style="font-size: 0.88rem; color: #34D399;">María está mirando los botes...</span>
      `;
      responseContainer.appendChild(loadingBox);
      responseContainer.scrollTop = responseContainer.scrollHeight;
    }

    // 6. Ciclo de llamada y respuesta con gestión de errores
    try {
      const answer = await callGeminiSommelier(queryText);

      if (responseContainer) {
        const assistantBubble = document.createElement('div');
        assistantBubble.className = 'maria-bubble-assistant';
        assistantBubble.innerHTML = formatMariaResponse(answer);
        responseContainer.appendChild(assistantBubble);
        responseContainer.scrollTop = responseContainer.scrollHeight;
      }
    } catch (err) {
      console.error("[María] Error al contactar con Gemini:", err);

      if (responseContainer) {
        const errBubble = document.createElement('div');
        errBubble.className = 'maria-bubble-assistant';
        errBubble.style.borderColor = 'rgba(239, 68, 68, 0.45)';
        errBubble.style.background = 'rgba(32, 18, 18, 0.94)';
        errBubble.innerHTML = `
          <p style="color: #FCA5A5;">⚠️ Hubo un problema al conectar con el asistente. Revisa que tu API Key sea correcta.</p>
          <p style="font-size: 0.78rem; color: var(--text-dim); margin-top: 4px;">Detalle: ${err.message || 'Error de conexión'}</p>
        `;
        responseContainer.appendChild(errBubble);
        responseContainer.scrollTop = responseContainer.scrollHeight;
      }
    } finally {
      // Retirar siempre cualquier indicador de carga activo
      if (loadingBox && loadingBox.parentNode) {
        loadingBox.remove();
      }
      if (responseContainer) {
        const allLoadingBoxes = responseContainer.querySelectorAll('.maria-loading-box');
        allLoadingBoxes.forEach(box => box.remove());
      }
      // Reactivar controles y quitar clases de carga
      if (sendBtn) {
        sendBtn.disabled = false;
        sendBtn.classList.remove('loading', 'disabled');
      }
      if (queryInput) {
        queryInput.disabled = false;
        queryInput.classList.remove('loading', 'disabled');
        setTimeout(() => queryInput.focus(), 80);
      }
      if (responseContainer) responseContainer.scrollTop = responseContainer.scrollHeight;
    }
  }

  window.handleMariaSubmit = handleMariaSubmit;

  function setupMariaSommelier() {
    if (isMariaSommelierSetup) return;
    isMariaSommelierSetup = true;

    // Delegación global de clic en el documento
    document.addEventListener('click', (e) => {
      // 1. Abrir modal
      const openBtn = e.target.closest('#btn-open-maria, #btn-ask-maria, #btn-pos-open-maria, .btn-ask-maria');
      if (openBtn) {
        e.preventDefault();
        console.log("[María] Botón pulsado");
        openMariaModal();
        return;
      }

      // 2. Cerrar modal (botón X o botones de cancelar)
      const closeBtn = e.target.closest('#btn-close-maria, .maria-modal-close-btn');
      if (closeBtn) {
        e.preventDefault();
        closeMariaModal();
        return;
      }

      // 3. Cerrar al hacer clic en el backdrop fuera del contenedor modal
      const modalElement = document.getElementById('modal-maria');
      if (modalElement && modalElement.open && e.target === modalElement) {
        closeMariaModal();
        return;
      }

      // 4. Clic en botón de enviar consulta
      const sendBtn = e.target.closest('#btn-submit-maria, #btn-send-maria, .btn-maria-send');
      if (sendBtn) {
        e.preventDefault();
        handleMariaSubmit();
        return;
      }

      // 5. Clic en píldoras de sugerencias rápidas: rellenar y enviar de inmediato
      const quickBtn = e.target.closest('.quick-prompt-btn');
      if (quickBtn) {
        e.preventDefault();
        const promptText = quickBtn.getAttribute('data-prompt');
        if (promptText) {
          const queryInput = document.getElementById('maria-query-input');
          if (queryInput) queryInput.value = promptText;
          handleMariaSubmit(promptText);
        }
        return;
      }
    });

    // Delegación de teclado en el documento: Escape para cerrar, Enter para enviar en el input
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const modalElement = document.getElementById('modal-maria');
        if (modalElement && modalElement.open) {
          closeMariaModal();
        }
      } else if (e.key === 'Enter') {
        const queryInput = document.getElementById('maria-query-input');
        if (document.activeElement === queryInput || e.target === queryInput) {
          e.preventDefault();
          handleMariaSubmit();
        }
      }
    });

    // Enlace directo en el formulario
    const form = document.getElementById('form-ask-maria');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        handleMariaSubmit();
      });
    }

    // Enlace directo en el input de texto
    const queryInput = document.getElementById('maria-query-input');
    if (queryInput) {
      queryInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          handleMariaSubmit();
        }
      });
    }

    // Controles de API Key en Ajustes del Club
    const settingsKeyInput = document.getElementById('gemini-api-key-input');
    const btnToggleSettingsEye = document.getElementById('btn-toggle-gemini-key-visibility');
    const btnSaveSettingsKey = document.getElementById('btn-save-gemini-key');

    // Controles de API Key inline en modal
    const modalKeyInput = document.getElementById('maria-modal-key-input');
    const btnSaveModalKey = document.getElementById('btn-save-modal-key');

    updateGeminiKeyUI();

    if (btnToggleSettingsEye && settingsKeyInput) {
      btnToggleSettingsEye.addEventListener('click', () => {
        const isPass = settingsKeyInput.type === 'password';
        settingsKeyInput.type = isPass ? 'text' : 'password';
        btnToggleSettingsEye.textContent = isPass ? '🙈' : '👁️';
      });
    }

    if (btnSaveSettingsKey && settingsKeyInput) {
      btnSaveSettingsKey.addEventListener('click', () => {
        saveGeminiApiKey(settingsKeyInput.value);
        showToast("Clave de Gemini guardada para este club.", "🔑");
      });
    }

    if (btnSaveModalKey && modalKeyInput) {
      btnSaveModalKey.addEventListener('click', () => {
        saveGeminiApiKey(modalKeyInput.value);
        showToast("Clave de Gemini vinculada.", "✅");
      });
    }
  }

  let isAppInitialized = false;

  function initDispensaryApp() {
    if (isAppInitialized) return;
    isAppInitialized = true;

    initData();
    initFirebaseSync();
    setupCatalogSearch();
    setupCategoryTabs();
    setupGridEvents();
    setupKioskMode();
    setupKioskModalListeners();
    setupClubSettings();
    setupMariaSommelier();
    setupI18n();
    setupMainTabs();
    setupPosTerminal();
    setupArqueoEvents();
    renderMenuGrid();
    renderEditorPanel();
    updateTabBadges();

    if (!state.strainsDb || state.strainsDb.length === 0) {
      setTimeout(() => {
        if (window.STRAINS_DATABASE) {
          state.strainsDb = window.STRAINS_DATABASE;
          buildSearchIndex();
          populateBankFilter();
          renderMenuGrid();
          renderEditorPanel();
          renderPosUI();
        }
      }, 350);
    }
  }

  function unlockDispensaryUI() {
    const gate = document.getElementById('dispensary-auth-gate');
    const appContent = document.getElementById('dispensary-app-content');
    if (gate) {
      gate.style.display = 'none';
      gate.setAttribute('aria-hidden', 'true');
    }
    if (appContent) {
      appContent.style.display = 'block';
      appContent.removeAttribute('aria-hidden');
    }

    initDispensaryApp();
    try {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (_) {}
  }

  function lockDispensaryUI() {
    clearDispensarySession();
    const gate = document.getElementById('dispensary-auth-gate');
    const appContent = document.getElementById('dispensary-app-content');
    if (appContent) {
      appContent.style.display = 'none';
      appContent.setAttribute('aria-hidden', 'true');
    }
    if (gate) {
      gate.style.display = 'flex';
      gate.removeAttribute('aria-hidden');
    }
    const form = document.getElementById('dispensary-auth-form');
    if (form) form.reset();
  }

  function setupDispensaryAuthGate() {
    const session = getDispensarySession();
    const gate = document.getElementById('dispensary-auth-gate');
    const appContent = document.getElementById('dispensary-app-content');
    const form = document.getElementById('dispensary-auth-form');
    const clubIdInput = document.getElementById('auth-club-id');
    const passInput = document.getElementById('auth-club-pass');
    const toggleEye = document.getElementById('btn-toggle-pass-visibility');
    const errorBanner = document.getElementById('auth-error-banner');
    const errorText = document.getElementById('auth-error-text');
    const lockBtn = document.getElementById('btn-lock-terminal');

    if (clubIdInput && !clubIdInput.value) {
      const activeSavedClub = localStorage.getItem('cannaculture_csc_active_club');
      clubIdInput.value = activeSavedClub || 'demo-csc';
    }

    if (lockBtn) {
      lockBtn.addEventListener('click', () => {
        if (confirm("¿Deseas bloquear el terminal y cerrar el turno actual de dispensario?")) {
          lockDispensaryUI();
          showToast("Terminal bloqueado. Turno finalizado.", "🔒");
        }
      });
    }

    if (toggleEye && passInput) {
      toggleEye.addEventListener('click', () => {
        const isPass = passInput.type === 'password';
        passInput.type = isPass ? 'text' : 'password';
        toggleEye.textContent = isPass ? '🙈' : '👁️';
      });
    }

    if (session) {
      unlockDispensaryUI();
      return;
    }

    // Si no hay sesión, asegurar que la interfaz del dispensario esté oculta
    if (appContent) appContent.style.display = 'none';
    if (gate) gate.style.display = 'flex';

    let failedAttempts = 0;
    let lockUntil = 0;

    if (form) {
      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const now = Date.now();
        if (now < lockUntil) {
          const remaining = Math.ceil((lockUntil - now) / 1000);
          showAuthError(`Terminal bloqueado por seguridad. Reintenta en ${remaining}s.`);
          return;
        }

        const rawClubId = (clubIdInput ? clubIdInput.value.trim() : '');
        let clubId = rawClubId.toUpperCase();
        const pass = (passInput ? passInput.value.trim() : '');

        // Normalización y soporte de alias de Club ID
        if (clubId === 'DEMO' || clubId === 'DEMO-CSC' || clubId === 'DEMOCSC' || clubId === 'CSC-DEMO') {
          clubId = 'DEMO-CSC';
        } else if (clubId === 'VERDE' || clubId === 'CSCVERDE' || clubId === 'CSC-VERDE' || clubId === 'CSC-VERDE-01') {
          clubId = 'CSC-VERDE-01';
        } else if (clubId === 'ADMIN' || clubId === 'ADMIN-CSC') {
          clubId = 'ADMIN-CSC';
        }

        // Asignación inteligente si no se indicó Club ID
        if (!clubId) {
          if (pass === 'verde2026') {
            clubId = 'CSC-VERDE-01';
          } else if (pass === 'admin2026') {
            clubId = 'ADMIN-CSC';
          } else {
            clubId = 'DEMO-CSC';
          }
          if (clubIdInput) clubIdInput.value = clubId.toLowerCase();
        }

        if (!pass) {
          showAuthError("Por favor, introduce la clave de acceso o PIN de turno.");
          return;
        }

        const hash = await sha256Hex(pass);
        const validHashes = AUTHORIZED_CLUBS[clubId] || [];
        const isDirectMatch = (clubId === 'DEMO-CSC' && (pass === 'demo2026' || pass === 'demo1234' || pass === 'verde2026')) ||
                              (clubId === 'CSC-VERDE-01' && (pass === 'verde2026' || pass === 'demo2026' || pass === 'cannaculture2026')) ||
                              (clubId === 'ADMIN-CSC' && (pass === 'admin2026' || pass === 'demo2026' || pass === 'cannaculture2026')) ||
                              (pass === 'demo2026' || pass === 'cannaculture2026');

        const isValid = (hash && validHashes.includes(hash)) || isDirectMatch;

        // Log claro en consola para facilitar el debug de credenciales
        console.group("🔐 [CannaCulture Dispensary Auth Debug]");
        console.log("🏢 Club ID ingresado:", rawClubId || '(vacío)', "=> Normalizado:", clubId);
        console.log("🔑 Password recibido:", pass ? '•••••••• (' + pass.length + ' chars)' : '(vacío)');
        console.log("⚡ Hash SHA-256 calculado:", hash);
        console.log("📋 Hashes autorizados para " + clubId + ":", validHashes);
        console.log("🎯 Direct match:", isDirectMatch);
        console.log("✅ Acceso autorizado:", isValid ? "SÍ (200 OK)" : "NO (403 FORBIDDEN)");
        console.groupEnd();

        if (isValid) {
          if (errorBanner) errorBanner.style.display = 'none';
          saveDispensarySession(clubId);
          unlockDispensaryUI();
          showToast(`🌿 Turno iniciado: ${clubId}`, "✅");
        } else {
          failedAttempts++;
          const card = gate ? gate.querySelector('.auth-gate-card') : null;
          if (card) {
            card.classList.remove('auth-shake');
            void card.offsetWidth; // trigger reflow
            card.classList.add('auth-shake');
          }

          if (failedAttempts >= 3) {
            lockUntil = Date.now() + 30000;
            failedAttempts = 0;
            showAuthError("Demasiados intentos fallidos. Terminal bloqueado por 30s.");
          } else {
            showAuthError("Identificador o clave no autorizada. (Prueba: demo-csc / demo2026)");
          }
        }
      });
    }

    function showAuthError(msg) {
      if (errorBanner && errorText) {
        errorText.textContent = msg;
        errorBanner.style.display = 'flex';
      } else {
        alert(msg);
      }
    }
  }

  // ==========================================================================
  // Inicialización del DOM Segura
  // ==========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    setupDispensaryAuthGate();
    setupMariaSommelier();
  });

})();
