import os

img_files = os.listdir(r'd:\cannaculture\img')
backup_files = os.listdir(r'd:\cannaculture\img_ratio_backup') if os.path.exists(r'd:\cannaculture\img_ratio_backup') else []

all_known = set(img_files + backup_files)

keywords = ['lsd', 'fruit', 'lemon', 'cake', 'punch', 'afghan', 'snow', 'storm', 'zkittlez', 'zombie', 'fuel', 'candy']

for kw in keywords:
    matches = [f for f in all_known if kw in f.lower()]
    print(f"\nKeyword '{kw}': {len(matches)} archivos")
    for m in matches[:10]:
        print("  ", m)
