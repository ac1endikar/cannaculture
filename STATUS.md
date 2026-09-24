# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-24 14:25  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `fix(mobile): optimizacion completa del chat de Mateo para movil v189`  
> **Version Cache-Busting:** `?v=2026_mobile_mateo_v189`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **677 cepas botanicas 100% unicas y originales, 0 duplicados visuales.**
- **55 Bancos Oficiales Incorporados** (ultima adicion en v188: Dr. Underground + Crockett Family Farms)

### v189 — Mobile Mateo Optimization
- **Ventana flotante**: Ahora ocupa pantalla casi completa en mobile (88dvh/92dvh) y se expande desde abajo como un sheet nativo iOS/Android.
- **Swipe-down para cerrar**: Deslizar el header del chat hacia abajo cierra el panel.
- **Sin zoom iOS**: Inputs con `font-size: 16px` minimo — ya no hace zoom automatico al hacer tap en el campo de texto.
- **Targets tactiles 44x44px**: Todos los botones del chat (send, photo, close, TTS) tienen minimo 44x44px de area tocable.
- **Pills responsive**: En mobile (<=480px) hacen scroll horizontal en lugar de desbordarse.
- **FAB compacto**: En <=480px el boton flotante muestra solo el emoji, sin texto.
- **Body scroll bloqueado**: Mientras el chat esta abierto en mobile, el body no se desplaza.
- **dvh units**: Usa `100dvh` (dynamic viewport height) para ajustarse al teclado virtual en iOS/Android.
- **Reasoning box adaptado**: Se ajusta al ancho del movil sin desbordamiento.
- **Sin auto-focus en mobile**: El input no recibe focus al abrir el chat (evita que el teclado virtual suba de forma inesperada).

---

## Metricas del Catalogo
- **Variedades Totales:** 677 (100% unicas)
- **Bancos Activos:** 55
- **Duplicados Visuales (pHash 256-bit):** 0
- **Fondos Blancos:** 0 (todos corregidos)
- **Fotoperiodicas:** 100%
- **Cobertura Linaje/Genetica:** 100%

---

## Historial de Versiones Recientes
### v188 — Dr. Underground + Crockett Family Farms (20 cepas HD)
- **55 Bancos Oficiales Incorporados**, ultimos agregados en v188:
  * **Dr. Underground (10 cepas de élite):**
    1. `drug-king-kong`: **King Kong** (75% Índica / 25% Sativa, Ed Rosenthal Super Bud x Chronic).
    2. `drug-melon-gum`: **Melon Gum** (60% Índica / 40% Sativa, Bubblegum x Lavender).
    3. `drug-crystal-meth`: **Crystal M.E.T.H.** (80% Sativa / 20% Índica, Destroyer x Critical Mass).
    4. `drug-painkiller`: **Painkiller** (75% Índica / 25% Sativa, Sensi Star x White Russian - Alto CBD).
    5. `drug-brooklyn-mango`: **Brooklyn Mango** (50% Híbrida, Brooklyn Mango Clone x NYC Diesel).
    6. `drug-kong-47`: **Kong 47** (60% Índica / 40% Sativa, King Kong x AK-47).
    7. `drug-black-jesus-og`: **Black Jesus OG** (85% Índica / 15% Sativa, Tahoe OG x Soul Star).
    8. `drug-u-pink-kush`: **U-Pink Kush** (80% Índica / 20% Sativa, Underground Pink Kush).
    9. `drug-soul-star`: **Soul Star** (75% Índica / 25% Sativa, Sensi Star x Peyote Purple).
    10. `drug-american-beauty`: **American Beauty** (55% Índica / 45% Sativa, Plushberry x King Kong).

  * **Crockett Family Farms (10 cepas de élite):**
    1. `cff-sour-tangie`: **Sour Tangie** (80% Sativa / 20% Índica, East Coast Sour Diesel x Tangie).
    2. `cff-clementine`: **Clementine** (70% Sativa / 30% Índica, Tangie x Lemon Skunk).
    3. `cff-banana-split`: **Banana Split** (60% Índica / 40% Sativa, Tangie x Banana Sherbet).
    4. `cff-citrus-sap`: **Citrus Sap** (50% Híbrida, GG4 x Tangie).
    5. `cff-crocketts-dawg`: **Crockett's Dawg** (60% Índica / 40% Sativa, Guava Dawg x Family Secret).
    6. `cff-strawberry-clem`: **Strawberry Clem** (50% Híbrida, Strawberry Banana x Clementine).
    7. `cff-strawberry-lemon-banana`: **Strawberry Lemon Banana** (55% Índica / 45% Sativa, Strawberry Banana x Lemon Skunk).
    8. `cff-tangie-jack`: **Tangie Jack** (80% Sativa / 20% Índica, Jack Herer x Tangie).
    9. `cff-banana-spritz`: **Banana Spritz** (65% Índica / 35% Sativa, Banana Sherbet x Spritzer).
    10. `cff-malawi-moonshine`: **Malawi Moonshine** (85% Sativa / 15% Índica, Malawi Sativa x Moonshine Haze).

- **Fotografias Botanicas Oficiales HD (v188):** 20 imagenes reales de cogollos en alta resolucion nativa (hasta 2048x2048), procesadas a 800x800 con el pipeline oscuro radial CannaCulture (WebP + JPG). Nitidez cristalina, sin pixelado, sin fondos blancos.
- **Auditoria Exhaustiva de Todo el Catalogo (677 imagenes):**
  * Metodo: pHash 256 bits (16x16) con umbral Hamming <= 4.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 677/677 cepas (100%).
- **Arquitectura Dual del Sommelier (Ollama local + Gemini Cloud 24/7).**


