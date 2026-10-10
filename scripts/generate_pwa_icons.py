"""
Script de generación de iconos PWA oficiales para CannaCulture.
Genera los iconos estándar, maskables y apple-touch-icon en assets/icons/ e img/icons/.
"""

import os
import sys
import math
from PIL import Image, ImageDraw, ImageFilter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def draw_botanical_leaf(draw, cx, cy, scale=1.0, color=(16, 185, 129), stem_color=(52, 211, 153)):
    """Dibuja una hoja botánica de cannabis estilizada de 7 folíolos simétricos."""
    # Parámetros de los folíolos: (ángulo en grados respecto a la vertical, longitud, ancho relativo)
    leaflets = [
        (0, 140 * scale, 28 * scale),      # Central
        (26, 115 * scale, 24 * scale),     # Superior derecho
        (-26, 115 * scale, 24 * scale),    # Superior izquierdo
        (52, 85 * scale, 20 * scale),      # Medio derecho
        (-52, 85 * scale, 20 * scale),     # Medio izquierdo
        (76, 55 * scale, 16 * scale),      # Inferior derecho
        (-76, 55 * scale, 16 * scale),     # Inferior izquierdo
    ]

    # Dibujar folíolos desde los más exteriores hacia el centro
    for angle_deg, length, width in reversed(leaflets):
        rad = math.radians(angle_deg - 90) # -90 para que 0 sea vertical hacia arriba
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        
        # Puntos del folíolo en forma de elipse lanceolada
        tip_x = cx + length * cos_a
        tip_y = cy + length * sin_a

        perp_cos = -sin_a
        perp_sin = cos_a

        # Punto medio del lóbulo
        mid_x = cx + (length * 0.45) * cos_a
        mid_y = cy + (length * 0.45) * sin_a

        w_half = width * 0.5
        p_left = (mid_x + w_half * perp_cos, mid_y + w_half * perp_sin)
        p_right = (mid_x - w_half * perp_cos, mid_y - w_half * perp_sin)

        poly = [(cx, cy), p_left, (tip_x, tip_y), p_right]
        draw.polygon(poly, fill=color)

        # Nervadura central del folíolo
        draw.line([(cx, cy), (tip_x, tip_y)], fill=stem_color, width=max(1, int(2 * scale)))

    # Tallo central inferior
    stem_len = 35 * scale
    draw.line([(cx, cy), (cx, cy + stem_len)], fill=stem_color, width=max(2, int(4 * scale)))
    # Nódulo de unión
    draw.ellipse((cx - 4 * scale, cy - 4 * scale, cx + 4 * scale, cy + 4 * scale), fill=stem_color)

def generate_base_master_icon(size=512, is_maskable=False):
    """Genera el lienzo maestro de 512x512."""
    bg_color = (11, 15, 14, 255) # #0B0F0E
    img = Image.new("RGBA", (size, size), bg_color)

    # Capa de resplandor esmeralda ambiental
    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    center = size // 2
    r_glow = int(size * 0.4)
    glow_draw.ellipse((center - r_glow, center - r_glow, center + r_glow, center + r_glow),
                      fill=(16, 185, 129, 65))
    glow = glow.filter(ImageFilter.GaussianBlur(int(size * 0.12)))
    img = Image.alpha_composite(img, glow)

    draw = ImageDraw.Draw(img)

    # Para iconos no-maskables, añadir un anillo exterior con borde esmeralda sutil
    if not is_maskable:
        ring_r = int(size * 0.44)
        draw.ellipse((center - ring_r, center - ring_r, center + ring_r, center + ring_r),
                     outline=(16, 185, 129, 140), width=max(2, int(size * 0.008)))
        inner_r = int(size * 0.41)
        draw.ellipse((center - inner_r, center - inner_r, center + inner_r, center + inner_r),
                     outline=(52, 211, 153, 50), width=1)

    # Escala de la hoja: En maskable debe ocupar máximo el 65% del tamaño para cumplir la Safe Zone del 80%
    scale = (size / 512.0) * (0.85 if is_maskable else 1.08)
    cy_offset = int(center + 20 * scale)

    # Hoja botánica con sombra suave
    shadow_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_layer)
    draw_botanical_leaf(shadow_draw, center, cy_offset + 4, scale=scale, color=(0, 0, 0, 160), stem_color=(0, 0, 0, 160))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(6))
    img = Image.alpha_composite(img, shadow_layer)

    # Hoja principal
    leaf_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    leaf_draw = ImageDraw.Draw(leaf_layer)
    draw_botanical_leaf(leaf_draw, center, cy_offset, scale=scale, color=(16, 185, 129), stem_color=(110, 231, 183))
    img = Image.alpha_composite(img, leaf_layer)

    return img

def main():
    assets_dir = "assets/icons"
    img_dir = "img/icons"
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)

    # 1. Generar Master Icon Estándar y Maskable
    master_standard = generate_base_master_icon(512, is_maskable=False)
    master_maskable = generate_base_master_icon(512, is_maskable=True)

    # 2. Diccionario de iconos a exportar
    icons_to_generate = [
        # (nombre_archivo, imagen_origen, dimensiones)
        ("icon-512x512.png", master_standard, (512, 512)),
        ("icon-192x192.png", master_standard, (192, 192)),
        ("icon-maskable-512x512.png", master_maskable, (512, 512)),
        ("icon-maskable-192x192.png", master_maskable, (192, 192)),
        ("apple-touch-icon.png", master_standard, (180, 180)),
        ("favicon-32x32.png", master_standard, (32, 32)),
        ("favicon-16x16.png", master_standard, (16, 16)),
    ]

    for fname, src_img, (w, h) in icons_to_generate:
        resized = src_img.resize((w, h), Image.Resampling.LANCZOS)
        
        # Guardar en assets/icons/
        p1 = os.path.join(assets_dir, fname)
        resized.save(p1, format="PNG", optimize=True)
        
        # Guardar en img/icons/
        p2 = os.path.join(img_dir, fname)
        resized.save(p2, format="PNG", optimize=True)
        
        kb = os.path.getsize(p1) / 1024
        print(f"[OK] Icono generado: {fname} ({w}x{h} px, {kb:.1f} KB)")

    print("Todos los iconos PWA generados con éxito.")

if __name__ == "__main__":
    main()
