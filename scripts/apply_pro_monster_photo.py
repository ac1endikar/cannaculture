import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

src_path = "d:/cannaculture/scratch/monster_candidates/cand_7.jpg"
im = Image.open(src_path)
w, h = im.size
print(f"Original size: {w}x{h}")

crop = im.crop((0, 0, 1152, 1152))
resized = crop.resize((700, 700), Image.Resampling.LANCZOS)

targets = [
    "d:/cannaculture/img/monster.webp",
    "d:/cannaculture/images/strains/monster.webp",
    "d:/cannaculture/images/strains/eva-seeds/monster.webp"
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    resized.save(t, "WEBP", quality=92)
    print(f"✅ Saved {t} ({os.path.getsize(t)} bytes)")
