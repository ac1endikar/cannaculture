import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count("White Label Seed Co.")
print(f"Occurrences of 'White Label Seed Co.' in bundle.js: {count}")

ids = re.findall(r'id:\s*["\'](wls-[^"\']+)["\']', text)
print(f"WLS strain IDs found in bundle.js ({len(ids)}):", ids)
