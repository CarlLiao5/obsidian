---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 送仓至 WFS（Shipping to WFS）

> 将库存从卖家仓库发送至 Walmart 配送中心的完整流程。

## 核心子页面

| 页面 | 说明 |
|------|------|
| [[theory/wfs-inbound-orders-schedule-delivery-appointments]] | 预约送货（LTL/FTL 须预约，小包裹无需预约）|
| [[theory/WFS-inbound-orders_-Send-inventory]] | 创建运输计划（6步流程）|
| [[theory/WFS-inbound-orders-Prepare-and-pack-shipments]] | 包装与准备要求 |
| [[theory/WFS-inbound-orders-Labels]] | 标签要求（主箱标签、收货标签）|
| [[WFS-inbound-orders-Select-&-pack-pallets]] | 托盘选择与打板 |
| [[WFS-inbound-orders_-Select-containers-and-dunnage]] | 集装箱选择与填充材料 |
| [[theory/WFS-inbound-orders-Shipment-routing-overview]] | 路由与承运商要求 |
| [[WFS-inbound-orders-Choose-a-shipment-method]] | 运输方式选择（ITS/直送）|
| [[wfs-inbound-orders-receiving]] | 收货流程与状态跟踪 |
| [[WPC-set-up-shipments]] | WPC 承运商发货设置 |
| [[WPC-prepare-pickup]] | WPC 提货准备 |
| [[WPC-track-shipments]] | WPC 追踪 |
| [[theory/WFS-Inventory-Transfer-Services]] | ITS 库存转移服务（单仓发送→全国分发）|
| [[theory/WFS-prep-services]] | WFS 预处理服务 |

## 送仓流程

```
Step 1：创建运输计划
  → [[theory/WFS-inbound-orders_-Send-inventory]]
  选择国内或跨境 → 添加商品（搜索或上传）→ 选择仓库/ITS → 选择承运商（WPC或自有）
  ↓
Step 2：准备发货
  → [[theory/WFS-inbound-orders-Prepare-and-pack-shipments]]
  标签（GTIN/UPC、原产国）→ 包装（保护材料）→ 托盘（40"×48" GMA A级）
  ↓
Step 3：预约交货
  → [[theory/wfs-inbound-orders-schedule-delivery-appointments]]
  LTL/FTL：提前预约（小包裹无需预约）
  ↓
Step 4：跟踪接收
  → [[wfs-inbound-orders-receiving]]
  Shipping Plans 页面跟踪 → Inbound Orders 页面查看接收状态
```

## WPC（Walmart 首选承运商）

- 支持包裹、LTL、FTL
- 折扣费率，运费从 WFS 销售扣款
- LTL/FTL 可从制造商/供应商地址提货
- 仅限美国本土 48 州，危险品禁运

## ITS（库存转移服务）

- 单仓发送 → Walmart 全国分发
- 费用：≤1lb $0.25；>2lb $0.35 + $0.10/lb
- 适合可分类库存，4 个工作日内部分库存可售

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 总览
- [[theory/Select-items-for-WFS]] — 选品要求
- [[theory/wfs-reports-inventory-health]] — 库存健康报告

---

> 源文件目录：`raw/Walmart_Fulfillment_Services__WFS_--Shipping_to_WFS/`