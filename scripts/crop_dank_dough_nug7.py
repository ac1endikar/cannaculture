import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'
src = os.path.join(img_dir, 'arc-dank-dough-nug7.jpg')

im = Image.open(src)
w, h = im.size

# Crop square centered at 2500x2500
min_dim = min(w, h)
left = (w - min_dim) // 2
top = (h - min_dim) // 2
cropped = im.crop((left, top, left + min_dim, top + min_dim))
cropped = cropped.resize((2000, 2000), Image.Resampling.LANCZOS)

dest1 = os.path.join(img_dir, 'arc-dank-dough.jpg')
dest2 = os.path.join(img_dir, 'arc-dank-dough-curedbud.jpg')

cropped.save(dest1, 'JPEG', quality=98)
cropped.save(dest2, 'JPEG', quality=98)

print(f"✅ Dank Dough updated to 2000x2000 dry bud macro crop -> {dest2} ({os.path.getsize(dest2):,} bytes)")
