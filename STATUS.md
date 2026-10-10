# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-10-10 14:30  
> **Servidor local:** Activo en `http://localhost:8080`  
> **Commit de cierre:** `feat(security): blindaje integral age verification gate +18 fail-secure y micro-badge v217`  
> **Version Cache-Busting:** `?v=217`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **877 cepas botanicas 100% unicas y originales, 0 duplicados visuales.**
- **75 Bancos Oficiales Incorporados (ampliación de 65 a 75 bancos de élite mundial).**
- **100 Nuevas Variedades Fotoperiódicas/Feminizadas/Regulares (estrictamente 0 autoflorecientes).**
- **Sistema Integral Age Verification Gate (+18) Blindado (v217):**
  - **Arquitectura Fail-Secure (Cero Fugas):** Inyección de bloqueo inmediato en `<head>` de `index.html`, `guia-cultivo.html` y `admin-dispensario.html` para erradicar el FOUC.
  - **Protección `<noscript>` Activa:** Bloqueo absoluto y pantalla de aviso legal si JavaScript se encuentra deshabilitado.
  - **Modal Glassmorphism Dark Emerald (`#0B0F0E`):** Diálogo nativo `<dialog id="age-gate-modal">` con captura y anulación del evento `cancel` (bloqueo total de tecla `Escape`) y bloqueo de scroll e interacciones (`overflow: hidden !important; touch-action: none;`).
  - **Descargo Jurídico Botánico Explícito:** Mayoría de edad (+18), finalidad estrictamente botánica, enciclopédica y de reducción de riesgos, y ámbito de consumo privado y Clubes Sociales de Cannabis (CSC).
  - **Trazabilidad Legal de 30 Días:** Token estructurado en `localStorage` (`cannaculture_age_consent`) con timestamp, política de versión `v217` y caducidad automática `expiresAt`.
  - **Redirección Segura Irreversible:** Salida para menores mediante `window.location.replace('https://www.google.com')` sin dejar rastro en el historial del navegador.
  - **Limpieza de Bypasses:** Eliminado definitivamente `autoUnlockCannaCatalog()` y overrides manuales en `js/app.js`.
  - **Micro-Badge Discreto en Cabecera (`🛡️ 18+`):** Sustitución de la píldora aparatosa por un indicador sutil e idéntico en las 3 páginas, con diálogo de revocación voluntaria y re-bloqueo del terminal.
- **CannaDispensario POS 2.0 (v216):** Terminal táctil de barra para Clubes Sociales de Cannabis (CSC) plenamente operativo en `admin-dispensario.html` con 3 pestañas, pesaje digital, cuotas de socio y arqueo diario.
- **Sommelier IA María 2.0 (v215):** Motor de puntuación multidimensional (`SommelierScoringEngine`) evaluando el catálogo íntegro de 877 cepas y 75 bancos en tiempo real con tríada de recomendaciones y mini-fichas interactivas.
- **Cobertura Linaje/Genetica:** 877/877 cepas (100%).
- **Fotografias Botanicas HD:** 100% macro flores reales descargadas localmente en `img/` como `.webp` y `.jpg`, resolución mínima >= 400x400 (hasta 2500px), 0 colisiones visuales, 0 fondos blancos, 0 ilustraciones.
- **Optimización de Rendimiento & Core Web Vitals (v214):** Filtrado y renderizado instantáneo (<8ms) con renderizado por lotes de 24 tarjetas mediante IntersectionObserver, pre-indexación en memoria `_searchIndex`, debounce adaptativo de 110ms sincronizado con `requestAnimationFrame`, priorización LCP (`fetchpriority="high"`, `loading="eager"`), CLS = 0.000 y skeleton shimmer placeholder.
- **Infraestructura SEO & Redes Sociales (v212):** Desplegada con `robots.txt`, `sitemap.xml` multilingüe, metadatos Open Graph, Twitter Cards, Schemas JSON-LD y banner oficial 1200x630px.
- **Infraestructura PWA & Soporte Offline (v213/v217):** Aplicación instalable con `manifest.webmanifest`, `sw.js` (3 capas de caché + LRU de imágenes), `offline.html`, iconos de alta resolución estándar y maskables, botón de instalación en cabecera y soporte iOS/Safari.

### v217 — Blindaje Integral Age Verification Gate (+18), Arquitectura Fail-Secure, Trazabilidad Legal de 30 Días y Micro-Badge Universal (`cannacultureapp.com`)
- **Arquitectura Universal y Desacoplada (`css/age-gate.css` & `js/age-gate.js`):**
  - Módulo independiente sin dependencias externas, integrado homogéneamente en los 3 puntos de acceso: `index.html`, `guia-cultivo.html` y `admin-dispensario.html`.
  - Detección ultra-temprana en `<head>` que previene el FOUC (Flash of Unverified Content) inyectando la regla `html.age-locked` antes del pintado del DOM.
  - Bloqueo visual profundo del fondo con desenfoque extremo (`backdrop-filter: blur(28px) saturate(180%)`) y bloqueo de eventos táctiles/puntero.
- **Directiva `<noscript>` Fail-Secure:**
  - Bloqueo absoluto de la aplicación si JavaScript está desactivado, mostrando una pantalla con el descargo legal obligatorio y prohibición de acceso.
- **Inmovilización del Modal `<dialog id="age-gate-modal">`:**
  - Bloqueo estricto del evento `cancel` (invalida la tecla `Escape`).
  - Bloqueo de scroll global en `<html>` y `<body>` (`overflow: hidden !important; touch-action: none;`).
- **Trazabilidad y Validez Jurídica de Consentimiento:**
  - Estructuración JSON en `localStorage` bajo `cannaculture_age_consent` con caducidad exacta a 30 días (`expiresAt: now + 30 días`) y validación de versión normativa (`policyVersion: 'v217'`).
  - Redirección segura para menores con `window.location.replace('https://www.google.com')` impidiendo el retorno mediante el botón atrás del historial.
- **Micro-Badge de Cabecera & Revocación Voluntaria:**
  - Sustitución de la píldora aparatosa por un micro-badge elegante `🛡️ 18+` (`.age-status-badge`) con tooltip accesible e integrado de forma uniforme en la cabecera de las 3 páginas.
  - Diálogo modal de revocación voluntaria (`#age-revoke-dialog`): Permite al usuario revocar su consentimiento legal en cualquier momento, purgando el token y re-bloqueando inmediatamente el terminal.
- **Service Worker & Cache-Busting (`v217`):**
  - Cachés actualizadas a `cannaculture-core-v217`, `cannaculture-images-v217` y `cannaculture-pages-v217`.
  - Precacheo de `css/age-gate.css?v=217` y `js/age-gate.js?v=217` en `CORE_ASSETS`.
  - Cache-busting sincronizado a `?v=217` en `index.html`, `guia-cultivo.html` y `admin-dispensario.html`.
  - Recompilados `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js`.
- **Arquitectura de 3 Pestañas Principales en Dispensario (`admin-dispensario.html`):**
  - `🌿 Carta & Menú en Barra`: Vista de administración de variedades activas, stock en bote, notas de cata y cuotas por nivel de socio (`tierStd`, `tierColab`, `tierTerap`).
  - `⚖️ Terminal Mostrador (POS)`: Mostrador táctil de barra para dispensación en directo frente al socio.
  - `📊 Arqueo & Movimientos`: Panel de control contable, estadísticas del día, alertas de botes casi vacíos y libro cronológico de dispensación.
- **Sincronización con 877 Cepas y 75 Bancos Criadores:**
  - Pre-indexación en memoria `_searchIndex` O(1) con normalización de diacríticos para búsqueda en tiempo real (<2ms).
  - Selector desplegable con los 75 bancos oficiales de élite para explorar el catálogo y añadir variedades con 1 clic heredando foto macro, THC, terpenos y linaje.
  - Fórmulas proporcionales para el cálculo sugerido de cuotas de socio (-10% Colaborador, -25% Terapéutico).
- **Terminal Mostrador (POS CSC):**
  - **Identificación de Socio:** Base de socios estatutarios en `localStorage` (`cannaculture_csc_members`) con visualización de avatar, número de socio, alias, nivel estatutario y barra de progreso de consumo mensual vs límite estatutario. Modal interactivo para alta rápida de nuevos socios.
  - **Báscula Digital Integrada:** Botonera rápida táctil (+0.5g, +1g, +2g, +5g, +10g, Borrar) y campo decimal exacto para sincronización con báscula física de precisión.
  - **Cálculo en Tiempo Real:** Aplicación automática de la cuota según el nivel del socio y cálculo instantáneo del total en euros (`g × €/g = Total €`).
  - **Validaciones de Seguridad:** Bloqueo automático ante excesos del límite mensual estatutario restante del socio o ante falta de stock disponible en el bote.
  - **Descuento y Registro:** Descuento instantáneo de gramos del bote, actualización del consumo del socio y guardado del ticket en el libro de movimientos.
- **Arqueo de Caja & Exportación de Datos:**
  - Cuadros de mando: Total gramos dispensados hoy, total aportaciones recibidas en caja (€), recuento de tickets y alerta de stock bajo (< 10g).
  - Libro cronológico de dispensaciones con filtrado diario y tabla detallada.
  - **Exportación CSV:** Descarga directa de archivo `.csv` formateado con UTF-8 BOM para apertura perfecta en Excel.
  - **Acta Imprimible:** Optimización para `@media print` para imprimir actas oficiales de cierre de dispensario para asambleas y libros de actas del club.
- **Service Worker & Cache-Busting (`v216`):**
  - Cachés de Service Worker actualizadas a `cannaculture-core-v216`, `cannaculture-images-v216` y `cannaculture-pages-v216`.
  - Cache-busting sincronizado a `?v=216` en `index.html`, `guia-cultivo.html` y `admin-dispensario.html`.
  - Recompilados `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js`.
- **Cobertura Linaje/Genetica:** 877/877 cepas (100%).
- **Fotografias Botanicas HD:** 100% macro flores reales descargadas localmente en `img/` como `.webp` y `.jpg`, resolución mínima >= 400x400 (hasta 2500px), 0 colisiones visuales, 0 fondos blancos, 0 ilustraciones.
- **Optimización de Rendimiento & Core Web Vitals (v214):** Filtrado y renderizado instantáneo (<8ms) con renderizado por lotes de 24 tarjetas mediante IntersectionObserver, pre-indexación en memoria `_searchIndex`, debounce adaptativo de 110ms sincronizado con `requestAnimationFrame`, priorización LCP (`fetchpriority="high"`, `loading="eager"`), CLS = 0.000 y skeleton shimmer placeholder.
- **Módulo CSC Mostrador & Kiosco:** Operativo con Ficha Técnica interactiva, Lightbox macro HD, catálogo de 877 cepas y selector multi-idioma reactivo (ES/EN/DE/IT).
- **Guía de Cultivo (`guia-cultivo.html`):** Página independiente operativa con 5 etapas interactivas y selector ES/EN/DE/IT.
- **Infraestructura SEO & Redes Sociales (v212):** Desplegada con `robots.txt`, `sitemap.xml` multilingüe, metadatos Open Graph, Twitter Cards, Schemas JSON-LD y banner oficial 1200x630px.
- **Infraestructura PWA & Soporte Offline (v213):** Aplicación instalable con `manifest.webmanifest`, `sw.js` (3 capas de caché + LRU de imágenes), `offline.html`, iconos de alta resolución estándar y maskables, botón de instalación en cabecera y soporte iOS/Safari.

### v215 — Motor Sommelier IA María 2.0, Scoring Multidimensional & Tríada de Recomendaciones Botánicas (`cannacultureapp.com`)
- **Motor de Recomendación Multidimensional (`SommelierScoringEngine`):**
  - Matriz de puntuación botánica algorítmica de 6 dimensiones que evalúa las 877 cepas del catálogo en tiempo real con latencia <5ms.
  - Ponderación de pesos: Efecto/Ánimo (+30 pts), Momento del día/Actividad (+25 pts), Perfil terpénico diana (+20 pts), Potencia y tolerancia al THC (+15 pts), Notas aromáticas y de sabor (+10 pts) y Factor de diversidad anti-repetición (-15 pts a cepas recomendadas recientemente).
- **Tríada de Recomendaciones Estructuradas (`generateRecommendationCardsHTML`):**
  - Sustitución de listas planas de texto por tríadas botánicas jerarquizadas:
    1. `🥇 Top Match`: Máxima afinidad matemática con la necesidad, atmósfera y perfil solicitado.
    2. `🧬 Alternativa Terpénica`: Cepa con el mismo terpeno dominante pero genética o banco diferente para enriquecer la cata.
    3. `⚖️ Opción Equilibrada`: Variedad con ratio balanceado, THC moderado o linaje clásico contrastado.
- **Mini-Fichas Botánicas Interactivas en el Chat:**
  - Tarjetas visuales glassmorphic (`.ai-rec-card`) con fotografía macro floral real, micro-badge del banco oficial, indicador de especie, píldora de THC, terpeno dominante con su color característico y perfil organoléptico.
  - Botones de acción directos:
    - `📋 Ficha`: Despacho del evento global `openStrainDetail` para abrir el modal técnico completo de la variedad.
    - `🔍 En Catálogo`: Conmutación reactiva a la sección `#section-catalog`, reseteo de filtros, inyección del término de búsqueda y scroll suave a la tarjeta.
    - `🌿 Terpeno`: Filtrado instantáneo del catálogo por la familia terpénica seleccionada.
- **Chips de Sugerencia Contextuales Actualizados:**
  - Renovación de los botones de acción rápida en `index.html` (tanto en la sección in-page como en la ventana flotante) cubriendo: desconexión post-trabajo, concentración y arte, notas cítricas, tertulia social, relax muscular para cine, baja tolerancia / CBD, diagnóstico botánico de tricomas (CannaDoctor) y efecto séquito.
  - Badges informativos actualizados a `877 cepas · 75 bancos` en toda la interfaz.
- **Estilos CSS y Experiencia Visual Premium (`css/styles.css`):**
  - Contenedor `.ai-rec-cards-container`, tarjetas `.ai-rec-card` con borde glow esmeralda interactivo, micro-badges y botones con estados hover/active pulidos y optimizaciones móviles.
- **Service Worker & Cache-Busting (`v215`):**
  - Cachés de Service Worker actualizadas a `cannaculture-core-v215`, `cannaculture-images-v215` y `cannaculture-pages-v215`.
  - Cache-busting sincronizado a `?v=215` en `index.html`, `guia-cultivo.html` y `admin-dispensario.html`.
  - Recompilados `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js`.

### v214 — Optimización Extrema de Rendimiento, Chunk Batching y Core Web Vitals (`cannacultureapp.com`)
- **Renderizado Progresivo por Lotes (24 tarjetas iniciales + Infinite Chunking):**
  - Fin del cuello de botella de renderizado síncrono masivo de 877 tarjetas (>21,900 nodos DOM) a la vez.
  - El renderizado inicial inyecta únicamente el primer lote de 24 tarjetas con tiempo de bloqueo del hilo principal inferior a 8 ms (reducción de TBT de ~450ms a <8ms).
  - Centinela reactivo `#catalog-scroll-sentinel` vigilado mediante `IntersectionObserver` con margen predictivo (`rootMargin: '450px 0px'`).
  - Inyección progresiva de lotes sucesivos de 24 tarjetas utilizando `DocumentFragment` (`createRange().createContextualFragment()`) sin provocar re-flows forzados ni repintados del catálogo completo.
- **Pre-indexación en Memoria O(1) (`_searchIndex`):**
  - Generación única en arranque de una cadena consolidada pre-minimizada en minúsculas por variedad (`strain._searchIndex`), compilando nombre, genética, banco, aka y terpenos/sabores.
  - Reducción del coste de búsqueda en tiempo real de más de 4,385 llamadas a `.toLowerCase()` por pulsación a una sola comprobación de subcadena (`_searchIndex.includes(query)`).
- **Micro-Debounce Adaptativo con `requestAnimationFrame`:**
  - Temporizador reactivo de 110 ms con sincronización al ciclo de refresco vertical de pantalla (`requestAnimationFrame`), eliminando el jank y garantizando un INP (*Interaction to Next Paint*) óptimo (< 50 ms).
- **Priorización de Carga de Imágenes Botánicas & Cero CLS:**
  - **LCP Booster:** Las primeras 8 tarjetas en el viewport reciben `fetchpriority="high"` y `loading="eager"`, evitando que el navegador demore las fotos del viewport superior.
  - **Offscreen Lazy:** Las tarjetas subsiguientes utilizan `loading="lazy"` y `fetchpriority="low"`, reduciendo drásticamente la contención de ancho de banda y memoria RAM.
  - **Cero CLS (0.000):** Dimensiones intrínsecas explícitas (`width="300" height="185"`) en etiquetas `<img>` y reserva de caja en CSS mediante `aspect-ratio: 16 / 10`.
  - **Placeholder Skeleton Shimmer:** Estilos CSS (`@keyframes cardSkeletonShimmer`) con degradado esmeralda animado y transición fluida `.is-loaded` de opacidad.
- **Sincronización PWA & Cache-Busting (`v214`):**
  - Cachés de Service Worker actualizadas a `cannaculture-core-v214`, `cannaculture-images-v214` y `cannaculture-pages-v214`.
  - Cache-busting actualizado a `?v=214` en todos los HTMLs y recompilados `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js`.


### v213 — Arquitectura PWA Instalable, Service Worker Offline Multinivel & Experiencia Nativa (`cannacultureapp.com`)
- **Web App Manifest (`manifest.webmanifest` & `manifest.json`):**
  - Declaración completa para instalación nativa (*standalone*) en Android, iOS, Windows y macOS.
  - Paleta temática `#0B0F0E` (theme-color y background_color), orientación libre y scope canónico `/`.
  - 3 atajos directos nativos (*shortcuts*): *Catálogo de Cepas*, *Guía de Cultivo* y *Sommelier IA María*.
- **Iconografía Oficial PWA (`assets/icons/` e `img/icons/`):**
  - Generador automatizado [`scripts/generate_pwa_icons.py`](file:///d:/cannaculture/scripts/generate_pwa_icons.py) con Pillow.
  - Iconos estándar de 192×192 y 512×512 px.
  - Iconos Android adaptables *maskable* (192×192 y 512×512 px) respetando la zona de seguridad central del 80%.
  - Icono optimizado para iOS Safari (`apple-touch-icon.png` 180×180 px) y favicons de escritorio (32×32 y 16×16 px).
- **Service Worker Multinivel (`sw.js`):**
  - **Core App Shell:** Pre-cacheo seguro de HTMLs, CSS, JS bundles, fuentes e iconos con estrategia *Stale-While-Revalidate*.
  - **Imágenes Botánicas:** Estrategia *Cache First* con poda automática LRU (*Least Recently Used*) limitada a 120 imágenes para proteger el almacenamiento del dispositivo.
  - **Navegación:** Estrategia *Network First* con almacenamiento dinámico de páginas consultadas y fallback automático a [`offline.html`](file:///d:/cannaculture/offline.html).
  - **Bypass Defensivo:** Peticiones externas de Firebase, Firestore, Google Auth y APIs no-GET excluidas de interceptación para total integridad de base de datos.
- **Experiencia de Usuario e Instalación (UX/UI):**
  - Módulo independiente [`js/pwa-manager.js`](file:///d:/cannaculture/js/pwa-manager.js) para control de registro, captura del evento `beforeinstallprompt` y detección de modo *standalone*.
  - Botón discreto `#btn-pwa-install` en la cabecera con estilo píldora esmeralda y micro-animación pulsante (`.btn-pwa-install-pill`).
  - Modal asistido instructivo para usuarios de iOS Safari explicando los pasos de "Añadir a la pantalla de inicio".
  - Pantalla autónoma y elegante de fallback offline [`offline.html`](file:///d:/cannaculture/offline.html).
- **Recompilación de Bundle & Cache-Busting (`?v=213`):**
  - Sincronizados `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js` mediante `python scripts/build_bundle.py`.
  - Cache-busting actualizado a `?v=213` en `index.html`, `guia-cultivo.html` y `admin-dispensario.html`.


### v212 — Infraestructura Completa de SEO Técnico, Social Meta (Open Graph & Twitter) y Sitemap Canónico (`cannacultureapp.com`)
- **Metadatos Técnicos SEO & Canónicos (`index.html`, `guia-cultivo.html`, `admin-dispensario.html`):**
  - **`index.html`:** Título y descripción optimizados reflejando las 877 cepas y 75 bancos de semillas mundiales, `<link rel="canonical" href="https://cannacultureapp.com/">`, directivas robots `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1`, Open Graph y Twitter Cards completos con imagen 1200x630, y Schema JSON-LD estructurado (`WebSite` y `Organization`).
  - **`guia-cultivo.html`:** Canonical `https://cannacultureapp.com/guia-cultivo.html`, meta description de las 5 etapas de cultivo, Open Graph de tipo `article`, Twitter Card `summary_large_image`, y Schema JSON-LD (`HowTo`) estructurado con los 5 pasos para Rich Snippets en Google.
  - **`admin-dispensario.html`:** Configurado como panel privado con directiva de seguridad y SEO `<meta name="robots" content="noindex, nofollow">`, canonical a su URL y metadata Open Graph/Twitter para visualización estética al compartirse de forma privada.
- **Banner Oficial Open Graph de 1200x630px (`assets/img/og-cannaculture-1200x630.jpg` e `img/og-cannaculture-1200x630.jpg`):**
  - Creado script determinista `scripts/generate_og_banner.py` usando Pillow.
  - Diseño dark botánico ultra-premium (`#0B0F0E`) con resplandores esmeralda (`#10B981`), composición de fotografía macro HD (KMintz / Blue Dream), píldora `2.0 ULTRA`, 4 tarjetas de estadísticas con iconos vectoriales nítidos (`877 Variedades`, `75 Bancos Élite`, `8 Terpenos Clave`, `Sommelier IA María`) y footer de marca.
  - Exportado en JPEG optimizado de 147.6 KB con ratio 1.91:1 exacto (1200×630 px).
- **Archivos de Indexación en la Raíz:**
  - **`robots.txt`:** Directivas RFC 9309 permitiendo páginas y recursos públicos (`/`, `/css/`, `/js/`, `/img/`, `/assets/`, `/guia-cultivo.html`), bloqueando el panel interno `/admin-dispensario.html` y carpetas de desarrollo (`/scripts/`, `/scratch/`, `/docs/`), y declarando `Sitemap: https://cannacultureapp.com/sitemap.xml` y `Host: https://cannacultureapp.com`.
  - **`sitemap.xml`:** XML estándar sitemaps.org 0.9 con namespace XHTML para internacionalización (`hreflang` para ES, EN, DE, IT y x-default), prioridades (1.0 para Home, 0.8 para Guía de Cultivo) y fechas actualizadas ISO 8601.
- **Recompilación de Bundle & Cache-Busting (`?v=212`):**
  - Sincronizados `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js` mediante `python scripts/build_bundle.py`.
  - Cache-busting actualizado a `?v=212` en `index.html`, `guia-cultivo.html` y `admin-dispensario.html`.


### v211 — Expansión Botánica Mayor: 10 Nuevos Bancos de Élite & 100 Cepas Fotoperiódicas (`877 Cepas · 75 Bancos`)
- **Incorporación de 10 Bancos de Culto Mundial (10 cepas de élite por banco):**
  1. **Jungle Boys (EE. UU.):** Wedding Cake, Strawberry Shortcake, Florida Wedding, Jungle Cake, Mimosa, Motorbreath, Topanga Canyon OG, Sunset Sherbet, Perfect Triangle, Frosted Kush.
  2. **Super Sativa Seed Club (Holanda):** Karel's Haze, Frosty Friday, Lava Freeze, Pineapple Poison, Kees' Old School Haze, Fat Pete's Cookies, TNT Trichome, Kosher Haze, Super Mad Sky Floater, Durban Dew.
  3. **Reggae Seeds (España):** Juanita la Lagrimosa, Dancehall, Guayaka, Session, Kalijah, Respect, O SDK, Roots, Blackdance, Revolution.
  4. **Clearwater Genetics (EE. UU.):** Dante's Inferno, Maitai #4, Apple Tarts, Zero Gravity, Creamsicle #4, Warheads, Spec #4, Dosi-Orange, Blue Razz, Head Doctor.
  5. **LIT Farms (EE. UU.):** Grandpas Cookies, Red Velvet, Watermelon Mimosa, Bangkok Purple, Apple Banana Gelato, Road Tripper, Formula 1, Gas Station Sushi, Lemon Cherry Garlic, Blizzard.
  6. **CSI Humboldt (EE. UU.):** Bubba Kush S1, Chem '91 S1, Triangle Kush S1, Mendocino Purple, Big Bad Wolf, Irene Kush S1, Urkle S1, Fallen Angel, Chem D S1, Old Family Purple.
  7. **Tiki Madman (EE. UU.):** Devil Driver, Space Mints, Tiki Rain, Ice Cream Cake x Sunset Sherb, Pirate Milk, Dante's Wrath, Tropical Runtz, Gelato 41 BX, Gary Satan, Cherry Cosmo.
  8. **Top Dawg Seeds (EE. UU.):** Star Dawg, Tres Dawg, JJ's Nigerian Silk, Guava Chem, City Slicker, Corey Haim, Hazy Kush, Sour Chem, White Dawg, Onion Ring.
  9. **Bloom Seed Co. (EE. UU.):** Strawberry Guava, Dulce de Uva, Melted Strawberries, Grape Cream Cake, Sherbanger, Black Maple, Funk MTN, Rainbow Belts 2.0, Papaya Power, Strawberry Bubbles.
  10. **Khalifa Genetics (Francia / Internacional):** Aladdin's Skunk, Balkh Hashplant, Sheberghan Hashplant, Limon Blanco V3, Persian Prince, Moroccan Beldia, South African Kwazulu, Siberian Ruderalis IBL, Desert Skunk, Sinai Landrace.
- **Descarga e Integración de 100 Fotografías Macro Reales:**
  - 100/100 imágenes botánicas de flor real descargadas, optimizadas y procesadas en WebP (`quality=88`, `method=6`) y JPG en la carpeta `img/`.
  - Dimensiones verificadas: 100% de las imágenes con resolución >= 400x400 y peso >= 15KB.
- **Ficha Botánica y Linaje Completo:**
  - 100% de variedades con `id`, `image`, `name`, `aka`, `bank`, `species` ("Índica", "Sativa", "Híbrida"), `thc`, `cbd`, `indicaPct`, `sativaPct` (suma exacta 100%), `floweringDays`, `rating`, `reviewsCount`, `yieldIndoor`, `yieldOutdoor`, `genetics`, `lineage`, `origin`, `dominantTerpene`, `terpenes`, `aroma`, `flavors`, `effects`, `activities`, `description` en español botánico, `visualColor` y `bgPattern`.
- **Actualización de la Interfaz (`index.html` & `js/app.js`):**
  - `<title>`, `<meta name="description">`, subtítulo y badges de métricas actualizados a **877 Cepas Catalogadas** y **75 Bancos Oficiales**.
  - Cajón colapsable (`.hero-banks-list`) actualizado con los 75 bancos en orden alfabético estricto A-Z.
  - Diccionario de emojis temáticos de bancos ampliado en `js/app.js` (`🌴 Jungle Boys`, `🚀 Super Sativa Seed Club`, `🦁 Reggae Seeds`, `🌊 Clearwater Genetics`, `🔥 LIT Farms`, `🌲 CSI Humboldt`, `🗿 Tiki Madman`, `🐕 Top Dawg Seeds`, `🌸 Bloom Seed Co.`, `🏺 Khalifa Genetics`).
- **Recompilación de Bundles & Cache-Busting (`?v=211`):**
  - Ejecutado `python scripts/build_bundle.py` sincronizando `js/bundle.js`, `js/bundle-v151.js` y `js/strains-data.js`.
  - Cache-busting actualizado a `?v=211` en `index.html`, `admin-dispensario.html` y `guia-cultivo.html`.

### v210 — Organización Visual Integral, Desaturación y Pulido Estético (`index.html` & `css/styles.css`)
- **Cabecera Principal Bipolarizada (`.header-main-bar`):** Reestructurada en un nivel superior con logo a la izquierda y utilidades ordenadas en píldoras esmeralda a la derecha (`+18`, Google Auth, Selector de Tema, Modo Sobrio, Dispensario CSC). En pantallas móviles, los textos secundarios se ocultan manteniendo los iconos accesibles y compactos sin desbordamiento.
- **Navegación en Rail Horizontal Continuo (`.nav-links`):** Eliminada la cuadrícula 2x4 que saturaba la pantalla verticalmente. Sustituida por un rail fluido de píldoras con scroll táctil horizontal suave en móvil y fila armónica en escritorio para las 8 secciones (`Catálogo`, `Favoritos`, `Activity Matcher`, `Sommelier IA`, `Mezclador & Vapo`, `Vivencias`, `Terpenos`, `Guía de Cultivo`).
- **Hero Desaturado y Elegante (`.hero-section`):** Sustituido el bloque de texto denso de 40 líneas por un badge botánico, tipografía nítida con gradiente esmeralda, 4 chips de estadísticas clave (`777 Cepas`, `65 Bancos`, `8 Terpenos`, `100% Macro HD`) y un cajón colapsable discreto (`<details class="hero-banks-accordion">`) para consultar los 65 bancos oficiales sin saturar visualmente el lienzo inicial.
- **Filtros y Búsqueda Nítidos (`.search-filter-bar`):** Normalizado el espaciado vertical y padding interno de los selectores (`.custom-select`) eliminando recortes de texto. Disposición responsive apilada en móvil y cuadrícula limpia en escritorio.
- **Verificación Visual:** Capturas automatizadas generadas y validadas en resolución nativa de escritorio (1280x800) y móvil (390x844).

### v209 — Actualización Integral de Correo Corporativo Oficial (`contacto@cannacultureapp.com`)
- **Aviso Legal & Canal de Contacto (`index.html`):** Enlace `mailto:` y texto visible actualizados en la sección de Propiedad Intelectual & Enlaces a `<a href="mailto:contacto@cannacultureapp.com" class="legal-contact-link"><strong>contacto@cannacultureapp.com</strong></a>`.
- **Ecosistema de Autenticación & Fallbacks (`index.html` & `js/app.js`):** Placeholders de entrada (`login-email`, `reg-email`) y fallbacks de sesión actualizados a `@cannacultureapp.com` para total consistencia de marca.
- **User-Agent de Scripts de Botánica (`scripts/check_wikimedia.py`):** Correo de contacto del bot botánico actualizado a `contacto@cannacultureapp.com`.
- **Recompilación de Bundle (`scripts/build_bundle.py`):** Corregido script generador para sincronizar también `bundle-v151.js` y regenerados con éxito `bundle.js`, `bundle-v151.js` y `strains-data.js`.
- **Cache-Busting Actualizado a v209:** Enlaces y queries en `index.html`, `admin-dispensario.html` y `guia-cultivo.html` actualizados a `?v=209`.

### v208 — Página Independiente "🌱 Guía de Cultivo" (`guia-cultivo.html`)
- **Nueva página autónoma:** `guia-cultivo.html` + `css/guia-cultivo.css` + `js/guia-cultivo.js` (fuera del bundle; no requiere `build_bundle.py`). Tema oscuro/esmeralda con los mismos tokens de diseño que `admin-dispensario.css`, tipografías Outfit + Plus Jakarta Sans.
- **Cabecera:** logo CannaCulture, enlaces Catálogo / Guía de Cultivo / Dispensario CSC y selector de idioma `[ 🇪🇸 ES | 🇬🇧 EN | 🇩🇪 DE | 🇮🇹 IT ]`.
- **Stepper de 5 etapas (tablist accesible, teclado ←/→/Home/End, deep-link `#etapa-N`):** Germinación & Plántula · Crecimiento Vegetativo · Floración · Punto Óptimo de Cosecha (tarjetas de tricomas transparentes/lechosos/ámbar) · Secado & Curado. Cada etapa: duración, parámetros clave, paso a paso y consejo clave.
- **Bloque "⚠️ 3 Errores Clásicos de Principiante a Evitar":** encharcamiento, sobrefertilización temprana y cosecha con prisas, cada uno con su solución.
- **I18N reactivo sin recarga:** objeto `I18N` (es/en/de/it) que traduce títulos, etapas, consejos, `<title>`, meta description y `lang` del documento. Idioma compartido con el kiosco vía `localStorage('kiosk_lang')`.
- **Navegación global:** enlace `🌱 Guía de Cultivo` añadido en `index.html` (`<a class="nav-btn">` sin `data-target`, ignorado por el router SPA de `app.js`) y en la barra de `admin-dispensario.html`.
- **Cache-Busting v208:** `guia-cultivo.css/js?v=208`, `admin-dispensario.css/js?v=208`, `strains-data.js?v=208`, y en `index.html` `styles.css?v=208` / `bundle.js?v=208`.

### v207 — Traducción Reactiva de Descripciones Botánicas en Ficha Técnica (`admin-dispensario.html`)
- **Sintetizador Botánico Multi-Idioma (`getLocalizedStrainDescription`):** Implementada función generadora botánica estructurada que sintetiza descripciones coherentes y elegantes en Inglés (`en`), Alemán (`de`) e Italiano (`it`) a partir de la variedad, especie botánica, linaje parental, terpenos dominantes, aromas y efectos. En Español (`es`) conserva la descripción oficial completa de la base de datos.
- **Actualización Instantánea en Modal Abierto (`#spec-modal-desc`):** Al conmutar entre idiomas en el selector de banderas del modal (`.lang-pill-btn`), el párrafo descriptivo se refresca de inmediato en tiempo real junto con los títulos, terpenos y perfil aromático sin cerrar el diálogo.
- **Cache-Busting Actualizado a v207:** Queries de versionado actualizadas en `admin-dispensario.html` a `?v=207` para CSS y JS (`admin-dispensario.css?v=207`, `strains-data.js?v=207`, `admin-dispensario.js?v=207`).

### v205 — Diferenciación de Jerarquía Visual y Colores de Botones en Tarjeta (`admin-dispensario.html`)
- **Botón Principal / Barra Ancha (`.kiosk-tap-pill`):** Preservado el acabado esmeralda distintivo (`background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #6EE7B7;`) con texto dinámico traducido (`${t.labels.tapToViewSpec}`).
- **Botón Secundario Inferior (`.btn-card-spec`, `.btn-card-ficha`):** Rediseñado con superficie oscura translúcida (`background: rgba(255, 255, 255, 0.04);`), borde sutil y neutro (`border: 1px solid rgba(255, 255, 255, 0.12);`), tipografía en blanco hueso suave (`color: #E2E8F0;`) y hover discreto (`background: rgba(255, 255, 255, 0.08); border-color: rgba(255, 255, 255, 0.25); color: #FFFFFF;`).
- **Adaptación I18N Reactiva (`I18N[lang].labels.specBtn`):** El botón secundario se sincroniza en vivo con el idioma activo (ES: `🔬 Ficha`, EN: `🔬 Spec Sheet`, DE: `🔬 Datenblatt`, IT: `🔬 Scheda`).
- **Cache-Busting Actualizado a v205:** Enlaces en `admin-dispensario.html` actualizados a `?v=205` para CSS y JS (`admin-dispensario.css?v=205`, `strains-data.js?v=205`, `admin-dispensario.js?v=205`).

### v204 — Eliminación Definitiva en JS & CSS del Botón Duplicado de Ficha en Modo Kiosco (`admin-dispensario.html`)
- **Condicionamiento Estricto en Plantilla JS (`js/admin-dispensario.js`):** La constante `isKioskModeActive = Boolean(state.isKioskMode || document.body.classList.contains('kiosk-mode'))` previene de raíz la generación de la sección `.card-actions` en el DOM de las tarjetas, garantizando que solo exista la barra táctil ergonómica superior (`.kiosk-tap-pill`).
- **Regla CSS de Respaldo Universal (`css/admin-dispensario.css`):** Añadido selector de respaldo exhaustivo (`body.kiosk-mode .strain-menu-card button:not(.kiosk-tap-pill), body.kiosk-mode .strain-menu-card .card-actions, body.kiosk-mode .strain-menu-card footer, body.kiosk-mode .dispensario-card .card-actions, body.kiosk-mode .btn-card-spec, body.kiosk-mode .btn-card-ficha, ...`) con `display: none !important; visibility: hidden !important; height: 0 !important; margin: 0 !important; padding: 0 !important; pointer-events: none !important;`.
- **Cache-Busting Actualizado a v204:** Queries de versionado actualizadas en `admin-dispensario.html` a `?v=204` para CSS y JS (`admin-dispensario.css?v=204`, `strains-data.js?v=204`, `admin-dispensario.js?v=204`).

### v203 — Eliminación de Redundancia en Modo Kiosco & Traducción Dinámica de Ficha (`admin-dispensario.html`)
- **Eliminación de Botón Redundante:** Ocultado el contenedor `.card-actions` y los selectores `.btn-card-spec` y `.btn-card-ficha` en `body.kiosk-mode` vía CSS (`display: none !important;`) y condicionado el template en `js/admin-dispensario.js` para que solo se renderice en Modo Encargado, manteniendo exclusivamente la barra táctil superior (`.kiosk-tap-pill`) en la vista mostrador.
- **Mapeo I18N Dinámico para Botón de Ficha (`specBtn`):** Incorporada la clave `specBtn` en `I18N[lang].labels` en los 4 idiomas:
  * es: `"🔬 Ficha"`
  * en: `"🔬 Spec Sheet"`
  * de: `"🔬 Datenblatt"`
  * it: `"🔬 Scheda"`
- **Cache-Busting Actualizado a v203:** Queries de versionado actualizadas en `admin-dispensario.html` a `?v=203` para CSS y JS.

### v202 — Sistema Multi-Idioma Reactivo ES/EN/DE/IT en Modo Kiosco & Ficha Técnica (`admin-dispensario.html`)
- **Arquitectura I18N Reactiva y Ligera:** Implementada la constante global `I18N` con soporte completo para 4 idiomas clave: Español 🇪🇸 (`es`), Inglés 🇬🇧 (`en`), Alemán 🇩🇪 (`de`) e Italiano 🇮🇹 (`it`), sin librerías ni dependencias externas.
  * Tiers de aportación traducidos: Estándar/Colaborador/Terapéutico, Standard/Collaborator/Therapeutic, Standard/Förderer/Therapeutisch, Standard/Collaboratore/Terapeutico.
  * Especies botánicas: Híbrida/Índica/Sativa, Hybrid/Indica/Sativa, Hybrid/Indica/Sativa, Ibrida/Indica/Sativa.
  * Estado de barra: Disponible/En reserva, Available/Reserved, Verfügbar/Reserviert, Disponibile/In riserva.
  * Diccionario de efectos botánicos y perfil terpénico aromático dinámico.
  * Persistencia en `localStorage.getItem('kiosk_lang') || 'es'`.
- **Selector Visual Táctil de Banderas en Kiosco:** Píldoras táctiles ergonómicas `[ 🇪🇸 ES | 🇬🇧 EN | 🇩🇪 DE | 🇮🇹 IT ]` integradas en el banner superior `#kiosk-top-notice`, en la barra de navegación y en la cabecera del modal botánico, con realce visual esmeralda tenue activo (`border: 1px solid var(--accent-emerald)`).
- **Actualización Instantánea en Modal Abierto:** Al cambiar de idioma mientras el modal de ficha técnica botánica (`#kiosk-strain-modal`) está abierto, sus textos, terpenos, notas y tiers se actualizan en tiempo real sin cerrar el diálogo (`renderKioskModalContent`).
- **Cache-Busting Actualizado a v202:** Queries de cache-busting actualizadas en `admin-dispensario.html` a `?v=202` en CSS y JS.

### v201 — Cache-Busting v201, Salto de Línea Forzado y Evento Click Infalible (`admin-dispensario.html`)
- **Cache-Busting Unificado v201:** Actualizados los enlaces en `admin-dispensario.html` a `css/admin-dispensario.css?v=201`, `js/admin-dispensario.js?v=201` y `js/strains-data.js?v=201` para invalidar inmediatamente la caché de navegador en clientes y tablets de mostrador.
- **Salto de Línea en Linaje y Notas de Lote (`css/admin-dispensario.css`):** Sobrescritura estricta con `!important` para `.card-lineage`, `.card-lot-note`, `.lot-note`, `.lineage-text` tanto en modo estándar como en modo Kiosco:
  * `white-space: normal !important;`
  * `overflow: visible !important;`
  * `text-overflow: clip !important;`
  * `word-break: break-word !important;`
  * `line-height: 1.4 !important;`
  * `display: block !important;`
  * `max-height: none !important; height: auto !important; -webkit-line-clamp: unset !important;`
- **Evento Click y Apertura Infalible de Modal en Modo Kiosco (`js/admin-dispensario.js`):**
  * `cursor: pointer !important` aplicado en CSS a todas las tarjetas y elementos descendientes en modo Kiosco.
  * Inyección de `onclick="window.handleCardClick && window.handleCardClick(event, '${item.id}')"` directo en la etiqueta `<article class="strain-menu-card">`.
  * Apertura segura del elemento nativo `<dialog id="kiosk-strain-modal">` con control de `modal.open`, envoltorio try/catch y fallback a `modal.setAttribute('open', '')` con centrado CSS absoluto (`top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 99999`).
  * Cálculo seguro del rating botánico sin riesgos de `RangeError` y fallback de fotografías botánicas.
  * Delegación doble reforzada en `strains-menu-grid` y exportación de funciones al entorno global `window`.

### v200 — Vista Kiosco Mostrador & Ficha Técnica Botánica Completa (`admin-dispensario.html`)
- **Corrección de Legibilidad en Tarjetas de Mostrador:** Eliminado el recorte agresivo `ellipsis`/`nowrap` en `.card-lineage` y `.card-lot-note`. Se implementó un clamp fluido de 2 líneas (`-webkit-line-clamp: 2; line-height: 1.35; white-space: normal;`) preservando la cuadrícula y añadiendo el atributo `title` nativo con el texto completo en linajes y notas agronómicas.
- **Ficha Técnica Botánica Interactiva (Modo Kiosco & Mostrador):** Modal popup reactivo (`#kiosk-strain-modal`) abierto al pulsar cualquier tarjeta en Vista Kiosco o el botón `🔬 Ficha`:
  * Fotografía macro en alta resolución 800×800 con badge `🔍 Toca para Zoom HD` y visor Lightbox a pantalla completa (`#kiosk-lightbox-dialog`).
  * Título de cepa, breeder/banco, badge botánico (Índica/Sativa/Híbrida), linaje parental completo y métricas THC/CBD/Floración.
  * Cuadro de aportaciones (€/g) por Tiers de socio (Nivel Estándar, Nivel Colaborador, Nivel Terapéutico) asignadas por el club.
  * Notas agronómicas y curado del lote local asignado en mostrador.
  * Desglose completo de terpenos dominantes con barras porcentuales coloreadas según `window.TERPENES_INFO`.
  * Etiquetas de efectos botánicos y perfil aromático/cata.
  * Descripción botánica oficial extraída dinámicamente de `strains-data.js`.
- **Navegación y Ergonomía Táctil:** Botón de cierre visible (✕), cierre por clic en backdrop exterior o pulsando la tecla `Escape`.

### v199 — Módulo Panel de Gestión del Dispensario para Encargados de CSC (`admin-dispensario.html`)
- **Panel Modular e Independiente:** Construido en `admin-dispensario.html` con lógica desacoplada en `js/admin-dispensario.js` y estilos dedicados en `css/admin-dispensario.css`, sin alterar la operatividad de `index.html`.
- **Estricta Terminología Legal CSC (España):** 0 ocurrencias de términos comerciales ("precio", "venta", "comprar"). Uso exclusivo de "Aportación/g", "Contribución", "Disponibilidad en mostrador", "Menú de previsión" y "Consumo Compartido".
- **Buscador en Tiempo Real del Catálogo Maestro:** Conectado a las 777 cepas maestras de `strains-data.js` con autocompletado en vivo, miniaturas HD 800x800 y adición instantánea en un solo toque táctil.
- **Menú Activo en Barra:** Tarjetas con miniaturas fotográficas HD, tags genéticos, switch deslizante táctil (En Barra / Disponible vs Agotado / Oculto), filtros rápidos de categorías (Todas, Flores, Extracciones, Comestibles) y contadores de stock y carta en tiempo real.
- **Editor de Cuotas y Previsiones por Niveles de Socio:** Configuración de cuotas de aportación (€/g) por categorías de socio (Nivel Estándar, Nivel Colaborador, Nivel Terapéutico), previsión en gramos de mostrador y notas de lote / cata local. Botón táctil con animación de guardado exitoso.
- **Vista Kiosco Mostrador (Tablet):** Modo interactivo a pantalla completa optimizado para tablets de mostrador para visualización de variedades disponibles por socios registrados.
- **Sincronización Híbrida Firebase Cloud / Demo Local:** Integración con Firebase Authentication y Firestore con persistencia reactiva en `localStorage`. Inicialización automática en Modo Demo precargado con Gelato #33, Amnesia Haze, Super Boof, Kmintz, Jealousy, etc. para interacción inmediata sin necesidad de login previo.
- **Acceso Directo desde Catálogo Principal:** Botón de acceso directo integrado en la barra de control de `index.html` (`⚖️ Dispensario CSC`).
- **Bundle & Cache-Busting:** Generado `js/strains-data.js` y recompilado `js/bundle.js`. Versionado unificado en `?v=2026_dispensario_csc_v199`.

### v198 — Restauracion de Iluminacion Natural Uniforme (70 Cepas Recientes)
- **Diagnostico y Correccion de Viñeta:** Eliminacion completa del filtro de viñeta radial artificial (`make_correct_vignette`), causante del oscurecimiento perimetral y foco de linterna central reportado por el usuario.
- **Alcance del Reprocesamiento:** 70 variedades de las incorporaciones recientes (Greenpoint Seeds, Big Buddha Seeds, Seed Junky Genetics, Bodhi Seeds, Oni Seed Co., Black Farm Genetix y Purple City Genetics).
- **Fidelidad Fotografica:** Encuadre centrado 1:1, preservacion integra de hojas de azucar y calices perimetrales, iluminacion balanceada y organica que coincide con el estandar historico del catalogo.
- **Unicidad dHash 256-bit:** Resolucion de candidatos para `bodhi-blue-tara`, `bodhi-dream-lotus`, `pcg-benzina` y `pcg-honey-runtz`. Auditoria global con 0 colisiones en las 1.498 imagenes de la base de datos.
- **Bundle & Cache-Busting:** Recompilado `bundle.js` y version actualizada en `index.html` (`?v=2026_natural_lighting_v198`).

### v197 — Greenpoint Seeds & Big Buddha Seeds (20 cepas HD)
- **Greenpoint Seeds (10 iconos del breeding de Colorado con cruces Stardawg / Chem):**
  1. `gp-gunslinger`: **Gunslinger** (60% Índica / 40% Sativa, Star Fighter x Stardawg).
  2. `gp-cookies-and-chem`: **Cookies and Chem** (60% Índica / 40% Sativa, Girl Scout Cookies x Stardawg).
  3. `gp-jelly-pie`: **Jelly Pie** (60% Índica / 40% Sativa, Grape Pie x Stardawg).
  4. `gp-city-slicker`: **City Slicker** (65% Índica / 35% Sativa, Gelato 33 x Stardawg).
  5. `gp-copper-chem`: **Copper Chem** (50% Híbrida, Chem 4 x Stardawg).
  6. `gp-tomahawk`: **Tomahawk** (55% Índica / 45% Sativa, Gorilla Glue #4 x Stardawg).
  7. `gp-purple-mountain-majesty`: **Purple Mountain Majesty** (70% Índica / 30% Sativa, Purple Urkle x Stardawg).
  8. `gp-texas-butter`: **Texas Butter** (70% Índica / 30% Sativa, Casey Jones x Stardawg).
  9. `gp-blizzard-bush`: **Blizzard Bush** (65% Índica / 35% Sativa, The White x Stardawg).
  10. `gp-night-terror-og`: **Night Terror OG** (70% Índica / 30% Sativa, Blue Dream x Rare Dankness #1).

- **Big Buddha Seeds (10 leyendas británicas del queso y skunk artesanal):**
  1. `bbs-big-buddha-cheese`: **Big Buddha Cheese** (60% Índica / 40% Sativa, UK Cheese clone x Afghan Indica). La campeona Cheese original de la High Times Cannabis Cup 2006.
  2. `bbs-blue-cheese`: **Blue Cheese** (75% Índica / 25% Sativa, Big Buddha Cheese x Blueberry).
  3. `bbs-chiesel`: **Chiesel** (60% Sativa / 40% Índica, Big Buddha Cheese x NYC Diesel).
  4. `bbs-buddha-tahoe`: **Buddha Tahoe** (80% Índica / 20% Sativa, Tahoe OG Kush clone x Big Buddha Cheese (Reversed)).
  5. `bbs-cheesy-dick`: **Cheesy Dick** (70% Índica / 30% Sativa, Big Buddha Cheese x Moby Dick).
  6. `bbs-cheese-dawg`: **Cheese Dawg** (75% Índica / 25% Sativa, Chemdawg 91 x Big Buddha Cheese (Reversed)).
  7. `bbs-silver-buddha-haze`: **Silver Buddha Haze** (75% Sativa / 25% Índica, Super Silver Haze x Big Buddha Cheese (Reversed)).
  8. `bbs-freeze-cheese-89`: **Freeze Cheese '89** (80% Índica / 20% Sativa, Friesland Indica 1989 x Big Buddha Cheese).
  9. `bbs-black-cheese`: **Black Cheese** (85% Índica / 15% Sativa, Black Spanish Indica x Big Buddha Cheese).
  10. `bbs-bubble-squeak`: **Bubble Squeak** (70% Índica / 30% Sativa, Bubblegum Indiana Cut x Big Buddha Cheese).

- **Fotografias Botanicas Oficiales HD (v197):** 20 imagenes macro reales de flores con procesado radial oscuro CannaCulture (WebP q90 + JPG q88). 0 fondos blancos, 0 halos, 0 marcas de agua.
- **Auditoria Exhaustiva Anti-Colision dHash / pHash (777 cepas, 1498 imagenes indexadas):**
  * Metodo: dHash / pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 777/777 cepas (100%).

### v196 — Seed Junky Genetics & Bodhi Seeds (20 cepas HD)
- **Seed Junky Genetics (10 iconos modernos de JBeezy, Los Ángeles):**
  1. `sj-kush-mints`: **Kush Mints** (55% Índica / 45% Sativa, Bubba Kush x Animal Mints).
  2. `sj-animal-mints`: **Animal Mints** (60% Índica / 40% Sativa, Animal Cookies x SinMint Cookies).
  3. `sj-jealousy`: **Jealousy** (50% Híbrida, Gelato 41 x Sherbert Bx1). Cepa del Año Leafly 2022.
  4. `sj-ice-cream-cake`: **Ice Cream Cake** (75% Índica / 25% Sativa, Wedding Cake x Gelato 33).
  5. `sj-gas-face`: **Gas Face** (70% Índica / 30% Sativa, Face Mints x [Biscotti x Sherbert]).
  6. `sj-animal-face`: **Animal Face** (70% Sativa / 30% Índica, Face Off OG x Animal Mints).
  7. `sj-permanent-marker`: **Permanent Marker** (60% Índica / 40% Sativa, [Biscotti x Jealousy] x Sherb Bx). Cepa del Año Leafly 2023.
  8. `sj-jungle-cake`: **Jungle Cake** (60% Índica / 40% Sativa, White Fire #43 x Wedding Cake).
  9. `sj-la-kush-cake`: **LA Kush Cake** (70% Índica / 30% Sativa, Wedding Cake x Kush Mints #11).
  10. `sj-the-soap`: **The Soap** (50% Híbrida, Animal Mints x Kush Mints).

- **Bodhi Seeds (10 iconos de cultivo orgánico y landraces de California):**
  1. `bodhi-goji-og`: **Goji OG** (60% Sativa / 40% Índica, Nepali OG x Snow Lotus).
  2. `bodhi-space-monkey`: **Space Monkey** (70% Índica / 30% Sativa, Gorilla Glue #4 x Wookie #15).
  3. `bodhi-dream-lotus`: **Dream Lotus** (60% Sativa / 40% Índica, Blue Dream x Snow Lotus).
  4. `bodhi-snow-lotus`: **Snow Lotus** (70% Índica / 30% Sativa, Afgooey x Blockhead).
  5. `bodhi-mothers-milk`: **Mother's Milk** (50% Híbrida, Nepali OG x Appalachia).
  6. `bodhi-sunshine-daydream`: **Sunshine Daydream** (60% Índica / 40% Sativa, Bubbashine x Appalachia).
  7. `bodhi-blue-tara`: **Blue Tara** (65% Índica / 35% Sativa, Bubbashine x Snow Lotus).
  8. `bodhi-good-medicine`: **Good Medicine** (50% Híbrida CBD, Harlequin x Appalachia).
  9. `bodhi-ancient-og`: **Ancient OG** (75% Índica / 25% Sativa, Iranian Landrace x Snow Lotus).
  10. `bodhi-prayer-tower`: **Prayer Tower** (70% Sativa / 30% Índica, Lemon Thai x Appalachia).

- **Fotografias Botanicas Oficiales HD (v196):** 20 imagenes reales de flores de cogollo de alta resolucion (hasta 3872x2592), procesadas a 800x800 con el pipeline radial oscuro CannaCulture (WebP calidad 90 + JPG calidad 88). Cero fondos blancos, cero logos o graficos 3D.
- **Auditoria Exhaustiva Anti-Colision dHash / pHash (757 cepas, 1478 imagenes indexadas):**
  * Metodo: dHash / pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 757/757 cepas (100%).

### v195 — Corrección Integral de Fotografías (30 cepas HD)

### v194 — Purple City Genetics (10 cepas HD)
- **Purple City Genetics (10 leyendas maestras de resina de Oakland, CA & Barcelona):**
  1. `pcg-gush-mints`: **Gush Mints** (70% Índica / 30% Sativa, Kush Mints x F1 Durb x Gushers).
  2. `pcg-honey-runtz`: **Honey Runtz** (50% Híbrida, Runtz x Honey Boo Boo).
  3. `pcg-benzina`: **Benzina** (65% Índica / 35% Sativa, Fuel OG x Gelato 33).
  4. `pcg-acid-wash`: **Acid Wash** (70% Índica / 30% Sativa, Biscotti x Gush Mints).
  5. `pcg-bishop`: **Bishop** (60% Índica / 40% Sativa, Vietnam Gold x Gush Mints).
  6. `pcg-orange-76`: **Orange 76** (65% Sativa / 35% Índica, Orange Cookies x Moroccan Peaches).
  7. `pcg-daily-operation`: **Daily Operation** (65% Índica / 35% Sativa, Batshit x Gush Mints).
  8. `pcg-fillmore-slim`: **Fillmore Slim** (60% Índica / 40% Sativa, Mac 1 x Forum Cut GSC).
  9. `pcg-hooch`: **Hooch** (70% Índica / 30% Sativa, Slurricane x Gush Mints).
  10. `pcg-space-station`: **Space Station** (75% Índica / 25% Sativa, Alien Kush x Gush Mints).

- **Fotografias Botanicas Oficiales HD (v194):** 10 imagenes reales de cogollos de alta resolucion procesadas a 800x800 con el pipeline radial oscuro CannaCulture (WebP calidad 90 + JPG calidad 88).
- **Auditoria Exhaustiva de Todo el Catalogo (737 cepas, 1458 imagenes indexadas):**
  * Metodo: dHash / pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 737/737 cepas (100%).

### v193 — Black Farm Genetix (10 cepas HD)
- **Black Farm Genetix (10 leyendas modernas de Sitges/Barcelona):**
  1. `bfg-glukies`: **Glukies** (70% Índica / 30% Sativa, Gorilla Glue #4 x Original Thin Mint Girl Scout Cookies).
  2. `bfg-wasabi`: **Wasabi** (75% Índica / 25% Sativa, Orange Punch x Do-Si-Dos).
  3. `bfg-tiramisu`: **Tiramisu** (70% Índica / 30% Sativa, Wedding Cake x Gelato 45).
  4. `bfg-acai-bananas`: **Acai & Bananas** (55% Índica / 45% Sativa, Acai Berry Cake x Banana Punch).
  5. `bfg-banana-slammer`: **Banana Slammer** (75% Índica / 25% Sativa, Slurricane x Banana Punch).
  6. `bfg-banana-glukies`: **Banana Glukies** (60% Índica / 40% Sativa, Glukies x Banana Punch).
  7. `bfg-limosa`: **Limosa** (65% Sativa / 35% Índica, Limoncello x Panna Cotta).
  8. `bfg-ipanema`: **Ipanema** (55% Índica / 45% Sativa, Tropicanna Glue x Banana Punch).
  9. `bfg-high-octane`: **High Octane** (75% Índica / 25% Sativa, Sunset Octane x Orange Punch).
  10. `bfg-peach-tsunami`: **Peach Tsunami** (50% Híbrida, Peach Ozz x Orange Punch).

- **Fotografias Botanicas Oficiales HD (v193):** 10 imagenes reales de cogollos de alta resolucion procesadas a 800x800 con el pipeline radial oscuro CannaCulture (WebP calidad 90 + JPG calidad 88).
- **Auditoria Exhaustiva de Todo el Catalogo (727 cepas, 1448 imagenes indexadas):**
  * Metodo: dHash / pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 727/727 cepas (100%).

### v192 — Reserva Privada & Oni Seed Co. (20 cepas HD)
- **Reserva Privada (10 iconos legendarios de California y DNA Genetics):**
  1. `rp-og-18`: **The OG #18** (75% Índica / 25% Sativa, OG Kush Phenotype #18).
  2. `rp-kosher-kush`: **Kosher Kush** (100% Índica, Unknown LA Pure Indica Clone / Jewish Gold).
  3. `rp-kandy-kush`: **Kandy Kush** (55% Índica / 45% Sativa, OG Kush x Trainwreck T4).
  4. `rp-purple-og-18`: **Purple OG #18** (85% Índica / 15% Sativa, The OG #18 x Purple Wreck).
  5. `rp-purple-wreck`: **Purple Wreck** (80% Sativa / 20% Índica, Purple Urkle x Trainwreck T4).
  6. `rp-cole-train`: **Cole Train** (75% Sativa / 25% Índica, Trainwreck x Hashplant).
  7. `rp-strawberry-banana`: **Strawberry Banana** (70% Índica / 30% Sativa, Strawberry Bubblegum x Banana Kush).
  8. `rp-lemon-larry-og`: **Lemon Larry OG** (70% Índica / 30% Sativa, Larry OG Phenotype).
  9. `rp-3-bears-og`: **3 Bears OG** (80% Índica / 20% Sativa, SFV OG IBL).
  10. `rp-sour-kush`: **Sour Kush** (50% Híbrida, Sour Diesel x OG Kush).

- **Oni Seed Co. (10 joyas modernas de Harry Palms & Oni Noodles):**
  1. `oni-tropicanna-cookies`: **Tropicanna Cookies** (65% Sativa / 35% Índica, Forum Cut GSC x Tangie).
  2. `oni-strawberry-guava`: **Strawberry Guava** (60% Índica / 40% Sativa, Strawberry Banana #14 x Papaya).
  3. `oni-papaya`: **Papaya** (75% Índica / 25% Sativa, Citral #13 x Ice #2 / KC Brains Mango x Afghani #1).
  4. `oni-tropicana-punch`: **Tropicana Punch** (70% Sativa / 30% Índica, Tropicanna Cookies x Purple Punch).
  5. `oni-papaya-punch`: **Papaya Punch** (55% Índica / 45% Sativa, Papaya x Purple Punch).
  6. `oni-black-garlic`: **Black Garlic** (70% Índica / 30% Sativa, GMO Cookies x Tropicanna Cookies).
  7. `oni-honey-bunny`: **Honey Bunny** (55% Sativa / 45% Índica, Tropicanna Cookies x Honey Boo Boo).
  8. `oni-mango-lemonade`: **Mango Lemonade** (70% Sativa / 30% Índica, Papaya x Tropicanna Cookies).
  9. `oni-tropicanna-banana`: **Tropicanna Banana** (50% Híbrida, Tropicanna Cookies x Banana OG).
  10. `oni-papaya-sorbet`: **Papaya Sorbet** (55% Índica / 45% Sativa, Papaya x Sherbert).

- **Fotografias Botanicas Oficiales HD (v192):** 20 imagenes reales de flores de cogollo de alta resolucion procesadas a 800x800 con el pipeline radial oscuro CannaCulture (WebP calidad 90 + JPG calidad 88).
- **Auditoria Exhaustiva de Todo el Catalogo (717 cepas, 1445 imagenes indexadas):**
  * Metodo: dHash / pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 717/717 cepas (100%).

### v191 — The Cali Connection & Cannarado Genetics (20 cepas HD)
- **The Cali Connection (10 cepas de culto californianas):**
  1. `cali-sfv-og-kush`: **SFV OG Kush** (90% Índica / 10% Sativa, San Fernando Valley OG x Afghani #1).
  2. `cali-tahoe-og-kush`: **Tahoe OG Kush** (80% Índica / 20% Sativa, Tahoe OG Clone x SFV OG Kush IBL).
  3. `cali-deadhead-og`: **Deadhead OG** (60% Sativa / 40% Índica, Chemdawg 91 Skunk VA x SFV OG Kush F4).
  4. `cali-alien-og`: **Alien OG** (50% Híbrida, Alien Kush x Tahoe OG Kush).
  5. `cali-blackwater`: **Blackwater** (85% Índica / 15% Sativa, Mendo Purps x SFV OG Kush F3).
  6. `cali-corleone-kush`: **Corleone Kush** (80% Índica / 20% Sativa, Pre-98 Bubba Kush x SFV OG Kush F4).
  7. `cali-jedi-kush`: **Jedi Kush** (70% Índica / 30% Sativa, Death Star x SFV OG Kush F5).
  8. `cali-larry-og-kush`: **Larry OG Kush** (70% Índica / 30% Sativa, Larry OG x SFV OG Kush IBL).
  9. `cali-grape-og`: **Grape OG** (60% Índica / 40% Sativa, Tahoe OG Kush x Grape Romulan).
  10. `cali-girl-scout-cookies`: **Girl Scout Cookies (Cali Connection)** (60% Índica / 40% Sativa, Forum Cut GSC x SFV OG Kush).

- **Cannarado Genetics (10 leyendas modernas de Colorado):**
  1. `cannarado-sundae-driver`: **Sundae Driver** (50% Híbrida, Fruity Pebbles OG x Grape Pie).
  2. `cannarado-wedding-pie`: **Wedding Pie** (70% Índica / 30% Sativa, Wedding Cake x Grape Pie).
  3. `cannarado-apple-sundae`: **Apple Sundae** (60% Sativa / 40% Índica, Sour Apple x Sundae Driver).
  4. `cannarado-birthday-cake`: **Birthday Cake** (65% Índica / 35% Sativa, Girl Scout Cookies x Cherry Pie).
  5. `cannarado-banana-sundae`: **Banana Sundae** (60% Índica / 40% Sativa, Banana OG x Sundae Driver).
  6. `cannarado-biscotti-sundae`: **Biscotti Sundae** (70% Índica / 30% Sativa, Biscotti x Sundae Driver).
  7. `cannarado-kitchen-sink`: **Kitchen Sink** (75% Índica / 25% Sativa, GMO Cookies x Sundae Driver).
  8. `cannarado-pie-hoe`: **Pie Hoe** (70% Índica / 30% Sativa, Grape Pie x Tahoe OG).
  9. `cannarado-5-alive`: **5 Alive** (70% Sativa / 30% Índica, Bubblegum x Orange Juice x Grape Pie).
  10. `cannarado-birthday-funk`: **Birthday Funk** (70% Índica / 30% Sativa, Birthday Cake x Dosidos).

- **Fotografias Botanicas Oficiales HD (v191):** 20 imagenes reales de cogollos de alta resolucion (hasta 4032x3024), procesadas a 800x800 con el pipeline radial oscuro CannaCulture (WebP + JPG).
- **Auditoria Exhaustiva de Todo el Catalogo (697 cepas, 1418 imagenes):**
  * Metodo: pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 697/697 cepas (100%).

### v190 — María Master Sumiller & CannaDoctor 2.0 (Femenino)
- **Identidad de María**: La anfitriona experta y sommelier oficial es ahora María, una sumiller y botánica culta, cercana y con criterio propio.
- **Concordancia en femenino**: Adaptación de todos los prompts de sistema (Gemini Cloud, LLM Local Ollama, Gemini Nano y Motor Autónomo), títulos de interfaz ("María | Master Sumiller & CannaDoctor 2.0", "María | Sumiller IA"), placeholders, badges y mensajes de razonamiento ("RAZONAMIENTO DE LA SOMMELIER").
- **Avatar Femenino**: Incorporación del avatar `👩‍🌾` tanto en el header inline de la sección como en el widget flotante.
- **Saludo Inicial Proactivo**: Al cargar el chat, María saluda y presenta de forma acogedora las capacidades de maridaje, CannaDoctor 2.0, charla abierta y locución interactiva.
- **Voz TTS Femenina**: Selector de síntesis de voz que prioriza voces naturales femeninas en español si están instaladas en el sistema/navegador.
- **Compatibilidad Retrospectiva**: Alias `MATEO_SYSTEM_PROMPT = MARIA_SYSTEM_PROMPT` preservado en cliente y servidor para evitar incompatibilidades.

### v189 — Mobile Optimization
- **Ventana flotante**: Sheet nativo a pantalla casi completa en móvil (88dvh/92dvh).
- **Swipe-down para cerrar**: Gesto táctil nativo para descartar la ventana flotante.
- **Sin zoom iOS**: Inputs con `font-size: 16px` mínimo.
- **Targets táctiles 44x44px**: Todos los botones con área táctil cómoda para dedos.
- **Pills scroll horizontal**: Desplazamiento fluido sin desbordar la pantalla.
- **FAB compacto**: Icono optimizado en pantallas estrechas (<=480px).

---

## Metricas del Catalogo
- **Variedades Totales:** 697 (100% unicas)
- **Bancos Activos:** 57
- **Duplicados Visuales (pHash 256-bit):** 0
- **Fondos Blancos:** 0 (todos corregidos)
- **Fotoperiodicas:** 100%
- **Cobertura Linaje/Genetica:** 100%

---

## Historial de Versiones Recientes
### v188 — Dr. Underground + Crockett Family Farms (20 cepas HD)
- **55 Bancos Oficiales Incorporados**, ultimos agregados en v188:
  * **Dr. Underground (10 cepas de élite):**
    1. `drug-king-kong`: **King Kong** (75% Índica / 25% Sativa, Ed Rosenthal Super Bud x Chronic).
    2. `drug-melon-gum`: **Melon Gum** (60% Índica / 40% Sativa, Bubblegum x Lavender).
    3. `drug-crystal-meth`: **Crystal M.E.T.H.** (80% Sativa / 20% Índica, Destroyer x Critical Mass).
    4. `drug-painkiller`: **Painkiller** (75% Índica / 25% Sativa, Sensi Star x White Russian - Alto CBD).
    5. `drug-brooklyn-mango`: **Brooklyn Mango** (50% Híbrida, Brooklyn Mango Clone x NYC Diesel).
    6. `drug-kong-47`: **Kong 47** (60% Índica / 40% Sativa, King Kong x AK-47).
    7. `drug-black-jesus-og`: **Black Jesus OG** (85% Índica / 15% Sativa, Tahoe OG x Soul Star).
    8. `drug-u-pink-kush`: **U-Pink Kush** (80% Índica / 20% Sativa, Underground Pink Kush).
    9. `drug-soul-star`: **Soul Star** (75% Índica / 25% Sativa, Sensi Star x Peyote Purple).
    10. `drug-american-beauty`: **American Beauty** (55% Índica / 45% Sativa, Plushberry x King Kong).

  * **Crockett Family Farms (10 cepas de élite):**
    1. `cff-sour-tangie`: **Sour Tangie** (80% Sativa / 20% Índica, East Coast Sour Diesel x Tangie).
    2. `cff-clementine`: **Clementine** (70% Sativa / 30% Índica, Tangie x Lemon Skunk).
    3. `cff-banana-split`: **Banana Split** (60% Índica / 40% Sativa, Tangie x Banana Sherbet).
    4. `cff-citrus-sap`: **Citrus Sap** (50% Híbrida, GG4 x Tangie).
    5. `cff-crocketts-dawg`: **Crockett's Dawg** (60% Índica / 40% Sativa, Guava Dawg x Family Secret).
    6. `cff-strawberry-clem`: **Strawberry Clem** (50% Híbrida, Strawberry Banana x Clementine).
    7. `cff-strawberry-lemon-banana`: **Strawberry Lemon Banana** (55% Índica / 45% Sativa, Strawberry Banana x Lemon Skunk).
    8. `cff-tangie-jack`: **Tangie Jack** (80% Sativa / 20% Índica, Jack Herer x Tangie).
    9. `cff-banana-spritz`: **Banana Spritz** (65% Índica / 35% Sativa, Banana Sherbet x Spritzer).
    10. `cff-malawi-moonshine`: **Malawi Moonshine** (85% Sativa / 15% Índica, Malawi Sativa x Moonshine Haze).

- **Fotografias Botanicas Oficiales HD (v188):** 20 imagenes reales de cogollos en alta resolucion nativa (hasta 2048x2048), procesadas a 800x800 con el pipeline oscuro radial CannaCulture (WebP + JPG). Nitidez cristalina, sin pixelado, sin fondos blancos.
- **Auditoria Exhaustiva de Todo el Catalogo (677 imagenes):**
  * Metodo: pHash 256 bits (16x16) con umbral Hamming <= 4.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 677/677 cepas (100%).
- **Arquitectura Dual del Sommelier (Ollama local + Gemini Cloud 24/7).**


