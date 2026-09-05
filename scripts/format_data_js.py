import sys, re, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Normalize quoted keys to unquoted JS keys for consistency with original database style
text = re.sub(r'\"id\":', 'id:', text)
text = re.sub(r'\"image\":', 'image:', text)
text = re.sub(r'\"name\":', 'name:', text)
text = re.sub(r'\"aka\":', 'aka:', text)
text = re.sub(r'\"bank\":', 'bank:', text)
text = re.sub(r'\"species\":', 'species:', text)
text = re.sub(r'\"thc\":', 'thc:', text)
text = re.sub(r'\"cbd\":', 'cbd:', text)
text = re.sub(r'\"yieldIndoor\":', 'yieldIndoor:', text)
text = re.sub(r'\"yieldOutdoor\":', 'yieldOutdoor:', text)
text = re.sub(r'\"floweringDays\":', 'floweringDays:', text)
text = re.sub(r'\"rating\":', 'rating:', text)
text = re.sub(r'\"reviewsCount\":', 'reviewsCount:', text)
text = re.sub(r'\"genetics\":', 'genetics:', text)
text = re.sub(r'\"origin\":', 'origin:', text)
text = re.sub(r'\"dominantTerpene\":', 'dominantTerpene:', text)
text = re.sub(r'\"terpenes\":', 'terpenes:', text)
text = re.sub(r'\"flavors\":', 'flavors:', text)
text = re.sub(r'\"effects\":', 'effects:', text)
text = re.sub(r'\"activities\":', 'activities:', text)
text = re.sub(r'\"description\":', 'description:', text)
text = re.sub(r'\"visualColor\":', 'visualColor:', text)
text = re.sub(r'\"bgPattern\":', 'bgPattern:', text)

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("✅ data.js key formatting normalized.")
