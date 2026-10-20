import os, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

img_dir = 'd:/cannaculture/img'

cands = [
    'arc-dank-dough-nug7.jpg',
    'arc-dank-dough-nug8.jpg',
    'arc-dank-dough-nug10.jpg',
    'arc-dank-dough-cand9.jpg',
    'arc-dank-dough-cand2.jpg',
    'arc-dank-dough-cand4.jpg'
]

for c in cands:
    p = os.path.join(img_dir, c)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"Candidate {c:25s}: {im.width}x{im.height} ({os.path.getsize(p):,} bytes)")
