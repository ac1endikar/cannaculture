with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'aceseeds-golden-tiger-flowering-real.jpg': 'aceseeds-golden-tiger-hd.jpg',
    'arc-rainbow-belts.jpg': 'arc-rainbow-belts-hd.jpg',
    'ripper-hawaiian-wave-bud.jpg': 'ripper-hawaiian-wave-hd.jpg',
    'sdm-mama-thai.jpg': 'sdm-mama-thai-hd.jpg',
    'ripper-haze-flowering-real.jpg': 'ripper-haze-flowering.jpg',
}

for old, new in replacements.items():
    if old in content:
        content = content.replace(f'img/{old}', f'img/{new}')
        print(f'Replaced img/{old} -> img/{new}')
    else:
        print(f'WARNING: {old} not found in data.js')

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated js/data.js successfully!')
