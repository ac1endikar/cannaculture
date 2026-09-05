// CannaCatalog 2.0 - Ruleta & Matcher de Actividades

import { STRAINS_DATABASE, ACTIVITIES_DATA, TERPENES_INFO } from './data.js?v=2026_clean_v45';

export class ActivityMatcher {
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
