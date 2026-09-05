#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

r = requests.get('https://eurogrow.es/buscar?controller=search&s=guanabana', headers=headers, timeout=10)
print("Eurogrow status:", r.status_code)
imgs = re.findall(r'https://eurogrow\.es/[^"\'\s>]+\.jpg', r.text)
print("Eurogrow imgs:", len(imgs))
for img in set(imgs):
    print(" ->", img)
