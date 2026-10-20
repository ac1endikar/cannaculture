import re

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

for sid in ["sensi-sensi-amnesia", "ihg-terple"]:
    m = re.search(rf'id:\s*["\']{sid}["\'].*?image:\s*["\']([^"\']+)["\']', text, re.DOTALL)
    if m:
        print(f"data.js [{sid}]: {m.group(1)}")
    else:
        print(f"data.js [{sid}]: NOT FOUND")

with open("js/bundle.js", "r", encoding="utf-8") as f:
    btext = f.read()

for sid in ["sensi-sensi-amnesia", "ihg-terple"]:
    m = re.search(rf'id:\s*["\']{sid}["\'].*?image:\s*["\']([^"\']+)["\']', btext, re.DOTALL)
    if m:
        print(f"bundle.js [{sid}]: {m.group(1)}")
    else:
        print(f"bundle.js [{sid}]: NOT FOUND")
