import re

backups = [
    "js/data.js.backup_before_all_real_hd",
    "js/data.js.backup_final_best",
    "js/data.js.backup_phase1"
]

for b in backups:
    with open(b, 'r', encoding='utf-8') as f:
        t = f.read()
    m_s = re.search(r'id:\s*["\']sensi-sensi-amnesia["\'].*?image:\s*["\']([^"\']+)["\']', t, re.DOTALL)
    m_t = re.search(r'id:\s*["\']ihg-terple["\'].*?image:\s*["\']([^"\']+)["\']', t, re.DOTALL)
    print(f"In {b}:")
    print("  sensi-sensi-amnesia:", m_s.group(1) if m_s else "NOT FOUND")
    print("  ihg-terple:", m_t.group(1) if m_t else "NOT FOUND")
