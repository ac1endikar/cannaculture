import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/bundle.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Look for undefined top-level references or typos in bundle.js
print("--- Checking bundle.js top-level variable declarations ---")

declared_vars = set(re.findall(r'(?:const|let|var|function|class)\s+([A-Za-z0-9_$]+)', code))
print(f"Declared symbols in bundle.js: {len(declared_vars)}")
for sym in ['STRAINS_DATABASE', 'TERPENES_INFO', 'ActivityMatcher', 'BitacoraManager', 'MissionGenerator', 'AmbientAudioEngine', 'AdvancedTools', 'AISommelierAgent', 'CannaAppMAX', 'initCannaApp']:
    if sym in declared_vars:
        print(f"  ✅ {sym} is declared")
    else:
        print(f"  ❌ {sym} is NOT declared")
