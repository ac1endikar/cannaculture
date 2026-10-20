import json, sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

path = r'C:\Users\endik\.gemini\antigravity-ide\brain\21575a99-8942-47a0-8565-c8c6d3ec5ac5\.system_generated\steps\223\content.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
for line in content.split('\n'):
    line = line.strip()
    if line.startswith('['):
        try:
            data = json.loads(line)
            if not data:
                print('(sin resultados)')
            for i, item in enumerate(data):
                title = item.get('title', {}).get('rendered', '')
                src = item.get('source_url', '')
                details = item.get('media_details', {})
                w = details.get('width', 0)
                h = details.get('height', 0)
                mime = item.get('mime_type', '')
                alt = item.get('alt_text', '')
                print(f'[{i+1}] [{w}x{h}] {title}')
                if alt: print(f'     alt: {alt}')
                print(f'     {src}')
            break
        except Exception as e:
            pass
