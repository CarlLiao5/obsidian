---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# WFS Prep Services

> 外包 WFS 库存准备工作

## 概述

使用 Prep Services 将 WFS 的库存准备工作外包。如果您缺乏正确一致地准备 Walmart 配送商品的时间、基础设施或可用劳动力，这是一个很好的选择。本指南将介绍如何请求每个单位的 poly bag 和商品标签。

## 工作原理

在 Seller Center 中创建货件时，您可以为 Walmart 配送商品选择商品准备选项。当您的商品到达指定的配送中心时，我们将完成您请求的准备并使商品在 Walmart.com 上可售。

我们将优先处理有计划准备服务的商品，而不是无计划准备的商品。我们还收取额外费用来纠正需要无计划准备工作的商品（例如缺失标签或不正确包装）。

## 费用和无计划准备

使用 Prep Services，您的商品将符合 WFS 包装和标签要求，如 [WFS Routing and Packaging Guide](https://azure-na-assets.contentstack.com/v3/assets/blta7903c6b840b702d/blt57da3349569cc081/WFS_Routing_Guide.pdf?branch=us_mplearn) 中所述。如果您自己准备商品，必须满足相同的要求。不符合的商品可能在配送中心被拒绝或延迟。如果商品需要在配送中心进行无计划准备工作（如缺失标签或不正确包装），我们将额外收取每单位 $0.20 的费用。

| 服务 | 描述 | Prep Service 费用 | 无计划 prep 费用 |
| --- | --- | --- | --- |
| Poly bagging | 我们将为每个可销售单位包装一个松散的透明袋，以保护其在储存和配送过程中 | $0.60/单位 | $0.80/单位 |
| Item labeling | 我们将为每个可销售单位放置可读可扫的标签，并确保每个商品正确标签、接收和储存 | $0.45/单位 | $0.65/单位 |

## 添加 prep 服务

### Seller Center

1. 登录 Seller Center 并转到 [**Shipping Plans**](https://seller.walmart.com/wfsLite/sendinventory) 页面
2. 选择 **Create plan** 并选择商品
3. 在 **Packing setup** 列中，您需要为每个单一 SKU 商品使用模板。创建或编辑模板时，可以选择是否要对该商品应用 WFS Prep Services
4. 更新每个商品的主箱数量以查看价格估算
5. 完成货件计划的其余部分并提交

提交入库订单后，您将无法修改 prep 服务设置。如果需要更改，请取消订单并创建新订单。

### API

请访问 Developer Portal 了解如何在我们的 Create Inbound Shipment API 中添加 prep 服务。

## 常见问题

**WFS Prep Services 费用如何显示在我的账单上？**

您将在结算报告中看到任何计划或无计划 prep 费用。

**哪些商品适合 poly bagging？**

需要额外防止泄漏保护的商品需要放入袋中。例如服装、毛绒玩具、小件物品（USB、珠宝、钥匙扣）、塑料瓶中的液体、粉末和颗粒。

**poly bagging 符合条件的商品最大尺寸是多少？**

poly bag 的最大尺寸为 18" x 24"。大多数可分类商品都可以，但我们可能需要将某些商品放入盒子中如果它们不适合我们现有的任何袋子。这种情况下不会收取额外费用。

**WFS Prep Services 会在商品或包装上的现有条形码上贴标签吗？**

不会，我们不会在现有条形码上贴标签。移除或覆盖任何现有的可扫描条形码。

**我们需要用透明袋发送 poly bagged 商品吗？**

只要带有可扫描条形码和所有必需的危警示，商品可以装在不透明 poly bag 或其他包装中发送。如果条形码不可见，商品将重新装袋或重新贴标签，并被视为无计划准备工作。

## 相关页面

[[theory/WFS-inbound-orders-Prepare-and-pack-shipments]]
[[theory/WFS-inbound-orders-Labels]]

---

> 来源：raw/Walmart_Fulfillment_Services__WFS_--WFS_programs_&_services--WFS-prep-services.md
