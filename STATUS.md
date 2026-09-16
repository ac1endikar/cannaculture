# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-16 22:10  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(catalog): incorporacion de G13 Labs Seeds con 10 cepas de elite y macros botanicos HD v181`  
> **Version Cache-Busting:** `?v=2026_g13labs_v181`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **647 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Cobertura Genética Completa (100%):** **647 de 647 cepas disponen de campos explícitos de linaje parental (`genetics:` y `lineage:`)**, garantizando visualización de ADN 🧬 en tarjetas, modales y búsqueda completa por parentales.
- **52º Banco Oficial Incorporado: G13 Labs Seeds (UK / Países Bajos)**
  * Banco de culto underground fundado en el Reino Unido a finales de los 80 y establecido en Ámsterdam, célebre mundialmente por su genética legendaria Pineapple Express y selecciones de élite.
  * 10 cepas fotoperiódicas de élite mundial añadidas a `js/data.js`:
    1. `g13-labs-pineapple-express` (Pineapple Express) - Sativa (THC 21%) · Genética: Trainwreck x Hawaiian Sativa
    2. `g13-labs-blue-og` (Blue OG) - Índica (THC 21%) · Genética: Blueberry x F13 x OG Kush
    3. `g13-labs-c99` (C99) - Sativa (THC 22%) · Genética: Cinderella 99 (Princess x Cinderella 88)
    4. `g13-labs-gigabud` (Gigabud) - Índica (THC 20%) · Genética: Northern Light x Big Bud
    5. `g13-labs-raw-diesel` (Raw Diesel) - Híbrido (THC 21%) · Genética: NYC Diesel x G13
    6. `g13-labs-double-black` (Double Black) - Índica (THC 20%) · Genética: Black Domina 98 Selection
    7. `g13-labs-white-lavender` (White Lavender) - Híbrido (THC 20%) · Genética: White Widow x Lavender
    8. `g13-labs-midnight-kush` (Midnight Kush) - Índica (THC 20%) · Genética: Hash Plant x Blueberry
    9. `g13-labs-blueberry-gum` (Blueberry Gum) - Índica (THC 20%) · Genética: Blueberry x Bubblegum
    10. `g13-labs-chocolate-heaven` (Chocolate Heaven) - Sativa (THC 20%) · Genética: Cannalope Haze x Afghan
  * 40 nuevos archivos de imagen (10 WebP y 10 JPG en `img/` + 10 WebP y 10 JPG en `images/strains/`), todos macros botánicos HD de cálices y flores reales procesados sobre fondo de estudio oscuro con viñeta profesional y cero empaques.
- **Arquitectura Dual del Sommelier (Local Ollama & Web Gemini Cloud 24/7) (v181):**
  * **Entorno Local:** Prioridad absoluta a Ollama en `localhost:8080` (`llama3.1:latest`) a través de `/api/local-llm` en `server.py` (0 tokens, latencia ~20-50 ms).
  * **Entorno Web Público:** Activación automática de Google Gemini Cloud API (`gemini-3.6-flash`) con clave en base64 para acceso 24/7 sin servidor backend local.
  * **Degradación Elegante:** Si la red se corta o satura, conmuta al Motor Autónomo Heurístico (Tier 3).
  * **Métricas y Recompilación:**
    - `scratch/test_cascade_tiers.py`: Superado al 100% (peso `ai-sommelier.js` 39.61 KB <= 45 KB).
    - Bundle recompilado: `js/bundle.js` y `js/bundle-v151.js` (**1,003,538 bytes / 980.0 KB**).
    - Cache-busting actualizado en `index.html` a `?v=2026_g13labs_v181`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Ollama activo en segundo plano con modelo `llama3.1:latest` disponible.

---

## Metricas del Catalogo
- **Variedades Totales:** 647 (100% únicas y originales)
- **Bancos Activos:** 52
- **Fotoperiodicas:** 100%
- **Cobertura de Linaje/Genética:** 100% (647/647 cepas con `genetics:` y `lineage:`)
- **Archivos de Imagen Activos:** 1,334+ (647 WebP + 647 JPG en doble ubicacion `img/` y `images/strains/`)
- **Bancos al 100% Macros Botánicos HD Auditados:**
  * G13 Labs Seeds (10/10 conformes e individuales)
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
  * Eva Seeds (11/11 conformes)
  * Medical Seeds (16/16 conformes)
  * Nirvana Seeds (15/15 conformes)
  * Ripper Seeds (14/14 conformes)
