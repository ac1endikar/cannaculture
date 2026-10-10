/**
 * CannaCulture Service Worker (v219)
 * Progressive Web App con soporte offline multinivel, estrategia LRU para imágenes
 * y bypass defensivo para Firebase & Firestore.
 */

const CACHE_CORE = 'cannaculture-core-v219';
const CACHE_IMAGES = 'cannaculture-images-v219';
const CACHE_PAGES = 'cannaculture-pages-v219';
const MAX_CACHED_IMAGES = 120;

const CORE_ASSETS = [
  '/',
  '/index.html',
  '/offline.html',
  '/css/age-gate.css?v=219',
  '/js/age-gate.js?v=219',
  '/css/styles.css?v=219',
  '/js/bundle.js?v=219',
  '/guia-cultivo.html',
  '/css/guia-cultivo.css?v=219',
  '/js/guia-cultivo.js?v=219',
  '/admin-dispensario.html',
  '/css/admin-dispensario.css?v=219',
  '/js/admin-dispensario.js?v=219',
  '/js/strains-data.js?v=219',
  '/manifest.webmanifest',
  '/assets/icons/icon-192x192.png',
  '/assets/icons/icon-512x512.png',
  '/assets/icons/icon-maskable-192x192.png',
  '/assets/icons/icon-maskable-512x512.png',
  '/assets/icons/apple-touch-icon.png',
  '/assets/icons/favicon-32x32.png',
  '/assets/icons/favicon-16x16.png'
];

// Función de poda LRU (Least Recently Used) para limitar almacenamiento de fotos
async function trimCache(cacheName, maxItems) {
  try {
    const cache = await caches.open(cacheName);
    const keys = await cache.keys();
    if (keys.length > maxItems) {
      const itemsToDelete = keys.length - maxItems;
      for (let i = 0; i < itemsToDelete; i++) {
        await cache.delete(keys[i]);
      }
    }
  } catch (err) {
    // Falla silenciosa defensiva
  }
}

// 1. EVENTO INSTALL: Pre-cacheo seguro del Core App Shell
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_CORE)
      .then(cache => {
        return Promise.allSettled(
          CORE_ASSETS.map(url => cache.add(url).catch(err => {
            console.warn('[SW v217] Precache advertencia en:', url, err);
          }))
        );
      })
      .then(() => self.skipWaiting())
  );
});

// 2. EVENTO ACTIVATE: Limpieza automática de cachés antiguas
self.addEventListener('activate', event => {
  const currentCaches = [CACHE_CORE, CACHE_IMAGES, CACHE_PAGES];
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => !currentCaches.includes(k)).map(oldKey => {
          console.log('[SW v217] Purgando caché obsoleta:', oldKey);
          return caches.delete(oldKey);
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. EVENTO FETCH: Interceptación inteligente por capas
self.addEventListener('fetch', event => {
  const request = event.request;

  // Solo interceptar peticiones GET
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // Bypass para llamadas a Firebase, Firestore, Google Auth y analytics
  if (
    url.hostname.includes('firebaseio.com') ||
    url.hostname.includes('googleapis.com') ||
    url.hostname.includes('identitytoolkit') ||
    url.hostname.includes('firestore') ||
    url.protocol === 'chrome-extension:'
  ) {
    return;
  }

  // ESTRATEGIA A: Navegación de páginas HTML (Network First con fallback a offline.html)
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          if (response && response.status === 200) {
            const clone = response.clone();
            caches.open(CACHE_PAGES).then(cache => cache.put(request, clone));
          }
          return response;
        })
        .catch(async () => {
          const cachedPage = await caches.match(request);
          if (cachedPage) return cachedPage;

          // Si es navegación a la raíz o guía, intentar del cache core
          const coreMatch = await caches.match(url.pathname);
          if (coreMatch) return coreMatch;

          // Fallback a pantalla offline
          const offlineFallback = await caches.match('/offline.html');
          return offlineFallback || new Response('Sin conexión', { status: 503, statusText: 'Offline' });
        })
    );
    return;
  }

  // ESTRATEGIA B: Imágenes botánicas de cepas (/img/, /assets/img/, .jpg, .webp, .png)
  const isImage = (
    url.pathname.startsWith('/img/') ||
    url.pathname.startsWith('/assets/img/') ||
    request.destination === 'image'
  );

  if (isImage) {
    event.respondWith(
      caches.match(request).then(cachedResponse => {
        if (cachedResponse) return cachedResponse;

        return fetch(request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_IMAGES).then(cache => {
              cache.put(request, clone);
              trimCache(CACHE_IMAGES, MAX_CACHED_IMAGES);
            });
          }
          return networkResponse;
        }).catch(() => {
          // Si falla imagen offline, retornar fallback o vacío transparente
          return caches.match('/assets/icons/icon-192x192.png');
        });
      })
    );
    return;
  }

  // ESTRATEGIA C: Core Assets (CSS, JS, Fonts, WebManifest) -> Stale-While-Revalidate
  event.respondWith(
    caches.match(request).then(cachedResponse => {
      const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse && networkResponse.status === 200) {
          const clone = networkResponse.clone();
          caches.open(CACHE_CORE).then(cache => cache.put(request, clone));
        }
        return networkResponse;
      }).catch(() => {
        // En caso de error de red, se mantiene el cachedResponse
      });

      return cachedResponse || fetchPromise;
    })
  );
});
