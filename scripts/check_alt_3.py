import os
from PIL import Image

def get_wb_pct(fname):
    p = os.path.join(r'd:\cannaculture\img', fname)
    if not os.path.exists(p): return 999.0
    im = Image.open(p).convert('RGB')
    thumb = im.resize((50, 50), Image.Resampling.BILINEAR)
    border = []
    for y in range(50):
        for x in range(50):
            if y == 0 or y == 49 or x == 0 or x == 49:
                border.append(thumb.getpixel((x, y)))
    white_cnt = sum(1 for (r, g, b) in border if r > 230 and g > 230 and b > 230)
    return (white_cnt / len(border)) * 100

print("Alternativas para ripper-washing-machine:")
for f in ['ripper-washing-machine.jpg', 'ripper-washing-machine-flowering.jpg', 'ripper-washing-machine-plant.jpg']:
    print(f"  {f}: {get_wb_pct(f):.1f}% blanco")

print("\nAlternativas para 00s-afghan-mass:")
for f in ['00s-critical-mass-bud-hd.jpg', 'wls-afghani-1-cand0.jpg', 'wls-afghani-1-cand2.jpg', 'wls-afghani-1-cand3.jpg', 'wls-afghani-1-cand4.jpg']:
    print(f"  {f}: {get_wb_pct(f):.1f}% blanco")

print("\nAlternativas para cannabiogen-leshaze:")
for f in [f for f in os.listdir(r'd:\cannaculture\img') if 'leshaze' in f or 'panama' in f]:
    print(f"  {f}: {get_wb_pct(f):.1f}% blanco")
