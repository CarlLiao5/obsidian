---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 批量操作（Bulk Operations）

> 使用 Excel/CSV 模板批量创建和管理 Sponsored Products 活动、广告组、商品和关键词。

## 功能概述

Bulk Operations 批量操作支持：
- 创建和更新活动
- 创建和修改广告组
- 添加、更新、启用/禁用商品
- 添加、更新、启用/禁用关键词
- 批量设置预算和出价
- 批量更改匹配类型
- 批量设置展示位置和出价倍数器

> **限制**：目前仅支持 Sponsored Products 活动，且仅限单账户操作。

---

## 操作流程

### Step 1 — 访问批量操作

在 Walmart Connect Ad Center 左侧导航栏选择 **Bulk Operations**。

### Step 2 — 下载模板或创建文件

两种方式：

1. **下载现有数据**（推荐）：获取账户中现有活动和广告组数据，在其基础上修改
2. **空白模板**：从零开始创建

> **注意**：对于多广告组的复杂活动结构，建议每个活动使用单独文件，避免定向冲突。

### Step 3 — 设置筛选条件

- 选择日期范围（**最长一个月**）
- 可选择排除已结束的活动
- 可排除零展示的活动中品

### Step 4 — 上传文件

上传状态：

| 状态 | 含义 |
|------|------|
| Uploaded | 上传成功，等待处理 |
| Partial success | 部分成功，部分失败 |
| Success | 全部成功 |
| Error | 全部失败 |

部分失败或失败时，可下载反馈文件查看具体错误原因。

---

## 模板字段说明

| 字段 | 说明 |
|------|------|
| **Record Type** | 要操作的记录类型（campaign/ad group/keyword/item 等） |
| **Operation** | 操作类型：**create** 或 **update** |
| **Campaign Id** | 活动 ID（新增留空，修改时填写） |
| **Ad Group Id** | 广告组 ID（新增留空） |
| **Campaign Name / Ad Group Name** | 名称（新增和修改均需填写） |
| **Start Date / End Date** | 活动起止日期（新增必须填写） |
| **Campaign Targeting Type** | 定向类型：automatic 或 manual |
| **Total Budget / Daily Budget** | 预算类型（二选一，两个都填更好） |
| **Bid** | 出价金额（商品/关键词级别） |
| **Suggested Bid** | 建议出价（仅参考） |
| **Item Id / Item Name** | 商品 ID 和名称 |
| **Keyword / Keyword Id / Match Type** | 关键词及匹配类型（exact/phrase/broad） |
| **Status** | 启用状态：enabled 或 disabled |
| **Placement Inclusion Type** | 展示位置类型（手动活动）：Search Ingrid / Buy Box / Carousel |
| **Placement Bid Multiplier** | 展示位置出价倍数（百分比，不含 % 符号） |
| **Platform Bid Multiplier** | 平台出价倍数：desktop / app / mobile |

### 匹配类型操作注意

- 同一关键词需要 broad 和 phrase 两种匹配 → **每个匹配类型占一行**
- 关键词 ID 由平台自动生成，新增关键词无需填写 ID

### 出价倍数器说明

| 活动类型 | 可用展示位置倍数器 |
|----------|---------------------|
| 手动活动 | Search Ingrid、Item Buybox |
| 自动活动 | Search Ingrid、Item Buybox、Homepage、Stock Up |

---

## 批量创建新活动顺序

在空白模板中创建完整新活动，需按以下顺序填写行：

```
1. Campaign（活动）
2. Campaign Placement Bid Multiplier（可选）
3. Campaign Platform Bid Multiplier（可选）
4. Campaign Placement Inclusion（可选）
5. Ad Group（广告组）
6. Item（商品）
7. Keyword（关键词）
```

---

## 上传注意事项

- **字符限制**：引号 `"` 和逗号 `,` 可能导致解析错误，需正确转义
- **通配符**：星号 `*` 技术上可接受，但可能导致错误，不推荐使用
- **文件大小**：最大 25 MB；超过需拆分为多个文件
- **等待时间**：上传处理最多需 4 小时
- **无法撤销**：上传开始后无法取消修改

---

## 最佳实践

1. **测试优先**：先上传小样本文件测试，确认无误后再大批量操作
2. **版本控制**：保留历史版本文件，便于追溯和回滚
3. **排除干扰**：删除不需修改的行（保留默认 `update` 值），避免覆盖意外
4. **日期范围**：每次批量操作限定一个月内数据
5. **错误反馈**：重点关注反馈文件中的错误代码，使用 [Bulk Update Resource](https://sforce.co/430HRY8) 解码

---

## 相关链接

- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略
- [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 出价倍数器
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 关键词添加
- [[theory/On-demand-reports]] — 按需报告
- [[theory/Keyword-recommendations]] — 关键词推荐报告

---

> 来源：`raw/walmart advertising guide/Bulk operations.md`
> 更新：2026-04-17
