---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 配送方式（Shipping Methods）

> Walmart Marketplace 提供五种配送方式：Value、Standard、TwoDay、OneDay 和 Freight，卖家可选择自配送或使用第三方仓储。

## 概述

作为 Marketplace 卖家，你有五种配送方式向客户发货。你必须至少支持一种配送方式（除非选择使用 WFS 仓储代发）。

### 五种配送方式详解

| 配送方式 | 转运时间 | 运费规则 | 绩效要求 |
|---------|---------|---------|---------|
| **Value** | 6-7 天 | 必须免费 | 无 |
| **Standard** | 3-5 天 | 可收费或免费 | 无 |
| **TwoDay** | 2 天 | 必须免费 | 准时送达率 >90%，有效追踪率 >95%，取消率 <1.5% |
| **OneDay** | 1 天 | 可收费或免费 | 需 TwoDay 资格或同等绩效标准 |
| **Freight** | 6-10 天 | 可收费或免费 | 仅限重量 > 150 磅的大件商品 |

### TwoDay 和 OneDay 快速配送计划

沃尔玛优先推送快速配送商品：
- 提升搜索排名
- 增强 Buy Box 优势
- 显示快速配送徽章
- 大促期间优先展示

**建议的履约配置**：

| 设置项 | 建议配置 |
|-------|---------|
| Lag Time | 设为 0 |
| 运营时间 | 截单时间延至 17:00 |
| 周末配送 | 启用周六/周日 |
| 承运商服务 | 优先使用 FedEx Express |
| Ship with Walmart | 使用可享 25% 折扣 |

### 承运商类型

#### 包裹承运商（Parcel Carriers）
- **首选**：USPS、FedEx、UPS
- **其他批准承运商**：包括 4PX、DHL、OnTrac、LaserShip 等数十家

#### 货运承运商（Freight Carriers）
- 商品重量 > 150 磅时必须使用货运
- **批准货运承运商**：ABF Logistics、AIT Worldwide、Estes、FedEx Freight、UPS Freight、SAIA、XPO Logistics 等

### Walmart+ 徽章计划

Walmart+ 徽章标识表示商品为自配送但提供快速、可靠配送：
- 沃尔玛承担 Walmart+ 会员的运费
- 卖家保持原有运费配置
- 商品须在 3 个日历日内发货
- 需达到 Seller Performance Standards

## 子页面列表

| wiki 页面名 | 说明 | 源文件 |
|------------|------|--------|
| [[theory/Shipping-methods_-Overview]] | 配送方式总览 | `Seller_Fulfillment_Services--Shipping_methods--Shipping-methods_-Overview.md` |
| [[theory/Shipping-methods_-expedited-delivery-programs]] | 快速配送计划（OneDay/TwoDay） | `Seller_Fulfillment_Services--Shipping_methods--Shipping-methods_-expedited-delivery-programs.md` |
| [[theory/Shipping-methods_-parcel-shipping-carriers]] | 包裹承运商详情 | `Seller_Fulfillment_Services--Shipping_methods--Shipping-methods_-parcel-shipping-carriers.md` |
| [[theory/Shipping-methods_-freight-shipping-carriers]] | 货运承运商详情 | `Seller_Fulfillment_Services--Shipping_methods--Shipping-methods_-freight-shipping-carriers.md` |
| [[theory/Retrieve-credentials-for-your-return-shipping-carrier-account]] | 获取退货承运商 API 凭证 | `Seller_Fulfillment_Services--Shipping_methods--Retrieve-credentials-for-your-return-shipping-carrier-account.md` |
| [[theory/walmart-badge-program-overview]] | Walmart+ 徽章计划概述 | `Seller_Fulfillment_Services--Shipping_methods--walmart-badge-program-overview.md` |
| [[theory/walmart-badge-enroll-your-items]] | 将商品注册到 Walmart+ 徽章计划 | `Seller_Fulfillment_Services--Shipping_methods--walmart-badge-enroll-your-items.md` |

## 相关页面

- [[theory/Fulfillment-methods_-overview]] — 配送方式概述
- [[Fulfillment_settings]] — 履约设置
- [[Shipping_Templates]] — 配送模板配置
- [[Ship_with_Walmart]] — Ship with Walmart 折扣运费
- [[theory/simplified-shipping-settings-overview]] — 简化配送设置
- [[theory/Seller-performance-standards]] — 卖家绩效标准

---

> 来源：`raw/Seller_Fulfillment_Services--Shipping_methods`
