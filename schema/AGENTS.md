# Walmart Marketplace Wiki - Agent Schema

> 本文件是 LLM Wiki 知识库的**核心配置文档**，定义了 wiki 的结构规范、工作流程和编辑约定。
>
> **目的**：确保 AI Agent 能够系统化地维护这个 Walmart 卖家运营知识库，保持跨页面的一致性和可发现性。
>
> **适用对象**：Claude Code、Cursor、OpenAI Codex 等 LLM Agent

---

## 核心原则：知识与方法论解耦 (Decoupling Principle)

本知识库的最高设计原则。所有工作流必须遵守。

### 1. 双层知识架构

| 层级 | 目录 | 来源 | 内容性质 |
|------|------|------|----------|
| **基础知识 (Theory)** | `wiki/theory/` | `raw/walmart guide/`、`raw/walmart advertising guide/` | 官方文档编译，纯陈述句，工具性 |
| **运营方法论 (Practice)** | `wiki/practice/` | `raw/note/`、`raw/Product Research/` | 实战经验，重点"如何操作"、"策略选择"、"效果验证" |

### 2. 单向引用规则

- `practice` 页面**可以**引用 `theory` 页面（作为理论支撑）。
- **严禁** `theory` 页面引用 `practice` 页面或包含任何"实战建议"。基础知识必须保持纯粹的工具性。

### 3. 编写规范

- **Theory**：语气为陈述句，严禁出现"我建议"、"小技巧"、"避坑指南"等主观表述。
- **Practice**：重点在于"如何操作"、"策略选择"和"效果验证"，允许主观判断和经验总结。

### 4. 嵌入语法强制化

当运营方法论需要复述基础知识时，Agent 必须使用 Obsidian 嵌入语法进行引用，**禁止重写或复制基础定义**：

```markdown
![[theory/PageName#Header]]
```

### 5. 个人心得处理逻辑

- **来源识别**：若源文件来自 `raw/note`，内容**必须**存放在 `wiki/practice/`。
- **双向隔离**：
  - 处理个人心得时，Agent 必须检索 `wiki/theory/` 中相关的基础定义。
  - 使用嵌入语法 `![[theory/page#section]]` 引入基础定义作为背景，下方再书写心得。
  - **禁令**：禁止在处理 `raw/note` 时修改 `wiki/theory/` 下的任何文件。

---

## Wiki 架构概览

```
walmart ZS/
├── raw/                              # 原始资料（只读，不修改）
│   ├── walmart guide/                # Walmart 官方帮助文档 → wiki/theory/
│   ├── walmart advertising guide/    # Walmart Connect 广告指南 → wiki/theory/
│   ├── Product Research/             # 竞品调研数据 → wiki/practice/
│   ├── note/                         # 运营笔记 → wiki/practice/
│   └── assets/                       # PDF、图片等（不可解析，不参与 wiki）
│
├── wiki/                             # LLM 生成的维基页面
│   ├── index.md                      # 分类索引（内容导向）
│   ├── log.md                        # 操作日志（时间导向，append-only）
│   ├── theory/                       # 基础知识层（官方文档编译）
│   │   └── *.md
│   └── practice/                     # 运营方法论层（实战经验）
│       └── *.md
│
└── schema/
    ├── llm-wiki.md                   # LLM Wiki 模式说明
    └── AGENTS.md                     # 本文件，核心配置
```

### 三层架构原则

1. **Raw Sources（原始资料）**：不可变源文档，Agent 只读取不修改
2. **Wiki（维基页面）**：Agent 完全拥有和维护的知识库，分 theory/practice 两层
3. **Schema（本文件）**：配置文档，定义 Agent 的工作方式

---

## Wiki 页面规范

### 命名规范

| 类型 | 命名规则 | 示例 |
|------|----------|------|
| 主题页面 | 使用 `--` 分隔层级 | `Walmart_Connect--Overview.md` |
| 子分类页面 | 上级分类名 + `--` + 具体主题 | `Sponsored_Products--Campaign_setup.md` |
| 操作指南 | 动词开头，清晰动作 | `How-to-update-content_-Overview.md` |
| 概念术语 | 简洁名词短语 | `WFS-fees.md` |

**禁止使用**：
- 中文文件名（会导致链接解析问题）
- 特殊字符（除 `-` 和 `_`）
- 超过 60 字符的文件名
- 空格

### 页面模板

**Theory 页面模板**：

```markdown
# [页面标题]

> [一句话描述：本页面涵盖什么]

## 概述
[简要说明——纯陈述句]

## 核心内容
[详细展开——客观描述，无主观建议]

## 操作步骤
[如适用，步骤列表]

## 注意事项
[官方文档中的关键提醒]

## 相关链接
- [[theory/相关页面1]]
- [[theory/相关页面2]]

---

**来源**：`raw/walmart guide/xxx.md`
**更新日期**：YYYY-MM-DD
```

**Practice 页面模板**：

```markdown
# [页面标题]

> [一句话描述：本页面涵盖什么]

## 核心认知
[基础知识嵌入引用]
![[theory/PageName#Header]]

[基于上述理论的实战解读]

## 策略框架
[如何操作、策略选择]

## 实践案例
[效果验证、数据对比]

## 常见误区
[踩坑经验]

## 相关链接
**基础知识**：
- ![[theory/相关页面1]]

**运营方法论**：
- [[practice/相关页面1]]

---

**来源**：`raw/note/xxx.md`
**创建日期**：YYYY-MM-DD
**更新日期**：YYYY-MM-DD
```

### Frontmatter（可选）

对于重要页面，可在顶部添加 YAML frontmatter：

```markdown
---
title: 页面标题
category: Advertising
layer: theory          # theory 或 practice
source: raw/xxx.md
tags: [advertising, overview]
created: 2026-04-13
updated: 2026-04-25
---
```

---

## Ingest 工作流

### 标准 Ingest 流程

当添加新原始资料时，Agent 必须执行以下步骤：

#### 1. 阅读源文件
- 完整阅读原始 markdown 或其他格式文档
- 提取关键信息：定义、步骤、政策、限制

#### 2. 创建/更新 Wiki 页面
- **新建页面**：根据源文件创建对应的 wiki 页面
- **更新现有页面**：如果源文件补充了已有页面的内容，追加或更新相关章节
- **合并内容**：多个相关源文件合并到同一页面

#### 3. 自动分类到 theory 或 practice

**来源识别（优先）**：

| 来源目录 | 目标目录 | 说明 |
|----------|----------|------|
| `raw/walmart guide/` | `wiki/theory/` | 官方帮助文档 |
| `raw/walmart advertising guide/` | `wiki/theory/` | 官方广告指南 |
| `raw/note/` | `wiki/practice/` | 运营笔记 |
| `raw/Product Research/` | `wiki/practice/` | 竞品调研 |

**文件名判断（备选）**：
- Practice 关键词：`methodology`、`sop`、`strategy`、`analysis`、`optimization`、`diagnostics`、`recovery`、`cold-start`、`case-study`
- Theory 关键词：`overview`、`guide`、`setup`、`campaign`、`policy`、`standard`

#### 4. 更新分类索引 (index.md)
- 在 index.md 中添加新页面的链接和说明
- 保持分类结构完整
- 区分 theory 和 practice 部分

#### 5. 建立交叉引用
- **Practice 页面**：使用嵌入语法 `![[theory/PageName#Header]]` 引用 theory 页面
- **Theory 页面**：禁止引用 practice 页面（保持知识纯度）
- 在相关页面中添加指向新页面的链接

#### 6. 更新操作日志 (log.md)
- 在 log.md 顶部添加新条目
- 格式：`## [YYYY-MM-DD] ingest | [源文件/主题]`
- 记录：创建的页面、更新的页面、关键发现、分类结果（theory/practice）

### Ingest 优先级

1. **高**：Walmart 官方帮助文档更新
2. **中**：广告指南、政策变更
3. **低**：运营笔记、竞品调研（可批量处理）

---

## Query 工作流

### 回答问题

1. **定位相关页面**：先读 index.md 找到相关分类
2. **阅读并综合**：读取 theory 和 practice 页面，提取答案
3. **引用来源**：使用 `[[theory/页面名]]` 或 `[[practice/页面名]]` 链接引用
4. **可写回 Wiki**：有价值的新发现可创建新 practice 页面

### 答案格式选择

| 问题类型 | 推荐格式 |
|----------|----------|
| 定义/概念 | Wiki 页面 |
| 对比分析 | 表格或比较页面 |
| 操作指南 | 步骤列表 + 截图说明 |
| 数据分析 | 图表（matplotlib） |
| 演示汇报 | Marp 幻灯片 |

---

## Lint 工作流

### 定期健康检查

Agent 应定期检查 wiki 健康状况：

#### 检查项目

1. **孤立页面**：未被引用的页面（使用 `find_orphans.py` 脚本）
2. **断裂链接**：`[[不存在]]` 的引用
3. **内容过时**：包含陈旧关键词（`TODO`、`FIXME`、`待更新`、`过时`、`deprecated`、`TBD`、`WIP`）
4. **小文件**：小于 500 字节的页面（可能内容不完整）
5. **超期未更新**：超过 180 天未修改的页面
6. **矛盾内容**：同一主题在不同页面的说法不一致
7. **Theory 页面污染**：检查 `wiki/theory/` 中是否包含主观表述（`我建议`、`小技巧`、`避坑指南`等）
8. **Practice 页面缺失嵌入**：检查 `wiki/practice/` 是否正确使用 `![[theory/...]]` 嵌入引用
9. **分类错误**：检查 theory 目录中是否有 practice 内容，反之亦然

#### 自动化 Lint 脚本

| 脚本 | 功能 |
|------|------|
| `find_orphans.py` | 检测孤儿页面（未被任何页面引用），并检查是否在 index.md 中存在 |
| `wiki_analysis.py` | 综合健康报告：孤立页面 + 陈旧页面（按时间排序）+ JSON 格式输出 |
| `check_ingest_status.py` | 对照 log.md 统计各目录已处理/待处理文件数 |
| `check_status2.py` | 按 raw 子目录分类统计，处理情况与 log.md 对照 |
| `classify_wiki_files.py` | 自动分类 wiki 文件到 theory/practice 目录 |

#### 修复优先级

1. 断裂链接（高优先级）
2. 分类错误（高优先级）
3. Theory 页面污染（高优先级）
4. 孤立页面添加导航
5. 内容过时标注
6. 矛盾内容协调

---

## 跨页引用规范

### 链接语法

```markdown
- Theory 页面间互引：[[theory/页面名]]
- Practice 页面间互引：[[practice/页面名]]
- Practice 引用 Theory：[[theory/页面名]] 或嵌入 ![[theory/页面名#章节]]
- Theory 引用 Practice：❌ 禁止
- 带显示文字：[[theory/页面名|显示文本]]
- 外部链接：[描述](URL)
```

### 引用链设计原则

- **密度适中**：每个页面应有 3-10 个内部链接
- **双向链接**：同层级页面（theory↔theory、practice↔practice）应双向链接
- **单向链接**：跨层级只允许 practice → theory
- **上下文清晰**：链接文本应描述目标页面的内容

---

## 分类体系

### 知识层级分类

| 层级 | 目录 | 页面数 | 说明 |
|------|------|--------|------|
| Theory | `wiki/theory/` | ~318 | 官方文档编译的基础知识 |
| Practice | `wiki/practice/` | ~14 | 运营方法论和实战经验 |

### 业务主题分类（index.md 顶部）

| 分类 | 包含内容 |
|------|----------|
| 基础运营 | Getting started、Catalog management、Item setup |
| 配送履约 | Seller Fulfillment Services、WFS |
| 财务与增长 | Taxes & Payments、Growth opportunities、Advertising |
| 订单与政策 | Order management、Policies & standards |

### 页面层级

```
主分类 → 子分类 → 具体页面
   ↓
[[theory/Catalog_management]] → [[theory/Catalog_management--Item_management]]
```

---

## 工具使用

### 搜索

- **文件搜索**：使用 Grep 工具搜索关键词
- **全文搜索**：配合 `wiki_analysis.py` 分析链接关系
- **注意路径**：搜索时需覆盖 `wiki/theory/` 和 `wiki/practice/` 两个目录

### 分析

- 运行 `wiki_analysis.py` 检查孤立页面和陈旧内容
- 运行 `find_orphans.py` 检测孤儿页面并验证 index.md 引用情况
- 运行 `check_ingest_status.py` / `check_status2.py` 追踪 ingest 进度
- 运行 `classify_wiki_files.py` 自动分类未归类文件
- 定期生成健康报告

### Python 脚本规范

所有 Wiki 维护脚本遵循以下约定：

| 约定 | 说明 |
|------|------|
| 文件位置 | 放在 `walmart ZS/` 根目录，与 `wiki/`、`raw/`、`schema/` 同级 |
| 路径格式 | Windows 绝对路径用 raw string（`r"h:\..."`），路径分隔符用 `\\` |
| 输出flush | `print()` 时加 `flush=True`，确保实时输出 |
| 递归搜索 | 使用 `glob.glob(..., recursive=True)` 而非 `os.walk` |
| JSON 输出 | 健康报告末尾输出 JSON 格式结果 |
| 字符编码 | 统一使用 `encoding='utf-8'` |
| 排除文件 | 统一排除 `index.md` 和 `log.md` |
| 目录遍历 | 必须遍历 `wiki/theory/` 和 `wiki/practice/` 两个子目录 |

---

## 日志格式

### log.md 条目格式

```markdown
## [YYYY-MM-DD] [操作类型] | [主题]

### 源文件
`raw/xxx.md`

### 创建/更新的 Wiki 页面
- [[theory/新页面1]] (theory)
- [[practice/新页面2]] (practice)

### 关键发现
- 发现1
- 发现2

### 链接关系
- 新增入链：[[theory/目标页面]]
- 新增出链：[[practice/目标页面]]

### 统计
- Wiki 页面总数：XXX (+Y)
- Theory：XXX
- Practice：XXX
```

### 操作类型

| 类型 | 说明 |
|------|------|
| `ingest` | 摄入新原始资料 |
| `query` | 回答问题 |
| `lint` | 健康检查和修复 |
| `update` | 更新已有内容 |
| `merge` | 合并多个页面 |

---

## 命名冲突处理

### 规则

1. **同主题不同来源**：保留较早的，标注来源差异
2. **同主题内容矛盾**：在页面中并列呈现，标注来源和日期
3. **重复命名**：使用更具体的描述性命名

### 命名建议

- 优先使用 Walmart 官方标题
- 保持与 Walmart Seller Center 导航一致
- 参考 [[theory/Sponsored-Products--Overview]] 等现有页面的命名风格

---

## 质量标准

### 页面质量检查

- [ ] 标题清晰，反映页面核心内容
- [ ] 包含概述或摘要
- [ ] 有实际内容（超过 500 字节）
- [ ] 有相关页面链接（3+ 个）
- [ ] 包含来源引用
- [ ] 链接语法正确（无断裂链接）
- [ ] 不包含陈旧标记关键词
- [ ] **Theory 页面无主观表述**
- [ ] **Practice 页面有嵌入引用**

### 陈旧关键词列表

| 关键词 | 含义 | 处理建议 |
|--------|------|----------|
| `TODO` | 待完成内容 | 补充或删除 |
| `FIXME` | 待修复内容 | 修复或标注 |
| `待更新` | 内容已过时 | 更新或删除 |
| `过时` | 明确标注过时 | 删除或更新 |
| `deprecated` | 已废弃 | 替换为新方案 |
| `TBD` | 待定内容 | 补充或删除 |
| `WIP` | 进行中内容 | 完成后移除 |

### 内容准确性

- 引用 Walmart 官方文档
- 标注信息来源和日期
- 不添加未经证实的推测
- 政策相关内容标注适用范围

---

## 特殊处理

### Excel 数据处理

对于 Excel 调研表（如竞品分析）：
1. 提取关键字段和指标
2. 转换为 wiki 表格格式
3. 创建对比分析页面（存入 `wiki/practice/`）
4. 保留原始数据引用

### 图片处理

- 图片保存到 `raw/assets/` 目录
- Wiki 中引用本地路径
- 重要图片在页面中说明其内容
- `raw/assets/` 目录在脚本中应排除，不参与文件遍历和分析

### Case Study 和邮件规范

**语言要求**：
- **Case Study 主体**：使用中文书写（便于中文卖家理解），存入 `wiki/practice/`
- **邮件模板**：必须使用英文书写（用于直接发送给 Walmart 英文团队）
- **其他内容**：根据上下文选择中文或英文

**Case Study 结构**：
1. 案例编号、问题类型、严重程度（中文）
2. 执行摘要（中文）
3. 问题陈述（中文）
4. 根本原因分析（中文）
5. 诊断步骤（中文）
6. 解决方案框架（中文）
7. **邮件模板**（英文）- 使用 ```code block``` 包裹
8. 后续行动（中文）
9. 相关参考文档（中文）

**邮件模板要求**：
- 使用标准商务英文格式
- 包含 Subject Line、Opening、Product Information、Issue Description、Requested Actions、Supporting Documentation、Closing
- 使用占位符 `[Placeholder]` 便于填写
- 清晰、专业、易于理解
- 避免过度复杂的句式

---

## 持续改进

本 schema 是动态文档，会随项目发展更新。

### 更新触发条件

- 新增重要分类
- 改变页面组织方式
- 引入新工具或工作流
- 发现更好的命名约定
- 开发新的维护脚本（需同步更新工具使用章节）

### 脚本开发约定

- **随用随建**：遇到重复性的人工检查，立即编写脚本固化
- **放根目录**：脚本文件放在 `walmart ZS/` 根目录，与 `wiki/`、`raw/`、`schema/` 同级
- **同步规范**：新脚本开发后，将检查逻辑同步到本 schema 的 Lint 工作流章节
- **最小工具集**：优先使用 Python 标准库，减少外部依赖

### 维护责任

- Agent 在每次 ingest 时考虑 schema 是否需要更新
- 大幅变更需在 log.md 中记录

---

## 响应规范 (Mandatory — Non-Negotiable)

每次执行完 **任意操作**（Ingest、Query、Lint、Update、Merge）后，**必须**在回复末尾追加以下板块，**不得跳过，不得省略，不得合并到正文**。

### 板块格式

```markdown
---
## 维护者追问

1. [具体问题1]
2. [具体问题2]
3. [具体问题3]
```

### 触发规则

| 操作类型                 | 追问方向                              |
| -------------------- | --------------------------------- |
| 刚完成 **ingest**       | 需要建立哪些交叉链接？是否有被覆盖的旧内容需要删除？        |
| 刚完成 **query**        | 是否将结论沉淀为正式 wiki 页面？               |
| 刚完成 **lint**         | 发现了哪些孤儿页面/断裂链接？需要立即修复吗？           |
| 刚完成 **update/merge** | 变更是否需要同步到 index.md？是否有其他页面需要联动更新？ |

### 自我检查清单（每次回复前核对）

- [ ] 回复末尾是否有「维护者追问」板块？
- [ ] 板块是否紧跟在正文之后（中间无其他内容）？
- [ ] 问题是否与本次操作类型匹配（不是泛泛而谈）？
- [ ] 问题是否具体、可回答，而不是套话？

### 违反后果

若未执行「维护者追问」板块，后续所有 Agent 操作将被视为**不完整**，用户有权要求重新执行。

### 语气要求

直接、专业、以结果为导向。不要废话，直接进入维护环节。

---

**最后更新**：2026-04-25
