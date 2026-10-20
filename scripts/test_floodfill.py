from PIL import Image
import numpy as np
from collections import deque

def convert_white_to_dark_studio(img_path, out_path, bg_color=(12, 16, 22), tol=35):
    im = Image.open(img_path).convert("RGBA")
    w, h = im.size
    
    # Recorte centrado 1:1 si no es cuadrada
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im = im.crop((left, top, left + crop_sz, top + crop_sz))
    w, h = im.size
    
    arr = np.array(im, dtype=np.uint8)
    # Mascara de visitados para flood fill
    visited = np.zeros((h, w), dtype=bool)
    
    # Encolar bordes que sean casi blancos (R>215, G>215, B>215)
    queue = deque()
    for x in range(w):
        for y in [0, h - 1]:
            r, g, b, _ = arr[y, x]
            if r > 215 and g > 215 and b > 215:
                queue.append((x, y))
                visited[y, x] = True
    for y in range(h):
        for x in [0, w - 1]:
            if not visited[y, x]:
                r, g, b, _ = arr[y, x]
                if r > 215 and g > 215 and b > 215:
                    queue.append((x, y))
                    visited[y, x] = True
                    
    # BFS flood fill
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx]:
                r, g, b, _ = arr[ny, nx]
                # Blanco o casi blanco
                if r > 205 and g > 205 and b > 205:
                    visited[ny, nx] = True
                    queue.append((nx, ny))
                    
    # Crear fondo oscuro de estudio con gradiente radial muy sutil
    bg = Image.new("RGB", (w, h), bg_color)
    bg_arr = np.array(bg, dtype=np.uint8)
    
    # Donde visited es True, poner bg_color
    res_rgb = np.array(im.convert("RGB"))
    res_rgb[visited] = bg_arr[visited]
    
    res_img = Image.fromarray(res_rgb)
    if w < 600 or h < 600:
        res_img = res_img.resize((600, 600), Image.Resampling.LANCZOS)
    res_img.save(out_path, "JPEG", quality=95, optimize=True)
    print(f"Convertido {out_path}: {res_img.size}")
    
    # Verificar esquinas
    corners = [res_img.getpixel((0,0)), res_img.getpixel((res_img.width-1, 0)), res_img.getpixel((0, res_img.height-1)), res_img.getpixel((res_img.width-1, res_img.height-1))]
    print(f"Esquinas resultantes: {corners}")

convert_white_to_dark_studio(r"d:\cannaculture\img\cannabiogen-sandstorm-bud.jpg", r"d:\cannaculture\scratch\test_sandstorm_dark.jpg")
