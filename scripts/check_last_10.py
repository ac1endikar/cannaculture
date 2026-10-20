import json

data = json.load(open('scratch/visual_audit_report.json', encoding='utf-8'))
flagged = data['flagged_strains']

print(f"Total cepas con no conformidad: {len(flagged)}\n")
for sid, info in flagged.items():
    print(f"ID: {sid} ({info['entry']['name']})")
    print(f"  Archivo: {info['meta'].get('fname')}")
    print(f"  Issues: {info['issues']}")
    print()
