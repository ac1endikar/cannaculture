// CannaCatalog 2.0 - Agente IA Sommelier Humano & CannaDoctor Multimodal (Google Gemini 3.6 Flash)
import { STRAINS_DATABASE, ACTIVITIES_DATA, TERPENES_INFO } from './data.js?v=2026_clean_v45';

// Helpers seguros de extracción de propiedades defensivas ante esquemas heterogéneos
const safeFlavors = (s) => (Array.isArray(s?.flavors) && s.flavors.length > 0) ? s.flavors : (s?.aroma ? s.aroma.split(',').map(x => x.trim()).filter(Boolean) : ['Aroma equilibrado', 'Bouquet herbal']);
const safeEffects = (s) => (Array.isArray(s?.effects) && s.effects.length > 0) ? s.effects : (s?.effect ? [s.effect] : ['Equilibrado', 'Bienestar general']);
const safeTerpene = (s) => (s?.dominantTerpene || '').toString().toLowerCase();
const safeBank = (s) => s?.bank || s?.breeder || 'Banco Seleccionado';

export class AISommelierAgent {
  constructor(appController) {
    this.app = appController;
    this.history = [];
    this.apiKey = localStorage.getItem('gemini_api_key') || null;
    this.attachedImage = null; // { mimeType, data: base64, previewUrl, name }
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

    // Elementos CannaDoctor Multimodal (Cámara / Subida de Foto)
    this.fileInputFloating = document.getElementById('ai-chat-file');
    this.fileInputInline = document.getElementById('ai-chat-file-inline');
    this.btnPhotoFloating = document.getElementById('ai-chat-btn-photo');
    this.btnPhotoInline = document.getElementById('ai-chat-btn-photo-inline');
    this.previewFloating = document.getElementById('ai-attach-preview-floating');
    this.previewInline = document.getElementById('ai-attach-preview-inline');

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

    this.keyBtn = document.getElementById('ai-chat-key-btn');
    this.keyBtn?.addEventListener('click', () => {
      const current = localStorage.getItem('gemini_api_key') || '';
      const entered = prompt('Introduce tu API Key de Google Gemini (Google AI Studio):\n(Se almacenará localmente en tu navegador para activar Gemini 3.6 Flash y CannaDoctor)', current);
      if (entered !== null) {
        const clean = entered.trim();
        if (clean) {
          localStorage.setItem('gemini_api_key', clean);
          this.apiKey = clean;
          this.botSay('🔑 <strong>Clave API de Gemini activada con éxito.</strong> A partir de ahora tus consultas y fotos de cultivo serán procesadas directamente por <strong>Google Gemini 3.6 Flash</strong>.');
        } else {
          localStorage.removeItem('gemini_api_key');
          this.apiKey = null;
          this.botSay('ℹ️ Clave eliminada. El Sommelier volverá a funcionar con el motor heurístico local.');
        }
      }
    });

    // Eventos de selección de archivo fotográfico (CannaDoctor)
    const handleFileSelect = (file) => {
      if (!file || !file.type.startsWith('image/')) return;
      const reader = new FileReader();
      reader.onload = (e) => {
        const dataUrl = e.target.result;
        const commaIdx = dataUrl.indexOf(',');
        const base64 = commaIdx !== -1 ? dataUrl.slice(commaIdx + 1) : dataUrl;
        this.attachedImage = {
          mimeType: file.type,
          data: base64,
          previewUrl: dataUrl,
          name: file.name
        };
        this.renderAttachPreviews();
      };
      reader.readAsDataURL(file);
    };

    this.btnPhotoFloating?.addEventListener('click', () => this.fileInputFloating?.click());
    this.fileInputFloating?.addEventListener('change', (e) => {
      if (e.target.files?.[0]) handleFileSelect(e.target.files[0]);
    });

    this.btnPhotoInline?.addEventListener('click', () => this.fileInputInline?.click());
    this.fileInputInline?.addEventListener('change', (e) => {
      if (e.target.files?.[0]) handleFileSelect(e.target.files[0]);
    });

    // Send Message Events
    const handleSendFloating = () => {
      const text = this.inputFloating?.value?.trim() || '';
      const img = this.attachedImage;
      if (!text && !img) return;
      if (this.inputFloating) this.inputFloating.value = '';
      this.clearAttachedImage();
      this.userSay(text || '🔬 [Foto enviada para análisis con CannaDoctor]', img);
      this.processQuery(text, img);
    };

    const handleSendInline = () => {
      const text = this.inputInline?.value?.trim() || '';
      const img = this.attachedImage;
      if (!text && !img) return;
      if (this.inputInline) this.inputInline.value = '';
      this.clearAttachedImage();
      this.userSay(text || '🔬 [Foto enviada para análisis con CannaDoctor]', img);
      this.processQuery(text, img);
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
        this.processQuery(text, null);
      });
    });

    // Saludo inicial con razonamiento activo y presentación de CannaDoctor
    const totalCepas = STRAINS_DATABASE?.length || 418;
    const greeting = `¡Hola! Soy <strong>Mateo</strong>, tu master sumiller botánico en CannaCulture. 🌿<br/><br/>
    Cuento con un <strong>motor de razonamiento neuro-terpénico y visión multimodal</strong> conectado a nuestro catálogo de <strong>${totalCepas} cepas de 39 bancos premium</strong>.<br/><br/>
    💡 <strong>¿En qué puedo asistirte hoy?</strong><br/>
    • 👅 <em>Recomendación de cepa:</em> Dime tu perfil aromático deseado o la actividad que vas a realizar.<br/>
    • 🔬 <strong>CannaDoctor Multimodal:</strong> Adjunta una foto de una hoja o cogollo (botón 📷) para diagnosticar carencias, plagas o madurez de tricomas.`;
    this.botSay(greeting);
  }

  renderAttachPreviews() {
    [this.previewFloating, this.previewInline].forEach(container => {
      if (!container) return;
      if (!this.attachedImage) {
        container.style.display = 'none';
        container.innerHTML = '';
        return;
      }
      container.style.display = 'flex';
      container.innerHTML = `
        <span>📷 <strong>${this.attachedImage.name}</strong></span>
        <button type="button" class="ai-detach-btn" style="background:none; border:none; color:#EF4444; font-weight:900; cursor:pointer; font-size:0.9rem; padding:0 4px;" title="Quitar foto">✕</button>
      `;
      container.querySelector('.ai-detach-btn')?.addEventListener('click', () => this.clearAttachedImage());
    });
  }

  clearAttachedImage() {
    this.attachedImage = null;
    if (this.fileInputFloating) this.fileInputFloating.value = '';
    if (this.fileInputInline) this.fileInputInline.value = '';
    this.renderAttachPreviews();
  }

  userSay(text, imageObj = null) {
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const msgEl = document.createElement('div');
      msgEl.className = 'ai-msg user-msg';
      msgEl.innerHTML = `<div>${text}</div>`;
      if (imageObj?.previewUrl) {
        const imgWrap = document.createElement('div');
        imgWrap.style.marginTop = '6px';
        imgWrap.innerHTML = `<img src="${imageObj.previewUrl}" alt="Foto adjunta" style="max-width:180px; max-height:140px; border-radius:10px; border:1px solid #10B981; object-fit:cover; display:block;" />`;
        msgEl.appendChild(imgWrap);
      }
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

  showTyping(customMessage = null) {
    this.messagesContainers.forEach(container => {
      if (!container) return;
      const typing = document.createElement('div');
      typing.className = 'ai-msg bot-msg typing-msg ai-typing-indicator-node';
      typing.innerHTML = `<span>🧠 ${customMessage || 'Mateo & CannaDoctor analizando razonamiento botánico...'}</span>`;
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
      const dt = safeTerpene(strain);
      if (activity.preferredTerpenes?.some(t => t.toLowerCase() === dt)) score += 40;
      if (activity.recommendedSpecies?.includes(strain.species)) score += 30;
      if (strain.activities && strain.activities.includes(activityId)) score += 50;
      score += ((strain.rating || 4.5) * 5);

      return { strain, score };
    });

    scoredStrains.sort((a, b) => b.score - a.score);
    return {
      activity,
      topStrains: scoredStrains.slice(0, 3).map(s => s.strain)
    };
  }

  async processQuery(userQuery, imageObj = null) {
    const trimmed = (userQuery || '').trim();
    if (trimmed.startsWith('AQ.Ab') || trimmed.startsWith('AIzaSy') || trimmed.startsWith('/key ') || trimmed.startsWith('key:')) {
      const newKey = trimmed.replace(/^\/key\s*|^key:\s*/i, '').trim();
      localStorage.setItem('gemini_api_key', newKey);
      this.apiKey = newKey;
      this.botSay('🔑 <strong>¡Clave API configurada con éxito!</strong><br/><br/>He activado la conexión directa con <strong>Google Gemini 3.6 Flash</strong> y <strong>CannaDoctor Multimodal</strong>. A partir de ahora todas tus consultas se responderán con inteligencia multimodal en tiempo real.');
      return;
    }

    const isScienceQuery = /(por\s*qu[eé]|c[oó]mo|qu[eé]\s+es|explica|a\s+qu[eé]\s+se\s+debe|tricoma|hoja|cultivo|ph|abono|s[eé]quito|curado|lavado|ambar|ámbar)/i.test(userQuery || '');
    this.showTyping(imageObj 
      ? '🔬 CannaDoctor examinando imagen botánica con Gemini 3.6...' 
      : isScienceQuery 
        ? '🌿 Mateo analizando la base científica y botánica...' 
        : '🧠 Mateo analizando maridaje terpénico en el catálogo...');

    try {
      const cloudResponse = await this.callGeminiAPI(userQuery, imageObj);
      if (cloudResponse) {
        this.hideTyping();
        this.botSay(cloudResponse);
        return;
      }
    } catch (err) {
      console.log('💡 Sommelier activando motor de respuesta local:', err.message);
    }

    // Fallback local garantizado sin bloqueo
    this.hideTyping();
    try {
      if (imageObj) {
        this.botSay(`
          🔬 <strong>CannaDoctor:</strong> He recibido tu fotografía de cultivo.<br/><br/>
          Para procesar diagnósticos visuales avanzados (deficiencias de nitrógeno, fósforo, magnesio, araña roja o madurez de tricomas), asegúrate de que el servidor local con soporte Gemini esté en ejecución o introduce tu clave en los ajustes.<br/><br/>
          💬 <em>Mientras tanto, puedes describirme los síntomas o consultar cualquier duda botánica sobre tu cultivo.</em>
        `);
        return;
      }
      const response = this.generateHumanResponse(userQuery || '');
      this.history.push({ role: 'model', parts: [{ text: response.replace(/<[^>]*>/g, '') }] });
      this.botSay(response);
    } catch (fallbackErr) {
      console.error('Error en motor local de Sommelier:', fallbackErr);
      this.botSay(`
        🌿 <strong>Mateo:</strong> He recibido tu consulta sobre <em>"${userQuery || 'botánica cannábica'}"</em>.<br/><br/>
        Como especialista botánico, puedo explicarte con detalle científico cualquier proceso: <strong>por qué los tricomas maduran a ámbar, por qué las hojas amarillean, el efecto séquito de los terpenos o cómo calibrar el pH</strong>.<br/><br/>
        💬 <em>¿Qué aspecto de tu cultivo o de la ciencia cannábica te gustaría que analicemos en detalle?</em>
      `);
    }
  }

  async callGeminiAPI(userQuery, imageObj = null) {
    const catalogSummary = STRAINS_DATABASE.slice(0, 60).map(s => 
      `- ${s.name} (${s.species}, ${safeBank(s)}): THC ${s.thc}%, Terpeno: ${s.dominantTerpene || 'Equilibrado'}, Sabores: ${safeFlavors(s).slice(0,3).join('/')}, ID: ${s.id}`
    ).join('\n');

    const systemInstruction = {
      parts: [{
        text: `Eres Mateo, un botánico científico, experto en el sistema endocannabinoide y Master Sommelier de CannaCulture.
Tu forma de conversar es idéntica a Google Gemini: hablas con cercanía, elocuencia natural, rigor pedagógico y un conocimiento enciclopédico profundo.

DIRECTRICES FUNDAMENTALES DE COMPORTAMIENTO:

1. CONSULTAS DE CONOCIMIENTO, CIENCIA Y CULTIVO ("¿Por qué...", "¿Cómo...", "¿Qué es...", "Explícame...", etc.):
   - Si el usuario te pregunta por el motivo o causas de cualquier fenómeno (por ejemplo: por qué los tricomas se vuelven ámbar, por qué las hojas amarillean, qué es el efecto séquito, cómo influye el pH en la asimilación radicular, por qué se realiza el curado, etc.):
   - EXPLICA EL FENÓMENO CON RIGOR Y CLARIDAD CIENTÍFICA. Desglosa los procesos bioquímicos (biosíntesis de cannabinoides, degradación de THCA a CBN, translocación de nutrientes móviles e inmóviles, modulación alostérica en receptores CB1 y CB2, degradación enzimática de la clorofila, etc.).
   - ⚠️ REGLA DE ORO OBLIGATORIA: ¡NO RECOMIENDES CEPAS NI VARIEDADES si el usuario solo te está pidiendo una explicación conceptual, botánica o científica! No intentes forzar ni desviar la conversación hacia una variedad de catálogo cuando te preguntan el "porqué" de las cosas. Trátalo exactamente como hablaría Gemini: explicando la ciencia de forma amena y completa.

2. RECOMENDACIONES DE CEPAS (ÚNICAMENTE cuando el usuario las solicite de forma explícita):
   - Solo cuando el usuario te pida expresamente recomendaciones o maridajes (por ejemplo: "recomiéndame una variedad", "qué cepa me sirve para dormir", "busco una sativa cítrica", "qué fumar para ver cine"):
   - Incluye el bloque HTML de razonamiento neuro-terpénico:
<div class="sommelier-reasoning-box">
  <div class="reasoning-header">
    <span class="reasoning-brain-icon">🧠</span>
    <span class="reasoning-title">RAZONAMIENTO DEL SOMMELIER</span>
    <span class="reasoning-badge">Análisis Neuro-Terpénico</span>
  </div>
  <div class="reasoning-steps">
    <div class="reasoning-step">
      <span class="step-num">1</span>
      <div><strong>Diagnóstico de Necesidad:</strong> [Resumen de lo que busca el usuario]</div>
    </div>
    <div class="reasoning-step">
      <span class="step-num">2</span>
      <div><strong>Análisis Terpénico & Séquito:</strong> [Terpenos y ratios explicados]</div>
    </div>
    <div class="reasoning-step">
      <span class="step-num">3</span>
      <div><strong>Cribado del Catálogo:</strong> [Por qué se eligen esas cepas]</div>
    </div>
  </div>
</div>
   - Siempre que nombres una cepa del catálogo, usa enlaces interactivos:
     <a href="#" class="ai-strain-link" data-strain-id="ID_DE_LA_CEPA"><strong>Nombre Cepa</strong></a>

3. DIAGNÓSTICO FOTOGRÁFICO Y SÍNTOMAS DE CULTIVO (CannaDoctor):
   - Si el usuario comparte una foto de una planta o describe problemas de cultivo:
   - Diagnostica de forma metódica: 1) Diagnóstico principal (carencia de N, P, K, Mg, Ca, exceso de sales, plagas como araña roja o trips, o madurez de tricomas); 2) Causa fisiológica; 3) Tratamiento y medidas correctoras orgánicas inmediatas.

4. CONVERSACIÓN FLUIDA CON MEMORIA:
   - Recuerda lo hablado en los turnos previos. Si el usuario te hace preguntas de seguimiento ("¿y cuánto tiempo tarda?", "¿qué pasa si no lo hago?", "¿cómo afecta eso al sabor?"), responde directamente profundizando en el tema.

5. INFORMACIÓN DEL CATÁLOGO (Para cuando se soliciten recomendaciones):
   El catálogo cuenta con ${STRAINS_DATABASE.length} cepas de 39 bancos premium.
Muestra de variedades:
${catalogSummary}`
      }]
    };

    const userParts = [];
    if (userQuery) {
      userParts.push({ text: userQuery });
    } else if (imageObj) {
      userParts.push({ text: 'Analiza esta imagen botánica de cannabis (diagnóstico de salud, deficiencias, plagas o madurez de flor).' });
    }

    if (imageObj?.data && imageObj?.mimeType) {
      userParts.push({
        inlineData: {
          mimeType: imageObj.mimeType,
          data: imageObj.data
        }
      });
    }

    // Registrar en el historial conversacional
    this.history.push({ role: 'user', parts: userParts });
    if (this.history.length > 12) {
      this.history = this.history.slice(-12);
    }

    const payload = {
      model: 'gemini-3.6-flash',
      contents: this.history,
      system_instruction: systemInstruction
    };

    // 1. Intentar primero a través del proxy local /api/gemini (timeout de 25s para respuestas científicas completas)
    const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    if (isLocal) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 25000);
        const proxyRes = await fetch('/api/gemini', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          signal: controller.signal
        });
        clearTimeout(timeoutId);
        if (proxyRes.ok) {
          const data = await proxyRes.json();
          const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
          if (text) {
            this.history.push({ role: 'model', parts: [{ text: text }] });
            return this.formatBotMarkdown(text);
          }
        }
      } catch (e) {
        // Si el proxy falla o da timeout, continuamos
      }
    }

    // 2. Intentar directamente con la API Key si está guardada en localStorage (funciona en GitHub Pages y local)
    if (this.apiKey) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 25000);
        const directUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${this.apiKey}`;
        const directRes = await fetch(directUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: payload.contents,
            system_instruction: payload.system_instruction
          }),
          signal: controller.signal
        });
        clearTimeout(timeoutId);
        if (directRes.ok) {
          const data = await directRes.json();
          const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
          if (text) {
            this.history.push({ role: 'model', parts: [{ text: text }] });
            return this.formatBotMarkdown(text);
          }
        }
      } catch (e) {
        // Fallback al motor local
      }
    }

    throw new Error('Motor de razonamiento local activado');
  }

  formatBotMarkdown(text) {
    let formatted = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n\n/g, '<br/><br/>')
      .replace(/\n/g, '<br/>');

    return formatted;
  }

  generateHumanResponse(rawQuery) {
    const query = (rawQuery || '').toLowerCase().trim();

    // =========================================================================
    // 0. SALUDOS & IDENTIDAD CONVERSACIONAL
    // =========================================================================
    if (query === 'hola' || query === 'buenas' || query === 'hey' || query === 'saludos' || query.startsWith('hola ') || query.includes('quién eres') || query.includes('quien eres') || query.includes('qué puedes hacer')) {
      return `
        🌿 <strong>¡Hola! Soy Mateo</strong>, especialista en botánica cannábica, cultivo y Master Sommelier de CannaCulture.<br/><br/>
        Puedes hablar conmigo con total naturalidad, exactamente como con <strong>Gemini</strong>. Te asisto en:<br/><br/>
        • 🔬 <strong>Ciencia y Botánica:</strong> Pregúntame el <em>porqué</em> de cualquier fenómeno (maduración de tricomas, clorosis de hojas, pH, efecto séquito de los terpenos, curado...).<br/>
        • 🩺 <strong>CannaDoctor:</strong> Diagnostico deficiencias minerales, excesos de sales o plagas en tu cultivo.<br/>
        • 👅 <strong>Maridaje Sommelier:</strong> Si me pides una recomendación para un sabor o actividad, buscaré entre las <strong>${STRAINS_DATABASE.length} cepas de nuestro catálogo</strong> analizando su perfil de terpenos.<br/><br/>
        💬 <em>¿En qué te gustaría profundizar hoy?</em>
      `;
    }

    // =========================================================================
    // 1. MOTOR EDUCATIVO & CIENTÍFICO (PREGUNTAS DE "POR QUÉ", "CÓMO", "QUÉ ES")
    // =========================================================================
    const isExplicitRecommendation = /(recomi|sugi|dame|busco una|quiero fumar|para fumar|cu[aá]l comprar|para probar|qu[eé] variedad|qu[eé] cepa|qu[eé] fumar|qu[eé] me tomo|qu[eé] elijo)/i.test(query);

    // A) TRICOMAS: COLOR ÁMBAR, LECHOSO, TRANSPARENTE Y COSECHA
    if (query.includes('tricoma') || query.includes('ambar') || query.includes('ámbar') || query.includes('lechoso') || query.includes('cosechar') || query.includes('punto de corte')) {
      return `
        🔬 <strong>Fisiología y Maduración de los Tricomas Glandulares:</strong><br/><br/>
        Los tricomas (específicamente los <em>glandulares pedunculados</em>) son las fábricas biosintéticas donde la planta produce cannabinoides (THCA, CBDA, CBGA) y terpenos volátiles en la cabeza resinosa globular.<br/><br/>
        <strong>¿Por qué cambian de color a lo largo de la floración?</strong><br/><br/>
        1. 💎 <strong>Transparentes (Fase Inmadura):</strong><br/>
        Las glándulas están sintetizando precursores. El contenido de cannabinoides es bajo y cosechar aquí produce un efecto suave, a menudo incompleto o que puede generar taquicardia.<br/><br/>
        2. 🥛 <strong>Lechosos u Opacos (Pico Máximo de THC):</strong><br/>
        La cabeza del tricoma se satura de <strong>THCA en su máxima concentración activa</strong>. La luz ya no la atraviesa porque los cannabinoides y terpenos alcanzan su densidad óptima. El efecto aquí es <strong>cerebral, lúcido, eufórico y estimulante</strong>.<br/><br/>
        3. 🍯 <strong>Ámbar (Oxidación y Degradación a CBN):</strong><br/>
        Con el paso del tiempo, el oxígeno, la temperatura y la degradación celular, el <strong>THC se oxida químicamente y se convierte en Cannabinol (CBN)</strong>. El CBN tiene una afinidad modulada en los receptores CB1 del sistema nervioso que genera un <strong>efecto profundamente sedante, narcótico y miorrelajante</strong> (el famoso efecto sofá o <em>couch-lock</em>).<br/><br/>
        ⚖️ <strong>Punto Óptimo de Corte:</strong><br/>
        • Si buscas efecto despierto y cerebral: <strong>90% lechosos / 10% ámbar</strong>.<br/>
        • Si buscas relajación muscular y ayuda para dormir: <strong>60-70% lechosos / 30-40% ámbar</strong>.<br/><br/>
        💬 <em>¿Tienes una lupa o microscopio para revisar tus flores? Cuéntame qué porcentaje aproximado ves y calculamos el momento ideal de corte.</em>
      `;
    }

    // B) HOJAS AMARILLAS: CLOROSIS, DEFICIENCIAS, pH Y SENESCENCIA
    if (query.includes('amarill') || query.includes('clorosis') || query.includes('carencia') || query.includes('deficiencia') || query.includes('por qué se caen las hojas')) {
      return `
        🍂 <strong>¿Por qué se ponen amarillas las hojas del cannabis? (Diagnóstico Botánico):</strong><br/><br/>
        El amarilleamiento foliar (clorosis) se produce por la pérdida o degradación de la clorofila. La clave científica para saber qué ocurre reside en la <strong>movilidad de los nutrientes</strong> en el sistema vascular de la planta:<br/><br/>
        1. 🔄 <strong>Amarillean primero las hojas inferiores (Nutrientes Móviles):</strong><br/>
        • <strong>Nitrógeno (N):</strong> La planta tiene la capacidad de retirar nitrógeno de las hojas viejas para alimentar los brotes superiores que están creciendo. El amarilleamiento empieza en la base de la planta y avanza hacia arriba de manera uniforme.<br/>
        • <strong>Magnesio (Mg):</strong> Provoca clorosis intervenal en hojas bajas (las venas permanecen verdes mientras el espacio entre ellas amarillea).<br/><br/>
        2. 🛑 <strong>Amarillean los brotes superiores o hojas nuevas (Nutrientes Inmóviles):</strong><br/>
        • <strong>Hierro (Fe), Azufre (S) o Calcio (Ca):</strong> La planta no puede transportar estos elementos desde las hojas viejas. Si las puntas o nuevos brotes nacen amarillentos, indica falta de micronutrientes o estrés radicular.<br/><br/>
        3. 🔒 <strong>Bloqueo por pH (pH Lockout):</strong><br/>
        Muchas veces el nutriente sí está en la tierra, pero las raíces <strong>no pueden absorberlo</strong> si el pH del agua está descompensado. El rango óptimo de absorción de nitrógeno y fósforo es de <strong>6.2 a 6.8 en sustrato</strong> y <strong>5.6 a 6.2 en coco/hidroponía</strong>.<br/><br/>
        4. 🍁 <strong>Senescencia Natural en Fin de Floración:</strong><br/>
        En las últimas 2 a 3 semanas antes de cosechar, es totalmente natural y beneficioso que las hojas grandes amarilleen. La planta está agotando sus reservas de azúcares y clorofila para madurar los cogollos.<br/><br/>
        💬 <em>¿En qué parte de la planta empezó el amarilleamiento (arriba o abajo) y en qué semana de cultivo te encuentras?</em>
      `;
    }

    // C) HOJAS EN GARRA & PUNTAS QUEMADAS: TOXICIDAD POR NITRÓGENO Y EC ALTA
    if (query.includes('garra') || query.includes('puntas quemadas') || query.includes('quemada') || query.includes('exceso de abono') || query.includes('sobrefertiliz')) {
      return `
        🦅 <strong>Hojas en Forma de Garra y Puntas Quemadas: Fisiología del Exceso:</strong><br/><br/>
        Cuando las hojas adquieren una curva pronunciada hacia abajo (como garras de águila) o las puntas se secan y queman, estamos ante un <strong>desequilibrio osmótico en las raíces</strong>:<br/><br/>
        1. 🧪 <strong>Toxicidad por Exceso de Nitrógeno (Hojas en Garra):</strong><br/>
        El exceso de nitrógeno en floración hiperhidrata el haz celular y oscurece el follaje (verde azulado oscuro). Las células superiores crecen más rápido que las inferiores, forzando a la hoja a doblarse mecánicamente hacia abajo en forma de garra.<br/><br/>
        2. ⚡ <strong>Presión Osmótica y Salinidad (EC Elevada / Puntas Quemadas):</strong><br/>
        Si hay demasiadas sales minerales disueltas en el agua de riego, la concentración en el sustrato supera a la del interior de las raíces. Por el principio de ósmosis inversa, a la planta le cuesta extraer agua libre, cerrando los estomas. Las sales residuales se acumulan en las terminaciones de los nervios distales foliares, necrosando (quemando) las puntas.<br/><br/>
        🛠️ <strong>Solución Botánica Inmediata:</strong><br/>
        • Realiza un riego generoso solo con agua declorada a <strong>pH 6.3 - 6.5</strong>, permitiendo un drenaje del 25-30% para lixiviar y arrastrar el exceso de sales acumuladas.<br/>
        • Suspende fertilizantes nitrogenados durante los siguientes 2 riegos.<br/><br/>
        💬 <em>¿Estás midiendo la Electroconductividad (EC) del drenaje o qué fertilizante has aplicado en los últimos riegos?</em>
      `;
    }

    // D) EFECTO SÉQUITO (ENTOURAGE EFFECT) & QUÍMICA DE TERPENOS
    if (query.includes('séquito') || query.includes('sequito') || query.includes('entourage') || (query.includes('por qué') && query.includes('terpeno'))) {
      return `
        🧬 <strong>El Efecto Séquito (Entourage Effect) y la Farmacología Cannábica:</strong><br/><br/>
        Propuesto por primera vez por los doctores <strong>Raphael Mechoulam</strong> y ampliado por el neurólogo <strong>Dr. Ethan Russo</strong>, el efecto séquito postula que los compuestos del cannabis <strong>no actúan de forma aislada, sino en una sinergia farmacológica holística</strong>.<br/><br/>
        <strong>¿Cómo interactúan en el organismo?</strong><br/><br/>
        1. 🧠 <strong>Modulación en los Receptores CB1 y CB2:</strong><br/>
        El THC puro administrado en aislamiento suele provocar taquicardia, ansiedad o sensación de aturdimiento. Sin embargo, en presencia de otros cannabinoides menores (CBD, CBG, CBC) y terpenos, estos actúan como moduladores alostéricos que modulan la respuesta del receptor CB1, suavizando la curva de ansiedad y potenciando la analgesia.<br/><br/>
        2. 🚪 <strong>Permeabilidad de la Barrera Hematoencefálica (Mirceno):</strong><br/>
        El <strong>Mirceno</strong> reduce la resistencia de la barrera hematoencefálica cerebral, permitiendo que el THC y otros cannabinoides penetren en las neuronas diana con mayor rapidez y eficiencia.<br/><br/>
        3. 🛡️ <strong>El Cariofileno como Cannabinoide Dietético:</strong><br/>
        El <strong>Beta-Cariofileno</strong> es el único terpeno conocido que activa directamente los receptores periféricos <strong>CB2</strong>, actuando como un potente antiinflamatorio sin producir colocón psicoactivo.<br/><br/>
        4. 💡 <strong>Preservación de Memoria (Alfa-Pineno):</strong><br/>
        El <strong>Pineno</strong> inhibe la enzima acetilcolinesterasa, lo que previene la degradación de acetilcolina en el hipocampo, contrarrestando la pérdida de memoria a corto plazo típica del consumo de THC.<br/><br/>
        💬 <em>Por esta razón, un extracto de espectro completo (Full Spectrum) o una flor curada tiene una riqueza terapéutica muy superior a los destilados de THC aislado al 99%.</em>
      `;
    }

    // E) POR QUÉ HUELE A PINO, LIMÓN, DIÉSEL O COMBUSTIBLE
    if ((query.includes('por qué') || query.includes('porque') || query.includes('a qué se debe')) && (query.includes('olor') || query.includes('huele') || query.includes('aroma') || query.includes('pino') || query.includes('limon') || query.includes('limón') || query.includes('diesel') || query.includes('gasolina'))) {
      return `
        🌲 <strong>¿Por qué el cannabis produce aromas a pino, limón, fruta o diésel?</strong><br/><br/>
        Los aromas del cannabis no son casuales: son el resultado de la biosíntesis de <strong>terpenos y compuestos orgánicos volátiles de azufre (VSC - Volatile Sulfur Compounds)</strong> que la planta desarrolló a lo largo de millones de años de evolución como defensa natural:<br/><br/>
        • <strong>Pino (Pineno):</strong> Es el mismo terpeno presente en coníferas y romero. En la naturaleza actúa como repelente natural de plagas y broncodilatador botánico.<br/>
        • <strong>Limón y Cítricos (Limoneno):</strong> Idéntico al aceite de cáscara de naranja o limón. Protege a la flor de hongos patógenos y estimula la liberación de dopamina en mamíferos.<br/>
        • <strong>Combustible / Diésel / Gasolina:</strong> Los estudios científicos recientes han descubierto que el aroma a queroseno y gas no proviene solo del Cariofileno o Mirceno, sino de <strong>compuestos orgánicos de azufre volátiles (VSC)</strong> como el <em>preniltiol</em>. Estos compuestos son biológicamente similares a los que emiten las mofetas o el ajo para disuadir a los herbívoros.<br/><br/>
        💬 <em>Cada cepa combina más de 40 terpenos distintos en ratios únicos, creando lo que los sumilleres denominamos la "huella dactilar olfativa" de la variedad.</em>
      `;
    }

    // F) ÍNDICA VS SATIVA: REALIDAD BOTÁNICA Y QUIMIOTÍPICA
    if ((query.includes('diferencia') || query.includes('por qué') || query.includes('origen')) && (query.includes('indica') || query.includes('índica') || query.includes('sativa'))) {
      return `
        🌿 <strong>La Realidad Científica: ¿Qué diferencia realmente a una Índica de una Sativa?</strong><br/><br/>
        1. 🌍 <strong>Diferencia Botánica y Geográfica (Jean-Baptiste Lamarck, 1785):</strong><br/>
        • <strong>Cannabis indica:</strong> Originaria de los valles áridos y fríos del Hindu Kush (Afganistán, Pakistán). Desarrolló hojas anchas para captar la luz solar en latitudes más altas, porte rechoncho y abundante resina pegajosa como escudo contra el viento seco y la radiación UV.<br/>
        • <strong>Cannabis sativa:</strong> Originaria de regiones ecuatoriales cálidas y húmedas (Colombia, Tailandia, México). Desarrolló hojas finas y aserradas con entrenudos largos para permitir la circulación de aire y evitar la condensación de moho.<br/><br/>
        2. 🔬 <strong>La Realidad Moderna: El Quimiotipo Terpénico:</strong><br/>
        Hoy en día, casi todas las cepas comerciales son híbridos polilinfáticos. Lo que determina que una flor te deje relajado en el sofá o activo y eufórico <strong>no es la forma de las hojas, sino el porcentaje de Mirceno</strong>:<br/>
        • Si el perfil tiene <strong>más del 0.5% de Mirceno</strong>, la interacción con el THC genera una sedación corporal profunda (efecto Índica).<br/>
        • Si el perfil tiene <strong>menos del 0.5% de Mirceno y predomina Limoneno o Terpinoleno</strong>, el efecto resulta alegre, creativo y cerebral (efecto Sativa).<br/><br/>
        💬 <em>¿Te llama más la atención la ciencia de los efectos cerebrales o los corporales para alguna necesidad concreta?</em>
      `;
    }

    // G) LAVADO DE RAÍCES (FLUSH): POR QUÉ SE HACE
    if (query.includes('lavado de ra') || query.includes('lavar ra') || query.includes('flush') || (query.includes('por qué') && query.includes('regar solo con agua'))) {
      return `
        🚿 <strong>¿Por qué se realiza el lavado de raíces antes de la cosecha?</strong><br/><br/>
        El lavado de raíces (o <em>flushing</em>) consiste en regar únicamente con agua osmotizada o declorada durante las últimas 1 a 2 semanas antes del corte:<br/><br/>
        1. 🧽 <strong>Lixiviación de Sales del Medio:</strong><br/>
        A lo largo de los meses de abonado, en el sustrato se acumulan sales de fósforo, potasio y nitratos. Regar con agua abundante a pH equilibrado sin fertilizantes solubiliza y arrastra esas sales residuales fuera de la maceta.<br/><br/>
        2. 🍽️ <strong>Metabolismo de Reservas Internas:</strong><br/>
        Al dejar de recibir comida exterior, la planta se ve obligada a consumir los nutrientes y almidones almacenados en sus propios tejidos y hojas. Esto provoca que las hojas se vuelvan amarillas en un proceso natural de autoconsumo.<br/><br/>
        3. 💨 <strong>Impacto en la Combustión y Sabor:</strong><br/>
        La clorofila no descompuesta y los nitratos residuales provocan que el humo sea acre, rasque la garganta, genere chispas en la brasa y deje una ceniza oscura y dura. Un buen lavado de raíces permite que los terpenos brillen en su máxima pureza, logrando una <strong>ceniza blanca y un humo suave</strong>.<br/><br/>
        💬 <em>¿En qué semana de floración estás y qué tipo de fertilizantes (orgánicos o minerales) has estado utilizando?</em>
      `;
    }

    // H) CURADO DE COGOLLOS Y REGLA 60/60
    if (query.includes('curado') || query.includes('curar') || query.includes('boveda') || (query.includes('por qué') && query.includes('secar'))) {
      return `
        🍯 <strong>¿Por qué el curado es tan importante como el cultivo? (Regla 60/60):</strong><br/><br/>
        El secado solo elimina el agua libre del tejido vegetal, pero la flor recién secada aún contiene mucha clorofila cruda, azúcares complejos y terpenos volátiles desestabilizados:<br/><br/>
        1. 🦠 <strong>Degradación Enzimática de la Clorofila:</strong><br/>
        Al envasar las flores secas en tarros de cristal herméticos con un <strong>58% a 62% de humedad relativa</strong> y a <strong>18-20°C</strong>, las enzimas de la planta siguen trabajando lentamente, descomponiendo la clorofila irritante y amarga en azúcares simples.<br/><br/>
        2. 🌸 <strong>Evolución y Maduración del Buqué Aromático:</strong><br/>
        Los monoterpenos más ligeros y volátiles se estabilizan mientras los sesquiterpenos se oxidan sutilmente, transformando un olor a "césped recién cortado" en el aroma maduro, complejo y resinoso definitivo.<br/><br/>
        3. 🌬️ <strong>La Técnica del "Burping" (Ventilación):</strong><br/>
        Durante las dos primeras semanas de curado, se deben abrir los frascos durante 10 a 15 minutos al día para liberar la humedad retenida en el núcleo del cogollo y renovar el oxígeno fresco.<br/><br/>
        💬 <em>¿Tienes higrómetro dentro de tus tarros de curado para monitorizar la humedad relativa?</em>
      `;
    }

    // I) TEMPERATURAS DE VAPORIZACIÓN Y EBULLICIÓN
    if (query.includes('temperatura') || query.includes('grados') || query.includes('vaporiz') || query.includes('ebullición')) {
      return `
        🌡️ <strong>Temperaturas de Ebullición de Cannabinoides y Terpenos:</strong><br/><br/>
        Al vaporizar o calentar cannabis, cada molécula tiene un punto de ebullición exacto donde pasa a estado de vapor sin combustión:<br/><br/>
        • 🌿 <strong>130°C — Beta-Cariofileno:</strong> Terpeno especiado, activa receptores CB2, potente antiinflamatorio.<br/>
        • 🌲 <strong>155°C — Alfa-Pineno:</strong> Aroma a pino, broncodilatador y protector de la memoria.<br/>
        • ⚡ <strong>157°C — THC (Delta-9-THC):</strong> Descarboxilación y activación del efecto cerebral eufórico.<br/>
        • 🥭 <strong>168°C — Mirceno:</strong> Aroma terroso/mango, relajante muscular y promotor del efecto sedante.<br/>
        • 🍋 <strong>176°C — Limoneno:</strong> Frescor cítrico, estimulante del estado de ánimo y ansiolítico.<br/>
        • 🛡️ <strong>180°C — CBD:</strong> Relajación muscular, ansiolítico y modulador de la psicoactividad.<br/>
        • 😴 <strong>185°C — CBN:</strong> Degradación del THC, máxima relajación corporal e inductor del sueño profundo.<br/>
        • 🪻 <strong>198°C — Linalool:</strong> Aroma a lavanda, sedante potente y calmante del sistema nervioso central.<br/><br/>
        💡 <em>Vaporizar entre 170°C y 185°C ofrece el mejor equilibrio entre sabor terpénico exquisito y efecto lúcido sin toxinas de combustión.</em>
      `;
    }

    // J) RESPUESTA DIDÁCTICA CIENTÍFICA GENERAL PARA CUALQUIER PREGUNTA DE "POR QUÉ" O "CÓMO"
    const isGenericWhyOrHow = /(por\s*qu[eé]|porque|por\s+que|c[oó]mo|como funciona|a\s+qu[eé]\s+se\s+debe|qu[eé]\s+es|qu[eé]\s+significa|explica)/i.test(query);
    if (isGenericWhyOrHow && !isExplicitRecommendation) {
      return `
        🔬 <strong>Explicación Botánica & Fisiológica:</strong><br/><br/>
        He analizado tu pregunta sobre <em>"${rawQuery}"</em> desde la perspectiva de la biología vegetal y la ciencia del cannabis:<br/><br/>
        1. 🧬 <strong>La Base Biológica:</strong> En el cannabis, casi todos los procesos morfológicos y químicos (producción de resina, coloración de tricomas, cambios de tonalidad foliar o asimilación de iones) responden a mecanismos de adaptación evolutiva frente a la radiación solar, la humedad ambiental y la disponibilidad de nutrientes en la rizosfera.<br/><br/>
        2. ⚖️ <strong>Factores Clave en Juego:</strong><br/>
        • <strong>Equilibrio de pH y Electroconductividad (EC):</strong> Regulan la presión osmótica que permite a los pelos radiculares ionizar minerales.<br/>
        • <strong>Déficit de Presión de Vapor (VPD):</strong> Controla la transpiración estomática y la absorción de agua.<br/>
        • <strong>Complejo Lumínico y Terpenogénesis:</strong> La intensidad lumínica (PPFD) y el espectro UV estimulan directamente la producción de tricomas defensivos cargados de cannabinoides y terpenos.<br/><br/>
        💬 <em>¿Te gustaría que desglosáramos algún punto concreto de este proceso o que analicemos los parámetros específicos de tu cultivo?</em>
      `;
    }

    // =========================================================================
    // 2. RECOMENDACIONES DE CEPAS (CUANDO EL USUARIO LAS PIDE O BUSCA SABORES/ACTIVIDADES)
    // =========================================================================

    // A) CÍTRICOS / LIMÓN / MANDARINA / NARANJA
    if (query.includes('citric') || query.includes('cítric') || query.includes('limon') || query.includes('limón') || query.includes('mandarina') || query.includes('naranja')) {
      const matches = STRAINS_DATABASE.filter(s => {
        const fl = safeFlavors(s);
        const dt = safeTerpene(s);
        return fl.some(f => f.toLowerCase().includes('limón') || f.toLowerCase().includes('cítrico') || f.toLowerCase().includes('mandarina') || f.toLowerCase().includes('naranja') || f.toLowerCase().includes('citrus')) || dt === 'limonene';
      }).sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'El usuario busca una experiencia estimulante con frescor cítrico en paladar.',
        'Priorizo cepas con dominancia en <strong>Limoneno</strong>, responsable de la elevación del ánimo y la estimulación de dopamina.',
        `Filtradas ${STRAINS_DATABASE.length} cepas del catálogo seleccionando las 3 mejor puntuadas con notas a limón exprimido y mandarina.`
      );

      return `
        ${reasoning}
        🍋 <strong>Recomendación Fundamentada — Perfil Cítrico & Refrescante:</strong>
        <br/><br/>
        En base al análisis terpénico, estas cepas combinan notas cítricas con un efecto alegre y despejado:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(245,158,11,0.25); color:#FCD34D; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | 🌿 Terpeno: ${TERPENES_INFO[s.dominantTerpene]?.name || s.dominantTerpene || 'Equilibrado'}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Para qué actividad te gustaría maridar esta selección cítrica? (Gaming, Creatividad, Paseo o Deporte)</em>
      `;
    }

    // B) FRUTAL / DULCE / ARÁNDANOS / CARAMELO / FRESA / BAYAS
    if (query.includes('frutal') || query.includes('fruta') || query.includes('frutas') || query.includes('dulce') || query.includes('arándano') || query.includes('bayas') || query.includes('caramelo') || query.includes('fresa') || query.includes('uva') || query.includes('tropica')) {
      const matches = STRAINS_DATABASE.filter(s => {
        const fl = safeFlavors(s);
        const dt = safeTerpene(s);
        return fl.some(f => f.toLowerCase().includes('dulce') || f.toLowerCase().includes('fruta') || f.toLowerCase().includes('arándano') || f.toLowerCase().includes('caramelo') || f.toLowerCase().includes('bayas') || f.toLowerCase().includes('tropical')) || dt === 'ocimene' || dt === 'terpinolene';
      }).sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(236,72,153,0.25); color:#F472B6; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | ✨ ${safeEffects(s).slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Prefieres una genética más relajante (Índica) o eufórica (Sativa) con este sabor?</em>
      `;
    }

    // C) PINO / BOSQUE / MADERA / INCIENSO HAZE / CEDRO
    if (query.includes('pino') || query.includes('bosque') || query.includes('madera') || query.includes('incienso') || query.includes('haze') || query.includes('cedro')) {
      const matches = STRAINS_DATABASE.filter(s => {
        const fl = safeFlavors(s);
        const dt = safeTerpene(s);
        return fl.some(f => f.toLowerCase().includes('pino') || f.toLowerCase().includes('madera') || f.toLowerCase().includes('incienso') || f.toLowerCase().includes('haze') || f.toLowerCase().includes('cedro')) || dt === 'pinene';
      }).sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(6,182,212,0.25); color:#67E8F9; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | 🧠 Claridad Láser</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Te gustaría maridar esta cepa con naturaleza, senderismo o creación artística?</em>
      `;
    }

    // D) DIÉSEL / GASOLINA / COMBUSTIBLE / GAS
    if (query.includes('diesel') || query.includes('diésel') || query.includes('gasolina') || query.includes('combustible') || query.includes('gas')) {
      const matches = STRAINS_DATABASE.filter(s => {
        const fl = safeFlavors(s);
        return fl.some(f => f.toLowerCase().includes('diésel') || f.toLowerCase().includes('diesel') || f.toLowerCase().includes('gasolina') || f.toLowerCase().includes('combustible'));
      }).sort((a, b) => (b.thc || 0) - (a.thc || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(16,185,129,0.25); color:#6EE7B7; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | ⚡ ${safeEffects(s).slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // E) GALLETA / COOKIES / VAINILLA / REPOSTERÍA / HELADO / CREMA
    if (query.includes('galleta') || query.includes('cookie') || query.includes('cookies') || query.includes('vainilla') || query.includes('reposteria') || query.includes('repostería') || query.includes('helado') || query.includes('crema')) {
      const matches = STRAINS_DATABASE.filter(s => {
        const fl = safeFlavors(s);
        return fl.some(f => f.toLowerCase().includes('galleta') || f.toLowerCase().includes('cookie') || f.toLowerCase().includes('vainilla') || f.toLowerCase().includes('helado') || f.toLowerCase().includes('crema') || f.toLowerCase().includes('masa'));
      }).sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(139,92,246,0.25); color:#C084FC; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | 😌 ${safeEffects(s).slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // F) QUESO / CHEESE / SKUNK
    if (query.includes('queso') || query.includes('cheese') || query.includes('skunk')) {
      const matches = STRAINS_DATABASE.filter(s => {
        const fl = safeFlavors(s);
        return fl.some(f => f.toLowerCase().includes('queso') || f.toLowerCase().includes('cheese') || f.toLowerCase().includes('skunk'));
      }).sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 3);

      const reasoning = this.buildReasoningBox(
        'Búsqueda de aromas Old School profundos a lácteo maduro y fondo Skunk.',
        'Análisis de compuestos de azufre orgánico y <strong>Mirceno potente</strong> característicos de las genéticas UK Cheese.',
        'Filtradas las variedades con buqué más añejo y bouquet terroso de Skunk tradicional.'
      );

      return `
        ${reasoning}
        🧀 <strong>Recomendación Fundamentada — Perfil Queso Curado & Skunk:</strong>
        <br/><br/>
        Variedades con buqué añejo y personalidad única para paladares exigentes:
        <br/><br/>
        ${matches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(234,179,8,0.25); color:#FDE047; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | 🥳 ${safeEffects(s).slice(0,2).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // 3. MAPEO DIRECTO CON ACTIVIDADES DEL ACTIVITY MATCHER
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
          `Mapeo de terpenos sinérgicos (<strong>${terpeneNames}</strong>) y equilibrio cannabinoide para evitar ansiedad o fatiga prematura.`,
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
            ${idx === 0 ? '🥇' : idx === 1 ? '🥈' : '🥉'} <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(16,185,129,0.2); color:#6EE7B7; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
            &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 🌿 Terpeno: ${TERPENES_INFO[s.dominantTerpene]?.name || s.dominantTerpene || 'Equilibrado'} | 👅 Sabores: ${safeFlavors(s).join(', ')}</small>
          `).join('<br/><br/>')}
          <br/><br/>
          💬 <em>¿Qué perfil de sabor prefieres para esta actividad? (🍋 Cítricos, 🍓 Frutal Dulce, 🌲 Pino Haze, ⛽ Diésel o 🍪 Galleta)</em>
        `;
      }
    }

    const hasIndica = query.includes('indica') || query.includes('índica') || query.includes('indicas') || query.includes('índicas');
    const hasSativa = query.includes('sativa') || query.includes('sativas') || query.includes('satva');

    // PETICIÓN EXPLICITA DE INDICA
    if ((hasIndica && isExplicitRecommendation) || query.includes('no quiero sativa') || query.includes('sin sativa')) {
      const indicaStrains = STRAINS_DATABASE.filter(s => (s.species || '').toLowerCase().includes('indica'));
      const topIndicas = indicaStrains.sort((a, b) => (b.thc || 0) - (a.thc || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(139,92,246,0.25); color:#C084FC; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 ${safeFlavors(s).join(', ')} | ⚡ ${safeEffects(s).join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Prefieres tu Índica con sabor a Queso 🧀, Galletas/Vainilla 🍪 o Frutas Dulces 🍓?</em>
      `;
    }

    // PETICIÓN EXPLICITA DE SATIVA
    if ((hasSativa && isExplicitRecommendation) || query.includes('no quiero indica') || query.includes('sin indica')) {
      const sativaStrains = STRAINS_DATABASE.filter(s => (s.species || '').toLowerCase().includes('sativa'));
      const topSativas = sativaStrains.sort((a, b) => (b.thc || 0) - (a.thc || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> <span style="background:rgba(245,158,11,0.25); color:#FCD34D; padding:2px 8px; border-radius:50px; font-size:0.75rem; font-weight:800;">${s.species}</span> — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">⚡ THC: ${s.thc}% | 👅 Sabores: ${safeFlavors(s).join(', ')} | ✨ ${safeEffects(s).join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Te llama más la atención el sabor Cítrico 🍋, Pino/Haze 🌲 o Diésel ⛽?</em>
      `;
    }

    // POTENCIA ALTA
    if ((query.includes('thc') || query.includes('potente') || query.includes('fuerte')) && isExplicitRecommendation) {
      const topThc = [...STRAINS_DATABASE].sort((a, b) => (b.thc || 0) - (a.thc || 0)).slice(0, 3);

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
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> (${s.species}) — <strong>${s.thc}% THC</strong> (<em>${safeBank(s)}</em>)<br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">👅 Sabores: ${safeFlavors(s).join(', ')} | ⚡ ${safeEffects(s).join(', ')}</small>
        `).join('<br/><br/>')}
        <br/><br/>
        💬 <em>¿Qué matiz aromático buscas en tu cepa potente?</em>
      `;
    }

    // BÚSQUEDA GENERAL POR PALABRA CLAVE DE CEPA O BANCO (Solo si coincide claramente con un nombre o banco)
    const searchMatches = STRAINS_DATABASE.filter(s => {
      const nm = (s.name || '').toLowerCase();
      const bk = safeBank(s).toLowerCase();
      return (query.length >= 3 && (nm.includes(query) || bk.includes(query)));
    }).slice(0, 3);

    if (searchMatches.length > 0) {
      const reasoning = this.buildReasoningBox(
        `Búsqueda personalizada para el término: <strong>"${rawQuery}"</strong>.`,
        'Filtrado terpénico y organoléptico por coincidencia en catálogo.',
        `Coincidencias encontradas en el catálogo de ${STRAINS_DATABASE.length} cepas.`
      );

      return `
        ${reasoning}
        🔍 <strong>Cepas encontradas para "${rawQuery}":</strong>
        <br/><br/>
        ${searchMatches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> (${s.species}) — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 Sabores: ${safeFlavors(s).join(', ')} | ⚡ ${safeEffects(s).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // =========================================================================
    // 3. RESPUESTA CONVERSACIONAL ABIERTA (SIN FORZAR RECOMENDACIONES)
    // =========================================================================
    return `
      🌿 <strong>Mateo:</strong> He recibido tu consulta: <em>"${rawQuery}"</em>.<br/><br/>
      Como especialista botánico, puedo responderte exactamente igual que <strong>Gemini</strong> sobre cualquier ámbito científico del cannabis:<br/><br/>
      • 🔬 <strong>Ciencia vegetal y cultivo:</strong> Explícame qué te ocurre o pregúntame el <em>porqué</em> de las hojas amarillas, exceso de abono, carencias o madurez de los tricomas.<br/>
      • 🧬 <strong>Química y Farmacología:</strong> Pregúntame sobre el efecto séquito, receptores CB1/CB2 o cómo interactúa el THC con cada terpeno.<br/>
      • 👅 <strong>Maridaje Sommelier:</strong> Si en cualquier momento deseas que te recomiende cepas de nuestro catálogo de <strong>${STRAINS_DATABASE.length} variedades</strong>, dime qué sabor o efecto buscas y te haré una selección a medida.<br/><br/>
      💬 <em>¿Qué aspecto te gustaría explorar o resolver hoy?</em>
    `;
  }
}
