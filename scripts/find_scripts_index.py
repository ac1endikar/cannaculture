import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

scripts = re.findall(r'<script[^>]*>.*?</script>|<script[^>]*/>|<script[^>]*>', text, re.DOTALL)
print(f"Total script tags in index.html: {len(scripts)}")
for s in scripts:
    print("--- SCRIPT TAG ---")
    print(s[:200])
