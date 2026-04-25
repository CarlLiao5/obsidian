# Step 3 — 添加出价倍数 (Add Bid Multipliers)

> 使用出价倍数（Bid Multipliers）优化广告在特定位置和平台上的竞争力。

## 概述

出价倍数让广告主在保持较低基础出价的同时，针对高价值展示位置或平台提高出价，实现精准投放和预算优化。

## 出价倍数类型

### Placement Multiplier（位置倍数）

针对不同展示位置调整出价：

| 展示位置 | 说明 |
|---------|------|
| Search In-grid | 搜索结果网格（手动活动默认） |
| Search Carousel | 搜索结果轮播 |
| Buy Box | 商品详情页购买框位置 |
| Item Page Carousel | 商品详情页轮播 |

**计算公式：**
> 最终出价 = 基础出价 × (1 + 位置倍数)

**示例：**
- 基础出价：$0.75
- Search In-grid 倍数：200%
- 最终出价：$0.75 × (1+200%) = **$2.25**

### Platform Multiplier（平台倍数）

针对不同设备平台调整出价：

| 平台 | 说明 |
|------|------|
| Desktop（桌面端） | PC 电脑 |
| App（移动 App） | Walmart 移动应用 |
| mWeb（移动网页） | 手机浏览器 |

**示例：**
- 基础出价：$0.20
- mWeb 倍数：90%
- 最终出价：$0.20 × (1+90%) = **$0.38**

### 倍数叠加

Placement 和 Platform 倍数可同时使用，**叠加后合并计算**：

> 最终出价 = 基础出价 × (1 + 位置倍数 + 平台倍数)

**示例（叠加）：**
- 基础出价：$1.00
- Buy Box 倍数：50%
- Desktop 倍数：150%
- 最终出价：$1.00 × (1+50%+150%) = **$3.00**

## 注意事项

- 倍数 = 0% 或留空 = 保持基础出价不变
- **无最高倍数限制**，请确认愿意支出的最高金额
- 可用于自动和手动活动

## 相关页面

- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]] — 创建自动活动
- [[theory/Sponsored-Products--Create-a-manual-campaign]] — 创建手动活动
- [[theory/Sponsored-Products--Step-2-Set-placement-inclusion]] — 展示位置设置（上一步）
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组（下一步）

---

> 来源：`raw/walmart advertising guide/Step 3 Add bid multipliers.md`