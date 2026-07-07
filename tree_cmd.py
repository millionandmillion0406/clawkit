#!/usr/bin/env python3
"""tree_cmd.py v2 - Project structure visualizer with stats"""
import os, sys, argparse

HIDDEN_DOTFILES = {'.git', '.DS_Store'}

def tree(dir_path, prefix='', max_depth=3, depth=0, pattern=None):
    if depth > max_depth:
        return 0, 0
    try:
        items = sorted(os.listdir(dir_path))
    except (PermissionError, OSError):
        print(f'{prefix}|-- [permission denied]')
        return 0, 0
    
    visible = []
    for item in items:
        if item in ('__pycache__', 'node_modules', '.venv', 'dist', 'build'):
            continue
        if item.startswith('.') and item not in HIDDEN_DOTFILES:
            # Show important config files like .gitignore, .env.example, .editorconfig
            if not os.path.isfile(os.path.join(dir_path, item)):
                continue
        full = os.path.join(dir_path, item)
        if os.path.islink(full):
            continue
        if pattern and os.path.isfile(full) and not any(item.endswith(p.lstrip('*')) for p in pattern.split(',')):
            continue
        visible.append(item)
    
    dirs = [i for i in visible if os.path.isdir(os.path.join(dir_path, i))]
    files = [i for i in visible if not os.path.isdir(os.path.join(dir_path, i))]
    
    display = dirs[:15] + files[:15]
    if len(dirs) > 15:
        print(f'{prefix}... ({len(dirs) - 15} more dirs)')
    if len(files) > 15:
        print(f'{prefix}... ({len(files) - 15} more files)')
    
    d_count, f_count = 0, 0
    for i, name in enumerate(display):
        is_last = (i == len(display) - 1)
        branch = "+-- " if is_last else "|-- "
        full = os.path.join(dir_path, name)
        
        if os.path.isdir(full):
            print(f'{prefix}{branch}{name}')
            sd, sf = tree(full, prefix + ('    ' if is_last else '|   '), max_depth, depth+1, pattern)
            d_count += 1 + sd
            f_count += sf
        else:
            print(f'{prefix}{branch}{name}')
            f_count += 1
    
    return d_count, f_count

def main():
    parser = argparse.ArgumentParser(description='Visualize project directory structure')
    parser.add_argument('path', nargs='?', default='.', help='Directory to scan')
    parser.add_argument('depth', nargs='?', type=int, default=3, help='Max depth (default: 3)')
    parser.add_argument('--pattern', '-p', help='File pattern filter, e.g. "*.py,*.md"')
    parser.add_argument('--all', '-a', action='store_true', help='Show dotfiles')
    args = parser.parse_args()
    
    if args.all:
        global HIDDEN_DOTFILES
        HIDDEN_DOTFILES = set()
    
    root = os.path.abspath(args.path)
    print(f'{root}')
    d, f = tree(root, max_depth=args.depth, pattern=args.pattern)
    print(f'\n{d} directories, {f} files')

if __name__ == '__main__':
    main()
