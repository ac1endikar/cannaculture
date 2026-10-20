/**
 * CannaCulture PWA Manager (v213)
 * Registro seguro de Service Worker, captura de beforeinstallprompt,
 * detección de modo standalone e interfaz reactiva para instalación.
 */

(function () {
  'use strict';

  let deferredPrompt = null;

  function isStandalone() {
    return (
      window.matchMedia('(display-mode: standalone)').matches ||
      window.navigator.standalone === true ||
      document.referrer.includes('android-app://')
    );
  }

  function initServiceWorker() {
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', function () {
        navigator.serviceWorker.register('/sw.js?v=213')
          .then(function (reg) {
            console.log('🌿 CannaCulture PWA Service Worker registrado con éxito (v213):', reg.scope);
            reg.addEventListener('updatefound', function () {
              const newWorker = reg.installing;
              if (newWorker) {
                newWorker.addEventListener('statechange', function () {
                  if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                    console.log('🔄 Nueva versión de CannaCulture disponible.');
                  }
                });
              }
            });
          })
          .catch(function (err) {
            console.warn('CannaCulture SW no registrado (entorno local o sin HTTPS):', err);
          });
      });
    }
  }

  function initInstallUI() {
    const btnInstall = document.getElementById('btn-pwa-install');
    if (!btnInstall) return;

    // Si ya se está ejecutando como app nativa standalone, ocultar botón permanentemente
    if (isStandalone()) {
      btnInstall.style.display = 'none';
      return;
    }

    // Capturar el evento de instalación en Android / Chromium
    window.addEventListener('beforeinstallprompt', function (e) {
      e.preventDefault();
      deferredPrompt = e;
      btnInstall.style.display = 'inline-flex';
      btnInstall.classList.add('pwa-pulse-glow');
    });

    // Soporte para iOS Safari
    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
    if (isIOS && !isStandalone()) {
      // En iOS Safari no existe beforeinstallprompt, mostrar botón con guía asistida
      btnInstall.style.display = 'inline-flex';
    }

    btnInstall.addEventListener('click', async function () {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        const choice = await deferredPrompt.userChoice;
        if (choice.outcome === 'accepted') {
          console.log('✅ Usuario aceptó instalar CannaCulture');
          btnInstall.style.display = 'none';
        }
        deferredPrompt = null;
      } else if (isIOS) {
        showIOSInstallDialog();
      }
    });

    window.addEventListener('appinstalled', function () {
      console.log('🎉 CannaCulture instalada exitosamente como PWA');
      btnInstall.style.display = 'none';
      deferredPrompt = null;
    });
  }

  function showIOSInstallDialog() {
    const existing = document.getElementById('pwa-ios-modal');
    if (existing) {
      existing.style.display = 'flex';
      return;
    }

    const modal = document.createElement('div');
    modal.id = 'pwa-ios-modal';
    modal.style.cssText = `
      position: fixed; inset: 0; z-index: 99999;
      background: rgba(0,0,0,0.85); backdrop-filter: blur(8px);
      display: flex; align-items: center; justify-content: center; padding: 1.5rem;
    `;
    modal.innerHTML = `
      <div style="
        background: #0F1715; border: 1px solid rgba(16,185,129,0.3); border-radius: 20px;
        max-width: 380px; width: 100%; padding: 2rem 1.5rem; text-align: center; color: #F1F5F9;
        box-shadow: 0 20px 40px rgba(0,0,0,0.8), 0 0 25px rgba(16,185,129,0.2);
      ">
        <div style="font-size: 2.8rem; margin-bottom: 0.75rem;">🌿</div>
        <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem; color: #FFFFFF;">Instalar en iPhone / iPad</h3>
        <p style="font-size: 0.9rem; color: #94A3B8; line-height: 1.5; margin-bottom: 1.5rem;">
          Para añadir CannaCulture a tu pantalla de inicio en Safari:
        </p>
        <div style="text-align: left; background: rgba(255,255,255,0.03); border-radius: 12px; padding: 1rem; margin-bottom: 1.5rem; font-size: 0.88rem; line-height: 1.6;">
          <p>1. Pulsa el botón <strong>Compartir</strong> <span style="font-size: 1.1rem;">⎋</span> en la barra inferior.</p>
          <p>2. Desplaza hacia abajo y selecciona <strong>Añadir a la pantalla de inicio</strong> <span>⊞</span>.</p>
          <p>3. Pulsa <strong>Añadir</strong> en la esquina superior derecha.</p>
        </div>
        <button id="btn-close-ios-pwa" style="
          width: 100%; background: linear-gradient(135deg, #10B981, #059669); color: white;
          border: none; padding: 0.8rem; border-radius: 10px; font-weight: 600; cursor: pointer;
        ">Entendido</button>
      </div>
    `;

    document.body.appendChild(modal);
    document.getElementById('btn-close-ios-pwa').addEventListener('click', function () {
      modal.style.display = 'none';
    });
  }

  // Inicializar PWA Manager
  initServiceWorker();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initInstallUI);
  } else {
    initInstallUI();
  }
})();
