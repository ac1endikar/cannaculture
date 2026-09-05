// CannaCatalog 2.0 MAX - Controlador Principal (Blindado y Defensivo)

import { STRAINS_DATABASE, TERPENES_INFO } from './data.js?v=2026_clean_v45';
import { ActivityMatcher } from './matcher.js';
import { BitacoraManager } from './bitacora.js';
import { MissionGenerator } from './missions.js';
import { AmbientAudioEngine } from './audio.js';
import { AdvancedTools } from './tools.js';
import { AISommelierAgent } from './ai-sommelier.js';

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
    this.btnHeaderCompare = document.getElementById('btn-header-compare');
    this.headerCompareBadge = document.getElementById('header-compare-badge');
    this.compareModal = document.getElementById('compare-modal');
    this.compareModalContent = document.getElementById('compare-modal-content');
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
    this.btnHeaderCompare?.addEventListener('click', () => {
      this.openCompareModal();
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

    this.updateCompareUI(false);
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

    this.updateCompareUI(true);
    if (this.compareModal && this.compareModal.open) {
      this.renderCompareModal();
    }
  }

  clearComparedStrains() {
    this.comparedStrains = [];
    try {
      localStorage.setItem('cannacatalog_compared', JSON.stringify([]));
    } catch (e) {}
    this.updateCompareUI(false);
    if (this.compareModal && this.compareModal.open) {
      this.renderCompareModal();
    }
    this.showToast('🗑️ Comparador vaciado.');
  }

  updateCompareUI(triggerGlow = false) {
    const count = (this.comparedStrains || []).length;

    // Actualizar botón discreto en cabecera del catálogo
    if (this.headerCompareBadge) {
      this.headerCompareBadge.textContent = `${count}/3`;
    }

    if (this.btnHeaderCompare) {
      if (count > 0) {
        this.btnHeaderCompare.classList.add('has-strains');
      } else {
        this.btnHeaderCompare.classList.remove('has-strains');
      }

      if (triggerGlow) {
        this.btnHeaderCompare.classList.remove('glow-pulse');
        // Forzar reflow para reiniciar animación
        void this.btnHeaderCompare.offsetWidth;
        this.btnHeaderCompare.classList.add('glow-pulse');
      }
    }

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
      this.showToast('⚖️ Selecciona hasta 3 variedades con el botón "⚖️ Comparar" en las tarjetas.');
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
              <span>⚖️</span> Comparador Cara a Cara
              <span style="font-size:0.8rem; background:rgba(16,185,129,0.2); color:#10B981; border:1px solid rgba(16,185,129,0.4); padding:3px 10px; border-radius:50px !important; font-weight:800;">${strains.length}/3 cepas</span>
            </h2>
            <div class="compare-modal-subtitle">Análisis analítico y organoléptico en columnas paralelas con Dark Glassmorphism</div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            ${strains.length > 0 ? `<button class="btn btn-outline-stash" style="padding:6px 14px; font-size:0.78rem; font-weight:700; border-radius:8px !important;" onclick="window.app && window.app.clearComparedStrains()">🗑️ Limpiar todo</button>` : ''}
            <button class="close-modal-btn compare-close-btn" onclick="document.getElementById('compare-modal').close()" title="Cerrar (ESC)" style="width:36px; height:36px; border-radius:50% !important; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.25); color:#fff; font-size:1.1rem; cursor:pointer;">✕</button>
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
