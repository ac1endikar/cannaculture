import numpy as np
from PIL import Image

src_path = 'd:/cannaculture/scratch/free_white/alch_2.jpg'
img = Image.open(src_path).convert('RGB')
w, h = img.size

# Crop centered 1000x1000 square with breathing room for the tip of the cola
box = (0, 30, 1000, 1030)
cropped = img.crop(box)

# Resize to standard 800x800 px
final_800 = cropped.resize((800, 800), Image.Resampling.LANCZOS)
arr = np.array(final_800, dtype=np.float32)

# Apply gentle 25px fade at bottom edge to perfectly melt into dark studio background
fade_len = 25
for y_idx in range(800 - fade_len, 800):
    progress = (800 - 1 - y_idx) / float(fade_len) # 1.0 down to 0.0
    arr[y_idx, :, :] *= progress

final_img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

out_primary = 'd:/cannaculture/img/soma-free-white-bud-hd.jpg'
out_secondary = 'd:/cannaculture/img/free-white-bud-hd.jpg'

final_img.save(out_primary, quality=95, optimize=True)
final_img.save(out_secondary, quality=95, optimize=True)

# Verification
arr_final = np.array(final_img)
corners = [
    arr_final[0:40, 0:40],
    arr_final[0:40, -40:],
    arr_final[-40:, 0:40],
    arr_final[-40:, -40:]
]
mean_lum = np.mean([np.mean(c) for c in corners])
print("[OK] Free White HD image generated successfully:")
print(f"Primary output: {out_primary}")
print(f"Secondary output: {out_secondary}")
print(f"Dimensions: {final_img.size} px (1:1 aspect ratio)")
print(f"Corner luminosity: {mean_lum:.2f}/255")
print(f"Bottom row mean: {np.mean(arr_final[-1, :]):.2f}/255")
