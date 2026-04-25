# WFS 库存管理（WFS Inventory Management）

> WFS 库存查看、补货、出库、转移与移除的完整指南。

## 访问路径

Seller Center → **WFS** → **Inventory**

## 库存状态说明

| 状态 | 说明 |
|------|------|
| **ATS（Available to Sell）** | 已接收、可供客户购买的库存 |
| **Reserved Units** | 已下单未发货（不计入 ATS，防止超卖）|
| **Inbound Units** | 已发送未到达仓库的在途库存 |
| **Damaged Receipts** | 接收时损坏、无法入库 |
| **Inventory Movement** | 因 MTR 正在转移中的库存 |
| **Inventory Review** | 接受合规/保质期/盘点检查（通常 24-48 小时）|

## 核心操作

### 补货

使用 [[theory/wfs-reports-inventory-health]] 中的 **Suggested Units** 列（预测需求 + 当前库存 + 在途）

### 转移（MTR）

将库存从当前仓库转移到另一个仓库 → [[wfs-inventory-movements-mtr]]

### 移除

处理库存（损坏/过期）或退回卖家 → [[WFS-inventory_-Remove-items-from-a-fulfillment-center]]

## 老化库存

超过 365 天收取 **$2.25/立方英尺/月** 长期仓储费  
详见 → [[theory/move-aged-inventory]]

## 相关页面

- [[theory/wfs-reports-inventory-health]] — 库存健康报告
- [[theory/move-aged-inventory]] — 清理老化库存
- [[wfs-inventory-movements-mtr]] — 库存转移
- [[theory/Shipping_to_WFS]] — 送仓流程

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--WFS_Inventory_management--manage-wfs-inventory.md`