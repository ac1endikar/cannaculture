import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open("js/data.js", "r", encoding="utf-8") as f:
    data_content = f.read()

# 1. Count before deletion
before_strains = re.findall(r'id:\s*["\']([^"\']+)["\']', data_content)
print(f"Total cepas antes de eliminar: {len(before_strains)}")

# Record lines of sensi-sensi-amnesia and ihg-terple
for idx, line in enumerate(data_content.splitlines(), 1):
    if 'sensi-sensi-amnesia' in line or 'ihg-terple' in line:
        print(f"  Línea {idx}: {line.strip()}")

# Delete sensi-sensi-amnesia object
# Match { ... id: "sensi-sensi-amnesia" ... },
pattern_sensi = r'\s*\{\s*id:\s*["\']sensi-sensi-amnesia["\'].*?\}(?:,\s*)?'
data_content, count_sensi = re.subn(pattern_sensi, '\n', data_content, count=1, flags=re.DOTALL)
print(f"Eliminado sensi-sensi-amnesia: {count_sensi} objeto(s)")

# Delete ihg-terple object
# Match { ... id: "ihg-terple" ... },
pattern_terple = r'\s*\{\s*id:\s*["\']ihg-terple["\'].*?\}(?:,\s*)?'
data_content, count_terple = re.subn(pattern_terple, '\n', data_content, count=1, flags=re.DOTALL)
print(f"Eliminado ihg-terple: {count_terple} objeto(s)")

# Clean any double commas or trailing syntax
data_content = re.sub(r',\s*,', ',', data_content)

# Write updated data.js
with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(data_content)

# Verify count after
after_strains = re.findall(r'id:\s*["\']([^"\']+)["\']', data_content)
print(f"Total cepas después de eliminar: {len(after_strains)}")
assert len(after_strains) == len(before_strains) - 2, "El conteo no disminuyó en 2!"

# Rebuild bundle.js
os.system("python scripts/build_bundle.py")

# Verify bundle.js does not contain either strain
with open("js/bundle.js", "r", encoding="utf-8") as f:
    bundle_code = f.read()

bundle_strains = re.findall(r'\bid:\s*["\']([^"\']+)["\']', bundle_code)
print(f"Total cepas en bundle.js: {len(bundle_strains)}")
assert "sensi-sensi-amnesia" not in bundle_code, "sensi-sensi-amnesia sigue presente en bundle.js!"
assert "ihg-terple" not in bundle_code, "ihg-terple sigue presente en bundle.js!"
print("✅ Ambas cepas eliminadas completamente de bundle.js (0 apariciones).")

# Update index.html to v118
with open("index.html", "r", encoding="utf-8") as f:
    idx_code = f.read()

idx_code_new = re.sub(r'bundle\.js\?v=[^"\'>\s]+', 'bundle.js?v=2026_phase2_custom3_v118', idx_code)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_code_new)
print("✅ index.html actualizado a: bundle.js?v=2026_phase2_custom3_v118")
