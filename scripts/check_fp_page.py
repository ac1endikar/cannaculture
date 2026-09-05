#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import re

url = 'https://florprohibida.com/semillas-marihuana-feminizadas/guanabana-blimburn-seeds.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://florprohibida\.com/[^"\'\s>]+\.jpg', html)
    print('Found imgs on page:')
    for u in set(imgs):
        if 'guanabana' in u:
            print(" ->", u)
except Exception as e:
    print('Error:', e)
