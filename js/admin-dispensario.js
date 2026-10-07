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

  // Configuración por defecto del club
  const DEFAULT_CLUB_CONFIG = {
    name: "CSC Verde Esperanza",
    associationNumber: "Reg. Asoc. 08/4291-CAT",
    city: "Barcelona, España",
    currency: "€",
    kioskTitle: "Carta del Dispensario • Consumo Compartido"
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

  // Estado reactivo de la aplicación
  let state = {
    menu: [],
    clubConfig: { ...DEFAULT_CLUB_CONFIG },
    currentFilter: 'all',
    selectedStrainId: null,
    isKioskMode: false,
    strainsDb: []
  };

  let currentUser = null;
  let unsubscribeFirestore = null;

  // Helper para buscar en la base de datos de 777 cepas
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

    // Comprobar parámetro URL para modo kiosco automático (?kiosk=1)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('kiosk') === '1') {
      state.isKioskMode = true;
    }

    // Si hay elementos, seleccionar el primero por defecto en el editor
    if (state.menu.length > 0 && !state.selectedStrainId) {
      state.selectedStrainId = state.menu[0].id;
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

    // En modo Kiosco mostramos las disponibles primero
    if (state.isKioskMode) {
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

    grid.innerHTML = items.map(item => {
      const strain = getStrainData(item.id) || {
        name: item.id.replace(/-/g, ' ').toUpperCase(),
        bank: 'CannaCulture Selection',
        species: 'Híbrida',
        image: `img/${item.id}.webp`,
        lineage: 'Linaje seleccionado para socios'
      };

      const isSelected = item.id === state.selectedStrainId;
      const speciesLower = (strain.species || 'hibrida').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
      const safeLineage = (strain.lineage || strain.genetics || 'Linaje botánico de alta pureza').replace(/"/g, '&quot;');
      const safeLotNotes = (item.lotNotes || 'Lote estándar del dispensario').replace(/"/g, '&quot;');
      const safeName = (strain.name || item.id).replace(/"/g, '&quot;');

      return `
        <article class="strain-menu-card ${isSelected ? 'selected' : ''} ${!item.available ? 'out-of-stock' : ''}" 
                 data-strain-id="${item.id}">
          <div class="card-top">
            <div class="card-photo-wrapper" data-spec-id="${item.id}" title="Ver ficha botánica y fotografía HD de ${safeName}">
              <img src="${strain.image || 'img/' + item.id + '.webp'}" 
                   alt="${safeName}" 
                   class="card-photo"
                   loading="lazy"
                   onerror="this.src='img/ths-darkstar-official.webp';" />
              <span class="species-chip ${speciesLower}">${strain.species || 'Híbrida'}</span>
            </div>
            
            <div class="card-headline">
              <h3 title="${safeName}">${strain.name}</h3>
              <p class="card-bank">🏛️ ${strain.bank || 'Banco Criador'}</p>
              <p class="card-lineage" title="${safeLineage}">🧬 ${strain.lineage || strain.genetics || 'Linaje botánico de alta pureza'}</p>
            </div>
          </div>

          <!-- Interruptor de disponibilidad en mostrador -->
          <div class="availability-control">
            <span class="availability-label ${item.available ? 'is-available' : 'is-out'}">
              ${item.available ? '🟢 En Barra / Disponible' : '⚪ Agotado / En reserva'}
            </span>
            <label class="toggle-switch" title="Alternar disponibilidad">
              <input type="checkbox" class="toggle-avail-input" data-strain-id="${item.id}" ${item.available ? 'checked' : ''}>
              <span class="toggle-slider"></span>
            </label>
          </div>

          <!-- Cuadro de cuotas de previsión / aportaciones -->
          <div class="card-tiers-row" title="Cuadro de aportaciones del club por niveles de socio">
            <div class="tier-mini-box tier-std">
              <div class="tier-mini-title">Estándar</div>
              <div class="tier-mini-val">${item.tierStd.toFixed(2)}€/g</div>
            </div>
            <div class="tier-mini-box tier-colab">
              <div class="tier-mini-title">Colaborador</div>
              <div class="tier-mini-val">${item.tierColab.toFixed(2)}€/g</div>
            </div>
            <div class="tier-mini-box tier-terap">
              <div class="tier-mini-title">Terapéutico</div>
              <div class="tier-mini-val">${item.tierTerap.toFixed(2)}€/g</div>
            </div>
          </div>

          <!-- Nota de lote botánico / cata local (legibilidad fluida en 2 líneas) -->
          <p class="card-lot-note" title="${safeLotNotes}">📋 ${item.lotNotes || 'Lote estándar del dispensario'}</p>

          <!-- Píldora de interacción táctil visible en Modo Kiosco -->
          <div class="kiosk-tap-pill" data-spec-id="${item.id}">
            <span>🔬</span>
            <span>Toca para ver Ficha Botánica & Terpenos</span>
          </div>

          <!-- Acciones de tarjeta en Modo Encargado -->
          <div class="card-actions">
            <button class="btn-card-spec" data-spec-id="${item.id}" title="Ver Ficha Técnica Botánica Completa">
              🔬 Ficha
            </button>
            <button class="btn-card-edit" data-edit-id="${item.id}" title="Editar aportaciones y notas de lote">
              ✏️ Modificar
            </button>
            <button class="btn-card-delete" data-delete-id="${item.id}" title="Retirar de la carta">
              🗑️
            </button>
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
  // Buscador del Catálogo Maestro (777 cepas)
  // ==========================================================================
  function setupCatalogSearch() {
    const searchInput = document.getElementById('catalog-search-input');
    const dropdown = document.getElementById('search-results-dropdown');
    if (!searchInput || !dropdown) return;

    let debounceTimer;

    searchInput.addEventListener('input', (e) => {
      clearTimeout(debounceTimer);
      const query = e.target.value.trim().toLowerCase();

      if (query.length < 2) {
        dropdown.classList.remove('active');
        dropdown.innerHTML = '';
        return;
      }

      debounceTimer = setTimeout(() => {
        executeSearch(query);
      }, 150);
    });

    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove('active');
      }
    });

    function executeSearch(query) {
      if (!state.strainsDb || !state.strainsDb.length) {
        dropdown.innerHTML = `<div style="padding: 16px; text-align: center; color: var(--text-muted);">Cargando catálogo maestro...</div>`;
        dropdown.classList.add('active');
        return;
      }

      const matches = state.strainsDb.filter(s => {
        const nameMatch = s.name && s.name.toLowerCase().includes(query);
        const bankMatch = s.bank && s.bank.toLowerCase().includes(query);
        const genMatch = s.genetics && s.genetics.toLowerCase().includes(query);
        const lineageMatch = s.lineage && s.lineage.toLowerCase().includes(query);
        return nameMatch || bankMatch || genMatch || lineageMatch;
      }).slice(0, 10);

      if (matches.length === 0) {
        dropdown.innerHTML = `
          <div style="padding: 16px; text-align: center; color: var(--text-dim); font-size: 0.88rem;">
            No se encontraron variedades para "<strong>${query}</strong>"
          </div>
        `;
        dropdown.classList.add('active');
        return;
      }

      dropdown.innerHTML = matches.map(s => {
        const isAlreadyInMenu = state.menu.some(m => m.id === s.id);
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
                  <span>🏛️ ${s.bank}</span>
                  <span>•</span>
                  <span>🧬 ${s.species || 'Híbrida'} (THC: ${s.thc || 20}%)</span>
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

      return `
        <div class="terpene-row">
          <div class="terpene-row-info">
            <span class="terpene-name" style="color: ${col};">
              🧬 ${info.name || key}
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
    const effects = Array.isArray(strain.effects) && strain.effects.length > 0 ? strain.effects : ['Relajación Corporal', 'Calma Profunda', 'Bienestar'];
    const flavors = Array.isArray(strain.flavors) && strain.flavors.length > 0 ? strain.flavors : ['Terroso Floral', 'Cítrico Fresco', 'Matices Herbales'];

    const effectsHtml = effects.map(eff => `<span class="spec-tag effect">✨ ${eff}</span>`).join('');
    const flavorsHtml = flavors.map(flv => `<span class="spec-tag flavor">🍋 ${flv}</span>`).join('');

    return `
      <div style="margin-bottom: 14px;">
        <div style="font-size: 0.76rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px;">Efectos & Sensaciones Botánicas</div>
        <div class="spec-tags-grid">${effectsHtml}</div>
      </div>
      <div>
        <div style="font-size: 0.76rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px;">Perfil de Cata & Notas Aromáticas</div>
        <div class="spec-tags-grid">${flavorsHtml}</div>
      </div>
    `;
  }

  function openKioskStrainModal(strainId) {
    const modal = document.getElementById('kiosk-strain-modal');
    const modalBody = document.getElementById('kiosk-modal-body');
    if (!modal || !modalBody) return;

    const item = state.menu.find(m => m.id === strainId);
    const strain = getStrainData(strainId) || {
      name: strainId.replace(/-/g, ' ').toUpperCase(),
      bank: 'CannaCulture Selection',
      species: 'Híbrida',
      image: `img/${strainId}.webp`,
      lineage: 'Linaje seleccionado para socios',
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
    const stars = '★'.repeat(Math.round(strain.rating || 5)) + '☆'.repeat(5 - Math.round(strain.rating || 5));
    const photoUrl = strain.image || `img/${strain.id}.webp`;
    const safeName = (strain.name || 'Variedad').replace(/"/g, '&quot;');
    const safeBank = (strain.bank || 'Banco').replace(/"/g, '&quot;');

    modalBody.innerHTML = `
      <!-- HERO PRINCIPAL DE LA VARIEDAD -->
      <section class="spec-hero">
        <div class="spec-photo-wrap" id="spec-photo-click" title="Toca para ampliar en fotografía macro HD">
          <img src="${photoUrl}" 
               alt="${safeName}" 
               class="spec-photo-img" 
               onerror="this.src='img/ths-darkstar-official.webp';" />
          <div class="spec-zoom-badge">🔍 Toca para Zoom HD</div>
        </div>

        <div class="spec-hero-meta">
          <div class="spec-badges-row">
            <span class="species-chip ${speciesLower}" style="position:static; padding:4px 10px; font-size:0.75rem;">
              ${strain.species || 'Híbrida'}
            </span>
            <span class="spec-bank-pill">🏛️ ${strain.bank || 'Banco Criador'}</span>
            <span style="color: #FBBF24; font-size: 0.85rem; font-weight: 700;">${stars}</span>
          </div>

          <h2 class="spec-title">${strain.name}</h2>
          <div class="spec-lineage">🧬 Linaje Parental: ${strain.lineage || strain.genetics || 'Selección botánica de alta pureza'}</div>

          <div class="spec-cannabinoids">
            <div class="cannabinoid-chip" style="color:#34D399;">
              🌿 THC: <strong>${strain.thc || 22}%</strong>
            </div>
            <div class="cannabinoid-chip" style="color:#06B6D4;">
              🧪 CBD: <strong>${strain.cbd || 0.1}%</strong>
            </div>
            ${strain.floweringDays ? `
            <div class="cannabinoid-chip" style="color:#FBBF24;">
              ⏱️ Floración: <strong>${strain.floweringDays}d</strong>
            </div>` : ''}
          </div>
        </div>
      </section>

      <!-- CUADRO DE APORTACIONES DEL CLUB (CONSUMO COMPARTIDO) -->
      <section class="spec-tiers-box">
        <div class="spec-tiers-header">
          <h3>
            <span>⚖️</span>
            <span>Previsión de Aportaciones del Club (Consumo Compartido)</span>
          </h3>
          <span class="spec-avail-pill ${itemData.available ? 'is-avail' : 'is-out'}">
            ${itemData.available ? '🟢 Disponible en Mostrador' : '⚪ Agotado / En reserva'}
          </span>
        </div>

        <div class="spec-tiers-grid">
          <div class="spec-tier-card std">
            <div class="spec-tier-name">Nivel Estándar</div>
            <div class="spec-tier-val">${itemData.tierStd.toFixed(2)}€/g</div>
            <div class="spec-tier-desc">Socio General</div>
          </div>
          <div class="spec-tier-card colab">
            <div class="spec-tier-name">Nivel Colaborador</div>
            <div class="spec-tier-val">${itemData.tierColab.toFixed(2)}€/g</div>
            <div class="spec-tier-desc">Socio Activo (-10%)</div>
          </div>
          <div class="spec-tier-card terap">
            <div class="spec-tier-name">Nivel Terapéutico</div>
            <div class="spec-tier-val">${itemData.tierTerap.toFixed(2)}€/g</div>
            <div class="spec-tier-desc">Socio Médico (-25%)</div>
          </div>
        </div>

        <!-- NOTAS DEL LOTE AGRONÓMICO Y CURADO -->
        <div class="spec-lot-card" style="margin-top: 14px;">
          <div class="spec-lot-title">📋 Notas Agronómicas & Curado del Lote Local</div>
          <div class="spec-lot-text">${itemData.lotNotes || 'Lote seleccionado y curado en condiciones óptimas de conservación.'}</div>
        </div>
      </section>

      <!-- TERPENOS, AROMAS Y PERFIL BOTÁNICO -->
      <section class="spec-terpenes-card">
        <div class="spec-section-heading">
          <span>🧬</span>
          <span>Perfil Terpénico & Aromas Dominantes</span>
        </div>

        <div class="terpene-bars-container">
          ${renderTerpenesSection(strain)}
        </div>

        ${renderEffectsAndFlavors(strain)}

        ${strain.description ? `
        <div class="spec-desc-text">
          <strong>Ficha Botánica Oficial:</strong> ${strain.description}
        </div>` : ''}
      </section>
    `;

    const photoBox = document.getElementById('spec-photo-click');
    if (photoBox) {
      photoBox.addEventListener('click', () => {
        openKioskLightbox(photoUrl, strain.name, `🏛️ ${strain.bank} • ${strain.species}`);
      });
    }

    modal.showModal();
  }

  function openKioskLightbox(imgSrc, title, subtitle) {
    const dialog = document.getElementById('kiosk-lightbox-dialog');
    const imgEl = document.getElementById('kiosk-lightbox-img');
    const titleEl = document.getElementById('kiosk-lightbox-title');
    const subEl = document.getElementById('kiosk-lightbox-subtitle');

    if (!dialog || !imgEl) return;
    imgEl.src = imgSrc;
    if (titleEl) titleEl.textContent = title || 'Fotografía Botánica HD';
    if (subEl) subEl.textContent = subtitle || 'ALTA RESOLUCIÓN • MACRO 800×800';

    dialog.showModal();
  }

  function setupKioskModalListeners() {
    const modal = document.getElementById('kiosk-strain-modal');
    const closeBtn = document.getElementById('btn-close-kiosk-modal');

    if (closeBtn && modal) {
      closeBtn.addEventListener('click', () => modal.close());
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
          modal.close();
        }
      });
    }

    const lightbox = document.getElementById('kiosk-lightbox-dialog');
    const closeLightboxBtn = document.getElementById('btn-close-kiosk-lightbox');

    if (closeLightboxBtn && lightbox) {
      closeLightboxBtn.addEventListener('click', () => lightbox.close());
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
          lightbox.close();
        }
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (lightbox && lightbox.open) lightbox.close();
        else if (modal && modal.open) modal.close();
      }
    });
  }

  // ==========================================================================
  // Manejo de Eventos en Grid (Toggles, Edición, Eliminación, Ficha Técnica)
  // ==========================================================================
  function setupGridEvents() {
    const grid = document.getElementById('strains-menu-grid');
    if (!grid) return;

    grid.addEventListener('click', (e) => {
      // 1. Click en botón o foto de Ficha Técnica
      const specBtn = e.target.closest('[data-spec-id]');
      if (specBtn) {
        const sid = specBtn.getAttribute('data-spec-id');
        openKioskStrainModal(sid);
        return;
      }

      // 2. Si está en Modo Kiosco, hacer click sobre cualquier parte de la tarjeta abre la Ficha Técnica
      if (state.isKioskMode || document.body.classList.contains('kiosk-mode')) {
        const card = e.target.closest('.strain-menu-card');
        if (card && !e.target.closest('.availability-control')) {
          const sid = card.getAttribute('data-strain-id');
          if (sid) {
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
          document.getElementById('editor-panel-card').scrollIntoView({ behavior: 'smooth' });
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
  // Inicialización del DOM
  // ==========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    initData();
    initFirebaseSync();
    setupCatalogSearch();
    setupCategoryTabs();
    setupGridEvents();
    setupKioskMode();
    setupKioskModalListeners();
    setupClubSettings();
    renderMenuGrid();
    renderEditorPanel();

    if (!state.strainsDb || state.strainsDb.length === 0) {
      setTimeout(() => {
        if (window.STRAINS_DATABASE) {
          state.strainsDb = window.STRAINS_DATABASE;
          renderMenuGrid();
          renderEditorPanel();
        }
      }, 350);
    }
  });

})();
