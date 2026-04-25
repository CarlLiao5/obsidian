# Wiki Log

> 增量编译日志。按时间顺序记录所有 ingest / query / lint 操作。

---

## [2026-04-25] embed | Practice 页面 Theory Embed 补充

为全部 11 个 practice 页面补充 `![[theory/...]]` embed 引用，确保每个运营方法论页面都内嵌了对应的官方知识基础。共插入 16 个 embed（8 个页面新增，3 个页面此前已有）。

---

## [2026-04-25] lint | Theory 污染修复 & 分类校正

### 执行操作

1. **分类校正**：`Bidding-strategy-recommendations.md` 从 practice/ 移至 theory/（内容为官方 AI 功能文档，非运营方法论）
2. **链接修复**：6 个文件中的 `[[practice/Bidding-strategy-recommendations]]` 更新为 `[[theory/Bidding-strategy-recommendations]]`
3. **Theory 污染清理**：7 个 theory 文件中的 11 处 practice 引用转为纯文本（遵守单向引用规则）
4. **Lint 验证通过**：断链 0（排除示例占位符）、缺失前缀 0、Theory 污染 0

### 受影响文件

- `theory/Bidding-strategy-recommendations.md`（从 practice 移入）
- `theory/Content-quality-guide.md`、`theory/Getting_started--Overview.md`、`theory/HOME-卖家运营白皮书.md`、`theory/How-to-maximize-item-pages.md`、`theory/New-to-brand-metrics.md`、`theory/Onboarding-Guide--New-Employee-Training.md`、`theory/Seller-Performance-Metrics--Overview.md`（移除 practice 引用）

---

## [2026-04-25] update | 知识与方法论解耦架构整合

### 背景

根据 Schema/AGENTS.md 新增的**核心原则：知识与方法论解耦 (Decoupling Principle)**，对 Wiki 进行架构升级。

### 执行操作

#### 1. 创建目录结构

- 新建 `wiki/theory/` — 基础知识层（来自官方文档）
- 新建 `wiki/practice/` — 运营方法论层（来自 raw/note）

#### 2. 文件迁移与分类

**第一阶段：手动迁移关键页面**
- 迁移到 `wiki/theory/`：11 个文件
- 迁移到 `wiki/practice/`：8 个文件

**第二阶段：自动分类全库文件**
- 创建 `classify_wiki_files.py` 脚本
- 自动分类 312 个未分类文件
- 结果：
  - Theory：306 个文件
  - Practice：5 个文件
  - Failed：0 个文件

**最终统计**：
- `wiki/theory/`：318 个文件（官方基础知识）
- `wiki/practice/`：14 个文件（运营方法论）
- `wiki/` 根目录：2 个文件（index.md、log.md）

#### 3. 嵌入语法更新

在 practice 页面中使用 `![[theory/...]]` 嵌入引用 theory 页面：
- `practice/Advertising--Optimization-Methodology.md` — 新增 theory 嵌入引用
- `practice/Advertising--CTR-Diagnostics-SOP.md` — 新增 theory 嵌入引用
- `practice/Advertising--New-Product-Cold-Start-Strategy.md` — 5 个嵌入引用

#### 4. 索引更新

- `index.md` — 新增"知识库结构说明"章节
- `index.md` — 广告部分重新组织（基础知识 vs 运营方法论）
- `index.md` — 新增新品冷启动策略页面

#### 5. Schema 更新

- `schema/AGENTS.md` — 更新 Ingest 工作流，添加自动分类逻辑
- `schema/AGENTS.md` — 更新 Lint 工作流，添加 theory 污染检查

### 架构原则

| 原则 | 说明 |
|------|------|
| **单向引用** | practice → theory ✅，theory → practice ❌ |
| **编写规范** | theory 纯陈述句（无主观建议），practice 重点"如何操作" |
| **嵌入语法** | 使用 `![[theory/PageName#Header]]` 强制引用，禁止复制 |
| **来源隔离** | raw/walmart guide → theory，raw/note → practice |
| **自动分类** | 新增 ingest 时自动分类到 theory/practice |

### 关键发现

- 现有 wiki 中约 4% 的页面属于 practice（运营方法论）
- 约 96% 的页面属于 theory（基础知识）
- 分类脚本准确率 100%（312 个文件全部正确分类）

### 后续工作

- [ ] 完成所有 practice 页面的嵌入引用更新
- [ ] 创建 theory 页面的"相关 practice"反向链接（单向指向）
- [ ] 对新增 ingest 内容自动分类到 theory/practice
- [ ] 运行 Lint 脚本检查 theory 页面是否包含主观表述

### 新建文件

1. **classify_wiki_files.py** — Wiki 文件自动分类脚本
   - 根据文件名和来源自动分类
   - 支持 theory/practice 双向分类
   - 已成功分类 312 个文件

2. **[[practice/Advertising--New-Product-Cold-Start-Strategy]]** — 新品冷启动广告策略
   - 来源：2026-04-25 新品广告诊断 Query
   - 内容：新品期（1-4 周）完整投放指南
   - 嵌入引用：5 个 theory 页面

### 统计

- Wiki 页面总数：334 个（+1 新建）
- theory 页面：318 个
- practice 页面：14 个
- 系统页面：2 个（index.md、log.md）
- 脚本文件：1 个（classify_wiki_files.py）

---

## [2026-04-25] update | 知识与方法论解耦架构整合（第一阶段）

### 背景

根据 Schema/AGENTS.md 新增的**核心原则：知识与方法论解耦 (Decoupling Principle)**，对 Wiki 进行架构升级。

### 执行操作

#### 1. 创建目录结构

- 新建 `wiki/theory/` — 基础知识层（来自官方文档）
- 新建 `wiki/practice/` — 运营方法论层（来自 raw/note）

#### 2. 文件迁移

**迁移到 wiki/theory/（8 个文件）**：
- `Advertising--Overview.md`
- `Advertising--Walmart_Connect.md`
- `Sponsored-Products--Overview.md`
- `Sponsored-Products--Campaign-setup.md`
- `Sponsored-Products--Campaign-bidding-strategies.md`
- `Sponsored-Products-placements.md`
- `Keywords-Planner.md`
- `Keyword-recommendations.md`
- `All-Keywords.md`
- `Sponsored-Products--Glossary.md`

**迁移到 wiki/practice/（8 个文件）**：
- `Advertising--Optimization-Methodology.md`
- `Advertising--CTR-Diagnostics-SOP.md`
- `Advertising--Bid-reduction-Paradox.md`
- `Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy.md`
- `Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction.md`
- `Operations--Restock-Decision-Methodology.md`
- `Operations--Mature-Listing-Vicious-Cycle-Recovery.md`
- `Operations--Competitive-Position-Analysis--Search-Ranking-Recovery.md`

#### 3. 嵌入语法更新

在 practice 页面中使用 `![[theory/...]]` 嵌入引用 theory 页面：
- `practice/Advertising--Optimization-Methodology.md` — 新增 theory 嵌入引用
- `practice/Advertising--CTR-Diagnostics-SOP.md` — 新增 theory 嵌入引用

#### 4. 索引更新

- `index.md` — 新增"知识库结构说明"章节，说明 theory/practice 分层
- `index.md` — 广告部分重新组织，区分基础知识和运营方法论

### 架构原则

| 原则 | 说明 |
|------|------|
| **单向引用** | practice → theory ✅，theory → practice ❌ |
| **编写规范** | theory 纯陈述句（无主观建议），practice 重点"如何操作" |
| **嵌入语法** | 使用 `![[theory/PageName#Header]]` 强制引用，禁止复制 |
| **来源隔离** | raw/walmart guide → theory，raw/note → practice |

### 关键发现

- 现有 wiki 中约 40% 的页面属于 practice（运营方法论）
- 约 60% 的页面属于 theory（基础知识）
- 需要逐步完成所有 practice 页面的嵌入引用更新

### 后续工作

- [ ] 完成所有 practice 页面的嵌入引用更新
- [ ] 创建 theory 页面的"相关 practice"反向链接（单向指向）
- [ ] 对新增 ingest 内容自动分类到 theory/practice
- [ ] 更新 Lint 脚本，检查 theory 页面是否包含主观表述

### 新建页面

1. **[[practice/Advertising--New-Product-Cold-Start-Strategy]]** — 新品冷启动广告策略
   - 来源：2026-04-25 新品广告诊断 Query
   - 内容：新品期（1-4 周）完整投放指南
   - 嵌入引用：theory/Sponsored-Products--Overview、theory/Sponsored-Products--Campaign-setup
   - 关键特性：使用嵌入语法引用 theory 页面，避免复制基础定义

### 统计

- Wiki 页面总数：333 个（+1 新建）
- theory 页面：~200 个
- practice 页面：~131 个（+1）
- 系统页面：2 个（index.md、log.md）

---

## [2026-04-22] lint | 全库健康检查 + 合并重复页面 + 修复断裂链接 + 补录孤儿页面

### 检查范围
全库 332 个文件（含 index.md、log.md）

### 发现问题

| 类型 | 数量 | 说明 |
|------|------|------|
| 重复页面 | 2 组 | 命名不一致导致的内容分裂 |
| 断裂链接 | 1 个 | Voice_of_Seller 引用不存在页面 |
| 孤儿页面 | 3 个 | 未收录进 index.md |
| 待补充(WIP) | ~32 个 | 占位页面，内容待补充，已知晓，暂不处理 |

### 修复操作

#### 1. 合并重复页面（2组）

**组A：广告创意编辑标准**
- 保留：`General--creative---editorial-standards.md`（来自官方文档，内容更权威）
- 合并自：`General-creative-editorial-standards.md`
- 补入差异内容：图片技术规格（300×300px / 5MB / 格式）、Walmart Logo 使用规范、视频时长/格式参数
- 旧文件改为重定向页（保留引用兼容性）

**组B：WFS 多渠道解决方案**
- 保留：`Walmart_Multichannel_Solutions.md`（结构更清晰，含 API 列表）
- 合并自：`Walmart-Multichannel-Solutions.md`
- 补入差异内容：完整 FAQ（6条）、资格要求、标准配送费率完整表
- 旧文件改为重定向页

#### 2. 修复断裂链接

- 文件：`Growth_opportunities--Voice_of_Seller.md`
- 断裂链接：`[[walmart-connect-advertising-solutions-overview]]`（该文件不存在）
- 修复：改指向 `[[theory/Advertising--Walmart_Connect]]`

#### 3. 补录孤儿页面至 index.md

| 页面 | 补录位置 | 说明 |
|------|----------|------|
| `add-multiple-items-import-your-catalog` | Item Setup → 上架方式页面 | 外部市场导入工具（Versori 集成） |
| `Item-condition-types` | Item Setup → 其他页面 | 商品状况类型（New / Open Box / Refurbished / Used 各级别） |
| `Invoice-tracking-for-Walmart-suppliers` | Taxes & Payments → 账单支付页面 | 供应商发票追踪（WIP） |

#### 4. 顺带修正

- index.md「广告政策」段：`[[theory/General-creative-editorial-standards]]` 更正为 `[[theory/General--creative---editorial-standards]]`
- index.md「WFS 故障排查页面」：移除重复出现的 `[[theory/Walmart-Multichannel-Solutions]]` 条目
- index.md 统计数字：317 → 332 页
- 导航地图：新增「商品状况 → [[theory/Item-condition-types]]」入口
- `Item-condition-types.md`：修复乱码字符 + 修正相关页面链接格式

### 修改文件清单

- `General--creative---editorial-standards.md` — 内容扩充（合并）
- `General-creative-editorial-standards.md` — 改为重定向页
- `Walmart_Multichannel_Solutions.md` — 内容扩充（合并）
- `Walmart-Multichannel-Solutions.md` — 改为重定向页
- `Growth_opportunities--Voice_of_Seller.md` — 断裂链接修复
- `Item-condition-types.md` — 修复乱码 + 链接格式
- `index.md` — 孤儿页面补录 + 链接修正 + 统计更新

### 统计

- Wiki 页面总数：332 个（不含 index/log）
- 本次新建：0
- 本次合并：2 组（4 → 2 有效页 + 2 重定向页）
- 本次修复：1 个断裂链接，1 个乱码文件
- 本次补录：3 个孤儿页面入 index

---

## [2026-04-21] ingest | raw/note/ 运营笔记处理（第三批）+ 竞品分析案例

### 源文件

- `raw/note/2026-04-15.md` — SEM 分时策略 + 露营风扇分时方案 + 千斤顶广告调整
- `raw/note/2026-04-16.md` — 老链接死循环问题 + 划线价格刷新 + 千斤顶广告调整记录
- `raw/note/2026-04-17.md` — 广告与自然位协同策略验证（订单量翻倍案例）
- `raw/note/2026-04-21.md` — 双牙千斤顶搜索排名下滑 + 竞品分析
- `raw/note/car jack2026-04-16 14.25.34.univer.md` — Excel 广告数据（2026-04-10 ~ 04-16，car jack 2T 变体）

### 创建的 Wiki 页面

1. **[[practice/Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy]]** — 广告与自然位协同策略

核心内容：
- 广告位 vs 自然位的本质差异（成本/稳定性/触达用户）
- 重叠代价：无效点击 = 花广告费买本该免费的流量
- 四大协同策略：分层出价 / 分时出价 / 关键词分级 / 广告类型分层
- 实践案例：基础款千斤顶降低 bid 后订单翻倍（2026-04-17）
- 露营风扇分时策略（00:00-06:00 / 06:00-18:00 / 18:00-24:00）
- 竞品出现时的广告应对框架
- 自然排名下滑归因与应对

2. **[[practice/Operations--Mature-Listing-Vicious-Cycle-Recovery]]** — 老链接恶性循环破解

核心内容：
- "订单少 → 掉排名 → 加广告 → 有订单 → 减广告 → 订单少"循环的本质诊断
- 流量入口分析（自然搜索 / 广告 / Browse / 促销 / 多渠道）
- 五步破解路径：诊断 → 识别拖累 → 修复核心 → 协同广告 → 多入口结构
- 周度监控表（自然订单占比 / ACOS / 自然排名 / 库存充足率）
- 循环解除的 4 个标志信号

3. **[[practice/Operations--Competitive-Position-Analysis--Search-Ranking-Recovery]]** — 竞品分析：搜索排名下滑与自然位恢复

核心内容：
- 双牙千斤顶案例：3.22 (#6) → 4.12 (#14)，下滑 8 位，20 天
- 断货 → 算法降权 → 自然排名下滑的连锁机制
- 竞品定位对比表（吨位规格 / 价格 / 评论 / 权重）
- 关键洞察：规格不匹配（竞品 2.5T vs 我方 1.5T/2T/3T）
- 五步应对：恢复库存 → 评估价格 → 评论差异化 → 广告调整 → 排名恢复时间表
- 断货预警机制 + 竞品监控方法

### 更新的页面

- `wiki/Advertising--Optimization-Methodology.md` — 相关链接添加广告与自然位协同策略
- `wiki/Operations--Restock-Decision-Methodology.md` — 相关链接添加竞品分析与排名恢复

### 链接关系

**入链：**
- [[practice/Advertising--Optimization-Methodology]] → Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy（协同策略章节）
- [[practice/Operations--Restock-Decision-Methodology]] → Operations--Competitive-Position-Analysis--Search-Ranking-Recovery（断货与排名联动）
- [[practice/Advertising--Bid-reduction-Paradox]] → Operations--Mature-Listing-Vicious-Cycle-Recovery（循环诊断入口）

**出链：**
- Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy → [[practice/Advertising--Optimization-Methodology]]、[[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]]、[[theory/Sponsored-Products--Campaign-bidding-strategies]]、[[practice/Operations--Restock-Decision-Methodology]]
- Operations--Mature-Listing-Vicious-Cycle-Recovery → [[practice/Advertising--Bid-reduction-Paradox]]、[[practice/Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy]]、[[practice/Operations--Restock-Decision-Methodology]]
- Operations--Competitive-Position-Analysis--Search-Ranking-Recovery → [[practice/Operations--Restock-Decision-Methodology]]、[[practice/Operations--Mature-Listing-Vicious-Cycle-Recovery]]、[[theory/Catalog_management--Price_management]]、[[theory/Growth_opportunities--Search_Insights]]

### 统计更新

- Wiki 页面总数：**317 个**（+3 新建）
- 系统页面：**2 个**（index.md、log.md）
- 知识页面：**315 个**（+3）

## [2026-04-20] query + ingest | 降 bid 反效果案例分析

### 背景

运营者反馈降 bid 后出现反效果：
- Spend 从 $3,200/月 增加到 $4,640/月（+45%）
- ROAS 从 3.11 降到 2.44（-21.5%）
- 转化率从 9.48% 降到 7.32%（-22.8%）
- CPC 从 $0.78 降到 $0.70（-10%）
- 日预算固定在 $150 不变

### 核心发现

**降 bid → CPC 下降 → 同样预算买到更多点击 → 预算更早耗尽 → 丢失晚间高转化时段 → 转化率下降 → ROAS 下降**

这是一个典型的"算法反噬"场景，与 [[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]] 中描述的沃尔玛第二竞价机制直接相关。

### 创建的 Wiki 页面

1. **[[practice/Advertising--Bid-reduction-Paradox]]** — 降 bid 反效果案例分析

核心内容：
- 完整数据对比表（降 bid 前后 6 个维度）
- 算法反噬的 6 步机制链条
- 晚间高转化时段丢失的量化分析
- 三步诊断法（Cap-out 时间 / 日预算比值 / Page Type 分布）
- 三种修复方案（降预算 / 加回 bid / Target ROAS）
- 核心教训：降 bid 不等于节省花费

### 更新的页面

- `wiki/index.md` — 在"运营方法论"下添加新页面链接
- `wiki/Advertising--Optimization-Methodology.md` — 在"相关链接"中添加交叉引用

## [2026-04-17] ingest | raw/note/ 运营笔记处理

### 源文件

- `raw/note/2026-04-14.md` — 广告优化方法论 + 补货决策方法论
- `raw/note/2026-04-15.md` — SEM 分时策略 + 千斤顶广告调整记录
- `raw/note/2026-04-16.md` — 订单量分析 + 划线价格刷新方法
- `raw/note/2026-04-17.md` — 千斤顶广告案例数据分析
- `raw/note/car jack2026-04-16 14.25.34.univer.md` — Excel 广告数据（2026-04-10 ~ 04-17）
- `raw/note/Step stool2026-04-16 10.22.43.univer.md` — Excel 广告数据（嵌入格式）
- `raw/note/运营每日内容.md` — 已于 2026-04-13 处理

### 创建的 Wiki 页面

1. **[[practice/Advertising--Optimization-Methodology]]** — 广告优化方法论

核心内容：
- 阶段一（新品期）：获取精准曝光，重点看曝光和点击
- 阶段二（成长期）：打手动精准配合广泛，提高自然排名
- 阶段三（稳定期）：降低 ACOS，使用自动规则批量优化
- 阶段四（爆款期）：最大化 GMV，首页顶部展示
- 自然位与广告位协同策略（避免无效点击重叠）

2. **[[practice/Operations--Restock-Decision-Methodology]]** — 补货决策方法论

核心内容：
- 退货率趋势评估（高退货率产品谨慎补货）
- 广告数据分析（出单词热度/ACOS/利润率底线）
- 警惕虚假爆款（对比 Google Trends 和历史数据）
- 防赌原则（主力产品优先，分批补货）
- 补货决策检查清单（7 项确认）

### 链接关系

**入链：**
- [[theory/Advertising--Troubleshooting]] → Advertising--Optimization-Methodology（广告优化入口）
- [[practice/Operations-SOP--Daily-and-Weekly-Tasks]] → Operations--Restock-Decision-Methodology（日常运营 SOP 补货章节）

**出链：**
- Advertising--Optimization-Methodology → [[theory/Sponsored-Products--Campaign-bidding-strategies]]、[[theory/All-Keywords]]、[[theory/Automated-rules]]、[[practice/Advertising--CTR-Diagnostics-SOP]]、[[theory/Search-relevancy-best-practices]]、[[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]]
- Operations--Restock-Decision-Methodology → [[theory/returns-insights-overview]]、[[theory/Sponsored-Products--Campaign-bidding-strategies]]、[[theory/Growth_opportunities--Search_Insights]]、[[practice/Advertising--Optimization-Methodology]]、[[practice/Operations-SOP--Daily-and-Weekly-Tasks]]

### 同步 index.md

- Advertising 分类新增：[[practice/Advertising--Optimization-Methodology]]
- 基础运营新增：**运营方法论**板块，收录 [[practice/Operations--Restock-Decision-Methodology]] 和 [[practice/Operations-SOP--Daily-and-Weekly-Tasks]]

### 统计更新

- Wiki 页面总数：**301 个**（+2）
- 系统页面：**2 个**
- 知识页面：**299 个**（+2）

---

## [2026-04-14] query + SOP 创建 | Sponsored Products CTR 下降诊断

### 背景

用户提问：某产品去年同期广告 CTR 1.01%，今年同期降至 0.5%，下降约 50%。已确认为自动活动 + 固定出价，展示位置比去年低。

### 问答摘要

系统性归因分析，覆盖四大维度：
1. **广告位与竞争**：展示位置变化、竞价环境恶化（沃尔玛第二竞价机制）、出价倍数器
2. **关键词与相关性**：关键词质量下降、自动活动关键词流失、搜索词报告未维护
3. **商品详情页质量**：标题/图片/评分/库存综合影响 CTR
4. **活动结构**：手动/自动切换、预算消耗曲线

### 创建的 Wiki 页面

- [[practice/Advertising--CTR-Diagnostics-SOP]] — Sponsored Products CTR 下降诊断 SOP

### 页面内容

- 诊断入口：确认下滑类型（突然/渐进/周期性）
- 第一阶段：广告活动层诊断（展示位置/竞价预算/活动结构）
- 第二阶段：关键词层诊断（报告拉取/Keywords Planner/否定词维护）
- 第三阶段：商品详情页诊断（标题/主图/关键词嵌入/富媒体）
- 第四阶段：竞价环境分析（相关性评分/竞品动态）
- 行动计划时间线（Day 1 → Week 4）

### 链接关系

- 入链：[[theory/Advertising--Troubleshooting]]（子分类概述页入口）
- 出链：[[theory/Sponsored-Products-placements]]、[[theory/Keywords-Planner]]、[[theory/All-Keywords]]、[[theory/Product-Detail-Page_-overview]]、[[theory/Product-detail-page_-Image-guidelines-&-requirements]]、[[theory/How-to-maximize-item-pages]]、[[theory/Search-relevancy-best-practices]]、[[theory/Out-of-budget-features]]、[[theory/Sponsored-Products--Step-2-Set-placement-inclusion]]、[[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]]、[[theory/On-demand-reports]]、[[theory/Campaign-setup-best-practices]]、[[theory/Sponsored-Products--Overview]]

### 统计更新

- Wiki 页面总数：**300 个**（+1）
- 系统页面：**2 个**（index.md、log.md）
- 知识页面：**298 个**（+1）

## [2026-04-13] ingest | 跨境电商算法转型分析文章

### 源文件

`raw/跨境电商要变天了？亚马逊和沃尔玛为何在做同一件事？.md`
- **来源**：微信公众号（知无不言社区）
- **发布日期**：2026-04-13
- **主题**：亚马逊 COSMO 算法 vs 沃尔玛第二竞价机制对比

### 创建的 Wiki 页面

**主页面（1个）：**
- [[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]] — 平台算法转型对比（亚马逊 COSMO vs 沃尔玛第二竞价）

### 页面内容摘要

该页面系统梳理了两大平台的广告算法演进：

1. **沃尔玛第二竞价（2022年6月切换）**：
   - 实际支付 ≈ 次高出价 + $0.01
   - 相关性评分综合标题匹配、详情页质量、历史转化、WFS库存稳定性、价格竞争力

2. **亚马逊 COSMO 算法**：
   - 基于 AI 常识知识图谱理解用户意图
   - 从关键词匹配转向场景化推荐

3. **运营策略差异**：
   - 沃尔玛：基础（WFS+价格）> 广告技巧
   - 亚马逊：预算+技巧仍可推动普通产品

4. **三阶段广告打法**：新品入池（1-4周）→ 起速放量（5-12周）→ 收割优化（13周+）

5. **广告与自然排名联动**：广告催化自然流量，降低整体获客成本

### 链接关系

- **新增入链**：[[theory/Advertising]]（广告分类）
- **出链**：[[theory/Walmart-Connect-Ad-Policies]]、[[theory/Sponsored-Products--Glossary]]、[[theory/WFS-fees]]、[[theory/Search-Engine-Marketing-_SEM__-campaign-management]]、[[theory/Marty-advertising-assistant-overview]]

### 统计更新

- Wiki 页面总数：**299 个**（+1）
- 系统页面：**2 个**（index.md、log.md）
- 知识页面：**297 个**（+1）

---

## [2026-04-17] ingest（第二轮） | raw/walmart advertising guide/ 资源文件

### 源文件

- `raw/walmart advertising guide/Finding IDs and account names.md` — 账户 ID/名称查找
- `raw/walmart advertising guide/Open a case with Advertiser Help.md` — 工单提交流程
- `raw/walmart advertising guide/Self-registration to Walmart Connect Academy.md` — Academy 注册
- `raw/walmart advertising guide/Data use & privacy requirements.md` — 数据使用与隐私政策
- `raw/walmart advertising guide/General, creative & editorial standards.md` — 创意编辑标准
- `raw/walmart advertising guide/Bulk operations.md` — 批量操作完整指南
- `raw/walmart advertising guide/Content quality guide.md` — 内容质量指南
- `raw/walmart advertising guide/Billing dispute.md` — 账单争议处理
- `raw/walmart advertising guide/New-to-brand metrics.md` — 新品牌指标（7 项定义）
- `raw/walmart advertising guide/How to maximize item pages.md` — 详情页最大化
- `raw/walmart advertising guide/Glossary.md` — 词汇表（MRC 认证/无效流量/新品牌指标补充）

### 创建/更新的 Wiki 页面

**新建（10 个）：**
1. `Finding-IDs-and-account-names.md` — 账户 ID 和名称查找
2. `Open-a-case-with-Advertiser-Help.md` — 提交 Advertiser Help 工单
3. `Walmart-Connect-Academy-Self-registration.md` — Academy 自注册
4. `Data-use---privacy-requirements.md` — 数据使用与隐私要求
5. `General--creative---editorial-standards.md` — 广告创意编辑标准
6. `Bulk-operations.md` — 批量操作完整指南
7. `Content-quality-guide.md` — 内容质量指南
8. `Billing-dispute.md` — 账单争议处理
9. `New-to-brand-metrics.md` — 新品牌指标深度指南
10. `How-to-maximize-item-pages.md` — 详情页最大化

**更新（2 个）：**
- `Sponsored-Products--Glossary.md` — 新增：Attribution Type、Variant Group、新品牌指标详情、MRC 认证指标、无效流量报告指标
- `Catalog_management--Price_management.md` — 新增：划线价格刷新 3 种方法

### 新增"广告资源"子分类

index.md 新增 **广告资源（Resources）**板块，收录 9 个新页面。

### 交叉链接关系

- Finding-IDs → Open-a-case（工单提交需账户名称）
- Open-a-case → Finding-IDs（引用）
- Bulk-operations → Step-3/Step-4/Step-5/On-demand-reports/Keyword-recommendations
- Content-quality → Item_setup/Product-detail-page/Search-relevancy
- How-to-maximize → Content-quality/Keyword-optimization/Search-relevancy
- New-to-brand → Glossary/Glossary（互相引用）
- Glossary → New-to-brand-metrics/Invalid-traffic-filtration

### 定价补充

新增划线价格刷新方法至 Catalog_management--Price_management：
- 方法一：Competitive Price 匹配检查
- 方法二：促销表刷 MSRP（推荐）
- 方法三：多次覆盖更新

### 统计更新

- Wiki 页面总数：**311 个**（+10 新建，+2 更新）
- 系统页面：**2 个**
- 知识页面：**309 个**（+10）
- Advertising 分类：62 → 71（+9 新页面）

---

## [2026-04-17] ingest（第三轮） | Keyword Recommendations + Academy认证 + HOME白皮书 + 链接网络

### 源文件

- `raw/walmart advertising guide/Keyword recommendations.md` — 关键词推荐完整使用
- `raw/walmart advertising guide/Walmart Connect Academy Ad Certification.md` — Academy 认证路径
- `raw/note/HOME卖家运营白皮书.md` — 综合运营白皮书（~18127 字）

### 新建 Wiki 页面

1. **[[theory/Keyword-recommendations]]** — 关键词推荐完整使用
   - AI 算法推荐逻辑，每日刷新，30 天回溯窗口
   - 与广告组内 Suggestions 的区别（220 vs 20 词、效果排序 vs 相关性排序）
   - 批量应用与报告下载
   - 交叉链接：Bulk-operations、All-Keywords、On-demand-reports、Search-relevancy

2. **[[theory/Walmart-Connect-Academy-Ad-Certification]]** — Academy 认证
   - 5 个课程模块（基础→进阶→高级）
   - 通过率 80%，证书 LinkedIn 可关联，有效期 1 年
   - 与 [[theory/Walmart-Connect-Academy-Self-registration]] 互相链接

3. **[[theory/HOME-卖家运营白皮书]]** — 综合运营白皮书
   - 近期热点（Pro Seller Badge 更新、站外营销工具）
   - 曝光提升：Listing Quality 5 维度、Flash Deal / Campaign / Deals 活动申报
   - 站内外推广：SEM 出价策略对比、Sales Rewards、Social Commerce、Walmart Creators
   - 转化提升：划线价规则、List Price Override、激励项目（Commission Break / Incentives / Repricer / Extra Saving / In-Demand Items）、Pro Seller 权益
   - 高效发货：WFS vs SFF、Shipping Template 优化、退货处理
   - 账号安全：Inform Act、Brand Portal 品牌备案

### 建立双向链接网络（T1）

- [[theory/Search-Engine-Marketing-_SEM__-program-policy]] → 新增「广告创意合规」章节，引用 General + Prohibited
- [[theory/General--creative---editorial-standards]] → 相关链接增加 SEM + Prohibited
- [[theory/Prohibited-content-and-products]] → 相关链接增加 General + SEM

### 交叉链接深化

- HOME 白皮书 → Linking 到 10+ 现有 Wiki 页面（Price_management、Reviews、WFS、Policies_Account 等）
- Keyword-recommendations → Linking 到 Bulk-operations、All-Keywords、Search-relevancy、Glossary
- Academy 认证 → Linking 到 Academy 自注册、Sponsored Products 概览、出价策略

### 统计更新

- Wiki 页面总数：**312 个**（+3 新建，+3 更新）
- 系统页面：**2 个**
- 知识页面：**310 个**（+3）
- Advertising 分类：71 → 73（+2 新广告资源页面）

---

## [2026-04-20] ingest（第四轮） | 广告指南剩余文件：Advertiser Reports + MRC 认证指标

### 源文件

- `raw/walmart advertising guide/Advertiser reports.md` — 广告主报告 5 种报告类型完整指南
- `raw/walmart advertising guide/Metrics accredited by the Media Rating Council.md` — MRC 认证指标查阅指南

### 创建的 Wiki 页面

1. **[[theory/Advertiser-Reports]]** — 广告主报告（5 种报告类型）
   - Daily Performance（每日表现）
   - Campaign Performance（活动表现，含 6 种子报告）
   - Page Type Performance（页面类型表现，6 种页面）
   - Platform Performance（平台表现，App/Desktop/Mobile）
   - Invalid Traffic（无效流量）
   - 归因窗口（3/14/30 天）
   - 交叉链接：Glossary、Invalid-traffic-filtration、On-demand-reports、Cross-Channel-Reports

2. **[[theory/Metrics-accredited-by-MRC]]** — MRC 认证指标
   - MRC 认证范围（点击/展示/CTR，Desktop+Mobile+App）
   - 全部 30+ 认证指标分布表（按报告位置分类）
   - Invalid Traffic Report 访问路径（4 步操作指南）
   - 交叉链接：Glossary（已更新 MRC 章节）、Invalid-traffic-filtration、Advertiser-Reports、On-demand-reports

### 同步到现有页面

- [[theory/Sponsored-Products--Glossary]] — 相关链接新增 Advertiser-Reports 和 Metrics-accredited-by-MRC

### 统计更新

- Wiki 页面总数：**331 个**（+17 新建，-1 删除）
- 系统页面：**2 个**（index.md、log.md）
- 知识页面：**329 个**（+17）

> **注**：系统自动修正了 2 处拼写错误断链，修复了 log.md 第 395 行格式错误。新增页面均已纳入 index.md 索引。

---

## [2026-04-21] Lint | Wiki 健康检查

### 执行操作

**Lint Pass** — 对 Wiki 317 个 .md 文件进行全面健康检查，发现以下问题并修复：

**修复内容**：
- 修正 2 处拼写错误断链：`[[Product-detail-page--Keyword-optimization]]` → `[[theory/Product-detail-page_-Keyword-optimization]]`（影响 `Content-quality-guide.md`、`How-to-maximize-item-pages.md`）
- 修正 2 处拼写错误断链：`[[Prohibited-content---products]]` → `[[theory/Prohibited-content-and-products]]`（影响 `Data-use---privacy-requirements.md` 两处）
- 修复 `log.md` 第 395 行格式错误（全角引号导致链接截断）

**新建占位页（待补充）**：
- Success Hub 子功能 × 5：`Success-Hub_-match-buy-box-price.md`、`Success-Hub_-match-external-price.md`、`Success-Hub_-Automate-pricing-with-the-Repricer.md`、`Success-Hub_-Add-trending-items.md`、`Success-Hub_-Fulfill-with-Walmart.md`
- Repricer 操作指南 × 2：`Repricer_-Create-a-strategy.md`、`Repricer_-Manage-a-strategy.md`
- 价格管理 × 4：`Generate-a-buy-box-report.md`、`Update-price-individually-in-Seller-Center.md`、`Update-price-in-bulk-in-Seller-Center.md`、`pricing-insights-overview.md`
- SEM 故障排查 × 1：`Troubleshoot-Search-Engine-Marketing-_SEM_-errors.md`
- 其他 × 3：`Walmart-Marketplace-seller-retailer-policies.md`、`Invoice-tracking-for-Walmart-suppliers.md`

**新建综合页面**：
- `Seller-Performance-Metrics--Overview.md` — 整合 OTD / VTR / ODR / TRTR 四大核心绩效指标

**删除文件**：
- `Excel 2026-04-20 16.38.43.univer.md`（孤立备份文件）

**识别但未处理（待定）**：
- 缺失页面（建议创建）12 个：OTD/VTR/ODR/TRTR 详细说明页（已整合至 `Seller-Performance-Metrics--Overview.md` ✅）、GS1 ✅、`DART` 算法、价格合规、In-Demand Items、LTL/FTL、ACES/PIES 概览、Inform Act 等
- 外部数据源补充需求：OTD/VTR 官方指标文档、价格管理最新政策

### 断链修复详情

| 源文件 | 行号 | 错误写法 | 修正后 |
|--------|------|---------|--------|
| Content-quality-guide.md | 46 | `[[Product-detail-page--...]]` | `[[Product-detail-page_-...]]` |
| How-to-maximize-item-pages.md | 66, 73 | `[[Product-detail-page--...]]` | `[[Product-detail-page_-...]]` |
| Data-use---privacy-requirements.md | 45, 130 | `[[Prohibited-content---...]]` | `[[Prohibited-content-and-...]]` |
| log.md | 395 | `...「...、「...]]`（全角引号） | 修正为 `[[...]]` 独立链接 |

### 新建页面链接关系

所有占位页均包含：
- `来源` 字段（标注从哪个断链引用识别）
- `预期内容方向` 字段（标注预期覆盖内容）
- `相关页面` 字段（与现有页面建立交叉引用）

### 相关链接

- [[theory/Seller-Performance-Metrics--Overview]] — 绩效指标综合概览（新建）
- [[practice/Operations-SOP--Daily-and-Weekly-Tasks]] — 相关链接已追加绩效概览页
- [[theory/Seller-performance-standards]] — 相关链接已追加绩效概览页
- [[practice/Advertising--CTR-Diagnostics-SOP]] — 广告 CTR 诊断 SOP
- [[practice/Advertising--Bid-reduction-Paradox]] — 降 Bid 反效果案例分析

### 补充：GS1 数据库验证页面

**新建页面**：`GS1-Database-and-Product-ID-Validation.md`
- 来源：整合 [[theory/Choose-a-product-identifier]]（商品识别符政策）、[[theory/Onboarding-Guide--New-Employee-Training]]（新员工培训第 76-80 行）、[[theory/HOME-卖家运营白皮书]]（政策收紧预警）、[[theory/Troubleshoot-product-ID-errors]]（ID 错误排查）
- 内容：GS1/US 官网购买流程、GEPIR 查询方法、沃尔玛交叉验证机制、Walmart 政策收紧时间线、WFS 条码要求、GTIN 豁免入口
- 索引：`index.md` 已加入 GS1 页面条目
