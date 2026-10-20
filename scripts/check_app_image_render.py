import re

with open("js/app.js", "r", encoding="utf-8") as f:
    text = f.read()

for line_no, line in enumerate(text.splitlines(), 1):
    if "strain.image" in line or "card-image" in line or "image" in line:
        if any(k in line for k in ["<img", "src=", "image", "background"]):
            print(f"L{line_no}: {line.strip()[:100]}")
