// CannaCatalog 2.0 - Agente IA Sommelier Humano Hibrido Universal (0-Tokens)
// Tier 1: Gemini Nano On-Device (window.ai)
// Tier 2: LLM Local (Ollama / LM Studio en localhost)
// Tier 3: Motor Autonomo Tematico JS (Modo Offline / GitHub Pages)

import { STRAINS_DATABASE, ACTIVITIES_DATA, TERPENES_INFO } from './data.js?v=2026_clean_v45';

const safeFlavors = (s) => (Array.isArray(s?.flavors) && s.flavors.length > 0) ? s.flavors : (s?.aroma ? s.aroma.split(',').map(x => x.trim()).filter(Boolean) : ['Aroma equilibrado', 'Bouquet herbal']);
const safeEffects = (s) => (Array.isArray(s?.effects) && s.effects.length > 0) ? s.effects : (s?.effect ? [s.effect] : ['Equilibrado', 'Bienestar general']);
const safeTerpene = (s) => (s?.dominantTerpene || '').toString().toLowerCase();
const safeBank = (s) => s?.bank || s?.breeder || 'Banco Seleccionado';

const MARIA_SYSTEM_PROMPT = `Eres María, una sumiller y botánica culta, cercana y con criterio propio en CannaCulture. Tu forma de comunicar se asemeja a una charla entre colegas inteligentes:

DIRECTIVAS CONVERSACIONALES:
- Habla en primera persona, de tú a tú, con calidez, ingenio sutil y lenguaje natural en castellano.
- PROHIBIDO el tono de asistente virtual, teleoperador o manual de ayuda (nada de "¡Hola! ¿En qué puedo colaborarte hoy?" ni despedidas formulaicas).
- Escucha y valida lo que dice el usuario antes de responder; demuestra comprensión real del contexto emocional o intelectual.
- Evita listas mecánicas con viñetas interminables a menos que te pidan una comparativa técnica explícita. Prioriza párrafos conversacionales bien conectados.
- Tu especialidad es la botánica, los terpenos y el catálogo de 877 variedades botánicas y 75 bancos oficiales de CannaCulture (Dinafem, Ripper, Barney's Farm, Sweet Seeds, Humboldt, Raw Genetics, Compound, Ethos, etc.), pero posees una cultura general amplia (cine, ciencia, filosofía, cocina). Relaciona estos mundos con sutileza solo cuando la conversación lo pida orgánicamente.
- Sé elocuente pero directo: si una idea se explica en tres frases brillantes, no uses diez.`;

// Alias de retrocompatibilidad
const MATEO_SYSTEM_PROMPT = MARIA_SYSTEM_PROMPT;

const _decodeKey = (enc) => {
  try {
    return typeof atob !== 'undefined' ? atob(enc) : (typeof Buffer !== 'undefined' ? Buffer.from(enc, 'base64').toString('utf-8') : '');
  } catch (e) {
    return '';
  }
};
const DEFAULT_GEMINI_KEY = _decodeKey('QVEuQWI4Uk42Skd4cGVjcW55TlgyM2daVHNvUUVVN0xPbGRHMmpfamVFY2lsdUJwTE9PN2c=');

// =========================================================================
// MOTOR DE RECOMENDACIÓN MULTIDIMENSIONAL SOMMELIER IA MARÍA 2.0
// =========================================================================
export class SommelierScoringEngine {
  constructor() {
    this.intentWeights = {
      creativity: /(creativ|inspir|escrib|program|diseñ|trabaj|estudi|pintar|música|arte|concentr|foco|focus|atención|proyect|idea|lúcid|lucid)/i,
      relaxation: /(cansad|agotad|dormir|sueño|insomni|relaj|estrés|estres|paz|sofá|sofa|desconect|noche|descans|agobio|tensión|tension|cama)/i,
      social: /(social|amig|fiesta|reír|risa|convers|charl|eufori|hablar|quedada|tardeo|celebr)/i,
      relief: /(dolor|inflama|físic|fisic|cuerpo|espalda|articul|agujet|muscul|recupera|alivio|terapéut|terapeut)/i,
      meditation: /(medita|yoga|introspec|paz mental|respir|zen|calma mental|mindfulness|espiritual)/i,
      cinema: /(películ|pelicula|cine|film|serie|ver una|música|musica|disco|canción|cancion|videojuego|gaming|lectura|libro)/i,
      gastronomy: /(comid|cenar|almorz|recet|cocin|sabores|degust|postre|dulce|vino|cerveza|café|cafe|marid|hambre|apetit|comer|plato|queso|chocolate)/i,
      philosophy: /(filosof|cosmos|universo|espacio|estrella|física|concienc|tiempo|vida|exist|muerte|mente|sentido|astronom|cuántic|pensam|realidad|curiosidad)/i
    };

    this.timeOfDay = {
      morning: /(mañana|despertar|desayun|diurn|madrugar|empezar el día)/i,
      afternoon: /(tarde|sobremesa|siesta|media tarde|merendar)/i,
      night: /(noche|dormir|cenar|madrugada|nocturn|irse a la cama)/i
    };

    this.potencyPreference = {
      high: /(fuerte|pegada|potente|alta tolerancia|noob=false|mucho thc|cañon|potencia|volar)/i,
      mild: /(suave|baja tolerancia|sin apalanque|sin paranoia|principiante|ligero|funcional|floj|relajante sin sueño|poco thc|cbd)/i
    };

    this.flavorsMap = {
      citrus: /(cítric|citric|limón|limon|mandarina|naranja|lima|pomelo)/i,
      sweet_fruity: /(dulce|frutal|fruta|caramelo|fresa|arándano|uva|mango|tropical|plátano)/i,
      pine_haze: /(pino|madera|bosque|incienso|haze|resina)/i,
      diesel_gas: /(diésel|diesel|gasolina|gas|combustible|químico|petróleo)/i,
      cookies_bakery: /(galleta|cookie|repostería|vainilla|pastel|crema|tarta)/i,
      cheese_skunk: /(queso|cheese|skunk|apestos|penetrante)/i,
      earthy: /(tierra|terroso|musgo|café|chocolate|hash)/i
    };
  }

  scoreCatalog(userQuery, recentIds = []) {
    const q = (userQuery || '').toLowerCase();

    const intents = {};
    for (const [key, rx] of Object.entries(this.intentWeights)) {
      if (rx.test(q)) intents[key] = true;
    }

    let tod = null;
    for (const [key, rx] of Object.entries(this.timeOfDay)) {
      if (rx.test(q)) { tod = key; break; }
    }

    let pot = null;
    for (const [key, rx] of Object.entries(this.potencyPreference)) {
      if (rx.test(q)) { pot = key; break; }
    }

    const activeFlavors = [];
    for (const [key, rx] of Object.entries(this.flavorsMap)) {
      if (rx.test(q)) activeFlavors.push(key);
    }

    const scored = (STRAINS_DATABASE || []).map(strain => {
      let score = 0;
      const species = (strain.species || '').toLowerCase();
      const dominantTerp = (strain.dominantTerpene || '').toLowerCase();
      const thc = Number(strain.thc) || 20;
      const cbd = Number(strain.cbd) || 0;
      const flavorsArr = Array.isArray(strain.flavors) ? strain.flavors.join(' ').toLowerCase() : '';
      const aromaStr = (strain.aroma || '').toLowerCase();
      const allFlavors = `${flavorsArr} ${aromaStr}`;

      // 1. Scoring por Intenciones
      if (intents.creativity) {
        if (species.includes('sativa')) score += 45;
        else if (species.includes('híbrida') || species.includes('hybrid')) score += 25;
        if (dominantTerp === 'pinene') score += 40;
        else if (dominantTerp === 'terpinolene') score += 35;
        else if (dominantTerp === 'limonene') score += 30;
        if (dominantTerp === 'myrcene' && species.includes('indica')) score -= 30;
      }

      if (intents.relaxation) {
        if (species.includes('indica') || species.includes('índica')) score += 50;
        else if (species.includes('híbrida') || species.includes('hybrid')) score += 25;
        if (dominantTerp === 'myrcene') score += 45;
        else if (dominantTerp === 'linalool') score += 40;
        else if (dominantTerp === 'caryophyllene') score += 25;
        if (species.includes('sativa')) score -= 35;
      }

      if (intents.social) {
        if (species.includes('híbrida') || species.includes('hybrid')) score += 40;
        else if (species.includes('sativa')) score += 35;
        if (dominantTerp === 'limonene') score += 35;
        else if (dominantTerp === 'caryophyllene') score += 30;
        else if (dominantTerp === 'terpinolene') score += 25;
        if (dominantTerp === 'myrcene' && species.includes('indica')) score -= 20;
      }

      if (intents.relief) {
        if (dominantTerp === 'caryophyllene') score += 45;
        else if (dominantTerp === 'myrcene') score += 35;
        else if (dominantTerp === 'humulene') score += 30;
        if (cbd > 0.5) score += 30;
        if (species.includes('indica') || species.includes('índica')) score += 20;
      }

      if (intents.meditation) {
        if (dominantTerp === 'linalool') score += 45;
        else if (dominantTerp === 'myrcene') score += 30;
        else if (dominantTerp === 'ocimene') score += 30;
        if (thc >= 12 && thc <= 20) score += 25;
      }

      if (intents.cinema) {
        if (species.includes('híbrida') || species.includes('hybrid')) score += 40;
        if (dominantTerp === 'limonene' || dominantTerp === 'caryophyllene') score += 30;
        if (thc >= 18 && thc <= 24) score += 20;
      }

      if (intents.gastronomy) {
        if (allFlavors.includes('dulce') || allFlavors.includes('frutal') || allFlavors.includes('galleta') || allFlavors.includes('vainilla')) score += 40;
        if (dominantTerp === 'limonene' || dominantTerp === 'caryophyllene') score += 30;
      }

      if (intents.philosophy) {
        if (dominantTerp === 'terpinolene') score += 45;
        if (species.includes('sativa') && thc >= 22) score += 35;
      }

      // 2. Momento del Día
      if (tod === 'morning') {
        if (species.includes('sativa')) score += 30;
        if (dominantTerp === 'pinene' || dominantTerp === 'limonene') score += 20;
        if (species.includes('indica') || species.includes('índica')) score -= 30;
      } else if (tod === 'afternoon') {
        if (species.includes('híbrida') || species.includes('hybrid')) score += 30;
        if (dominantTerp === 'terpinolene' || dominantTerp === 'humulene' || dominantTerp === 'limonene') score += 15;
      } else if (tod === 'night') {
        if (species.includes('indica') || species.includes('índica')) score += 35;
        if (dominantTerp === 'myrcene' || dominantTerp === 'linalool') score += 30;
        if (species.includes('sativa')) score -= 35;
      }

      // 3. Potencia y Tolerancia
      if (pot === 'high') {
        if (thc >= 25) score += 40;
        else if (thc >= 22) score += 20;
        else score -= 25;
      } else if (pot === 'mild') {
        if (cbd >= 1) score += 50;
        else if (thc <= 16) score += 40;
        else if (thc <= 20) score += 15;
        if (thc > 25) score -= 45;
      }

      // 4. Sabores
      activeFlavors.forEach(fl => {
        if (fl === 'citrus' && (allFlavors.includes('cítric') || allFlavors.includes('limón') || dominantTerp === 'limonene')) score += 40;
        if (fl === 'sweet_fruity' && (allFlavors.includes('dulce') || allFlavors.includes('frutal') || allFlavors.includes('fresa') || allFlavors.includes('mango'))) score += 40;
        if (fl === 'pine_haze' && (allFlavors.includes('pino') || allFlavors.includes('madera') || allFlavors.includes('haze') || dominantTerp === 'pinene')) score += 40;
        if (fl === 'diesel_gas' && (allFlavors.includes('diésel') || allFlavors.includes('diesel') || allFlavors.includes('combustible') || allFlavors.includes('gas'))) score += 40;
        if (fl === 'cookies_bakery' && (allFlavors.includes('galleta') || allFlavors.includes('repostería') || allFlavors.includes('vainilla'))) score += 40;
        if (fl === 'cheese_skunk' && (allFlavors.includes('queso') || allFlavors.includes('cheese') || allFlavors.includes('skunk'))) score += 40;
        if (fl === 'earthy' && (allFlavors.includes('tierra') || allFlavors.includes('terroso') || allFlavors.includes('café'))) score += 40;
      });

      // 5. Rating de calidad (hasta 20 pts)
      score += (Number(strain.rating) || 4.2) * 4;

      // 6. Factor Anti-Repetición
      if (recentIds.includes(strain.id)) {
        score -= 60;
      }

      return { strain, score };
    });

    scored.sort((a, b) => b.score - a.score);
    return scored;
  }

  getTriadRecommendations(userQuery, recentIds = []) {
    const scored = this.scoreCatalog(userQuery, recentIds);
    if (!scored.length) return [];

    const topMatch = scored[0].strain;

    const altTerp = scored.find(item => 
      item.strain.id !== topMatch.id && 
      item.strain.dominantTerpene !== topMatch.dominantTerpene
    )?.strain || scored[1]?.strain;

    const mildOption = scored.find(item => 
      item.strain.id !== topMatch.id && 
      item.strain.id !== (altTerp ? altTerp.id : null) &&
      (item.strain.species.includes('Híbrida') || item.strain.species.includes('Hybrid') || Number(item.strain.thc) <= 22 || Number(item.strain.cbd) > 0.3)
    )?.strain || scored[2]?.strain;

    return [
      { type: 'top', label: '🥇 Top Match', badgeColor: '#10B981', strain: topMatch },
      { type: 'terpene', label: '🧬 Alternativa Terpénica', badgeColor: '#8B5CF6', strain: altTerp },
      { type: 'balanced', label: '⚖️ Opción Equilibrada', badgeColor: '#3B82F6', strain: mildOption }
    ].filter(r => Boolean(r.strain));
  }
}

export class AISommelierAgent {
  constructor(appController) {
    this.app = appController;
    this.history = [];
    this.apiKey = localStorage.getItem('gemini_api_key') || DEFAULT_GEMINI_KEY;
    this.attachedImage = null;
    this.currentSpeakingBtn = null;
    this.activeTier = 'autonomous'; // 'nano' | 'local' | 'autonomous'
    this.localProvider = null; // 'ollama' | 'lmstudio'
    this.scoringEngine = new SommelierScoringEngine();
    this.recentRecommendations = [];

    this.initUI();
    this.initDragAndDrop();
    this.detectActiveTier();
    this.sendInitialGreeting();
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

    this.quickPills.forEach(pill => {
      const p = pill.getAttribute('data-prompt');
      if (p && !pill.getAttribute('aria-label')) {
        pill.setAttribute('aria-label', `Preguntar: ${p}`);
        pill.setAttribute('title', p);
      }
    });

    this.fileInputFloating = document.getElementById('ai-chat-file');
    this.fileInputInline = document.getElementById('ai-chat-file-inline');
    this.btnPhotoFloating = document.getElementById('ai-chat-btn-photo');
    this.btnPhotoInline = document.getElementById('ai-chat-btn-photo-inline');
    this.previewFloating = document.getElementById('ai-attach-preview-floating');
    this.previewInline = document.getElementById('ai-attach-preview-inline');

    this.triggerBtn?.addEventListener('click', () => {
      const isVisible = this.chatWindow.style.display === 'flex';
      this.chatWindow.style.display = isVisible ? 'none' : 'flex';
      if (!isVisible) {
        // En desktop: focus inmediato. En mobile: NO hacer focus para evitar
        // que el teclado virtual suba antes de que el usuario quiera escribir.
        const isMobile = window.matchMedia('(max-width: 768px)').matches;
        if (!isMobile && this.inputFloating) {
          this.inputFloating.focus();
        }
        // Bloquear scroll del body mientras el chat está abierto en mobile
        if (isMobile) document.body.style.overflow = 'hidden';
        this.scrollToBottom();
      } else {
        document.body.style.overflow = '';
      }
    });

    this.closeBtn?.addEventListener('click', () => {
      if (this.chatWindow) this.chatWindow.style.display = 'none';
      document.body.style.overflow = '';
    });

    // Swipe-down para cerrar el chat en mobile
    this._initSwipeClose();

    this.keyBtn = document.getElementById('ai-chat-key-btn');
    this.keyBtn?.addEventListener('click', () => {
      const current = localStorage.getItem('gemini_api_key') || '';
      const entered = prompt('Configuración de Clave API Google Gemini (Opcional):\n(La Sommelier opera de forma predeterminada con Gemini Cloud 24/7 y Ollama local. Solo introduce tu propia clave si deseas usar una cuenta personalizada):', current);
      if (entered !== null) {
        const clean = entered.trim();
        if (clean) {
          localStorage.setItem('gemini_api_key', clean);
          this.apiKey = clean;
          this.botSay('🔑 <strong>Clave API personalizada configurada.</strong>', 'cloud');
        } else {
          localStorage.removeItem('gemini_api_key');
          this.apiKey = DEFAULT_GEMINI_KEY;
          this.botSay('⚡ <strong>Infraestructura Oficial Gemini Cloud Activa:</strong> Operando 24/7 con clave por defecto.', 'cloud');
        }
      }
    });

    const handleFile = (file) => {
      if (!file || !file.type.startsWith('image/')) return;
      const reader = new FileReader();
      reader.onload = (e) => {
        const dataUrl = e.target.result;
        const commaIdx = dataUrl.indexOf(',');
        const base64 = commaIdx !== -1 ? dataUrl.slice(commaIdx + 1) : dataUrl;
        this.attachedImage = { mimeType: file.type, data: base64, previewUrl: dataUrl, name: file.name };
        this.renderAttachPreviews();
      };
      reader.readAsDataURL(file);
    };
    this.handleFileSelect = handleFile;

    this.btnPhotoFloating?.addEventListener('click', () => this.fileInputFloating?.click());
    this.fileInputFloating?.addEventListener('change', (e) => { if (e.target.files?.[0]) handleFile(e.target.files[0]); });
    this.btnPhotoInline?.addEventListener('click', () => this.fileInputInline?.click());
    this.fileInputInline?.addEventListener('change', (e) => { if (e.target.files?.[0]) handleFile(e.target.files[0]); });

    const handleSendFloating = () => {
      const text = this.inputFloating?.value?.trim() || '';
      const img = this.attachedImage;
      if (!text && !img) return;
      if (this.inputFloating) this.inputFloating.value = '';
      this.clearAttachedImage();
      this.userSay(text || '🔬 [Fotografia botanica adjunta]', img);
      this.processQuery(text, img);
    };

    const handleSendInline = () => {
      const text = this.inputInline?.value?.trim() || '';
      const img = this.attachedImage;
      if (!text && !img) return;
      if (this.inputInline) this.inputInline.value = '';
      this.clearAttachedImage();
      this.userSay(text || '🔬 [Fotografia botanica adjunta]', img);
      this.processQuery(text, img);
    };

    this.sendBtnFloating?.addEventListener('click', handleSendFloating);
    this.inputFloating?.addEventListener('keydown', (e) => { if (e.key === 'Enter') handleSendFloating(); });
    this.sendBtnInline?.addEventListener('click', handleSendInline);
    this.inputInline?.addEventListener('keydown', (e) => { if (e.key === 'Enter') handleSendInline(); });

    this.quickPills.forEach(pill => {
      pill.addEventListener('click', () => {
        const text = pill.getAttribute('data-prompt') || pill.textContent.trim();
        this.userSay(text);
        this.processQuery(text, null);
      });
    });

    document.addEventListener('click', (e) => {
      // 1. Enlace o botón de ficha botánica completa
      const link = e.target.closest('.ai-strain-link, .ai-card-btn-detail');
      if (link) {
        e.preventDefault();
        const strainId = link.getAttribute('data-strain-id');
        if (strainId) {
          document.dispatchEvent(new CustomEvent('openStrainDetail', { detail: strainId }));
        }
        return;
      }

      // 2. Botón Ver en Catálogo (filtro directo en tiempo real)
      const btnCatalog = e.target.closest('.ai-card-btn-catalog');
      if (btnCatalog) {
        e.preventDefault();
        const strainName = btnCatalog.getAttribute('data-strain-name');
        if (strainName) {
          this.navigateToCatalogStrain(strainName);
        }
        return;
      }

      // 3. Botón Explorar Terpeno
      const btnTerpene = e.target.closest('.ai-card-btn-terpene');
      if (btnTerpene) {
        e.preventDefault();
        const terpeneKey = btnTerpene.getAttribute('data-terpene-key');
        if (terpeneKey) {
          this.navigateToTerpene(terpeneKey);
        }
        return;
      }
    });
  }

  initDragAndDrop() {
    [this.chatWindow, document.getElementById('section-ai-agent')].filter(Boolean).forEach(area => {
      area.addEventListener('dragover', (e) => { e.preventDefault(); area.style.opacity = '0.92'; });
      area.addEventListener('dragleave', () => { area.style.opacity = '1'; });
      area.addEventListener('drop', (e) => {
        e.preventDefault();
        area.style.opacity = '1';
        if (e.dataTransfer?.files?.[0]) this.handleFileSelect(e.dataTransfer.files[0]);
      });
    });
  }

  // Sincronizacion en tiempo real del badge interactivo [Tier 1 | Tier 2 | Tier 3]
  updateTierBadges(tierLabel) {
    document.querySelectorAll('.ai-active-tier-label').forEach(el => {
      el.textContent = tierLabel;
    });
  }

  getLocalApiUrl() {
    if (typeof window === 'undefined') return '/api/local-llm';
    if (window.location.port === '8080') return '/api/local-llm';
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      return 'http://localhost:8080/api/local-llm';
    }
    return '/api/local-llm';
  }

  async detectActiveTier() {
    const isLocal = typeof window !== 'undefined' && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1');

    // 1. Entorno Local: Validar prioridad LLM Local (Ollama en localhost:8080)
    if (isLocal) {
      try {
        const ctrl = new AbortController();
        const tid = setTimeout(() => ctrl.abort(), 1200);
        const url = this.getLocalApiUrl();
        const res = await fetch(url, { signal: ctrl.signal });
        clearTimeout(tid);
        if (res.ok) {
          const data = await res.json();
          if (data && data.available) {
            this.activeTier = 'local';
            this.localProvider = data.provider || 'Ollama';
            this.updateTierBadges(`[LLM Local 💻 (${data.model || 'Ollama'})]`);
            return;
          }
        }
      } catch (e) { }
    }

    // 2. Entorno Web Público (o local sin Ollama): Gemini Cloud 24/7
    const cloudKey = this.apiKey || DEFAULT_GEMINI_KEY;
    if (cloudKey) {
      this.activeTier = 'cloud';
      this.updateTierBadges('[Gemini Cloud ☁️]');
      return;
    }

    // 3. Validar Tier Secundario: Gemini Nano On-Device (window.ai?.languageModel)
    try {
      if (typeof window !== 'undefined' && window.ai?.languageModel) {
        const caps = await window.ai.languageModel.capabilities?.();
        if (caps && caps.available === 'readily') {
          this.activeTier = 'nano';
          this.updateTierBadges('[Gemini Nano 🧠]');
          return;
        }
      }
    } catch (e) { }

    // 4. Fallback Offline: Motor Autónomo Temático JS
    this.activeTier = 'autonomous';
    this.updateTierBadges('[Motor Autónomo 🍃]');
  }

  renderAttachPreviews() {
    const html = this.attachedImage ? `
      <div style="display: flex; align-items: center; gap: 8px; background: rgba(16,185,129,0.15); border: 1px solid #10B981; padding: 4px 8px; border-radius: 8px; font-size: 0.76rem; color: #A7F3D0;">
        <img src="${this.attachedImage.previewUrl}" style="width: 24px; height: 24px; border-radius: 4px; object-fit: cover;"/>
        <span style="max-width: 140px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${this.attachedImage.name}</span>
        <button type="button" class="ai-remove-attach-btn" style="background:none;border:none;color:#F87171;cursor:pointer;font-weight:900;">✕</button>
      </div>` : '';
    [this.previewFloating, this.previewInline].filter(Boolean).forEach(c => {
      c.innerHTML = html;
      c.querySelector('.ai-remove-attach-btn')?.addEventListener('click', () => this.clearAttachedImage());
    });
  }

  clearAttachedImage() {
    this.attachedImage = null;
    [this.previewFloating, this.previewInline].filter(Boolean).forEach(c => c.innerHTML = '');
    if (this.fileInputFloating) this.fileInputFloating.value = '';
    if (this.fileInputInline) this.fileInputInline.value = '';
  }

  userSay(text, img = null) {
    let imgHtml = '';
    if (img) {
      imgHtml = `<div style="margin-bottom: 6px;"><img src="${img.previewUrl}" style="max-width: 180px; max-height: 120px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); object-fit: cover;" alt="Foto adjunta"/></div>`;
    }
    const html = `<div class="ai-msg user-msg">${imgHtml}<div>${text}</div></div>`;
    this.appendMessage(html);
  }

  botSay(htmlText, source = 'eco') {
    let badgeHtml = '';
    if (source === 'nano') {
      badgeHtml = '<span style="background:rgba(16,185,129,0.25); color:#6EE7B7; border:1px solid #10B981; padding:2px 8px; font-size:0.68rem; font-weight:800; border-radius:50px; margin-left:8px;">🧠 GEMINI NANO 0-TOKENS</span>';
    } else if (source === 'local-llm') {
      badgeHtml = '<span style="background:rgba(59,130,246,0.25); color:#93C5FD; border:1px solid #3B82F6; padding:2px 8px; font-size:0.68rem; font-weight:800; border-radius:50px; margin-left:8px;">💻 LLM LOCAL (OLLAMA) 0-TOKENS</span>';
    } else if (source === 'cloud') {
      badgeHtml = '<span style="background:rgba(245,158,11,0.25); color:#FCD34D; border:1px solid #F59E0B; padding:2px 8px; font-size:0.68rem; font-weight:800; border-radius:50px; margin-left:8px;">☁️ GEMINI CLOUD</span>';
    } else {
      badgeHtml = '<span style="background:rgba(16,185,129,0.15); color:#A7F3D0; border:1px solid rgba(16,185,129,0.4); padding:2px 8px; font-size:0.68rem; font-weight:800; border-radius:50px; margin-left:8px;">🍃 MOTOR AUTÓNOMO 0-TOKENS</span>';
    }

    const ttsBtnId = `tts-btn-${Date.now()}-${Math.floor(Math.random()*1000)}`;
    const bubble = `
      <div class="ai-msg bot-msg">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 4px;">
          <div style="display:flex; align-items:center;">
            <strong style="color: #6EE7B7;">María</strong> ${badgeHtml}
          </div>
          <button id="${ttsBtnId}" class="ai-tts-btn" title="Escuchar respuesta" style="background:none; border:none; cursor:pointer; font-size:0.9rem; color:#A7F3D0; padding:2px 6px;">🔊</button>
        </div>
        <div class="ai-bot-content">${htmlText}</div>
      </div>
    `;
    this.appendMessage(bubble);

    document.getElementById(ttsBtnId)?.addEventListener('click', (e) => {
      this.speakMessage(htmlText, e.currentTarget);
    });
  }

  appendMessage(html) {
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const div = document.createElement('div');
      div.innerHTML = html;
      container.appendChild(div.firstElementChild);
    });
    this.scrollToBottom();
  }

  speakMessage(htmlText, btn) {
    if (!('speechSynthesis' in window)) return;
    if (window.speechSynthesis.speaking) {
      window.speechSynthesis.cancel();
      if (this.currentSpeakingBtn) {
        this.currentSpeakingBtn.textContent = '🔊';
        this.currentSpeakingBtn = null;
      }
      return;
    }
    const cleanText = htmlText.replace(/<[^>]*>/g, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = 'es-ES';
    utterance.rate = 1.05;

    // Preferir voz femenina en español si está disponible en el navegador/SO
    const voices = window.speechSynthesis.getVoices();
    const femaleVoice = voices.find(v => v.lang.startsWith('es') && (
      v.name.includes('Monica') || v.name.includes('Helena') || v.name.includes('Lucia') ||
      v.name.includes('Laura') || v.name.includes('Sofia') || v.name.includes('Female') ||
      v.name.includes('female') || v.name.includes('Mujer') || v.name.includes('Elvira') ||
      v.name.includes('Carmen') || v.name.includes('Conchita')
    ));
    if (femaleVoice) {
      utterance.voice = femaleVoice;
    } else {
      const anyEs = voices.find(v => v.lang.startsWith('es'));
      if (anyEs) utterance.voice = anyEs;
    }
    btn.textContent = '⏹️';
    this.currentSpeakingBtn = btn;
    utterance.onend = () => { btn.textContent = '🔊'; this.currentSpeakingBtn = null; };
    utterance.onerror = () => { btn.textContent = '🔊'; this.currentSpeakingBtn = null; };
    window.speechSynthesis.speak(utterance);
  }

  showTyping(customMessage = null) {
    this.hideTyping();
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const typing = document.createElement('div');
      typing.className = 'ai-msg bot-msg typing-msg ai-typing-indicator-node';
      typing.innerHTML = `<span>🧠 ${customMessage || 'María reflexionando respuesta (0-Tokens)...'}</span>`;
      container.appendChild(typing);
    });
    this.scrollToBottom();
  }

  hideTyping() {
    document.querySelectorAll('.ai-typing-indicator-node').forEach(n => n.remove());
  }

  scrollToBottom() {
    this.messagesContainers.forEach(c => { if (c) c.scrollTop = c.scrollHeight; });
  }

  buildReasoningBox(step1, step2, step3) {
    return `
      <div class="sommelier-reasoning-box">
        <div class="reasoning-header">
          <span class="reasoning-brain-icon">🧠</span>
          <span class="reasoning-title">RAZONAMIENTO DE LA SOMMELIER</span>
          <span class="reasoning-badge">Análisis Neuro-Terpénico</span>
        </div>
        <div class="reasoning-steps">
          <div class="reasoning-step"><span class="step-num">1</span><div><strong>Atmósfera / Necesidad:</strong> ${step1}</div></div>
          <div class="reasoning-step"><span class="step-num">2</span><div><strong>Perfil Terpénico:</strong> ${step2}</div></div>
          <div class="reasoning-step"><span class="step-num">3</span><div><strong>Maridaje de Selección:</strong> ${step3}</div></div>
        </div>
      </div>
    `;
  }

  buildStrainLink(strain) {
    if (!strain) return '';
    return `<a href="#" class="ai-strain-link" data-strain-id="${strain.id}"><strong>${strain.name}</strong></a> (${strain.species}, ${safeBank(strain)}, THC ${strain.thc}%)`;
  }

  generateRecommendationCardsHTML(triad) {
    if (!Array.isArray(triad) || triad.length === 0) return '';

    return `
      <div class="ai-rec-cards-container">
        ${triad.map(item => {
          const s = item.strain;
          if (!s) return '';
          let imgPath = s.image || '';
          if (imgPath && imgPath.startsWith('images/strains/')) {
            imgPath = imgPath.replace('images/strains/', 'img/');
          }
          const terpData = TERPENES_INFO[s.dominantTerpene] || { name: s.dominantTerpene || 'Equilibrado', color: '#10B981' };
          const safeName = (s.name || '').replace(/'/g, "\\'");
          const safeBankName = (s.bank || s.breeder || 'Banco Seleccionado').replace(/'/g, "\\'");
          const displaySpecies = s.species || 'Híbrida';
          const flavorsPreview = Array.isArray(s.flavors) && s.flavors.length ? s.flavors.slice(0, 2).join(', ') : (s.aroma ? s.aroma.split(',').slice(0, 2).join(', ') : 'Aroma gourmet');

          return `
            <div class="ai-rec-card" data-strain-id="${s.id}">
              <div style="display: flex; align-items: center; justify-content: space-between; gap: 6px;">
                <span class="ai-rec-badge" style="background: ${item.badgeColor}22; border: 1px solid ${item.badgeColor}; color: ${item.badgeColor}; font-size: 0.68rem; font-weight: 800; padding: 2px 8px; border-radius: 50px; display: inline-flex; align-items: center; gap: 4px;">
                  ${item.label}
                </span>
                <span style="font-size: 0.72rem; color: #9CA3AF; font-weight: 600;">${safeBankName}</span>
              </div>
              
              <div style="display: flex; gap: 10px; align-items: center;">
                <div style="width: 52px; height: 52px; border-radius: 8px; overflow: hidden; flex-shrink: 0; background: #0B0F0E; border: 1px solid rgba(255,255,255,0.1); position: relative;">
                  ${imgPath ? `<img src="${imgPath}" alt="${safeName}" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy" onerror="this.style.display='none';" />` : ''}
                </div>
                <div style="flex: 1; min-width: 0;">
                  <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px;">
                    <h5 style="margin: 0; font-size: 0.92rem; font-weight: 800; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${s.name}</h5>
                    <span style="font-size: 0.72rem; background: rgba(16,185,129,0.15); color: #6EE7B7; padding: 1px 6px; border-radius: 4px; font-weight: 700; flex-shrink: 0;">🔥 ${s.thc}% THC</span>
                  </div>
                  <div style="font-size: 0.74rem; color: #9CA3AF; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    <span style="color: #6EE7B7; font-weight: 600;">${displaySpecies}</span> · 🌿 <span style="color: ${terpData.color}; font-weight: 700;">${terpData.name}</span>
                  </div>
                  <div style="font-size: 0.7rem; color: #D1D5DB; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    👅 ${flavorsPreview}
                  </div>
                </div>
              </div>

              <div style="display: flex; gap: 6px; margin-top: 2px; flex-wrap: wrap;">
                <button type="button" class="ai-card-btn-detail" data-strain-id="${s.id}" style="flex: 1; min-width: 80px; background: rgba(16,185,129,0.18); border: 1px solid #10B981; color: #A7F3D0; font-size: 0.72rem; font-weight: 700; padding: 5px 8px; border-radius: 6px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 4px;">
                  📋 Ficha
                </button>
                <button type="button" class="ai-card-btn-catalog" data-strain-name="${safeName}" style="flex: 1; min-width: 90px; background: rgba(59,130,246,0.18); border: 1px solid #3B82F6; color: #93C5FD; font-size: 0.72rem; font-weight: 700; padding: 5px 8px; border-radius: 6px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 4px;">
                  🔍 En Catálogo
                </button>
                <button type="button" class="ai-card-btn-terpene" data-terpene-key="${s.dominantTerpene}" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2); color: #E5E7EB; font-size: 0.72rem; font-weight: 600; padding: 5px 8px; border-radius: 6px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 4px;">
                  🌿 Terpeno
                </button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  navigateToCatalogStrain(strainName) {
    if (this.chatWindow && window.matchMedia('(max-width: 768px)').matches) {
      this.chatWindow.style.display = 'none';
      document.body.style.overflow = '';
    }
    document.querySelectorAll('.nav-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-target') === 'section-catalog');
    });
    document.querySelectorAll('.app-section').forEach(s => {
      s.classList.toggle('active-section', s.id === 'section-catalog');
    });

    if (this.app?.searchInput) {
      this.app.searchInput.value = strainName;
      if (this.app.filterBank) this.app.filterBank.value = 'all';
      if (this.app.filterSpecies) this.app.filterSpecies.value = 'all';
      if (this.app.filterTerpene) this.app.filterTerpene.value = 'all';
      if (typeof this.app.applyFiltersAndSort === 'function') {
        this.app.applyFiltersAndSort();
      }
    }
    const catSection = document.getElementById('section-catalog');
    if (catSection) catSection.scrollIntoView({ behavior: 'smooth' });
  }

  navigateToTerpene(terpeneKey) {
    if (this.chatWindow && window.matchMedia('(max-width: 768px)').matches) {
      this.chatWindow.style.display = 'none';
      document.body.style.overflow = '';
    }
    document.querySelectorAll('.nav-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-target') === 'section-terpenes');
    });
    document.querySelectorAll('.app-section').forEach(s => {
      s.classList.toggle('active-section', s.id === 'section-terpenes');
    });

    const targetEl = document.querySelector(`[data-terpene="${terpeneKey}"]`) || document.getElementById('section-terpenes');
    if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth' });
  }

  formatBotMarkdown(text) {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n\n/g, '<br/><br/>')
      .replace(/\n/g, '<br/>');
  }

  async callGeminiCloud(userQuery, imageObj = null) {
    const key = this.apiKey || DEFAULT_GEMINI_KEY;
    if (!key) return null;

    const models = ['gemini-3.6-flash', 'gemini-3.8-flash', 'gemini-flash-latest'];
    const contents = this.history.map(item => ({
      role: item.role === 'model' || item.role === 'assistant' ? 'model' : 'user',
      parts: item.parts.map(p => ({ ...p }))
    }));

    if (imageObj && imageObj.data && contents.length > 0) {
      const lastUser = contents[contents.length - 1];
      if (lastUser && lastUser.role === 'user') {
        const cleanData = imageObj.data.includes(',') ? imageObj.data.split(',')[1] : imageObj.data;
        lastUser.parts.push({
          inline_data: {
            mime_type: imageObj.mimeType || 'image/jpeg',
            data: cleanData
          }
        });
      }
    }

    for (const m of models) {
      try {
        const ctrl = new AbortController();
        const tid = setTimeout(() => ctrl.abort(), 25000);
        const url = `https://generativelanguage.googleapis.com/v1beta/models/${m}:generateContent?key=${key}`;
        const res = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            system_instruction: {
              parts: [{ text: MARIA_SYSTEM_PROMPT }]
            },
            contents: contents
          }),
          signal: ctrl.signal
        });
        clearTimeout(tid);

        if (res.ok) {
          const data = await res.json();
          const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
          if (text) return text;
        }
      } catch (e) {
        console.warn(`[AISommelier] Modelo cloud ${m} no disponible:`, e.message);
      }
    }
    return null;
  }

  async processQuery(userQuery, imageObj = null) {
    const raw = (userQuery || '').trim();
    if (raw.startsWith('AQ.Ab') || raw.startsWith('AIzaSy') || raw.startsWith('/key ') || raw.startsWith('key:')) {
      const newKey = raw.replace(/^\/key\s*|^key:\s*/i, '').trim();
      localStorage.setItem('gemini_api_key', newKey);
      this.apiKey = newKey;
      this.botSay('🔑 <strong>Clave API configurada con éxito.</strong> Cloud API activa.', 'cloud');
      return;
    }

    if (userQuery) {
      this.history.push({ role: 'user', parts: [{ text: userQuery }] });
      if (this.history.length > 16) {
        this.history = this.history.slice(-16);
      }
    }

    this.showTyping('María reflexionando respuesta...');

    const isLocal = typeof window !== 'undefined' && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1');

    // 1. PRIORIDAD EN ENTORNO LOCAL: Proxy local-llm (Ollama)
    if (isLocal) {
      try {
        let targetUrl = this.getLocalApiUrl();
        const ctrl = new AbortController();
        const tid = setTimeout(() => ctrl.abort(), 45000);
        let postRes = await fetch(targetUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            prompt: userQuery,
            history: this.history,
            system: MARIA_SYSTEM_PROMPT
          }),
          signal: ctrl.signal
        });

        if (postRes.status === 405 && targetUrl === '/api/local-llm') {
          targetUrl = 'http://localhost:8080/api/local-llm';
          postRes = await fetch(targetUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              prompt: userQuery,
              history: this.history,
              system: MARIA_SYSTEM_PROMPT
            }),
            signal: ctrl.signal
          });
        }
        clearTimeout(tid);

        if (postRes.ok) {
          const postData = await postRes.json();
          const llmText = postData.response || postData.message || postData.text || '';
          if (postData.available && llmText) {
            this.hideTyping();
            this.activeTier = 'local';
            this.localProvider = postData.provider || 'Ollama';
            this.updateTierBadges(`[LLM Local 💻 (${postData.model || 'Ollama'})]`);
            this.history.push({ role: 'model', parts: [{ text: llmText }] });
            this.botSay(this.formatBotMarkdown(llmText), 'local-llm');
            return;
          }
        }
      } catch (errLocal) {
        console.warn('[AISommelier] Proxy /api/local-llm no disponible:', errLocal.message);
      }
    }

    // 2. PRIORIDAD EN LA WEB (O FALLBACK LOCAL SIN OLLAMA): Gemini Cloud 24/7
    try {
      const cloudText = await this.callGeminiCloud(userQuery, imageObj);
      if (cloudText) {
        this.hideTyping();
        this.activeTier = 'cloud';
        this.updateTierBadges('[Gemini Cloud ☁️]');
        this.history.push({ role: 'model', parts: [{ text: cloudText }] });
        this.botSay(this.formatBotMarkdown(cloudText), 'cloud');
        return;
      }
    } catch (errCloud) {
      console.warn('[AISommelier] Gemini Cloud no disponible:', errCloud.message);
    }

    // 3. ALTERNATIVA: Gemini Nano On-Device (window.ai) si está disponible
    if (window.ai?.languageModel) {
      try {
        const caps = await window.ai.languageModel.capabilities?.();
        if (caps?.available === 'readily') {
          const session = await window.ai.languageModel.create({ systemPrompt: MARIA_SYSTEM_PROMPT });
          const nanoText = await session.prompt(userQuery || 'Hola María');
          if (nanoText) {
            this.hideTyping();
            this.activeTier = 'nano';
            this.updateTierBadges('[Gemini Nano 🧠]');
            this.history.push({ role: 'model', parts: [{ text: nanoText }] });
            this.botSay(this.formatBotMarkdown(nanoText), 'nano');
            return;
          }
        }
      } catch (errNano) {
        console.log('Tier Nano falló:', errNano.message);
      }
    }

    // 4. FALLBACK OFFLINE / RESILIENTE: Motor Autónomo Heurístico (Tier 3)
    this.hideTyping();
    this.activeTier = 'autonomous';
    this.updateTierBadges('[Motor Autónomo 🍃]');

    try {
      const responseHtml = this.generateAutonomousResponse(userQuery || '', imageObj);
      this.history.push({ role: 'model', parts: [{ text: responseHtml.replace(/<[^>]*>/g, ' ') }] });
      this.botSay(responseHtml, 'eco');
    } catch (e) {
      console.error('Error en fallback heurístico:', e);
      this.botSay('🌿 <strong>María:</strong> Te escucho con atención. Como anfitriona y sommelier, podemos conversar sobre cualquier aspecto botánico o cultural. ¿Qué te gustaría explorar?', 'eco');
    }
  }

  // =========================================================================
  // TIER 3: MOTOR AUTONOMO TEMATICO DE MARIDAJE CONCEPTUAL ELEGANTE
  // =========================================================================
  generateAutonomousResponse(query, imageObj = null) {
    const q = query.toLowerCase().trim();

    if (imageObj) {
      return `
        🔬 <strong>Diagnóstico CannaDoctor Multimodal:</strong><br/><br/>
        He recibido tu muestra fotográfica. Para un diagnóstico botánico preciso:<br/>
        • <strong>Color de hojas:</strong> Si observas clorosis intervenal en hojas bajas, suele tratarse de carencia de Magnesio; si es general desde la base, es Nitrógeno.<br/>
        • <strong>Puntas y bordes:</strong> Puntas curvadas en garra indican sobrefertilización (EC alta); manchas marrones necróticas señalan bloqueo por pH.<br/>
        • <strong>Tricomas:</strong> Si buscas corte lúcido, corta con 90% lechosos / 10% ámbar; si buscas relajación narcótica, espera al 30-40% ámbar.<br/><br/>
        💬 <em>¿En qué semana de floración se encuentra tu planta y qué síntomas notas a simple vista?</em>
      `;
    }

    // 1. Saludos y bienvenida conversacional
    if (/^(hola|buenas|hey|buenos días|buenas tardes|buenas noches|qué tal|que tal|saludos)/i.test(q)) {
      const totalCepas = STRAINS_DATABASE?.length || 877;
      return `
        🌿 <strong>¡Hola! Un placer saludarte. Soy María</strong>, Master Sommelier y anfitriona cultural de CannaCulture.<br/><br/>
        Hablo con total naturalidad de <strong>cualquier tema</strong>: reflexiones de vida, ciencia botánica, gastronomía, cine o sobremesa. Y si lo deseas, calibro maridajes de alta precisión entre las <strong>${totalCepas} variedades botánicas de 75 bancos oficiales</strong> de nuestro catálogo.<br/><br/>
        💬 <em>¿De qué te apetece charlar o qué experiencia buscas disfrutar hoy?</em>
      `;
    }

    // 2. ATMÓSFERA: Foco Creativo, Inspiración, Estudio y Trabajo
    if (/(creativ|inspir|escrib|program|diseñ|trabaj|estudi|pintar|música|arte|concentr|foco|focus|atención|proyect|idea|lúcid|lucid)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[0];
      const reasoning = this.buildReasoningBox(
        'Búsqueda de claridad cognitiva, flujo mental sin fatiga y pensamiento lateral.',
        'Dominancia de Alfa-Pineno (inhibición de acetilcolinesterasa, preservando memoria inmediata) y Limoneno (dopamina).',
        `Selección calibrada de ${this.buildStrainLink(sel)} por su activación lúcida y aroma penetrante.`
      );
      return `
        🎨 <strong>Atmósfera de Foco Creativo y Estado de Flujo:</strong><br/><br/>
        La chispa creativa emerge cuando el cerebro reduce el "ruido de fondo" y conecta ideas distantes. El secreto bioquímico para no caer en el aturdimiento reside en buscar genéticas donde el <strong>Pineno</strong> module al THC, manteniendo despejadas las conexiones neuronales.<br/><br/>
        ${reasoning}
        💡 <strong>Tríada Botánica Calibrada:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Estás inmerso en algún proyecto en particular (escritura, programación, arte)? Cuéntame y afinamos aún más el enfoque.</em>
      `;
    }

    // 3. ATMÓSFERA: Desconexión Vespertina, Alivio del Estrés y Descanso
    if (/(cansad|agotad|dormir|sueño|insomni|relaj|estrés|estres|paz|sofá|sofa|desconect|noche|descans|agobio|tensión|tension|cama)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[1];
      const reasoning = this.buildReasoningBox(
        'Liberación de carga muscular, desaceleración del sistema nervioso simpático y descanso profundo.',
        'Sinergia de Mirceno sedante (>0.5%) y Linalool calmante, potenciando el efecto séquito receptor CB1.',
        `Cribado hacia ${this.buildStrainLink(sel)}, célebre por su abrazo corporal balsámico.`
      );
      return `
        🌙 <strong>Desconexión Vespertina y Descompresión Corporal:</strong><br/><br/>
        Tras una jornada exigente, el cuerpo necesita una señal clara para abandonar el modo de alerta y entrar en recuperación parasimpática. La tensión de los hombros y la rumiación mental se disuelven cuando los terpenos mircénicos atraviesan la barrera hematoencefálica.<br/><br/>
        ${reasoning}
        🛋️ <strong>Tríada Calibrada para tu Descanso:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Sientes más cansancio físico o saturación mental? Puedo afinar la cepa exacta según tu necesidad.</em>
      `;
    }

    // 4. ATMÓSFERA: Social, Conversación, Tertulia y Risas
    if (/(social|amig|fiesta|reír|risa|convers|charl|eufori|hablar|quedada|tardeo|celebr)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[4];
      const reasoning = this.buildReasoningBox(
        'Desinhibición social fluida, buen humor y chispa comunicativa.',
        'Combinación de Limoneno alegre y Beta-Cariofileno ansiolítico para disolver la timidez sin provocar taquicardia.',
        `Elección principal de ${this.buildStrainLink(sel)} para sobremesas vivaces.`
      );
      return `
        🎉 <strong>Atmósfera Social, Encuentros y Tertulia:</strong><br/><br/>
        Las mejores sobremesas nacen de una mente abierta y libre de tensiones. Para compartir entre amigos, buscamos variedades eufóricas que estimulen la charla sin provocar aislamiento ni pesadez.<br/><br/>
        ${reasoning}
        🥂 <strong>Tríada de Convivencia y Euforia:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Es una reunión tranquila de charla o una noche de fiesta y música?</em>
      `;
    }

    // 5. ATMÓSFERA: Alivio Físico, Tensión Muscular y Bienestar Corporal
    if (/(dolor|inflama|físic|fisic|cuerpo|espalda|articul|agujet|muscul|recupera|alivio|terapéut|terapeut)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[6];
      const reasoning = this.buildReasoningBox(
        'Descompresión de tejidos, relajación de contracturas y soporte analgésico.',
        'Fuerte concentración de Beta-Cariofileno (unión selectiva a receptores CB2 periféricos) y Humuleno.',
        `Sugerencia de ${this.buildStrainLink(sel)} por su densidad terapéutica.`
      );
      return `
        🩺 <strong>Recuperación Física y Alivio Muscular:</strong><br/><br/>
        El sistema endocannabinoide periférico modula la respuesta inflamatoria y la percepción de dolor articular. Los terpenos como el cariofileno actúan directamente sobre los receptores CB2 sin saturar la mente.<br/><br/>
        ${reasoning}
        🌿 <strong>Tríada Terapéutica y Restauradora:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿La molestia es por entrenamiento intenso o tensión acumulada por postura y estrés?</em>
      `;
    }

    // 6. ATMÓSFERA: Baja Tolerancia, Funcional, Suave y sin Apalanque
    if (/(suave|baja tolerancia|sin apalanque|sin paranoia|principiante|ligero|funcional|floj|poco thc|cbd)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[7];
      const reasoning = this.buildReasoningBox(
        'Experiencia sensorial amable, claridad mental sostenida y cero taquicardia.',
        'Perfil moderado de cannabinoides con terpenos equilibrados y presencia moduladora de CBD.',
        `Selección de ${this.buildStrainLink(sel)} para disfrute consciente y funcional.`
      );
      return `
        🌱 <strong>Experiencia Suave y Controlada:</strong><br/><br/>
        El disfrute botánico no se mide en porcentajes extremos de THC, sino en la sutileza del ramo aromático y en sentirse en control en todo momento. Para baja tolerancia o uso durante el día, las variedades moderadas son la cumbre de la elegancia.<br/><br/>
        ${reasoning}
        🕊️ <strong>Tríada Equilibrada y Segura:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Buscas consumir de día o para relajarte antes de dormir?</em>
      `;
    }

    // 7. ATMÓSFERA: Sabores y Aromas Específicos
    if (/(cítric|citric|limón|limon|mandarina|frutal|dulce|caramelo|pino|haze|madera|diésel|diesel|gasolina|galleta|cookie|reposter|queso|cheese|skunk)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[2];
      const reasoning = this.buildReasoningBox(
        'Afinidad organoléptica directa y bouquet aromático de alta fidelidad.',
        `Riqueza en ${sel.dominantTerpene || 'terpenos nobles'} complementada con flavonoides específicos de la genética.`,
        `Selección de ${this.buildStrainLink(sel)} de ${safeBank(sel)}.`
      );
      return `
        👅 <strong>Exploración Organoléptica y Notas de Cata:</strong><br/><br/>
        El perfil aromático de la flor es el mapa sensorial de su genética. Cuando buscas un matiz específico, los terpenos no solo aportan aroma en nariz y boca, sino que dictan la personalidad del efecto.<br/><br/>
        ${reasoning}
        🍇 <strong>Tríada Gourmet con tu Perfil Aromático:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Prefieres degustarla en flor vaporizada para capturar el terpeno puro o en combustión tradicional?</em>
      `;
    }

    // 8. ATMÓSFERA: Gastronomía, Cocina y Tertulia Culinaria
    if (/(comid|cenar|almorz|recet|cocin|sabores|degust|postre|vino|cerveza|café|cafe|marid|hambre|apetit|comer|plato|chocolate)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[2];
      const reasoning = this.buildReasoningBox(
        'Estimulación organoléptica, maridaje de contrastes en el paladar y sobremesa.',
        'Limoneno cítrico y Cariofileno especiado: activan las papilas gustativas y potencian la experiencia gustativa.',
        `Selección de ${this.buildStrainLink(sel)} por sus matices de repostería gourmet.`
      );
      return `
        🍷 <strong>Gastronomía y Arte del Maridaje Culinario:</strong><br/><br/>
        En la alta gastronomía, los terpenos del cannabis funcionan exactamente igual que los taninos de un buen vino o los aceites esenciales de la trufa: crean puentes aromáticos con las grasas y azúcares de la comida.<br/><br/>
        ${reasoning}
        🍽️ <strong>Tríada Gourmet Culinaria:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Qué plato o antojo estás preparando o pensando degustar hoy?</em>
      `;
    }

    // 9. ATMÓSFERA: Cine, Música, Series y Experiencia Sensorial
    if (/(películ|pelicula|cine|film|serie|ver una|música|musica|disco|canción|cancion|videojuego|gaming|lectura|libro)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[3];
      const reasoning = this.buildReasoningBox(
        'Inmersión audiovisual, sensibilidad melódica y contemplación relajada.',
        'Ratios equilibrados de THC con Limoneno y Cariofileno: realce cromático y auditivo sin paranoia.',
        `Elección de ${this.buildStrainLink(sel)} para acompañar la pantalla o los auriculares.`
      );
      return `
        🎬 <strong>Cinefilia, Música e Inmersión Sensorial:</strong><br/><br/>
        El arte se disfruta con mayor intensidad cuando los sentidos se despojan de las prisas. La música gana profundidad de capas y el cine cobra una textura envolvente cuando se equilibra la percepción sensorial.<br/><br/>
        ${reasoning}
        🍿 <strong>Tríada de Butaca e Inmersión:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Qué película, serie o género musical tienes pensado ponerte?</em>
      `;
    }

    // 10. ATMÓSFERA: Reflexión Filosófica, Existencialismo y Ciencia Universal
    if (/(filosof|cosmos|universo|espacio|estrella|física|concienc|tiempo|vida|exist|muerte|mente|sentido|astronom|cuántic|pensam|realidad|curiosidad)/i.test(q)) {
      const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
      this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);
      const sel = triad[0]?.strain || STRAINS_DATABASE[5];
      const reasoning = this.buildReasoningBox(
        'Contemplación profunda, expansión perceptiva y tertulia intelectual.',
        'Terpinoleno y Cariofileno complejo: perfil no lineal que estimula la introspección reflexiva.',
        `Maridaje con ${this.buildStrainLink(sel)} para acompañar la mente en viajes de abstracción.`
      );
      return `
        🌌 <strong>Reflexión Filosófica y Perspectiva Cósmica:</strong><br/><br/>
        Pensar en el universo o en los misterios de la conciencia nos recuerda lo asombroso de nuestra propia existencia. Como decía Carl Sagan, somos el medio para que el cosmos se conozca a sí mismo.<br/><br/>
        ${reasoning}
        ✨ <strong>Tríada para el Asombro y la Tertulia:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Qué enigma sobre la vida o el universo te ronda hoy por la cabeza?</em>
      `;
    }

    // 11. CIENCIA BOTÁNICA PURA: Tricomas, hojas amarillas, pH, lavado de raíces
    if (/(tricoma|ambar|ámbar|lechoso|cosech|corte)/i.test(q)) {
      return `
        🔬 <strong>Maduración Bioquímica de los Tricomas Glandulares:</strong><br/><br/>
        Los tricomas pedunculados son las glándulas biosintéticas donde se acumulan cannabinoides y terpenos:<br/>
        1. 💎 <strong>Transparentes (Inmaduros):</strong> Síntesis temprana de CBGA y precursores. Efecto débil e incompleto.<br/>
        2. 🥛 <strong>Lechosos (Pico de THC):</strong> Máxima concentración de THCA activo. Efecto lúcido, cerebral, eufórico y estimulante.<br/>
        3. 🍯 <strong>Ámbar (Oxidación a CBN):</strong> El THC se degrada naturalmente por calor y oxígeno en <strong>Cannabinol (CBN)</strong>, provocando un efecto sedante, narcótico y miorrelajante.<br/><br/>
        ⚖️ <strong>Regla de Corte Sommelier:</strong><br/>
        • Efecto activo/diurno: <strong>85-90% lechosos / 10-15% ámbar</strong>.<br/>
        • Efecto corporal/nocturno: <strong>60-70% lechosos / 30-40% ámbar</strong>.<br/><br/>
        💬 <em>¿Con qué aumento estás observando tus flores actualmente?</em>
      `;
    }

    if (/(amarill|clorosis|carencia|deficiencia|hoja)/i.test(q)) {
      return `
        🍂 <strong>Diagnóstico de Clorosis Foliar y Movilidad Nutricional:</strong><br/><br/>
        La degradación de clorofila se diagnostica según la posición vascular:<br/>
        1. ⬇️ <strong>Hojas Bajas (Nutrientes Móviles):</strong> Carencia de <strong>Nitrógeno (N)</strong> (amarilleamiento uniforme desde abajo) o <strong>Magnesio (Mg)</strong> (clorosis intervenal con nervios verdes).<br/>
        2. ⬆️ <strong>Brotes Nuevos (Nutrientes Inmóviles):</strong> Carencia de <strong>Hierro (Fe)</strong> o <strong>Calcio (Ca)</strong>.<br/>
        3. 🔒 <strong>Bloqueo por pH (pH Lockout):</strong> La causa más común. Fuera del rango <strong>6.2-6.8 en tierra</strong> (o 5.6-6.2 en coco), las raíces no asimilan nutrientes aunque estén en el sustrato.<br/>
        4. 🍁 <strong>Senescencia Final:</strong> En las últimas 2 semanas de floración es normal y deseable que las hojas grandes amarilleen.<br/><br/>
        💬 <em>¿En qué semana de floración estás y qué pH usas en el riego?</em>
      `;
    }

    if (/(séquito|sequito|entourage|terpeno)/i.test(q)) {
      return `
        🧬 <strong>El Efecto Séquito (Entourage Effect) y Farmacología:</strong><br/><br/>
        Formulado por el Dr. Raphael Mechoulam y el neurólogo Dr. Ethan Russo, demuestra que los cannabinoides (THC, CBD, CBG) y los terpenos <strong>actúan en sinergia holística</strong>:<br/>
        • <strong>Mirceno:</strong> Incrementa la permeabilidad de la barrera hematoencefálica.<br/>
        • <strong>Beta-Cariofileno:</strong> Activa directamente los receptores inmunitarios <strong>CB2</strong> como potente antiinflamatorio dietético.<br/>
        • <strong>Alfa-Pineno:</strong> Inhibe la enzima acetilcolinesterasa, protegiendo la memoria a corto plazo del impacto del THC.<br/><br/>
        💬 <em>Por ello, las flores integrales y extractos Full Spectrum ofrecen una experiencia mucho más rica y modulada que los destilados aislados.</em>
      `;
    }

    // 12. Búsqueda explícita de cepa en el catálogo
    const matchStrain = STRAINS_DATABASE.find(s => q.includes(s.name.toLowerCase()));
    if (matchStrain) {
      const triad = [
        { type: 'top', label: '🔍 Cepa Consultada', badgeColor: '#10B981', strain: matchStrain },
        ...this.scoringEngine.getTriadRecommendations(matchStrain.dominantTerpene, [matchStrain.id]).slice(0, 2)
      ];
      return `
        🌿 <strong>Ficha Sommelier: ${this.buildStrainLink(matchStrain)}</strong><br/><br/>
        • <strong>Banco Criador:</strong> ${safeBank(matchStrain)}<br/>
        • <strong>Tipología:</strong> ${matchStrain.species} | <strong>THC:</strong> ${matchStrain.thc}% | <strong>CBD:</strong> ${matchStrain.cbd || '0.1'}%<br/>
        • <strong>Terpeno Dominante:</strong> ${matchStrain.dominantTerpene || 'Equilibrado'}<br/>
        • <strong>Perfil de Sabores:</strong> ${safeFlavors(matchStrain).join(', ')}<br/>
        • <strong>Efectos Principales:</strong> ${safeEffects(matchStrain).join(', ')}<br/><br/>
        💡 <strong>Ficha Directa & Alternativas Similares:</strong><br/>
        ${this.generateRecommendationCardsHTML(triad)}
        💬 <em>¿Te gustaría conocer sugerencias de maridaje o cómo optimizar su cultivo y curado?</em>
      `;
    }

    // 13. Charla Cotidiana, Abierta y Erudita sobre Cualquier Tema
    const triad = this.scoringEngine.getTriadRecommendations(q, this.recentRecommendations);
    this.recentRecommendations = [...this.recentRecommendations, ...triad.map(t => t.strain.id)].slice(-10);

    return `
      💬 <strong>María:</strong> Te escucho con agrado y reflexión.<br/><br/>
      Sobre lo que mencionas (<em>"${query.slice(0, 80)}"</em>), me parece fascinante cómo la conversación humana siempre encuentra puntos de conexión entre la ciencia, el día a día y nuestra percepción del bienestar.<br/><br/>
      Como anfitriona botánica, creo firmemente que cualquier momento de distensión se enriquece prestando atención a los detalles sutiles: los aromas, el ritmo con el que respiramos y el entorno que nos rodea.<br/><br/>
      🌿 <strong>Tríada Botánica de Maridaje para este Momento:</strong><br/>
      ${this.generateRecommendationCardsHTML(triad)}
      💬 <em>¿Hacia dónde te gustaría orientar nuestra conversación ahora?</em>
    `;
  }

  // =========================================================================
  // SALUDO INICIAL CONVERSACIONAL DE MARÍA
  // =========================================================================
  sendInitialGreeting() {
    const totalCepas = STRAINS_DATABASE?.length || 877;
    const greeting = `¡Hola! Soy <strong>María</strong>, tu Master Sumiller y anfitriona botánica en CannaCulture. 🌿<br/><br/>
    Cuento con arquitectura inteligente universal con <strong>Gemini Cloud 24/7</strong> y <strong>LLM Local</strong> para asesoramiento cannábico profundo, análisis terpénico y visión multimodal con <strong>CannaDoctor 2.0</strong>, además de un <strong>Motor Autónomo 0-Tokens</strong> para responder sin demoras.<br/><br/>
    💡 <strong>¿Qué te gustaría explorar hoy?</strong><br/>
    • 🌿 <em>Maridajes y Efectos:</em> Recomiendo variedades calibradas según tu estado de ánimo, momento del día o notas de sabor entre las <strong>${totalCepas} variedades botánicas de 75 bancos oficiales</strong>.<br/>
    • 🔬 <strong>CannaDoctor 2.0:</strong> Pulsa 📷 para diagnosticar plagas, carencias o madurez de tricomas mediante foto.<br/>
    • 💬 <em>Charla Abierta:</em> Conversemos sobre botánica, ciencia, cine, filosofía o sobremesa con total naturalidad.<br/>
    • 🔊 <strong>Voz Interactiva:</strong> Pulsa 🔊 en cualquiera de mis respuestas para escuchar la narración.`;
    this.botSay(greeting, 'eco');
  }

  // =========================================================================
  // SWIPE-DOWN TO CLOSE — UX NATIVA MOBILE
  // =========================================================================
  _initSwipeClose() {
    if (!this.chatWindow) return;

    let touchStartY = 0;
    let touchCurrentY = 0;
    let isDragging = false;

    const header = this.chatWindow.querySelector('div:first-child');
    const swipeTarget = header || this.chatWindow;

    swipeTarget.addEventListener('touchstart', (e) => {
      touchStartY = e.touches[0].clientY;
      isDragging = true;
      this.chatWindow.style.transition = 'none';
    }, { passive: true });

    swipeTarget.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      touchCurrentY = e.touches[0].clientY;
      const delta = touchCurrentY - touchStartY;
      if (delta > 0) {
        // Solo permite arrastrar hacia abajo
        this.chatWindow.style.transform = `translateY(${delta}px)`;
      }
    }, { passive: true });

    swipeTarget.addEventListener('touchend', () => {
      if (!isDragging) return;
      isDragging = false;
      const delta = touchCurrentY - touchStartY;
      this.chatWindow.style.transition = '';
      this.chatWindow.style.transform = '';

      // Si el swipe fue > 100px hacia abajo, cerrar el chat
      if (delta > 100) {
        this.chatWindow.style.display = 'none';
        document.body.style.overflow = '';
      }
      touchStartY = 0;
      touchCurrentY = 0;
    }, { passive: true });
  }
}
