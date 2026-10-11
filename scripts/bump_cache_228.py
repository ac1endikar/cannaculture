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
    c = c.replace('?v=227', '?v=228')
    c = c.replace('v227', 'v228')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Bumped cache to v228 in {fp}")
