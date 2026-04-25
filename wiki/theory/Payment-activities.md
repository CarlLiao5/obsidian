---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 支付活动（Payment Activities）

> 支付报表中可能出现的资金延迟情况：支付储备、支付冻结、支付暂停。

## 三种支付活动类型

| 类型 | 说明 | 触发场景 |
|------|------|----------|
| **Payment Reserves（支付储备）** | 预留金额用于覆盖预期退款、退单或其他风险 | 正常业务行为；跨境进口预留运费 |
| **Payment Holds（支付冻结）** | 订单发货 7 天后可能冻结，冻结期结束后在下一周期处理 | 新卖家滚动冻结；账户审查 |
| **Payment Suspensions（支付暂停）** | 账户审查期间暂停所有资金发放 | 合规/法律问题审查 |

## 结算周期

- **双周结算**：每 14 天一次
- **Cut-off**：每周期结算截止时间（太平洋时间周五午夜）
- Cut-off 后到达的订单进入下一周期
- 结算周期可在 Statements 页面的 **Payment Information** 中查看

## 冻结触发原因

- 合规问题
- 客户订单争议
- 支付服务商审查
- 性能/风险审查
- 运输问题
- 预期发票
- 异常交易
- **法律问题**：TRO（临时限制令）、诉讼案件、CA Prop 65、UCC 留置权

## 新卖家冻结

详见 → [[theory/new-seller-payment-hold-policy]]（美国最长 14 天，非美国最长 21 天；解锁条件：90 天 + $7,500）

## 相关页面

- [[theory/Payment-processing]] — 收款方式配置
- [[theory/Payment-statements-and-transactions]] — 付款报表解读
- [[theory/final-settlement-payout-policy]] — 最终结算政策

---

> 来源：`raw/Taxes_&_payments--Payments--Payment-activities.md`