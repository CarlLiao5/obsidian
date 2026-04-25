#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wiki Link Path Updater
Batch update all [[wikilinks]] to include theory/ or practice/ prefix.
"""

import os
import re
import glob

WIKI_ROOT = r"H:\360MoveData\Users\Administrator\Desktop\双向同步文件\笔记\walmart ZS\wiki"
THEORY_DIR = os.path.join(WIKI_ROOT, "theory")
PRACTICE_DIR = os.path.join(WIKI_ROOT, "practice")

def build_file_map():
    """Build a map: filename (no ext) -> 'theory' or 'practice'"""
    fmap = {}
    for f in os.listdir(THEORY_DIR):
        if f.endswith('.md'):
            name = f[:-3]
            fmap[name] = 'theory'
    for f in os.listdir(PRACTICE_DIR):
        if f.endswith('.md'):
            name = f[:-3]
            fmap[name] = 'practice'
    return fmap

def update_links_in_content(content, fmap):
    """
    Replace [[PageName]] with [[theory/PageName]] or [[practice/PageName]]
    Also handle [[PageName|Display]] and ![[PageName]] and ![[PageName#Header]]
    Skip links that already have theory/ or practice/ prefix.
    """
    changes = 0

    def replacer(match):
        nonlocal changes
        full = match.group(0)
        prefix = match.group(1)  # '!' or ''
        inner = match.group(2)   # content inside [[ ]]

        # Already has path prefix
        if inner.startswith('theory/') or inner.startswith('practice/'):
            return full

        # Extract page name (before | or #)
        page_part = inner.split('|')[0].split('#')[0].strip()

        # Skip external-looking or empty
        if not page_part or '/' in page_part or page_part.startswith('http'):
            return full

        # Remove .md extension if present
        lookup = page_part
        if lookup.endswith('.md'):
            lookup = lookup[:-3]

        if lookup in fmap:
            layer = fmap[lookup]
            new_inner = inner.replace(page_part, layer + '/' + page_part, 1)
            changes += 1
            return prefix + '[[' + new_inner + ']]'

        return full

    # Match ![[...]] and [[...]] but not [...](...) markdown links
    pattern = r'(!?)\[\[([^\]]+)\]\]'
    new_content = re.sub(pattern, replacer, content)
    return new_content, changes

def process_file(filepath, fmap, dry_run=False):
    """Process a single file, updating links."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, changes = update_links_in_content(content, fmap)

    if changes > 0 and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes

def main():
    print("=" * 60, flush=True)
    print("Wiki Link Path Updater", flush=True)
    print("=" * 60, flush=True)

    fmap = build_file_map()
    print("File map: {} theory, {} practice".format(
        sum(1 for v in fmap.values() if v == 'theory'),
        sum(1 for v in fmap.values() if v == 'practice')
    ), flush=True)

    total_changes = 0
    files_changed = 0

    # Process all .md files in wiki/ (including subdirs)
    all_files = glob.glob(os.path.join(WIKI_ROOT, '**', '*.md'), recursive=True)

    for filepath in sorted(all_files):
        relpath = os.path.relpath(filepath, WIKI_ROOT)
        changes = process_file(filepath, fmap, dry_run=False)
        if changes > 0:
            print("[{:3d} links] {}".format(changes, relpath), flush=True)
            total_changes += changes
            files_changed += 1

    print("", flush=True)
    print("=" * 60, flush=True)
    print("Done.", flush=True)
    print("  Files changed: {}".format(files_changed), flush=True)
    print("  Links updated: {}".format(total_changes), flush=True)
    print("=" * 60, flush=True)

if __name__ == "__main__":
    main()
