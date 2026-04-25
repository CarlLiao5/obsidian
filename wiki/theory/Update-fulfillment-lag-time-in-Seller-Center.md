# 更新配送延迟时间（Update Fulfillment Lag Time）

> 为特定 SKU 设置备货延迟天数（超过 2 天备货须申请豁免）。

## 概述

**Fulfillment Lag Time**：卖家准备商品发货所需的天数。Walmart 要求在收到订单后 **2 个工作日内** 发货。如需更多备货时间，须申请豁免。

> Lag Time 超过 1 天必须通过豁免申请并获得批准。

## 更新方式

### 方式一：模板批量更新（推荐）

1. Seller Center → **Catalog** → **Update items** → **Update with file**
2. 下载 **Change fulfillment lag time** 模板
3. 填写 SKU 和对应 Lag Time（≤1 可直接填写；>1 须先有豁免批准）
4. 上传模板并 Submit
5. 生效时间：最快 15 分钟，最多 4 小时

> 每批次最多上传 **20,000** 条 SKU。

### 方式二：Catalog 页面直接更新

1. Catalog 页面 → **Columns** → 勾选 **Fulfillment lag time** → **Apply**
2. 在 Fulfillment lag time 列直接修改数字
3. 点击 **Update**

## 豁免申请

Lag Time > 1 天须先申请 → [[theory/Submit-a-lag-time-exemption-request]]

## 注意事项

- 仅在必要时添加 Lag Time（超过 1 天会限制 OneDay 和 TwoDay Delivery 计划的资格）
- Lag Time 由 Walmart 全权酌情批准，Walmart 有权随时修改豁免条件

## 相关页面

- [[theory/Fulfillment-methods_-overview]] — 配送方式总览
- [[theory/Submit-a-lag-time-exemption-request]] — 申请延迟豁免
- [[theory/Seller-performance-standards]] — 绩效标准（按时发货率）

---

> 来源：`raw/Seller_Fulfillment_Services--Fulfillment_settings--Update-fulfillment-lag-time-in-Seller-Center.md`