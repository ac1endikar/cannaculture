import sys, re, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.split('{\n    id:')
print(f"Total T.H. Seeds strains found in data.js:")
count = 0
for b in blocks[1:]:
    if 'bank: "TH Seeds"' in b or 'bank: \'TH Seeds\'' in b:
        count += 1
        lines = b.splitlines()
        s_id = lines[0].strip().strip('",')
        s_name = ""
        s_img = ""
        for l in lines:
            if 'name:' in l and not s_name:
                s_name = l.split('name:')[1].strip().strip('",')
            if 'image:' in l:
                s_img = l.split('image:')[1].strip().strip('",')
        exists = "EXISTS" if os.path.exists(os.path.join('d:/cannaculture', s_img)) else "MISSING"
        print(f"  {count:2d}. [{exists}] ID: {s_id:25s} | Name: {s_name:25s} | Image: {s_img}")
