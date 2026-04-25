# 履约设置（Fulfillment Settings）

> 履约设置用于配置延迟发货时间豁免、运营时间、周末配送和第三方仓储合作。

## 概述

卖家自配送（Seller Fulfillment Services）的履约设置模块允许卖家在 Seller Center 中配置各项配送运营参数，确保订单在承诺时效内完成处理和发货。

### 主要配置项

|| 设置项 | 说明 |
||------|------|
| **延迟发货时间（Lag Time）** | 订单确认后发货所需的工作日数，默认要求 2 个工作日内发货 |
| **延迟时间豁免（Lag Time Exemption）** | 适用于定制品/Print-on-Demand（最长 5 天）或大件/货运商品（最长 10 天） |
| **运营时间（Operating Schedule）** | 定义截单时间和工作日，默认周一至周五，截单时间 14:00 |
| **周末配送（Weekend Delivery）** | 启用周六/周日配送，提升配送时效准确性 |
| **合作伙伴仓（Partner Fulfillment）** | 通过 Deliverr 或 ShipBob 代发，自动获得 TwoDay 资格 |

### 延迟时间豁免政策

- **定制品/Print-on-Demand**：最长豁免 5 个工作日
- **大件/货运（LTL）**：最长豁免 10 个工作日
- **新卖家临时豁免**：可能有固定到期日的临时豁免资格
- 延迟时间越短，客户转化率越高，且更易获得快速配送计划资格

### 运营时间设置要求

- 每日配送支持时间：当地时区 11:00 之前
- 每周至少 5 个工作日
- 每年每个仓库最多可设置 30 天休息日（Additional Days Off）

## 子页面列表

| wiki 页面名 | 说明 | 源文件 |
|------------|------|--------|
| [[theory/Update-fulfillment-lag-time-in-Seller-Center]] | 在 Seller Center 中更新发货延迟时间 | `Seller_Fulfillment_Services--Fulfillment_settings--Update-fulfillment-lag-time-in-Seller-Center.md` |
| [[theory/Submit-a-lag-time-exemption-request]] | 提交延迟发货时间豁免申请 | `Seller_Fulfillment_Services--Fulfillment_settings--Submit-a-lag-time-exemption-request.md` |
| [[theory/Fulfillment-Center-operating-schedule]] | 配置履约中心运营时间和截单时间 | `Seller_Fulfillment_Services--Fulfillment_settings--Fulfillment-Center-operating-schedule.md` |
| [[theory/weekend-delivery-settings]] | 设置周末（周六/周日）配送选项 | `Seller_Fulfillment_Services--Fulfillment_settings--weekend-delivery-settings.md` |
| [[theory/add-a-partner-fulfillment-center-in-seller-center]] | 添加 Deliverr/ShipBob 合作伙伴仓储 | `Seller_Fulfillment_Services--Fulfillment_settings--add-a-partner-fulfillment-center-in-seller-center.md` |
| [[theory/add-a-seller-managed-fulfillment-center-in-seller-center]] | 添加卖家自营履约中心 | `Seller_Fulfillment_Services--Fulfillment_settings--add-a-seller-managed-fulfillment-center-in-seller-center.md` |

## 相关页面

- [[theory/Fulfillment-methods_-overview]] — 配送方式概述
- [[theory/Shipping-methods_-Overview]] — 配送方式详解
- [[theory/Seller_Fulfillment_Services]] — 卖家自配送总览
- [[Shipping_Templates]] — 配送模板配置
- [[theory/simplified-shipping-settings-overview]] — 简化配送设置
- [[Ship_with_Walmart]] — Ship with Walmart 沃尔玛代发标签服务

---

> 来源：`raw/Seller_Fulfillment_Services--Fulfillment_settings`
