# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-16 18:15  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(catalog): incorporacion de Mandala Seeds con 10 cepas de elite y macros botanicos HD v179`  
> **Version Cache-Busting:** `?v=2026_mandala_seeds_v179`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **637 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **51º Banco Oficial Incorporado: Mandala Seeds (España / Alemania)**
  * Fundado en 2004 por Mike & Jasmin (biólogos y genetistas botánicos pioneros en cultivo orgánico y selección de landraces puras).
  * 10 cepas fotoperiódicas de élite mundial añadidas a `js/data.js`:
    1. `mandala-satori` (Satori) - Sativa (THC 25%, High Times Strain of the Year)
    2. `mandala-hashberry` (Hashberry) - Índica (THC 20%, High Times Top 10)
    3. `mandala-mandala-1` (Mandala #1) - Híbrida (THC 21%)
    4. `mandala-krystalica` (Krystalica) - Sativa (THC 23%)
    5. `mandala-8-miles-high` (8 Miles High) - Sativa (THC 22%)
    6. `mandala-kalichakra` (Kalichakra) - Sativa (THC 20%)
    7. `mandala-beyond-the-brain` (Beyond the Brain) - Sativa (THC 24%)
    8. `mandala-california-dream` (California Dream) - Híbrida (THC 21%)
    9. `mandala-speed-queen` (Speed Queen) - Índica (THC 19%)
    10. `mandala-purple-paro-valley` (Purple Paro Valley) - Sativa (THC 18%)
  * 40 nuevos archivos de imagen (10 WebP y 10 JPG en `img/` + 10 WebP y 10 JPG en `images/strains/`), todos macros botánicos HD de cálices y flores reales procesados sobre fondo de estudio oscuro con viñeta profesional y cero empaques.
- **Arquitectura Dual del Sommelier (Local Ollama & Web Gemini Cloud 24/7) (v179):**
  * **Entorno Local:** Prioridad absoluta a Ollama en `localhost:8080` (`llama3.1:latest`) a través de `/api/local-llm` en `server.py` (0 tokens, latencia ~20-50 ms).
  * **Entorno Web Público:** Activación automática de Google Gemini Cloud API (`gemini-3.6-flash`) con clave en base64 para acceso 24/7 sin servidor backend local.
  * **Degradación Elegante:** Si la red se corta o satura, conmuta al Motor Autónomo Heurístico (Tier 3).
  * **Métricas y Recompilación:**
    - `scratch/test_cascade_tiers.py`: Superado al 100% (peso `ai-sommelier.js` 39.61 KB <= 45 KB).
    - Bundle recompilado: `js/bundle.js` y `js/bundle-v151.js` (**983,225 bytes / 960.2 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_mandala_seeds_v179`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Ollama activo en segundo plano con modelo `llama3.1:latest` disponible.

---

## Metricas del Catalogo
- **Variedades Totales:** 637 (100% únicas y originales)
- **Bancos Activos:** 51
- **Fotoperiodicas:** 100%
- **Archivos de Imagen Activos:** 1,294+ (637 WebP + 637 JPG en doble ubicacion `img/` y `images/strains/`)
- **Bancos al 100% Macros Botánicos HD Auditados:**
  * Mandala Seeds (10/10 conformes e individuales)
  * Brothers Grimm Seeds (10/10 conformes e individuales)
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
- **Bundle Principal:** `js/bundle.js` (983,225 bytes)
