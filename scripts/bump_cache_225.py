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
    c = c.replace('?v=224', '?v=225')
    c = c.replace('v224', 'v225')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Bumped cache in {fp}")
