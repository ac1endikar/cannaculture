import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

path = r'C:\Users\endik\.gemini\antigravity-ide\brain\21575a99-8942-47a0-8565-c8c6d3ec5ac5\.system_generated\steps\390\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'(?:src|href|data-src|data-image)=["\']([^"\']+)["\']', text)
print(f"Total src/href attributes: {len(imgs)}")
for item in set(imgs):
    if any(ext in item.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp', '/media/', '/image/', '/p/']):
        print("  ", item)
