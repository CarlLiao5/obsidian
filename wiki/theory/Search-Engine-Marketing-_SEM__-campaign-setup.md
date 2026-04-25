---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# SEM 活动设置 (Search Engine Marketing - Campaign Setup)

> 在 Seller Center 中设置 Custom 或 Quick start SEM 广告活动的完整步骤。

## 概述

在 Seller Center 的 Search Engine Marketing 页面点击 **+ Create new campaign** 创建广告活动。需具有 **admin 访问权限**。

## 活动类型

| 类型 | 说明 |
|------|------|
| **Quick start** | 自动推荐高销售潜力商品，快速建站 |
| **Custom** | 手动选择商品，自定义预算和出价策略 |

## 设置步骤

### Step 1 — 选择活动类型

在 SEM 页面右上角选择 **+ Create new campaign**，选择 Custom 或 Quick start，点击 Continue。

### Step 2 — 添加活动详情

1. **命名活动**：使用唯一名称
2. **选择商品**：
   - 单独添加：搜索商品名称/SKU/Item ID，勾选后添加
   - 批量上传：下载 Item ID/SKU 模板，填写后上传
   - 支持逗号分隔一次性搜索多个商品
3. **设置预算和排期**：
   - 开始日期：默认为次日
   - 结束日期：可选，最少在开始日期后 21 天
   - 日预算：设定每日最高花费
4. **选择出价策略**：

| 策略 | 目标 | 适用场景 |
|------|------|----------|
| **Maximize Clicks** | 在预算内获取最多点击 | 新品推广、数据积累期 |
| **Target ROAS (tROAS)** | 实现目标广告支出回报率 | 有历史销售数据、优化期 |

**提示：** 先用 Maximize Clicks 积累数据，再切换到 tROAS 优化。

### Step 3 — 启动活动

点击 Start campaign。活动在创建当天显示"Scheduled"，在开始日期后变为"Running"。

## 竞价算法（两阶段）

| 阶段 | 时长 | 特征 |
|------|------|------|
| **Learning（学习期）** | 约 7-10 天 | 算法测试不同出价水平，可能出现展示不稳定、ROAS 波动 |
| **Optimizing（优化期）** | 学习期结束后 | 算法仅在预期 ROAS 最佳时出价，低需求/高竞争商品可能降低花费 |

## 相关页面

- [[theory/Advertising--SEM]] — SEM 项目总览
- [[theory/Search-Engine-Marketing-_SEM__-campaign-management]] — 活动管理
- [[theory/Search-Engine-Marketing-_SEM__-program-policy]] — 政策合规
- [[theory/Troubleshoot-Search-Engine-Marketing-_SEM_-errors]] — 错误排查

---

> 来源：`raw/Advertising--Search_Engine_Marketing__SEM_--Search-Engine-Marketing-_SEM__-campaign-setup.md`
> 更新：2025-07-28