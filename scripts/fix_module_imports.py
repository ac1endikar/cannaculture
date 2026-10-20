import os, sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

js_dir = 'd:/cannaculture/js'
version_param = '?v=2026_clean_v45'

for f in os.listdir(js_dir):
    if f.endswith('.js') and f != 'bundle.js':
        p = os.path.join(js_dir, f)
        with open(p, 'r', encoding='utf-8') as fp:
            text = fp.read()
        
        # Replace data.js query string with consistent version
        updated = re.sub(r'./data\.js(?:\?[^"\']*)?', f'./data.js{version_param}', text)
        
        if updated != text:
            with open(p, 'w', encoding='utf-8') as fp:
                fp.write(updated)
            print(f"✅ Updated imports in {f}")
