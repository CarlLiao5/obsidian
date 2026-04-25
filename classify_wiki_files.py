#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wiki 文件自动分类脚本
根据文件来源和内容特征，自动分类到 theory/ 或 practice/
"""

import os
import re
from pathlib import Path

# 配置
WIKI_ROOT = r"H:\360MoveData\Users\Administrator\Desktop\双向同步文件\笔记\walmart ZS\wiki"
THEORY_DIR = os.path.join(WIKI_ROOT, "theory")
PRACTICE_DIR = os.path.join(WIKI_ROOT, "practice")
RAW_ROOT = r"H:\360MoveData\Users\Administrator\Desktop\双向同步文件\笔记\walmart ZS\raw"

# 确保目录存在
os.makedirs(THEORY_DIR, exist_ok=True)
os.makedirs(PRACTICE_DIR, exist_ok=True)

# Practice 关键词（来自 raw/note 的运营方法论）
PRACTICE_KEYWORDS = [
    "methodology",  # 方法论
    "sop",  # 标准操作流程
    "paradox",  # 悖论/案例分析
    "strategy",  # 策略
    "analysis",  # 分析
    "optimization",  # 优化
    "diagnostics",  # 诊断
    "recovery",  # 恢复
    "cold-start",  # 冷启动
    "case-study",  # 案例研究
]

# Theory 关键词（官方基础知识）
THEORY_KEYWORDS = [
    "overview",  # 概览
    "guide",  # 指南
    "setup",  # 设置
    "campaign",  # 活动
    "bidding",  # 出价
    "placement",  # 展示位置
    "keyword",  # 关键词
    "glossary",  # 词汇表
    "policy",  # 政策
    "standard",  # 标准
    "requirement",  # 要求
    "how-to",  # 操作指南
    "step",  # 步骤
]

def classify_file(filename):
    """
    根据文件名分类
    返回: 'theory', 'practice', 或 'unknown'
    """
    filename_lower = filename.lower()

    # 检查 practice 关键词
    for keyword in PRACTICE_KEYWORDS:
        if keyword in filename_lower:
            return "practice"

    # 检查 theory 关键词
    for keyword in THEORY_KEYWORDS:
        if keyword in filename_lower:
            return "theory"

    # 默认分类逻辑
    # 如果包含"Advertising--"且不是 overview/troubleshooting，可能是 theory
    if "advertising--" in filename_lower and "overview" in filename_lower:
        return "theory"

    # 如果包含"Sponsored-Products--"，通常是 theory
    if "sponsored-products--" in filename_lower:
        return "theory"

    # 如果包含"Operations--"，通常是 practice
    if "operations--" in filename_lower:
        return "practice"

    # 如果包含"Algorithm-transition"，是 practice
    if "algorithm-transition" in filename_lower:
        return "practice"

    # 其他情况默认为 theory（官方文档）
    return "theory"

def move_file(src, dest_dir):
    """移动文件到目标目录"""
    dest = os.path.join(dest_dir, os.path.basename(src))
    try:
        os.rename(src, dest)
        return True, dest
    except Exception as e:
        return False, str(e)

def main():
    """主函数"""
    print("=" * 60)
    print("Wiki File Auto-Classification")
    print("=" * 60)

    # Get all .md files in wiki root
    files = [f for f in os.listdir(WIKI_ROOT)
             if f.endswith('.md') and os.path.isfile(os.path.join(WIKI_ROOT, f))]

    # Exclude system files
    exclude_files = {'index.md', 'log.md'}
    files = [f for f in files if f not in exclude_files]

    print("\nFound {} unclassified files\n".format(len(files)))

    theory_count = 0
    practice_count = 0
    failed_count = 0

    for filename in sorted(files):
        src_path = os.path.join(WIKI_ROOT, filename)
        classification = classify_file(filename)

        if classification == "theory":
            success, result = move_file(src_path, THEORY_DIR)
            if success:
                print("[OK] [THEORY] {}".format(filename), flush=True)
                theory_count += 1
            else:
                print("[NG] [ERROR] {}: {}".format(filename, result), flush=True)
                failed_count += 1

        elif classification == "practice":
            success, result = move_file(src_path, PRACTICE_DIR)
            if success:
                print("[OK] [PRACTICE] {}".format(filename), flush=True)
                practice_count += 1
            else:
                print("[NG] [ERROR] {}: {}".format(filename, result), flush=True)
                failed_count += 1

    print("\n" + "=" * 60)
    print("Classification Complete")
    print("  Theory:   {} files".format(theory_count))
    print("  Practice: {} files".format(practice_count))
    print("  Failed:   {} files".format(failed_count))
    print("=" * 60)

if __name__ == "__main__":
    main()
