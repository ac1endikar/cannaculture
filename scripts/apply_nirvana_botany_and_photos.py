import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

images_to_save = [
    ("nirvana-northern-light", "scratch/test_nirvana-northern-light.png"),
    ("nirvana-gsc", "scratch/test_nirvana-gsc.png"),
    ("nirvana-og-kush", "scratch/test_nirvana-og-kush.png"),
    ("nirvana-gelato", "scratch/test_nirvana-gelato.png"),
    ("nirvana-white-widow", "scratch/test_nirvana-white-widow.png"),
]

os.makedirs('img', exist_ok=True)
os.makedirs('images/strains/nirvana-seeds', exist_ok=True)

for strain_id, src in images_to_save:
    if os.path.exists(src):
        im = Image.open(src)
        if im.size != (800, 800):
            im = im.resize((800, 800), Image.Resampling.LANCZOS)
            
        p1 = f"img/{strain_id}.webp"
        p2 = f"images/strains/nirvana-seeds/{strain_id}.webp"
        
        im.save(p1, 'WEBP', quality=92, method=6)
        im.save(p2, 'WEBP', quality=92, method=6)
        print(f"[OK] Saved {p1} and {p2} ({os.path.getsize(p1):,} bytes)")
    else:
        print(f"[ERROR] Missing source: {src}")

print("\nImages deployed successfully.")
