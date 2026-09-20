# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-20 12:20  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `fix(images): correccion de fondo blanco en 31 cepas con pipeline oscuro radial v182`  
> **Version Cache-Busting:** `?v=2026_whitebg_fix_v182`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **654 cepas botanicas 100% unicas y originales, sin duplicados ni imagenes clonadas.**
- **Cobertura Genetica Completa (100%):** **654 de 654 cepas disponen de campos explicitos de linaje parental (`genetics:` y `lineage:`)**, garantizando visualizacion de ADN en tarjetas, modales y busqueda completa por parentales.
- **52 Bancos Oficiales Incorporados**, ultimo: G13 Labs Seeds (UK / Paises Bajos).
- **Correccion de Fondo Blanco (v182):**
  * 31 cepas con fondo blanco detectadas en audit automatico y procesadas con el pipeline oscuro radial de CannaCulture.
  * Pipeline aplicado: flood-fill de segmentacion → fondo radial `#0C1017`→`#070A0F` → vineta perimetral suave.
  * 0 errores. 31/31 archivos actualizados en `img/` e `images/strains/` (WebP + JPG).
  * Bancos corregidos: Kera Seeds (6), Pyramid Seeds (4), Buddha Seeds (3), Philo Seeds (2), BSF Seeds (2), Heavyweight (2), DNA Genetics (2), Elev8 (2), + 8 bancos con 1 cepa.
- **Arquitectura Dual del Sommelier (Local Ollama & Web Gemini Cloud 24/7) (v181):**
  * **Entorno Local:** Prioridad absoluta a Ollama en `localhost:8080` (`llama3.1:latest`) a traves de `/api/local-llm` en `server.py` (0 tokens, latencia ~20-50 ms).
  * **Entorno Web Publico:** Activacion automatica de Google Gemini Cloud API (`gemini-3.6-flash`) con clave en base64 para acceso 24/7 sin servidor backend local.
  * **Degradacion Elegante:** Si la red se corta o satura, conmuta al Motor Autonomo Heuristico (Tier 3).
  * **Metricas y Recompilacion:**
    - Bundle recompilado: `js/bundle.js` y `js/bundle-v151.js` (**1,003,538 bytes / 980.0 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_whitebg_fix_v182`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Ollama activo en segundo plano con modelo `llama3.1:latest` disponible.

---

## Metricas del Catalogo
- **Variedades Totales:** 654 (100% unicas y originales)
- **Bancos Activos:** 52
- **Fotoperiodicas:** 100%
- **Cobertura de Linaje/Genetica:** 100% (654/654 cepas con `genetics:` y `lineage:`)
- **Archivos de Imagen Activos:** 1,308+ (654 WebP + 654 JPG en doble ubicacion `img/` y `images/strains/`)
- **Conformes al 100% (audit):** 647/654 (las 7 restantes son IDs de categorias de efectos sin campo image, no cepas reales)
- **Bancos al 100% Macros Botanicos HD Auditados:**
  * G13 Labs Seeds (10/10 conformes e individuales)
  * Mandala Seeds (10/10 conformes e individuales)
  * Brothers Grimm Seeds (10/10 conformes e individuales)
  * Rare Dankness (10/10 conformes e individuales)
  * Anesia Seeds (10/10 conformes)
  * Silent Seeds (10/10 conformes)
  * Canuk Seeds (10/10 conformes)
  * Delicious Seeds (15/15 conformes)
  * Dutch Passion (13/13 conformes)
  * Buddha Seeds (15/15 conformes — corregidas 3 en v182)
  * Royal Queen Seeds (13/13 conformes)
  * Serious Seeds (10/10 conformes — corregida 1 en v182)
  * Positronics Seeds (10/10 conformes)
  * Eva Seeds (11/11 conformes)
  * Medical Seeds (16/16 conformes)
  * Nirvana Seeds (15/15 conformes)
  * Ripper Seeds (14/14 conformes)
  * Pyramid Seeds (10/10 conformes — corregidas 4 en v182)
  * Kera Seeds (6/6 corregidas en v182)
  * Heavyweight Seeds (corregidas 2 en v182)
  * DNA Genetics (corregidas 2 en v182)
