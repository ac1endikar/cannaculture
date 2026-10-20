import os, shutil, sys

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

os.makedirs('images/strains', exist_ok=True)
os.makedirs('img', exist_ok=True)

mappings = {
    '00-kush.jpg': 'img/sensi-hindu-kush-bud.jpg',
    'chocolate-skunk.jpg': 'img/oo-super-skunk-bud-real.jpg',
    'gorilla-00.jpg': 'img/bsf-gorilla-ghost.jpg',
    'california-kush.jpg': 'img/dinafem-og-kush.jpg',
    'sweet-soma.jpg': 'img/positronics-somango-47-bud.jpg',
    'gorilla-girl.jpg': 'img/sweet-gorilla-girl.jpg',
    'san-fernando-lemon-kush.jpg': 'img/dna-kosher-kush.jpg',
    'black-jack.jpg': 'img/sweet-black-jack.jpg',
    'sweet-tai.jpg': 'img/cannabiogen-jamaica-blue-mountain-bud.jpg'
}

for target_name, src in mappings.items():
    if os.path.exists(src):
        dest_images = os.path.join('images/strains', target_name)
        dest_img = os.path.join('img', target_name)
        shutil.copy2(src, dest_images)
        shutil.copy2(src, dest_img)
        print(f"Prepared {target_name} from {src}")
    else:
        print(f"Source not found: {src}")
