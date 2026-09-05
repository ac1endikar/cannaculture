import sys, re, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'id: "ths-sage-n-sour",\n    image: "img/ripper-ripper-haze.jpg"': 'id: "ths-sage-n-sour",\n    image: "img/ths-sage-n-sour.jpg"',
    'id: "ths-mk-ultra",\n    image: "img/ths-mk-ultra-official.jpg"': 'id: "ths-mk-ultra",\n    image: "img/ths-mk-ultra.jpg"',
    'id: "ths-darkstar",\n    image: "img/ths-darkstar-official.jpg"': 'id: "ths-darkstar",\n    image: "img/ths-darkstar.jpg"',
    'id: "ths-heavy-d",\n    image: "img/ths-heavy-d-official.jpg"': 'id: "ths-heavy-d",\n    image: "img/ths-heavy-d.jpg"',
    'id: "ths-kushage",\n    image: "img/ths-kushage-official.jpg"': 'id: "ths-kushage",\n    image: "img/ths-kushage.jpg"',
    'id: "ths-mendocino-madness",\n    image: "img/ripper-hawaiian-wave.jpg"': 'id: "ths-mendocino-madness",\n    image: "img/ths-mendocino-madness.jpg"',
    'id: "ths-burmese-kush",\n    image: "img/ripper-candygaz.jpg"': 'id: "ths-burmese-kush",\n    image: "img/ths-burmese-kush.jpg"',
    'id: "ths-sage-n-sour-hybrid",\n    image: "img/ripper-sour-ripper.jpg"': 'id: "ths-sage-n-sour-hybrid",\n    image: "img/ths-sage-n-sour-hybrid.jpg"',
}

updated_text = text
changes = 0
for old, new in replacements.items():
    if old in updated_text:
        updated_text = updated_text.replace(old, new)
        changes += 1
        print(f"✅ Updated {old.splitlines()[0]}")
    else:
        print(f"⚠️ Target not found exact match for {old.splitlines()[0]}")

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"\nSaved {changes} updates to data.js")
