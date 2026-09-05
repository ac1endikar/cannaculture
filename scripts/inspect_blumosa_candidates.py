import os, sys
from PIL import Image, ImageStat

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

for f in sorted(os.listdir(img_dir)):
    if f.startswith('ths-blumosa-real') and f.endswith('.jpg'):
        p = os.path.join(img_dir, f)
        im = Image.open(p).convert('RGB')
        w, h = im.size
        stat = ImageStat.Stat(im)
        corners = [im.getpixel((0,0)), im.getpixel((w-1,0)), im.getpixel((0,h-1)), im.getpixel((w-1,h-1))]
        avg_corner = sum(sum(c) for c in corners) / (4 * 3)
        print(f"{f:30s} {w}x{h} px | mean_rgb={stat.mean[0]:.1f},{stat.mean[1]:.1f},{stat.mean[2]:.1f} | corner_bg={avg_corner:.1f} | size={os.path.getsize(p):,} bytes")
