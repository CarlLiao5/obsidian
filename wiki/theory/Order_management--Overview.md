---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 订单管理子分类

> [[theory/Order_management]] 的详细子分类索引。

## 子分类

| 子分类 | 说明 | 页面数 |
|--------|------|--------|
| [[theory/Order_management--Order_status]] | 订单状态管理（确认/取消/追踪/拆单/暂停）| 1 |
| [[theory/Order_management--Customer_care]] | 客户服务（响应政策/消息回复/邮件模板）| 1 |
| [[theory/Order_management--Returns_&_refunds]] | 退款与退货（退款/退货规则/Keep It/Replacement）| 1 |
| [[theory/Order_management--Troubleshooting]] | 订单问题排查（欺诈/丢失/错误/退款争议）| 1 |

## 订单生命周期

```
收到订单 → [[theory/Acknowledge-orders-in-Seller-Center]]（确认订单）
    ↓
发货准备 → [[theory/Pause-sales-&-order-operations]]（如需要暂停）
    ↓
发货   → [[theory/Update-tracking-numbers-in-Seller-Center]]（上传追踪号）
          [[theory/Split-customer-orders-in-Seller-Center]]（如需拆单）
    ↓
标记已发货 → Seller Center
    ↓
客户问题 → [[theory/Respond-to-customer-messages-in-Seller-Center]]
    ↓
退货   → [[theory/returns-policy]] → [[theory/Add-a-Keep-It-Rule]] / [[theory/Create-item-level-return-rules]]
```

## 关键规则

- 取消率必须 **< 2%**（→ [[theory/Seller-performance-standards]]）
- 有效追踪率必须 **≥ 97%**
- 客户消息须 **48 小时内**回复（BBB/总检察长投诉：**1 小时内**）
- 超过 95% 响应率要求

## 关联分类

- [[theory/Seller_Fulfillment_Services]] — 配送履约
- [[theory/Policies_&_standards--Orders_&_returns]] — 订单与退货政策层
- [[theory/wfs-returns-overview]] — WFS 退货

---

> 源文件目录：`raw/Order_management/`