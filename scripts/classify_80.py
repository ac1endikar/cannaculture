import json

data = json.load(open('scratch/visual_audit_report.json', encoding='utf-8'))
flagged = data['flagged_strains']

dupes_group = {} # fname -> list of (sid, name, bank)
exclusive_low_res = [] # (sid, name, fname, w, h)
false_positives = [] # banner name etc.

for sid, info in flagged.items():
    issues = info['issues']
    fname = info['meta'].get('fname')
    is_dupe = any('DUPLICAD' in i for i in issues)
    is_low = any('RESOLUCION_BAJA' in i for i in issues)
    is_name = any('NOMBRE_NO_BOTANICO' in i for i in issues)
    
    if is_name and not is_dupe and not is_low:
        false_positives.append((sid, fname, issues))
    elif is_dupe:
        if fname not in dupes_group:
            dupes_group[fname] = []
        dupes_group[fname].append((sid, info['entry']['name'], info['entry']['bank'], info['meta'].get('size')))
    elif is_low:
        exclusive_low_res.append((sid, info['entry']['name'], fname, info['meta'].get('size')))

print(f"Total cepas flagged: {len(flagged)}")
print(f"\n1. Falsos positivos por nombre botánico ('Bruce Banner'): {len(false_positives)}")
for fp in false_positives:
    print(f"   {fp[0]}: {fp[1]} - {fp[2]}")

print(f"\n2. Grupos de duplicados residuales: {len(dupes_group)} grupos ({sum(len(v) for v in dupes_group.values())} cepas)")
for fname, strains in dupes_group.items():
    s_names = [f"{s[0]} ({s[1]})" for s in strains]
    print(f"   Archivo: {fname} [{strains[0][3]}] -> {len(strains)} cepas: {', '.join(s_names)}")

print(f"\n3. Cepas exclusivas con resolución baja (<600x600 px): {len(exclusive_low_res)} cepas")
for item in exclusive_low_res:
    print(f"   {item[0]} ({item[1]}): {item[2]} -> {item[3]}")
