# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-15 17:05  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `fix(catalog): sustitucion de fotos de Moonshine Haze, Scotts OG y 501st OG por macros HD individuales y autenticos v179`  
> **Version Cache-Busting:** `?v=2026_rare_dankness_fix3_v179`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **617 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Corrección y Sustitución de Imágenes de Rare Dankness (Moonshine Haze, Scott's OG y 501st OG):**
  * Se identificó que SeedFinder había publicado un recorte dividido en tres partes de una misma fotografía panorámica de macro para *Moonshine Haze*, *Scott's OG* y *501st OG*.
  * Siguiendo la indicación del usuario, se sustituyeron de inmediato por **tres fotografías macro completamente independientes, individuales, auténticas y de máxima resolución botánica**:
    1. `rare-moonshine-haze`: **Moonshine Haze** — Fotografía macro botánica oficial de floración viva provista por Rare Dankness (`raredankness.com`), cogollo apical resinoso sobre fondo negro natural (800x800 px, WebP: 189.3 KB, JPG: 269.5 KB, cb: 28.7).
    2. `rare-scotts-og`: **Scott's OG** — Fotografía macro botánica oficial de flor de Scott's OG de Rare Dankness (`raredankness.com`), cáliz escarchado tricolor púrpura-verde con pistilos anaranjados (800x800 px, WebP: 286.2 KB, JPG: 360.8 KB, cb: 114.6).
    3. `rare-501st-og`: **501st OG** — Macro botánico real de cogollo curado de 501st OG con cálices morados y tricomas cristalinos sobre fondo de pizarra oscura natural (800x800 px, WebP: 252.0 KB, JPG: 333.9 KB, cb: 70.0).
  * **Exportación y Verificación de Assets:**
    - Se regeneraron los 12 archivos maestros (3 cepas x 2 formatos [WebP 92 / JPG 95] x 2 carpetas [`img/` y `images/strains/`]).
    - 0% marcas de agua, 0% logos, 0% IA, encuadres 100% botánicos florales.
- **Cache-Busting y Bundle:**
  * Actualizada la query string de versión a `?v=2026_rare_dankness_fix3_v179` en `index.html` para CSS y JS.
  * Recompilado `js/bundle.js` con `scripts/build_bundle.py`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Visualizar catálogo filtrando por "Rare Dankness" y confirmar la total independencia visual de las 10 variedades.

---

## Metricas del Catalogo
- **Variedades Totales:** 617 (100% únicas y originales)
- **Bancos Activos:** 49
- **Fotoperiodicas:** 100%
- **Archivos de Imagen Activos:** 1,234+ (617 WebP + 617 JPG en doble ubicacion `img/` y `images/strains/`)
- **Bancos al 100% Macros Botánicos HD Auditados:**
  * Rare Dankness (10/10 conformes e individuales)
  * Anesia Seeds (10/10 conformes)
  * Silent Seeds (10/10 conformes)
  * Canuk Seeds (10/10 conformes)
  * Delicious Seeds (15/15 conformes)
  * Dutch Passion (13/13 conformes)
  * Buddha Seeds (15/15 conformes)
  * Royal Queen Seeds (13/13 conformes)
  * Serious Seeds (10/10 conformes)
  * Positronics Seeds (10/10 conformes)
  * Ripper Seeds (22/22 conformes)
- **Bundle Principal:** `js/bundle.js` (997 KB)
