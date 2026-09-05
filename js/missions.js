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
