# scripts/convert_to_webp.py
import os
import sys
import re
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

IMG_DIR = r"d:\cannaculture\img"
DATA_JS = r"d:\cannaculture\js\data.js"
BACKUP_JS = r"d:\cannaculture\js\data.js.bak_before_webp"

def convert_images():
    total_before = 0
    total_after = 0
    count = 0
    already_converted = 0

    for root, _, files in os.walk(IMG_DIR):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in [".jpg", ".jpeg", ".png"]:
                src_path = os.path.join(root, file)
                dst_path = os.path.splitext(src_path)[0] + ".webp"
                
                size_before = os.path.getsize(src_path)
                total_before += size_before

                if os.path.exists(dst_path):
                    total_after += os.path.getsize(dst_path)
                    already_converted += 1
                    continue

                try:
                    with Image.open(src_path) as img:
                        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                            img = img.convert("RGBA")
                        else:
                            img = img.convert("RGB")
                        img.save(dst_path, "WEBP", quality=85, method=6)
                    
                    total_after += os.path.getsize(dst_path)
                    count += 1
                except Exception as e:
                    print(f"Error procesando {file}: {e}")

    mb_before = total_before / (1024 * 1024)
    mb_after = total_after / (1024 * 1024)
    saved = 100 - (mb_after / mb_before * 100) if mb_before > 0 else 0

    print(f"\n✅ Total imágenes analizadas: {count + already_converted}")
    print(f"   - Nuevas convertidas: {count}")
    print(f"   - Ya existentes: {already_converted}")
    print(f"📦 Tamaño antes: {mb_before:.2f} MB")
    print(f"⚡ Tamaño después: {mb_after:.2f} MB")
    print(f"📉 Ahorro total: {saved:.1f}%\n")

def update_data_js():
    if not os.path.exists(DATA_JS):
        print("No se encontró js/data.js")
        return

    with open(DATA_JS, "r", encoding="utf-8") as f:
        content = f.read()

    with open(BACKUP_JS, "w", encoding="utf-8") as f:
        f.write(content)

    updated_content = re.sub(r'\.(jpg|jpeg|png)(\?v=[^"\']*)?', r'.webp\2', content, flags=re.IGNORECASE)

    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("📄 Referencias actualizadas en js/data.js (backup creado).")

if __name__ == "__main__":
    convert_images()
    update_data_js()
