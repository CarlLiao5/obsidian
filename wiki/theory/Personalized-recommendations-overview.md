# 个性化推荐总览 (Personalized Recommendations Overview)

> Walmart Connect 基于 AI 提供的个性化优化建议总览。

## 概述

个性化推荐帮助广告主优化活动设置并最大化表现，可在 Dashboard 和 Recommendations 页面查看。包含预算、出价策略、商品和关键词管理等类别。

## 推荐类别

### 预算推荐（Budget）

| 推荐类型 | 说明 | 位置 | 更新频率 |
|---------|------|------|---------|
| **Out-of-budget alert** | 预算耗尽警报，提供预算建议 | Dashboard / All Campaigns / 活动编辑页 | 每日 |
| **Budget-at-risk** | 预算风险预警（过去 7 天至少花完一次���预算） | Dashboard / All Campaigns / 活动编辑页 | 每日 |

### 出价策略推荐（Bidding Strategy）

| 推荐类型 | 说明 | 适用对象 | 更新频率 |
|---------|------|---------|---------|
| **Switch to Target ROAS** | 从 Fixed/Dynamic 切换到 Target ROAS 可提升销售 | 现有自动活动 | 每日 |
| **Optimize your ROAS target** | 调整 ROAS 目标和预算可提升销售 | 使用 Target ROAS 的活动 | 每日 |
| **Target ROAS learning paused alert** | Target ROAS 活动无法完成学习期 | Target ROAS 活动 | 每日 |
| **Suggested Bids** | 商品/关键词建议出价 | 创建/编辑活动时 | 每日 |

### 商品推荐（Items）

| 推荐类型 | 说明 | 更新频率 |
|---------|------|---------|
| **Item recommendations** | 识别有潜力未推广商品 | 每周 |

### 关键词推荐（Keywords）

| 推荐类型 | 说明 | 更新频率 |
|---------|------|---------|
| **Keyword recommendations** | 识别有潜力新关键词 | 每日 |
| **Suggested keywords** | 基于商品相关性的关键词建议 | 每日 |

## 资格条件

| 类别 | 名称 | 资格标准 |
|------|------|---------|
| Budget | Out-of-budget alert | 日预算和/或总预算已耗尽，或过去 7 天至少花完一次 |
| Bidding | Switch to Target ROAS | 使用 Fixed/Dynamic 的自动活动有潜力提升销售 |
| Bidding | Optimize ROAS target | 使用 Target ROAS 的活动可进一步优化 |
| Bidding | Learning paused alert | Target ROAS 活动无法退出学习期 |
| Items | Item recommendations | 有高质量未推广商品 |
| Keywords | Keyword recommendations | 有新增关键词机会 |

## 如何工作

Walmart Connect 平台分析 Sponsored Search 活动设置和表现，判断是否有优化建议。仅当活动符合特定资格标准时才会显示推荐。

## 相关页面

- [[theory/Bidding-strategy-recommendations]] — 出价策略推荐
- [[theory/Item-recommendations]] — 商品推荐
- [[theory/Keyword-recommendations]] — 关键词推荐
- [[theory/Out-of-budget-features]] — 超预算功能

---

> 来源：`raw/walmart advertising guide/Personalized recommendations overview.md`