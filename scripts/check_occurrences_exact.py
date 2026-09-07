import os
import re

files_to_check = ['index.html']
for root, dirs, files in os.walk('js'):
    for f in files:
        if f.endswith('.js'):
            files_to_check.append(os.path.join(root, f))

for fpath in files_to_check:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        for target in ['sensi-sensi-amnesia', 'sensi amnesia', 'ihg-terple', 'terple']:
            if target in content.lower():
                matches = [l.strip() for l in content.splitlines() if target in l.lower()]
                print(f"File {fpath} matches '{target}' ({len(matches)} matches):")
                for m in matches[:5]:
                    print(f"  {m[:100]}")
