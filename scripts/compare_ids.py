import re

with open("js/data.js", "r", encoding="utf-8") as f:
    d_ids = re.findall(r'\bid:\s*["\']([^"\']+)["\']', f.read())

with open("js/bundle.js", "r", encoding="utf-8") as f:
    b_ids = re.findall(r'\bid:\s*["\']([^"\']+)["\']', f.read())

print(f"data.js IDs: {len(d_ids)}")
print(f"bundle.js IDs: {len(b_ids)}")

diff = set(b_ids) - set(d_ids)
print("IDs in bundle.js but not in data.js:", diff)
