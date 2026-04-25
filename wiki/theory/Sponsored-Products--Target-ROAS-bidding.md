# 目标 ROAS 出价 (Target ROAS Bidding)

> 使用 AI 算法自动优化以达到设定 ROAS 目标的智能出价策略。

## 概述

Target ROAS（目标广告支出回报率）出价利用 AI 算法计算最优出价，帮助广告主有效实现目标 ROAS，从而提高活动效率、节省时间。

**限制：** 此功能目前仅对**曾经使用过此功能**的广告主开放，新广告主访问已暂停（可能将来扩展）。

**最低预算：** 所有 Target ROAS 活动需日预算 **≥ $50**。

## 适用条件

- 仅限**现有活动**（不能新建活动时选择）
- 仅限 **Sponsored Products 自动活动**
- 日预算 ≥ $50
- 需通过平台推荐开启

## 优势

- **提升绩效**：AI 实时设置和优化出价以实现 ROAS 目标
- **节省时间**：无需手动设置出价和定期监控表现
- **智能预算分配**：投资引导向可带来更好效果的广告位

## 活动生命周期

### Learning Phase（学习期）

活动上线后前 **14-30 天** 为学习期，系统收集数据以优化出价。

**禁止操作：** 在学习期更改 ROAS 目标、删除畅销品、降低预算（会导致重新进入学习期）。

### Optimization Phase（优化期）

学习期结束后进入优化期，系统按 ROAS 目标优化出价。

### Learning Paused（学习暂停）

若活动无法从学习期进入优化期，显示此状态。

**应对措施：** 切换到动态出价，或向活动添加更多有质量分的商品。

## 表现指标

Target ROAS 活动关注以下指标：
- **ROAS**：实际广告支出回报率
- **学习期后的销售**：14 天归因窗口（学习期结束后再等 14 天评估）

**ROAS 目标设置建议：** 从当前平均表现开始，逐渐提高（最高 +20%），待结果稳定后再继续调整。

## 自动回退机制

若活动持续表现不佳（长期处于 Learning Paused 或持续低效运行），Walmart Connect 可能自动将活动切换回之前的出价策略（若无可用策略则切换到动态出价）。切换前会发出警告。

## 相关页面

- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略对比
- [[theory/Sponsored-Products--Dynamic-bidding]] — 动态出价
- [[theory/Bidding-strategy-recommendations]] — 出价策略推荐工具
- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]] — 创建活动

---

> 来源：`raw/walmart advertising guide/Target ROAS bidding.md`