from PIL import Image

for name in ['heavyweight-lemon-cake-bud.jpg', 'heavyweight-fruit-punch-bud.jpg', 'bf-lsd.jpg']:
    im = Image.open('img/' + name).convert('RGB')
    w, h = im.size
    active_cols = []
    for x in range(w):
        has_content = False
        for y in range(0, h, 5):
            r, g, b = im.getpixel((x, y))
            if r < 240 or g < 240 or b < 240:
                has_content = True
                break
        if has_content:
            active_cols.append(x)
    if active_cols:
        print(f"{name}: active cols {active_cols[0]} to {active_cols[-1]} (w={active_cols[-1]-active_cols[0]}, h={h})")
    else:
        print(f"{name}: blank")
