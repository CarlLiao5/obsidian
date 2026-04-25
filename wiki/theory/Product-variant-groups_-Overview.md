# 商品变体组（Product Variant Groups）概述

> 将同一商品的不同规格（颜色/尺寸等）聚合到同一商品详情页的机制，提升客户选择体验和搜索可见性。

## 概述

变体组将多个彼此仅在属性（如颜色、尺寸）上有差异的商品聚合到一个商品页上。例如：一件 T 恤提供 5 种颜色 × 4 种尺码 = 20 个子 SKU，它们共享一个父商品页。

## 变体组创建方式

| 方法 | 适用场景 |
|------|----------|
| **Catalog 页面创建** | 最多 49 个现有商品 → [[Create-a-variant-group_-Items-dashboard]] |
| **Full Setup Template** | 50 个及以上商品 → [[Create-a-variant-group_-Full-Setup-Template]] |
| **API** | 批量程序化创建 → Walmart Developer APIs |

## 变体管理操作

创建变体组后，可执行：
- 编辑变体属性
- 添加或移除子商品
- 合并两个变体组
- 拆分变体组
- 添加新的变体属性

详情 → [[Manage-a-variant-group]]

## 常见错误排查

变体组操作时可能遇到各类错误，参考 → [[Troubleshoot-product-variant-errors]]

## 关键提示

- 变体有助于**搜索可见性**和**客户购买转化**
- 每个子商品有独立 SKU 和 Item ID
- 变体广告：同一变体组的商品均可投放 [[theory/Advertise-with-Walmart-Connect-sponsored-search|Sponsored Products]]

## 相关页面

- [[theory/Item_setup]] — 商品设置总览
- [[theory/Item_setup--Item_setup_methods]] — 上架方式
- [[Create-a-variant-group_-Full-Setup-Template]] — 模板创建
- [[Create-a-variant-group_-Items-dashboard]] — 仪表板创建

---

> 来源：`raw/Item_setup--Variant_management--Product-variant-groups_-Overview.md`
> 更新：2025-07-01