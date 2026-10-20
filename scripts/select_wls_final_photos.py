import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

# Afghani #1 candidate: wls-afghani-1-cand4.jpg (768x768 official product photo)
afghani_src = os.path.join(img_dir, 'wls-afghani-1-cand4.jpg')
if os.path.exists(afghani_src):
    im = Image.open(afghani_src)
    im.save(os.path.join(img_dir, 'wls-afghani-1.jpg'), 'JPEG', quality=95)
    im.save(os.path.join(img_dir, 'wls-afghani-1-official.jpg'), 'JPEG', quality=95)
    print(f"OK: Afghani #1 updated to {im.width}x{im.height} official product photo")

# Master Kush candidate: wls-master-kush-cand6.jpg (1080x1080 official product photo) or cand0 (600x600)
kush_src = os.path.join(img_dir, 'wls-master-kush-cand6.jpg')
if not os.path.exists(kush_src):
    kush_src = os.path.join(img_dir, 'wls-master-kush-cand0.jpg')

if os.path.exists(kush_src):
    im = Image.open(kush_src)
    im.save(os.path.join(img_dir, 'wls-master-kush.jpg'), 'JPEG', quality=95)
    im.save(os.path.join(img_dir, 'wls-master-kush-official.jpg'), 'JPEG', quality=95)
    print(f"OK: Master Kush updated to {im.width}x{im.height} official product photo")
