// ==========================================================================
// CANNACATALOG 2.0 MAX - SISTEMA DE COMUNIDAD, FIREBASE AUTH, FAVORITOS Y RESEÑAS
// ==========================================================================

export class CommunityManager {
  constructor() {
    this.auth = window.auth || (typeof firebase !== 'undefined' ? firebase.auth() : null);
    this.db = window.db || (typeof firebase !== 'undefined' ? firebase.firestore() : null);
    this.googleProvider = window.googleProvider || (typeof firebase !== 'undefined' ? new firebase.auth.GoogleAuthProvider() : null);
    
    this.currentUser = null;
    this.userFavorites = new Set();
    this.currentModalStrainId = null;
    this.selectedRating = 5;
    this.isInitialized = false;
  }

  init() {
    if (this.isInitialized) return;
    this.isInitialized = true;

    // Reconectar referencias globales si se montaron asíncronamente
    if (!this.auth && window.auth) this.auth = window.auth;
    if (!this.db && window.db) this.db = window.db;
    if (!this.googleProvider && window.googleProvider) this.googleProvider = window.googleProvider;

    if (this.auth) {
      this.auth.onAuthStateChanged((user) => {
        this.currentUser = user;
        this.updateHeaderAuthUI(user);
        if (user) {
          this.loadUserFavorites(user.uid);
        } else {
          this.userFavorites.clear();
          this.updateAllFavoriteHearts();
        }
      });
    } else {
      console.warn('⚠️ CommunityManager: Firebase Auth no está listo en el arranque.');
    }
  }

  // 1. AUTENTICACIÓN CON GOOGLE
  async loginWithGoogle() {
    try {
      if (!this.auth || !this.googleProvider) {
        if (typeof firebase !== 'undefined') {
          this.auth = firebase.auth();
          this.googleProvider = new firebase.auth.GoogleAuthProvider();
        } else {
          alert('El servicio de autenticación de Google se está conectando. Por favor, intenta de nuevo en unos segundos.');
          return null;
        }
      }
      this.googleProvider.setCustomParameters({ prompt: 'select_account' });
      const result = await this.auth.signInWithPopup(this.googleProvider);
      const user = result.user;
      
      if (window.app && typeof window.app.showToast === 'function') {
        window.app.showToast(`🌿 ¡Bienvenido(a), ${user.displayName || 'Compañero Cannábico'}!`);
      }
      return user;
    } catch (error) {
      console.error('Error en Google Sign-In:', error);
      if (error.code !== 'auth/popup-closed-by-user' && error.code !== 'auth/cancelled-popup-request') {
        alert(`Error al iniciar sesión con Google: ${error.message}`);
      }
      return null;
    }
  }

  async logout() {
    try {
      if (this.auth) {
        await this.auth.signOut();
        this.currentUser = null;
        this.userFavorites.clear();
        this.updateAllFavoriteHearts();
        this.updateHeaderAuthUI(null);
        if (window.app && typeof window.app.showToast === 'function') {
          window.app.showToast('👋 Has cerrado sesión correctamente.');
        }
      }
    } catch (error) {
      console.error('Error cerrando sesión:', error);
    }
  }

  // 2. ACTUALIZACIÓN DEL ESTADO DE AUTENTICACIÓN EN EL HEADER
  updateHeaderAuthUI(user) {
    const container = document.getElementById('auth-container');
    if (!container) return;

    if (user) {
      const firstName = (user.displayName || 'Usuario').split(' ')[0];
      const photo = user.photoURL || '';

      container.innerHTML = `
        <div class="auth-user-session" style="display: inline-flex; align-items: center; gap: 6px;">
          <div class="auth-pill-user" title="${user.displayName || ''} (${user.email || ''})" style="display: inline-flex; align-items: center; gap: 6px; background: rgba(16,185,129,0.18); border: 1px solid rgba(16,185,129,0.45); padding: 3px 10px 3px 4px; border-radius: 50px; cursor: pointer;" onclick="window.communityManager.openUserProfileModal()">
            ${photo ? `<img src="${photo}" alt="${user.displayName}" style="width: 22px; height: 22px; border-radius: 50%; object-fit: cover; border: 1.5px solid #10B981;" onerror="this.style.display='none'" />` : `<span style="font-size: 0.9rem;">👤</span>`}
            <span style="font-size: 0.72rem; font-weight: 800; color: #6EE7B7; max-width: 85px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${firstName}</span>
          </div>
          <button id="btn-header-logout" class="btn-logout-pill" onclick="window.communityManager.logout()" title="Cerrar Sesión" style="background: rgba(239,68,68,0.2); border: 1px solid rgba(239,68,68,0.45); color: #FCA5A5; padding: 3px 8px; border-radius: 50px; font-size: 0.68rem; font-weight: 800; cursor: pointer; display: inline-flex; align-items: center; gap: 3px; transition: all 0.2s ease;">
            🚪 Salir
          </button>
        </div>
      `;
    } else {
      container.innerHTML = `
        <button id="btn-user-auth" class="btn btn-auth-pill" onclick="window.communityManager.loginWithGoogle()" title="Iniciar sesión con Google" aria-label="Iniciar sesión con Google">
          <svg width="13" height="13" viewBox="0 0 24 24" style="vertical-align: middle; flex-shrink: 0;"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.665-5.17 3.665-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.35 24 12 24z"/><path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.25C.45 8.18 0 9.99 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.35 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/></svg>
          <span id="auth-btn-text">Iniciar con Google</span>
        </button>
      `;
    }
  }

  openUserProfileModal() {
    if (!this.currentUser) {
      this.loginWithGoogle();
      return;
    }
    const modal = document.getElementById('auth-modal');
    const formsWrapper = document.getElementById('auth-forms-wrapper');
    const profileWrapper = document.getElementById('auth-profile-wrapper');
    
    if (formsWrapper) formsWrapper.style.display = 'none';
    if (profileWrapper) profileWrapper.style.display = 'block';

    const pName = document.getElementById('profile-user-name');
    const pEmail = document.getElementById('profile-user-email');
    const pLogs = document.getElementById('profile-stats-logs');
    
    if (pName) pName.textContent = this.currentUser.displayName || 'Usuario Google';
    if (pEmail) pEmail.textContent = this.currentUser.email || '';
    if (pLogs) pLogs.textContent = this.userFavorites.size;
    const pLogsLabel = pLogs?.previousElementSibling;
    if (pLogsLabel) pLogsLabel.textContent = '❤️ Cepas Favoritas';

    if (modal && typeof modal.showModal === 'function') {
      if (!modal.open) modal.showModal();
    }
  }

  // 3. SISTEMA DE FAVORITOS (COLECCIÓN FIRESTORE users/${uid}/favorites)
  async loadUserFavorites(uid) {
    if (!this.db || !uid) return;
    try {
      const snap = await this.db.collection('users').doc(uid).collection('favorites').get();
      this.userFavorites = new Set(snap.docs.map(doc => doc.id));
      this.updateAllFavoriteHearts();
      
      // Sincronizar con Stash de bitácora si existe
      if (window.app && window.app.bitacora) {
        this.userFavorites.forEach(id => {
          if (!window.app.bitacora.stash.includes(id)) {
            window.app.bitacora.stash.push(id);
          }
        });
        window.app.updateStashCounter();
      }
    } catch (err) {
      console.error('Error recuperando favoritos de Firestore:', err);
    }
  }

  isFavorite(strainId) {
    return this.userFavorites.has(strainId);
  }

  async toggleFavorite(strainId) {
    if (!this.currentUser) {
      const user = await this.loginWithGoogle();
      if (!user) return; // Si cancela el popup
    }

    const uid = this.currentUser.uid;
    const isFav = this.userFavorites.has(strainId);

    if (isFav) {
      // Quitar de favoritos
      this.userFavorites.delete(strainId);
      this.updateFavoriteButtonUI(strainId, false);
      if (window.app && typeof window.app.showToast === 'function') {
        window.app.showToast('💔 Cepa eliminada de tus favoritos');
      }
      try {
        if (this.db) {
          await this.db.collection('users').doc(uid).collection('favorites').doc(strainId).delete();
        }
      } catch (err) {
        console.error('Error eliminando de Firestore:', err);
      }
    } else {
      // Agregar a favoritos
      this.userFavorites.add(strainId);
      this.updateFavoriteButtonUI(strainId, true);
      if (window.app && typeof window.app.showToast === 'function') {
        window.app.showToast('❤️ ¡Cepa guardada en tus favoritos!');
      }
      try {
        if (this.db) {
          await this.db.collection('users').doc(uid).collection('favorites').doc(strainId).set({
            strainId: strainId,
            addedAt: firebase.firestore.FieldValue ? firebase.firestore.FieldValue.serverTimestamp() : new Date().toISOString()
          });
        }
      } catch (err) {
        console.error('Error guardando en Firestore:', err);
      }
    }

    // Mantener sincronía con Stash local
    if (window.app && window.app.bitacora) {
      const idx = window.app.bitacora.stash.indexOf(strainId);
      if (isFav && idx !== -1) {
        window.app.bitacora.stash.splice(idx, 1);
      } else if (!isFav && idx === -1) {
        window.app.bitacora.stash.push(strainId);
      }
      window.app.updateStashCounter();
    }
  }

  updateFavoriteButtonUI(strainId, isFav) {
    // 1. Corazón en el banner de la tarjeta
    document.querySelectorAll(`.card-fav-btn[data-strain-id="${strainId}"]`).forEach(btn => {
      btn.classList.toggle('active', isFav);
      btn.innerHTML = `<span class="fav-icon">${isFav ? '❤️' : '🤍'}</span>`;
      btn.title = isFav ? 'Quitar de Favoritos' : 'Guardar en Favoritos';
    });

    // 2. Corazón en los botones de acción de la tarjeta
    document.querySelectorAll(`.btn-fav-toggle[data-strain-id="${strainId}"]`).forEach(btn => {
      btn.classList.toggle('active', isFav);
      btn.innerHTML = isFav ? '❤️' : '🤍';
      btn.title = isFav ? 'Quitar de Favoritos' : 'Añadir a Favoritos';
    });

    // 3. Botón en el modal de detalle
    document.querySelectorAll(`.modal-fav-btn[data-strain-id="${strainId}"]`).forEach(btn => {
      btn.classList.toggle('active', isFav);
      btn.innerHTML = isFav ? '❤️ En tus Favoritos' : '🤍 Guardar en Favoritos';
    });
  }

  updateAllFavoriteHearts() {
    document.querySelectorAll('.card-fav-btn[data-strain-id]').forEach(btn => {
      const id = btn.getAttribute('data-strain-id');
      const isFav = this.userFavorites.has(id);
      btn.classList.toggle('active', isFav);
      btn.innerHTML = `<span class="fav-icon">${isFav ? '❤️' : '🤍'}</span>`;
      btn.title = isFav ? 'Quitar de Favoritos' : 'Guardar en Favoritos';
    });

    document.querySelectorAll('.btn-fav-toggle[data-strain-id]').forEach(btn => {
      const id = btn.getAttribute('data-strain-id');
      const isFav = this.userFavorites.has(id);
      btn.classList.toggle('active', isFav);
      btn.innerHTML = isFav ? '❤️' : '🤍';
      btn.title = isFav ? 'Quitar de Favoritos' : 'Añadir a Favoritos';
    });

    document.querySelectorAll('.modal-fav-btn[data-strain-id]').forEach(btn => {
      const id = btn.getAttribute('data-strain-id');
      const isFav = this.userFavorites.has(id);
      btn.classList.toggle('active', isFav);
      btn.innerHTML = isFav ? '❤️ En tus Favoritos' : '🤍 Guardar en Favoritos';
    });
  }

  // 4. PESTAÑA DE RESEÑAS Y VIVENCIAS EN MODAL DE DETALLE
  switchModalTab(tab) {
    const tabSpec = document.getElementById('tab-btn-spec');
    const tabReviews = document.getElementById('tab-btn-reviews');
    const contentSpec = document.getElementById('modal-tab-spec-content');
    const contentReviews = document.getElementById('modal-tab-reviews-content');

    if (tab === 'spec') {
      tabSpec?.classList.add('active');
      tabReviews?.classList.remove('active');
      if (contentSpec) contentSpec.style.display = 'block';
      if (contentReviews) contentReviews.style.display = 'none';
    } else {
      tabSpec?.classList.remove('active');
      tabReviews?.classList.add('active');
      if (contentSpec) contentSpec.style.display = 'none';
      if (contentReviews) {
        contentReviews.style.display = 'block';
        if (this.currentModalStrainId) {
          this.loadAndRenderReviews(this.currentModalStrainId, contentReviews);
        }
      }
    }
  }

  async initModalForStrain(strainId) {
    this.currentModalStrainId = strainId;
    this.selectedRating = 5;

    // Actualizar badge de conteo preliminar
    const badge = document.getElementById('modal-reviews-count-badge');
    if (badge) badge.textContent = '...';

    if (this.db) {
      try {
        const snap = await this.db.collection('reviews').where('strainId', '==', strainId).get();
        if (badge) badge.textContent = snap.docs.length;
      } catch (err) {
        if (badge) badge.textContent = '0';
      }
    } else if (badge) {
      badge.textContent = '0';
    }
  }

  async loadAndRenderReviews(strainId, container) {
    if (!container) return;

    container.innerHTML = `
      <div style="text-align: center; padding: 2.5rem 1rem; color: var(--text-muted);">
        <div style="font-size: 2rem; margin-bottom: 0.6rem; animation: sobrioPulse 1.5s infinite;">⭐</div>
        <p style="font-size: 0.9rem; font-weight: 600;">Cargando vivencias y valoraciones de la comunidad...</p>
      </div>
    `;

    try {
      let reviews = [];
      if (this.db) {
        const snap = await this.db.collection('reviews').where('strainId', '==', strainId).get();
        reviews = snap.docs.map(d => ({ id: d.id, ...d.data() }));
        // Ordenar client-side por fecha descendente
        reviews.sort((a, b) => {
          const tA = a.createdAt?.toMillis ? a.createdAt.toMillis() : (a.createdAt ? new Date(a.createdAt).getTime() : 0);
          const tB = b.createdAt?.toMillis ? b.createdAt.toMillis() : (b.createdAt ? new Date(b.createdAt).getTime() : 0);
          return tB - tA;
        });
      }

      const badge = document.getElementById('modal-reviews-count-badge');
      if (badge) badge.textContent = reviews.length;

      this.renderReviewsDOM(strainId, reviews, container);
    } catch (err) {
      console.error('Error al cargar reseñas:', err);
      container.innerHTML = `
        <div style="padding: 1.5rem; text-align: center; background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.3); border-radius: 12px; color: #FCA5A5;">
          <p>⚠️ No se pudieron cargar las reseñas en este momento.</p>
        </div>
      `;
    }
  }

  renderReviewsDOM(strainId, reviews, container) {
    const totalReviews = reviews.length;
    const avgScore = totalReviews > 0
      ? (reviews.reduce((acc, r) => acc + (Number(r.rating) || 5), 0) / totalReviews).toFixed(1)
      : '5.0';

    const starsHtml = '★'.repeat(Math.round(avgScore)) + '☆'.repeat(5 - Math.round(avgScore));

    const formHtml = this.currentUser ? `
      <div class="review-compose-box" style="background: rgba(16,185,129,0.06); border: 1.5px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 1.25rem; margin-bottom: 1.5rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.9rem; flex-wrap: wrap; gap: 8px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            ${this.currentUser.photoURL ? `<img src="${this.currentUser.photoURL}" style="width: 28px; height: 28px; border-radius: 50%; object-fit: cover; border: 1.5px solid #10B981;" alt="${this.currentUser.displayName}" />` : '👤'}
            <span style="font-size: 0.84rem; font-weight: 800; color: #fff;">
              Escribiendo como <span style="color: #6EE7B7;">${this.currentUser.displayName || 'Usuario CannaCatalog'}</span>
            </span>
          </div>
          <div class="rating-stars-interactive" id="star-picker" style="display: flex; gap: 4px; font-size: 1.35rem; cursor: pointer;">
            <span data-star="1" onclick="window.communityManager.setRating(1)" title="1 Estrella" style="color: #FFD700; transition: transform 0.15s;">★</span>
            <span data-star="2" onclick="window.communityManager.setRating(2)" title="2 Estrellas" style="color: #FFD700; transition: transform 0.15s;">★</span>
            <span data-star="3" onclick="window.communityManager.setRating(3)" title="3 Estrellas" style="color: #FFD700; transition: transform 0.15s;">★</span>
            <span data-star="4" onclick="window.communityManager.setRating(4)" title="4 Estrellas" style="color: #FFD700; transition: transform 0.15s;">★</span>
            <span data-star="5" onclick="window.communityManager.setRating(5)" title="5 Estrellas" style="color: #FFD700; transition: transform 0.15s;">★</span>
          </div>
        </div>

        <div id="star-rating-label" style="font-size: 0.76rem; font-weight: 700; color: #FCD34D; margin-bottom: 0.6rem;">
          ⭐ 5 de 5 — ¡Excepcional / Imprescindible!
        </div>

        <textarea id="review-comment-input" rows="3" placeholder="Comparte tu experiencia con esta variedad: perfil aromático, efectos psicoactivos, consejos de cultivo, cata o vaporización..." style="width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 0.8rem; color: #fff; font-family: inherit; font-size: 0.88rem; resize: vertical; margin-bottom: 0.8rem; outline: none;"></textarea>

        <div style="display: flex; justify-content: flex-end;">
          <button id="btn-submit-review" onclick="window.communityManager.submitReview('${strainId}')" class="btn btn-emerald-lg" style="padding: 0.6rem 1.4rem; font-size: 0.85rem; font-weight: 800; border-radius: 10px !important;">
            ✍️ Publicar Reseña y Vivencia
          </button>
        </div>
      </div>
    ` : `
      <div class="review-login-prompt" style="background: rgba(0,0,0,0.35); border: 1px dashed rgba(16,185,129,0.4); border-radius: 14px; padding: 1.25rem; text-align: center; margin-bottom: 1.5rem;">
        <div style="font-size: 1.5rem; margin-bottom: 0.3rem;">💬</div>
        <h4 style="color: #fff; font-size: 0.95rem; font-weight: 800; margin-bottom: 0.4rem;">¿Has probado o cultivado esta variedad?</h4>
        <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 0.9rem;">
          Inicia sesión con Google para calificar con estrellas y compartir tu vivencia con la comunidad.
        </p>
        <button class="btn btn-auth-pill" onclick="window.communityManager.loginWithGoogle()" style="padding: 6px 16px; font-size: 0.82rem; border-radius: 50px;">
          <svg width="14" height="14" viewBox="0 0 24 24" style="vertical-align: middle;"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.665-5.17 3.665-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.35 24 12 24z"/><path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.25C.45 8.18 0 9.99 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.35 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/></svg>
          Iniciar sesión con Google para opinar
        </button>
      </div>
    `;

    const reviewsListHtml = reviews.length > 0 ? `
      <div class="reviews-list-wrapper" style="display: flex; flex-direction: column; gap: 0.9rem;">
        ${reviews.map(r => {
          const rStars = '★'.repeat(r.rating || 5) + '☆'.repeat(5 - (r.rating || 5));
          let dateStr = 'Reciente';
          if (r.createdAt) {
            const d = r.createdAt.toDate ? r.createdAt.toDate() : new Date(r.createdAt);
            dateStr = d.toLocaleDateString('es-ES', { day: '2-digit', month: 'short', year: 'numeric' });
          }
          const isOwn = this.currentUser && r.userId === this.currentUser.uid;

          return `
            <div class="review-entry-card" style="background: rgba(255,255,255,0.035); border: 1px solid rgba(255,255,255,0.09); border-radius: 14px; padding: 1.1rem; backdrop-filter: blur(8px);">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.6rem;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  ${r.userPhoto ? `<img src="${r.userPhoto}" alt="${r.userName}" style="width: 28px; height: 28px; border-radius: 50%; object-fit: cover; border: 1px solid rgba(16,185,129,0.5);" onerror="this.style.display='none'" />` : '<span style="font-size: 1.1rem;">👤</span>'}
                  <div>
                    <div style="font-size: 0.85rem; font-weight: 800; color: #fff;">${r.userName || 'Usuario CannaCatalog'}</div>
                    <div style="font-size: 0.72rem; color: var(--text-muted);">${dateStr}</div>
                  </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="color: #FFD700; font-size: 0.95rem; font-weight: 700; text-shadow: 0 1px 4px rgba(0,0,0,0.6);">${rStars}</span>
                  ${isOwn ? `
                    <button onclick="window.communityManager.deleteReview('${r.id}', '${strainId}')" title="Eliminar mi reseña" style="background: transparent; border: none; color: #F87171; cursor: pointer; font-size: 0.8rem; padding: 2px 4px;">
                      🗑️
                    </button>
                  ` : ''}
                </div>
              </div>
              <p style="font-size: 0.86rem; color: rgba(255,255,255,0.92); line-height: 1.5; margin: 0; white-space: pre-line;">${r.comment || ''}</p>
            </div>
          `;
        }).join('')}
      </div>
    ` : `
      <div style="text-align: center; padding: 2.2rem 1rem; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 14px; color: var(--text-muted);">
        <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">🌱</div>
        <h4 style="font-size: 0.92rem; color: #fff; margin-bottom: 0.3rem;">Aún no hay vivencias registradas</h4>
        <p style="font-size: 0.8rem;">¡Sé el primero de la comunidad en dejar tu reseña y vivencia sobre esta genética!</p>
      </div>
    `;

    container.innerHTML = `
      <div class="community-reviews-sheet">
        <!-- HEADER RESUMEN -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 1rem 1.25rem; margin-bottom: 1.3rem;">
          <div>
            <div style="font-size: 0.72rem; text-transform: uppercase; font-weight: 800; letter-spacing: 0.5px; color: var(--primary-emerald); margin-bottom: 2px;">
              VALORACIÓN DE LA COMUNIDAD
            </div>
            <div style="display: flex; align-items: baseline; gap: 6px;">
              <span style="font-size: 1.6rem; font-weight: 900; color: #fff;">${avgScore}</span>
              <span style="font-size: 0.95rem; color: #FFD700;">${starsHtml}</span>
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 1.1rem; font-weight: 800; color: #6EE7B7;">${totalReviews}</div>
            <div style="font-size: 0.74rem; color: var(--text-muted);">Reseña(s) publicada(s)</div>
          </div>
        </div>

        <!-- FORMULARIO O CTA LOGIN -->
        ${formHtml}

        <!-- LISTADO DE RESEÑAS -->
        <div style="margin-top: 1rem;">
          <h4 style="font-size: 0.88rem; font-weight: 800; color: #fff; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 6px;">
            📖 Vivencias Compartidas (${totalReviews})
          </h4>
          ${reviewsListHtml}
        </div>
      </div>
    `;
  }

  setRating(rating) {
    this.selectedRating = rating;
    const picker = document.getElementById('star-picker');
    const label = document.getElementById('star-rating-label');
    
    if (picker) {
      const stars = picker.querySelectorAll('[data-star]');
      stars.forEach((s, idx) => {
        if (idx < rating) {
          s.textContent = '★';
          s.style.color = '#FFD700';
        } else {
          s.textContent = '☆';
          s.style.color = 'rgba(255,255,255,0.3)';
        }
      });
    }

    if (label) {
      const texts = {
        1: '⭐ 1 de 5 — Mala / No recomendada',
        2: '⭐⭐ 2 de 5 — Regular / Mejorable',
        3: '⭐⭐⭐ 3 de 5 — Buena / Correcta',
        4: '⭐⭐⭐⭐ 4 de 5 — Muy buena / Recomendada',
        5: '⭐⭐⭐⭐⭐ 5 de 5 — ¡Excepcional / Imprescindible!'
      };
      label.textContent = texts[rating] || `${rating} Estrellas`;
    }
  }

  async submitReview(strainId) {
    if (!this.currentUser) {
      this.loginWithGoogle();
      return;
    }

    const commentInput = document.getElementById('review-comment-input');
    const comment = commentInput ? commentInput.value.trim() : '';

    if (!comment || comment.length < 3) {
      alert('Por favor escribe unas palabras sobre tu vivencia o experiencia con esta cepa.');
      commentInput?.focus();
      return;
    }

    const btn = document.getElementById('btn-submit-review');
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = '⏳ Publicando...';
    }

    try {
      if (this.db) {
        await this.db.collection('reviews').add({
          strainId: strainId,
          userId: this.currentUser.uid,
          userName: this.currentUser.displayName || 'Usuario CannaCatalog',
          userPhoto: this.currentUser.photoURL || '',
          rating: Number(this.selectedRating) || 5,
          comment: comment,
          createdAt: firebase.firestore.FieldValue ? firebase.firestore.FieldValue.serverTimestamp() : new Date().toISOString()
        });
      }

      if (window.app && typeof window.app.showToast === 'function') {
        window.app.showToast('✨ ¡Tu vivencia y reseña se han publicado con éxito!');
      }

      const contentReviews = document.getElementById('modal-tab-reviews-content');
      if (contentReviews) {
        await this.loadAndRenderReviews(strainId, contentReviews);
      }
    } catch (err) {
      console.error('Error publicando reseña:', err);
      alert(`Error al publicar reseña: ${err.message}`);
      if (btn) {
        btn.disabled = false;
        btn.innerHTML = '✍️ Publicar Reseña y Vivencia';
      }
    }
  }

  async deleteReview(reviewId, strainId) {
    if (!confirm('¿Estás seguro de que deseas eliminar esta vivencia?')) return;

    try {
      if (this.db) {
        await this.db.collection('reviews').doc(reviewId).delete();
      }
      if (window.app && typeof window.app.showToast === 'function') {
        window.app.showToast('🗑️ Reseña eliminada.');
      }
      const contentReviews = document.getElementById('modal-tab-reviews-content');
      if (contentReviews) {
        await this.loadAndRenderReviews(strainId, contentReviews);
      }
    } catch (err) {
      console.error('Error eliminando reseña:', err);
      alert('No se pudo eliminar la reseña.');
    }
  }
}

// Instancia global disponible en toda la aplicación
window.communityManager = new CommunityManager();
