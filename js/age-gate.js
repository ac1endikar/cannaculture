/**
 * CannaCulture - Age Verification Gate Controller (v218 - Memoria Volátil Estricta)
 * Arquitectura Fail-Secure: Verificación gestionada ÚNICAMENTE en memoria volátil JS.
 * CERO almacenamiento en sessionStorage y localStorage.
 * Al recargar la página (F5), refrescar o abrir nueva pestaña, la memoria se vacía
 * y el modal +18 salta OBLIGATORIAMENTE sin excepción.
 */

(function () {
  'use strict';

  /* ==========================================================================
     1. CHEQUEO TEMPRANO FAIL-SECURE (MEMORIA VOLÁTIL)
     ========================================================================== */
  function isConsentValid() {
    try {
      // Purgar obligatoriamente cualquier persistencia residual en almacenamiento
      localStorage.removeItem('cannaculture_age_consent');
      localStorage.removeItem('cannacatalog_age_verified');
      localStorage.removeItem('canna_age_verified');
      sessionStorage.removeItem('cannaculture_age_session');
    } catch (_) {}

    // La verificación reside EXCLUSIVAMENTE en la memoria volátil de la sesión JS actual
    return window._cannacultureAgeVerified === true;
  }

  // Si no está verificado en la memoria de la página actual, bloquear inmediatamente el elemento raíz antes de pintar
  if (!isConsentValid()) {
    document.documentElement.classList.add('age-locked');
    if (document.body) {
      document.body.classList.add('age-locked');
    } else {
      document.addEventListener('DOMContentLoaded', function () {
        document.body.classList.add('age-locked');
      });
    }
  }

  /* ==========================================================================
     2. GESTOR DE EVENTOS Y DIÁLOGO MODAL
     ========================================================================== */
  class CannaAgeGateManager {
    constructor() {
      this.modal = null;
      this.revokeDialog = null;
      this.btnPermit = null;
      this.btnDeny = null;
      this.statusBadges = [];
      this.init();
    }

    init() {
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => this.bindUI());
      } else {
        this.bindUI();
      }
    }

    bindUI() {
      this.modal = document.getElementById('age-gate-modal');
      this.revokeDialog = document.getElementById('age-revoke-dialog');
      this.btnPermit = document.getElementById('btn-age-permit');
      this.btnDeny = document.getElementById('btn-age-deny');
      this.statusBadges = Array.from(document.querySelectorAll('.age-status-badge, #age-status-badge, #btn-age-status'));

      // 1. Bloqueo estricto del evento 'cancel' en el diálogo (inmoviliza la tecla Escape)
      if (this.modal) {
        this.modal.addEventListener('cancel', (e) => {
          e.preventDefault();
        });
      }

      if (this.revokeDialog) {
        this.revokeDialog.addEventListener('cancel', (e) => {
          e.preventDefault();
          this.closeRevokeDialog();
        });
      }

      // 2. Acciones del modal de verificación
      if (this.btnPermit) {
        this.btnPermit.addEventListener('click', (e) => {
          e.preventDefault();
          this.grantConsent();
        });
      }

      if (this.btnDeny) {
        this.btnDeny.addEventListener('click', (e) => {
          e.preventDefault();
          this.denyConsent();
        });
      }

      // 3. Acciones de los badges de cabecera
      this.statusBadges.forEach((badge) => {
        badge.addEventListener('click', (e) => {
          e.preventDefault();
          this.promptRevokeConsent();
        });
      });

      // 4. Botones del diálogo de revocación
      const btnCancelRevoke = document.getElementById('btn-revoke-cancel');
      const btnConfirmRevoke = document.getElementById('btn-revoke-confirm');

      if (btnCancelRevoke) {
        btnCancelRevoke.addEventListener('click', (e) => {
          e.preventDefault();
          this.closeRevokeDialog();
        });
      }

      if (btnConfirmRevoke) {
        btnConfirmRevoke.addEventListener('click', (e) => {
          e.preventDefault();
          this.confirmRevocation();
        });
      }

      // 5. Evaluar estado de visualización en la sesión
      if (!isConsentValid()) {
        this.lockAndShowModal();
      } else {
        this.unlockContent();
      }
    }

    lockAndShowModal() {
      document.documentElement.classList.add('age-locked');
      document.body.classList.add('age-locked');

      if (this.modal) {
        try {
          if (typeof this.modal.showModal === 'function') {
            if (!this.modal.open) this.modal.showModal();
          } else {
            this.modal.setAttribute('open', '');
          }
        } catch (_) {
          this.modal.setAttribute('open', '');
        }
      }

      this.updateBadges(false);
    }

    unlockContent() {
      // 1. Eliminar cualquier barrera residual de visualización
      const lockStyle = document.getElementById('age-lock-style');
      if (lockStyle) lockStyle.remove();
      const mainApp = document.getElementById('main-app');
      if (mainApp) mainApp.style.display = '';
      const mainHeader = document.querySelector('.main-header');
      if (mainHeader) mainHeader.style.display = '';

      const finalizeUnlock = () => {
        document.documentElement.classList.remove('age-locked');
        document.body.classList.remove('age-locked');
        this.updateBadges(true);

        // Despachar evento global de verificación para reactivar el renderizado del catálogo
        document.dispatchEvent(new CustomEvent('cannaAgeVerified', { detail: { verified: true } }));
        if (window.app && typeof window.app.applyFiltersAndSort === 'function') {
          window.app.applyFiltersAndSort();
        }
      };

      if (this.modal) {
        this.modal.classList.add('closing');
        setTimeout(() => {
          try {
            if (typeof this.modal.close === 'function') {
              if (this.modal.open) this.modal.close();
            }
          } catch (_) {}
          this.modal.removeAttribute('open');
          this.modal.classList.remove('closing');
          finalizeUnlock();
        }, 280);
      } else {
        finalizeUnlock();
      }
    }

    grantConsent() {
      // Registrar consentimiento exclusivamente en memoria volátil JS
      window._cannacultureAgeVerified = true;

      try {
        localStorage.removeItem('cannaculture_age_consent');
        localStorage.removeItem('cannacatalog_age_verified');
        localStorage.removeItem('canna_age_verified');
        sessionStorage.removeItem('cannaculture_age_session');
      } catch (_) {}

      this.unlockContent();

      // Notificación discreta de confirmación
      if (window.catalogApp && typeof window.catalogApp.showToast === 'function') {
        window.catalogApp.showToast('🛡️ Mayoría de edad (+18) verificada.');
      }
    }

    denyConsent() {
      // Redirección segura inmediata sin dejar rastro en el historial de navegación
      window.location.replace('https://www.google.com');
    }

    updateBadges(verified) {
      this.statusBadges.forEach((badge) => {
        if (verified) {
          badge.style.display = 'inline-flex';
          badge.setAttribute('title', 'Acceso verificado para mayores de 18 años. Clic para revocar consentimiento.');
          badge.setAttribute('aria-label', 'Mayoría de edad +18 verificada');
        } else {
          badge.setAttribute('title', 'Acceso restringido +18 sin verificar');
          badge.setAttribute('aria-label', 'Sin verificar mayoría de edad');
        }
      });
    }

    promptRevokeConsent() {
      if (this.revokeDialog) {
        try {
          if (typeof this.revokeDialog.showModal === 'function') {
            if (!this.revokeDialog.open) this.revokeDialog.showModal();
          } else {
            this.revokeDialog.setAttribute('open', '');
          }
        } catch (_) {
          this.revokeDialog.setAttribute('open', '');
        }
      } else {
        // Fallback en caso de que el elemento revokeDialog no esté en el DOM
        if (window.confirm('🛡️ Consentimiento de Mayoría de Edad (+18) activo.\n\n¿Deseas revocar tu consentimiento y bloquear el acceso inmediatamente?')) {
          this.confirmRevocation();
        }
      }
    }

    closeRevokeDialog() {
      if (this.revokeDialog) {
        try {
          if (typeof this.revokeDialog.close === 'function') {
            if (this.revokeDialog.open) this.revokeDialog.close();
          }
        } catch (_) {}
        this.revokeDialog.removeAttribute('open');
      }
    }

    confirmRevocation() {
      window._cannacultureAgeVerified = false;
      try {
        localStorage.removeItem('cannaculture_age_consent');
        localStorage.removeItem('cannacatalog_age_verified');
        localStorage.removeItem('canna_age_verified');
        sessionStorage.removeItem('cannaculture_age_session');
      } catch (_) {}

      this.closeRevokeDialog();
      // Recargar la página para activar la directiva fail-secure desde el encabezado
      window.location.reload();
    }
  }

  // Instanciación global
  window.CannaAgeGate = new CannaAgeGateManager();
})();
