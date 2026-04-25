---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 出价策略详解 (Campaign Bidding Strategies)

> Sponsored Products 三种出价策略（Dynamic / Target ROAS / Fixed）的对比与最佳实践。

## 三种出价策略概览

| 策略 | 定向类型 | 目标 | 特点 | 广告类型 |
|------|---------|------|------|---------|
| **Target ROAS** | 自动 | 在设定 ROAS 目标内最大化销售 | AI 自动计算最优出价 | 仅 Sponsored Products |
| **Dynamic Bidding** | 自动/手动 | 最大化转化 | 系统实时调整出价（+100%/-50%） | Sponsored Products |
| **Fixed Bidding** | 自动/手动 | 严格预算控制 | 手动固定出价，精确控制 | Sponsored Brands/Products/Videos |

## Target ROAS（目标 ROAS 出价）

**仅限现有活动适用（新活动不可用）。**

利用 AI 算法自动计算最优出价以达到设定的 ROAS 目标。

**特点：**
- 系统根据转化价值动态调整出价
- 日预算最低 $50
- 需通过平台推荐开启，不能新建
- 活动有学习期（14-30 天）

**关键指标：** ROAS、销售额

## Dynamic Bidding（动态出价）

系统根据转化概率实时调整出价，转化可能性高时自动加价，转化可能性低时自动降价。

**出价调整范围：**
- 最高可加价 **+100%**
- 最低可降价 **-50%**（不低于最低出价）

**最佳实践：**
- 活动至少 10+ 个商品，同一商品类别
- 使用建议出价设置基础出价
- 不要用相同商品同时创建动态和非动态两个活动（自我竞争）
- 按类别拆分品牌活动

**关键指标：** 转化量、订单数

## Fixed Bidding（固定出价）

手动固定出价，不自动调整。需要广告主根据表现手动优化。

**适用场景：**
- 需要精确控制每次点击成本
- 预算有限且需预测花费
- 手动精细化管理广告

## 最佳实践（通用）

### 新活动
- 确保商品有库存
- 避免同时运行相同商品的多个活动
- 开启超预算提醒

### 现有活动
- 等待活动积累一定互动数据后再优化
- 不要创建相同商品的多个活动（设置不同出价策略）

### 活动优化
- 避免频繁在三种出价策略之间切换
- 避免在活动进行中减少预算或禁用商品/关键词
- 若活动每日花完预算，增加日预算

## 三策略对比图

```
出价策略选择逻辑：
│
├─ 新品/数据积累期 → Dynamic Bidding（默认）
│
├─ 有历史数据且想优化 ROAS → Target ROAS（需推荐）
│
└─ 需精确控制成本/需投放 Sponsored Brands/Videos → Fixed Bidding
```

## 相关页面

- [[theory/Sponsored-Products--Dynamic-bidding]] — 动态出价详解
- [[theory/Sponsored-Products--Target-ROAS-bidding]] — 目标 ROAS 出价详解
- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]] — 创建活动
- [[theory/Bidding-strategy-recommendations]] — 出价策略推荐工具

---

> 来源：`raw/walmart advertising guide/Campaign bidding strategies.md`