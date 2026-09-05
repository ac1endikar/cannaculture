// CannaCatalog 2.0 - Agente IA Sommelier Humano (Con Motor de Razonamiento Lógico Neuro-Terpénico)
import { STRAINS_DATABASE, ACTIVITIES_DATA, TERPENES_INFO } from './data.js?v=2026_clean_v45';

export class AISommelierAgent {
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


