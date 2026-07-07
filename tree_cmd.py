#!/usr/bin/env python3
import os, sys

def tree(dir_path, prefix='', max_depth=3, depth=0):
    if depth > max_depth: return
    try:
        items = sorted([i for i in os.listdir(dir_path) 
                       if not i.startswith('.') and i not in ('__pycache__','node_modules')])
    except: return
    dirs = [i for i in items if os.path.isdir(os.path.join(dir_path,i))]
    files = [i for i in items if not os.path.isdir(os.path.join(dir_path,i))]
    for i, name in enumerate(dirs[:15] + files[:15]):
        is_last = (i == len(dirs[:15] + files[:15]) - 1)
        branch = "|-- " if not is_last else "+-- "
        print(f'{prefix}{branch}{name}')
        if os.path.isdir(os.path.join(dir_path,name)):
            tree(os.path.join(dir_path,name), prefix + ('|   ' if not is_last else '    '), max_depth, depth+1)

arg = sys.argv[1] if len(sys.argv) > 1 else '.'
print(f'=== {os.path.abspath(arg)} ===')
tree(arg)
