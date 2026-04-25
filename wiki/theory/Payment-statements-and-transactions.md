---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 支付报表与交易（Payment Statements and Transactions）

> 在 Seller Center 中查看支付汇总和交易详情，支持 90 天内订单查询。

## Statements（支付报表）

**Period Summary**：查看当前周期余额和计划结算日期
- 发货后 24-48 小时显示余额
- 可下载 Payments Report（对账报告）

## Payments Report 核心字段

| 字段 | 说明 |
|------|------|
| Order # | Walmart.com 订单号 |
| PO # | 采购订单号 |
| Transaction type | 交易类型（销售/退款）|
| SKU / GTIN | 商品识别 |
| Gross amount | 客户付款总额 |
| Net amount | 应付卖家金额 |
| Referral fee | 推荐费（佣金）|
| Referral fee % | 佣金率 |
| Shipping revenue | 运费收入 |
| Tax collected | 代收代缴税费 |

## Transactions（交易）

- 可搜索 PO# 或客户订单号
- 可按交易类型或日期筛选
- 可导出交易记录

## 结算周期

| 注册地 | 冻结期 | 解锁条件 |
|--------|--------|----------|
| 美国 | 最长 14 天 | 首次发货后 90 天 **且** $7,500 |
| 非美国 | 最长 21 天 | 首次发货后 90 天 **且** $7,500 |

详见 → [[theory/new-seller-payment-hold-policy]]

## 相关页面

- [[theory/Payment-processing]] — 收款方式配置
- [[theory/Payment-activities]] — 支付活动详解（储备/冻结/暂停）
- [[theory/final-settlement-payout-policy]] — 最终结算政策

---

> 来源：`raw/Taxes_&_payments--Payments--Payment-statements-and-transactions.md`