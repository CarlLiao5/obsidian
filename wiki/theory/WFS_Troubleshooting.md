# WFS 故障排查（WFS Troubleshooting）

> 解决 WFS 仓储配送相关的常见问题，包括入库问题、订单切换和商品 Feed 错误。

## 概述

WFS Troubleshooting 模块帮助卖家识别和解决使用 WFS 过程中遇到的各类问题。

### 问题分类

#### 入库问题（Inbound Issues）

| 问题类型 | 解决方向 |
|---------|---------|
| **入库数量差异** | 开调查case，需在到货后10-50天内提交 |
| **入库拒收/退货** | 检查商品合规性、尺寸/重量限制 |
| **入库追踪问题** | 确认追踪号有效、发货地址正确 |

#### 订单切换问题（Fulfillment Switch）

当 WFS 库存售罄后，订单可能切换为卖家自配送：

| 情况 | 卖家责任 |
|-----|---------|
| 切换为Seller Fulfilled | 卖家需自行履约或设置库存为0 |
| 绩效影响 | 不履约或频繁取消会影响绩效指标 |

**预防措施**：
- 定期检查库存状态
- 及时补货到 WFS
- 审核未发货订单

#### 商品 Feed 错误

批量添加/转换 WFS 商品时可能遇到的错误：

| 常见错误 | 解决方法 |
|---------|---------|
| 缺少尺寸/重量 | 在 Trade Item Configurations 标签填写 |
| 缺少电池类型 | 选择电池类型或"Dose Not Contain a Battery" |
| 缺少原产国 | 填写商品制造国家 |
| 缺少售价 | 填写商品价格 |
| Hazmat 审核中 | 等待最多3个工作日 |

### 提交调查的要求

对于入库数量差异调查：

| 承运商 | Parcel | LTL/FTL |
|-------|--------|---------|
| **WPC** | 无需文件 | 提单（BOL）含发货人和承运商签收 |
| **非WPC** | 交付证明 | 提单（BOL）含发货人和承运商签收 |

调查窗口：到货后 **10-50 天**

## 子页面列表

| wiki 页面名 | 说明 | 源文件 |
|------------|------|--------|
| [[Troubleshoot-WFS-receiving-issues_-open-a-dispute-claim]] | 入库问题调查申请 | `Walmart_Fulfillment_Services__WFS_--Troubleshooting--Troubleshoot-WFS-receiving-issues_-open-a-dispute-claim.md` |
| [[Troubleshoot-Walmart-fulfilled-orders-switching-to-seller-fulfilled]] | WFS 订单切换为自配送的排查 | `Walmart_Fulfillment_Services__WFS_--Troubleshooting--Troubleshoot-Walmart-fulfilled-orders-switching-to-seller-fulfilled.md` |
| [[theory/Troubleshoot-WFS-inbound-order-issues]] | 入库订单常见错误和解决方法 | `Walmart_Fulfillment_Services__WFS_--Troubleshooting--Troubleshoot-WFS-inbound-order-issues.md` |
| [[Troubleshoot-item-feed-errors]] | 商品 Feed 模板错误排查 | `Walmart_Fulfillment_Services__WFS_--Troubleshooting--Troubleshoot-item-feed-errors.md` |

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 总览
- [[theory/Getting_started_with_WFS]] — WFS 入门指南
- [[theory/WFS_item_setup]] — WFS 商品设置
- [[theory/Shipping_to_WFS]] — 配送到 WFS
- [[theory/Order_management--Troubleshooting]] — 订单管理问题排查
- [[theory/Walmart-Multichannel-Solutions]] — WFS 多渠道配送
- [[theory/WFS-prep-services]] — WFS Prep 服务
- [[theory/wfs-prohibited-products-policy]] — WFS 禁售商品

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--Troubleshooting`
