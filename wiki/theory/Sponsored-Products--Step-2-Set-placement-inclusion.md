---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Step 2 — 设置展示位置 (Set Placement Inclusion)

> 手动 Sponsored Products 活动的展示位置（Placement）配置。

## 概述

手动活动允许广告主选择广告在哪些位置展示。自动活动则默认包含全部展示位置且无法选择。

## 展示位置类型

### Search In-grid（搜索结果网格）

手动活动的默认展示位置，无法关闭。顾客搜索词与投放关键词匹配时，广告出现在搜索结果网格内。

### Search Carousel（搜索结果轮播）

顾客搜索词与投放关键词匹配时，广告出现在搜索结果下方的轮播位。

### Buy Box & Item Carousel（购买框及商品轮播）

顾客进入商品详情页时，如果锚点实体（标题/品牌/类目）与投放关键词匹配，广告出现在购买框位置或商品详情页轮播位。

**锚点实体（Anchor Item Entities）：**

| 实体类型 | 示例 |
|---------|------|
| 商品标题 | Great Value All Purpose Cleaner, Lemon Scent, 32 fl oz |
| 品牌 | Great Value |
| 类目 | Household Essentials / Cleaning Supplies / All-Purpose Cleaners |

### 匹配类型与 Item Page 展示

| 匹配类型 | 匹配规则 |
|---------|---------|
| **Exact（精确）** | 关键词词序完全一致（停用词除外），无额外词 |
| **Phrase（短语）** | 所有词在同一实体中出现（顺序不固定），可有前缀/后缀 |
| **Broad（广泛）** | 所有词以任意顺序出现，无需连续 |

## 定向策略示例

**示例 1 — 定向洗发水类目页面**

先用广泛/短语匹配定向类目层级（`beauty`、`hair care`），再用精准匹配定向具体商品。

**示例 2 — 定向已知具体商品页面**

用精确匹配商品标题（如 `"Equate Everyday Clean Dandruff Shampoo, 33.8 fl. oz."`），或用短语/广泛匹配包含部分词的商品。

**示例 3 — 定向自有品牌商品页面（防御竞争）**

用品牌词精确匹配（如 `"Equate"`），确保自家广告出现在自家商品页面，防止竞品广告占据。

## 相关页面

- [[theory/Sponsored-Products--Create-a-manual-campaign]] — 创建手动活动
- [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 添加出价倍数（下一步）

---

> 来源：`raw/walmart advertising guide/Step 2 Set placement inclusion.md`