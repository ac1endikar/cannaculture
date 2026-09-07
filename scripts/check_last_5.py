import json

d = json.load(open('scratch/visual_audit_report.json', encoding='utf-8'))
for c in d['white_backgrounds']:
    print(f"{c['id']}: {c['file']} - {c['detail']}")
