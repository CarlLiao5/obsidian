---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 付款处理（Payment Processing）

> Walmart Marketplace 的收款方式、结算周期与付款服务商配置。

## 概述

卖家可通过 Marketplace Wallet 或第三方服务商收取 Walmart Marketplace 的销售款项。

## 收款方式

### Marketplace Wallet（市场钱包）

- 内置于 Walmart 平台的存款账户
- 款项先存入钱包，再通过 ACH 转账至绑定的美国商业银行账户
- 无隐藏费用，钱包账户名须与银行账户名一致

### 第三方服务商

| 实体注册地 | 可选服务商 |
|------------|------------|
| 美国 | Marketplace Wallet、Hyperwallet、Payoneer、PingPong |
| 中国/香港 | Payoneer、PingPong、LianLian、Airwallex、WorldFirst、NetEase |
| 加拿大 | Payoneer |
| 其他国家 | Payoneer、PingPong |

**注意：** 同时只能配置一家收款服务商；如通过 Payoneer 直链注册而非 Seller Center 内注册，提取资金可能产生 $1.50 手续费。

## 结算周期

- **默认周期**：每 14 天（双周）结算一次
- **新卖家：** 订单发货后约 28 天收到款项（滚动延迟）
- **Cut-off 时间：** 在 Statements 页面的 Payment Information 中查看，Cut-off 后的发货通知将在下一周期结算

## 结算计算

付款金额 = 销售收入 − 各类费用（含推荐费、退款等）

## 付款暂停/延迟情况

以下情况可能导致付款暂停或延迟：
- 高退货率或高拒付率
- 销售假冒或非法商品

## 相关页面

- [[theory/Taxes_&_payments]] — 税务与支付总览
- [[theory/new-seller-payment-hold-policy]] — 新卖家付款冻结政策
- [[theory/final-settlement-payout-policy]] — 结算与放款政策
- [[marketplace-wallet-apply-and-enroll]] — 市场钱包注册
- [[theory/Payment-statements-and-transactions]] — 付款报表

---

> 来源：`raw/Taxes_&_payments--Payments--Payment-processing.md`