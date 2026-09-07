import re

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

strains = re.findall(r'id:\s*["\']([^"\']+)["\']', text)
print(f"Total strains in data.js: {len(strains)}")

sensi_idx = None
terple_idx = None

for i, s in enumerate(strains):
    if s == "sensi-sensi-amnesia": sensi_idx = i
    if s == "ihg-terple": terple_idx = i

print(f"sensi-sensi-amnesia index: {sensi_idx}")
print(f"ihg-terple index: {terple_idx}")
