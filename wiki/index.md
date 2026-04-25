# Walmart Marketplace 知识库

> LLM 增量维护的 Walmart 卖家运营知识库，基于官方帮助文档自动编译。

---

## 📚 知识库结构说明

本知识库采用**分层治理**架构，实现知识品质的可持续发展：

| 层级 | 目录 | 来源 | 特点 | 访问权限 |
|------|------|------|------|----------|
| **核心知识区** | `wiki/theory/` | Walmart 官方文档 | 纯陈述句，无主观建议，工具性 | 只读（管理员维护） |
| **标准方法论区** | `wiki/practice/` | 运营笔记→审核→通过 | 经审核的运营实践、策略、SOP | 全员可见 |
| **待审区** | `wiki/pending/` | 新摄入的心得、SOP、研究 | 隔离缓冲区，待审核 | 仅提交者和审核者可见 |
| **存档区** | `wiki/archive/` | 被拒绝或已弃用的内容 | 已驳回或过时的页面 | 参考用途 |

**引用规则**：
- ✅ Practice 可以引用 Theory（使用嵌入语法 `![[theory/...]]`）
- ✅ Pending 可以引用 Theory 和 Practice（但会被审核）
- ❌ Theory 禁止引用 Practice / Pending（保持知识纯度）
- ❌ Practice 禁止引用 Pending（仅引用已审核的内容）

**工作流**：
```
同事提交心得 → Agent 整理至 pending/（隔离）
    ↓
你（或资深运营）通过 PR 查看 pending/（加入审核元数据）
    ↓
审核通过 → 移动至 practice/（全员可见）
审核拒绝 → 标记 rejected，移至 archive/（留存记录）
```

---

## 分类索引

### 📦 基础运营

**运营方法论：**
| [[practice/Operations--Restock-Decision-Methodology]] | 补货决策方法论（多维度评估） | 1 |
| [[practice/Operations-SOP--Daily-and-Weekly-Tasks]] | 日常运营 SOP（日/周工作清单） | 1 |
| [[theory/HOME-卖家运营白皮书]] | HOME 卖家运营白皮书（综合运营指南，1 8K字） | 1 |
| [[practice/Operations--Mature-Listing-Vicious-Cycle-Recovery]] | 老链接恶性循环破解（流量入口结构诊断） | 新增 |
| [[practice/Operations--Competitive-Position-Analysis--Search-Ranking-Recovery]] | 竞品分析与搜索排名恢复策略 | 新增 |
| [[practice/Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy]] | 广告与自然位协同策略（避免无效重叠） | 新增 |

| 分类 | 说明 | 页面数 |
|------|------|--------|
| [[theory/Getting_started]] | 新卖家入门指引 | 4 |
| [[theory/Onboarding-Guide--New-Employee-Training]] | **新员工培训指南**（新人必读，30 天成长路径）| 1 |
| [[theory/Catalog_management]] | 商品目录管理（增删改查、价格、库存、报告） | 4 |
| [[theory/Item_setup]] | 商品上架配置（内容、图片、变体、汽车适配） | 8 |

### 🚚 配送履约

| 分类 | 说明 | 页面数 |
|------|------|--------|
| [[theory/Seller_Fulfillment_Services]] | 卖家自配送（FBM）配置 | 6 |
| [[theory/Walmart_Fulfillment_Services__WFS_]] | WFS 仓储配送（Walmart 自营仓） | 16 |

### 💰 财务与增长

| 分类 | 说明 | 页面数 |
|------|------|--------|
| [[theory/Taxes_&_payments]] | 收款、结算、税务、账单 | 10 |
| [[theory/Growth_opportunities]] | 增长工具、激励计划、评论管理 | 13 |
| [[theory/Advertising]] | Walmart Connect 广告（SEM、展示） | 73 |

### 📋 订单与政策

| 分类 | 说明 | 页面数 |
|------|------|--------|
| [[theory/Order_management]] | 订单生命周期、客服、退换货、故障排查 | 18 |
| [[theory/Policies_&_standards]] | 卖家合规政策与绩效标准 | 11 |

---

## 知识页面目录

### Advertising（广告）

**基础知识 (Theory)：**
- [[theory/Advertising--Overview]] — 广告解决方案总览
- [[theory/Advertising--Walmart_Connect]] — Walmart Connect 站内广告
- [[theory/Sponsored-Products--Overview]] — Sponsored Products 概览
- [[theory/Sponsored-Products--Campaign-setup]] — 活动设置完整流程
- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略详解
- [[theory/Sponsored-Products-placements]] — 展示位置详解
- [[theory/Keywords-Planner]] — 关键词规划器
- [[theory/Keyword-recommendations]] — 关键词推荐
- [[theory/All-Keywords]] — 关键词管理
- [[theory/Sponsored-Products--Glossary]] — 术语词汇表

**运营方法论 (Practice)：**
- [[practice/Advertising--Optimization-Methodology]] — 广告优化方法论（阶段性目的驱动）
- [[practice/Advertising--New-Product-Cold-Start-Strategy]] — 新品冷启动广告策略（1-4 周完整指南）
- [[practice/Advertising--CTR-Diagnostics-SOP]] — CTR 下降诊断 SOP
- [[practice/Advertising--Bid-reduction-Paradox]] — 降 bid 反效果案例分析
- [[practice/Advertising--Traffic-Pattern-Analysis--Ad-vs-Organic-Synergy]] — 广告与自然位协同策略
- [[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]] — 沃尔玛算法与广告策略联动

**广告资源（Resources）：**
- [[theory/Finding-IDs-and-account-names]] — 查找广告账户 ID 和名称
- [[theory/Open-a-case-with-Advertiser-Help]] — 提交 Advertiser Help 工单
- [[theory/Walmart-Connect-Academy-Self-registration]] — Walmart Connect Academy 自注册
- [[theory/Walmart-Connect-Academy-Ad-Certification]] — 广告认证考试路径（新增）
- [[theory/Keyword-recommendations]] — 关键词推荐完整使用指南（新增）
- [[theory/Data-use---privacy-requirements]] — 数据使用与隐私要求
- [[theory/General--creative---editorial-standards]] — 广告创意与编辑标准
- [[theory/Bulk-operations]] — 批量操作完整指南
- [[theory/Content-quality-guide]] — 内容质量指南
- [[theory/Billing-dispute]] — 账单争议处理
- [[theory/Sponsored-Products--Glossary]] — 词汇表（MRC 认证指标/新品牌指标补充）

**广告活动页面：**
- [[theory/Advertise-with-Walmart-Connect-sponsored-search]] — Sponsored Search 详解
- [[theory/Search-Engine-Marketing-_SEM__-campaign-management]] — SEM 活动管理
- [[theory/Search-Engine-Marketing-_SEM__-campaign-setup]] — SEM 活动设置
- [[theory/Search-Engine-Marketing-_SEM__-program-policy]] — SEM 政策合规
- [[theory/Troubleshoot-Search-Engine-Marketing-_SEM_-errors]] — SEM 故障排查（待补充）
- [[theory/sales-rewards-attribution-program-generate-referral-links]] — 生成推荐链接
- [[theory/walmart-connect-advertising-onsite-display]] — Onsite Display
- [[theory/walmart-connect-solutions-brand-shop-shelf]] — Brand Shop
- [[theory/Getting-started-with-Sponsored-Search]] — Sponsored Search 完整指南
- [[theory/Accessing-Walmart-Connect-Ad-Center]] — 访问 Ad Center
- [[theory/Creating-and-managing-ad-accounts]] — 创建和管理广告账户
- [[theory/User-roles-and-permissions]] — 用户角色和权限
- [[theory/Account-access-as-a-non-admin-user]] — 非管理员访问管理

**Sponsored Products（商品推广）：**
- [[theory/Sponsored-Products--Overview]] — Sponsored Products 概览
- [[theory/Sponsored-Products--Glossary]] — 术语词汇表
- [[theory/Sponsored-Products--Campaign-setup]] — 活动设置完整流程
- [[theory/Sponsored-Products--Step-1-Create-an-automatic-campaign]] — 创建自动活动
- [[theory/Sponsored-Products--Create-a-manual-campaign]] — 创建手动活动
- [[theory/Sponsored-Products--Expanded-targeting]] — 扩展定向
- [[theory/Sponsored-Products--Step-2-Set-placement-inclusion]] — 设置展示位置
- [[theory/Sponsored-Products--Step-3-Add-bid-multipliers]] — 添加出价倍数器
- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组
- [[theory/Sponsored-Products--Step-4-continued-Add-items-to-an-ad-group]] — 添加商品到广告组
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 添加和选择关键词
- [[theory/Sponsored-Products--Campaign-bidding-strategies]] — 出价策略详解
- [[theory/Sponsored-Products--Dynamic-bidding]] — 动态出价
- [[theory/Sponsored-Products--Target-ROAS-bidding]] — 目标 ROAS 出价
- [[theory/Sponsored-Products-placements]] — 展示位置详解

**报告与分析：**
- [[theory/All-Campaigns]] — 全部活动管理
- [[theory/All-Keywords]] — 全部关键词管理
- [[theory/New-to-brand-metrics]] — 新品牌指标详解
- [[theory/Item-Health-reports]] — 商品健康报告
- [[theory/Cross-Channel-Reports]] — 跨渠道报告
- [[theory/Path-to-Conversion]] — 转化路径
- [[theory/Walmart-Ad-Mix-Modeling]] — Ad Mix Modeling
- [[theory/On-demand-reports]] — 按需报告
- [[theory/Custom-reports]] — 自定义报告
- [[theory/Advertiser-Reports]] — 广告主报告（5 种报告类型，第四轮新增）
- [[theory/Metrics-accredited-by-MRC]] — MRC 认证指标查阅指南（第四轮新增）

**优化工具：**
- [[theory/Keywords-Planner]] — 关键词规划器
- [[theory/Automated-rules]] — 自动规则
- [[theory/Item-recommendations]] — 商品推荐
- [[theory/Keyword-recommendations]] — 关键词推荐
- [[theory/Personalized-recommendations-overview]] — 个性化推荐概览
- [[theory/Bidding-strategy-recommendations]] — 出价策略推荐
- [[theory/Out-of-budget-features]] — 超预算功能
- [[theory/Bulk-operations]] — 批量操作
- [[theory/Search-relevancy-best-practices]] — 搜索相关性最佳实践
- [[theory/How-to-maximize-item-pages]] — 最大化商品详情页
- [[theory/Campaign-setup-best-practices]] — 活动设置最佳实践
- [[theory/Finding-IDs-and-account-names]] — 查找 ID 和账户名称
- [[theory/Marty-advertising-assistant-overview]] — Marty 广告助手（AI）

**广告政策：**
- [[theory/Walmart-Connect-Ad-Policies]] — 广告政策总览
- [[theory/General--creative---editorial-standards]] — 创意与编辑标准
- [[theory/Category-specific-requirements]] — 类别特定要求
- [[theory/Prohibited-content-and-products]] — 禁止内容与商品
- [[theory/Sponsored-Products--Glossary]] — 术语表

**算法与策略：**
- [[practice/Algorithm-transition--Amazon-COSMO-vs-Walmart-second-price-auction]] — 平台算法转型对比（亚马逊 COSMO vs 沃尔玛第二竞价）

**账户管理：**
- [[theory/User-roles-and-permissions]] — 用户角色和权限
- [[theory/Account-access-as-a-non-admin-user]] — 非管理员访问管理
- [[theory/Open-a-case-with-Advertiser-Help]] — 联系广告主支持

**Academy 与认证：**
- [[theory/Walmart-Connect-Academy-Ad-Certification]] — Ad Certification 认证
- [[theory/Self-registration-to-Walmart-Connect-Academy]] — Academy 自助注册

**账单与发票：**
- [[theory/Marketplace-sellers-Billing-Policy]] — Marketplace 卖家账单政策
- [[theory/Billing-dispute]] — 账单争议
- [[theory/Invoice-tracking]] — 发票追踪
- [[theory/Invoice-request]] — 发票申请
- [[theory/Walmart-Connect-Product-Terms]] — 产品条款
- [[theory/Invalid-traffic-filtration]] — 无效流量过滤

### Catalog Management（目录管理）

**子分类概述：**
- [[theory/Catalog_management--Overview]] — 目录管理总览
- [[theory/Catalog_management--Item_management]] — 商品管理（增删改查、批量操作）
- [[theory/Catalog_management--Price_management]] — 价格管理（定价规则、调价、Buy Box）
- [[theory/Catalog_management--Reporting]] — 报告（Buy Box/商品/促销/消费者洞察）
- [[theory/Catalog_management--Seller-fulfilled_inventory_management]] — 自配送库存管理
- [[theory/Catalog_management--Troubleshooting]] — 目录管理故障排查

**目录管理页面：**
- [[theory/Product-detail-page_-the-buy-box]] — Buy Box 机制
- [[theory/Generate-a-buy-box-report]] — 生成 Buy Box 报告（待补充）
- [[theory/Pricing-rules]] — 定价规则
- [[theory/Repricer_-overview]] — 智能调价概述
- [[theory/Repricer_-Create-a-strategy]] — 创建调价策略（待补充）
- [[theory/Repricer_-Manage-a-strategy]] — 管理调价策略（待补充）
- [[theory/pricing-insights-overview]] — 价格洞察概览（待补充）
- [[theory/Update-price-individually-in-Seller-Center]] — 单品调价（待补充）
- [[theory/Update-price-in-bulk-in-Seller-Center]] — 批量调价（待补充）

### Getting Started（新卖家入门）

**子分类概述：**
- [[theory/Getting_started--Overview]] — 新卖家入门总览
- [[theory/Getting_started--Walmart_Fulfillment_Services__WFS_]] — WFS 入门子分类
- [[theory/Getting_started--Seller_Forum]] — 卖家论坛使用指南
- [[Getting_started--Advertising]] — 广告解决方案入门（新增）

**WFS 入驻子页面：**
- [[theory/Walmart_Fulfillment_Services__WFS_]] — WFS 仓储配送总览
- [[theory/Getting_started_with_WFS]] — WFS 入门指南
- [[theory/Getting_started_with_WFS--API-calls-for-WFS]] — API 集成 WFS
- [[theory/Getting_started_with_WFS--WFS-international-sellers]] — 国际卖家使用 WFS
- [[theory/Getting_started_with_WFS--WFS-settings-billing-information]] — 账单信息设置
- [[theory/Getting_started_with_WFS--WFS-settings-contact-information]] — 账户联系人设置
- [[theory/Getting_started_with_WFS--WFS-settings-return-rules]] — 退货规则设置
- [[theory/WFS-seller-onboarding-setup]] — WFS 入驻全流程
- [[theory/Shipping_to_WFS]] — 送仓全流程
- [[theory/Walmart_Cross_Border_-_Imports]] — 跨境进口（FCL/LCL）

**运营工作流：**
- [[practice/Operations-SOP--Daily-and-Weekly-Tasks]] — 日常运营 SOP（日/周工作清单）

### Growth（增长机会）

**子分类概述：**
- [[theory/Growth_opportunities--Overview]] — 增长机会总览
- [[theory/Growth_opportunities--Success_Hub]] — 成功中心
- [[theory/Growth_opportunities--Reviews]] — 评论管理（加速器、同步、回复）
- [[theory/Growth_opportunities--Assortment_Growth]] — 商品组合增长
- [[theory/Growth_opportunities--Financing_options]] — 融资选项（Walmart Marketplace Capital）
- [[theory/Growth_opportunities--Listing_Quality]] — Listing 质量优化
- [[theory/Growth_opportunities--Pricing]] — 定价激励（推荐费减免/Walmart 资助激励）
- [[theory/Growth_opportunities--Promotions]] — 促销定价
- [[theory/Growth_opportunities--Pro_Seller]] — Pro Seller 计划
- [[theory/Growth_opportunities--Search_Insights]] — 搜索洞察
- [[theory/Growth_opportunities--Voice_of_Seller]] — 卖家之声
- [[theory/Growth_opportunities--Walmart_Business]] — Walmart Business

**评论与激励页面：**
- [[theory/Success-Hub-Overview]] — 成功中心概述
- [[theory/Success-Hub_-match-buy-box-price]] — 匹配黄金购物车价格（待补充）
- [[theory/Success-Hub_-match-external-price]] — 匹配外部价格（待补充）
- [[theory/Success-Hub_-Automate-pricing-with-the-Repricer]] — Repricer 联动（待补充）
- [[theory/Success-Hub_-Add-trending-items]] — 添加趋势品（待补充）
- [[theory/Success-Hub_-Fulfill-with-Walmart]] — WFS 履约引导（待补充）
- [[theory/Success-Hub_-restock-your-seller-fulfilled-inventory]] — 补货建议
- [[theory/review-accelerator-overview]] — 评论加速器概述
- [[theory/Marketplace-reviews_-overview]] — 评论政策总览
- [[theory/marketplace-reviews-respond-to-reviews]] — 公开回复客户评价
- [[theory/Marketplace-reviews_-review-syndication]] — 评论同步
- [[theory/recognized-reviewer-program-how-to-enroll-items]] — Recognized Reviewer 注册
- [[theory/Review-Accelerator-Program_-How-to-enroll]] — Review Accelerator 注册

**Listing 优化页面：**
- [[theory/Listingquality-and-rewards-dashboard]] — Listing 质量与奖励仪表盘
- [[theory/listingquality-fix-issues]] — 修复 Listing 质量问题
- [[theory/Bulk-attribute-editor]] — 批量属性编辑器
- [[theory/Report-incorrect-product-type]] — 报告错误的产品类型

**促销定价页面：**
- [[theory/Promotional-pricing_-Overview]] — 促销定价概述
- [[promotional-pricing set-up-via-the-promotions-dashboard]] — 促销仪表盘设置
- [[theory/price-incentives-overview]] — 价格激励概述
- [[theory/Comparison-Price-rules]] — 比较价格规则
- [[theory/reduced-referral-fee-incentives-manage-item-enrollment]] — 推荐费减免管理
- [[theory/walmart-funded-incentives-manage-item-enrollment]] — Walmart 资助激励管理
- [[theory/walmart-funded-program-enrollment]] — Walmart 资助计划注册

**Pro Seller 页面：**
- [[theory/pro-seller-overview]] — Pro Seller 概述
- [[theory/Pro-Seller_-Pro-listing-savings]] — Pro Listing 节省

### Item Setup（商品设置）

**子分类概述：**
- [[theory/Item_setup--Overview]] — 商品设置总览
- [[theory/Item_setup--Item_setup_methods]] — 上架方式（Full Setup / Match / Import）
- [[theory/Item_setup--Automotive_fitment]] — 汽车配件适配子分类
- [[theory/Item_setup--Item_content,_imagery,_and_media]] — 商品内容、图片和媒体
- [[theory/Item_setup--Resold]] — 转售商品
- [[theory/Item_setup--Troubleshooting]] — 商品设置故障排查
- [[theory/Item_setup--Variant_management]] — 变体管理

**上架方式页面：**
- [[theory/Add-a-new-item_-Search-the-Walmart-catalog]] — 搜索 Walmart 目录匹配
- [[theory/Add-items-in-bulk_-full-setup]] — 批量完整设置
- [[theory/Add-items-in-bulk_-Set-up-items-by-match]] — 按匹配设置
- [[theory/Add-items-in-bulk_-Upload-a-spreadsheet]] — 上传电子表格批量设置
- [[theory/add-multiple-items-import-your-supplier-catalog]] — 导入其他平台商品目录
- [[theory/add-multiple-items-import-your-catalog]] — 从外部市场导入商品目录（Import items 工具，Versori 集成）
- [[theory/Add-a-New-Item_-Create-a-new-item]] — 创建新商品

**内容与图片页面：**
- [[theory/Product-Detail-Page_-overview]] — 商品详情页政策
- [[theory/Product-detail-page_-Image-guidelines-&-requirements]] — 图片指南与要求
- [[theory/Product-detail-page_-Item-attribution-&-categorization]] — 属性与分类
- [[theory/Product-detail-page_-Keyword-optimization]] — 关键词优化
- [[theory/Product-detail-page_-rich-media]] — 富媒体

**其他页面：**
- [[theory/Product-variant-groups_-Overview]] — 商品变体组
- [[theory/Item-condition-types]] — 商品状况类型（New / Open Box / Certified Refurbished / Used 各级别）
- [[theory/automotive-fitment-overview]] — 汽车配件适配概述
- [[theory/Automotive-Fitment_-Add-missing-attributes-and-ACES-coverage]] — 添加缺失属性和 ACES 覆盖
- [[theory/manage-duplicate-listings-in-seller-center]] — 管理重复商品
- [[theory/duplicate-listings-policy]] — 重复商品政策
- [[theory/request-a-gtin-exemption]] — 申请 GTIN 豁免
- [[theory/Choose-a-product-identifier]] — 商品识别符政策（GTIN/UPC/ISBN/EAN）
- [[theory/GS1-Database-and-Product-ID-Validation]] — GS1 数据库验证与商品 ID 交叉核验
- [[theory/Troubleshoot-item-setup-errors]] — 商品设置错误排查
- [[theory/Troubleshoot-product-ID-errors]] — 商品 ID 错误排查
- [[theory/resold-program-item-setup]] — 转售商品设置

### Order Management（订单管理）

**子分类概述：**
- [[theory/Order_management--Overview]] — 订单管理总览
- [[theory/Order_management--Order_status]] — 订单状态处理子分类
- [[theory/Order_management--Customer_care]] — 客服处理子分类
- [[theory/Order_management--Returns_&_refunds]] — 退货退款子分类
- [[theory/Order_management--Troubleshooting]] — 故障排查子分类

**订单状态页面：**
- [[theory/Cancel-an-order-in-Seller-Center]] — 取消订单
- [[theory/Acknowledge-orders-in-Seller-Center]] — 确认订单
- [[theory/Pause-sales-&-order-operations]] — 暂停销售
- [[theory/Split-customer-orders-in-Seller-Center]] — 拆分客户订单
- [[theory/Update-tracking-numbers-in-Seller-Center]] — 更新追踪号

**客服页面：**
- [[theory/Customer-Care-policy]] — 客服政策
- [[theory/Respond-to-customer-messages-in-Seller-Center]] — 回复客户消息
- [[theory/Create-a-new-customer-email-template]] — 创建客户邮件模板

**退货退款页面：**
- [[theory/returns-policy]] — 退货政策
- [[theory/Issue-a-standard-refund-in-Seller-Center]] — 标准退款
- [[theory/Issue-adjustments-or-non-standard-refunds-in-Seller-Center]] — 非标准退款/超额退款
- [[theory/Add-a-Keep-It-Rule]] — Keep It 规则
- [[theory/add-replacement-rules]] — Replacement 替换规则
- [[theory/Create-item-level-return-rules]] — 商品级退货规则
- [[theory/Request-a-return-policy-exemption]] — 退货政策豁免申请
- [[theory/returns-insights-overview]] — 退货洞察报告
- [[theory/Update-seller-fulfilled-return-center-settings]] — 退货中心设置
- [[theory/Update-seller-fulfilled-return-label-settings]] — 退货标签设置

**故障排查页面：**
- [[theory/Cancel-fraudulent-orders]] — 取消欺诈订单
- [[theory/Troubleshoot-lost-or-undelivered-orders]] — 排查丢失/未送达订单
- [[theory/Troubleshoot-post-transaction-order-errors_-Incorrect-orders]] — 排查错误订单
- [[theory/Troubleshoot-post-transaction-order-errors_-Mispriced-items]] — 排查错误定价
- [[theory/troubleshoot-a-customer-return]] — 排查客户退货
- [[theory/Dispute-a-failed-delivery-return-refund]] — 争议失败的配送退货退款
- [[theory/Dispute-a-Walmart-Customer-Care-refund]] — 争议 Walmart 客服退款

### Policies & Standards（政策标准）

**子分类概述：**
- [[theory/Policies_&_standards--Overview]] — 政策与标准子分类索引
- [[theory/Policies_&_standards--Account]] — 账户政策总览
- [[theory/Policies_&_standards--Orders_&_returns]] — 订单与退货政策
- [[theory/Policies_&_standards--Performance]] — 绩效标准
- [[theory/Policies_&_standards--Product_listings]] — 产品列表政策
- [[theory/Policies_&_standards--Shipping_&_fulfillment]] — 配送与履约政策
- [[theory/Policies_&_standards--Troubleshooting]] — 政策故障排查

**绩效标准页面：**
- [[theory/Seller-Performance-Metrics--Overview]] — 绩效指标综合概览（OTD/VTR/ODR/TRTR）
- [[theory/Seller-performance-standards]] — 卖家绩效标准
- [[theory/negative-feedback-rate-overview]] — 负面反馈率概述
- [[theory/Performance-alarms]] — 绩效警报
- [[theory/performance-dashboard-item-not-received-rate]] — 未收到率仪表盘
- [[theory/performance-dashboard-return-rate]] — 退货率仪表盘
- [[theory/Order-&-fulfillment-performance_-carrier-performance]] — 承运商绩效
- [[theory/Order-&-fulfillment-performance_-regional-performance]] — 区域绩效

**政策页面：**
- [[theory/Walmart-Marketplace-seller-retailer-policies]] — 卖家与零售商政策索引（待补充）
- [[theory/Prohibited-products-policy_-overview]] — 禁售商品政策
- [[theory/Seller-suspension-and-termination]] — 账户暂停与终止
- [[theory/seller-forum-policy]] — 卖家论坛政策
- [[theory/seller-forum-overview]] — 卖家论坛使用指南

**争议与退款政策页面：**
- [[theory/Troubleshooting--Appeal-a-dispute-decision]] — 争议裁定申诉
- [[theory/Credit-Card-Chargeback-policy]] — 信用卡拒付政策
- [[theory/Dispute-standards]] — 争议标准
- [[theory/Returns-Shipping-Service-RSS-policy]] — RSS 退货运输政策
- [[theory/Tax-collection-and-remittance-policy-addendum]] — 税务代缴政策附录
- [[theory/no-haggling-policy]] — 禁止议价政策

**配送政策页面：**
- [[theory/Shipping-and-fulfillment-policy]] — 配送与履约政策

### Seller Fulfillment（卖家配送）

**子分类概述：**
- [[theory/Seller_Fulfillment_Services--Overview]] — 卖家自配送总览
- [[theory/Seller_Fulfillment_Services]] — 卖家配送服务总览
- [[theory/Seller_Fulfillment_Services--Fulfillment_settings]] — 履约设置子分类
- [[theory/Seller_Fulfillment_Services--Ship_with_Walmart]] — Ship with Walmart 子分类
- [[theory/Seller_Fulfillment_Services--Shipping_Templates]] — 配送模板子分类
- [[theory/Seller_Fulfillment_Services--Shipping_methods]] — 配送方式子分类

**履约设置页面：**
- [[theory/Fulfillment-methods_-overview]] — 配送方式概述
- [[theory/simplified-shipping-settings-overview]] — 简化配送设置
- [[theory/Update-fulfillment-lag-time-in-Seller-Center]] — 更新配送延迟时间
- [[theory/Submit-a-lag-time-exemption-request]] — 延迟时间豁免申请
- [[theory/Fulfillment-Center-operating-schedule]] — 履约中心运营时间
- [[theory/weekend-delivery-settings]] — 周末配送设置
- [[theory/add-a-partner-fulfillment-center-in-seller-center]] — 添加合作伙伴履约中心
- [[theory/add-a-seller-managed-fulfillment-center-in-seller-center]] — 添加卖家管理履约中心

**配送模板页面：**
- [[Shipping-templates_-Overview]] — 配送模板概述
- [[theory/Shipping-templates_-add-settings-manually]] — 手动添加设置
- [[theory/Shipping-templates_-Assign-SKUs]] — 分配 SKU
- [[theory/Shipping-templates_-manage-settings]] — 管理设置

**配送方式页面：**
- [[theory/Shipping-methods_-Overview]] — 配送方式概述
- [[theory/Shipping-methods_-expedited-delivery-programs]] — 快递配送计划
- [[theory/Shipping-methods_-freight-shipping-carriers]] — 货运承运商
- [[theory/Shipping-methods_-parcel-shipping-carriers]] — 包裹承运商
- [[theory/Retrieve-credentials-for-your-return-shipping-carrier-account]] — 获取退货承运商凭证
- [[theory/walmart-badge-program-overview]] — Walmart 徽章计划概述
- [[theory/walmart-badge-enroll-your-items]] — 注册 Walmart 徽章商品

**Ship with Walmart 页面：**
- [[theory/Ship-with-Walmart-Overview]] — Ship with Walmart 概述
- [[theory/ship-with-walmart-seller-protections-policy]] — 卖家保护政策
- [[theory/buy-shipping-labels-in-seller-center]] — 购买配送标签

### Taxes & Payments（税务与支付）

**子分类概述：**
- [[theory/Taxes_&_payments--Overview]] — 税务与支付子分类索引
- [[theory/Taxes_&_payments]] — 税务与支付总览
- [[theory/Taxes_&_payments--Billing_Information]] — 账单信息子分类
- [[theory/Taxes_&_payments--Payments]] — 支付子分类
- [[theory/Taxes_&_payments--Settings]] — 设置子分类
- [[theory/Taxes_&_payments--Troubleshooting]] — 支付故障排查
- [[theory/Tax_information]] — 税务信息总览

**收款与结算页面：**
- [[theory/Payment-processing]] — 付款处理与结算
- [[theory/new-seller-payment-hold-policy]] — 新卖家付款冻结政策
- [[theory/Payment-activities]] — 支付活动
- [[theory/Payment-statements-and-transactions]] — 支付报表与交易
- [[theory/final-settlement-payout-policy]] — 最终结算支付政策
- [[theory/get-paid-early-request-a-one-time-transfer]] — 提前收款（一次性转账）

**账单支付页面：**
- [[theory/billing-methods-add-an-ach-u-s-bank]] — 添加 ACH 银行账户
- [[theory/Billing-Methods_-Add-a-credit-card]] — 添加信用卡
- [[theory/billing-methods-set-up-a-paypal-account]] — 设置 PayPal 账户
- [[theory/set-up-payment-information-in-seller-center]] — 设置收款信息
- [[theory/Invoice-tracking-for-Walmart-suppliers]] — 供应商发票追踪（待补充）

**税务信息页面：**
- [[theory/Sales-tax-collection]] — 销售税代收代缴（含 46 个州完整列表）
- [[theory/Product-fees-&-tax-collection]] — 商品费用与税务
- [[theory/Product-tax-codes-for-shipping-fees]] — 运费产品税码
- [[theory/Tax-classifications-and-documentation]] — 税务分类与文档
- [[theory/Update-tax-information-in-Seller-Center]] — 更新税务信息
- [[theory/Retrieve-form-1099-K]] — 获取 1099-K 表格

### WFS（Walmart 配送服务）

**子分类概述：**
- [[theory/walmart-fulfillment-services-wfs-overview]] — WFS 服务概述
- [[theory/WFS_basics]] — WFS 基础（路由指南、退货政策）
- [[theory/Getting_started_with_WFS]] — WFS 入门指南
- [[theory/WFS_item_setup]] — WFS 商品设置子分类
- [[theory/Shipping_to_WFS]] — 送仓全流程子分类
- [[theory/WFS_Inventory_management]] — WFS 库存管理子分类
- [[theory/WFS_reports]] — WFS 报告子分类
- [[theory/WFS_growth_opportunities]] — WFS 增长工具
- [[theory/WFS_programs_&_services]] — WFS 附加服务
- [[theory/WFS_policies_&_standards]] — WFS 政策与标准
- [[theory/WFS_Troubleshooting]] — WFS 故障排查
- [[theory/Walmart_Multichannel_Solutions]] — WFS 多渠道解决方案
- [[theory/Walmart_Cross_Border_-_Imports]] — 跨境进口

**WFS 核心页面：**
- [[theory/WFS-fees]] — WFS 费用详解（履约/仓储/Prep/退货）
- [[theory/WFS-fees-calculator]] — WFS 费用计算器
- [[theory/manage-wfs-inventory]] — 管理 WFS 库存
- [[theory/wfs-reports-inventory-health]] — WFS 库存健康报告
- [[theory/move-aged-inventory]] — 清理老化库存
- [[theory/wfs-returns-overview]] — WFS 退货处理
- [[theory/Select-items-for-WFS]] — 选品加入 WFS

**WFS 报告页面：**
- [[theory/WFS_reports]] — WFS 报告（GMV/入库/退货/结算等）

**WFS 政策页面：**
- [[theory/wfs-prohibited-products-policy]] — WFS 禁售商品
- [[theory/WFS-hazardous-materials-overview]] — WFS 危险品概述
- [[theory/Shipping-and-fulfillment-policy]] — 配送与履约政策

**WFS 附加服务页面：**
- [[theory/WFS-prep-services]] — WFS Prep 服务
- [[theory/Walmart_Multichannel_Solutions]] — 多渠道配送

**WFS 故障排查页面：**
- [[theory/Troubleshoot-WFS-inbound-order-issues]] — WFS 入库问题排查
- [[theory/WFS_Troubleshooting]] — WFS 故障排查总览

---

## 导航地图

```
新卖家入门 (Getting Started)
    ├─ 账户合规 → [[theory/Policies_&_standards--Account]]
    ├─ WFS 开通 → [[theory/Getting_started--Walmart_Fulfillment_Services__WFS_]]
    └─ 商品上架 → [[theory/Item_setup]]

商品上架 (Item Setup)
    ├─ 选择识别符 → [[theory/Choose-a-product-identifier]]
    ├─ 商品状况 → [[theory/Item-condition-types]]
    ├─ 变体管理 → [[theory/Product-variant-groups_-Overview]]
    └─ 错误排查 → [[theory/Troubleshoot-item-setup-errors]]

配送履约 (Fulfillment)
    ├─ 卖家自配送 → [[theory/Seller_Fulfillment_Services]]
    └─ WFS 仓储配送 → [[theory/Walmart_Fulfillment_Services__WFS_]]

订单管理 (Order Management)
    ├─ 订单状态 → [[theory/Order_management--Order_status]]
    ├─ 退货退款 → [[theory/Order_management--Returns_&_refunds]]
    └─ 问题排查 → [[theory/Order_management--Troubleshooting]]

财务 (Taxes & Payments)
    ├─ 收款设置 → [[theory/Payment-processing]]
    ├─ 结算政策 → [[theory/final-settlement-payout-policy]]
    └─ 税务 → [[theory/Tax_information]]

增长 (Growth)
    ├─ 评论管理 → [[theory/Growth_opportunities--Reviews]]
    ├─ 成功中心 → [[theory/Success-Hub-Overview]]
    └─ 广告 → [[theory/Advertising]]

政策 (Policies)
    ├─ 账户政策 → [[theory/Policies_&_standards--Account]]
    ├─ 绩效标准 → [[theory/Policies_&_standards--Performance]]
    ├─ 禁售商品 → [[theory/Prohibited-products-policy_-overview]]
    └─ 申诉流程 → [[theory/Troubleshooting--Appeal-a-dispute-decision]]
```

---

## 治理机制

### 页面元数据（Frontmatter 规范）

每一条方法论都必须包含审核元数据，确保有据可查：

```yaml
---
author: [提交人姓名]
auditor: [审核人姓名/未审核]
status: pending | verified | deprecated | rejected
audit_date: YYYY-MM-DD
tags: [tag1, tag2]
---
```

- **status 流转**：`pending` → `verified` → 或 `deprecated` / `rejected`
- **audit_date**：首次通过审核的日期（用于追踪政策变更历史）
- **author**：content 的创作者（用于追责和沟通）
- **auditor**：最近一次审核的执行人

### 审核流程

1. **引入（Agent 操作）**：Agent 将 raw/ 非官方资料转化为 Markdown，自动存入 `wiki/pending/`，设置 `status: pending`
2. **初审（你的操作）**：检查 pending/ 内容，对比与 practice/ 现有内容，标记冲突
3. **通过（你的操作）**：更新 Frontmatter（`auditor`、`audit_date`、`status: verified`），物理移动至 practice/
4. **拒绝（你的操作）**：在 Frontmatter 加入拒绝原因，移至 archive/，保持 `status: rejected`

### 自动合规检查

运行 `wiki-lint` 脚本检查：
- ✅ wiki/theory/ 是否被非管理员修改（越权检查）
- ✅ wiki/pending/ 中是否有超过 7 天未审核的页面（滞留检查）
- ✅ wiki/theory/ 页面是否非法引用 wiki/pending/（引用合法性）

## 关于本知识库

本知识库按 LLM Wiki 规范维护：
- **源文件**：`raw/`（Immutable，不可修改）
- **Wiki 页面**：`wiki/`（分层治理维护）
- **日志**：`wiki/log.md`（增量记录）
- **交叉链接**：所有页面使用 `[[双向链接]]` 格式互联

每次 ingest 操作后，自动更新本 index.md 和 `wiki/log.md`。

当前统计：
- Wiki 页面总数：**332 个**
- 系统页面：**2 个**（index.md、log.md）
- 知识页面：**330 个**
- 待审页面：**0 个**
