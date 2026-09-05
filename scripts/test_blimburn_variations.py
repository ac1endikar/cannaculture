#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from PIL import Image
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

patterns = [
    'Guanabana.webp',
    'Guanabana-1.webp',
    'Guanabana-2.webp',
    'Guanabana-3.webp',
    'Guanabana-4.webp',
    'guanabana.webp',
    'guanabana-1.webp',
    'guanabana-2.webp',
    'guanabana-3.webp',
    'GUANABANA.webp',
    'guanabana_1.webp',
    'guanabana_2.webp',
    'Guanabana-1024x768.jpeg.webp',
    'guanabana-1024x768.jpeg.webp',
    'Guanabana-1024x768.jpg.webp',
    'Guanabana-1024x768.webp',
    'Guanabana-800x800.webp',
    'Guanabana-scaled.webp',
    'Guanabana-scaled.jpg',
    'Guanabana.jpg',
    'Guanabana-2.jpg',
    'Guanabana-1024x768.jpeg',
    'Guanabana-1024x768.jpg'
]

base_2021 = 'https://blimburnseeds.com/wp-content/uploads/2021/04/'
base_2025 = 'https://blimburnseeds.es/wp-content/uploads/2025/09/'

for base in [base_2021, base_2025]:
    for p in patterns:
        u = base + p
        try:
            r = requests.get(u, headers=headers, timeout=5)
            if r.status_code == 200 and len(r.content) > 10000:
                print(f"FOUND: {u} ({len(r.content)} bytes)")
                dest = f"d:/cannaculture/scratch/guanabana/blim_{p}"
                with open(dest, 'wb') as f:
                    f.write(r.content)
                with Image.open(dest) as im:
                    print(f"  Dimensions: {im.size}, Mode: {im.mode}")
        except Exception as e:
            pass
