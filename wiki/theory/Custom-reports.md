---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 自定义报告

> 使用自定义维度、指标和分组构建专属报告，自定义分析广告活动表现。

## 功能概述

自定义报告（Custom Reports）让你进一步分析 Walmart Connect Sponsored Search 活动表现，可按不同时间范围、活动等构建自定义报告。

## 主要用途

| 用例 | 配置 |
|------|------|
| 按月比较新品牌订单 | Month 维度 + New-to-Brand Orders 指标 |
| 识别驱动最多店内销售的展示位置 | Placement 维度 + In-Store Orders (Beta) 指标 |
| 比较每周店内销售变化 | Week 维度 + In-Store Orders (Beta) 指标 |
| 按品牌类型比较表现 | Brand 维度 + 任意指标 |
| 使用自定义指标比较表现 | 拖放移除默认指标（如 Conversion Rate） |
| 与上期比较 | 时间偏移（Time shift）功能 |

## 报告组件

| 组件                 | 说明                                |
| ------------------ | --------------------------------- |
| **Dimensions（维度）** | 分组字段，决定表格行（拖放到 Filter By 或 Split） |
| **Measures（指标）**   | 绩效指标，决定表格列（拖放到 Measure）           |
| **Split**          | 将维度嵌套为表格行                         |
| **Filter By**      | 按维度筛选特定值                          |

## 可用维度

Date (Day/Week/Month)、Ad Group (Id/Name)、Campaign (Id/Name/Type)、Item (Id/Name)、Bidded Keyword、Brand、Match Type、Page Type、Placement、Platform、Bidded Category Path Name

## 可用指标

Impressions、Clicks、Average CPC、CTR、Ad Spend、Units Sold、Conversion Rate、Sales Revenue、ROAS、In-Store Attribution 指标（Beta）、New-to-Brand 指标

## 报告限制

- 最多 **3 个 Split 字段**（每个默认 5 行，最多 100 行）
- 折线图报告仅显示 **3 个指标** 和 **2 个 Split** 字段
- 指标在 Measure 中的顺序决定表格列顺序

## 时间偏移（Time Shift）

时间偏移可在同一视图中比较不同时间段的指标表现，添加额外列显示时间差异。红色表示下降，绿色表示增长。

## 保存和导出

- **保存报告**：点击 **Save Report**，保存到已有报告或创建新报告
- **导出 CSV**：点击下载图标立即下载

## 相关页面

- [[theory/On-demand-reports]] — 按需报告
- [[theory/All-Campaigns]] — 全部活动
- [[theory/New-to-brand-metrics]] — 新品牌指标

---

> 来源：`raw/walmart advertising guide/Custom reports.md`
