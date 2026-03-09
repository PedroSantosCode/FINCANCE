import re

file_path = r'c:\Users\Alice\Desktop\My Site\FINCANCE_PSW\contas\templates\pagar_conta.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Retrieve all {% ... %} tags
# Be careful with tags spanning newlines, although I fixed one.
tags = re.findall(r'({%.*?%})', content, re.DOTALL)
stack = []

print(f"Analyzing {len(tags)} tags...")

for i, tag in enumerate(tags):
    # Normalize tag content
    t_clean = tag.replace('\n', ' ').strip()
    inner = t_clean[2:-2].strip()
    parts = inner.split()
    if not parts:
        continue
    
    tag_name = parts[0]
    
    # Ignore self-closing or non-block tags
    if tag_name in ['extends', 'load', 'csrf_token', 'include', 'url', 'static', 'else', 'elif', 'empty']:
        continue
        
    if tag_name in ['block', 'if', 'for', 'with', 'while']:
        stack.append((tag_name, tag))
        # print(f"{i}: OPEN  {tag_name:<10}")
    
    elif tag_name.startswith('end'):
        expected = tag_name[3:] # e.g. 'if' from 'endif'
        
        if not stack:
            print(f"ERROR at tag {i} '{tag}': unexpected {tag_name}, stack is empty")
            break
            
        last_name, last_tag = stack[-1]
        
        if last_name == expected:
            stack.pop()
            # print(f"{i}: CLOSE {tag_name:<10}")
        else:
            print(f"ERROR at tag {i} '{tag}': expected end{last_name}, got {tag_name}")
            print(f"  > Last open tag was: {last_tag}")
            break
            
if stack:
    print("ERROR: Unclosed tags remaining at end of file:")
    for tag_name, tag in stack:
        print(f"  {tag_name} : {tag}")
else:
    print("SUCCESS: All tags balanced!")
