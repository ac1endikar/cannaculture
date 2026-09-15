# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-15 20:35  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(ai): calibracion de hiperparametros de muestreo y prosa conversacional de Mateo v173`  
> **Version Cache-Busting:** `?v=2026_mateo_human_calibration_v173`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **617 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Calibración Conversacional Humana y Soporte Multimodelo de Mateo (v173):**
  * **Hiperparámetros de Muestreo Calibrados (`server.py`):**
    - `temperature`: `0.78` (mayor fluidez, soltura y naturalidad conversacional).
    - `top_p`: `0.9` (enriquecimiento de vocabulario y profundidad estilística).
    - `presence_penalty`: `0.6` (prevención activa de bucles y frases predecibles).
    - `frequency_penalty`: `0.4` (variedad léxica continuada).
  * **Detección Dinámica de Modelo en Ollama (`server.py`):**
    - Consulta dinámica a `http://127.0.0.1:11434/api/tags`.
    - Priorización automática de `qwen2.5:7b` si se encuentra instalado; selección de `llama3.1:latest` en su defecto.
  * **Reescritura del System Prompt de Mateo (`js/ai-sommelier.js` y `server.py`):**
    - Sustituido por la directiva de colega culto, botánico y sommelier de criterio propio.
    - Prohibición estricta de tono de asistente virtual, teleoperador o manual de ayuda.
    - Eliminadas las listas mecánicas con viñetas interminables en favor de párrafos conversacionales orgánicos.
    - Registro de turnos de usuario en el historial multi-turno de `AISommelierAgent`.
  * **Métricas y Recompilación:**
    - `js/ai-sommelier.js` se mantiene optimizado en **35.58 KB** (36,429 bytes, dentro del límite estricto de <= 45 KB).
    - Recompilación exitosa de `js/bundle.js` y `js/bundle-v151.js` (**954.5 KB**).
    - Cache-busting sincronizado en `index.html` a `?v=2026_mateo_human_calibration_v173`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Conversar con Mateo probando tanto el modelo local Ollama como el motor autónomo.

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
