import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

terpenes_part = text[:text.find("export const STRAINS_DATABASE = [")]
strains_part = text[text.find("export const STRAINS_DATABASE = ["):]

# Find all objects by counting matching braces
objects = []
idx = 0
n = len(strains_part)

while idx < n:
    # Find start of an object: {
    start = strains_part.find('{', idx)
    if start == -1:
        break
    
    # Count braces until balanced
    brace_count = 0
    end = start
    for i in range(start, n):
        char = strains_part[i]
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i
                break
    
    if brace_count == 0:
        obj_str = strains_part[start:end+1].strip()
        # Verify it's a strain object containing "id:"
        if 'id:' in obj_str or '"id":' in obj_str:
            # Clean quotes around keys
            c = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', obj_str)
            objects.append(c)
        idx = end + 1
    else:
        idx = start + 1

print(f"Parsed {len(objects)} strain objects from STRAINS_DATABASE cleanly with brace matching.")

formatted_database = "export const STRAINS_DATABASE = [\n  " + ",\n  ".join(objects) + "\n];\n"
final_content = terpenes_part.strip() + "\n\n" + formatted_database

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"✅ Cleaned data.js ({len(final_content):,} bytes)")
