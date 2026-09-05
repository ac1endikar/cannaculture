import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

ths_ids = re.findall(r'id:\s*"([^"]+)"', text)
th_seeds = [i for i in ths_ids if i.startswith('ths-')]
print(f"Total ths- IDs found in data.js: {len(th_seeds)}")
for i in th_seeds:
    print("  -", i)
