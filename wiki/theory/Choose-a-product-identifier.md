# 商品识别符政策（Choose a Product Identifier）

> GTIN / UPC / ISBN / EAN 四大类商品 ID 的要求、规则与常见问题。

## 概述

Product ID（商品识别符）是每件商品唯一的通用代码。Walmart 通过 GS1 数据库交叉验证商品 ID 的真实性和产品信息准确性。**无效商品 ID 将导致商品下架，甚至账户暂停。**

## 四种接受的商品 ID

| 类型 | 全称 | 适用场景 | 位数 |
|------|------|---------|------|
| **GTIN** | Global Trade Item Number | 通用，全球范围 | 14 位 |
| **UPC** | Universal Product Code | 通用，主要北美 | 12 位 |
| **ISBN** | International Standard Book Number | 仅书籍和出版物 | 10 或 13 位 |
| **EAN** | European Article Number | 主要欧洲 | 13 位 |

**注意：** SKU 号码和型号不是有效的商品 ID。

## 无效商品 ID 的情形

- 分配给优惠券、退款或限制流通编号的码
- 类型错误使用（如服装分配了图书专用码）
- 品牌注册与使用品牌不一致
- 由与品牌无关的公司注册的商品 ID

建议直接从 [GS1](https://www.gs1us.org/upcs-barcodes-prefixes/how-to-get-a-upc-barcode) 购买商品 ID，避免与 GS1 数据库出现差异。

## 关键规则

| 规则 | 说明 |
|------|------|
| 每件商品必须有唯一商品 ID | 即使 GTIN 和 UPC 同时存在，每件商品也需要独立 ID |
| **禁止复用** 商品 ID | 每个商品 ID 仅对应一件商品 |
| 品牌变更需新 ID | 主要品牌变更（如名称更换）需重新购买商品 ID；次要变更（如添加公司品牌名）无需新 ID |
| 格式要求 | 仅输入数字，不含破折号或空格 |

## GTIN 豁免

无商品 ID 的商品（如私标、手工首饰），可申请 GTIN/UPC 豁免：
- 豁免后配送选项：**仅支持 Seller Fulfilled**（设置时须选择）
- 上传成功后可转换为其他配送方式
- 详见 [[theory/request-a-gtin-exemption]]

## 相关页面

- [[theory/request-a-gtin-exemption]] — 申请 GTIN 豁免
- [[theory/Product-variant-groups_-Overview]] — 变体组建立需要商品 ID
- [[theory/Item_setup--Overview]] — 商品设置总览

---

> 来源：`raw/Policies_&_standards--Product_listings--Choose-a-product-identifier.md`
