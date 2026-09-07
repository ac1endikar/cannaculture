import os
from PIL import Image

targets = [
    ("Caramel Cream (Sweet)", "sweet-cream-caramel", "img/sweet-cream-caramel-real.jpg"),
    ("Caramel Cream (00)", "oo-caramel-cream", "img/oo-caramel-cream-bud.jpg"),
    ("Guawi (ACE)", "aceseeds-guawi", "img/aceseeds-guawi-bud.jpg"),
    ("Malawi (ACE)", "aceseeds-malawi", "img/aceseeds-malawi-bud-real.jpg"),
    ("Super Malawi Haze (ACE)", "aceseeds-super-malawi-haze", "img/aceseeds-super-malawi-haze-bud-real.jpg"),
    ("Valley Girl (Archive)", "arc-valley-girl", "img/arc-valley-girl-bud-real.jpg"),
    ("Zkittlez OG (Barney)", "bf-zkittlez-og", "img/bf-zkittlez-og-bud-hd.jpg"),
    ("Gorilla Ghost (BSF)", "bsf-gorilla-ghost", "img/bsf-gorilla-ghost.jpg"),
    ("Sandstorm (Cannabiogen)", "cannabiogen-sandstorm", "img/cannabiogen-sandstorm-bud-real.jpg"),
    ("Leshaze (Cannabiogen)", "cannabiogen-leshaze", "img/cannabiogen-leshaze-bud.jpg"),
    ("Cheese (Dinafem)", "dinafem-cheese", "img/dinafem-cheese.jpg"),
    ("Passion Fruit (Dutch Passion)", "dp-passion-fruit", "img/dp-passion-fruit-bud-real.jpg"),
    ("Fruit Punch (Heavyweight)", "heavyweight-fruit-punch", "img/heavyweight-fruit-punch-official-real.jpg"),
    ("Terple (In-House)", "ihg-terple", "img/ihg-terple-bud-real.jpg"),
    ("Northern Light (Nirvana)", "nirvana-northern-light", "img/nirvana-northern-light-flower-hd.jpg"),
    ("Gelato (Nirvana)", "nirvana-gelato", "img/nirvana-gelato-bud-hd.jpg"),
    ("White Widow (Green House)", "ghs-white-widow", "img/ghs-white-widow-bud.jpg")
]

for label, sid, rel_path in targets:
    fpath = os.path.join(r"d:\cannaculture", rel_path.replace("/", os.sep))
    if os.path.exists(fpath):
        with Image.open(fpath) as im:
            im_rgb = im.convert("RGB")
            w, h = im_rgb.size
            corners = [im_rgb.getpixel((0,0)), im_rgb.getpixel((w-1, 0)), im_rgb.getpixel((0, h-1)), im_rgb.getpixel((w-1, h-1))]
            white_corners = sum(1 for c in corners if sum(c)/3 > 215)
            print(f"{label:32} | {sid:26} | {w}x{h} px | Esquinas: {corners}")
    else:
        print(f"{label:32} | {sid:26} | NO EXISTE: {rel_path}")
