import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

db_start = text.find('export const STRAINS_DATABASE = [')
db_text = text[db_start:]
chunks = re.split(r'(?=\bid\s*:\s*["\'])', db_text)

strains = []
banks = {}
species_count = {}
terpenes_count = {}
thc_values = []
cbd_values = []
flowering_values = []

for chunk in chunks:
    id_m = re.search(r'\bid\s*:\s*["\']([^"\']+)["\']', chunk)
    name_m = re.search(r'\bname\s*:\s*["\']([^"\']+)["\']', chunk)
    bank_m = re.search(r'\bbank\s*:\s*["\']([^"\']+)["\']', chunk)
    spec_m = re.search(r'\bspecies\s*:\s*["\']([^"\']+)["\']', chunk)
    thc_m = re.search(r'\bthc\s*:\s*([0-9.]+)', chunk)
    cbd_m = re.search(r'\bcbd\s*:\s*([0-9.]+)', chunk)
    flow_m = re.search(r'\bfloweringDays\s*:\s*([0-9]+)', chunk)
    terp_m = re.search(r'\bdominantTerpene\s*:\s*["\']([^"\']+)["\']', chunk)

    if id_m:
        sid = id_m.group(1)
        sname = name_m.group(1) if name_m else sid
        sbank = bank_m.group(1) if bank_m else 'Desconocido'
        sspec = spec_m.group(1) if spec_m else 'Híbrida'
        sterp = terp_m.group(1) if terp_m else 'desconocido'

        strains.append({
            'id': sid,
            'name': sname,
            'bank': sbank,
            'species': sspec,
            'terpene': sterp
        })

        banks[sbank] = banks.get(sbank, [])
        banks[sbank].append(sname)

        species_count[sspec] = species_count.get(sspec, 0) + 1
        terpenes_count[sterp] = terpenes_count.get(sterp, 0) + 1

        if thc_m:
            thc_values.append(float(thc_m.group(1)))
        if cbd_m:
            cbd_values.append(float(cbd_m.group(1)))
        if flow_m:
            flowering_values.append(int(flow_m.group(1)))

print("="*60)
print(f"AUDITORÍA COMPLETA DE CANNACATALOG (js/data.js)")
print("="*60)
print(f"Total cepas catalogadas: {len(strains)}")
print(f"Total bancos registrados: {len(banks)}")
print(f"THC Promedio: {sum(thc_values)/len(thc_values):.1f}% (Min: {min(thc_values)}%, Max: {max(thc_values)}%)")
print(f"Floración Promedio: {sum(flowering_values)/len(flowering_values):.0f} días")
print("\n--- Distribución por Especie ---")
for sp, c in sorted(species_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {sp:10}: {c:3d} cepas ({c/len(strains)*100:.1f}%)")

print("\n--- Terpenos Dominantes ---")
for t, c in sorted(terpenes_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {t:15}: {c:3d} cepas ({c/len(strains)*100:.1f}%)")

print("\n--- Ranking Completo de Bancos por Número de Cepas ---")
sorted_banks = sorted(banks.items(), key=lambda x: len(x[1]), reverse=True)
for i, (b, s_list) in enumerate(sorted_banks, 1):
    print(f"{i:2d}. {b:<25}: {len(s_list):2d} cepas | Ejemplos: {', '.join(s_list[:3])}")

print("\n" + "="*60)
print("DETALLE DE BANCOS CANDIDATOS A EXPANSIÓN (CEPAS ACTUALES)")
print("="*60)
target_banks = [
    'Nirvana Seeds',
    'Dutch Passion',
    'Humboldt Seed',
    'Buddha Seeds',
    'Philosopher Seeds',
    'Sensi Seeds',
    'Green House Seed Co.',
    'Serious Seeds',
    'Barney',
    'Royal Queen Seeds',
    'ACE Seeds',
    'Cannabiogen'
]
for tb in target_banks:
    strains_in_bank = banks.get(tb, [])
    print(f"\n--- {tb} ({len(strains_in_bank)} cepas actuales) ---")
    for s in sorted(strains_in_bank):
        print(f"  • {s}")
