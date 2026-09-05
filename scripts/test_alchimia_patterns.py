#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

al_patterns = [
    'https://www.alchimiaweb.com/images/xl/1632_1_.jpg',
    'https://www.alchimiaweb.com/images/xl/1632_2_.jpg',
    'https://www.alchimiaweb.com/images/xl/1632_3_.jpg',
    'https://www.alchimiaweb.com/images/big/1632_1_.jpg',
    'https://www.alchimiaweb.com/images/big/1632_2_.jpg',
    'https://www.alchimiaweb.com/images/xl/guanabana_1632_1_.jpg',
    'https://www.alchimiaweb.com/images/xl/guanabana-blimburn-seeds_1632_1_.jpg',
    'https://www.alchimiaweb.com/images/big/guanabana_1632_1_.jpg',
    'https://www.alchimiaweb.com/images/xl/guanabana_1_.jpg',
    'https://www.alchimiaweb.com/images/xl/guanabana.jpg',
    'https://www.alchimiaweb.com/images/big/guanabana.jpg',
    'https://www.alchimiaweb.com/images/product/1632.jpg'
]

for u in al_patterns:
    try:
        r = requests.head(u, headers=headers, timeout=4)
        if r.status_code == 200:
            print("Found Alchimia image:", u, r.headers.get('Content-Length'))
    except:
        pass
