---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Automotive Fitment: Add Missing Attributes and ACES Coverage

> 为汽车配件商品添加适配属性和 ACES 车辆兼容性数据

## 概述

为帮助确保您的列表在购物者使用 Walmart.com 上的 [Auto Parts Fitment widget](https://www.walmart.com/search?q=auto+filters) 时显示，您需要在文件中有 Aftermarket Catalog Exchange Standard (ACES) 记录。本指南介绍如何更新缺失的适配属性和提供 ACES 车辆兼容性数据。

## 核心步骤

### Step 1 — 开始

如果您还没有设置，需要先在 Walmart Marketplace 上设置您的汽车商品列表。

### Step 2 — 更新适配属性

必须更新 AAIA Brand ID、Manufacturer Part Number 和 Part Terminology ID 属性才能启用适配。

在 Seller Center 中选择 **Update items**。在 **Update items in bulk GTINs** 屏幕上，选择您的配送类型并选择 **By GTIN Match**。在框中添加商品的 GTIN 并选择 **Match**。选择 **Download** 按钮下载模板。

在模板中，您必须更新 Part Terminology ID、Manufacturer Part Number 和 AAIA Brand ID。

| 属性 | 来源 |
| --- | --- |
| AAIA Brand ID (BrandAAIAID) | ACES 文件的标题 |
| Manufacturer Part Number (Part) | ACES 文件中的每条记录 |
| Part Terminology ID (PartType id) | ACES 文件中的每条记录 |

完成后，将模板重新上传到 Seller Center。

**Pro 提示：** 您可以生成 **Fitment missing attributes** 报告来确保完成所有步骤。

### Step 3 — 上传文件

上传 ACES 或 PIES 文件前，确保每个文件符合我们的[文件要求](https://azure-na-assets.contentstack.com/v3/assets/blta7903c6b840b702d/blt6c2fd56f6019e9e4/Automotive-Fitment-file-requirements.pdf?branch=us_mplearn)。

有两种方式上传 ACES 和 PIES 文件：
- 使用 [Fitment landing page](https://seller.walmart.com/items-and-inventory/fitment-update)
- 在 Seller Center 中导航到您的 [**Catalog**](https://seller.walmart.com/catalog/list-items)，选择要更新的商品旁边的复选框，从 **Manage items** 下拉菜单中选择 **Update fitment info**

**灯泡附加指南：**
如果您的灯泡有多个 Part Type Applications，使用 PTID 11718 作为 Multi-Purpose Light Bulbs 来标记商品 Part Terminology ID。为每个兼容的特定 Part Terminology ID（PartType id）提供多个单独的 ACES 记录。

## 常见问题

**作为品牌所有者如何注册获取 AAIA Brand ID？**
直接从 Auto Care Association [注册获取 AAIA Brand ID](https://digital.autocare.org/data-standards-documentation/)。

**如何知道属性更新是否成功？**
在 Seller Center 的 [**Catalog**](https://seller.walmart.com/catalog/list-items) 页面，您可以查看适配产品详情并按 **Fitment Fit Type** 或 **Fitment Attributes** 筛选以检查信息是否缺失。

**为什么 ACES 报告中某些单元格为空？**
空白单元格表示您的产品缺少 ACES 覆盖或适配必填属性。**Fitment Missing ACES Report** 列出所有没有 ACES 覆盖的商品。

**为什么更新了适配属性并提供了 ACES 记录后商品仍出现在 Fitment Missing ACES Report 中？**
很可能是因为标记到商品的属性与 ACES 记录不完全匹配。标签到商品的 Part Terminology ID、AAIA Brand ID 和 Manufacturer Part Number 必须与 ACES 文件完全匹配（包括空格、连字符、下划线等）。

## 相关页面

[[theory/Item_setup--Overview]]
[[theory/Troubleshoot-product-ID-errors]]

---

> 来源：raw/Item_setup--Automotive_fitment--Automotive-Fitment_-Add-missing-attributes-and-ACES-coverage.md
