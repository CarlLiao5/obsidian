# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'h:\360MoveData\Users\Administrator\Desktop\双向同步文件\笔记\walmart ZS\wiki\index.md', 'rb') as f:
    raw = f.read()

lines = raw.split(b'\n')

# Fix lines 13, 14, 15 (0-indexed: 12, 13, 14)
# These MUST be UTF-8 encoded bytes
line13 = '| [[Operations--Mature-Listing-Vicious-Cycle-Recovery]] | 老链接恶性循环破解（流量入口结构诊断） | 新增 |'.encode('utf-8')
line14 = '| [[Operations--Competitive-Position-Analysis--Search-Ranking-Recovery]] | 竞品分析与搜索排名恢复策略 | 新增 |'.encode('utf-8')
line15 = '| [[Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy]] | 广告与自然位协同策略（避免无效重叠） | 新增 |'.encode('utf-8')

# Verify correct decoding
print('Verifying...')
print('Line 13:', line13.decode('utf-8'))
print('Line 14:', line14.decode('utf-8'))
print('Line 15:', line15.decode('utf-8'))

lines[12] = line13
lines[13] = line14
lines[14] = line15

result = b'\n'.join(lines)
with open(r'h:\360MoveData\Users\Administrator\Desktop\双向同步文件\笔记\walmart ZS\wiki\index.md', 'wb') as f:
    f.write(result)

print('\nSUCCESS: index.md fixed')
