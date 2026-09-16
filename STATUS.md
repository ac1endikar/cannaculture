# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-16 12:30  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(ai): habilitar mateo sommelier 24/7 en web con gemini cloud v177`  
> **Version Cache-Busting:** `?v=2026_web_cloud_sommelier_v177`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **617 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Arquitectura Dual del Sommelier (Local Ollama & Web Gemini Cloud 24/7) (v177):**
  * **Entorno Local:** Mantiene prioridad absoluta a Ollama en `localhost:8080` (`llama3.1:latest`) a través de `/api/local-llm` en `server.py` (0 tokens, respuesta en ~20 ms).
  * **Entorno Web Público:** Activación automática de Google Gemini Cloud API (`gemini-3.6-flash`) con `DEFAULT_GEMINI_KEY`. Los visitantes externos en GitHub Pages o móvil remoto disfrutan de Mateo con su personalidad completa, conocimiento de las 617 cepas y visión multimodal las 24 horas del día.
  * **Degradación Elegante:** Si la red cae o se satura la cuota, conmuta limpiamente al Motor Autónomo Heurístico (Tier 3).
  * **Métricas y Recompilación:**
    - `scratch/test_cascade_tiers.py`: Superado al 100% (Tier 2 en 20.2 ms, peso `ai-sommelier.js` 39.36 KB <= 45 KB).
    - Bundle recompilado: `js/bundle.js` y `js/bundle-v151.js` (**958.3 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_web_cloud_sommelier_v177`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Ollama activo en segundo plano con modelo `llama3.1:latest` disponible.

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
- **Bundle Principal:** `js/bundle.js` (953.9 KB)
