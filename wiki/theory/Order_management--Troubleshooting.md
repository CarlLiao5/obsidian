---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 订单管理故障排查（Order Management: Troubleshooting）

> 欺诈订单、丢失订单、错误订单及争议订单的处理指南。

## 欺诈订单处理

### 三种处理路径

| 场景 | 处理方式 |
|------|---------|
| 未发货且收到沃尔玛邮件通知 | Seller Center → Orders → 选择欺诈订单 → _Cancel – Fraud, stop shipment_ |
| 已发货 | 联系承运商发起 Stop Shipment → 成功后退款；联系支持获取运费补偿 |
| 未收到通知但疑似欺诈 | 发起 Cancel → 选择 _Fraud, stop shipment_ → _Contact Walmart Risk Prevention team_ |

**注意：** 只有沃尔玛确认欺诈后才能使用 _Cancel – Fraud, stop shipment_ 取消代码。若订单最终送达，请勿退款——沃尔玛将正常支付。

**欺诈审查时间：** 4 小时内完成审查。审查期间不影响绩效指标。

## 丢失/未送达订单

| 步骤 | 操作 |
|------|------|
| 1 | 检查 [[theory/Order_management--Order_status]] 中的订单状态和追踪信息 |
| 2 | 联系支持，提供订单号和追踪信息 |
| 3 | 如为 WFS 订单，参考 [[theory/wfs-returns-overview]] 中的丢失包裹处理流程 |

## 错误订单（Mispaced / Incorrect Orders）

客户收到错误商品或数量不符：
1. 登录 Seller Center → **Orders** → 找到相关订单
2. 联系支持，说明情况
3. 安排退回错误商品并补发正确商品

## 争议裁定申诉（Appeal a Dispute Decision）

如对沃尔玛裁定不满，可在 **30 天内提交一次申诉**：
- 路径：Seller Center → Help → 联系支持
- 终局裁定后不可再次申诉
- 详见 [[theory/Troubleshooting--Appeal-a-dispute-decision]]

## 信用卡拒付（Chargeback）

客户向金融机构提出争议：
- 详细政策：[[theory/Credit-Card-Chargeback-policy]]（Policies 层）
- 处理时限：响应银行要求的争议期限

## 相关页面

- [[theory/Order_management]] — 订单管理总览
- [[theory/Order_management--Order_status]] — 订单状态处理
- [[theory/Order_management--Returns_&_refunds]] — 退货退款处理
- [[theory/Troubleshooting--Appeal-a-dispute-decision]] — 争议申诉

---

> 来源：`raw/Order_management--Troubleshooting/` 下多个文件综合编译
