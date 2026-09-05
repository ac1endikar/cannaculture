import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text_data = f.read()

with open('d:/cannaculture/js/bundle.js', 'r', encoding='utf-8') as f:
    text_bundle = f.read()

count_data = text_data.count("The Flying Dutchmen")
count_bundle = text_bundle.count("The Flying Dutchmen")

print(f"Occurrences of 'The Flying Dutchmen' in data.js: {count_data}")
print(f"Occurrences of 'The Flying Dutchmen' in bundle.js: {count_bundle}")

tfd_data_ids = re.findall(r'id:\s*["\'](tfd-[^"\']+)["\']', text_data)
tfd_bundle_ids = re.findall(r'id:\s*["\'](tfd-[^"\']+)["\']', text_bundle)

print(f"TFD IDs in data.js ({len(tfd_data_ids)}): {tfd_data_ids}")
print(f"TFD IDs in bundle.js ({len(tfd_bundle_ids)}): {tfd_bundle_ids}")
