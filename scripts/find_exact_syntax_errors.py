import sys, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

def check_file(filepath):
    print(f"\n================ Check {filepath} ================")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    stack = []
    for line_num, line in enumerate(lines, 1):
        for char_num, char in enumerate(line, 1):
            if char in '([{':
                stack.append((char, line_num, char_num))
            elif char in ')]}':
                if not stack:
                    print(f"❌ Extra closing '{char}' at Line {line_num}, Col {char_num}")
                else:
                    top_char, top_line, top_col = stack.pop()
                    expected = {')': '(', ']': '[', '}': '{'}[char]
                    if top_char != expected:
                        print(f"❌ Mismatch at Line {line_num}, Col {char_num}: got '{char}', expected match for '{top_char}' from Line {top_line}")
    
    if stack:
        print(f"❌ Unclosed brackets left in stack ({len(stack)}):")
        for char, l, c in stack[:10]:
            print(f"   Unclosed '{char}' at Line {l}, Col {c}")

check_file('d:/cannaculture/js/data.js')
check_file('d:/cannaculture/js/ai-sommelier.js')
