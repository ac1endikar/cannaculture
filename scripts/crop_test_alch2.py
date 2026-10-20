import numpy as np
from PIL import Image

src_path = 'd:/cannaculture/scratch/free_white/alch_2.jpg'
img = Image.open(src_path).convert('RGB')
w, h = img.size
print(f"Original: {w}x{h}")

# We want a 1:1 square, minimum 800x800 px (or 900x900 or 1000x1000).
# The bud extends from top to bottom.
# Let's crop a square centered horizontally, with slightly more room at top for the tip of the cola.
# Height is 1200, width is 1000.
# If we take a square of side 1000:
# y_start = 50, y_end = 1050 (or y_start = 20, y_end = 1020) so the tip has breathing room.

box = (0, 30, 1000, 1030) # 1000 x 1000
cropped = img.crop(box)

# Let's scale to 850x850 or 800x800
final_800 = cropped.resize((800, 800), Image.Resampling.LANCZOS)
final_800.save('d:/cannaculture/scratch/free_white/test_800.jpg', quality=95)

# Also check corner luminosity
arr = np.array(final_800)
corners = [
    arr[0:40, 0:40],
    arr[0:40, -40:],
    arr[-40:, 0:40],
    arr[-40:, -40:]
]
print("Final 800x800 corner luminosity:", np.mean([np.mean(c) for c in corners]))
