# Troubleshoot WFS inbound order issues

> WFS 货件计划的常见错误及解决方法

## 概述

当您向 Walmart 配送服务 (WFS) 发送库存时，您的货件计划可能会出现问题。这可能是由于信息不正确或系统错误。本指南将介绍常见错误及解决方法。

## 错误和下一步

| 错误消息 | 下一步 |
| --- | --- |
| Expected Delivery Date should be of future and not the past | 确保预计发货日期至少在 2 天后 |
| expectedDeliveryDate cannot be null/empty | 输入至少距今 2 天的预计发货日期 |
| itemQty should be product of innerPackQty and vendorPackQty | 检查商品数量、vendor pack 数量和 inner pack 数量至少为 1 |
| postalCode cannot be null/empty | 输入有效的邮编 |
| Shipment Plan is already created for this inbound order | 此货件计划 ID 已存在。请输入新的 |
| innerPackQty should be great then zero | inner pack 数量必须至少为 1 |
| vendorPackQty should be great then zero | vendor pack 数量必须至少为 1 |
| itemQty should be great then zero | 商品数量必须至少为 1 |
| sellerId and inboundOrderId is mandatory | 货件计划缺少您的 seller ID 和计划 ID |
| Error parsing json input | 模板缺少必需的列。下载新模板并重新提交 |
| Items Dimensions are not suitable for creating po for sku | 您的商品大于 WFS 的最大尺寸。我们允许商品最大 120" x 105" x 93" 和 500 磅 |
| Item is not WFS Eligible for sku | 该商品可能被禁止 |
| Item information is not present for sku | 您的商品可能未设置为 Walmart 配送 |

## 相关页面

[[theory/WFS-inbound-orders_-Send-inventory]]

---

> 来源：raw/Walmart_Fulfillment_Services__WFS_--Troubleshooting--Troubleshoot-WFS-inbound-order-issues.md
