import os, sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

js_dir = 'd:/cannaculture/js'

files_in_order = [
    'data.js',
    'matcher.js',
    'bitacora.js',
    'missions.js',
    'audio.js',
    'tools.js',
    'ai-sommelier.js',
    'app.js'
]

bundled_code = ["// CannaCatalog 2.0 Bundled Version for Direct File Access\n"]

for filename in files_in_order:
    filepath = os.path.join(js_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Remove import statements
    code = re.sub(r'import\s+[^;]+;\n?', '', code)
    # Remove export statements
    code = re.sub(r'\bexport\s+const\s+', 'const ', code)
    code = re.sub(r'\bexport\s+class\s+', 'class ', code)
    code = re.sub(r'\bexport\s+default\s+', '', code)
    
    bundled_code.append(f"// --- {filename} ---")
    bundled_code.append(code)
    bundled_code.append("\n")

bundle_path = os.path.join(js_dir, 'bundle.js')
full_content = "\n".join(bundled_code)
with open(bundle_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

bundle_v148_path = os.path.join(js_dir, 'bundle-v148.js')
with open(bundle_v148_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

print(f"✅ Created {bundle_path} ({os.path.getsize(bundle_path):,} bytes)")
print(f"✅ Created {bundle_v148_path} ({os.path.getsize(bundle_v148_path):,} bytes)")
