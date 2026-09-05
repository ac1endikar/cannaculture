#!/usr/bin/env python3
"""
Corrige en data.js:
1. Paths rotos (con ?v=... en URLs locales)
2. Imágenes duplicadas incorrectas (segunda cepa usando foto de otra)
3. Actualiza paths cuando se descargan nuevas fotos
"""
import re
import sys
import os
import shutil

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# 1. Corrige paths rotos (quita query params de rutas locales)
# ripper-sideral-user.jpg?v=user_sideral_v1 -> ripper-sideral.jpg
content = content.replace(
    '"img/ripper-sideral-user.jpg?v=user_sideral_v1"',
    '"img/ripper-sideral.jpg"'
)
content = content.replace(
    '"img/ripper-jungle-punch-user.jpg?v=user_jungle_v1"',
    '"img/ripper-jungle-punch.jpg"'
)

# 2. Corrige imágenes duplicadas - da imagen propia a cada cepa
# El formato es: busca el bloque del strain por su ID y cambia su image

def fix_strain_image(content, strain_id, new_image_path):
    """Cambia la imagen de una cepa específica buscando por su ID."""
    # Busca el patrón: id: "strain_id" seguido eventualmente de image: "..."
    # Necesitamos ser cuidadosos de no cambiar el primer strain si comparten imagen
    
    # Patrón: encuentra el bloque que contiene este id y cambia su imagen
    pattern = r'(id:\s*"' + re.escape(strain_id) + r'"[^}]{0,500}?)(image:\s*")([^"]+)(")'
    replacement = r'\g<1>\g<2>' + new_image_path + r'\g<4>'
    
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
    if new_content == content:
        sys.stdout.write('  WARN: No se pudo cambiar imagen de %s\n' % strain_id)
    else:
        sys.stdout.write('  OK: %s -> %s\n' % (strain_id, new_image_path))
    return new_content


# Mapa de correcciones: strain_id -> nueva ruta de imagen
CORRECTIONS = {
    # Ripper Seeds - duplicados
    'ripper-pink-rozay': 'img/ripper-pink-rozay.jpg',
    'ripper-zombie-wash': 'img/ripper-zombie-wash.jpg',
    'ripper-candy-crack': 'img/ripper-candy-crack.jpg',
    'ripper-fuel-og': 'img/ripper-fuel-og.jpg',
    'ripper-juicy-zkittlez': 'img/ripper-juicy-zkittlez.jpg',
    
    # Barney's Farm - duplicados
    'bf-zkittlez-og': 'img/bf-zkittlez-og.jpg',
    'bf-wedding-cake': 'img/bf-wedding-cake.jpg',
    'bf-pineapple-chunk': 'img/bf-pineapple-chunk.jpg',
    'bf-acapulco-gold': 'img/bf-acapulco-gold.jpg',
    'bf-lsd': 'img/bf-lsd.jpg',
    
    # Sweet Seeds - duplicados
    'ss-bigdevil-xl': 'img/sweet-big-devil-xl.jpg',
    'ss-crystal-candy': 'img/sweet-crystal-candy.jpg',
    'ss-red-hot-cookies': 'img/sweet-red-hot-cookies.jpg',
    'ss-black-cream-auto': 'img/sweet-black-cream-auto.jpg',
    'ss-sweet-amnesia-haze': 'img/sweet-amnesia-haze.jpg',
    
    # Royal Queen Seeds - duplicados
    'rqs-purple-queen': 'img/rqs-purple-queen.jpg',
    'rqs-og-kush-auto': 'img/rqs-og-kush-auto.jpg',
    'rqs-blue-mystic': 'img/rqs-blue-mystic.jpg',
    'rqs-watermelon': 'img/rqs-watermelon.jpg',
    'rqs-honey-cream': 'img/rqs-honey-cream.jpg',
    
    # Dutch Passion - duplicados
    'dp-auto-mazar': 'img/dp-auto-mazar.jpg',
    'dp-mazar': 'img/dp-mazar.jpg',
    'dp-frisian-dew': 'img/dp-frisian-dew.jpg',
    'dp-skywalker-og': 'img/dp-skywalker-og.jpg',
    
    # Philosopher Seeds - duplicados
    'phil-lemon-og-candy': 'img/philo-lemon-og-candy.jpg',
    'phil-snow-storm': 'img/philo-snow-storm.jpg',
    'phil-critical-sensi-star': 'img/philo-critical-sensi-star.jpg',
    'phil-bubbas-gift': 'img/philo-bubbas-gift.jpg',
    
    # 00 Seeds Bank - duplicados
    '00s-white-smurf': 'img/00s-white-smurf.jpg',
    '00s-critical-mass': 'img/00s-critical-mass.jpg',
    '00s-cheese-xl': 'img/00s-cheese-xl.jpg',
}

sys.stdout.write('Aplicando correcciones a data.js...\n\n')

# Aplica todas las correcciones
for strain_id, new_img in CORRECTIONS.items():
    # Solo cambia si la imagen nueva existe (fue descargada) o si es un fix de path
    fname = new_img.replace('img/', '')
    img_exists = os.path.exists(os.path.join(IMG_DIR, fname))
    
    if img_exists:
        content = fix_strain_image(content, strain_id, new_img)
    else:
        # Aun asi cambia el path para que apunte al futuro archivo
        content = fix_strain_image(content, strain_id, new_img)
        sys.stdout.write('    (imagen aun no descargada, path actualizado)\n')

# Guarda backup
backup_path = DATA_JS + '.backup_phase1'
if not os.path.exists(backup_path):
    shutil.copy2(DATA_JS, backup_path)
    sys.stdout.write('\nBackup guardado: %s\n' % backup_path)

# Guarda cambios
with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(content)

# Cuenta cambios
changes = sum(1 for a, b in zip(original, content) if a != b)
sys.stdout.write('\ndata.js actualizado. Cambios realizados: ~%d caracteres modificados\n' % changes)
sys.stdout.write('Total correcciones aplicadas: %d\n' % len(CORRECTIONS))
