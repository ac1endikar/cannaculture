import json, sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('scratch/white_bg_list.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in range(min(30, len(items))):
    x = items[i]
    print(f"{i+1:2d}. {x['wb_pct']:5.1f}% | [{x['bank']}] {x['name']} ({x['id']}) -> {x['fname']} {x['size']}")
