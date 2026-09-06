// CannaCatalog 2.0 - Generador de Misiones Temáticas

import { STRAINS_DATABASE, TERPENES_INFO } from './data.js?v=2026_clean_v45';

export class MissionGenerator {
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

  static async generateMissionAsync(strainId, activityId) {
    const fallbackMission = this.generateMission(strainId, activityId);
    const strain = STRAINS_DATABASE.find(s => s.id === strainId) || STRAINS_DATABASE[0];
    const dominantTerpene = strain.dominantTerpene;
    const terpeneName = TERPENES_INFO[dominantTerpene]?.name || dominantTerpene || 'Equilibrado';

    const apiKey = localStorage.getItem('gemini_api_key');
    const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

    if (!isLocal && !apiKey) {
      return fallbackMission;
    }

    const safeFlavors = (s) => (Array.isArray(s?.flavors) && s.flavors.length > 0) ? s.flavors : (s?.aroma ? [s.aroma] : ['Equilibrado']);
    const safeEffects = (s) => (Array.isArray(s?.effects) && s.effects.length > 0) ? s.effects : (s?.effect ? [s.effect] : ['Relajación']);

    const prompt = `Actúa como el Diseñador Maestro de Misiones Botánicas y Sensoriales de CannaCulture.
Genera una misión lúdica, inmersiva y de bienestar única para la cepa "${strain.name}":
- Especie: ${strain.species} (Banco: ${strain.breeder || strain.bank || 'Premium'})
- THC: ${strain.thc}% | CBD: ${strain.cbd || 0.1}%
- Terpeno dominante: ${terpeneName}
- Perfil aromático y sabores: ${safeFlavors(strain).join(', ')}
- Efectos reportados: ${safeEffects(strain).join(', ')}

Diseña una experiencia sensorial que aproveche la farmacología y terpenos de esta variedad (estimulante/creativa si es sativa o relajante/inmersiva si es índica).
Devuelve EXCLUSIVAMENTE un bloque JSON válido (sin markdown exterior) con este formato exacto:
{
  "title": "🎮 Misión: [Título Épico y Poético de la Experiencia]",
  "tasks": [
    "Paso 1 de preparación sensorial o ambiente sonoro",
    "Paso 2 de degustación, inhalación lenta y apreciación terpénica",
    "Paso 3 de inmersión en la actividad (arte, paseo, cine, introspección, etc.)",
    "Paso 4 de cierre de relajación profunda o reflexión"
  ],
  "audioStyle": "[Género musical o atmósfera sonora recomendada]"
}`;

    const payload = {
      model: 'gemini-3.8-flash',
      contents: [{ role: 'user', parts: [{ text: prompt }] }]
    };

    try {
      let rawJson = null;
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 12000);

      if (isLocal) {
        const res = await fetch('/api/gemini', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          signal: controller.signal
        });
        clearTimeout(timeoutId);
        if (res.ok) {
          const data = await res.json();
          rawJson = data.candidates?.[0]?.content?.parts?.[0]?.text;
        }
      } else if (apiKey) {
        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${apiKey}`;
        const res = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ contents: payload.contents }),
          signal: controller.signal
        });
        clearTimeout(timeoutId);
        if (res.ok) {
          const data = await res.json();
          rawJson = data.candidates?.[0]?.content?.parts?.[0]?.text;
        }
      }

      if (rawJson) {
        let clean = rawJson.trim();
        if (clean.startsWith('```json')) clean = clean.slice(7);
        if (clean.startsWith('```')) clean = clean.slice(3);
        if (clean.endsWith('```')) clean = clean.slice(0, -3);
        const parsed = JSON.parse(clean.trim());

        if (parsed.title && Array.isArray(parsed.tasks) && parsed.tasks.length > 0) {
          return {
            id: 'mission_ai_' + Date.now(),
            strainName: strain.name,
            strainSpecies: strain.species,
            terpeneName: terpeneName,
            title: parsed.title,
            tasks: parsed.tasks,
            audioStyle: parsed.audioStyle || 'Ambient Relax'
          };
        }
      }
    } catch (e) {
      console.log('Fallo generando misión IA, usando plantilla local:', e.message);
    }

    return fallbackMission;
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
