import re

with open("js/bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

# Find all occurrences of STRAINS_DATABASE
db_matches = re.findall(r'(?:export\s+)?const\s+STRAINS_DATABASE\s*=\s*\[', text)
print(f"STRAINS_DATABASE declarations in bundle.js: {len(db_matches)}")

# Find all strain ids in bundle.js
ids = re.findall(r'\bid:\s*["\']([^"\']+)["\']', text)
print(f"Total strain IDs in bundle.js: {len(ids)}")

dupes = set([x for x in ids if ids.count(x) > 1])
print(f"Duplicate IDs in bundle.js: {dupes}")

# Check where sensi-sensi-amnesia and ihg-terple appear
for sid in ["sensi-sensi-amnesia", "ihg-terple"]:
    occurrences = [m.start() for m in re.finditer(rf'\bid:\s*["\']{re.escape(sid)}["\']', text)]
    print(f"ID '{sid}' appears {len(occurrences)} times at indices {occurrences}")
