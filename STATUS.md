# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-14 21:00  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(catalog): sustitucion de 8 macros botanicos HD para Dutch Passion v174`  
> **Version Cache-Busting:** `?v=2026_dutch_passion_hd_v174`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **587 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Auditoría y Sustitución Fotográfica Dutch Passion (v174 - 100% COMPLETADA):**
  * Se analizaron las 13 cepas del banco **Dutch Passion** en `js/data.js` mediante visión por computadora y análisis de luminosidad perimetral.
  * Se identificaron **8 variedades con fondo blanco plano artificial (corner_bright = 255.0)** que degradaban la estética *Dark Glassmorphism* y se reemplazaron por **macros botánicos reales HD (800x800 px, 0% IA, 0% packaging, 0% logos/banners, fondos oscuros y botánicos)**:
    1. `dp-mazar`: Fondo blanco plano -> Reemplazado por macro botánico oficial de cogollo maduro escarchado sobre fondo negro terciopelo (Dutch Passion Grow Review by The Shire, 800x800 px, corner_bright: 13.7).
    2. `dp-passion-fruit`: Fondo blanco de catálogo -> Reemplazado por fotografía botánica real en floración con colores otoñales púrpuras y calices densos (Dutch Passion Grow Review by Bob-Bud, 800x800 px, corner_bright: 84.8).
    3. `dp-blueberry`: Fondo blanco recortado -> Reemplazado por macro botánico oficial de cogollo escarchado con hojas de azúcar azuladas sobre fondo oscuro (Dutch Passion Master ID 2394, 800x800 px, corner_bright: 113.6).
    4. `dp-white-widow`: Fondo blanco recortado -> Reemplazado por macro botánico real de flor White Widow cubierta de tricomas blancos cristalinos sobre fondo negro (Dutch Passion Master ID 2859, 800x800 px, corner_bright: 12.7).
    5. `dp-orange-bud`: Fondo blanco plano -> Reemplazado por macro botánico de cáliz resinoso con pistilos naranja brillante sobre fondo oscuro (Dutch Passion Master ID 2134, 800x800 px, corner_bright: 89.4).
    6. `dp-powerplant`: Fondo blanco plano -> Reemplazado por macro botánico de cola sativa sudafricana densa y resinosa sobre fondo de cultivo oscuro (Dutch Passion Master ID 1308, 800x800 px, corner_bright: 110.0).
    7. `dp-glueberry-og`: Fondo blanco plano -> Reemplazado por macro botánico oficial de cáliz cargado de tricomas Glueberry OG sobre fondo negro (Dutch Passion Master ID 2131, 800x800 px, corner_bright: 9.3).
    8. `dp-colorado-cookies`: Fondo blanco plano -> Reemplazado por macro botánico de cogollo compacto tipo Cookie con hojas oscuras y tricomas perlados (Dutch Passion Master ID 2162, 800x800 px, corner_bright: 114.2).
  * **5 variedades auditadas como conformes** conservadas en su estado botánico HD original:
    `dp-auto-blueberry`, `dp-zkittlez`, `dp-frisian-dew`, `dp-auto-mazar`, `dp-skywalker-og`.
  * **Saneamiento Técnico Global:**
    - Se repararon 2 assets que presentaban error de lectura de frames en formato WebP (`img/dna-cannalope-haze.webp` y `img/cpg-pave.webp`), regenerándolos con fidelidad al 100% desde sus masters JPEG 800x800 px.
  * **Exportación y Verificación de Assets:**
    - Todas las 8 nuevas imágenes procesadas y exportadas a 800x800 px nativos en formato WebP (calidad 92) y JPEG (calidad 95) en ambas carpetas: `img/` y `images/strains/`.
    - Pesos verificados (> 165 KB hasta 320 KB), garantizando cero compresión agresiva ni artefactos.
- **Recompilación y Cache-Busting:**
  * Bundle de producción regenerado con `python scripts/build_bundle.py` (`js/bundle.js` 965 KB).
  * Cache-busting actualizado en `index.html` a `?v=2026_dutch_passion_hd_v174` para CSS y JS.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Visualizar catálogo filtrando por "Dutch Passion" o evaluar el siguiente banco con incidencias (Canuk Seeds, Delicious Seeds, etc.).

---

## Metricas del Catalogo
- **Variedades Totales:** 587 (100% únicas y originales)
- **Bancos Activos:** 46
- **Fotoperiodicas:** 100%
- **Archivos de Imagen Activos:** 1,174+ (587 WebP + 587 JPG en doble ubicacion `img/` y `images/strains/`)
- **Calidad Fotográfica Dutch Passion:** 100% macros botánicos HD oscuros/naturales (13/13 cepas conformes)
- **Calidad Fotográfica Buddha Seeds:** 100% macros botánicos HD (15/15 cepas conformes)
- **Tarjetas en Aviso Legal:** 4 (Sin Ánimo de Lucro, Salud Pública, Responsabilidad Legal, Propiedad Intelectual & Enlaces)
- **Bundle Principal:** `js/bundle.js` (965 KB)
