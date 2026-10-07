# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-10-07 18:45  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `fix(i18n): traduccion reactiva de descripciones botanicas en ficha tecnica v207`  
> **Version Cache-Busting:** `?v=207`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **777 cepas botanicas 100% unicas y originales, 0 duplicados visuales.**
- **65 Bancos Oficiales Incorporados**
- **Cobertura Linaje/Genetica:** 777/777 cepas (100%).
- **Fotografias Botanicas HD:** 100% macro flores reales en fondo oscuro, 0 fondos blancos, 0 colisiones visuales, 0 viñetas artificiales.
- **Módulo CSC Mostrador & Kiosco:** Operativo con Ficha Técnica interactiva, Lightbox macro HD, legibilidad fluida en tarjetas, persistencia híbrida Firebase / Demo y selector multi-idioma reactivo (ES/EN/DE/IT).

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


