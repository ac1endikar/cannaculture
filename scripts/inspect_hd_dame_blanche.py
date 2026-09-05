import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

for f in sorted(os.listdir(img_dir)):
    if f.startswith('tfd-dame-blanche-new') and f.endswith('.jpg'):
        p = os.path.join(img_dir, f)
        im = Image.open(p)
        print(f"{f:32s} {im.width}x{im.height} ({os.path.getsize(p):,} bytes)")
