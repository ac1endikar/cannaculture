from PIL import Image, ImageFilter, ImageOps
import os

def convert_white_to_studio_dark(input_path, output_path, bg_color=(10, 15, 13)):
    """
    Convierte fondos blancos planos en fondos oscuros de estudio fotográfico.
    Preserva los detalles macro del cogollo y elimina el halo blanco.
    """
    im = Image.open(input_path).convert('RGB')
    w, h = im.size
    
    # Create mask of background
    # White background threshold: R>225, G>225, B>225 and low saturation
    # We can compute a whiteness score per pixel
    gray = ImageOps.grayscale(im)
    
    # Mask where pixel is very bright white
    # Using point transform for thresholding
    # 255 if near white, 0 otherwise
    threshold = 220
    mask_white = gray.point(lambda p: 255 if p > threshold else 0)
    
    # Clean up mask with slight blur to anti-alias edges
    mask_white_blurred = mask_white.filter(ImageFilter.GaussianBlur(radius=1.5))
    
    # Foreground mask is inverted (255 = keep flower, 0 = background)
    fg_mask = ImageOps.invert(mask_white_blurred)
    
    # Create dark studio background (radial vignette)
    # Center slightly lighter, edges dark (#0a0f0d to #030504)
    bg = Image.new('RGB', (w, h), bg_color)
    
    # Composite: where fg_mask is 255, take flower; where 0, take dark bg
    result = Image.composite(im, bg, fg_mask)
    
    result.save(output_path, 'JPEG', quality=95)
    
    # Check new border whiteness
    thumb = result.resize((50, 50))
    border_pixels = [thumb.getpixel((x, y)) for y in range(50) for x in range(50) if y == 0 or y == 49 or x == 0 or x == 49]
    wb_count = sum(1 for (r, g, b) in border_pixels if r > 200 and g > 200 and b > 200)
    wb_pct = (wb_count / len(border_pixels)) * 100
    avg_bright = sum((r + g + b) / 3 for (r, g, b) in thumb.getdata()) / (50 * 50)
    
    print(f"Processed: {os.path.basename(output_path)} -> Borde blanco: {wb_pct:.1f}%, Brillo: {avg_bright:.1f}/255")
    return wb_pct < 10.0

test_files = [
    ('img/ripper-kroma-plant.jpg', 'img/ripper-kroma-bud-hd.jpg'),
    ('img/bsf-lebron-haze-fem-real.jpg', 'img/bsf-lebron-haze-bud-hd.jpg'),
    ('img/dinafem-sweet-grapefruit.jpg', 'img/dinafem-sweet-grapefruit-bud-hd.jpg'),
    ('img/rqs-royal-gorilla-bud.jpg', 'img/rqs-royal-gorilla-bud-hd.jpg')
]

for inp, outp in test_files:
    convert_white_to_studio_dark(inp, outp)
