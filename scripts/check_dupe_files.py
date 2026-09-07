import os
import json

data = json.load(open('scratch/visual_audit_report.json', encoding='utf-8'))
flagged = data['flagged_strains']

img_files = os.listdir(r'd:\cannaculture\img')
img_files_lower = {f.lower(): f for f in img_files}

print("=== VERIFICACIÓN DE ARCHIVOS EXISTENTES EN IMG/ PARA LAS 48 CEPAS DUPLICADAS ===")

dupe_strains = []
for sid, info in flagged.items():
    if any('DUPLICAD' in i for i in info['issues']):
        dupe_strains.append(sid)

for sid in dupe_strains:
    matches = [f for f in img_files if sid in f]
    print(f"{sid}: matches in img/ -> {matches}")
