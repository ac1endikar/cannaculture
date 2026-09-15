# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-15 20:58  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `fix(server): resolver error 405 admitiendo GET y OPTIONS en /api/local-llm v175`  
> **Version Cache-Busting:** `?v=2026_fix_405_endpoint_v175`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **617 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Soporte Completo a GET, POST y OPTIONS con CORS en `/api/local-llm` (v175):**
  * **Corrección de Error 405 en `server.py`:**
    - Soporte explícito en `do_GET` para `/api/local-llm` ejecutando `check_local_llm()` y respondiendo `200 OK` con JSON de disponibilidad.
    - Soporte explícito en `do_OPTIONS` para preflight CORS con `Content-Length: 0` y código `200 OK`.
    - Cabeceras CORS completas en `end_headers`: `Access-Control-Allow-Origin: *`, `Access-Control-Allow-Methods: GET, POST, OPTIONS`, `Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With`.
    - Coincidencia flexible de rutas (soporte para sub-rutas y query params).
  * **Blindaje en `js/ai-sommelier.js`:**
    - Incorporado `getLocalApiUrl()` que detecta si la página se sirve desde Live Server (ej. puerto 5500) o puerto 8080, reencaminando peticiones a `http://localhost:8080/api/local-llm` si recibe un 405.
  * **Verificación Automatizada:**
    - Pruebas en Python de peticiones GET, OPTIONS y POST a `/api/local-llm`: las 3 devuelven 200 OK sin excepciones.
  * **Métricas y Recompilación:**
    - Recompilación exitosa de `js/bundle.js` y `js/bundle-v151.js` (**955.3 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_fix_405_endpoint_v175`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Probar el chat de Mateo tanto en `http://localhost:8080` como en cualquier otro puerto local.

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
