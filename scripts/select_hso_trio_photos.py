import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

targets = [
    ("hso-liberty-haze", "hso-liberty-haze-cand0.jpg"),
    ("hso-707-headband", "hso-707-headband-cand0.jpg"),
    ("hso-blue-fire", "hso-blue-fire-cand2.jpg")
]

for prefix, cand_name in targets:
    src = os.path.join(img_dir, cand_name)
    if os.path.exists(src):
        im = Image.open(src)
        dest1 = os.path.join(img_dir, f"{prefix}.jpg")
        dest2 = os.path.join(img_dir, f"{prefix}-official.jpg")
        im.save(dest1, 'JPEG', quality=95)
        im.save(dest2, 'JPEG', quality=95)
        print(f"✅ {prefix} updated to {im.width}x{im.height} official product photo -> {dest2}")
