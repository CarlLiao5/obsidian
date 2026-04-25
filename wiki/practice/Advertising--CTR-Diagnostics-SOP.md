---
author: 运营团队
auditor: 待审核
status: pending
audit_date: null
tags: [运营实践, 待审核]
---

# Sponsored Products CTR 下降诊断 SOP

> 适用于自动/手动广告活动 CTR 从基线明显下滑时的系统性排查与修复流程。

---

## 诊断入口：确认 CTR 下滑

### Step 0：建立基线

在分析前，先明确：
- **历史 CTR 均值**是多少？（去年/上月/上周）
- **下滑幅度**：从 1.01% 降至 0.5%，下降约 50%
- **下滑节奏**：突然下降（1-2天内）还是渐进式（数周）

| 下滑类型 | 可能原因 | 优先级 |
|----------|----------|--------|
| 突然下降 | 竞价环境剧变、平台算法调整、账户问题 | 高 |
| 渐进下降 | Listing 质量退化、关键词老化、季节性 | 中 |
| 周期性下降 | 正常季节波动 | 低 |

---

## 第一阶段：广告活动层诊断

### 1.1 检查展示位置分布

**操作路径**：Ad Center → Campaigns → 选择活动 → Placements

**诊断要点**：
- 对比去年同期和今年的展示位置分布（Search In-grid / My Items / Buy Box）
- Search In-grid 是高意向流量，CTR 通常最高
- 展示位置比去年低 → 优先检查是否有 Placement Exclusion 或倍数器被误调

**基础知识参考**：
![[theory/Sponsored-Products-placements]]

### 1.2 检查竞价与预算

**诊断要点**：
- 去年 vs 今年平均 CPC 是否上升？（竞价加剧）
- 日预算是否耗尽时间提前？（展示时段缩短）
- 预算耗尽 → 系统降低曝光频率，CTR 随之下降

**参考**：[[theory/Out-of-budget-features]]、[[theory/Sponsored-Products--Dynamic-bidding]]

### 1.3 检查活动结构

- 自动活动是否被暂停/修改？
- 广告组是否混杂了不相关的 SKU？
- 匹配类型是否有调整？

**参考**：[[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]]、[[theory/Campaign-setup-best-practices]]

---

## 第二阶段：关键词层诊断

### 2.1 拉取关键词表现报告

**操作路径**：Ad Center → Reports → On-demand reports → Item Keyword Performance

| 字段 | 诊断阈值 | 处理动作 |
|------|----------|----------|
| CTR < 0.3% | 预警 | 暂停或降低出价 |
| CTR < 0.1% | 危险 | 立即暂停 |
| Impressions 暴跌 | — | 检查展示位置/出价/关键词匹配 |
| Spend 高但无转化 | — | 添加否定关键词 |

**参考**：[[theory/All-Keywords]]

### 2.2 补充高质量关键词

**使用 Keywords Planner**（Tools → Keywords Planner → Add items）：

1. 输入 SKU，获取相关搜索词
2. 按 **Traffic keyword frequency bucket** 排序，优先选择中高频词
3. 匹配类型优先级：Broad（广泛撒网）→ Phrase（收窄）→ Exact（精准收割）
4. 将 Top 20 关键词添加到手动活动

**参考**：[[theory/Keywords-Planner]]

### 2.3 竞品关键词截流

- 在 Raw query 列中识别竞品品牌词
- 配件/兼容类商品可添加竞品品牌词吸引精准流量

### 2.4 否定关键词维护

| 否定类型 | 使用场景 |
|----------|----------|
| 广泛否定 | 词组与你的产品无关 |
| 精确否定 | 特定搜索词带来曝光但不转化 |

**操作路径**：Ad Center → Keywords → Negative Keywords

---

## 第三阶段：商品详情页层诊断

> 商品详情页是 CTR 的根本。广告将用户引到 Listing，用户看到页面的第一眼决定是否点击。

### 3.1 标题诊断

| 检查项 | 标准 |
|--------|------|
| 字符数 | ≤ 150 字符（超出会被截断） |
| 核心关键词位置 | 前 80 字符内必须包含主搜索词 |
| 禁止内容 | 全大写、促销语（Free Shipping/Sale）、特殊字符（~!*$）、竞品名称、URL |

**参考**：[[theory/Product-Detail-Page_-overview]]

### 3.2 主图合规检查

| 要求 | 规格 |
|------|------|
| 最小像素 | 1500×1500（推荐 2200×2200） |
| 背景 | 纯白 (#255/255/255) |
| 文件格式 | JPG/PNG，≤ 5MB |
| 禁止 | 水印、Logo、促销文字、图片中包含配件（除非附带） |

**参考**：[[theory/Product-detail-page_-Image-guidelines-&-requirements]]

### 3.3 关键词嵌入 Listing

循环迭代流程：

1. 下载 **Item Keyword Report**（Reports → Item Keyword Performance）
2. 识别带来点击（高 CTR）和转化（高 CVR）的搜索词
3. 将这些词自然融入：标题 → 描述 → 关键特性
4. 等待 48-72 小时，观察 CTR 变化
5. 如无改善，重复 Step 1

**参考**：[[theory/How-to-maximize-item-pages]]、[[theory/Search-relevancy-best-practices]]

### 3.4 富媒体补充

| 类型 | 作用 |
|------|------|
| 多角度图（4+张） | 增强购买信心 |
| 360° 旋转图 | 降低退货率 |
| 视频 | 提升停留时间和转化 |
| 对比图表 | 突显产品优势 |

**参考**：[[theory/Product-detail-page_-rich-media]]

---

## 第四阶段：竞价环境分析

### 4.1 相关性评分

沃尔玛第二竞价机制中，相关性评分综合考量：
- 标题关键词匹配度
- 详情页内容质量
- 历史转化率
- WFS 库存稳定性
- 价格竞争力

**参考**：[[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]]

### 4.2 竞品动态

- 品类是否有新卖家进入？
- 头部卖家的价格是否更具竞争力？
- 竞品的 Listing 质量（图片/评分）是否有提升？

---

## 行动计划时间线

| 阶段 | 时间 | 动作 | 工具 |
|------|------|------|------|
| **Day 1** | 立即 | 拉取关键词报告，暂停 CTR < 0.2% 的关键词 | All-Keywords |
| **Day 1** | 立即 | 审查标题（是否被截断、核心词是否靠前） | Product-Detail-Page_-overview |
| **Day 2-3** | 短期 | 优化标题 + 主图，上传 Keywords Planner 新词到手动活动 | Keywords Planner |
| **Week 1** | 中期 | 创建新的手动精确匹配活动，与自动活动并行测试 | Campaign setup |
| **Week 1** | 中期 | 排查展示位置变化，调整 Placement Inclusion | Sponsored-Products-placements |
| **Week 2-3** | 观察 | 监控 CTR 变化趋势，对比优化前后数据 | On-demand reports |
| **Week 4** | 复盘 | 评估各活动/关键词的 CTR 和 ROAS，决定预算重新分配 | Custom-reports |

---

## 相关页面

**广告核心**
- [[theory/Sponsored-Products--Overview]] — Sponsored Products 概览
- [[theory/Sponsored-Products-placements]] — 展示位置详解
- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略

**关键词优化**
- [[theory/Keywords-Planner]] — 关键词规划器
- [[theory/Keyword-recommendations]] — 关键词推荐
- [[theory/All-Keywords]] — 关键词管理
- [[theory/Search-relevancy-best-practices]] — 搜索相关性最佳实践

**商品详情页**
- [[theory/Product-Detail-Page_-overview]] — 商品详情页政策
- [[theory/How-to-maximize-item-pages]] — 最大化商品详情页
- [[theory/Product-detail-page_-Image-guidelines-&-requirements]] — 图片标准
- [[theory/Product-detail-page_-Keyword-optimization]] — 关键词优化

**报告工具**
- [[theory/On-demand-reports]] — 按需报告
- [[theory/Item-Health-reports]] — 商品健康报告
- [[theory/Custom-reports]] — 自定义报告

---

> 来源：基于知识库 Advertising × Item Setup 分类问答编译  
> 创建日期：2026-04-14
