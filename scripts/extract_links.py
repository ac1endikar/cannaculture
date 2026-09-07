import re

path = r'C:\Users\endik\.gemini\antigravity-ide\brain\c506c0f1-22e0-475b-a32d-e8561a2fd772\.system_generated\steps\1700\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|png|webp|jpeg)', text)
for img in sorted(set(imgs)):
    print(img)
