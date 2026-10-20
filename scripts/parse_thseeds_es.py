import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

path = r'C:\Users\endik\.gemini\antigravity-ide\brain\21575a99-8942-47a0-8565-c8c6d3ec5ac5\.system_generated\steps\411\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Look for links ending in .html
html_links = re.findall(r'href=["\']([^"\']+\.html)["\']', text)
print(f"Total .html links found: {len(html_links)}")
for l in set(html_links):
    print("  LINK:", l)

# Look for img src
imgs = re.findall(r'src=["\']([^"\']+)["\']', text)
print(f"\nTotal imgs found: {len(imgs)}")
for i in set(imgs):
    if '/media/' in i or '/catalog/' in i or '.jpg' in i or '.webp' in i:
        print("  IMG:", i)
