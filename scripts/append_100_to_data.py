import os
import sys
import re
import json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
DATA_JS = os.path.join(ROOT, "js", "data.js")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from fetch_100_strains_catalog import NEW_STRAINS

with open(DATA_JS, "r", encoding="utf-8") as f:
    text = f.read()

strains_start = text.find("export const STRAINS_DATABASE = [")
if strains_start == -1:
    print("Error: Could not find STRAINS_DATABASE in data.js")
    sys.exit(1)

# Format each new strain cleanly as a JS object
def format_strain_to_js(s):
    # Remove 'query' if present
    obj = {k: v for k, v in s.items() if k != 'query'}
    
    # We want pretty JS output:
    lines = ["  {"]
    
    # Ordered keys for nice consistency
    key_order = [
        'id', 'image', 'name', 'aka', 'bank', 'species', 'thc', 'cbd',
        'indicaPct', 'sativaPct', 'floweringDays', 'rating', 'reviewsCount',
        'yieldIndoor', 'yieldOutdoor', 'genetics', 'lineage', 'origin',
        'dominantTerpene', 'terpenes', 'aroma', 'flavors', 'effects',
        'activities', 'description', 'visualColor', 'bgPattern'
    ]
    
    for k in key_order:
        if k not in obj:
            continue
        v = obj[k]
        if isinstance(v, str):
            val_str = json.dumps(v, ensure_ascii=False)
            lines.append(f'    {k}: {val_str},')
        elif isinstance(v, (int, float)):
            lines.append(f'    {k}: {v},')
        elif isinstance(v, dict):
            # Format terpenes: { myrcene: 45, limonene: 30, ... }
            inner = ", ".join(f"{tk}: {tv}" for tk, tv in v.items())
            lines.append(f'    {k}: {{ {inner} }},')
        elif isinstance(v, list):
            val_str = json.dumps(v, ensure_ascii=False)
            lines.append(f'    {k}: {val_str},')
    
    # Remove trailing comma on last line
    if lines[-1].endswith(','):
        lines[-1] = lines[-1][:-1]
    
    lines.append("  }")
    return "\n".join(lines)

def apply_new_strains():
    global text
    # Check if already applied
    for s in NEW_STRAINS:
        if f'id: "{s["id"]}"' in text or f'id: \'{s["id"]}\'' in text:
            print(f"Strain {s['id']} already exists in data.js! Skipping duplicate insertion.")
            return

    # Find the end of STRAINS_DATABASE array:
    # Look for last `\n];`
    match = re.search(r'\n\];\s*$', text)
    if not match:
        print("Error: Could not find end of STRAINS_DATABASE array `];`")
        return
    
    idx_close = match.start()
    
    formatted_new = [format_strain_to_js(s) for s in NEW_STRAINS]
    new_block = ",\n" + ",\n".join(formatted_new) + "\n];\n"
    
    new_text = text[:idx_close] + new_block
    
    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write(new_text)
    
    print(f"✅ Successfully appended {len(NEW_STRAINS)} strains to {DATA_JS}")

if __name__ == '__main__':
    apply_new_strains()
