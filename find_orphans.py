# -*- coding: utf-8 -*-
import os
import re

wiki_dir = r"h:\360MoveData\Users\Administrator\Desktop\walmart ZS\wiki"
exclude_files = {'index.md', 'log.md'}

# 获取所有 wiki 页面名称
all_files = [f for f in os.listdir(wiki_dir) if f.endswith('.md') and f not in exclude_files]
page_names = set(f[:-3] for f in all_files)

# 扫描所有文件，提取 [[页面名称]] 链接
referenced_pages = set()
link_details = []
pattern = re.compile(r'\[\[([^\]]+)\]\]')

for f in all_files:
    filepath = os.path.join(wiki_dir, f)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = pattern.findall(content)
            for match in matches:
                referenced_pages.add(match.strip())
    except Exception as e:
        print(f"Error reading {f}: {e}")

# 找出孤儿页面（没有被任何页面引用的）
orphan_pages = page_names - referenced_pages

print("=" * 80)
print("孤儿页面清单（未被任何页面引用）")
print("=" * 80)
for page in sorted(orphan_pages):
    filepath = os.path.join(wiki_dir, page + '.md')
    size = os.path.getsize(filepath) if os.path.exists(filepath) else 0
    print(f"  - {page} ({size} bytes)")

print(f"\n总计: {len(orphan_pages)} 个孤儿页面")

# 检查 index.md 是否引用了这些页面
print("\n" + "=" * 80)
print("检查孤儿页面是否在 index.md 中被引用")
print("=" * 80)
index_path = os.path.join(wiki_dir, 'index.md')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

for page in sorted(orphan_pages):
    if page in index_content:
        print(f"  [index.md中已引用] {page}")
    else:
        print(f"  [未被引用] {page}")
