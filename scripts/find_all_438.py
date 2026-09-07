import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    if '.git' in dirs: dirs.remove('.git')
    if 'scratch' in dirs: dirs.remove('scratch')
    for f in files:
        if f.endswith(('.html', '.js', '.md')) and not f.endswith(('.bak', '.backup')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for line_no, line in enumerate(fp, 1):
                    if '438' in line:
                        print(f"{p}:{line_no}: {line.strip()[:100]}")
