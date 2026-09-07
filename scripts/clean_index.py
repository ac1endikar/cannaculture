with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<dialog id="image-lightbox-modal"')
if idx != -1:
    header_part = content[:idx]
    lightbox_and_end = """<dialog id="image-lightbox-modal" class="lightbox-dialog">
    <div class="lightbox-wrapper">
      <!-- Botón cierre flotante -->
      <button class="lightbox-close-btn" id="lightbox-close-btn" onclick="document.getElementById('image-lightbox-modal').close()" title="Cerrar (ESC)">✕</button>

      <!-- Info superior -->
      <div class="lightbox-header">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 1.4rem;">🌿</span>
          <div>
            <h3 id="lightbox-title" class="lightbox-title-text">Genética</h3>
            <span id="lightbox-subtitle" class="lightbox-subtitle-text">FOTOGRAFÍA BOTÁNICA • ALTA RESOLUCIÓN HD</span>
          </div>
        </div>
        <div id="lightbox-zoom-indicator" class="lightbox-zoom-indicator">100% (Vista Original)</div>
      </div>

      <!-- Viewport / Canvas interactivo para Zoom y Arrastre -->
      <div id="lightbox-viewport" class="lightbox-viewport">
        <img id="lightbox-img" src="" alt="Foto en alta resolución" class="lightbox-main-img" draggable="false" />
        <div class="lightbox-zoom-hint">🔍 Rueda del ratón / Pellízcalo para hacer Zoom • Arrastra para mover</div>
      </div>

      <!-- Barra de controles flotante estilo CannaCatalog Glass -->
      <div class="lightbox-controls-bar">
        <button id="lightbox-btn-zoom-out" class="lightbox-ctrl-btn" title="Alejar (-)">➖ Alejar</button>
        <button id="lightbox-btn-reset" class="lightbox-ctrl-btn" title="Restablecer (100%)">🔄 100%</button>
        <button id="lightbox-btn-zoom-in" class="lightbox-ctrl-btn" title="Acercar (+)">➕ Acercar</button>
        <button id="lightbox-btn-hd" class="lightbox-ctrl-btn hd-btn" title="Zoom Macro HD 2.5x">🔬 Macro 2.5x HD</button>
      </div>
    </div>
  </dialog>

  <!-- Cargador Bundled Blindado para compatibilidad total HTTP y archivo local file:// -->
  <script src="js/bundle.js?v=2026_phase2_custom3_v114"></script>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(header_part + lightbox_and_end)
    print('Cleaned index.html successfully')
else:
    print('Lightbox modal not found!')
