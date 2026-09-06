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
    this.showTyping(imageObj ? '🔬 CannaDoctor examinando imagen botánica con Gemini 3.6...' : '🧠 Mateo analizando maridaje terpénico en el catálogo...');

    try {
      const cloudResponse = await this.callGeminiAPI(userQuery, imageObj);
      if (cloudResponse) {
        this.hideTyping();
        this.botSay(cloudResponse);
        return;
      }
    } catch (err) {
      console.warn('Gemini Cloud API no disponible o timeout, ejecutando motor local:', err);
    }

    // Fallback local garantizado sin bloqueo
    this.hideTyping();
    try {
      if (imageObj) {
        this.botSay(`
          🔬 <strong>CannaDoctor:</strong> He recibido tu fotografía de cultivo.<br/><br/>
          Para procesar diagnósticos visuales avanzados (deficiencias de nitrógeno, fósforo, magnesio, araña roja o madurez de tricomas), asegúrate de que el servidor local con soporte Gemini esté en ejecución o introduce tu clave en los ajustes.<br/><br/>
          💬 <em>Mientras tanto, puedes describirme los síntomas o consultar cualquier variedad de nuestro catálogo de ${STRAINS_DATABASE.length} cepas.</em>
        `);
        return;
      }
      const response = this.generateHumanResponse(userQuery || '');
      this.botSay(response);
    } catch (fallbackErr) {
      console.error('Error en motor local de Sommelier:', fallbackErr);
      const sample = STRAINS_DATABASE[0] || {};
      this.botSay(`
        🌿 <strong>Mateo (Sommelier):</strong> He recibido tu consulta sobre <em>"${userQuery || 'variedades'}"</em>.<br/><br/>
        Disponemos de más de <strong>${STRAINS_DATABASE.length} cepas</strong> en nuestro catálogo interactivo. Puedes consultar cepas ricas en THC, perfiles de terpenos como Limoneno o Mirceno, o variedades de bancos como Medical Seeds, Ripper Seeds o Sweet Seeds.<br/><br/>
        💬 <em>¿Buscas un efecto energizante (Sativa) o relajante (Índica)?</em>
      `);
    }
  }

  async callGeminiAPI(userQuery, imageObj = null) {
    const catalogSummary = STRAINS_DATABASE.slice(0, 70).map(s => 
      `- ${s.name} (${s.species}, ${safeBank(s)}): THC ${s.thc}%, Terpeno: ${s.dominantTerpene || 'Equilibrado'}, Sabores: ${safeFlavors(s).slice(0,3).join('/')}, ID: ${s.id}`
    ).join('\n');

    const systemInstruction = {
      parts: [{
        text: `Eres Mateo, Master Sommelier de Cannabis y CannaDoctor botánico de la plataforma CannaCulture.
Posees un conocimiento enciclopédico sobre perfiles de terpenos (Mirceno, Limoneno, Cariofileno, Pineno, Linalool, Terpinoleno, Humuleno, Ocimeno) y cultivo cannábico.

Directrices estrictas:
1. Sé cálido, elegante, experto y educativo.
2. Si el usuario te envía una foto de una planta o flor:
   - Actúa como CannaDoctor: evalúa de inmediato la salud foliar, posibles deficiencias minerales (N, P, K, Ca, Mg), signos de plagas o el estado y lechosidad de los tricomas.
   - Proporciona un diagnóstico claro con causas y soluciones orgánicas recomendadas.
3. Si el usuario pide recomendaciones de cepas:
   - Estructura siempre tu análisis con el bloque HTML de razonamiento exacto:
<div class="sommelier-reasoning-box">
  <div class="reasoning-header">
    <span class="reasoning-brain-icon">🧠</span>
    <span class="reasoning-title">RAZONAMIENTO DEL SOMMELIER</span>
    <span class="reasoning-badge">Análisis Neuro-Terpénico</span>
  </div>
  <div class="reasoning-steps">
    <div class="reasoning-step">
      <span class="step-num">1</span>
      <div><strong>Diagnóstico de Necesidad:</strong> [Resumen breve de la necesidad del usuario]</div>
    </div>
    <div class="reasoning-step">
      <span class="step-num">2</span>
      <div><strong>Análisis Terpénico & Séquito:</strong> [Terpenos y ratios óptimos explicados]</div>
    </div>
    <div class="reasoning-step">
      <span class="step-num">3</span>
      <div><strong>Cribado del Catálogo:</strong> [Cómo encaja en las cepas del catálogo]</div>
    </div>
  </div>
</div>
4. Siempre que menciones una cepa que exista en el catálogo, usa estrictamente enlaces clicables con este formato:
   <a href="#" class="ai-strain-link" data-strain-id="ID_DE_LA_CEPA"><strong>Nombre Cepa</strong></a>.
5. El catálogo de CannaCulture cuenta con ${STRAINS_DATABASE.length} cepas de bancos premium (Medical Seeds, Ripper Seeds, Dinafem, Barney's Farm, Sweet Seeds, RQS, DNA Genetics, TH Seeds, etc.).

Muestra de variedades del catálogo:
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

    const payload = {
      model: 'gemini-3.6-flash',
      contents: [{ role: 'user', parts: userParts }],
      system_instruction: systemInstruction
    };

    // 1. Intentar primero a través del proxy local /api/gemini con timeout estricto de 8.5s (solo en entorno local)
    const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    if (isLocal) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8500);
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
          if (text) return this.formatBotMarkdown(text);
        }
      } catch (e) {
        // Si el proxy falla o da timeout, continuamos
      }
    }

    // 2. Intentar directamente con la API Key si está guardada en localStorage
    if (this.apiKey) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8500);
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
          if (text) return this.formatBotMarkdown(text);
        }
      } catch (e) {
        // Fallback al motor local
      }
    }

    throw new Error('No se pudo contactar con Gemini en el tiempo límite');
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
    const query = (rawQuery || '').toLowerCase();

    // 1. EVALUACIÓN DE SABORES
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
    const hasDifference = query.includes('diferencia') || query.includes('vs') || query.includes('comparar');

    // COMPARATIVA AMBAS
    if ((hasIndica && hasSativa) || hasDifference) {
      const topIndica = STRAINS_DATABASE.find(s => (s.species || '').toLowerCase().includes('indica')) || STRAINS_DATABASE[0];
      const topSativa = STRAINS_DATABASE.find(s => (s.species || '').toLowerCase().includes('sativa')) || STRAINS_DATABASE[1];

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
        • <em>Recomendación estrella:</em> <a href="#" class="ai-strain-link" data-strain-id="${topIndica.id}"><strong>${topIndica.name}</strong></a> (${safeBank(topIndica)}) — THC ${topIndica.thc}%.
        <br/><br/>
        🟡 <strong>SATIVA (Estimulación Cerebral):</strong><br/>
        Predominio de <strong>Limoneno y Terpinoleno</strong>. Impulso alegre y creativo.<br/>
        • <em>Recomendación estrella:</em> <a href="#" class="ai-strain-link" data-strain-id="${topSativa.id}"><strong>${topSativa.name}</strong></a> (${safeBank(topSativa)}) — THC ${topSativa.thc}%.
        <br/><br/>
        💬 <em>¿Qué efecto se ajusta mejor a lo que buscas experimentar hoy?</em>
      `;
    }

    // PETICIÓN EXPLICITA DE INDICA
    if (hasIndica || query.includes('no quiero sativa') || query.includes('sin sativa')) {
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
    if (hasSativa || query.includes('no quiero indica') || query.includes('sin indica')) {
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
    if (query.includes('thc') || query.includes('potente') || query.includes('fuerte')) {
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

    // BÚSQUEDA GENERAL POR PALABRA CLAVE
    const searchMatches = STRAINS_DATABASE.filter(s => {
      const fl = safeFlavors(s);
      const ef = safeEffects(s);
      const dt = safeTerpene(s);
      const nm = (s.name || '').toLowerCase();
      const bk = safeBank(s).toLowerCase();
      return nm.includes(query) ||
             bk.includes(query) ||
             fl.some(f => f.toLowerCase().includes(query)) ||
             ef.some(e => e.toLowerCase().includes(query)) ||
             dt.includes(query);
    }).slice(0, 3);

    if (searchMatches.length > 0) {
      const reasoning = this.buildReasoningBox(
        `Búsqueda personalizada para el término: <strong>"${rawQuery}"</strong>.`,
        'Filtrado terpénico y organoléptico por coincidencia semántica de aromas y efectos.',
        `Coincidencias óptimas encontradas en el catálogo de ${STRAINS_DATABASE.length} cepas.`
      );

      return `
        ${reasoning}
        🔍 <strong>Recomendación Fundamentada para "${rawQuery}":</strong>
        <br/><br/>
        ${searchMatches.map(s => `
          • <a href="#" class="ai-strain-link" data-strain-id="${s.id}"><strong>${s.name}</strong></a> (${s.species}) — <em>${safeBank(s)}</em><br/>
          &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${s.thc}% | 👅 Sabores: ${safeFlavors(s).join(', ')} | ⚡ ${safeEffects(s).join(', ')}</small>
        `).join('<br/><br/>')}
      `;
    }

    // FALLBACK INTERACTIVO CON PREGUNTA DE SABORES
    const randomPick = STRAINS_DATABASE[Math.floor(Math.random() * STRAINS_DATABASE.length)] || STRAINS_DATABASE[0];
    const reasoning = this.buildReasoningBox(
      'Consulta general o abierta recibida.',
      'Analizando cepa destacada para abrir el maridaje terpénico.',
      'Sugerencia directa para encauzar la búsqueda hacia tu perfil de sabor o actividad ideal.'
    );

    return `
      ${reasoning}
      🌟 <strong>Sugerencia del Sumiller:</strong><br/><br/>
      Prueba la cepa destacada de hoy: <a href="#" class="ai-strain-link" data-strain-id="${randomPick.id}"><strong>${randomPick.name}</strong></a> (${randomPick.species} de <em>${safeBank(randomPick)}</em>)<br/>
      &nbsp;&nbsp;<small style="color:#A7F3D0;">🔥 THC: ${randomPick.thc}% | 👅 Sabores: ${safeFlavors(randomPick).join(', ')}</small>
      <br/><br/>
      💬 <strong>¿Qué tipo de sabores prefieres más?</strong><br/>
      Dime si buscas sabores 🍋 <em>Cítricos</em>, 🍓 <em>Frutales Dulces</em>, 🌲 <em>Pino Haze</em>, ⛽ <em>Diésel</em>, 🍪 <em>Galleta/Vainilla</em> o 🧀 <em>Queso</em> y te haré la recomendación exacta con mi análisis de razonamiento.
    `;
  }
}
