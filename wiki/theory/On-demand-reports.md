# 按需报告

> 10 种可下载的按需报告，用于分析活动表现和导出数据。

## 报告类型总览

| 报告名称 | 说明 | 适用活动类型 |
|----------|------|--------------|
| **Keyword Recommendations** | 手动活动每日更新的关键词建议 | Sponsored Products（手动） |
| **Item Recommendations** | 识别可能表现良好的未推广商品（每周更新） | Sponsored Products |
| **Keyword Performance** | 按出价关键词的活动和广告组表现 | 手动出价活动 |
| **Placement Performance** | 按展示位置的活动和广告组表现 | 所有 Sponsored Search |
| **Item Keyword Performance** | 搜索 In-grid 关键词与商品 ID 对的表现 | Sponsored Products |
| **Item Performance** | 活动和广告组商品级表现 | 所有 Sponsored Search |
| **Search Term Impression Share** | 搜索词的展示份额和排名洞察 | Sponsored Products |
| **Attributed Purchases** | 归因于 Sponsored Search 的购买商品洞察 | 所有 Sponsored Search |
| **History Logs** | 90 天账户访问和活动变更记录 | 所有 Sponsored Search |
| **Campaign Snapshot** | 批量导出活动结构（JSON 格式） | 所有 Sponsored Search |

## 请求报告

1. 导航到 **Reports → On-demand**
2. 点击 **Request Report**
3. 选择报告类型
4. 选择归因窗口（3 天 / 14 天 / 30 天）
5. 选择分组方式（累积或每日）
6. 选择报告时间段
7. 点击 **Request Report**

报告生成最多需要 30 分钟。报告在 3 天后过期。

## 报告详情

### Keyword Recommendations（仅手动 Sponsored Products）

- 活动启动 3 天后可用
- 每日更新
- 识别潜在关键词以增强商品可见性

### Item Recommendations

- 每周三下午更新（数据截至前一天）
- 可按品牌、类别和部门筛选
- 建议每周审查

### Keyword / Item Keyword Performance

- 仅显示点击数 > 0 的关键词的展示数据
- 如果搜索词是字母或数字则为搜索页展示
- 如果是数字则是商品页展示（URL: `walmart.com/ip/ITEMID`）
- 如果是下划线分隔的数字则是浏览页展示

### Placement Performance

| 展示位置 | 自动活动 | 手动活动 |
|----------|----------|----------|
| Search In-grid | ✓ | ✓ |
| Browse In-grid | ✓ | — |
| Search Carousel | ✓ | ✓* |
| Browse Carousel | ✓ | — |
| Item Carousel | ✓ | ✓* |
| Buy Box | ✓ | ✓* |
| Home Page | ✓ | — |
| StockUp | ✓ | — |

*仅当启用时

### Item Performance

- 提供配送类型（Shipping / Curbside pickup and delivery）的归因销售数据
- Marketplace 卖家可按 SKU ID 比较商品表现

### Campaign Snapshot

- JSON 格式导出活动结构
- 每天限制请求 1 次
- 用于活动迁移（API Partner 间）

### History Logs

- **Access History**：90 天用户和 API 合作伙伴访问记录
- **Campaign History**：90 天所有级别的变更记录（活动/广告组/商品/关键词/出价倍数/展示位置/SBA 档案）

### Search Term Impression Share

- 提供搜索词级别的展示份额洞察
- 包含 Top of Search 展示份额和排名
- 每天至少 10 次展示的搜索词优先
- 每天最多 330,000 行

### Attributed Purchases

- 3/14/30 天归因窗口
- 按活动、广告组、归因类型、广告商品、销售额、订单、销量和新品牌指标分段
- 仅适用于请求期间 **Orders > 0** 的活动

## 相关页面

- [[theory/Custom-reports]] — 自定义报告
- [[theory/Item-Health-reports]] — 商品健康报告
- [[theory/Keyword-recommendations]] — 关键词推荐
- [[theory/Item-recommendations]] — 商品推荐

---

> 来源：`raw/walmart advertising guide/On-demand reports.md`
