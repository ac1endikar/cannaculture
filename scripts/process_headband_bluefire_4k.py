import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

# Process 707 Headband 2000x2000 photo
hb_src = os.path.join(img_dir, '707-headband-hd3_707_Headba.jpg')
if os.path.exists(hb_src):
    im = Image.open(hb_src)
    dest1 = os.path.join(img_dir, 'hso-707-headband-4k.jpg')
    dest2 = os.path.join(img_dir, 'hso-707-headband.jpg')
    im.save(dest1, 'JPEG', quality=95)
    im.save(dest2, 'JPEG', quality=95)
    print(f"✅ 707 Headband updated to {im.width}x{im.height} 4K photo -> {dest1} ({os.path.getsize(dest1):,} bytes)")

# Process Blue Fire 2400x2400 photo
bf_src = os.path.join(img_dir, 'blue-fire-hd4_Blue_Fire_.jpg')
if os.path.exists(bf_src):
    im = Image.open(bf_src)
    dest1 = os.path.join(img_dir, 'hso-blue-fire-4k.jpg')
    dest2 = os.path.join(img_dir, 'hso-blue-fire.jpg')
    im.save(dest1, 'JPEG', quality=95)
    im.save(dest2, 'JPEG', quality=95)
    print(f"✅ Blue Fire updated to {im.width}x{im.height} 4K photo -> {dest1} ({os.path.getsize(dest1):,} bytes)")
