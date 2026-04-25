---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# WFS 退货规则设置（WFS Settings: Customize Return Rules）

> 自定义 WFS 退货处理方式：Restock / Return to Me / Dispose。

## 概述

当客户退货时，WFS 会检查商品状况并按你设置的退货规则处理。规则可按类别设置，也可对所有商品使用统一规则。

**权限要求：** 须拥有 Admin 或 Read and Write 访问权限。

## 三种处理方式

| 处理方式 | 说明 | 费用 |
|---------|------|------|
| **Restock（补货）** | 商品放回货架继续销售 | 免费 |
| **Return to Me（退回给我）** | 将商品退回卖家指定美国地址 | 按重量收费 |
| **Dispose（处置）** | 捐赠或丢弃 | 按重量收费 |

**默认规则：** 可售商品 → Restock；不可售商品 → Dispose

## 设置步骤

1. Seller Center → **Account settings** → **Returns**
2. 选择 **Walmart Fulfilled Returns**
3. **WFS Return Address**：添加退货接收地址
4. **WFS Return Preferences**：点击 Add Return Rules 设置退货处理规则
5. **Damages at Receiving**：设置入库时损坏商品的处理方式

## 关键规则

- 对于标记为"Walmart at fault"的退货，沃尔玛将保留商品（无论你设置的规则如何）
- 部分商品不适用客户退货（详见 [[theory/wfs-returns-overview]]）
- 退货地址必须为美国境内地址

## 相关页面

- [[theory/wfs-returns-overview]] — WFS 退货处理全流程
- [[theory/wfs-returns-overview]] — WFS 退货政策
- [[theory/WFS-seller-onboarding-setup]] — WFS 入驻设置

---

> 来源：`raw/Walmart_Fulfillment_Services__WFS_--Getting_started_with_WFS--WFS-settings-return-rules.md`
