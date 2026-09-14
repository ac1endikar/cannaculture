# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-14 13:25  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.ps1` o `server.py`)  
> **Commit de cierre:** `feat(catalog): sustitucion de 8 macros botanicos HD para Buddha Seeds v173`  
> **Version Cache-Busting:** `?v=2026_buddha_macros_hd_v173`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **587 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Auditoría y Sustitución Fotográfica Buddha Seeds (v173 - 100% COMPLETADA):**
  * Se analizaron las 15 cepas del banco **Buddha Seeds** en `js/data.js` mediante visión por computadora y análisis métrico.
  * Se identificaron **8 variedades con defectos de calidad** (artefactos corruptos, packaging o ilustraciones vectoriales/cartoons) y se reemplazaron por **macros botánicos reales HD (800x800 px, 0% IA, 0% packaging, 0% logos/banners)**:
    1. `buddha-deimos`: Corrupción/glitch estático en el tercio inferior -> Reemplazado por macro botánico oficial de flor central (CannaConnection Master 800x800).
    2. `buddha-purple-kush`: Ruido digital severo y sobreexposición -> Reemplazado por macro botánico HD de calices y tricomas púrpuras (CannaConnection Master 800x800).
    3. `buddha-white-dwarf`: Caja de semillas/packaging cubriendo la planta -> Reemplazado por fotografía botánica limpia de cogollo maduro con 0% packaging (CannaConnection Master 800x800).
    4. `buddha-gorila`: Dibujo animado/cartoon de King Kong -> Reemplazado por fotografía botánica real de cogollo central masivo sobre fondo negro uniforme.
    5. `buddha-gelato`: Ilustración de copa de helado con artefactos -> Reemplazada por macro botánico real de cogollo con hojas de azúcar púrpuras sobre fondo negro.
    6. `buddha-cookie`: Dibujo cartoon de galletas -> Reemplazado por macro botánico real de cola escarchada con tricomas blancos sobre fondo negro.
    7. `buddha-dosi2`: Emblema gráfico vectorial -> Reemplazado por macro botánico real de cogollo con pistilos anaranjados sobre fondo negro.
    8. `buddha-wedding-cheesecake`: Emblema gráfico vectorial -> Reemplazado por fotografía botánica real de flor central densa y resinosa sobre fondo negro.
  * **7 variedades auditadas como conformes** conservadas en su estado botánico HD original:
    `buddha-magnum`, `buddha-syrup`, `buddha-med-gom`, `buddha-big-buddha-cheese`, `buddha-medikit`, `buddha-kabrales`, `buddha-tokay-haze`.
  * **Exportación y Verificación de Assets:**
    - Todas las 8 nuevas imágenes procesadas y exportadas a 800x800 px en formato WebP (calidad 92) y JPEG (calidad 95) en ambas carpetas: `img/` y `images/strains/`.
    - Pesos de archivo verificados (> 70 KB hasta 241 KB), sin thumbnails corruptos ni degradación.
- **Recompilación y Cache-Busting:**
  * Bundle de producción regenerado con `python scripts/build_bundle.py` (`js/bundle.js` 965 KB).
  * Cache-busting actualizado en `index.html` a `?v=2026_buddha_macros_hd_v173` para CSS y JS.
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
- **Calidad Fotográfica Buddha Seeds:** 100% macros botánicos HD (15/15 cepas conformes)
- **Tarjetas en Aviso Legal:** 4 (Sin Ánimo de Lucro, Salud Pública, Responsabilidad Legal, Propiedad Intelectual & Enlaces)
- **Bundle Principal:** `js/bundle.js` (965 KB)
