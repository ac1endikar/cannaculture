import os

target_files = [
    "heavyweight-lemon-cake-bud-hd.jpg",
    "heavyweight-fruit-punch-bud-hd.jpg",
    "bf-lsd-bud-hd.jpg"
]

img_dir = r"d:\cannaculture\img"

print("=== PASO 1: COMPROBACIÓN Y BORRADO DE ARCHIVOS FÍSICOS ===")
for filename in target_files:
    full_path = os.path.join(img_dir, filename)
    exists = os.path.exists(full_path)
    if exists:
        os.remove(full_path)
        print(f"ARCHIVO DETECTADO Y ELIMINADO: {full_path}")
    else:
        print(f"NO EXISTE EN DISCO (ELIMINADO): {full_path}")
