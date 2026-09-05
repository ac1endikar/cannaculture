# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Última actualización:** 2026-09-05 17:22  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado vía `server.ps1`)

---

## 1. Información General del Proyecto
- **Tipo:** Single Page Application (SPA) modular en Vanilla JS + Vanilla CSS.
- **Base de datos:** 402 cepas únicas y consolidadas pertenecientes a 38 bancos de semillas premium en `js/data.js`.
- **Cargador de producción:** `js/bundle.js` (versión actual en `index.html`: `?v=2026_dock_fix_v128`).
- **Tema:** Dark Theme Glassmorphism con paleta esmeralda / dorado mate (#080C0B, acentos #10B981 y #D4AF37).

---

## 2. Estado de la Fase Visual y Rendimiento
- **Fase 2 de Reemplazo y Optimización Visual de Imágenes:** **100% COMPLETADA (143/143)**
- **Optimización WebP Masiva:** **100% COMPLETADA (955/955)**
  - Reducción de peso de assets: **388.69 MB ➔ 182.41 MB (Ahorro del 53.1%)**.
  - 402/402 referencias en `js/data.js` migradas a `.webp` (0 imágenes faltantes).
  - Lazy Loading (`loading="lazy"` + `decoding="async"`) activo en tarjetas del catálogo.
- **Mobile Responsive Engine (Ficha Técnica):** **100% OPTIMIZADO** (Soporte fluido en ≤768px, ≤480px y ≤400px).
- **Módulo Comparador Cara a Cara & HUD Táctil (v128):** **100% COMPLETADO Y OPERATIVO** (Cero colisiones con el Sommelier IA).

---

## 3. Tareas Completadas Recientemente (2026-09-05)
1. ✅ **Corrección de Superposición UI — Dock Comparador vs Botón Flotante Sommelier IA (17:22):**
   - **Comportamiento Dinámico del Sommelier IA (`#ai-chat-trigger` / `.sommelier-fab-btn`):** Transición CSS suave `bottom 0.35s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s ease`. Al activarse el comparador (clase reactiva `.compare-dock-visible` en `document.body`), el botón del Sommelier se desplaza automáticamente hacia arriba a `bottom: 110px !important;` en móviles anclado a la derecha (margen de 16px), con `z-index: 100` y sombra con blur esmeralda preservada, evitando cualquier solapamiento con los controles de comparación.
   - **Refinamiento del Dock Comparador como HUD Táctil (`#compare-floating-dock`):**
     * Fondo *Dark Glassmorphism* `rgba(6, 11, 9, 0.92)` con `backdrop-filter: blur(20px)`, borde superior `1px solid rgba(16, 185, 129, 0.35)` y sombra envolvente `0 -8px 30px rgba(0, 0, 0, 0.8)`.
     * Safe-area padding para dispositivos modernos: `padding-bottom: calc(12px + env(safe-area-inset-bottom, 0px));`.
     * Layout horizontal optimizado en móvil: Cabecera compacta a la izquierda (icono `⚖️` + badge contador `N/3`), carrusel horizontal táctil de chips con miniaturas HD en el centro, y a la derecha botón brillante de lanzamiento "⚖️ Comparar (N/3)" junto a botón de vaciado "🗑️ Limpiar".
   - **Build y Versión:** Bundle recompilado vía `python scripts/build_bundle.py` (608,885 bytes) y versión sincronizada en `index.html` a `?v=2026_dock_fix_v128` tanto en `<link rel="stylesheet">` como en `<script src="js/bundle.js">`.

2. ✅ **Implementación Fase 2 — Módulo Comparador Cara a Cara (17:15):**
   - **Botón Toggle en Tarjetas de Cepa:** Integrado en el footer de cada tarjeta del catálogo con estados visuales activos ("⚖️ Comparando") e inactivos ("⚖️ Comparar").
   - **Gestión de Estado Reactiva:** Array de cepas seleccionadas con límite estricto de máximo 3 variedades. Disparo de Toast defensivo si el usuario intenta seleccionar una 4ª variedad sin antes desmarcar alguna.
   - **Dock Flotante Inferior (`#compare-floating-dock`):** Diseñado con estética nativa *Dark Glassmorphism* (fondo `#060b09f0`, blur 28px, bordes esmeralda). Contiene contador dinámico, miniaturas circulares HD con botón individual para remover, botón de vaciado rápido "🗑️ Limpiar" y botón de lanzamiento directo "⚖️ Comparar Cara a Cara (N/3)". Adaptado para dispositivos móviles (≤540px).
   - **Modal Cara a Cara en Columnas Paralelas (`#compare-modal`):**
     * Fotografía botánica macro HD con zoom lightbox interactivo y banco criador.
     * Barras visuales calibradas con precisión milimétrica: THC (escala 0-35%) y CBD (escala 0-20%).
     * Indicador visual de proporción genética Índica / Sativa.
     * Tiempo de floración (semanas y días) junto con cálculo automático de dificultad (Baja / Media / Alta) mediante badges cromáticos.
     * Perfil organoléptico: Terpeno principal con cromatografía oficial (`TERPENES_INFO`), terpenos secundarios, aromas, descriptores de sabor y linaje botánico/genético completo.
   - **Build y Versión:** Bundle recompilado vía `python scripts/build_bundle.py` (608,331 bytes) y versión sincronizada en `index.html` a `?v=2026_compare_v127` en CSS y JS.

2. ✅ **Optimización Mobile Responsive del Modal de Ficha Técnica (16:45):**
   - **Solapamiento superior resuelto:** Botón de cierre (✕) reubicado a `top: 10px; right: 10px; z-index: 60` en esfera dark glass de 34×34 px y badge "🔍 Toca para ver foto HD" a `top: 10px; left: 10px` con margen de seguridad, evitando colisión con títulos o badges.
   - **Eliminación de truncamientos en métricas (2 cols):** Padding ajustado a `8px 10px`, labels con `font-size: 0.70rem` flexible, valores a `1.15rem` y unidades `.pro-metric-unit` flexibles. Palabras como "CULTIVO OUTDOOR" y "1200 g/planta" se leen completas sin corte.
   - **Solapamiento inferior y scroll arreglado:** Incrementado el `padding-bottom` de `.pro-body-scrollable` a `110px !important` con `overscroll-behavior: contain` y `overflow-y: auto`, garantizando que el footer fijo "🚀 Generar Misión IA" nunca tape ningún dato al llegar al final.
   - **Ajuste de viewport en compactos (<400px):** `width: 95vw-96vw`, `height: 90vh`, `padding: 0 !important;` en el diálogo para que `.pro-spec-sheet` se ajuste con un borde verde esmeralda único y perfectamente alineado.

2. ✅ **Optimización WebP y Lazy Loading en Catálogo (16:30):**
   - Script `scripts/convert_to_webp.py` ejecutado para convertir 955 imágenes a WebP (calidad 85, resolución nativa 1:1).
   - Ahorro de 206.28 MB en disco y transferencia de red.
   - Respaldo preventivo creado en `js/data.js.bak_before_webp`.
   - Modificado el generador de tarjetas en `js/app.js` para aplicar `loading="lazy"` y `decoding="async"`.

2. ✅ **Módulo Comparador Interactivo "Cara a Cara" (16:35):**
   - **Botón Toggle en Tarjetas:** Añadido `⚖️ Comparar` a cada tarjeta con límite estricto de 3 variedades simultáneas y advertencia defensiva Toast.
   - **Dock Flotante (`#compare-floating-dock`):** Barra inferior animada en *Dark Glassmorphism* con contador, miniaturas interactivas de cepas seleccionadas, botón de eliminación individual, botón "⚖️ Comparar Ahora" y botón para vaciar selección.
   - **Modal de Comparación Paralela (`#compare-modal`):**
     * Barras visuales de cannabinoides (THC a escala 0-35%, CBD a escala 0-15%).
     * Proporción dual Índica / Sativa con desglose cromático y porcentual.
     * Semanas de floración y clasificación automática de dificultad de cultivo (Baja / Media / Alta) con badges de color.
     * Perfil de terpeno dominante con color oficial de `TERPENES_INFO`, terpenos secundarios y aromas.
     * Píldoras de efectos sensoriales destacados.
     * Linaje genético, procedencia botánica y botón de acceso a la ficha técnica completa.

3. ✅ **Build y Versionado (16:38):**
   - Recompilado `js/bundle.js` mediante `python scripts/build_bundle.py` (609,859 bytes).
   - Actualizado el tag de versión en `index.html` a `?v=2026_phase2_custom3_v125`.

4. ✅ **Eliminación Física de Disco y Reemplazo Botánico Real — Guanábana y Free White (12:15):**
   - **Archivos antiguos eliminados físicamente de `d:\cannaculture\img\`:**
     * `blimburn-guanabana-bud.jpg` (41 KB, fotografía errónea de fruto tropical) -> **ELIMINADO**.
     * `soma-free-white.jpg` (236 KB, fotografía errónea de flor de jazmín) -> **ELIMINADO**.
     * Confirmación vía script y HTTP: Ambos archivos devuelven 404 (eliminación física permanente).
   - **Nuevas fotografías botánicas reales guardadas:**
     * `img/blimburn-guanabana-bud-real.jpg` (800×800 px, 218 KB, macro de flor de Guanábana de *Blimburn Seeds*).
     * `img/free-white-bud-real.jpg` (800×800 px, 230 KB, macro de flor curada de *Alchimia*).
   - **Actualización de base de datos:** Modificados los IDs `blimburn-guanabana` y `soma-free-white` en `js/data.js`.
   - **Recompilación y Caché:** `js/bundle.js` recompilado exitosamente y versión incrementada a `?v=2026_phase2_custom3_v124` en `index.html`.
2. ✅ **Corrección Crítica de Fotografía Botánica — Free White (Soma Seeds) (12:05):**
   - **Problema detectado:** La entrada `soma-free-white` tenía asignada una imagen ajena al cannabis (flores de jardín / jazmín blanco).
   - **Solución botánica real (CERO IA):** Obtenida fotografía botánica macro real de alta resolución del cogollo maduro de la línea blanca curada (*White Widow*) desde Alchimia (`https://www.alchimiaweb.com/blog/wp-content/uploads/2022/12/White-Widow-Auto.png`, 1000×1200 px original).
   - **Normalización e Integración:** Procesada a formato 1:1 cuadrado (800×800 px, 230 KB) centrada en el ápice de la flor, con fondo de estudio oscuro puro (luminosidad de esquinas 0.0/255) y suave desvanecido del tallo inferior, cumpliendo al 100% con *Dark Glassmorphism*.
3. ✅ **Corrección Crítica de Fotografía Botánica — Guanábana (Blimburn Seeds) (11:15):**
   - **Problema detectado:** La fotografía previa correspondía erróneamente al fruto tropical de guanábana (*Annona muricata*) sobre fondo blanco.
   - **Solución botánica real (CERO IA):** Descargada fotografía botánica macro oficial del cogollo maduro de Guanábana desde el repositorio oficial del banco creador (*Blimburn Seeds*: `https://blimburnseeds.com/wp-content/uploads/2021/04/Guanabana.webp`).
   - **Normalización e Integración:** Procesada a formato 1:1 cuadrado (800×800 px, 218 KB) sobre lienzo de estudio oscuro (`#080a09` / degradado radial `#161c18`) con desvanecimiento suavizado del tallo inferior, garantizando compatibilidad 100% con *Dark Glassmorphism* (luminosidad de esquinas 9.3/255).
4. ✅ **Auditoría y Purga de Genéticas Duplicadas e Inconsistentes (10:35):**
   - Detección exhaustiva de duplicados mediante `scripts/clean_duplicates.py` por ID exacto y combinación normalizada de banco y variedad.
   - **Caso detectado y consolidado:** `Ripper Haze` (Ripper Seeds).
     * *Entrada conservada:* `ripper-ripper-haze` (Ficha oficial y completa: Selección élite Amnesia Haze, 24% THC, 65 días de floración, 1er premio Cannabis Champions Cup, 640 valoraciones).
     * *Entrada purgada:* `ripper-haze` (Entrada contradictoria redundante: 21% THC, 72 días de floración, descripción genérica).
   - Base de datos consolidada netamente de **403 a 402 variedades únicas**.
   - Verificación sintáctica integral: 0 comas huérfanas, 0 errores de balanceo de llaves en `js/data.js`.
5. ✅ **Resolución previa de las 4 excepciones pendientes (Fase 2 al 100%):**
   - Royal Gorilla, Eli, Bruce Banner #3 y Sensi Amnesia con fotografía macro botánica oficial en HD y fondos oscuros de estudio.
6. ✅ **Corrección visual previa de Tutankhamon, Goldmine y Wembley:**
   - Sustituidas imágenes erróneas por macro fotografía botánica HD con fondo oscuro de estudio.
7. ✅ **Corrección de `border-radius: 0` en inputs:**
   - Normalizado a `var(--radius-sm) !important` en `css/styles.css` e `index.html`.
8. ✅ **Optimización responsive en barra de navegación superior:**
   - Implementado `repeat(auto-fit, minmax(...))` con prevención de desbordamiento en resoluciones ≤1024px y ≤768px.

---

## 4. Tareas Pendientes
- Ninguna tarea pendiente inmediata. Fase 2 y correcciones críticas completadas al 100%.

---

## 5. Respaldos y Puntos de Restauración
- **Copia de seguridad de imágenes:** `d:\cannaculture\img_backup_20260903\` (948 archivos, 370.66 MB).
- **Copia de seguridad integral comprimida:** `C:\Backups\cannaculture_backup_20260903_0142.zip` (725.23 MB en disco `C:\`).

---

## 6. Regla de Mantenimiento
- Mantener este archivo actualizado tras la finalización de cada tarea para consulta rápida y referencia operativa inmediata.
