import sys, re, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Update image paths in data.js for Blue Dream and Sapphire OG
replacements = {
    'id: "hso-blue-dream",\n    image: "img/hso-blue-dream.jpg"': 'id: "hso-blue-dream",\n    image: "img/hso-blue-dream-official.jpg"',
    'id: "hso-sapphire-og",\n    image: "img/hso-blue-dream.jpg"': 'id: "hso-sapphire-og",\n    image: "img/hso-sapphire-og-official.jpg"',
    'id: "hso-sapphire-og",\n    image: "img/hso-sapphire-og.jpg"': 'id: "hso-sapphire-og",\n    image: "img/hso-sapphire-og-official.jpg"',
    'id: "hso-liberty-haze",\n    image: "img/hso-girl-scout-cookies.jpg"': 'id: "hso-liberty-haze",\n    image: "img/hso-liberty-haze.jpg"',
    'id: "hso-707-headband",\n    image: "img/hso-trainwreck.jpg"': 'id: "hso-707-headband",\n    image: "img/hso-707-headband.jpg"',
    'id: "hso-blue-fire",\n    image: "img/hso-og-eddy-lepp.jpg"': 'id: "hso-blue-fire",\n    image: "img/hso-blue-fire.jpg"'
}

changes = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changes += 1

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Updated {changes} image paths in data.js for Humboldt strains")

# Re-inspect all Humboldt strains
strains_part = text[text.find("export const STRAINS_DATABASE = ["):]
blocks = strains_part.split('\n  {\n')

for b in blocks:
    m_id = re.search(r'id:\s*["\']([^"\']+)["\']', b)
    m_name = re.search(r'name:\s*["\']([^"\']+)["\']', b)
    m_img = re.search(r'image:\s*["\']([^"\']+)["\']', b)
    m_bank = re.search(r'bank:\s*["\']([^"\']+)["\']', b)
    if m_id and m_bank and 'Humboldt' in m_bank.group(1):
        print(f"  Strain: {m_name.group(1):25s} | ID: {m_id.group(1):20s} | Image: {m_img.group(1)}")
