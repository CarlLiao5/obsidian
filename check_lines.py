# -*- coding: utf-8 -*-
with open(r'h:\360MoveData\Users\Administrator\Desktop\双向同步文件\笔记\walmart ZS\wiki\index.md', 'rb') as f:
    raw = f.read()

lines = raw.split(b'\n')
for i in [60, 61, 62, 63, 64, 65]:
    try:
        print(f'Line {i+1}: {lines[i].decode("utf-8")}')
    except:
        print(f'Line {i+1}: {lines[i]}')
