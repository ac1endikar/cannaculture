import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

ids = re.findall(r'id:\s*["\']([^"\']+)["\']', text)
print(f"Total strain IDs found: {len(ids)}")
seen = set()
dups = []
for i in ids:
    if i in seen:
        dups.append(i)
    seen.add(i)

print(f"Total unique IDs: {len(seen)}")
print(f"Duplicates ({len(dups)}):", dups)
