#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m1 = re.search(r'\{\s*id:\s*["\']ripper-ripper-haze["\'].*?\n  \},?', text, re.DOTALL)
m2 = re.search(r'\{\s*id:\s*["\']ripper-haze["\'].*?\n  \},?', text, re.DOTALL)

print("=== RIPPER-RIPPER-HAZE ===")
if m1:
    print(m1.group(0))

print("\n=== RIPPER-HAZE ===")
if m2:
    print(m2.group(0))
