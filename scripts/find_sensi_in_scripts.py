import os
import re

for fname in os.listdir('scripts'):
    if fname.endswith('.py'):
        path = os.path.join('scripts', fname)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if 'sensi-amnesia' in content or 'sensi_amnesia' in content:
                print(f"Found in {fname}:")
                for line in content.splitlines():
                    if 'amnesia' in line.lower() and ('http' in line or 'img' in line or 'bucket' in line):
                        print("  ", line.strip())
