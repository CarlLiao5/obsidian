---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 关键词规划器

> 根据历史搜索数据为所选商品生成关键词建议列表。

## 功能概述

关键词规划器（Keywords Planner）根据历史搜索流量和所选商品的关联词生成关键词列表：
- 显示顾客搜索时商品出现的频率
- 显示特定关键词在 Walmart.com 被搜索的频率

## 使用步骤

1. 在左侧导航栏 **Tools** 下点击 **Keywords Planner**
2. 点击 **Add items**，输入商品 ID 并搜索
3. 选中商品后点击 **Add x items for keyword suggestions**
4. 导出 CSV 格式的关键词列表用于手动活动

**注意：** 也可使用 CSV 模板批量上传多个商品。

## 表格数据说明

| 列名                                   | 说明                                            |
| ------------------------------------ | --------------------------------------------- |
| **Normalized query**                 | 相似搜索词归一化后的查询（如 "motor bicycles"）              |
| **Raw query**                        | 顾客实际输入的原始搜索词（如 "motorbike", "motorized bike"） |
| **Item keyword frequency bucket**    | 商品在该搜索词下展示的频率                                 |
| **Traffic keyword frequency bucket** | 该搜索词被顾客搜索的频率                                  |
|                                      |                                               |

## 选择相关关键词

关键词列表中的词可能与你的商品不相关，原因包括：

- 商品分类（Taxonomy）映射错误
- 商品 Product Type 映射错误
- Global Product Type 映射错误

遇到映射问题可联系 Partner Support 开 case（[Sellers](https://sellerhelp.walmart.com/s/contact) / [Suppliers](https://supplierhelp.walmart.com/s/contact)）。

## 无关键词建议的排查

- **新发布商品**：需要时间积累关键词建议，建议先运行自动活动增加曝光
- **超过 60 天无建议**：联系广告主支持开 case

## 匹配类型说明

| 匹配类型 | 范围 | 说明 |
|----------|------|------|
| **Broad（广泛）** | 最广 | 捕获最广泛的顾客覆盖面 |
| **Phrase（词组）** | 中等 | 包含指定词组，范围收窄 |
| **Exact（精确）** | 最窄 | 仅精确匹配关键词 |

建议先以 Broad 匹配类型竞价以覆盖最广泛的顾客触达。

## 相关页面

- [[theory/All-Keywords]] — 全部关键词管理
- [[theory/Keyword-recommendations]] — 关键词推荐
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 添加和选择关键词
- [[theory/Sponsored-Products--Create-a-manual-campaign]] — 创建手动活动

---

> 来源：`raw/walmart advertising guide/Keywords Planner.md`
