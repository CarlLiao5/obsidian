---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 购买配送标签（Buy Shipping Labels in Seller Center）

> 通过 Ship with Walmart 在 Seller Center 中购买折扣配送标签的完整流程。

## 概述

卖家自配送（seller-fulfilled）订单可在 Seller Center 中通过 **Ship with Walmart** 购买折扣配送标签。API 支持 USPS、FedEx、Yanwen 和 SF Express；**不支持 UPS**。

## 标签购买流程

### Step 1 — 准备工作

导航至 Seller Center 的 **Orders** 页面（Unshipped 标签页）。

> **建议**：先在 Account Settings 中配置默认配送和标签设置。

### Step 2 — 购买标签

**单个订单：**
1. 在 Unshipped 标签页点击订单的 PO 编号
2. 确保 Fulfilled by 列显示 **Seller**
3. 点击 **Ship items** → 选择 **Ship with Walmart**
4. 输入包裹类型和重量 → 点击 **Estimate rate** 查看预估价格
5. 确认后点击购买（最终费用以承运商实际扫描重量为准）

**批量订单：**
1. 勾选多个订单 → **Process orders**
2. 为每行填写必要信息
3. 如从中国发货：将 **Ship from** 字段改为 China，商品描述和发货地址使用中文
4. 勾选要购买标签的行 → **Buy Shipping**

### Step 3 — 打印标签

购买成功后点击 **Print label** 打印标签，然后将包裹交给承运商。最后点击 **Mark as Shipped**（一旦标记为已发货，标签无法取消或修改）。

## 承运商优惠费率

使用 WPC（Walmart Preferred Carrier）可享受折扣费率，须遵守 [Terms of Service](https://azure-na-assets.contentstack.com/v3/assets/blta7903c6b840b702d/blt21c4a68205029aca/67c756f2a00ad9164d087c8c/Ship_With_Walmart_Program_Terms_091622.pdf)。

## 相关页面

- [[theory/Seller_Fulfillment_Services]] — 卖家配送服务总览
- [[theory/Ship-with-Walmart-Overview]] — Ship with Walmart 总览
- [[theory/walmart-badge-program-overview]] — Walmart Badge 加急配送

---

> 来源：`raw/Seller_Fulfillment_Services--Ship_with_Walmart--buy-shipping-labels-in-seller-center.md`