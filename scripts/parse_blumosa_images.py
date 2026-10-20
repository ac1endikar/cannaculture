import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

path = r'C:\Users\endik\.gemini\antigravity-ide\brain\21575a99-8942-47a0-8565-c8c6d3ec5ac5\.system_generated\steps\899\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find image URLs
imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', text, re.IGNORECASE)
print(f"Total image URLs found on Blumosa page: {len(imgs)}")
for img in sorted(list(set(imgs))):
    print("  IMAGE:", img)
