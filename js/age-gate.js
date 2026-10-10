/**
 * CannaCulture - Age Verification Gate Controller (v217)
 * Arquitectura Fail-Secure, Trazabilidad Legal de 30 días y Bloqueo Infranqueable
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'cannaculture_age_consent';
  const CURRENT_POLICY_VERSION = 'v217';
  const TTL_MS = 30 * 24 * 60 * 60 * 1000; // 30 días de persistencia

  /* ==========================================================================
     1. CHEQUEO TEMPRANO FAIL-SECURE (ANTI-FOUC)
     ========================================================================== */
  function isConsentValid() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return false;
      const data = JSON.parse(raw);
      if (!data || data.verified !== true) return false;
      if (data.policyVersion !== CURRENT_POLICY_VERSION) return false;
      if (typeof data.expiresAt !== 'number' || Date.now() >= data.expiresAt) return false;
      return true;
    } catch (_) {
      // Fallback seguro en memoria para navegadores con almacenamiento restringido
      return window._cannaAgeSessionVerified === true;
    }
  }

  // Si no está verificado, bloquear inmediatamente el elemento raíz antes de pintar
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

      // 5. Evaluar estado de visualización
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
          document.documentElement.classList.remove('age-locked');
          document.body.classList.remove('age-locked');
        }, 280);
      } else {
        document.documentElement.classList.remove('age-locked');
        document.body.classList.remove('age-locked');
      }

      this.updateBadges(true);
    }

    grantConsent() {
      const now = Date.now();
      const consentPayload = {
        verified: true,
        timestamp: now,
        policyVersion: CURRENT_POLICY_VERSION,
        expiresAt: now + TTL_MS
      };

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(consentPayload));
        // Limpiar claves legadas obsoletas
        localStorage.removeItem('cannacatalog_age_verified');
        localStorage.removeItem('canna_age_verified');
      } catch (_) {
        window._cannaAgeSessionVerified = true;
      }

      this.unlockContent();

      // Notificación discreta de confirmación
      if (window.catalogApp && typeof window.catalogApp.showToast === 'function') {
        window.catalogApp.showToast('🛡️ Mayoría de edad (+18) verificada correctamente.');
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
          badge.setAttribute('title', 'Acceso verificado para mayores de 18 años. Clic para consultar o revocar consentimiento.');
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
        if (window.confirm('🛡️ Consentimiento de Mayoría de Edad (+18) activo.\n\n¿Deseas revocar tu consentimiento y bloquear el acceso en este dispositivo?')) {
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
      try {
        localStorage.removeItem(STORAGE_KEY);
        localStorage.removeItem('cannacatalog_age_verified');
        localStorage.removeItem('canna_age_verified');
      } catch (_) {}
      window._cannaAgeSessionVerified = false;

      this.closeRevokeDialog();
      // Recargar la página para activar la directiva fail-secure desde el encabezado
      window.location.reload();
    }
  }

  // Instanciación global
  window.CannaAgeGate = new CannaAgeGateManager();
})();
