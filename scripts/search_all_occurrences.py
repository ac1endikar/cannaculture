import os
import re

search_terms = ["sensi-sensi-amnesia", "ihg-terple", "sensi amnesia", "terple"]

for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root or "__pycache__" in root:
        continue
    for fname in files:
        if fname.endswith(('.js', '.html', '.json', '.ts')):
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for term in search_terms:
                    if term in content.lower():
                        matches = [line.strip() for line in content.splitlines() if term in line.lower()]
                        print(f"File {path} matches '{term}':")
                        for m in matches[:3]:
                            print(f"  {m[:120]}")
                        break
