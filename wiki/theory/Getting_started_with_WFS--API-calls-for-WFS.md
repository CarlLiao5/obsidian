---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# WFS API 集成（API Calls for WFS）

> 通过 Walmart Marketplace API 自动化 WFS 全流程——商品管理、库存、入库订单等。

## 概述

Walmart Marketplace APIs 在你的系统与 WFS 之间建立无缝数据交换。通过 API，无需登录 Seller Center 即可完成几乎所有 WFS 操作。

**前置条件：** 需要 Client ID 和 Client Secret 生成访问令牌（每次 API 调用都需重新生成）。

## 核心功能

| 功能 | 对应 API |
|------|---------|
| 添加/转换商品 | `POST Convert items for WFS` |
| 检查商品是否因危险品被搁置 | `GET Item compliance` |
| 查看/更新库存 | `GET / WFS inventory`, `PUT / WFS inventory` |
| 创建入库配送计划 | `POST Inbound orders` |
| 推荐入库数量 | `GET Restock recommendations` |
| 获取支付和库存健康报告 | `GET WFS Reports` |

API 文档入口：[Developer Portal](https://developer.walmart.com/us-marketplace)

## 推荐 API

| API | 用途 |
|-----|------|
| [Restock Recommendations](https://developer.walmart.com/us-marketplace/docs/get-wfs-restock-recommendations) | 根据当前库存和销售预测，推荐应补货的 WFS 商品 |
| [Fulfill with WFS Recommendations](https://developer.walmart.com/us-marketplace/docs/get-wfs-convert-recommendations) | 列出最适合从自配送转为 WFS 的商品 |
| [Unpublished Recommendations](https://developer.walmart.com/us-marketplace/docs/get-wfs-unpublished-recommendations) | 查看当前未发布的 WFS 商品及原因 |

## 第三方服务商

| 类型 | 服务范围 | 代表方案商 |
|------|---------|---------|
| 全套服务 | 商品设置、库存、订单履约、定价 | ChannelEngine, Rithum, Sellercloud |
| 专业服务 | 特定业务功能 | GeekSeller, Zentail |

接入方式：在 Seller Center → **Apps** 页面连接已批准的方案商。

## 注意事项

- 查看 WFS 订单需将 `shipNodeType` 设为 `WFSFulfilled`（默认仅返回自配送订单）
- Walmart Preferred Carrier 报价目前不支持通过 API 获取 FTL 报价
- WPC 首选承运商报价目前不通过 API 提供 FTL

## 相关页面

- [[theory/Walmart_Fulfillment_Services__WFS_]] — WFS 总览
- [[theory/WFS-seller-onboarding-setup]] — WFS 入驻设置
- [[theory/WFS_Inventory_management]] — WFS 库存管理
- [[theory/Shipping_to_WFS]] — 送仓全流程

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--Getting_started_with_WFS--API-calls-for-WFS.md`
