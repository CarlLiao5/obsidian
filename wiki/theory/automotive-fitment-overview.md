# 汽车配件适配（Automotive Fitment）概述

> 通过 ACES/PIES 标准文件，为汽车配件商品匹配特定车型，提升搜索可见性和转化率。

## 概述

Walmart Marketplace 使用行业标准文件，帮助客户在 Walmart.com 上找到与他们的车辆完全匹配的汽车配件。Auto Parts Fitment Widget 允许顾客按车型筛选配件。

## 核心机制

汽车配件必须满足两个条件才能在 Widget 中展示：
1. **标记必需的适配属性**（Brand AAIA、Manufacturing Part Number、Part Terminology ID）
2. **提交 ACES 或 PIES 文件**（Aftermarket Catalog Exchange Standard / Product Information Exchange Standard）

## 必需属性

| 属性 | 说明 |
|------|------|
| **Brand AAIA** | Auto Care Association 分配的 4 字母品牌代码 |
| **Manufacturing Part Number** | 制造商/品牌所有者设定的唯一标识符 |
| **Part Terminology ID** | 每个记录的主键标识符 |

所有属性值必须与 ACES XML 或 ACES Excel 文件中的对应值**完全一致**。

## 第三方服务商

如需帮助创建 ACES/PIES 文件：

| 服务商 | 类型 |
|--------|------|
| Paramount Data Management (PDM) | Walmart 折扣合作伙伴 |
| Optiwise | Walmart 折扣合作伙伴 |
| eCatSolution | Walmart 折扣合作伙伴 |
| Parts Square | Walmart 折扣合作伙伴 |
| Opticat | 标准服务商 |
| SEMA Data Co-op (SDC) | 标准服务商 |
| DCI | 标准服务商 |

## 违规后果

使用 Fitment Widget 即表示确认所有提供的信息均准确、合法，并拥有提供该信息的权利。

## 相关页面

- [[theory/Item_setup]] — 商品设置总览
- [[troubleshoot-automotive-fitment-errors]] — 适配错误排查
- [[theory/Automotive-Fitment_-Add-missing-attributes-and-ACES-coverage]] — 提交缺失属性

---

> 来源：`raw/Item_setup--Automotive_fitment--automotive-fitment-overview.md`