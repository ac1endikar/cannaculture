"""
Script de generación del banner oficial Open Graph (1200x630px) para CannaCulture.
Genera assets/img/og-cannaculture-1200x630.jpg y su réplica en img/og-cannaculture-1200x630.jpg.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def draw_vector_icon(draw, icon_type, cx, cy, size=18, color=(52, 211, 153)):
    """Dibuja iconos vectoriales geométricos nítidos para evitar fallos de fuentes/emojis."""
    r = size // 2
    if icon_type == "leaf":
        # Hoja / Botánica estilizada
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=color, width=2)
        draw.line([(cx - r, cy + r), (cx + r, cy - r)], fill=color, width=2)
    elif icon_type == "bank":
        # Edificio / Banco clásico: frontón triangular + columnas
        draw.polygon([(cx, cy - r - 2), (cx - r - 2, cy - r // 3), (cx + r + 2, cy - r // 3)], outline=color, width=2)
        # Columnas
        draw.line([(cx - r + 1, cy - r // 3), (cx - r + 1, cy + r)], fill=color, width=2)
        draw.line([(cx, cy - r // 3), (cx, cy + r)], fill=color, width=2)
        draw.line([(cx + r - 1, cy - r // 3), (cx + r - 1, cy + r)], fill=color, width=2)
        draw.line([(cx - r - 3, cy + r), (cx + r + 3, cy + r)], fill=color, width=2)
    elif icon_type == "flask":
        # Matraz de laboratorio / Terpenos
        draw.line([(cx - 3, cy - r), (cx + 3, cy - r)], fill=color, width=2)
        draw.line([(cx, cy - r), (cx, cy - 2)], fill=color, width=2)
        draw.polygon([(cx, cy - 2), (cx - r, cy + r), (cx + r, cy + r)], outline=color, width=2)
        draw.ellipse((cx - 2, cy + 3, cx + 2, cy + 7), fill=color)
    elif icon_type == "ai":
        # Estrella / Chispa de Inteligencia Artificial (4 puntas)
        draw.line([(cx, cy - r), (cx, cy + r)], fill=color, width=2)
        draw.line([(cx - r, cy), (cx + r, cy)], fill=color, width=2)
        draw.line([(cx - r // 2, cy - r // 2), (cx + r // 2, cy + r // 2)], fill=color, width=1)
        draw.line([(cx - r // 2, cy + r // 2), (cx + r // 2, cy - r // 2)], fill=color, width=1)
    elif icon_type == "shield":
        # Escudo de seguridad / 18+
        draw.polygon([(cx, cy - r), (cx + r, cy - r + 3), (cx + r - 2, cy + 2), (cx, cy + r), (cx - r + 2, cy + 2), (cx - r, cy - r + 3)],
                     outline=color, width=2)

def create_og_banner():
    width = 1200
    height = 630

    # Crear lienzo base RGB oscuro
    bg_color = (11, 15, 14)  # #0B0F0E
    banner = Image.new("RGBA", (width, height), bg_color + (255,))

    # Añadir resplandores esmeralda ambientales en el fondo
    glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # Resplandores ambientales
    glow_draw.ellipse((-150, -150, 500, 500), fill=(16, 185, 129, 45))
    glow_draw.ellipse((120, 280, 720, 750), fill=(5, 150, 105, 35))
    glow_draw.ellipse((720, 80, 1320, 680), fill=(16, 185, 129, 50))

    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(90))
    banner = Image.alpha_composite(banner, glow_layer)

    # Cargar y componer fotografía macro botánica en lateral derecho
    macro_path = "img/kmintz.png"
    if not os.path.exists(macro_path):
        macro_path = "img/blue_dream.png"

    if os.path.exists(macro_path):
        macro_img = Image.open(macro_path).convert("RGBA")
        macro_size = 660
        macro_img = macro_img.resize((macro_size, macro_size), Image.Resampling.LANCZOS)

        # Máscara de degradado horizontal suave para fundir con el fondo oscuro a la izquierda
        mask = Image.new("L", (macro_size, macro_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        fade_width = 260
        for x in range(macro_size):
            if x < fade_width:
                alpha = int(255 * (x / fade_width) ** 1.6)
            else:
                alpha = 255
            mask_draw.line([(x, 0), (x, macro_size)], fill=alpha)

        flower_x = width - macro_size + 45
        flower_y = (height - macro_size) // 2

        flower_canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        flower_canvas.paste(macro_img, (flower_x, flower_y), mask)
        banner = Image.alpha_composite(banner, flower_canvas)

    # Capa de viñeta para asegurar legibilidad total de los textos a la izquierda
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    for x in range(780):
        alpha = int(220 * (1 - (x / 780) ** 1.3))
        overlay_draw.line([(x, 0), (x, height)], fill=(11, 15, 14, alpha))

    banner = Image.alpha_composite(banner, overlay)

    # Fuentes del sistema
    font_segoe_bold = "C:/Windows/Fonts/segoeuib.ttf"
    font_segoe_reg = "C:/Windows/Fonts/segoeui.ttf"
    font_arial_bold = "C:/Windows/Fonts/arialbd.ttf"
    font_arial_reg = "C:/Windows/Fonts/arial.ttf"

    font_path_bold = font_segoe_bold if os.path.exists(font_segoe_bold) else font_arial_bold
    font_path_reg = font_segoe_reg if os.path.exists(font_segoe_reg) else font_arial_reg

    font_badge = ImageFont.truetype(font_path_bold, 15)
    font_logo_canna = ImageFont.truetype(font_path_bold, 68)
    font_version = ImageFont.truetype(font_path_bold, 20)
    font_tagline = ImageFont.truetype(font_path_bold, 24)
    font_desc = ImageFont.truetype(font_path_reg, 17)
    font_pill = ImageFont.truetype(font_path_bold, 19)
    font_pill_sub = ImageFont.truetype(font_path_reg, 13)
    font_footer = ImageFont.truetype(font_path_reg, 15)
    font_footer_bold = ImageFont.truetype(font_path_bold, 15)

    draw = ImageDraw.Draw(banner)

    # 1. Eyebrow Badge (+18 y Categoría)
    badge_x = 75
    badge_y = 65
    badge_w = 330
    badge_h = 32
    draw.rounded_rectangle((badge_x, badge_y, badge_x + badge_w, badge_y + badge_h), radius=16,
                           fill=(6, 78, 59, 210), outline=(16, 185, 129, 230), width=1)
    # Icono de escudo vectorial
    draw_vector_icon(draw, "shield", badge_x + 22, badge_y + badge_h // 2, size=13, color=(52, 211, 153))
    draw.text((badge_x + 36, badge_y + 7), "CATÁLOGO BOTÁNICO OFICIAL • +18", font=font_badge, fill=(52, 211, 153))

    # 2. Logotipo Maestro: CANNA CULTURE 2.0 ULTRA
    logo_y = 120
    draw.text((badge_x, logo_y), "CANNA", font=font_logo_canna, fill=(255, 255, 255))
    canna_bbox = draw.textbbox((badge_x, logo_y), "CANNA", font=font_logo_canna)
    culture_x = canna_bbox[2] + 16
    draw.text((culture_x, logo_y), "CULTURE", font=font_logo_canna, fill=(16, 185, 129))

    # Badge de versión centrado y alineado armónicamente
    culture_bbox = draw.textbbox((culture_x, logo_y), "CULTURE", font=font_logo_canna)
    version_text = "2.0 ULTRA"
    v_text_bbox = draw.textbbox((0, 0), version_text, font=font_version)
    v_w = v_text_bbox[2] - v_text_bbox[0] + 24
    v_h = 36
    v_x = culture_bbox[2] + 16
    v_y = logo_y + (culture_bbox[3] - logo_y - v_h) // 2 + 6

    draw.rounded_rectangle((v_x, v_y, v_x + v_w, v_y + v_h), radius=8,
                           fill=(6, 78, 59, 230), outline=(16, 185, 129, 220), width=1)
    draw.text((v_x + 12, v_y + 6), version_text, font=font_version, fill=(52, 211, 153))

    # 3. Subtítulo / Claims de Autoridad
    sub_y = 215
    draw.text((badge_x, sub_y), "Enciclopedia Botánica & Sommelier Inteligente IA", font=font_tagline, fill=(241, 245, 249))

    desc_y = 252
    draw.text((badge_x, desc_y), "Base de datos clasificada con linajes, terpenos, floración y ratios THC/CBD.", font=font_desc, fill=(148, 163, 184))

    # 4. Píldoras de Estadísticas Maestras (2x2 Grid)
    pill_w = 265
    pill_h = 68
    grid_gap_x = 20
    grid_gap_y = 16

    row1_y = 302
    row2_y = row1_y + pill_h + grid_gap_y

    pills_data = [
        # (x, y, titulo, subtitulo, tipo_icono)
        (badge_x, row1_y, "877 Variedades", "Fotoperiódicas & Feminizadas", "leaf"),
        (badge_x + pill_w + grid_gap_x, row1_y, "75 Bancos Élite", "Líderes Mundiales Oficiales", "bank"),
        (badge_x, row2_y, "8 Terpenos Clave", "Perfiles de Aroma & Efecto", "flask"),
        (badge_x + pill_w + grid_gap_x, row2_y, "Sommelier IA María", "Recomendación Reactiva", "ai")
    ]

    for px, py, ptitle, psub, itype in pills_data:
        # Fondo redondeado con sutil gradiente/borde
        draw.rounded_rectangle((px, py, px + pill_w, py + pill_h), radius=12,
                               fill=(15, 23, 21, 220), outline=(52, 211, 153, 90), width=1)
        # Icono vectorial centrado verticalmente
        draw_vector_icon(draw, itype, px + 28, py + pill_h // 2, size=18, color=(52, 211, 153))
        # Textos
        draw.text((px + 52, py + 12), ptitle, font=font_pill, fill=(255, 255, 255))
        draw.text((px + 52, py + 38), psub, font=font_pill_sub, fill=(148, 163, 184))

    # 5. Barra Inferior / Footer
    footer_line_y = 508
    draw.line([(badge_x, footer_line_y), (badge_x + 550, footer_line_y)], fill=(16, 185, 129, 60), width=1)

    footer_y = 530
    draw.text((badge_x, footer_y), "cannacultureapp.com", font=font_footer_bold, fill=(52, 211, 153))
    url_bbox = draw.textbbox((badge_x, footer_y), "cannacultureapp.com", font=font_footer_bold)
    draw.text((url_bbox[2] + 12, footer_y), "•  Guía de Cultivo en 5 Etapas  •  Panel Dispensario CSC", font=font_footer, fill=(148, 163, 184))

    # 6. Marco perimetral fino esmeralda para terminación ultra-premium
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=(16, 185, 129, 70), width=1)

    # Convertir a RGB y optimizar para guardar
    final_banner = banner.convert("RGB")

    os.makedirs("assets/img", exist_ok=True)
    os.makedirs("img", exist_ok=True)

    dest_paths = [
        "assets/img/og-cannaculture-1200x630.jpg",
        "img/og-cannaculture-1200x630.jpg"
    ]

    for p in dest_paths:
        final_banner.save(p, format="JPEG", quality=88, optimize=True)
        size_kb = os.path.getsize(p) / 1024
        print(f"[OK] Banner generado: {p} ({size_kb:.1f} KB, 1200x630 px)")

if __name__ == "__main__":
    create_og_banner()
