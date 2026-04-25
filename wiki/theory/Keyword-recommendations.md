# 关键词推荐（Keyword Recommendations）

> 基于 AI 算法自动识别高潜力关键词，帮助优化 Sponsored Products 手动活动的广告表现。

## 功能概述

Keyword Recommendations 自动分析以下数据来源：

- 账户内**活跃活动的表现数据**
- Walmart **有机搜索数据**（自然搜索词）

每 7 天提供一次推荐建议，并**每日刷新**数据。

> **限制**：仅适用于已启动 7 天以上的 **手动（Manual）Campaign**。

---

## 两种关键词工具的区别

| 维度 | Keyword Recommendations（本页） | 广告组内 Suggestions |
|------|--------------------------------|--------------------|
| 关键词数量 | 每个广告组最多 **20 个**推荐词 | 每个广告组最多 **220 个**可选词 |
| 数据来源 | 活跃 SP 自动+手动活动表现 + 有机搜索数据 | 仅与广告组内商品的**相关性** |
| 排名依据 | 基于**效果**排序，效果好的词置顶 | 仅按相关性排序 |
| 最低要求 | 广告组须已上线并运行 **3 天以上** | 无最低要求 |
| 推荐逻辑 | 识别全新关键词机会 | 提供相关性匹配词 |

---

## 如何使用

### 快速应用

1. 在 **Dashboard** 或 **Recommendations 页面** 预览关键词推荐
2. 点击 **Apply all** 直接将所有推荐词应用到活跃活动
3. 所有关键词将使用平台**建议出价（Suggested Bids）**添加

### 逐个审查应用

1. 点击 **View 2 recommendations** 逐个查看推荐词
2. 在活动或广告组级别选择要应用的关键词
3. 点击应用后将收到确认通知

### 生成报告

1. 在 Dashboard 的推荐小组件中点击 **Request report**
2. 系统跳转到 [[theory/On-demand-reports]] 页面下载报告
3. 报告每个广告组最多显示 **20 个推荐词**，含建议出价

---

## 报告指标说明

| 指标 | 定义 |
|------|------|
| **Unique Keywords** | 不计匹配类型的推荐词总数（同一词若有 3 种匹配类型 = 1 个唯一词） |
| **Total Keywords** | 含所有匹配类型组合的推荐词总数（同一词有 3 种匹配 = 3 个总词数） |

---

## 批量应用

使用 [[theory/Bulk-operations]] 功能可同时将推荐关键词批量添加到多个广告组：

1. 在关键词推荐报告中选择目标词
2. 在 Bulk Operations 模板中粘贴
3. 上传，一次性应用

---

## 常见问题

**Q：为什么没有关键词推荐？**
- 广告组未上线运行满 3 天
- 所有推荐词已添加完毕
- 无活跃广告组（需有活跃广告组才显示小组件）

**Q：每天都有新推荐吗？**
- 推荐数据每日刷新，回溯窗口为 **30 天**
- 每日最多生成一次新报告

**Q：应该使用多少推荐词？**
- 建议逐个审查，优先选择与商品高度相关且有增长潜力的词
- 不必一次性全部添加，观察效果后再逐步扩展

**Q：推荐词效果不好怎么办？**
- 参考 [[theory/All-Keywords]] 中的关键词表现报告
- 效果差的词及时降低出价或暂停
- 结合 [[theory/Search-relevancy-best-practices]] 评估相关性

---

## 相关链接

- [[theory/All-Keywords]] — 关键词管理报告
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 关键词添加完整步骤
- [[theory/Bulk-operations]] — 批量操作
- [[theory/On-demand-reports]] — 按需报告
- [[theory/Search-relevancy-best-practices]] — 搜索相关性最佳实践
- [[theory/Sponsored-Products--Glossary]] — 广告术语表

---

> 来源：`raw/walmart advertising guide/Keyword recommendations.md`
> 更新：2026-04-17
