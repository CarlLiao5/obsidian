# -*- coding: utf-8 -*-
import os

wiki_dir = r"h:\360MoveData\Users\Administrator\Desktop\walmart ZS\wiki"
raw_dir = r"h:\360MoveData\Users\Administrator\Desktop\walmart ZS\raw"

# 获取 wiki 中所有页面名（不含扩展名）
wiki_files = []
for f in os.listdir(wiki_dir):
    if f.endswith('.md') and f not in ['index.md', 'log.md']:
        wiki_files.append(f[:-3])

print(f"Wiki 知识页面数: {len(wiki_files)}")

# 获取 raw 中所有源文件路径
raw_files = []
for root, dirs, files in os.walk(raw_dir):
    for f in files:
        if f.endswith('.md'):
            full_path = os.path.join(root, f)
            # 计算相对于 raw_dir 的路径
            rel_path = os.path.relpath(full_path, raw_dir)
            raw_files.append(rel_path)

print(f"Raw 源文件总数: {len(raw_files)}")

# 统计 raw 子目录
raw_guide_count = sum(1 for f in raw_files if f.startswith('walmart guide\\'))
raw_adv_count = sum(1 for f in raw_files if f.startswith('walmart advertising guide\\'))
raw_note_count = sum(1 for f in raw_files if f.startswith('note\\'))

print(f"  - walmart guide: {raw_guide_count}")
print(f"  - walmart advertising guide: {raw_adv_count}")
print(f"  - note: {raw_note_count}")
print(f"  - 其他: {len(raw_files) - raw_guide_count - raw_adv_count - raw_note_count}")

# 检查 raw/walmart guide/ 已处理情况
print("\n=== 检查 walmart guide 目录 ===")
import glob
raw_guide_files = glob.glob(os.path.join(raw_dir, 'walmart guide', '**', '*.md'), recursive=True)
print(f"raw/walmart guide/ 文件数: {len(raw_guide_files)}")

# 读取 log.md 看记录的处理情况
with open(os.path.join(wiki_dir, 'log.md'), 'r', encoding='utf-8') as f:
    log_content = f.read()

print("\n=== log.md 关键记录 ===")
# 查找 ingest 记录
import re
ingest_sections = re.findall(r'## \[[\d-]+\] ingest.*?(?=\n## |\Z)', log_content, re.DOTALL)
for section in ingest_sections[:5]:
    # 只取前几行
    lines = section.strip().split('\n')[:10]
    print(''.join(lines[:5]) + "...")
