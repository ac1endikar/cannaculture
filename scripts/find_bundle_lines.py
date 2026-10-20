import re

with open("js/bundle.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Scanning js/bundle.js for line numbers...")
for idx, line in enumerate(lines, 1):
    if any(k in line.lower() for k in ['sensi amnesia', '"terple"', 'sensi-sensi-amnesia', 'ihg-terple']):
        print(f"Line {idx}: {line.strip()}")
