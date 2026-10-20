from PIL import Image
import os
import sys
from collections import deque

def convert_white_to_dark_studio(im_rgb, bg_color=(14, 18, 24), tol=215):
    w, h = im_rgb.size
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im = im_rgb.crop((left, top, left + crop_sz, top + crop_sz))
    w, h = im.size
    
    pixels = im.load()
    visited = set()
    queue = deque()
    
    for x in range(w):
        for y in [0, h - 1]:
            r, g, b = pixels[x, y]
            if r >= tol and g >= tol and b >= tol:
                visited.add((x, y))
                queue.append((x, y))
    for y in range(h):
        for x in [0, w - 1]:
            if (x, y) not in visited:
                r, g, b = pixels[x, y]
                if r >= tol and g >= tol and b >= tol:
                    visited.add((x, y))
                    queue.append((x, y))
                    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                r, g, b = pixels[nx, ny]
                if r >= 200 and g >= 200 and b >= 200:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
    for x, y in visited:
        pixels[x, y] = bg_color
        
    if w < 600:
        im = im.resize((600, 600), Image.Resampling.LANCZOS)
    return im

IMG_DIR = r"d:\cannaculture\img"
fpath = os.path.join(IMG_DIR, "dp-skywalker-og-bud-real.jpg")
im = Image.open(fpath).convert("RGB")
im_dark = convert_white_to_dark_studio(im)
im_dark.save(fpath, "JPEG", quality=95, optimize=True)
corners = [im_dark.getpixel((0,0)), im_dark.getpixel((im_dark.width-1, 0)), im_dark.getpixel((0, im_dark.height-1)), im_dark.getpixel((im_dark.width-1, im_dark.height-1))]
print("dp-skywalker-og esquinas corregidas:", corners)
