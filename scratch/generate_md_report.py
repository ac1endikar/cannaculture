import json

with open('scratch/visual_audit_report.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

md = []
md.append("# Reporte de Auditoría Visual - CannaCulture")
md.append(f"- **Total genéticas en catálogo:** {d['total_strains']}")
md.append(f"- **Conformes con estándar botánico HD:** {d['total_strains'] - d['total_flagged']}")
md.append(f"- **Genéticas con no-conformidad:** {d['total_flagged']}\n")

md.append("## 1. Imágenes Reutilizadas / Placeholders Copiados (105 cepas afectadas)")
md.append("Estas genéticas comparten el mismo archivo de imagen con otras cepas, siendo placeholders genéricos en vez de fotos botánicas específicas de la variedad:\n")

dupes = {}
for item in d['non_cannabis_or_dupes']:
    f = item['file']
    dupes.setdefault(f, []).append(item)

for f, items in sorted(dupes.items(), key=lambda x: len(x[1]), reverse=True):
    md.append(f"### `img/{f}` (usado en {len(items)} cepas):")
    for it in items:
        md.append(f"- **[{it['bank']}] {it['name']}** (`{it['id']}`)")
    md.append("")

md.append("## 2. Fondos Blancos Planos / Packshots de Estudio Claro (92 cepas)")
md.append("Imágenes con bordes blancos intensos (>40%) o luminosidad media excesiva que rompen con la estética dark glassmorphism:\n")
md.append("| Banco | Cepa | ID | Archivo | Detalle |")
md.append("| :--- | :--- | :--- | :--- | :--- |")
for it in d['white_backgrounds']:
    md.append(f"| {it['bank']} | {it['name']} | `{it['id']}` | `{it['file']}` | {it['detail']} |")

md.append("\n## 3. Ratios Anómalos (Banners y Tiras Verticales) (14 cepas)")
md.append("| Banco | Cepa | ID | Archivo | Detalle |")
md.append("| :--- | :--- | :--- | :--- | :--- |")
for it in d['ratio_skewed']:
    md.append(f"| {it['bank']} | {it['name']} | `{it['id']}` | `{it['file']}` | {it['detail']} |")

md.append("\n## 4. Resolución Degradada (< 600x600 px) (119 cepas)")
md.append("| Banco | Cepa | ID | Archivo | Detalle |")
md.append("| :--- | :--- | :--- | :--- | :--- |")
for it in d['low_resolutions']:
    md.append(f"| {it['bank']} | {it['name']} | `{it['id']}` | `{it['file']}` | {it['detail']} |")

report_content = "\n".join(md)
with open('scratch/reporte_auditoria_visual.md', 'w', encoding='utf-8') as f:
    f.write(report_content)

print(f"Reporte MD generado con éxito ({len(report_content)} caracteres).")
