---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Billing Dispute 账单争议处理

> 通过 High Radius EIPP 门户对 Walmart 广告账单提出争议的操作指南。

## 访问争议工具

账单争议通过 Walmart 的 Accounts Payable 门户 [High Radius](https://walmart.highradius.com/) 处理。

详细操作手册：[High Radius EIPP Guide](https://gecrm.my.salesforce.com/sfc/p/61000000ZKTc/a/KW00000035Wu/fipXq0.DxaGUTQDmAng.WljVOu1YlcUWPixRkXt5PZM)

---

## 开启争议的操作步骤

### Step 1 — 选择发票类型

登录 High Radius 后，进入 **EIPP** 模块，选择：

| Tab | 用途 |
|-----|------|
| **OPEN BILLS**（未结账单） | 查看当月未付款发票 |
| **CLOSED BILLS**（已结账单） | 查看当月已付款发票 |

如需查看历史发票，使用高级搜索功能，并在 *Customer Number* 列中填写 10 位客户编号。

### Step 2 — 选择要争议的发票

勾选需要争议的发票前的复选框，然后点击 **Dispute**。

> **提示**：如果找不到目标发票，使用高级搜索按客户编号搜索该供应商下的所有发票。

### Step 3 — 选择争议原因

点击 Dispute Reason 下拉菜单，选择合适的争议原因：

| 争议原因类型 | 说明 |
|-------------|------|
| Additional support documentation needed | 需要补充支持文档（如备份请求） |
| 其他原因 | 根据实际情况选择对应原因 |

### Step 4 — 填写争议金额

在 Dispute Amount 字段中点击蓝色区域，填写争议金额。

> **注意**：若金额超过千位，无需输入逗号。

### Step 5 — 填写说明

在 Comments 字段中，提供详细的事实陈述支持您的争议理由。如有支持邮件，建议：
1. 将邮件内容复制到 Word 文档
2. 作为附件上传

### Step 6 — 上传附件

点击 **Upload** 按钮，上传支持文档（如截图、邮件等）。

### Step 7 — 保存

点击 **Save** 完成争议提交。

---

## 争议管理

关于争议管理的详细说明，请参考 [High Radius EIPP Guide](https://gecrm.my.salesforce.com/sfc/p/61000000ZKTc/a/KW00000035Wu/fipXq0.DxaGUTQDmAng.WljVOu1YlcUWPixRkXt5PZM) 中的 **Dispute Management** 章节。

---

## 相关链接

- [[theory/Marketplace-sellers-Billing-Policy]] — Marketplace 卖家账单政策
- [[theory/Invoice-tracking-for-Walmart-suppliers]] — 供应商发票追踪
- [[theory/Invoice-request]] — 发票申请
- [[theory/Finding-IDs-and-account-names]] — 查找广告账户名称（提交工单时需用到）

---

> 来源：`raw/walmart advertising guide/Billing dispute.md`
> 更新：2026-04-17
