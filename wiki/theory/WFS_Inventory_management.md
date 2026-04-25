# WFS 库存管理

> WFS 库存的查看、补货、出库、转移与移除完整指南。

## 核心子页面

| 页面 | 说明 |
|------|------|
| [[theory/manage-wfs-inventory]] | WFS 库存查看与补货 |
| [[wfs-inventory-health-page]] | 库存健康诊断（ATS/预留/损坏/在途）|
| [[wfs-inventory-movements-mtr]] | 库存转移（MTR）：仓库间调拨 |
| [[outbound-wfs-shipments]] | WFS 出库（配送给客户）|
| [[WFS-inventory_-Remove-items-from-a-fulfillment-center]] | 从仓库移除库存（处理/退回）|
| [[manage-wfs-multi-box-inventory]] | 多箱库存管理 |
| [[theory/move-aged-inventory]] | 清理老化库存（超过365天收取长期仓储费）|

## 库存状态说明

| 状态 | 说明 |
|------|------|
| **ATS（Available to Sell）** | 已接收、可供客户购买的库存 |
| **Reserved Units** | 已下单未发货（不计入 ATS，防止超卖）|
| **Inbound Units** | 已发送未到达仓库的在途库存 |
| **Damaged Receipts** | 接收时损坏、无法入库 |
| **Inventory Movement** | 因 MTR 正在转移中的库存 |
| **Inventory Review** | 正在接受合规/保质期/盘点检查（24-48小时）|

## 关键操作

### 补货

- 使用 [[theory/wfs-reports-inventory-health]] 中的 **Suggested Units** 列（预测需求 + 当前库存 + 在途）
- 或通过 [[theory/Success-Hub-Overview]] → Restock WFS items 建议

### 转移（MTR）

- [[wfs-inventory-movements-mtr]] — 在仓库间转移库存

### 移除

- [[WFS-inventory_-Remove-items-from-a-fulfillment-center]] — 移除处理（≤2lb $0.35 + $0.20/lb；退货 $4.70-$155）

### 老化库存

- 超过 365 天收取 **$2.25/立方英尺/月** 长期仓储费
- 使用 Optimize 面板：调价 / 优化内容 / SEM / 多渠道
- 或直接移除库存

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 总览
- [[theory/wfs-reports-inventory-health]] — 库存健康报告
- [[theory/Success-Hub-Overview]] — 成功中心补货建议

---

> 源文件目录：`raw/Walmart_Fulfillment_Services__WFS_--WFS_Inventory_management/`