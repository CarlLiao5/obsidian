---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# WFS 账单信息设置（WFS Settings: Billing Information）

> 在 Seller Center 中添加和管理 WFS 账单支付方式（信用卡或 ACH 银行账户）。

## 概述

WFS 账单用于自动支付：履约费、仓储费、客户退款及扣款。只有销售额不足以覆盖费用时才扣款，不收取处理费。

**权限要求：** 须拥有 Admin 或 Read and Write 访问权限。

## 支持的支付方式

| 类型 | 说明 |
|------|------|
| 信用卡 | Visa / Mastercard / Amex / Discover / JCB / UnionPay（须为商业信用卡） |
| ACH 银行账户 | 任何美国银行 ACH 网络账户（如 Citibank、Bank of America） |

账单周期与结算周期一致（如每两周结算，账单也每两周生成）。

## 银行账户验证（ACH）

使用 microdeposit（小额验证存款）方式验证：
1.沃尔玛存入两笔 $0.01–$0.99 的小额款项
2. 账户到账后，在 Seller Center 输入两笔金额完成验证
3. 验证通常需要 **2–3 个工作日**
4. 验证完成后，microdeposit 款项将在 3 个工作日内从账户中提取

**常见失败原因：**
- 银行账户设置了限制 → 联系银行移除限制或申请例外
- 银行不接受 ACH 存款 → 更换银行账户

## 设置路径

**Seller Center → Account Settings → Billing Services → Add billing method**

账单失败时：检查余额是否充足、账户是否有 active holds；联系银行或信用卡机构。

## 相关页面

- [[theory/WFS-seller-onboarding-setup]] — WFS 入驻设置
- [[theory/WFS-fees]] — WFS 费用详解
- [[theory/Payment-processing]] — 付款处理

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--Getting_started_with_WFS--WFS-settings-billing-information.md`
