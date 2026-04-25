#!/usr/bin/env python3
"""
Add Frontmatter to wiki pages that don't have one.
This script processes all markdown files in wiki/theory and wiki/practice.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def get_frontmatter_template(file_path, status="pending"):
    """Generate frontmatter based on file location and status."""
    if "theory" in str(file_path):
        return f"""---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: {datetime.now().strftime('%Y-%m-%d')}
tags: [官方文档, 知识库]
---

"""
    else:  # practice
        return """---
author: 运营团队
auditor: 待审核
status: pending
audit_date: null
tags: [运营实践, 待审核]
---

"""

def has_frontmatter(content):
    """Check if content already has YAML frontmatter."""
    if not content.startswith("---"):
        return False
    try:
        match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        return match is not None
    except:
        return False

def add_frontmatter_to_file(file_path):
    """Add frontmatter to a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has frontmatter
        if has_frontmatter(content):
            return False

        # Generate and prepend frontmatter
        frontmatter = get_frontmatter_template(file_path)
        new_content = frontmatter + content

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False

def process_wiki_directory(wiki_dir):
    """Process all markdown files in theory and practice directories."""
    wiki_path = Path(wiki_dir)

    for section in ["theory", "practice"]:
        section_path = wiki_path / section
        if not section_path.exists():
            continue

        print(f"\nProcessing wiki/{section}/...")
        count = 0
        for md_file in section_path.glob("*.md"):
            if add_frontmatter_to_file(md_file):
                count += 1
                print(f"  ✓ {md_file.name}")

        print(f"  Total: {count} files updated")

if __name__ == "__main__":
    wiki_dir = Path(__file__).parent.parent / "wiki"
    print(f"Adding Frontmatter to wiki pages...\n")
    print(f"Wiki directory: {wiki_dir}")
    process_wiki_directory(wiki_dir)
    print("\n✅ Frontmatter addition complete!")
