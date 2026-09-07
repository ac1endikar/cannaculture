from PIL import Image
import os

images = [
    ("oo-caramel-cream", "img/oo-caramel-cream-bud-hd.jpg"),
    ("sweet-cream-caramel", "img/sweet-cream-caramel-bud-hd.jpg"),
    ("bf-zkittlez-og", "img/bf-zkittlez-og-bud-hd.jpg"),
    ("nirvana-white-widow", "img/nirvana-white-widow-flowering-real.jpg"),
    ("ripper-criminal-plus", "img/ripper-criminal-plus-plant.jpg"),
    ("sweet-black-jack", "img/sweet-black-jack-bud-real.jpg"),
    ("ripper-kmintz", "img/ripper-kmintz-plant.jpg"),
    ("sensi-sensi-amnesia", "img/sensi-sensi-amnesia-bud-real.jpg"),
    ("phil-lemon-og-candy", "img/philo-lemon-og-candy.jpg"),
    ("ihg-terple", "img/ihg-terple-bud-hd.jpg"),
    ("raw-rainbow-studz", "img/raw-rainbow-studz-bud-real.jpg")
]

for name, path in images:
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{name:<25} | Path: {path:<40} | Size: {im.size} | Format: {im.format}")
    else:
        print(f"{name:<25} | Path: {path:<40} | NOT FOUND")
