import re

content = open('js/data.js', encoding='utf-8').read()
ids = [
    '00s-cheese-xl', '00s-white-smurf',
    'bsf-gorilla-glue-auto', 'bsf-lebron-haze-auto', 'bsf-red-critical-auto',
    'dinafem-critical-auto-2', 'dinafem-moby-dick-auto', 'dinafem-gorilla-auto',
    'dp-auto-blueberry', 'dp-auto-mazar',
    'rqs-og-kush-auto',
    'paradise-red-velvet-auto', 'paradise-stromboli-auto',
    'ss-bigdevil-xl', 'ss-black-cream-auto'
]

for s_id in ids:
    m = re.search(rf'\{{\s*id:\s*["\']{re.escape(s_id)}["\'].*?\n\s*\}}', content, re.DOTALL)
    if m:
        obj_text = m.group(0)
        img_m = re.search(r'image:\s*["\']([^"\']+)["\']', obj_text)
        img = img_m.group(1) if img_m else 'NO IMAGE'
        print(f"ID: {s_id} | Image: {img}")
    else:
        print(f"NOT FOUND: {s_id}")
