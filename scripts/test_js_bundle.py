import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/bundle.js', 'r', encoding='utf-8') as f:
    code = f.read()

print(f"Bundle JS total size: {len(code):,} bytes")

# Check if STRAINS_DATABASE is defined
if "const STRAINS_DATABASE =" in code or "var STRAINS_DATABASE =" in code or "STRAINS_DATABASE =" in code:
    print("✅ STRAINS_DATABASE is defined")
else:
    print("❌ STRAINS_DATABASE missing")

# Check if CannaAppMAX is defined
if "class CannaAppMAX" in code:
    print("✅ CannaAppMAX class is defined")

# Check if initCannaApp is present at the end
if "initCannaApp()" in code:
    print("✅ initCannaApp readyState check is present")
