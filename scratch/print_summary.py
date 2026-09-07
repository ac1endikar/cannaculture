import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/visual_audit_report.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== 1. IMAGENES REUTILIZADAS / DUPLICADAS (PLACEHOLDERS DE BANCO) ===")
dupes_by_file = {}
for item in d['non_cannabis_or_dupes']:
    f = item['file']
    if f not in dupes_by_file:
        dupes_by_file[f] = []
    dupes_by_file[f].append(f"{item['bank']} - {item['name']} ({item['id']})")

for f, strains in sorted(dupes_by_file.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"\n[Archivo: img/{f}] -> Usado en {len(strains)} cepas:")
    for s in strains:
        print(f"   * {s}")

print("\n" + "=" * 80)
print(f"=== 2. FONDOS BLANCOS PLANOS ({len(d['white_backgrounds'])} cepas) ===")
print("=" * 80)
for item in d['white_backgrounds'][:15]:
    print(f"* [{item['bank']}] {item['name']} (ID: {item['id']}) -> {item['file']} ({item['detail']})")
if len(d['white_backgrounds']) > 15:
    print(f"... y {len(d['white_backgrounds']) - 15} más.")

print("\n" + "=" * 80)
print(f"=== 3. RESOLUCIÓN DEGRADADA (< 600x600 px) ({len(d['low_resolutions'])} cepas) ===")
print("=" * 80)
for item in d['low_resolutions'][:15]:
    print(f"* [{item['bank']}] {item['name']} (ID: {item['id']}) -> {item['file']} ({item['detail']})")
if len(d['low_resolutions']) > 15:
    print(f"... y {len(d['low_resolutions']) - 15} más.")

print("\n" + "=" * 80)
print(f"=== 4. RATIOS ANÓMALOS (BANNERS / TIRAS VERTICALES) ({len(d['ratio_skewed'])} cepas) ===")
print("=" * 80)
for item in d['ratio_skewed']:
    print(f"* [{item['bank']}] {item['name']} (ID: {item['id']}) -> {item['file']} ({item['detail']})")
