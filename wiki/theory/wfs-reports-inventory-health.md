# WFS 库存健康报告（WFS Reports: Inventory Health）

> 了解 WFS 库存水平、入库状态、在途库存与补货建议的核心工具。

## 概述

WFS Inventory Health 报告提供商品级别的库存和销售信息，帮助卖家做出补货决策。

## 访问路径

- **Seller Center**：Reports → Inventory 部分
- **API**：参见 Walmart Developer Portal

## 关键指标

| 指标 | 说明 |
|------|------|
| **Available Units（ATS）** | 已接收、可供客户购买的库存 |
| **Reserved Units** | 已下单但未发货的库存（不计入 ATS，防止超卖）|
| **Inbound Units** | 已发送但尚未到达 WFS 仓库的在途库存 |
| **Damaged Receipts** | 接收时损坏、无法入库的库存 |
| **Inventory Movement** | 因 MTR（库存转移请求）正在移动中的库存 |
| **Inventory Review** | 正在接受合规、保质期、盘点或卖家申请的移除检查（通常 24-48 小时）|
| **Cube Used** | 商品在 WFS 网络中占用的立方空间 |
| **Suggested Units** | 基于预测销售需求和当前库存的建议补货量 |
| **First In Stock Date** | 商品首次到达配送中心的日期 |

## 重要提示

- 报告中的 ATS 更新频率**低于**库存页面（Inventory page）
- 报告导出可能需要额外时间（大报告）
- **Suggested Units** 基于：预测销售需求 + 当前 ATS + 在途库存

## 关联指标

- [[theory/wfs-inbound-orders-schedule-delivery-appointments]] — 送仓预约
- [[theory/manage-wfs-inventory]] — 库存管理
- [[wfs-reports-gmv-penetration]] — GMV 渗透报告

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 概览
- [[theory/WFS_Inventory_management]] — 库存管理全指南

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--WFS_reports--wfs-reports-inventory-health.md`
> 更新：2025-10-02