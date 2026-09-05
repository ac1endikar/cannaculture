#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'\{\s*id:\s*["\'][^"\']*guanabana[^"\']*["\'].*?\n  \},?', text, re.DOTALL | re.IGNORECASE)
if m:
    print(m.group(0))
else:
    for i, line in enumerate(text.splitlines(), 1):
        if 'guanabana' in line.lower():
            print(f"Line {i}: {line}")
