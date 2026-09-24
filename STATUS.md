# Estado Actual del Proyecto: CannaCatalog 2.0 ULTRA

> **Ultima actualizacion:** 2026-09-24 15:45  
> **Servidor local:** Activo en `http://localhost:8080` (ejecutado via `server.py`)  
> **Commit de cierre:** `feat(catalog): incorporacion de The Cali Connection y Cannarado Genetics con 20 cepas HD v191`  
> **Version Cache-Busting:** `?v=2026_cali_cannarado_v191`

---

## Punto de Reanudacion para la Siguiente Sesion
- **Estado del Catalogo:** **697 cepas botanicas 100% unicas y originales, 0 duplicados visuales.**
- **57 Bancos Oficiales Incorporados** (ultima adicion en v191: The Cali Connection + Cannarado Genetics)

### v191 — The Cali Connection & Cannarado Genetics (20 cepas HD)
- **The Cali Connection (10 cepas de culto californianas):**
  1. `cali-sfv-og-kush`: **SFV OG Kush** (90% Índica / 10% Sativa, San Fernando Valley OG x Afghani #1).
  2. `cali-tahoe-og-kush`: **Tahoe OG Kush** (80% Índica / 20% Sativa, Tahoe OG Clone x SFV OG Kush IBL).
  3. `cali-deadhead-og`: **Deadhead OG** (60% Sativa / 40% Índica, Chemdawg 91 Skunk VA x SFV OG Kush F4).
  4. `cali-alien-og`: **Alien OG** (50% Híbrida, Alien Kush x Tahoe OG Kush).
  5. `cali-blackwater`: **Blackwater** (85% Índica / 15% Sativa, Mendo Purps x SFV OG Kush F3).
  6. `cali-corleone-kush`: **Corleone Kush** (80% Índica / 20% Sativa, Pre-98 Bubba Kush x SFV OG Kush F4).
  7. `cali-jedi-kush`: **Jedi Kush** (70% Índica / 30% Sativa, Death Star x SFV OG Kush F5).
  8. `cali-larry-og-kush`: **Larry OG Kush** (70% Índica / 30% Sativa, Larry OG x SFV OG Kush IBL).
  9. `cali-grape-og`: **Grape OG** (60% Índica / 40% Sativa, Tahoe OG Kush x Grape Romulan).
  10. `cali-girl-scout-cookies`: **Girl Scout Cookies (Cali Connection)** (60% Índica / 40% Sativa, Forum Cut GSC x SFV OG Kush).

- **Cannarado Genetics (10 leyendas modernas de Colorado):**
  1. `cannarado-sundae-driver`: **Sundae Driver** (50% Híbrida, Fruity Pebbles OG x Grape Pie).
  2. `cannarado-wedding-pie`: **Wedding Pie** (70% Índica / 30% Sativa, Wedding Cake x Grape Pie).
  3. `cannarado-apple-sundae`: **Apple Sundae** (60% Sativa / 40% Índica, Sour Apple x Sundae Driver).
  4. `cannarado-birthday-cake`: **Birthday Cake** (65% Índica / 35% Sativa, Girl Scout Cookies x Cherry Pie).
  5. `cannarado-banana-sundae`: **Banana Sundae** (60% Índica / 40% Sativa, Banana OG x Sundae Driver).
  6. `cannarado-biscotti-sundae`: **Biscotti Sundae** (70% Índica / 30% Sativa, Biscotti x Sundae Driver).
  7. `cannarado-kitchen-sink`: **Kitchen Sink** (75% Índica / 25% Sativa, GMO Cookies x Sundae Driver).
  8. `cannarado-pie-hoe`: **Pie Hoe** (70% Índica / 30% Sativa, Grape Pie x Tahoe OG).
  9. `cannarado-5-alive`: **5 Alive** (70% Sativa / 30% Índica, Bubblegum x Orange Juice x Grape Pie).
  10. `cannarado-birthday-funk`: **Birthday Funk** (70% Índica / 30% Sativa, Birthday Cake x Dosidos).

- **Fotografias Botanicas Oficiales HD (v191):** 20 imagenes reales de cogollos de alta resolucion (hasta 4032x3024), procesadas a 800x800 con el pipeline radial oscuro CannaCulture (WebP + JPG).
- **Auditoria Exhaustiva de Todo el Catalogo (697 cepas, 1418 imagenes):**
  * Metodo: pHash 256 bits (16x16) con umbral Hamming <= 8.
  * **Resultado: 0 duplicados en todo el catalogo.**
- **Cobertura Linaje/Genetica:** 697/697 cepas (100%).

### v190 — María Master Sumiller & CannaDoctor 2.0 (Femenino)
- **Identidad de María**: La anfitriona experta y sommelier oficial es ahora María, una sumiller y botánica culta, cercana y con criterio propio.
- **Concordancia en femenino**: Adaptación de todos los prompts de sistema (Gemini Cloud, LLM Local Ollama, Gemini Nano y Motor Autónomo), títulos de interfaz ("María | Master Sumiller & CannaDoctor 2.0", "María | Sumiller IA"), placeholders, badges y mensajes de razonamiento ("RAZONAMIENTO DE LA SOMMELIER").
- **Avatar Femenino**: Incorporación del avatar `👩‍🌾` tanto en el header inline de la sección como en el widget flotante.
- **Saludo Inicial Proactivo**: Al cargar el chat, María saluda y presenta de forma acogedora las capacidades de maridaje, CannaDoctor 2.0, charla abierta y locución interactiva.
- **Voz TTS Femenina**: Selector de síntesis de voz que prioriza voces naturales femeninas en español si están instaladas en el sistema/navegador.
- **Compatibilidad Retrospectiva**: Alias `MATEO_SYSTEM_PROMPT = MARIA_SYSTEM_PROMPT` preservado en cliente y servidor para evitar incompatibilidades.

### v189 — Mobile Optimization
- **Ventana flotante**: Sheet nativo a pantalla casi completa en móvil (88dvh/92dvh).
- **Swipe-down para cerrar**: Gesto táctil nativo para descartar la ventana flotante.
- **Sin zoom iOS**: Inputs con `font-size: 16px` mínimo.
- **Targets táctiles 44x44px**: Todos los botones con área táctil cómoda para dedos.
- **Pills scroll horizontal**: Desplazamiento fluido sin desbordar la pantalla.
- **FAB compacto**: Icono optimizado en pantallas estrechas (<=480px).

---

## Metricas del Catalogo
- **Variedades Totales:** 697 (100% unicas)
- **Bancos Activos:** 57
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


