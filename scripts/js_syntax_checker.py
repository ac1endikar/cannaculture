import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

strains_part = text[text.find("export const STRAINS_DATABASE = ["):]
array_content = strains_part[strains_part.find("[")+1 : strains_part.rfind("];")].strip()

# Check for missing commas between objects: } { or } \n {
missing_commas = re.findall(r'\}[ \t\r\n]+\{', array_content)
print(f"Missing commas between objects: {len(missing_commas)}")

# Check for trailing commas before ]: , \n ];
trailing_commas = re.findall(r',[\s\n]*\]', strains_part)
print(f"Trailing commas before closing array: {len(trailing_commas)}")

# Count total objects
objs = array_content.split('\n  {')
print(f"Total split objects: {len(objs)}")
