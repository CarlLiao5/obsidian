---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 取消订单（Cancel an Order）

> 订单状态管理中取消订单的完整流程、取消率要求与常见问题处理。

## 概述

Walmart **不推荐**取消订单，因为它会：
1. 负面影响客户体验
2. 拉高[[theory/Seller-performance-standards|取消率]]（Cancel Rate）
3. 影响[[theory/Product-detail-page_-the-buy-box|Buy Box]]绩效

卖家须保持取消率 **< 2%**。

## 取消流程

### Step 1 — 找到订单

在 Seller Center 的 **Orders** 仪表板中定位对应订单（Purchase Order #）。

### Step 2 — 发起取消

- **取消整个订单**：在订单行点击 **Cancel order**
- **部分取消**（部分发货的订单）：点击右侧三个点 → **Cancel**（仅限未发货商品）

### Step 3 — 选择原因并确认

从下拉列表中选择取消原因，点击 **Cancel order** 确认。
如改变主意，选择 **Do not cancel order** 关闭操作窗口。

## 常见场景

| 场景 | 处理方式 |
|------|----------|
| **缺货取消** | 订单取消后，商品在该仓库标记为 unavailable，防止后续订单再触发取消 |
| **已发货订单** | 无法取消；可参考 [[theory/Issue-adjustments-or-non-standard-refunds-in-Seller-Center]] 申请退款 |
| **客户主动要求取消** | 在 Seller Center 中收到通知，按上述流程处理 |
| **商品已在承运商手中** | 建议客户收到商品后从 Walmart 账户发起退货 |

## 关键限制

- 订单标记为 Shipped 或 Canceled 后视为**关闭**，无法修改
- 取消不可逆，操作前请确认无其他替代方案

## 相关页面

- [[theory/Order_management]] — 订单管理总览
- [[theory/Order_management--Order_status]] — 订单状态管理
- [[theory/Pause-sales-&-order-operations]] — 暂停销售与订单操作
- [[theory/Seller-performance-standards]] — 绩效标准（取消率要求）
- [[theory/Issue-adjustments-or-non-standard-refunds-in-Seller-Center]] — 已发货订单退款处理

---

> 来源：`raw/Order_management--Order_status--Cancel-an-order-in-Seller-Center.md`
> 更新：2025-10-06