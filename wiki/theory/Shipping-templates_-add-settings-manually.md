---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Shipping templates: Add settings manually

> 手动添加国内和国际配送设置

## 概述

本指南将介绍如何使用 Seller Center 中的配送模板添加国内和国际配送设置。

## 添加设置

### 步骤 1 — 开始

导航到 Seller Center 中的 **Shipping Profile** 页面，选择 [_Shipping Templates_](https://seller.walmart.com/settings/shipping-profile/shipping-templates)。

### 步骤 2 — 创建模板

选择 **Create shipping template** 按钮并选择以下选项之一：

- **Manual shipping settings**：为从美国发货的商品创建模板
- **International shipping settings**：为从中国、香港或印度发货的商品创建模板。您必须使用此选项来设置国际运输时间（7、9 和 13 天）

### 步骤 3 — 添加配送规则

选择 **Edit template name**，然后在 **Shipping Methods and Regions** 部分下自定义您的配送设置。对于国际模板，选择配送中心所在的国家/地区。从下拉菜单中选择要更改的运输时间，为每种配送方式和区域添加新的配送规则。

您可以在 **Rate** 下更新配送费用。配送费用需遵守 [Egregious Shipping Cost 规则](https://marketplacelearn.walmart.com/guides/Catalog%20management/Price%20management/Pricing-rules)。完成后，选择 **Save Template**。

### 步骤 4 — 将 SKU 分配到模板

创建模板后，您需要将 SKU 分配到模板，以定义每件商品的配送规则。如果您最近在 Seller Center 中添加了卖家管理的配送中心，必须等待四个小时才能将 SKU 分配到配送中心。如果不等待所需时间，您的配送设置将恢复到默认配送模板，创建的所需模板将不会被激活。

## 常见问题

**为什么我无法编辑模板的配送费用？**

每个模板每小时限制一次更改。每天最多可以进行 10 次编辑。如果超过此限制，您的配送模板将被锁定 24 小时。

**为什么我无法设置或编辑订单总金额模板的价格？**

如果配送价值超过 Egregious Shipping Cost 规则，您将无法创建或更新配送模板。在每个商品价格层级下调整配送费用并重新提交模板。

**如何从 Value 配送中移除 SKU？**

要移除 Value Shipping 中的 SKU，必须创建付费标准配送模板。创建模板后，必须等待四个小时，然后将 SKU 添加到付费标准配送模板。这将从 Value 配送模板中移除 SKU 并将其添加到付费标准模板。

**如何从默认配送模板禁用阿拉斯加和夏威夷的 Value 配送？**

要禁用阿拉斯加和夏威夷的 Value 配送，选择 **Edit templates**，然后选择 **Add Shipping Rule** 并取消选择 **Hawaii and Alaska – Street**。

**还有其他类型的配送模板吗？**

是的。还有 Default、Custom、Paid Standard 和 Freight。请访问 [_Shipping Templates: Overview_](https://marketplacelearn.walmart.com/guides/Shipping%20&%20fulfillment/Shipping%20Templates/Shipping-templates:-overview) 了解更多信息。

## 相关页面

[[Shipping-templates_-Overview]]
[[theory/Shipping-templates_-Assign-SKUs]]

---

> 来源：raw/Seller_Fulfillment_Services--Shipping_Templates--Shipping-templates_-add-settings-manually.md
