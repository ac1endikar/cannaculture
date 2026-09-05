import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.split('{\n    id:')
print(f"Total blocks split: {len(blocks)}")
for b in blocks:
    if 'wls-afghani-1' in b or 'wls-master-kush' in b:
        print("--------------------------------------------------")
        print("{\n    id:" + b[:400])
