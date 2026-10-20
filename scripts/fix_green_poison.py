from PIL import Image
import os

src = r"d:\cannaculture\img\sweet-green-poison-bud.jpg"
im = Image.open(src)
im_600 = im.resize((600, 600), Image.Resampling.LANCZOS)
im_600.save(src, 'JPEG', quality=95, optimize=True)

# Actualizar data.js para que apunte a sweet-green-poison-bud.jpg en vez de sweet-green-poison-plant.jpg
data_js = r"d:\cannaculture\js\data.js"
with open(data_js, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('"sweet-green-poison-plant.jpg"', '"sweet-green-poison-bud.jpg"')
text = text.replace('sweet-green-poison-plant.jpg', 'sweet-green-poison-bud.jpg')

with open(data_js, 'w', encoding='utf-8') as f:
    f.write(text)

print("Arreglado sweet-green-poison -> sweet-green-poison-bud.jpg a 600x600 px")
