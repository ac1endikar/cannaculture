import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

path = r'C:\Users\endik\.gemini\antigravity-ide\brain\21575a99-8942-47a0-8565-c8c6d3ec5ac5\.system_generated\steps\365\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Look for relative image paths or product links
srcs = re.findall(r'src=["\']([^"\']+)["\']', text)
print(f"Total src attributes: {len(srcs)}")
for s in set(srcs):
    print("  src:", s)

links = re.findall(r'href=["\']([^"\']+)["\']', text)
print(f"\nTotal href attributes: {len(links)}")
product_links = [l for l in set(links) if '/en/' in l or 'product' in l or '.html' in l]
for l in product_links[:30]:
    print("  link:", l)
