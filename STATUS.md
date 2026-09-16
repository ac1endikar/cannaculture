# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-16 14:45  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(catalog): incorporacion de Brothers Grimm Seeds con 10 cepas de elite y macros botanicos HD v178`  
> **Version Cache-Busting:** `?v=2026_brothers_grimm_seeds_v178`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **627 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **50º Banco Oficial Incorporado: Brothers Grimm Seeds (EE.UU. / Colorado)**
  * Creadores legendarios fundados por MrSoul (Rick Campanella) responsables de Cinderella 99, Rosetta Stone, Apollo 11.
  * 10 cepas fotoperiódicas de élite mundial añadidas a `js/data.js`:
    1. `bg-cinderella-99` (Cinderella 99) - Sativa (THC 22%)
    2. `bg-rosetta-stone` (Rosetta Stone) - Híbrida (THC 23%)
    3. `bg-apollo-11` (Apollo 11) - Sativa (THC 21%)
    4. `bg-killer-queen` (Killer Queen) - Híbrida (THC 24%)
    5. `bg-princess-haze` (Princess Haze) - Sativa (THC 23%)
    6. `bg-queen-of-soul` (Queen of Soul) - Sativa (THC 24%)
    7. `bg-grimm-glue` (Grimm Glue) - Híbrida (THC 28%)
    8. `bg-durban-thai-c99` (Durban Thai x C99) - Sativa (THC 22%)
    9. `bg-ocifer` (Ocifer) - Híbrida (THC 29%)
    10. `bg-genius-juice` (Genius Juice) - Sativa (THC 25%)
  * 40 nuevos archivos de imagen (10 WebP y 10 JPG en `img/` + 10 WebP y 10 JPG en `images/strains/`), todos macros botánicos HD de cálices y flores reales procesados sobre fondo de estudio oscuro con viñeta profesional y cero empaques.
- **Arquitectura Dual del Sommelier (Local Ollama & Web Gemini Cloud 24/7) (v178):**
  * **Entorno Local:** Prioridad absoluta a Ollama en `localhost:8080` (`llama3.1:latest`) a través de `/api/local-llm` en `server.py` (0 tokens, latencia ~20-50 ms).
  * **Entorno Web Público:** Activación automática de Google Gemini Cloud API (`gemini-3.6-flash`) con clave en base64 para acceso 24/7 sin servidor backend local.
  * **Degradación Elegante:** Si la red se corta o satura, conmuta al Motor Autónomo Heurístico (Tier 3).
  * **Métricas y Recompilación:**
    - `scratch/test_cascade_tiers.py`: Superado al 100% (peso `ai-sommelier.js` 39.61 KB <= 45 KB).
    - Bundle recompilado: `js/bundle.js` y `js/bundle-v151.js` (**971,053 bytes / 948.3 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_brothers_grimm_seeds_v178`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Ollama activo en segundo plano con modelo `llama3.1:latest` disponible.

---

## Metricas del Catalogo
- **Variedades Totales:** 627 (100% únicas y originales)
- **Bancos Activos:** 50
- **Fotoperiodicas:** 100%
- **Archivos de Imagen Activos:** 1,274+ (627 WebP + 627 JPG en doble ubicacion `img/` y `images/strains/`)
- **Bancos al 100% Macros Botánicos HD Auditados:**
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
- **Bundle Principal:** `js/bundle.js` (971,053 bytes)
