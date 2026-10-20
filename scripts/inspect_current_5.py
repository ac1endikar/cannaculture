from PIL import Image

for fname in ["cannabiogen-sandstorm-bud.jpg", "cannabiogen-caribe-bud.jpg", "soma-free-white.jpg", "tfd-the-real-mccoy.jpg", "raw-rainbow-studz.jpg"]:
    path = rf"d:\cannaculture\img\{fname}"
    with Image.open(path) as im:
        print(f"{fname}: {im.size}, format {im.format}")
        # sample border
        corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
        print(f"  corners: {corners}")
