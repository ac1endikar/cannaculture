from PIL import Image

for name in ['heavyweight-lemon-cake-bud.jpg', 'heavyweight-fruit-punch-bud.jpg', 'bf-lsd.jpg']:
    im = Image.open('img/' + name).convert('RGB')
    w, h = im.size
    print(f"=== {name} ({w}x{h}) ===")
    # Tomar 10 muestras a lo largo del ancho (x) y ver color promedio
    for i in range(10):
        x = int((i / 9) * (w - 1))
        pixel = im.getpixel((x, h // 2))
        print(f"  x={x:4d}: {pixel}")
