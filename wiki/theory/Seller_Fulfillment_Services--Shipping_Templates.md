# 配送模板（Shipping Templates）

> 配送模板用于定义不同地区、承运方式和运费规则，是设置卖家自配送商品运费的核心工具。

## 概述

在开始配送商品之前，卖家需要为每个配送区域设置配送规则。配送模板可在 Seller Center 或通过 Walmart APIs 创建，支持国内和国际两种模板类型。

### 模板类型

|| 模板类型 | 说明 | 限制 |
||---------|------|------|
| **Default（默认模板）** | 每个账号一个，不可删除 | 设置整个目录的默认配送规则 |
| **Custom（自定义模板）** | 最多创建 60 个 | 可为不同商品组设置不同规则 |
| **Paid Standard（付费标准模板）** | 不可用免费配送时使用 | 可禁用 Value 配送 |
| **Freight（货运模板）** | 大件/超重商品（LTL） | 商品重量 > 150 磅或属于货运类目 |
| **International（国际模板）** | 从中国/香港/印度发货 | 支持 7/9/13 天更长转运时间 |

### 配送方式

| 配送方式 | 转运时间 | 运费 | 说明 |
|---------|---------|------|------|
| **Value** | 6-7 天 | 免费 | 默认模板默认启用，不可收费 |
| **Standard** | 3-5 天 | 可收费 | 付费则失去搜索排名优势 |
| **TwoDay** | 2 天 | 免费 | 需达到绩效标准，不可收费 |
| **OneDay** | 1 天 | 可收费 | 需达到绩效标准或已获 TwoDay 资格 |
| **Freight** | 6-10 天 | 可收费 | 仅限大件/超重商品 |

### 运费编辑限制

- 每小时最多 1 次修改
- 每天最多 10 次修改
- 超限后模板锁定 24 小时

## 子页面列表

| wiki 页面名 | 说明 | 源文件 |
|------------|------|--------|
| [[theory/Shipping-templates_-overview]] | 配送模板概述和类型说明 | `Seller_Fulfillment_Services--Shipping_Templates--Shipping-templates_-overview.md` |
| [[theory/Shipping-templates_-add-settings-manually]] | 手动添加国内/国际配送设置 | `Seller_Fulfillment_Services--Shipping_Templates--Shipping-templates_-add-settings-manually.md` |
| [[theory/Shipping-templates_-Assign-SKUs]] | 将 SKU 分配到配送模板 | `Seller_Fulfillment_Services--Shipping_Templates--Shipping-templates_-Assign-SKUs.md` |
| [[theory/Shipping-templates_-manage-settings]] | 管理/修改/删除配送模板 | `Seller_Fulfillment_Services--Shipping_Templates--Shipping-templates_-manage-settings.md` |

## 相关页面

- [[theory/Shipping-methods_-Overview]] — 配送方式详解
- [[theory/Fulfillment-methods_-overview]] — 配送方式概述
- [[Fulfillment_settings]] — 履约设置
- [[theory/add-a-seller-managed-fulfillment-center-in-seller-center]] — 添加自营履约中心

---

> 来源：`raw/Seller_Fulfillment_Services--Shipping_Templates`
