import os

bundle_path = r"d:\cannaculture\js\bundle.js"
size = os.path.getsize(bundle_path)
print(f"=== PASO 3: TAMAÑO CONFIRMADO DE js/bundle.js ===")
print(f"Ruta: {bundle_path}")
print(f"Tamaño exacto: {size} bytes ({size / 1024:.2f} KB)")
