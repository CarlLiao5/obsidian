# 创建手动活动 (Create a Manual Campaign)

> 在 Walmart Connect Ad Center 中创建 Sponsored Products 手动广告活动的完整步骤。

## 概述

手动活动让卖家完全控制选择哪些商品和关键词进行定向，适合有经验的广告主。建议用于：
- 补充自动活动，对高绩效词加大投放
- 聚焦有限关键词集
- 商品在 Walmart 有较长历史

## 创建步骤

### Step 1 — 命名活动

点击 Dashboard 或 All Campaigns 页的 **Create campaign**，输入活动名称。

### Step 2 — 选择活动类型

在 *Targeting* 部分选择：
- **Campaign Type**：Sponsored Products
- **Targeting Tactic**：**Manual（手动）**

### Step 3 — 设置排期与预算

| 设置项 | 说明 |
|--------|------|
| **Start Date** | 选择当天则数小时内启动 |
| **Daily Budget** | Marketplace 卖家最低 $10，供应商最低 $50 |
| **End Date** | 可选，默认为无限期 |
| **Total Budget** | 可选，Marketplace 最低 $50，供应商最低 $100 |

### Step 4 — 选择出价策略

| 出价策略 | 说明 | 可用于手动活动 |
|---------|------|--------------|
| **Dynamic Bidding** | 系统实时调整出价 | ✅ |
| **Fixed Bidding** | 手动固定出价 | ✅ |
| **Target ROAS** | 优化 ROAS | ❌ 仅限现有活动 |

### Step 5 — 继续后续步骤

手动活动后续步骤与自动活动不同：

1. **Step 2** — [[theory/Sponsored-Products--Step-2-Set-placement-inclusion]] — 设置展示位置（手动活动专属）
2. **Step 3** — [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 添加出价倍数
3. **Step 4** — [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组
4. **Step 4续** — [[theory/Sponsored-Products--Step-4-continued-Add-items-to-an-ad-group]] — 添加商品
5. **Step 5** — [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 添加关键词（手动活动专属）

## 关键词匹配类型

| 类型 | 说明 | 示例 |
|------|------|------|
| **Broad（广泛）** | 词序无关，可插入其他词 | `water bottle` 可匹配 `best water bottle` |
| **Phrase（短语）** | 词序固定，中间可有其他词 | `water bottle` 可匹配 `reusable water bottle` |
| **Exact（精确）** | 词序完全一致（无插入词） | `water bottle` 仅匹配 `water bottle` |

**出价规则：** 出价不能超过 $100，最多 2 位小数。

## 商品详情页定向

手动活动可定向到特定商品详情页（Item Page Placements），通过锚点实体（Item Title / Brand / Taxonomy）和关键词匹配类型实现。

## 相关页面

- [[theory/Sponsored-Products--Campaign-setup]] — 活动设置完整流程
- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]] — 创建自动活动
- [[theory/Sponsored-Products--Step-2-Set-placement-inclusion]] — 展示位置设置
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 添加关键词

---

> 来源：`raw/walmart advertising guide/Create a manual campaign.md`