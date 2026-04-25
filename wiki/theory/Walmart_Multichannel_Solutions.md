# WFS 多渠道解决方案（Walmart Multichannel Solutions）

> 使用 WFS 库存同时为 Walmart.com 和 Amazon、eBay、Temu 等多渠道订单履约，统一库存管理。

## 概述

Walmart Multichannel Solutions（MCS）让你可以用同一 WFS 库存为 Walmart.com 和其他电商平台的客户订单履约，实现真正的全渠道统一管理。

### 核心优势

| 优势 | 说明 |
|-----|------|
| **全渠道履约** | 同时服务 Walmart.com、Amazon、eBay、Temu、Shein 等 |
| **统一库存池** | 单一库存源，所有渠道共享，可移动老化和过期库存 |
| **灵活配送速度** | 选择加急（2天）或标准（3-5天） |
| **无品牌包装** | 使用通用包装（poly bag 或棕色纸箱），适合任何渠道 |
| **退货管理** | 沃尔玛统一处理各渠道退货 |
| **API 自动化** | 与现有系统集成，自动化客户订单 |

### 支持的销售渠道

| 渠道类型 | 说明 |
|---------|------|
| **Marketplace 平台** | Amazon、eBay、Temu、Shein 等 |
| **独立站** | 自有电商网站（符合服务条款即可） |
| **默认** | 所有 WFS 商品默认在 Walmart.com 上架；也可仅履约非 Walmart 渠道 |

### 配送和包装

| 项目 | 说明 |
|-----|------|
| **配送范围** | 仅限美国 50 州和波多黎各，不配送 P.O. Box |
| **加急配送** | 2 个工作日 |
| **标准配送** | 3-5 个工作日 |
| **包装** | 无品牌塑料袋或棕色纸箱 |

### 资格要求

- 必须使用 Walmart 配送服务（WFS）
- 必须在文件中有默认计费方式以支付 WFS 费用
- 商品必须符合 WFS 的产品要求
- Multi-box 和 big and bulky 商品目前**不符合**条件

---

## 费用说明

| 费用类型 | 说明 |
|---------|------|
| **履约费** | 按配送速度和重量计算，批量购买有订单级折扣 |
| **仓储费** | 与 WFS 标准仓储费相同 |
| **Referral Fee** | 多渠道订单**无** Referral Fee |
| **退货费** | 按实际退货处理费用收取 |

#### 加急配送费率（Expedited - 2 business days）

| 运输重量 | 1件 | 2件 | 3件 | 4+件 |
|---------|-----|-----|-----|-------|
| ≤ 6 oz | $9.45 | 每件减 $2.50 | 每件减 $3.00 | 每件减 $3.50 |
| > 6 oz ≤ 12 oz | $9.75 | - | - | - |
| > 12 oz ≤ 1 lb | $10.05 | - | - | - |
| 2–30 lb | $11.35 + $0.75/lb（超过2lb部分） | - | - | - |

#### 标准配送费率（Standard - 3–5 business days）

| 运输重量 | 1件 | 2件 | 3件 | 4+件 |
|---------|-----|-----|-----|-------|
| ≤ 6 oz | $7.45 | 每件减 $2.50 | 每件减 $3.00 | 每件减 $3.50 |
| > 6 oz ≤ 12 oz | $7.75 | - | - | - |
| > 12 oz ≤ 1 lb | $8.05 | - | - | - |
| 2–30 lb | $8.65 + $0.60/lb（超过2lb部分） | - | - | - |
| 31–150 lb | $28.05 + $0.60/lb（超过31lb部分） | - | - | - |

---

## API 集成

MCS 提供专用 API 支持自动化运营：

| API 功能 | 说明 |
|---------|------|
| Create Customer Order | 提交客户订单 |
| Get WFS Inventory | 实时查看各渠道库存 |
| Fetch Delivery Promise | 获取预计配送日期 |
| Cancel Customer Order | 取消订单 |
| Get Fulfillment Order Status | 追踪履约状态 |
| Create Customer Return Order | 创建退货 RMA |

---

## 常见问题

**你们处理退货吗？**
是的，沃尔玛可以为你处理来自任何销售渠道的退货。

**商品是否必须同时在 Walmart.com 上架？**
不是必须的。可以仅为非 Walmart 渠道（如 Amazon、eBay、Temu、Shein）履约。

**价格在美国各地相同吗？**
价格在全国范围内一致。

**需要添加计费方式吗？**
是的，需要计费方式来收取配送、储存和退货费用。

**为什么 Walmart 账户有负余额？**
可能是 Walmart.com 销售额不足以支付 Multichannel Solutions 的费用。

**发货到国际吗？**
不，仅运送到美国本土 50 个州和波多黎各。

---

## 子页面列表

| wiki 页面名 | 说明 | 源文件 |
|------------|------|--------|
| [[multichannel-api]] | 多渠道 API 集成指南 | `Walmart_Fulfillment_Services__WFS_--Walmart_Multichannel_Solutions--multichannel-api.md` |
| [[walmart-cross-border-imports-overview]] | 沃尔玛跨境进口服务 | `Walmart_Fulfillment_Services__WFS_--Walmart_Multichannel_Solutions--walmart-cross-border-imports-overview.md` |

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 总览
- [[theory/WFS_programs_&_services]] — WFS 附加服务
- [[theory/Shipping_to_WFS]] — 配送到 WFS
- [[theory/WFS_Inventory_management]] — WFS 库存管理
- [[theory/Walmart_Cross_Border_-_Imports]] — 跨境进口
- [[theory/WFS-fees]] — WFS 费用详解

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--Walmart_Multichannel_Solutions`
> 更新：2026-04-22（合并自 Walmart-Multichannel-Solutions.md，补入 FAQ、资格要求、标准配送费率表）
