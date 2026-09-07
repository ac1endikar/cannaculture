# Protocolo Obligatorio de Sincronización con GitHub - CannaCulture

A partir de este momento, se aplican estrictamente estas dos reglas para cualquier sesión de trabajo:

## 1. FASE DE ARRANQUE (Al recibir cualquier nueva tarea / prompt)
- **Ejecutar antes de cualquier acción**: Antes de leer código en detalle, editar archivos o proponer cambios, ejecutar en terminal:
  ```bash
  git pull origin main
  ```
- **Verificación**: Comprobar que la rama local esté al día con `origin/main` para garantizar que siempre se trabaje sobre la última versión subida.

## 2. FASE DE CIERRE (Al indicar fin de sesión, cierre, o tras completar el objetivo)
- **Recompilación de Bundle**: Si se modificó código fuente en `js/`, ejecutar:
  ```bash
  python scripts/build_bundle.py
  ```
- **Cache-Busting**: Actualizar la query string de versión de cache-busting en `index.html` (CSS `styles.css?v=...` y JS `bundle.js?v=...`).
- **Bitácora de Estado**: Actualizar `STATUS.md` reflejando con exactitud los cambios realizados y la nueva versión.
- **Secuencia de Subida Git**:
  ```bash
  git add -A
  git commit -m "<tipo>(<alcance>): descripción concisa de lo trabajado"
  git push origin main
  ```
- **Confirmación**: Mostrar el hash del commit resultante y confirmar que `origin/main` ha quedado completamente actualizado.
