// CannaCatalog 2.0 - Bitácora de Vivencias y Safari de Caminatas (Stash & Logbook)

export class BitacoraManager {
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
