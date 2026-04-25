# Sponsored Products 子分类概览

## 产品概述

Sponsored Products 是 Walmart Connect 提供的按点击付费（PPC）站内广告解决方案，帮助卖家在沃尔玛搜索结果页面和商品详情页获得更高的曝光度。通过精准的关键词和商品定向，广告主可以有效提升商品销量和品牌知名度。

Sponsored Products 广告采用竞价模式，广告主只需为实际点击付费，广告展示完全免费。这种广告形式适用于希望扩大市场份额、提升新商品曝光度、或清理库存的卖家。

---

## 活动类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| **自动活动（Automatic Campaigns）** | 系统自动匹配相关搜索词和商品 | 新手上路、快速测试、关键词调研 |
| **手动活动（Manual Campaigns）** | 广告主自行设置关键词和出价 | 精细化运营、精准控制、成熟卖家 |

---

## 出价策略

| 策略类型 | 说明 | 特点 |
|----------|------|------|
| **Dynamic Bidding - Down Only** | 系统仅在可能降低转化的情况下自动降低出价 | 控制成本、适合保守策略 |
| **Dynamic Bidding - Up and Down** | 系统可自动上下调整出价以争取更多转化 | 积极获取流量 |
| **Target ROAS（tROAS）** | 以目标广告支出回报率为优化方向 | 注重投资回报率 |
| **Fixed Bidding** | 固定出价，不自动调整 | 完全控制、稳定可控 |

---

## 活动结构

Sponsored Products 采用层级式结构，便于精细化管理：

```
Campaign（活动）
└── Ad Group（广告组）
    ├── Items（商品定向）
    └── Keywords（关键词定向）
```

- **Campaign（活动层）**：设置整体预算、出价策略、活动时间
- **Ad Group（广告组）**：按产品类别或主题分组，方便管理和优化
- **Item/Keyword（定向层）**：具体商品或关键词，决定广告展示位置

---

## 关键功能

- **Placement（展示位置）**：可选择搜索结果内网格、商品详情页、购物车页面等
- **Bid Multipliers（出价倍数）**：针对特定展示位置或受众调整出价
- **Negative Keywords（否定关键词）**：屏蔽不相关的搜索词，避免无效点击
- **Campaign Reporting（活动报告）**：实时监控广告表现，优化投放策略

---

## 相关页面

**创建活动步骤**
- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]]
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]]
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]]

**核心功能**
- [[theory/Sponsored-Products--Campaign-bidding-strategies]]
- [[theory/Sponsored-Products--Dynamic-bidding]]
- [[theory/Sponsored-Products--Target-ROAS-bidding]]
- [[theory/Sponsored-Products--Expanded-targeting]]
- [[theory/Sponsored-Products-placements]]

**管理工具**
- [[theory/All-Campaigns]]
- [[theory/All-Keywords]]
- [[theory/Sponsored-Products--Glossary]]

---

**来源**：Walmart Connect Sponsored Products 官方文档
