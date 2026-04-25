# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime, timedelta
import json

wiki_dir = r"h:\360MoveData\Users\Administrator\Desktop\walmart ZS\wiki"

# 排除的文件
exclude_files = {'index.md', 'log.md'}

# 获取所有 .md 文件（排除 index.md 和 log.md）
all_files = []
for f in os.listdir(wiki_dir):
    if f.endswith('.md') and f not in exclude_files:
        all_files.append(f)

print(f"总文件数（不含index/log）: {len(all_files)}", flush=True)

# 提取页面名称（不含扩展名）
page_names = set()
for f in all_files:
    page_name = f[:-3]  # 移除 .md
    page_names.add(page_name)

print(f"总页面名称数: {len(page_names)}", flush=True)

# 扫描所有文件，提取 [[页面名称]] 链接
referenced_pages = set()
link_details = []  # (from_file, linked_page)

pattern = re.compile(r'\[\[([^\]]+)\]\]')

for f in all_files:
    filepath = os.path.join(wiki_dir, f)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = pattern.findall(content)
            for match in matches:
                # 清理匹配到的名称（可能有空格变化）
                linked_name = match.strip()
                referenced_pages.add(linked_name)
                link_details.append((f, linked_name))
    except Exception as e:
        print(f"Error reading {f}: {e}", flush=True)

print(f"被引用的页面名称数: {len(referenced_pages)}", flush=True)
print(f"总链接数: {len(link_details)}", flush=True)

# 找出孤儿页面（没有被任何页面引用的）
orphan_pages = page_names - referenced_pages
print(f"孤儿页面数: {len(orphan_pages)}", flush=True)

# 获取文件元数据并识别陈旧页面
today = datetime.now()
days_threshold = 180
size_threshold = 500

# 关键词
stale_keywords = ['TODO', 'FIXME', '待更新', '过时', 'deprecated', 'TBD', 'WIP']

file_metadata = {}
stale_pages = []
small_pages = []

for f in all_files:
    filepath = os.path.join(wiki_dir, f)
    try:
        stat = os.stat(filepath)
        size = stat.st_size
        mtime = datetime.fromtimestamp(stat.st_mtime)
        days_ago = (today - mtime).days
        
        # 读取内容检测关键词
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.count('\n') + 1
        except:
            content = ""
            lines = 0
        
        file_metadata[f] = {
            'size': size,
            'mtime': mtime,
            'days_ago': days_ago,
            'lines': lines
        }
        
        # 检测陈旧内容
        reasons = []
        if days_ago > days_threshold:
            reasons.append(f"超过{days_ago}天未修改")
        if size < size_threshold:
            reasons.append(f"文件过小({size}字节)")
            small_pages.append(f)
        
        # 检查关键词
        content_upper = content.upper()
        for kw in stale_keywords:
            if kw.upper() in content_upper:
                reasons.append(f"包含'{kw}'")
        
        if reasons:
            stale_pages.append({
                'file': f,
                'page': f[:-3],
                'mtime': mtime,
                'size': size,
                'days_ago': days_ago,
                'lines': lines,
                'reasons': reasons
            })
            
    except Exception as e:
        print(f"Error stat {f}: {e}", flush=True)

# 输出结果
print("\n" + "="*80, flush=True)
print("=== 统计总览 ===", flush=True)
print(f"总 Wiki 页面数: {len(all_files)} 个（不含 index/log）", flush=True)
print(f"已链接页面数: {len(page_names & referenced_pages)} 个", flush=True)
print(f"孤儿页面数: {len(orphan_pages)} 个", flush=True)
print(f"包含链接数: {len(link_details)} 个", flush=True)
print(f"陈旧页面数: {len(stale_pages)} 个", flush=True)

print("\n=== 孤儿页面清单 ===", flush=True)
print(f"{'页面名':<60} {'大小':>8} {'最后修改':>12} {'行数':>6}", flush=True)
print("-" * 90, flush=True)

orphan_list = []
for f in sorted(all_files):
    page = f[:-3]
    if page in orphan_pages:
        meta = file_metadata.get(f, {})
        size = meta.get('size', 0)
        mtime = meta.get('mtime', datetime.now()).strftime('%Y-%m-%d')
        lines = meta.get('lines', 0)
        print(f"{page:<60} {size:>8} {mtime:>12} {lines:>6}", flush=True)
        orphan_list.append({'page': page, 'size': size, 'mtime': mtime, 'lines': lines})

print(f"\n孤儿页面共 {len(orphan_list)} 个", flush=True)

print("\n=== 陈旧内容清单（按时间排序）===", flush=True)
print(f"{'页面名':<55} {'最后修改':>12} {'大小':>8} {'原因':<30}", flush=True)
print("-" * 110, flush=True)

# 按最后修改时间排序（最旧的在前）
stale_pages_sorted = sorted(stale_pages, key=lambda x: x['mtime'])

for item in stale_pages_sorted:
    reasons_str = "; ".join(item['reasons'])
    mtime_str = item['mtime'].strftime('%Y-%m-%d')
    print(f"{item['page']:<55} {mtime_str:>12} {item['size']:>8} {reasons_str:<30}", flush=True)

print(f"\n陈旧页面共 {len(stale_pages_sorted)} 个", flush=True)

print("\n=== 建议处理 ===", flush=True)
if len(orphan_pages) > 0:
    print(f"- {len(orphan_pages)} 个孤儿页面需要考虑删除或添加导航链接", flush=True)
if len(small_pages) > 0:
    print(f"- {len(small_pages)} 个页面文件过小（<{size_threshold}字节），可能内容不完整", flush=True)
old_count = len([p for p in stale_pages if p['days_ago'] > days_threshold])
if old_count > 0:
    print(f"- {old_count} 个页面超过180天未更新，建议审核内容时效性", flush=True)

print("\n=== JSON格式输出（方便后续处理）===", flush=True)
result = {
    'total_pages': len(all_files),
    'linked_pages': len(page_names & referenced_pages),
    'orphan_pages': len(orphan_pages),
    'orphan_list': orphan_list,
    'stale_pages': [
        {
            'page': p['page'],
            'mtime': p['mtime'].strftime('%Y-%m-%d'),
            'size': p['size'],
            'days_ago': p['days_ago'],
            'reasons': p['reasons']
        } for p in stale_pages_sorted
    ]
}
print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
