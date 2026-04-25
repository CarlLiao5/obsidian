# 价格管理（Price Management）

> 定价规则、智能调价工具、Buy Box 机制与价格报告的完整指南。

## 核心操作流

```
定价规则 → [[theory/Pricing-rules]]（合规要求、哄抬价格禁止）
  ↓
设置价格 → [[theory/Update-price-individually-in-Seller-Center]]（单件）
          [[theory/Update-price-in-bulk-in-Seller-Center]]（批量）
          [[How-to-Update-Price_-Overview]]（概览）
  ↓
智能调价 → [[theory/Repricer_-Create-a-strategy]]（创建策略）
          [[theory/Repricer_-Manage-a-strategy]]（管理策略）
  ↓
Buy Box   → [[theory/Product-detail-page_-the-buy-box]]（Buy Box 机制）
          [[theory/Generate-a-buy-box-report]]（Buy Box 报告）
  ↓
价格洞察 → [[theory/pricing-insights-overview]]（定价洞察）
```

## 定价方法对比

| 方法 | 说明 | 适用场景 |
|------|------|----------|
| 单独更新 | Catalog 页直接修改价格 | 少量商品快速调整 |
| 批量更新 | Price and Promotion 模板 | 大量商品统一调价 |
| API | 程序化批量更新 | 大型目录自动化 |
| Repricer | 基于规则自动调价 | 持续监控竞争价格 |

## 划线价格（Reference Price）刷新

> 运营实践技巧：划线价格（Compare at price / Was price）决定前台折扣展示效果，若划线价格未及时更新，折扣标签会失效，影响点击率。

### 判断划线价格是否需要刷新

当以下信号出现时，说明划线价格已过期或失效：

- 前台折扣标签消失（如 "Save 20%" 不再显示）
- `Competitive Price` 匹配成功但前台无反应
- 历史最低价数据库未同步当前售价

### 刷新方法（3 种方案）

**方法一：Competitive Price 匹配检查（最快）**

1. 进入 Flash Deals 界面，筛选查看是否有匹配到该 SKU
2. 若匹配成功，划线价格会自动更新
3. 若无匹配，进入方法二

**方法二：促销表刷 MSRP（推荐）**

1. 在 Seller Center 下载促销模板
2. 填写 MSRP（Manufacturer's Suggested Retail Price）字段
3. 上传促销表，等待系统同步（通常 30 分钟 - 2 小时）
4. 检查前台划线价格是否更新

**方法三：多次覆盖更新（兜底方案）**

1. 若方法一、二均无效，多次（2-3 次）重复提交当前售价
2. 每次提交间隔 10-15 分钟
3. 让系统强制刷新数据库缓存的划线价格

### 刷新后验证

- 清除浏览器缓存（或使用隐私模式）重新查看商品页面
- 确认划线价格（删除线价格）与实际折扣比例正确显示

### 相关链接

- [[theory/Comparison-Price-rules]] — 比较价规则（90 天最低价计算）
- [[theory/Catalog_management--Price_management]] — 定价管理总览
- [[theory/Growth_opportunities--Promotions]] — 促销工具与激励计划

---

## 关键规则

- 禁止哄抬价格（紧急情况/需求激增时大幅涨价）
- 比较价（Reference Price）须基于过去 90 天的实际最低成交价
- 价格严重偏离（与同站/竞争平台相比）会被**自动下架**，48 小时后可重新上架

## 相关页面

- [[theory/Pricing-rules]] — 定价合规要求
- [[theory/Comparison-Price-rules]] — 比较价规则（Policies 层）
- [[theory/Catalog_management]] — 目录管理总览
- [[theory/Growth_opportunities--Pricing]] — 价格激励计划（Walmart 补贴）

---

> 源文件目录：`raw/Catalog_management--Price_management/`