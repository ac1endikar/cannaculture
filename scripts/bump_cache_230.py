import re

files_to_update = [
    'admin-dispensario.html',
    'sw.js',
    'index.html',
    'guia-cultivo.html'
]

for filename in files_to_update:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('?v=229', '?v=230')
    new_content = new_content.replace('cannaculture-core-v229', 'cannaculture-core-v230')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated {filename}")
