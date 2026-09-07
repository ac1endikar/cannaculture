import re

with open("js/bundle.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total líneas en js/bundle.js: {len(lines)}")

# Search for any trace of sensi-sensi-amnesia or ihg-terple
sensi_lines = [i+1 for i, l in enumerate(lines) if "sensi-sensi-amnesia" in l or "sensi amnesia" in l.lower()]
terple_lines = [i+1 for i, l in enumerate(lines) if "ihg-terple" in l or "terple" in l.lower()]

print(f"Líneas de Sensi Amnesia en bundle.js: {sensi_lines} (Debe ser [])")
print(f"Líneas de Terple en bundle.js: {terple_lines} (Debe ser [])")

# Show surrounding lines around line 3845
print("\n--- Líneas 3842-3855 en bundle.js (Zona anterior de Sensi Amnesia): ---")
for idx in range(3841, min(3855, len(lines))):
    print(f"L{idx+1}: {lines[idx].rstrip()[:90]}")

# Count total strain objects in bundle.js
strains = re.findall(r'id:\s*["\']([^"\']+)["\']', "\n".join(lines))
strain_ids = [s for s in strains if not s.startswith(('log_', 'mission_'))]
print(f"\nTotal real cepas en bundle.js: {len(strain_ids)}")
