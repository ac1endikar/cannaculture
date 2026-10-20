import re

files = [
    'd:/cannaculture/index.html',
    'd:/cannaculture/guia-cultivo.html',
    'd:/cannaculture/admin-dispensario.html',
    'd:/cannaculture/sw.js'
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('?v=226', '?v=227')
    c = c.replace('v226', 'v227')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Bumped cache to v227 in {fp}")
