import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

banks = re.findall(r'bank:\s*"([^"]+)"', content)
unique_banks = sorted(list(set(banks)))

print(f"Total strains in database: {len(banks)}")
print(f"Total unique seed banks: {len(unique_banks)}\n")

for b in unique_banks:
    c = banks.count(b)
    print(f"  - {b}: {c} strain(s)")
