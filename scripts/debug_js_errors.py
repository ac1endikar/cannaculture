import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

js_dir = 'd:/cannaculture/js'

files = ['data.js', 'matcher.js', 'bitacora.js', 'missions.js', 'audio.js', 'tools.js', 'ai-sommelier.js', 'app.js', 'bundle.js']

for f in files:
    p = os.path.join(js_dir, f)
    if not os.path.exists(p):
        print(f"❌ File missing: {f}")
        continue
    with open(p, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check for basic unbalanced brackets / braces / parens
    parens = content.count('(') - content.count(')')
    braces = content.count('{') - content.count('}')
    brackets = content.count('[') - content.count(']')
    
    print(f"{f:20s}: parens_diff={parens:3d}, braces_diff={braces:3d}, brackets_diff={brackets:3d}, size={len(content):,} bytes")
