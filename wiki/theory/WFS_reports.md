# WFS 报告体系

> 12 种 WFS 报告的完整索引与用途说明。

## 报告分类

| 报告 | 说明 | 用途 |
|------|------|------|
| [[theory/wfs-reports-inventory-health]] | 库存健康（ATS/在途/损坏/建议补货量）| 补货决策 |
| [[wfs-reports-gmv-penetration]] | GMV 渗透率（12周/每日/单品级 WFS 销售占比）| 增长分析 |
| [[wfs-reports-inbound-receipts]] | 入库收货（期望数量/签入/接收/损坏）| 入库争议 |
| [[wfs-reports-inbound-transportation]] | 入库运输（运输方式/成本/时效）| 运输管理 |
| [[wfs-reports-orders]] | WFS 订单报告 | 销售分析 |
| [[wfs-reports-customer-returns]] | 客户退货（退货原因/责任归属/处置结果/RTV）| 退货分析 |
| [[wfs-reports-item-conversion]] | 商品转换报告（WFS vs 自配送 GMV）| 转换效果 |
| [[wfs-reports-storage-report-overview]] | 存储报告（当前库存/长期仓储费）| 成本管理 |
| [[wfs-reports-settlement]] | WFS 结算报告 | 对账 |
| [[Marketplace-and-WFS-payment-report-overview]] | Marketplace + WFS 合并支付报告 | 财务核对 |
| [[wfs-reports-inventory-reconciliation]] | 库存对账报告 | 库存准确性 |

## 访问路径

- Seller Center → **WFS** → **Reports**
- 或 API 接入（Developer Portal）

## 关键指标

- **ATS 365+ days**：超365天长期仓储费触发
- **ATS 271–365 days**：即将产生长期费
- **Suggested Units**：建议补货量（预测需求+当前库存+在途）

## 相关页面

- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 总览
- [[theory/WFS_Inventory_management]] — 库存管理
- [[theory/move-aged-inventory]] — 清理老化库存

---

> 源文件目录：`raw/Walmart_Fulfillment_Services__WFS_--WFS_reports/`