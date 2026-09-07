import re
import subprocess

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

ids = re.findall(r'id:\s*["\']([^"\']+)["\']', content)
print(f"Total strain IDs in js/data.js: {len(ids)}")
print(f"Contains 'sensi-sensi-amnesia': {'sensi-sensi-amnesia' in ids}")
print(f"Contains 'ihg-terple': {'ihg-terple' in ids}")

# Run node --check to verify valid JavaScript syntax
try:
    res = subprocess.run(['node', '--check', 'js/data.js'], capture_output=True, text=True)
    if res.returncode == 0:
        print("js/data.js syntax is VALID!")
    else:
        print("js/data.js syntax error:", res.stderr)
except Exception as e:
    print("Node check skipped or error:", e)
