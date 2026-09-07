from PIL import Image, ImageDraw, ImageFilter, ImageOps
import math

def create_studio_radial_gradient(width, height, center_color=(20, 28, 24), edge_color=(6, 9, 8)):
    """Generates a subtle, luxurious dark studio backdrop with soft center glow."""
    base = Image.new('RGB', (width, height), edge_color)
    # Draw radial glow
    glow = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(glow)
    
    cx, cy = width // 2, height // 2
    max_radius = int(math.hypot(cx, cy))
    
    # We can create a smaller radial glow and resize it with bilinear/bicubic filter for maximum smoothness
    gw, gh = 100, 100
    small_glow = Image.new('L', (gw, gh), 0)
    s_draw = ImageDraw.Draw(small_glow)
    s_cx, s_cy = gw // 2, gh // 2
    s_r = 45
    for r in range(s_r, 0, -1):
        intensity = int(255 * (1.0 - (r / s_r) ** 1.5))
        s_draw.ellipse([s_cx - r, s_cy - r, s_cx + r, s_cy + r], fill=intensity)
    
    glow = small_glow.resize((width, height), Image.Resampling.BICUBIC)
    
    # Center color image
    center_img = Image.new('RGB', (width, height), center_color)
    # Composite center glow over edge color
    backdrop = Image.composite(center_img, base, glow)
    return backdrop

print("Created gradient function successfully!")
