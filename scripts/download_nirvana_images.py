import urllib.request
import os
import sys
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

images = [
    ("nirvana-aurora-indica", "https://nirvanashop.com/cdn/shop/files/Aurora20fem.png?v=1784572707"),
    ("nirvana-bubblelicious", "https://nirvanashop.com/cdn/shop/files/Bubblelicious_20fem.png?v=1784572749"),
    ("nirvana-master-kush", "https://nirvanashop.com/cdn/shop/files/master-kush-feminized-marijuana-seeds.png?v=1784572761"),
    ("nirvana-ak-48", "https://nirvanashop.com/cdn/shop/files/ak-48-feminized-marijuana-seeds.png?v=1784572703"),
    ("nirvana-wonder-woman", "https://nirvanashop.com/cdn/shop/files/Wonder20fem.png?v=1784572821"),
    ("nirvana-somango-xxl", "https://nirvanashop.com/cdn/shop/files/Somango20fem.png?v=1784572702"),
    ("nirvana-papaya", "https://nirvanashop.com/cdn/shop/files/Papaya_20fem.png?v=1784572816"),
    ("nirvana-hawaii-maui-waui", "https://nirvanashop.com/cdn/shop/files/Hawaii20Waui_20fem.png?v=1784572755"),
    ("nirvana-super-skunk", "https://nirvanashop.com/cdn/shop/files/Super20fem.png?v=1784572703"),
    ("nirvana-blackjack", "https://nirvanashop.com/cdn/shop/files/Black20fem.png?v=1784572707"),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

os.makedirs('img', exist_ok=True)
os.makedirs('images/strains/nirvana-seeds', exist_ok=True)

for strain_id, url in images:
    target_webp = f"img/{strain_id}.webp"
    target_backup = f"images/strains/nirvana-seeds/{strain_id}.webp"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            img = Image.open(io.BytesIO(data))
            
            # Convert RGBA to RGB with clean dark/black background if needed, or maintain transparent/webp
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                # Convert with white or dark background, but WebP supports RGBA directly
                # If transparent, let's keep RGBA for clean rendering on dark UI
                pass
            else:
                img = img.convert('RGB')
            
            # Resize to exact 800x800 if not already
            if img.size != (800, 800):
                img = img.resize((800, 800), Image.Resampling.LANCZOS)
                
            img.save(target_webp, 'WEBP', quality=92, method=6)
            img.save(target_backup, 'WEBP', quality=92, method=6)
            print(f"✅ Guardado {target_webp} ({os.path.getsize(target_webp):,} bytes)")
    except Exception as e:
        print(f"❌ Error en {strain_id} ({url}): {e}")

print("\nVerificación de archivos guardados:")
for strain_id, _ in images:
    p = f"img/{strain_id}.webp"
    print(f"  {p}: {'EXISTE' if os.path.exists(p) else 'NO EXISTE'} ({os.path.getsize(p) if os.path.exists(p) else 0:,} bytes)")
