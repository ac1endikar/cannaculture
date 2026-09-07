import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

print("=== BUSCANDO 'AMNESIA' EN js/data.js ===")
chunks = re.split(r'(?=\bid\s*:\s*["\'])', text)
amnesia_strains = []
terple_strains = []

for c in chunks:
    id_m = re.search(r'\bid\s*:\s*["\']([^"\']+)["\']', c)
    name_m = re.search(r'\bname\s*:\s*["\']([^"\']+)["\']', c)
    bank_m = re.search(r'\bbank\s*:\s*["\']([^"\']+)["\']', c)
    img_m = re.search(r'\bimage\s*:\s*["\']([^"\']+)["\']', c)
    if id_m:
        sid = id_m.group(1)
        sname = name_m.group(1) if name_m else ""
        sbank = bank_m.group(1) if bank_m else ""
        simg = img_m.group(1) if img_m else ""
        
        if "amnesia" in sid.lower() or "amnesia" in sname.lower():
            amnesia_strains.append((sid, sname, sbank, simg))
        if "terple" in sid.lower() or "terple" in sname.lower():
            terple_strains.append((sid, sname, sbank, simg))

print(f"Total cepas con Amnesia: {len(amnesia_strains)}")
for s in amnesia_strains:
    print(f"  ID: {s[0]:<30} | Name: {s[1]:<25} | Bank: {s[2]:<20} | Image: {s[3]}")

print(f"\nTotal cepas con Terple: {len(terple_strains)}")
for s in terple_strains:
    print(f"  ID: {s[0]:<30} | Name: {s[1]:<25} | Bank: {s[2]:<20} | Image: {s[3]}")
