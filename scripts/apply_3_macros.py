import shutil
from PIL import Image

src_lsd = r"C:\Users\endik\.gemini\antigravity-ide\brain\c506c0f1-22e0-475b-a32d-e8561a2fd772\bf_lsd_bud_hd_1788532659407.jpg"
src_lemon = r"C:\Users\endik\.gemini\antigravity-ide\brain\c506c0f1-22e0-475b-a32d-e8561a2fd772\hw_lemon_cake_bud_1788532677217.jpg"
src_fruit = r"C:\Users\endik\.gemini\antigravity-ide\brain\c506c0f1-22e0-475b-a32d-e8561a2fd772\hw_fruit_punch_bud_1788532694877.jpg"

dst_lsd = r"d:\cannaculture\img\bf-lsd-bud-hd.jpg"
dst_lemon = r"d:\cannaculture\img\heavyweight-lemon-cake-bud-hd.jpg"
dst_fruit = r"d:\cannaculture\img\heavyweight-fruit-punch-bud-hd.jpg"

for src, dst in [(src_lsd, dst_lsd), (src_lemon, dst_lemon), (src_fruit, dst_fruit)]:
    shutil.copy2(src, dst)
    im = Image.open(dst)
    print(f"Copiado {dst}: {im.size} px")
