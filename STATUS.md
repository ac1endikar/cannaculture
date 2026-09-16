# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-16 11:40  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(server): optimizar latencia de sondeo LLM local con fast-path y cache v176`  
> **Version Cache-Busting:** `?v=2026_local_llm_fast_probe_v176`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **617 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Sondeo LLM Local Ultrarrápido & Resiliente (v176):**
  * **Optimización Fast-Path:** Sondeo secuencial priorizando Ollama (11434) de forma directa. Elimina por completo el retraso de timeout de LM Studio (1234), reduciendo la latencia de respuesta de ~1,050 ms a **~20 ms** (< 300 ms límite estricto).
  * **Caché en Memoria:** Cacheado de 5 segundos en `server.py` para respuestas instantáneas (< 1 ms) en peticiones recurrentes de la UI.
  * **Aumento de Timeout Inferencia:** Elevado a 90 segundos para permitir arranque en frío sin cortes durante la carga de modelos grandes en GPU/RAM.
  * **Verificación End-to-End Superada:** Mateo (`llama3.1:latest`) respondiendo fluidamente a consultas botánicas complejas en español, con tono cercano, cálido y sin plantillas fijas.
  * **Métricas y Recompilación:**
    - `scratch/test_cascade_tiers.py`: Superado al 100% (Tier 2 en 20.8 ms, peso `ai-sommelier.js` 36.35 KB <= 45 KB).
    - Bundle recompilado: `js/bundle.js` y `js/bundle-v151.js` (**955.3 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_local_llm_fast_probe_v176`.
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
