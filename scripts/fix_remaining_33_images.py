"""
Fix the remaining 33 low-quality images in data.js.
Phase A: Swap paths in data.js to use existing HD files already on disk.
"""
import re, os

DATA_JS = os.path.join(os.path.dirname(__file__), '..', 'js', 'data.js')
IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'img')

# Mapping: current low-quality file -> better HD file already on disk
SWAPS = {
    # CRITICAL (<30KB)
    'ghs-super-silver-haze-flowering-real.jpg': None,  # No HD on disk - needs download
    'rqs-og-kush-auto-flowering-real.jpg': 'rqs-og-kush-auto.jpg',  # 149KB

    # LOW QUALITY (30-65KB) - HD available on disk
    'cpg-gastro-pop-flowering-real.jpg': 'cpg-gastro-pop.jpg',  # 284KB
    'aceseeds-golden-tiger-flowering-real.jpg': None,  # No HD - needs download
    'arc-rainbow-belts.jpg': None,  # No HD - needs download
    'aceseeds-zamaldelica-official.jpg': 'aceseeds-zamaldelica-bud.jpg',  # 70KB
    'ripper-hawaiian-wave-bud.jpg': None,  # No HD - needs download
    'dp-mazar-flowering-real.jpg': 'dp-mazar.jpg',  # 125KB
    'ripper-ripper-haze-flowering-real.jpg': 'ripper-haze-flowering.jpg',  # 276KB
    'ghs-bubba-kush-flowering-real.jpg': 'ghs-bubba-kush-bud.jpg',  # 74KB
    'ripper-zombie-kush-flowering-real.jpg': 'ripper-zombie-kush-flowering.jpg',  # 1172KB!
    'dp-frisian-dew-flowering-real.jpg': 'dp-frisian-dew.jpg',  # 140KB
    'dna-strawberry-banana-flowering-real.jpg': 'dna-strawberry-banana.jpg',  # 327KB
    'positronics-claustrum-flowering-real.jpg': 'positronics-claustrum-bud.jpg',  # 78KB
    'ths-melonsicle-flowering-real.jpg': 'ths-melonsicle.jpg',  # 95KB
    'rqs-royal-gorilla-flowering-real.jpg': 'rqs-royal-gorilla-bud.jpg',  # 264KB
    'bsf-orange-blossom-flowering-real.jpg': 'bsf-orange-blossom.jpg',  # 297KB
    'ths-french-macaron-flowering-real.jpg': 'ths-french-macaron.jpg',  # 85KB
    'bf-runtz-muffin-flowering-real.jpg': 'bf-runtz-muffin.jpg',  # 431KB
    'eth-grandpas-cookies-flowering-real.jpg': 'eth-grandpas-cookies.jpg',  # 412KB
    'eth-colin-og-flowering-real.jpg': 'eth-colin-og.jpg',  # 409KB
    'cpg-red-bullz-flowering-real.jpg': 'cpg-red-bullz.jpg',  # 204KB
    'sensi-jack-herer-flowering-real.jpg': 'sensi-jack-herer-bud.jpg',  # 940KB
    'aceseeds-purple-haze-x-malawi-flowering-real.jpg': 'aceseeds-purple-haze-x-malawi-bud.jpg',  # 73KB
    'bf-mimosa-orange-punch-flowering-real.jpg': 'bf-mimosa-orange-punch-bud.jpg',  # 297KB
    'sensi-super-skunk-flowering-real.jpg': 'sensi-super-skunk-bud.jpg',  # 644KB
    'serious-serious-6-flowering-real.jpg': None,  # No HD - needs download
    'sdm-mama-thai.jpg': None,  # No HD - needs download
    'dna-3peat-flowering-real.jpg': 'dna-3peat.jpg',  # 81KB
    'serious-bubble-gum-flowering-real.jpg': 'serious-bubble-gum-bud.jpg',  # 252KB
    'cpg-high-society-flowering-real.jpg': 'cpg-high-society.jpg',  # 2263KB
    'ghs-super-lemon-haze-flowering-real.jpg': None,  # No HD - needs download
}

def main():
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    swapped = 0
    skipped = 0
    needs_download = []

    for old_file, new_file in SWAPS.items():
        if new_file is None:
            needs_download.append(old_file)
            skipped += 1
            continue

        # Verify the new file exists and is larger
        new_path = os.path.join(IMG_DIR, new_file)
        old_path = os.path.join(IMG_DIR, old_file)
        if not os.path.exists(new_path):
            print(f"  [SKIP] {new_file} not found on disk!")
            skipped += 1
            continue

        new_size = os.path.getsize(new_path)
        old_size = os.path.getsize(old_path) if os.path.exists(old_path) else 0

        if new_size <= old_size:
            print(f"  [SKIP] {new_file} ({new_size//1024}KB) not larger than {old_file} ({old_size//1024}KB)")
            skipped += 1
            continue

        # Replace in data.js
        old_ref = f'img/{old_file}'
        new_ref = f'img/{new_file}'

        if old_ref in content:
            content = content.replace(old_ref, new_ref)
            print(f"  [SWAP] {old_file} ({old_size//1024}KB) -> {new_file} ({new_size//1024}KB)")
            swapped += 1
        else:
            print(f"  [NOT FOUND] '{old_ref}' not in data.js")
            skipped += 1

    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n{'='*60}")
    print(f"RESULT: {swapped} swapped, {skipped} skipped")
    print(f"\nNeeds download ({len(needs_download)}):")
    for f in needs_download:
        print(f"  - {f}")

if __name__ == '__main__':
    main()
