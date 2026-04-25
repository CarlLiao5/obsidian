---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Sponsored Products — 活动设置完整指南

> Sponsored Products 广告活动创建与管理完整流程。

## 流程概览

创建 Sponsored Products 广告活动共 5 个步骤：

| 步骤 | 内容 | 适用活动类型 |
|------|------|------------|
| Step 1 | 创建活动 + 设置预算 + 选择出价策略 | 自动 / 手动 |
| Step 2 | 设置展示位置（Placement Inclusion） | 仅手动 |
| Step 3 | 添加出价倍数（Bid Multipliers） | 自动 / 手动 |
| Step 4 | 创建广告组 + 添加商品 | 自动 / 手动 |
| Step 5 | 添加关键词并设置出价 | 仅手动 |

## 快速入口

- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]] — Step 1 详细指南
- [[theory/Sponsored-Products--Create-a-manual-campaign]] — 手动活动创建指南
- [[theory/Sponsored-Products--Step-2-Set-placement-inclusion]] — 展示位置设置
- [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 出价倍数
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组
- [[theory/Sponsored-Products--Step-4-continued-Add-items-to-an-ad-group]] — 添加商品
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 添加关键词

## 关键概念

### 活动类型对比

| | 自动（Automatic） | 手动（Manual） |
|---|---|---|
| 定向方式 | Walmart AI 自动匹配关键词 | 卖家自选关键词 |
| 关键词控制 | 无 | 完全控制 |
| 展示位置 | 全部位置（无法选择） | 可选择具体位置 |
| 出价倍数 | 支持 | 支持 |
| 出价策略 | Dynamic / Target ROAS / Fixed | Dynamic / Fixed |
| 最低出价 | $0.20 | $0.30 |

### 预算要求

| 账户类型 | 最低日预算 | 最低总预算 |
|---------|----------|-----------|
| Marketplace 卖家 | $10 | $50 |
| Walmart 供应商 | $50 | $100 |

**预算滚动规则：** 未使用的日预算会滚动到次日（但日花费上限为日预算的 2 倍）。

### 关键词匹配类型

| 匹配类型 | 说明 | 示例 |
|---------|------|------|
| **Broad（广泛）** | 词序无关，可插入其他词 | `wireless mouse` 可匹配 `best wireless mouse for gaming` |
| **Phrase（短语）** | 词序固定，中间可有其他词 | `wireless mouse` 可匹配 `buy wireless mouse cheap` |
| **Exact（精确）** | 词序完全一致 | `wireless mouse` 仅匹配 `wireless mouse` |

### 出价策略

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| **Dynamic Bidding（动态出价）** | 系统根据转化概率实时调整出价（±100%/-50%） | 追求转化量 |
| **Target ROAS（目标 ROAS）** | 算法自动优化以达到设定 ROAS 目标 | 优化销售效率（仅限现有活动） |
| **Fixed Bidding（固定出价）** | 手动固定出价，不自动调整 | 精确控制成本 |

## 活动创建流程图

```
创建活动
    │
    ▼
Step 1: 命名 + 选择类型（自动/手动）+ 设置日期/预算 + 选择出价策略
    │
    ▼
[手动活动] Step 2: 设置展示位置（Search In-grid / Search Carousel / Buy Box）
    │
    ▼
Step 3: 设置出价倍数（Placement & Platform 倍数）
    │
    ▼
Step 4: 创建广告组
    │
    ▼
Step 4续: 添加商品（搜索 / CSV 上传）
    │
    ▼
[手动活动] Step 5: 添加关键词 + 设置匹配类型 + 设置出价
    │
    ▼
保存广告组 → 启动活动
```

## 相关页面

- [[theory/Sponsored-Products--Overview]] — Sponsored Products 概览
- [[theory/Sponsored-Products--Glossary]] — 术语词汇表
- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略对比
- [[theory/Sponsored-Products--Dynamic-bidding]] — 动态出价详解
- [[theory/Sponsored-Products--Target-ROAS-bidding]] — 目标 ROAS 出价
- [[theory/Sponsored-Products--Expanded-targeting]] — 扩展定向（品牌词/互补品）
- [[theory/All-Campaigns]] — 活动数据管理
- [[theory/Keywords-Planner]] — 关键词规划工具

---

> 来源：`raw/walmart advertising guide/` 下全部 Step 文件及 Getting started with Sponsored Search playbooks.md