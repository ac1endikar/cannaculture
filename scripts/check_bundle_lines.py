import re

with open('js/bundle.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_section = 'header'
section_counts = {}
extra_ids = []
for i, line in enumerate(lines):
    if line.startswith('// --- '):
        current_section = line.strip()
    m = re.search(r'id:\s*["\']([^"\']+)["\']', line)
    if m:
        val = m.group(1)
        section_counts[current_section] = section_counts.get(current_section, 0) + 1
        if current_section != '// --- data.js ---':
            extra_ids.append((current_section, i+1, val))

for sec, count in section_counts.items():
    print(f"{sec}: {count}")

print(f"\nExtra IDs outside data.js ({len(extra_ids)}):")
for sec, line_no, val in extra_ids:
    print(f"  [{sec}] L{line_no}: id = '{val}'")
