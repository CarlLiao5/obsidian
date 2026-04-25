# 广告定向政策与数据使用规范

> Walmart Connect 广告定向规则、第三方标签授权、流量政策与个人信息收集要求。

## 广告主命名规范（Naming Conventions）

广告主在平台上自定义命名的字段（如自定义受众、关键词、广告组名称等）**不得包含敏感个人信息或受保护类别的暗示**。

### 可自定义命名的元素

| 类别 | 可命名元素 |
|------|-----------|
| 受众/数据元素 | Custom audiences、Item sets、Custom locations |
| 内容 | Creatives/Creative folders、Campaign names、Tags、Ad groups |
| 其他 | Manual shelf names、Keywords |

### 命名要求

- 必须与所推广的产品和品牌相关
- 易于阅读（禁止符号、emoji、超链接）

### 禁止内容

命名不得引用或暗示以下敏感信息：
- 未满 18 岁的人群
- 种族、民族、国籍、性别认同、残障、退伍军人身份、性取向、宗教
- 敏感健康或基因数据（医疗诊断/状况、治疗、健康状况）
- 个人可识别信息（精确地理位置、生物特征、财务数据）
- 任何个人化、掠夺性、歧视性、攻击性或骚扰性内容

---

## 定向政策（Targeting Policy）

个性化广告允许广告主基于用户过去的在线行为定向，提供更相关的体验。

### 禁止定向行为

Walmart Connect **不允许**以下定向方式：

- 违反命名规范
- 共享或暗示个人隐私或可识别信息
- 针对未成年人
- 针对产品/服务在法律上受限的地区
- 针对 [[theory/Prohibited-content-and-products|Prohibited products]] 的行为
- 创建基于用户历史搜索、浏览、购买行为的敏感兴趣类别定向

### 禁止定向的敏感兴趣类别

| 类别 | 类别 |
|------|------|
| 种族和民族 | 性兴趣和亲密健康 |
| 性别和性别认同 | 特定妊娠相关兴趣 |
| 残障 | 特定婚姻状态 |
| 性取向 | 非法活动 |
| 宗教或信仰体系 | 敏感心理或身体健康数据 |
| 经济困难或脆弱性 | 成瘾 |
| 掠夺性金融行为 | 葬礼和其他死亡相关服务 |
| 移民 | 政治信仰或隶属关系 |
| 受保护阶层 | 工会成员资格 |

---

## 第三方标签政策（Third-party Tags）

> 仅以下列出的第三方供应商标签获批使用。任何未列出的标签均视为**未批准**。

### 已批准站内供应商（Onsite Display）

| 供应商 | 批准格式 | 附加说明 |
|--------|----------|----------|
| DoubleVerify | Image 1×1 像素 或 JavaScript 1×1 像素 | 仅用于监测，不允许屏蔽；JavaScript 格式需用于可看性监测；App 环境不适用 |
| Integral AdScience | Image 1×1 像素 或 JavaScript 1×1 像素 | 同上 |

### 已批准第三方展示供应商

| 供应商 | 批准格式 | 说明 |
|--------|----------|------|
| Campaign Manager (DCM) | Image 1×1 像素 | 仅允许跟踪像素 |

### 已批准CTV/OTT供应商

| 供应商 | 批准格式 | 说明 |
|--------|----------|------|
| Innovid | Video Image 1×1 px | CTV 动态创意优化 |
| Liveramp | Image 1×1 | CTV、上下文定向 |
| Kargo | Image 1×1 | CTV、上下文定向 |
| Kerv | Image 1×1 | CTV 二维码激活 |

### 已批准站外测量合作伙伴

| 供应商 | 批准格式 | 测量类型 |
|--------|----------|----------|
| Adelaide | Image 1×1 | 注意力测量 |
| Crossix | Image 1×1 | Rx 销售提升、品牌力 |
| DISQO | Image 1×1 | 品牌力提升 |
| Foursquare | Image 1×1 | 地理位置提升 |
| iSpot | Image 1×1 | CTV 测量 |
| Nielsen ONE | Image 1×1 | 品牌力、DAR |
| SambaTV | Image 1×1 | ACR、CTV |
| TransUnion Neustar | Image 1×1 | MTA 测量 |
| Upwave | Image 1×1 | 品牌力提升 |

---

## 无效流量政策（Invalid Traffic Policy）

Walmart **严格禁止**无效流量（IVT）。IVT 指由机器人或其他非人类来源生成的流量，用于虚增广告指标。

- Walmart 在建立业务关系前审查广告主和第三方供应商的 IVT 参与情况
- 对 Display 广告，Walmart 额外使用 HUMAN（第三方网络安全公司，MRC 认证）进行 IVT 检测

---

## 个人信息收集要求（Collection of Personal Information）

### 站外落地页的个人信息收集

所有收集个人信息（如邮箱、姓名）的站外广告落地页，**必须包含隐私政策声明**。

从 Walmart 网站重定向时，落地页的视觉和体验必须与 Walmart 有明显区别，并明确告知用户已离开 Walmart。离开 Walmart.com 时必须显示过渡页（Interstitial），内容如：

> "You are now leaving Walmart.com and being directed to an external page"

---

## 相关链接

- [[theory/Data-use---privacy-requirements]] — 数据使用与隐私要求（待创建时链接）
- [[theory/Prohibited-content-and-products]] — 禁止内容与商品
- [[theory/Sponsored-Products--Glossary]] — 广告术语表
- [[theory/Search-Engine-Marketing-_SEM__-program-policy]] — SEM 政策合规

---

> 来源：`raw/walmart advertising guide/Data use & privacy requirements.md`
> 更新：2026-04-17
