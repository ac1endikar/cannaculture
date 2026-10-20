import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

def strip_strings_and_comments(js_text):
    # Remove single line comments
    js_text = re.sub(r'//.*$', '', js_text, flags=re.M)
    # Remove multi line comments
    js_text = re.sub(r'/\*.*?\*/', '', js_text, flags=re.S)
    # Remove template literals `${...}` handles separately, but simple regex for string literals
    # Replace strings with empty string
    js_text = re.sub(r'"(?:[^"\\]|\\.)*"', '""', js_text)
    js_text = re.sub(r"'(?:[^'\\]|\\.)*'", "''", js_text)
    js_text = re.sub(r'`(?:[^`\\]|\\.)*`', "``", js_text, flags=re.S)
    return js_text

for filename in ['data.js', 'app.js', 'bundle.js']:
    filepath = os.path.join('d:/cannaculture/js', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    clean = strip_strings_and_comments(text)
    
    parens = clean.count('(') - clean.count(')')
    braces = clean.count('{') - clean.count('}')
    brackets = clean.count('[') - clean.count(']')
    print(f"{filename:15s}: parens={parens:2d}, braces={braces:2d}, brackets={brackets:2d}")
