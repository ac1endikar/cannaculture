import os
import shutil
from pathlib import Path
from PIL import Image

img_dir = Path("d:/cannaculture/img")

# 1. PHYSICAL REMOVAL OF OLD ERRONEOUS FILES
old_files = [
    img_dir / "blimburn-guanabana-bud.jpg",
    img_dir / "soma-free-white.jpg"
]

removed = []
for old in old_files:
    if old.exists():
        os.remove(old)
        removed.append(str(old))
        print(f"[DELETED] Physically removed old erroneous file: {old}")
    else:
        print(f"[NOT FOUND] File was already removed: {old}")

# Verify old files are gone
for old in old_files:
    assert not old.exists(), f"Error: {old} still exists!"
print("[CONFIRMED] Old erroneous files do NOT exist in img/")

# 2. SAVE NEW REAL BOTANICAL PHOTOS WITH REQUESTED NAMES
# Guanabana
src_guanabana = img_dir / "blimburn-guanabana-bud-hd.jpg"
dest_guanabana = img_dir / "blimburn-guanabana-bud-real.jpg"
if not dest_guanabana.exists() or dest_guanabana.stat().st_size != src_guanabana.stat().st_size:
    shutil.copy2(src_guanabana, dest_guanabana)
with Image.open(dest_guanabana) as img:
    print(f"[CREATED] {dest_guanabana.name}: {img.size} px ({dest_guanabana.stat().st_size} bytes)")

# Free White
src_free_white = img_dir / "soma-free-white-bud-hd.jpg"
dest_free_white = img_dir / "free-white-bud-real.jpg"
if not dest_free_white.exists() or dest_free_white.stat().st_size != src_free_white.stat().st_size:
    shutil.copy2(src_free_white, dest_free_white)
with Image.open(dest_free_white) as img:
    print(f"[CREATED] {dest_free_white.name}: {img.size} px ({dest_free_white.stat().st_size} bytes)")

print("[OK] Finished purge and rename script.")
