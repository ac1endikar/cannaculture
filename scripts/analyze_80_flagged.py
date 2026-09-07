import json

data = json.load(open('scratch/visual_audit_report.json', encoding='utf-8'))
flagged = data['flagged_strains']

print(f"Total cepas flagged: {len(flagged)}")

dupes = []
low_res = []
both = []

for sid, info in flagged.items():
    issues = info['issues']
    has_dupe = any('DUPLICADA' in i or 'NO_BOTANICA' in i for i in issues)
    has_low = any('RESOLUCION_BAJA' in i for i in issues)
    
    if has_dupe and has_low:
        both.append((sid, info))
    elif has_dupe:
        dupes.append((sid, info))
    elif has_low:
        low_res.append((sid, info))
    else:
        print(f"Otro issue en {sid}: {issues}")

print(f"\n1. Solo resolución baja: {len(low_res)}")
print(f"2. Solo duplicadas/no botánicas: {len(dupes)}")
print(f"3. Ambos (duplicada + baja resolución): {len(both)}")

print("\n--- DETALLE DE RESOLUCIÓN BAJA (primeras 15) ---")
for sid, info in (low_res + both)[:15]:
    meta = info['meta']
    print(f"  {sid} ({meta.get('fname')}): {meta.get('size')} px - {info['issues']}")

print("\n--- DETALLE DE DUPLICADAS / NO BOTÁNICAS ---")
for sid, info in (dupes + both):
    meta = info['meta']
    print(f"  {sid} ({meta.get('fname')}): {meta.get('size')} px - {info['issues']}")
