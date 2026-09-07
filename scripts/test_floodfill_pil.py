from PIL import Image
from collections import deque

def convert_white_to_dark_studio(img_path, out_path, bg_color=(14, 18, 24), tol=215):
    im = Image.open(img_path).convert("RGB")
    w, h = im.size
    
    # Recorte 1:1 centrado
    crop_sz = min(w, h)
    left = (w - crop_sz) // 2
    top = (h - crop_sz) // 2
    im = im.crop((left, top, left + crop_sz, top + crop_sz))
    w, h = im.size
    
    pixels = im.load()
    visited = set()
    queue = deque()
    
    # Encolar bordes blancos
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
                    
    # BFS
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                r, g, b = pixels[nx, ny]
                if r >= 200 and g >= 200 and b >= 200:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
    # Reemplazar píxeles visitados por el color de fondo oscuro
    for x, y in visited:
        pixels[x, y] = bg_color
        
    if w < 600:
        im = im.resize((600, 600), Image.Resampling.LANCZOS)
    im.save(out_path, "JPEG", quality=95, optimize=True)
    print(f"Convertido {out_path}: {im.size}")
    corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
    print(f"Esquinas: {corners}")

convert_white_to_dark_studio(r"d:\cannaculture\img\cannabiogen-sandstorm-bud.jpg", r"d:\cannaculture\scratch\test_sandstorm_dark.jpg")
