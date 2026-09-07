from PIL import Image
import os

p = r"d:\cannaculture\img\ghs-exodus-cheese-bud.jpg"
if os.path.exists(p):
    with Image.open(p) as im:
        print("ghs-exodus-cheese:", im.size)
        corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
        print("  corners:", corners)
else:
    print("No existe")
