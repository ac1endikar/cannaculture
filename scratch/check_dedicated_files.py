import json, os

with open('scratch/white_bg_list.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

img_files = os.listdir('img')
img_files_lower = {f.lower(): f for f in img_files}

print(f"Total strains in white_bg: {len(items)}")

for x in items:
    sid = x['id']
    name = x['name']
    bank = x['bank']
    cur_f = x['fname']
    
    # Try finding candidate file matching id or name
    slug = sid.replace('_', '-')
    candidates = []
    for fl, real_f in img_files_lower.items():
        if slug in fl and real_f != cur_f:
            candidates.append(real_f)
    if candidates:
        print(f"[{bank}] {name} ({sid}) currently '{cur_f}' has candidates: {candidates}")
