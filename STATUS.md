# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-15 18:15  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(ai): motor sommelier hibrido 0 tokens, proxy local y blindaje legal v172`  
> **Version Cache-Busting:** `?v=2026_zero_token_hybrid_v172`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **617 cepas botánicas 100% únicas y originales, sin duplicados ni imágenes clonadas.**
- **Despliegue del Sommelier Híbrido Universal 0-Tokens con Control de Arquitectura (v172):**
  * **Núcleo Zero-Token Cascade (`js/ai-sommelier.js`):**
    - **Tier 1 (Gemini Nano On-Device):** Detección automática en Chrome Built-in AI (`window.ai?.languageModel`) con validación de disponibilidad (`capabilities().available === 'readily'`) y System Prompt erudito y reflexivo de Mateo.
    - **Tier 2 (LLM Local vía Proxy en `server.py`):** Conexión no bloqueante a través de `/api/local-llm` hacia Ollama (`127.0.0.1:11434`) o LM Studio (`127.0.0.1:1234`) con sondeo concurrente multihilo y timeout estricto <= 150 ms para no congelar la UI.
    - **Tier 3 (Motor Autónomo Temático JS):** Modo offline inmediato para GitHub Pages estructurado por atmósferas sensoriales y estados de ánimo (Foco Creativo, Reflexión Filosófica y Cósmica, Desconexión Vespertina, Gastronomía y Sobremesa, Arte/Cinefilia, y Ciencia Botánica pura). Capacidad de responder elocuentemente sobre cualquier tema de conversación sin errores robóticos ni evasivas.
    - **Restricción Estricta de Peso Cumplida:** `js/ai-sommelier.js` optimizado a **35.03 KB** (35,868 bytes), cumpliendo holgadamente el límite de <= 45 KB.
    - **Guardián 0-Tokens:** Llamadas a APIs externas de pago totalmente desactivadas por defecto.
- **Proxy en `server.py` (`/api/local-llm`):**
  * Manejador GET/POST integrado con cabeceras CORS y sondeo paralelo con `concurrent.futures` hacia los puertos 11434 y 1234.
- **UI & Blindaje Legal (`index.html` y `styles.css`):**
  * **Header del Chat:** Añadido badge interactivo glassmorphic `⚡ Modo Ilimitado (0 Tokens)` que refleja la fuente activa en tiempo real: `[Gemini Nano 🧠]`, `[LLM Local 💻]` o `[Motor Autónomo 🍃]`.
  * **Aviso Legal (Footer):** Confirmada la 4ª tarjeta del grid de aviso legal con la cláusula de "Propiedad Intelectual & Enlaces" y canal directo de atención: `contacto.cannacatalog@gmail.com`.
- **Métricas y Recompilación:**
  * Bundle principal recompilado: `js/bundle.js` (**953.9 KB**, reducción de 43.6 KB).
  * Cache-busting actualizado en `index.html` a `?v=2026_zero_token_hybrid_v172`.
- **Acciones para Iniciar Siguiente Sesion:**
  1. Ejecutar `git pull origin main` (Protocolo AGENTS.md).
  2. Servidor local activo en `http://localhost:8080`.
  3. Interactuar con el Sommelier IA conversando sobre cualquier tema libre o explorando el catálogo.

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
