import json
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_JS = r"d:\cannaculture\js\data.js"

with open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# Buscaremos las 16 variedades
search_terms = [
    ("Caramel Cream / Cream Caramel", r"(caramel|cream)"),
    ("Guawi", r"guawi"),
    ("Malawi", r"\bmalawi\b"),
    ("Super Malawi Haze", r"super-malawi|super\s+malawi"),
    ("Valley Girl", r"valley-girl|valley"),
    ("Zkittlez OG", r"zkittlez-og"),
    ("Gorilla Ghost", r"gorilla-ghost"),
    ("Sandstorm", r"sandstorm"),
    ("Leshaze", r"leshaze"),
    ("Cheese", r"\bcheese\b"),
    ("Passion Fruit", r"passion-fruit"),
    ("Fruit Punch", r"fruit-punch"),
    ("Terple", r"terple"),
    ("Northern Light", r"northern-light"),
    ("Gelato", r"\bgelato\b"),
    ("White Widow", r"white-widow")
]

# Parse strains
lines = content.splitlines()
in_strains = False
strains = []
curr = {}

for line in lines:
    line_s = line.strip()
    if "export const STRAINS_DATABASE = [" in line_s:
        in_strains = True
        continue
    if in_strains and line_s.startswith("];"):
        in_strains = False
        break
    if not in_strains:
        continue
        
    if line_s.startswith("{") and "id:" in line_s:
        curr = {}
    m_id = re.search(r'id:\s*["\']([^"\']+)["\']', line_s)
    if m_id:
        curr["id"] = m_id.group(1)
    m_name = re.search(r'name:\s*["\']([^"\']+)["\']', line_s)
    if m_name:
        curr["name"] = m_name.group(1)
    m_bank = re.search(r'bank:\s*["\']([^"\']+)["\']', line_s)
    if m_bank:
        curr["bank"] = m_bank.group(1)
    m_img = re.search(r'image:\s*["\']([^"\']+)["\']', line_s)
    if m_img:
        curr["image"] = m_img.group(1)
    if (line_s.startswith("},") or line_s == "}") and "id" in curr:
        strains.append(curr)
        curr = {}

print(f"Total cepas cargadas: {len(strains)}")

for label, pattern in search_terms:
    print(f"\n=== BÚSQUEDA: {label} ===")
    matches = [s for s in strains if re.search(pattern, s['id'], re.I) or re.search(pattern, s['name'], re.I)]
    for m in matches:
        print(f"  ID: {m['id']:30} | Name: {m['name']:25} | Bank: {m.get('bank', ''):20} | Image: {m.get('image', '')}")
