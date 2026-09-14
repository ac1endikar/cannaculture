# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-14 11:58  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.ps1` o `server.py`)  
> **Commit de cierre:** `fix(catalog): depurar 13 duplicados redundantes preservando 587 cepas originales v172`  
> **Version Cache-Busting:** `?v=2026_dedup_original_v172`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **587 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Depuración de Duplicados (v172 - 100% COMPLETADA):**
  * Se realizó auditoría exhaustiva en la base de datos detectando 13 entradas duplicadas redundantes y clones de imagen:
    1. `dp-mazar-afghan` y `dp-mazar-ii` (clones redundantes de la original `dp-mazar` de Dutch Passion).
    2. `hso-trainwreck-b` (clon con misma foto de la original `hso-trainwreck` de Humboldt Seed).
    3. `hso-blue-dream-b` (clon con misma foto de la original `hso-blue-dream` de Humboldt Seed).
    4. Duplicados Barney's Farm: `bf-runtz-muffin`, `bf-critical-kush`, `bf-wedding-cake`, `bf-lsd`, `bf-pineapple-chunk` (se conservaron las versiones canónicas `barneys-` con mejores fichas y reseñas).
    5. Duplicados Sweet Seeds: `gorilla-girl` y `black-jack` (se conservaron las versiones canónicas `sweet-gorilla-girl` y `sweet-black-jack`).
    6. Falsos clones entre bancos: `hso-liberty-haze` (copia de Barney's Farm) y `philo-sugar-black-rose` (copia de Delicious Seeds).
  * Resultado tras saneamiento: 0 imágenes duplicadas, 0 cepas duplicadas dentro del mismo banco, balance de sintaxis JS perfecto (`brace: 0, bracket: 0`).
- **Verificación en Navegador Headless (DOM Real):**
  * Tarjetas `.strain-card` renderizadas en el DOM: **587**.
  * Contador dinámico: `'Mostrando 587 cepa(s)'`.
  * Ausencia total de los 13 duplicados verificada.
  * Presencia de las versiones originales y canónicas verificada.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Levantar servidor local con `powershell -ExecutionPolicy Bypass -File server.ps1`.
  3. Visualizar catálogo en `http://localhost:8080`.

---

## Metricas del Catalogo
- **Variedades Totales:** 587 (100% únicas y originales)
- **Bancos Activos:** 46
- **Fotoperiodicas:** 100%
- **Archivos de Imagen Activos:** 1,174+ (587 WebP + 587 JPG en doble ubicacion `img/` y `images/strains/`)
- **Tarjetas en Aviso Legal:** 4 (Sin Ánimo de Lucro, Salud Pública, Responsabilidad Legal, Propiedad Intelectual & Enlaces)
- **Bundle Principal:** `js/bundle.js` (965 KB)
