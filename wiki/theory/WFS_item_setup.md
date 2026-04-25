---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# WFS 商品设置

> 将商品转换为 WFS 履约的完整指南，包括选品、转换、危险品、多箱商品设置。

## 核心子页面

| 页面 | 说明 |
|------|------|
| [[theory/Select-items-for-WFS]] | 选择适合 WFS 的商品（尺寸/重量/要求） |
| [[Convert-seller-fulfilled-items-to-WFS]] | 将现有自配送商品转为 WFS |
| [[WFS-hazmat-item-setup]] | 危险品（化学品/电池/农药）合规设置 |
| [[WFS-big-and-bulky-items]] | 大件商品设置（>150lb）|
| [[WFS-multi-box-items]] | 多箱商品设置 |
| [[WFS-item-spec-sheet-setup]] | 商品规格表设置 |
| [[WFS-compliance-safety-data-sheets]] | 安全数据表（SDS）要求 |
| [[WFS-compliance-batteries-FAQ]] | 电池合规 FAQ |
| [[theory/wfs-prohibited-products-policy]] | WFS 禁售商品政策 |
| [[Item-setup-methods_-Overview]] | 商品设置方法总览 |

## WFS 商品要求

| 要求 | 限制 |
|------|------|
| 最大重量 | 500 lb（含包装）|
| 最大尺寸 | 120" × 105" × 93"（含包装）|
| 温度控制 | 不支持 |
| 发货地 | 美国境内或清关后到达 |

## 商品设置流程

```
选择商品 → [[theory/Select-items-for-WFS]]
    ↓
转换为 WFS → [[Convert-seller-fulfilled-items-to-WFS]]（单个）或批量模板
    ↓
危险品（如有）→ [[WFS-hazmat-item-setup]]（3工作日审查）
    ↓
大件/多箱 → [[WFS-big-and-bulky-items]] / [[WFS-multi-box-items]]
    ↓
提交并跟踪 → Activity Feed（最多24小时）
```

## 关键规则

- 含有化学品、气雾剂、农药、电池（含锂电池）的商品须额外信息并通过合规审查
- 危险品审查需要 **3 个工作日**
- WFS 商品不可更改 SKU 或 Product ID
- 新商品通过合规审查后自动上架

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 总览
- [[theory/WFS-seller-onboarding-setup]] — WFS 入驻流程
- [[theory/Shipping_to_WFS]] — 送仓

---

> 源文件目录：`raw/Walmart_Fulfillment_Services__WFS_--WFS_item_setup/`