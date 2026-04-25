# 广告优化方法论

> 运营实践总结：广告优化的本质是以阶段性目的为驱动，根据当前目标调整广告动作，而非盲目调整出价或预算。

## 核心原则

**广告优化 = 动作，但动作之前必须有目的。**

任何广告调整操作之前，必须先明确：**本次调整的目的是什么？**

- 目的不清 → 调整无效 → 资源浪费
- 目的明确 → 动作精准 → 效果可评估

## 各阶段目的与优化策略

### 阶段一：新品期

**核心目的**：获取有效精准曝光，积累数据

**优化策略**：
- 开启自动活动进行关键词测试
- 重点关注：曝光量（Impressions）、点击量（Clicks）
- 尽量避免在搜索首页展示（新品转化率低，浪费预算）
- 等待评论积累后再做其他调整

**基础知识参考**：
![[theory/Sponsored-Products--Overview#新品期]]

**信号判断**：
- 有足够点击数据（建议 100+ clicks/周）→ 进入下一阶段
- 点击少 → 优化主图、标题、价格

---

### 阶段二：成长期

**核心目的**：提高自然搜索排名（Natural Rank）

**优化策略**：
- 开打手动精准关键词（Exact Match）
- 配合手动广泛匹配（Broad Match）扩展流量
- 使用[[theory/Sponsored-Products--Expanded-targeting|扩展定向]]功能
- 关注转化率（CR）和加购率（Add to Cart）

**关键指标**：
- 广告订单 + 自然订单的协同增长
- 自然排名逐步上升

---

### 阶段三：稳定期 / 优化期

**核心目的**：降低 ACOS，提升广告利润贡献

**优化策略**：
- 分析关键词报告（参考 ![[theory/All-Keywords]]），筛选高 ACOS 关键词降低出价或暂停
- 使用自动规则批量优化低效关键词
- 开启 Target ROAS 出价（参考 ![[theory/Sponsored-Products--Campaign-bidding-strategies#Target-ROAS]]）
- 结合 SEM 做站外引流

---

### 阶段四：爆款期

**核心目的**：最大化 GMV，同时控制 ACOS 在合理范围

**优化策略**：
- 设置充足的日预算，确保不因预算限制损失订单
- 开启首页顶部展示位置倍数器（[[theory/Sponsored-Products--Step-3-Add-bid-multipliers|出价倍数器]]）
- 结合 [[theory/Growth_opportunities--Promotions|促销定价]] 进一步放量
- 警惕：爆款≠无限广告投入，需动态平衡广告与自然流量

## 常见优化误区

| 误区 | 原因 | 正确做法 |
|------|------|----------|
| 预算耗尽就加预算 | 未分析原因 | 先确认预算消耗时段是否符合预期 |
| ACOS 高就降 bid | ACOS 本身不是唯一指标 | 结合 [[theory/New-to-brand-metrics|New-to-Brand 指标]] 和整体 ROAS 判断 |
| 自然位靠前就关广告 | 忽视广告对自然排名的催化作用 | 维持广告投放，广告+自然联动降低整体获客成本 |

## 自然位与广告位协同策略

**核心逻辑**：
- 广告位与自然位距离太近 → 增加无效点击（同一人反复看到同一商品）
- 适当拉开距离 → 覆盖更多搜索意图，提升整体转化

**操作建议**：
- 自然排名靠前的产品，可适当降低广告 bid
- 让广告位置展示在第二页或首页底部
- 自然位置展示在首页顶部
- 用户无论点击哪个位置，都能形成转化

## 相关链接

- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略详解
- [[theory/All-Keywords]] — 关键词管理
- [[theory/Automated-rules]] — 自动规则优化
- [[practice/Advertising--CTR-Diagnostics-SOP]] — CTR 下降诊断 SOP
- [[theory/Search-relevancy-best-practices]] — 搜索相关性最佳实践
- [[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]] — 平台算法与广告策略
- [[practice/Advertising--Bid-reduction-Paradox]] — 降 bid 反效果案例分析（Cap-out 时间前移）
- [[practice/Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy]] — 广告与自然位协同策略（避免无效重叠）
- [[practice/Operations--Mature-Listing-Vicious-Cycle-Recovery]] — 老链接恶性循环破解

---

> 来源：`raw/note/2026-04-14.md`
> 更新：2026-04-17
