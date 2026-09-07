from PIL import Image, ImageDraw, ImageFilter, ImageOps
import os

def create_studio_backdrop(width, height):
    base = Image.new('RGB', (width, height), (7, 10, 9))
    glow = Image.new('L', (100, 100), 0)
    g_draw = ImageDraw.Draw(glow)
    for r in range(48, 0, -1):
        intensity = int(255 * (1.0 - (r / 48) ** 1.6))
        g_draw.ellipse([50 - r, 50 - r, 50 + r, 50 + r], fill=intensity)
    glow_resized = glow.resize((width, height), Image.Resampling.BICUBIC)
    center_glow = Image.new('RGB', (width, height), (22, 32, 27))
    backdrop = Image.composite(center_glow, base, glow_resized)
    return backdrop

def studio_dark_transform(input_path, output_path, min_dim=600):
    im = Image.open(input_path).convert('RGB')
    w, h = im.size
    
    if w < min_dim or h < min_dim:
        scale = max(min_dim / w, min_dim / h)
        w, h = int(w * scale), int(h * scale)
        im = im.resize((w, h), Image.Resampling.LANCZOS)
    
    orig_w, orig_h = w, h
    fw_scale = 1.0
    if w > 1200 or h > 1200:
        fw_scale = 1200 / max(w, h)
        work_im = im.resize((int(w * fw_scale), int(h * fw_scale)), Image.Resampling.BILINEAR)
    else:
        work_im = im
        
    ww, wh = work_im.size
    
    # Identify near-white pixels
    # In RGB, white has R>220, G>220, B>220
    # Also check difference between max and min channel (saturation) < 25
    rgb_pix = work_im.load()
    white_mask = Image.new('L', (ww, wh), 0)
    w_draw = white_mask.load()
    
    for y in range(wh):
        for x in range(ww):
            r, g, b = rgb_pix[x, y]
            if r > 215 and g > 215 and b > 215:
                w_draw[x, y] = 255
    
    # Border-connected floodfill:
    # Canvas with 1px border initialized to 255
    padded = Image.new('L', (ww + 2, wh + 2), 255)
    padded.paste(white_mask, (1, 1))
    
    # Flood-fill connected 255s starting at (0, 0) with 128
    ImageDraw.floodfill(padded, (0, 0), 128)
    
    # Background is exactly where value == 128
    cropped = padded.crop((1, 1, ww + 1, wh + 1))
    bg_mask = cropped.point(lambda p: 255 if p == 128 else 0)
    
    if fw_scale != 1.0:
        bg_mask = bg_mask.resize((orig_w, orig_h), Image.Resampling.BILINEAR)
        
    # Soft feather
    blurred_bg = bg_mask.filter(ImageFilter.GaussianBlur(radius=2.0))
    fg_mask = ImageOps.invert(blurred_bg)
    
    backdrop = create_studio_backdrop(orig_w, orig_h)
    result = Image.composite(im, backdrop, fg_mask)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    result.save(output_path, 'JPEG', quality=95)
    
    # Verify new metrics
    thumb = result.resize((50, 50))
    border_pixels = [thumb.getpixel((x, y)) for y in range(50) for x in range(50) if y == 0 or y == 49 or x == 0 or x == 49]
    wb_count = sum(1 for (r, g, b) in border_pixels if r > 200 and g > 200 and b > 200)
    wb_pct = (wb_count / len(border_pixels)) * 100
    
    print(f"[OK] {os.path.basename(output_path)} ({orig_w}x{orig_h} px) -> Borde blanco: {wb_pct:.1f}%")
    return wb_pct < 5.0

studio_dark_transform('img/ripper-double-glock-plant.jpg', 'img/ripper-double-glock-bud-hd.jpg')
studio_dark_transform('img/bsf-gorilla-glue-4.jpg', 'img/bsf-gorilla-glue-4-bud-hd.jpg')
