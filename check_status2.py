# -*- coding: utf-8 -*-
import os

wiki_dir = r"h:\360MoveData\Users\Administrator\Desktop\walmart ZS\wiki"
raw_dir = r"h:\360MoveData\Users\Administrator\Desktop\walmart ZS\raw"

# 获取 wiki 中所有页面名（不含扩展名）
wiki_files = []
for f in os.listdir(wiki_dir):
    if f.endswith('.md') and f not in ['index.md', 'log.md']:
        wiki_files.append(f[:-3])

print(f"Wiki 页面数: {len(wiki_files)}")

# 获取 raw 文件名映射（处理 walmart guide 和 walmart advertising guide）
raw_to_wiki_map = {}

for root, dirs, files in os.walk(raw_dir):
    for f in files:
        if f.endswith('.md'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, raw_dir)
            raw_to_wiki_map[rel_path] = f[:-3]

print(f"Raw 文件总数: {len(raw_to_wiki_map)}")

# 分类统计
raw_guide = {k: v for k, v in raw_to_wiki_map.items() if k.startswith('walmart guide\\')}
raw_adv = {k: v for k, v in raw_to_wiki_map.items() if k.startswith('walmart advertising guide\\')}
raw_note = {k: v for k, v in raw_to_wiki_map.items() if k.startswith('note\\')}
raw_others = {k: v for k, v in raw_to_wiki_map.items() if not (k.startswith('walmart guide\\') or k.startswith('walmart advertising guide\\') or k.startswith('note\\'))}

print(f"\nwalmart guide: {len(raw_guide)} 个文件")
print(f"walmart advertising guide: {len(raw_adv)} 个文件")
print(f"note: {len(raw_note)} 个文件")
print(f"其他: {len(raw_others)} 个文件")
print(f"总计: {sum(len(x) for x in [raw_guide, raw_adv, raw_note, raw_others])} 个文件")

# 根据 log.md 查看已处理的
log_path = os.path.join(wiki_dir, 'log.md')
with open(log_path, 'r', encoding='utf-8') as f:
    log = f.read()

# 统计 log 中记录的 ingest
import re
sections = re.findall(r'## \[([\d-]+)\] ingest \| (.*?)\n(.*?)(?=\n## |\Z)', log, re.DOTALL)
print(f"\nLog 中的 ingest 记录数: {len(sections)}")
for date, topic, content in sections:
    # 查找创建的页面
    pages = re.findall(r'- \[\[(.*?)\]\]', content)
    print(f"  [{date}] {topic}: 创建了 {len(pages)} 个页面")
    if pages:
        for p in pages[:3]:
            print(f"    - {p}")
        if len(pages) > 3:
            print(f"    ... 还有 {len(pages)-3} 个")

# 计算剩余未处理的
print("\n=== 待处理文件统计 ===")
print(f"walmart advertising guide 已处理（log 中记录 62 个全部处理）")
print(f"walmart guide 已处理（log 中记录 362 个全部处理）")
print(f"note/运营每日内容.md - 待处理")
print(f"跨境电商要变天了？... - 已处理（log 中记录）")

# 列出所有待处理文件
print("\n待处理文件列表:")
for path, name in sorted(raw_note.items()):
    print(f"  {path}")
for path, name in sorted(raw_others.items()):
    print(f"  {path}")
