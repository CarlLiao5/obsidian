---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# GS1 数据库与商品 ID 交叉验证

> 解释沃尔玛如何通过 GS1 数据库验证商品 ID（GTIN/UPC/EAN/ISBN）的真实性，以及卖家如何在 GS1 官网注册、查询和管理商品 ID。
>
> **来源**：整合自 [[theory/Choose-a-product-identifier]]（商品识别符政策）、[[theory/Onboarding-Guide--New-Employee-Training]]（新员工培训）、[[theory/HOME-卖家运营白皮书]]（政策收紧预警）、[[theory/Troubleshoot-product-ID-errors]]（ID 错误排查）、[[theory/Troubleshoot-item-setup-errors]]（无效 ID 错误）。
>
> **更新日期**：2026-04-21

---

## GS1 是什么

**GS1**（Global Standards One）是一个全球性非营利组织，负责制定和管理商品识别符的国际标准。GS1 体系确保每一件商品在全球范围内拥有唯一的"身份证号码"。

GS1 在各国有分支机构，其中美国为 **GS1 US**（[gs1us.org](https://www.gs1us.org)），负责北美地区的 UPC/GTIN 分配与管理。

---

## Walmart 如何进行 GS1 数据库交叉验证

### 验证机制

当卖家提交商品时，Walmart 会将商品 ID（GTIN/UPC）与 GS1 数据库中的注册记录进行比对，核验以下信息：

| 验证维度 | 说明 |
|---------|------|
| **ID 有效性** | 该商品 ID 是否真实存在于 GS1 数据库 |
| **注册人一致性** | GS1 数据库中注册的 brand owner（品牌所有者）是否与卖家账号信息一致 |
| **产品信息匹配** | GS1 数据库中的产品名称、描述、类目是否与提交内容一致 |
| **ID 类型合法性** | 是否为 GTIN/UPC/EAN/ISBN 之一，位数是否正确 |
| **唯一性** | 同一商品 ID 是否被多个卖家重复使用 |

### 政策收紧时间线

> **重要预警**：根据官方公告，Walmart 对 GS1 数据库和商品 ID 的交叉核验**暂定于 2025 年 12 月后全面启动**。届时，未在 GS1 官方注册的 UPC/GTIN 将直接导致商品审核被拒或已上架商品被下架。

### 验证失败的后果

| 错误类型 | 触发场景 | 后果 |
|---------|---------|------|
| **Invalid Product ID** | ID 格式错误或不在 GS1 数据库 | 商品审核被拒，无法上架 |
| **未授权使用 Product ID** | 使用了其他品牌注册的 ID | 商品下架 + 账户警告 |
| **品牌不一致** | GTIN 注册品牌与当前卖家不符 | 商品被抑制（suppressed） |
| **重复 Product ID** | 同一 ID 被多个卖家使用 | listing 合并或下架 |

---

## 四种商品 ID 类型

|| 类型 | 全称 | 适用商品 | 位数 | 来源 |
|------|------|------|---------|------|------|
| **GTIN** | Global Trade Item Number | 通用商品 | 14 位 | GS1 US 购买 |
| **UPC** | Universal Product Code | 主要北美商品 | 12 位 | GS1 US 购买 |
| **ISBN** | International Standard Book Number | 图书/出版物 | 10 或 13 位 | 出版社/ISBN 机构 |
| **EAN** | European Article Number | 欧洲商品 | 13 位 | 制造商提供 |

### 重要规则

- **SKU 和型号不是有效的商品 ID**
- **每件商品必须有唯一 ID**，即使同一商品同时拥有 GTIN 和 UPC，也需要各自对应不同的商品
- **禁止复用**：每个商品 ID 仅对应一件商品，不可重复分配给其他商品
- **品牌变更需重新购买 ID**：主要品牌变更（如品牌名称更换）需重新购买商品 ID；次要变更（如添加公司品牌名）无需新 ID
- **EAN 不能用于 Walmart Fulfillment（WFS）标签**：必须使用 GTIN 或 UPC

---

## 如何注册/购买 GS1 商品 ID

### GS1 US 官网购买流程

1. **访问**：[gs1us.org](https://www.gs1us.org)
2. **选择套餐**：GS1 US 提供不同规模的包（从 1 个 UPC 到大量 GTIN 不等）
3. **公司前缀注册**：购买公司前缀（GS1 Company Prefix），这是分配商品 ID 的基础
4. **分配商品 ID**：在获得前缀后，自行为每件商品分配唯一的 GTIN/UPC
5. **在 GS1 数据库更新产品信息**：购买 ID 后需将产品信息（名称、描述、图片、类目）录入 GS1 数据库

### 常见陷阱

> ⚠️ **踩坑警告**：从**非 GS1 官方渠道**购买的 UPC/GTIN 通常是他人已注册过的条码，即使能用也会在 Walmart 的品牌一致性验证中失败。**必须从 GS1 US 官网直接购买**，才能确保 ID 与自己的品牌信息绑定。

常见无效来源：
- eBay / 淘宝等第三方平台购买的便宜条码
- 前任品牌所有者遗留的条码
- 制造商分配给其他公司的条码

### 何时需要新 ID

| 场景 | 是否需要新 ID |
|------|------------|
| 全新自有品牌商品 | ✅ 需要新购 |
| 已有 GTIN/UPC 的品牌商品 | ❌ 沿用制造商提供的 ID |
| 品牌改名（主要变更） | ✅ 需要新购 |
| 新增 SKU 变体（颜色/尺寸） | ✅ 每个变体需要独立 ID |
| 手工/私标商品（无品牌 ID） | 可申请 [[request-a-gtin-exemption\|GTIN 豁免]] |

---

## 如何查询/验证现有商品 ID

### 在 GS1 数据库查询

**GEPIR**（Global Electronic Party Information Register）：[gepir.gs1.org](https://gepir.gs1.org)

可输入任意 GTIN/UPC/EAN，查询该 ID 的注册信息：
- 品牌所有者名称
- 商品名称
- 注册时间

### 在 Walmart Seller Center 排查

如果商品 ID 报错，参考 [[theory/Troubleshoot-product-ID-errors]] 和 [[theory/Troubleshoot-item-setup-errors]]：

1. 检查商品 ID 位数是否正确（GTIN 14 位 / UPC 12 位）
2. 在制造商官网或包装上核实条码
3. 通过 GEPIR 确认注册人是否为你的品牌
4. 如确认 ID 有效但系统报错，联系 Seller Support

---

## GTIN 豁免（无 ID 的替代方案）

对于**私标商品、手工商品或确实无法获得商品 ID** 的情况，可申请 GTIN 豁免：

- 申请路径：Seller Center → Catalog → **GTIN Exemptions**
- 审批时间：最多 3 个工作日
- 适用范围：自有品牌、手工首饰、无制造商 ID 的定制商品
- 详见 [[theory/request-a-gtin-exemption]]

---

## WFS 商品的特殊要求

| 要求 | 说明 |
|------|------|
| 必须有可扫描条码 | 每个可销售单位必须有 GTIN/UPC 条形码标签 |
| EAN 不可用 | WFS 不接受 EAN 作为产品标识符 |
| 禁止覆盖原有条码 | 不要移除或覆盖制造商条码；如条码无法扫描，WFS 会重新贴标 |
| 变体独立条码 | 每个变体商品必须有唯一的条形码 |
| WFS 商品不可更改 Product ID | 一旦入仓，SKU 和 Product ID 均不可修改 |

---

## 运营行动清单

> 新品上架前必做：

- [ ] 确认商品 ID 类型（GTIN/UPC/ISBN/EAN）
- [ ] 验证 ID 在 GS1 数据库存在且品牌名一致（[gepir.gs1.org](https://gepir.gs1.org)）
- [ ] 如为自有品牌，从 [gs1us.org](https://www.gs1us.org) 购买公司前缀并分配 GTIN
- [ ] 在 GS1 数据库中完整录入产品信息（名称/描述/类目）
- [ ] 确认每个 SKU 变体拥有独立 ID
- [ ] 测试打印条码，确保可扫描

---

## 相关页面

**商品 ID 政策**
- [[theory/Choose-a-product-identifier]] — 商品识别符政策（四种 ID 详解）
- [[theory/request-a-gtin-exemption]] — 申请 GTIN 豁免
- [[theory/Troubleshoot-product-ID-errors]] — 商品 ID 错误排查
- [[theory/Troubleshoot-item-setup-errors]] — 上架错误排查（含无效 ID 章节）
- [[Update-a-product-ID]] — 更新商品识别符

**重复 listing**
- [[theory/duplicate-listings-policy]] — 重复 listing 政策
- [[theory/manage-duplicate-listings-in-seller-center]] — 重复 listing 处理

**WFS 相关**
- [[theory/WFS-inbound-orders-Labels]] — WFS 标签指南（含条形码要求）
- [[theory/Getting_started_with_WFS--WFS-international-sellers]] — 国际卖家 WFS 注意事项（EAN 不可用）

---

> **创建日期**：2026-04-21
> **来源**：整合自 [[theory/Choose-a-product-identifier]]（商品识别符政策）、[[theory/Onboarding-Guide--New-Employee-Training]]（新员工培训第 76-80 行）、[[theory/HOME-卖家运营白皮书]]（政策收紧预警）、[[theory/Troubleshoot-product-ID-errors]]（ID 错误排查）、[[theory/Troubleshoot-item-setup-errors]]（Invalid Product ID 章节）
