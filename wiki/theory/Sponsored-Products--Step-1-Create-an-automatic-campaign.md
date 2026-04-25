---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Step 1 — 创建自动活动 (Create an Automatic Campaign)

> 在 Walmart Connect Ad Center 中创建 Sponsored Products 自动广告活动的完整步骤。

## 概述

自动活动利用 Walmart Connect 的 AI 和机器学习自动定向和优化广告，系统自动判断最佳受众和展示位置。建议用于：新品推广、扩大覆盖、节省优化时间。

## 创建步骤

### Step 1 — 命名活动

点击 Dashboard 或 All Campaigns 页的 **Create campaign**，输入活动名称。建议使用描述性命名规则。

### Step 2 — 选择活动类型

在 *Targeting* 部分选择：

- **Campaign Type**：Sponsored Products
- **Targeting Tactic**：**Automatic（自动）**

自动活动由系统根据商品标题、描述、类目自动匹配搜索词，无需手动选择关键词。

### Step 3 — 设置排期与预算

| 设置项 | 说明 |
|--------|------|
| **Start Date（开始日期）** | 选择当天则数小时内启动 |
| **Daily Budget（日预算）** | Marketplace 卖家最低 $10，供应商最低 $50 |
| **End Date（结束日期）** | 可选，默认为无限期 |
| **Total Budget（总预算）** | 可选，Marketplace 最低 $50，供应商最低 $100 |

**日预算滚动规则：** 未用完的日预算会累积到次日（日花费上限为日预算的 2 倍）。

### Step 4 — 选择出价策略

| 出价策略 | 说明 |
|---------|------|
| **Dynamic Bidding（动态出价）** | 系统根据转化概率实时调整出价（自动活动推荐） |
| **Target ROAS（目标 ROAS）** | 优化销售效率，仅限现有活动适用（新活动不可选） |
| **Fixed Bidding（固定出价）** | 手动固定出价 |

### Step 5 — 扩展定向（Expanded Targeting）

可选功能，帮助扩大活动覆盖：

- **Brand Term Targeting（品牌词定向）**：可对品牌词和竞品品牌词出价（自动启用）
- **Complementary Targeting（互补品定向）**：将广告展示在相关商品详情页轮播位

### Step 6 — 继续后续步骤

完成后，进入以下步骤：
- [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 添加出价倍数（可选）
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组

## 最低要求汇总

| 要求 | Marketplace 卖家 | Walmart 供应商 |
|------|-----------------|---------------|
| 日预算最低 | $10 | $50 |
| 总预算最低（若设） | $50 | $100 |
| 出价最低 | $0.20 | $0.20 |

## 相关页面

- [[theory/Sponsored-Products--Campaign-setup]] — 活动设置完整流程
- [[theory/Sponsored-Products--Create-a-manual-campaign]] — 创建手动活动
- [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 出价倍数
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组

---

> 来源：`raw/walmart advertising guide/Step 1 Create an automatic campaign.md`