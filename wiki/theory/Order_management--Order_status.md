---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 订单状态管理（Order Status）

> 订单从确认到发货的全流程管理，包括追踪号更新、拆单、暂停销售。

## 核心操作

| 操作 | 说明 | 关键规则 |
|------|------|----------|
| [[theory/Acknowledge-orders-in-Seller-Center]] | 确认订单可履行 | 确认后状态从 New → Acknowledged |
| [[theory/Cancel-an-order-in-Seller-Center]] | 取消订单（不可逆）| 取消率必须 < 2% |
| [[theory/Update-tracking-numbers-in-Seller-Center]] | 上传追踪号 | 有效追踪率 ≥ 99% |
| [[theory/Split-customer-orders-in-Seller-Center]] | 拆单发货 | 每个包裹单独追踪 |
| [[theory/Pause-sales-&-order-operations]] | 暂停销售 | 库存归零 / 设置额外休息日 / 临时停用 |

## 取消订单流程

1. Orders 页面找到 PO#
2. 选择 Cancel order（部分发货订单：3个点→Cancel）
3. 选择取消原因
4. 确认（不可逆）

**注意：** 已发货订单无法取消。

## 追踪号更新

- 最多可编辑：标记已发货后 24 小时内或承运商首次扫描前（以较早者为准）
- 无效追踪或未达到 99% 标准 → 销售限制/暂停/终止

## 关联页面

- [[theory/Order_management]] — 订单管理总览
- [[theory/Cancel-fraudulent-orders]] — 欺诈订单处理
- [[theory/Troubleshoot-lost-or-undelivered-orders]] — 丢失/未送达订单
- [[theory/Troubleshoot-post-transaction-order-errors_-Incorrect-orders]] — 错误订单

---

> 源文件目录：`raw/Order_management--Order_status/`