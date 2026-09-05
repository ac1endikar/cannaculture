import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

# Blue Dream HSO candidate: hso-blue-dream-cand4.jpg (720x720)
bd_src = os.path.join(img_dir, 'hso-blue-dream-cand4.jpg')
if os.path.exists(bd_src):
    im = Image.open(bd_src)
    im.save(os.path.join(img_dir, 'hso-blue-dream.jpg'), 'JPEG', quality=95)
    im.save(os.path.join(img_dir, 'hso-blue-dream-official.jpg'), 'JPEG', quality=95)
    print(f"✅ Blue Dream HSO updated to {im.width}x{im.height} -> hso-blue-dream-official.jpg")

# Sapphire OG candidate: hso-sapphire-og-cand2.jpg (1080x1080)
saph_src = os.path.join(img_dir, 'hso-sapphire-og-cand2.jpg')
if os.path.exists(saph_src):
    im = Image.open(saph_src)
    im.save(os.path.join(img_dir, 'hso-sapphire-og.jpg'), 'JPEG', quality=95)
    im.save(os.path.join(img_dir, 'hso-sapphire-og-official.jpg'), 'JPEG', quality=95)
    print(f"✅ Sapphire OG updated to {im.width}x{im.height} -> hso-sapphire-og-official.jpg")
