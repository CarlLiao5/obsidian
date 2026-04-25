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

| 层级                   | 目录               | 来源                                                    | 内容性质                        |
| -------------------- | ---------------- | ----------------------------------------------------- | --------------------------- |
| **基础知识 (Theory)**    | `wiki/theory/`   | `raw/walmart guide/`、`raw/walmart advertising guide/` | 官方文档编译，纯陈述句，工具性             |
| **运营方法论 (Practice)** | `wiki/practice/` | `raw/note/`、`raw/Product Research/`                   | 实战经验，重点"如何操作"、"策略选择"、"效果验证" |

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
│   ├── Product Research/             # 竞品调研数据 → wiki/pending/
│   ├── note/                         # 运营笔记 → wiki/pending/
│   └── assets/                       # PDF、图片等（不可解析，不参与 wiki）
│
├── wiki/                             # LLM 生成的维基页面（分层治理）
│   ├── index.md                      # 分类索引（内容导向）
│   ├── log.md                        # 操作日志（时间导向，append-only）
│   ├── theory/                       # 【核心区】基础知识层（官方文档编译，只读）
│   │   └── *.md
│   ├── practice/                     # 【标准区】运营方法论层（已审核，全员可见）
│   │   └── *.md
│   ├── pending/                      # 【待审区】待审核内容隔离缓冲区
│   │   └── *.md (status: pending)
│   └── archive/                      # 【存档区】已拒绝或过时的内容
│       └── *.md (status: rejected/deprecated)
│
├── scripts/
│   ├── wiki-lint.sh                  # 自动化合规审计脚本
│   └── add-frontmatter.sh            # 批量添加元数据脚本
│
└── schema/
    ├── llm-wiki.md                   # LLM Wiki 模式说明
    └── AGENTS.md                     # 本文件，核心配置
```

### 四层架构原则

1. **Raw Sources（原始资料）**：不可变源文档，Agent 只读取不修改
2. **Wiki（维基页面）**：Agent 完全拥有和维护的知识库，分四层：
   - **Theory**：官方知识（管理员维护，仅读引用）
   - **Practice**：已审核方法论（全员可见）
   - **Pending**：待审核内容（隔离缓冲）
   - **Archive**：已拒绝或过时（参考用）
3. **Schema（本文件 AGENTS.md）**：核心配置文档，定义 Agent 的所有工作方式和权限规则

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

### Frontmatter（必须）

**每个 wiki 页面都必须包含以下 YAML frontmatter**，用于审核追踪和元数据管理：

```markdown
---
author: 创作者名字
auditor: 审核人名字或"未审核"
status: verified | pending | rejected | deprecated
audit_date: YYYY-MM-DD 或 null
tags: [tag1, tag2, tag3]
rejection_reason: 仅当 status=rejected 时填写
---

# 页面标题

页面内容...
```

**字段说明**：

| 字段 | 含义 | 示例 |
|------|------|------|
| `author` | 内容创作者 | 张三、Walmart 官方、Agent |
| `auditor` | 最近审核人（未审核则为 null） | 李四、未审核 |
| `status` | 内容当前状态 | `verified`（已验证）/ `pending`（待审）/ `rejected`（已拒）/ `deprecated`（已弃） |
| `audit_date` | 通过审核的日期（未审核则为 null） | 2026-04-26 或 null |
| `tags` | 内容分类标签 | [广告, 优化, 方法论] |
| `rejection_reason` | 拒绝原因（仅 status=rejected 时填写） | "缺乏数据支撑" |

**状态流转规则**：

```
pending (新摄入)
    ↓
verified (通过审核) → 进入 practice/
    ↓
deprecated (已弃用)
    
rejected (已拒绝) → 进入 archive/
```

**Agent 在摄入时的职责**：
1. Theory 页面：设置 `author: Walmart 官方`, `status: verified`, `audit_date: 今天`
2. Pending 页面：设置 `author: [源文件创建者]`, `status: pending`, `audit_date: null`, `auditor: null`
3. 自动推断适当的 tags（基于内容分类）

---

## 审核与治理工作流（New in v2.0）

### 背景与目标

在原有"知识与方法论解耦"的基础上，新增**审核隔离机制**，确保：
- 未审核的内容不污染标准区（practice/）
- 所有决策有据可查（Frontmatter 元数据）
- 冲突自动检测（避免信息混乱）
- 审核流程可持续（循环迭代）

### 四层隔离架构

```
【核心区】          【标准区】          【待审区】          【存档区】
theory/            practice/          pending/          archive/
(只读)             (全员可见)          (隔离缓冲)         (参考用)

Official           Verified           Pending            Rejected/
Knowledge          Methods            Content           Deprecated

status:            status:            status:            status:
verified           verified           pending            rejected/
(Admin Only)       (After Review)      (New Ingest)      deprecated
```

### Audit Workflow 四步流程

#### Step 1: Ingest（Agent 摄入）

Agent 扫描 raw/ 并按规则路由。详见下方"标准 Ingest 流程"章节的完整步骤。

**快速摄入清单**：
- [ ] 根据来源目录判断目标位置（theory 还是 pending）
- [ ] 添加完整的 Frontmatter（author, status, tags）
- [ ] 对于 pending 内容，检查是否与 practice/ 现有内容冲突
- [ ] 如发现冲突，在页面顶部添加 `> [!warning]` 冲突警告块
- [ ] 更新 wiki/log.md 记录摄入操作
- [ ] Theory 内容禁止引用 Pending（保持知识纯度）

#### Step 2: Review（审核者初审）

审核者打开 wiki/pending/ 页面，执行审核清单（见下方"标准 Ingest 流程"部分）。

**快速审核清单**：
- [ ] 内容质量（清晰性、准确性、可操作性）
- [ ] 与 practice/ 的冲突检测
- [ ] Frontmatter 完整性
- [ ] 链接有效性

**三种可能的结果**：
1. ✅ **通过审核** → Step 3 (Approve)
2. ⚠️ **发现冲突** → Step 2.1 (Resolve Conflicts)
3. ❌ **拒绝审核** → Step 4 (Reject)

#### Step 2.1: Resolve Conflicts（冲突协商）

如发现与 practice/ 现有方法论的矛盾：

```markdown
> [!warning] 内容冲突检测
> 
> 本页与现有方法论存在潜在矛盾：
>
> **冲突 1**：出价策略
> - [[pending/New-Strategy]]: 降价提升转化率
> - [[practice/Existing-Method]]: 保持高价维持品牌
>
> **建议**：编辑 pending 页面，添加适用条件"仅适用于低端商品"
```

**处理流程**：
1. 分析冲突原因（场景差异、数据不足、政策变更）
2. 确定是否可通过编辑修改来协商
3. 与原提交者沟通修改建议
4. 修改后重新审核

#### Step 3: Approve（通过审核）

更新 Frontmatter，移动文件至 practice/：

```yaml
# 前
---
author: 张三
auditor: null
status: pending
audit_date: null
---

# 后
---
author: 张三
auditor: 李四              # ← 填入审核人名字
status: verified          # ← 改为 verified
audit_date: 2026-04-26   # ← 填入审核日期
---
```

**操作步骤**：
```bash
# 1. 更新 Frontmatter
# 2. 移动文件
mv wiki/pending/filename.md wiki/practice/filename.md
# 3. 更新 wiki/index.md（如需添加新分类）
# 4. 更新 wiki/log.md（记录审核操作）
```

#### Step 4: Reject（拒绝审核）

标记拒绝原因，移动文件至 archive/：

```yaml
---
author: 张三
auditor: 李四
status: rejected                  # ← 改为 rejected
audit_date: 2026-04-26
rejection_reason: "缺乏数据支撑" # ← 填写拒绝原因
---
```

**常见拒绝原因**：
- 违反官方政策
- 缺乏数据支撑
- 与现有方法论无法协商的冲突
- 内容过时或已被更新版本替代

**操作步骤**：
```bash
# 1. 更新 Frontmatter
# 2. 移动文件
mv wiki/pending/filename.md wiki/archive/filename.md
# 3. 更新 wiki/log.md（记录拒绝和原因）
# 4. 可选：通知提交者拒绝原因
```

### 冲突检测规则

Agent 在摄入时必须检测 pending 与 practice 的冲突。

**冲突类型**：

| 类型 | 示例 | 处理方式 |
|------|------|----------|
| 事实冲突 | A 说"降价有效"，B 说"降价亏损" | 标记为警告，让审核者判断是否适用于不同场景 |
| 政策冲突 | 建议违反 Walmart 官方政策 | 自动拒绝（policy conflict） |
| 命名冲突 | 同一概念用了不同术语 | 标记为冲突，统一术语 |

**自动警告生成**：

```python
# 伪代码：Agent 应实现此逻辑
if detect_potential_conflict(pending_page, practice_pages):
    add_warning_block(pending_page, conflicts_found)
    log_conflict(pending_page, conflicting_practice_pages)
```

### 引用规则（升级版）

```
Theory  ←→  Theory    ✅ 允许
Theory  ←   Practice  ✅ 允许引用（反向引用）
Theory  →   Practice  ❌ 禁止（保持知识纯度）

Practice ←  Theory    ✅ 允许（主要）
Practice ←  Practice  ✅ 允许
Practice →  Pending   ❌ 禁止（仅引用已验证内容）

Pending  ←  Theory    ✅ 允许
Pending  ←  Practice  ✅ 允许
Pending  →  Pending   ⚠️ 谨慎（审核时需检查双方状态）
```

### 日志维护规范（升级版）

每次操作后，更新 wiki/log.md：

```markdown
## 2026-04-26

| 操作 | 文件 | 操作者 | 备注 |
|------|------|--------|------|
| ingest | pending/New-SOP.md | Agent | 来源：raw/note/ |
| verified | practice/Advertising--Method.md | 李四 | 合并自 pending/ |
| rejected | archive/Old-Strategy.md | 李四 | 原因：违反官方政策 |
```

### 自动化工具

#### 1. wiki-lint.sh（合规检查）

```bash
bash scripts/wiki-lint.sh

# 检查项：
✅ 越权修改检查（谁修改了 theory/）
✅ 滞留检测（pending 中 >7 天的页面）
✅ 非法引用检查（theory 不能引用 pending）
✅ Frontmatter 完整性
```

#### 2. add-frontmatter.sh（元数据添加）

已自动为所有 332 个页面添加 Frontmatter。

---

### 工作流场景示例

#### 场景 1：同事提交运营笔记

```
1️⃣  同事在 raw/note/ 提交：team-feedback.txt
     内容：关于广告优化的新发现

2️⃣  Agent 扫描到新文件，执行 ingest：
     - 转化为 Markdown
     - 添加 Frontmatter（status: pending）
     - 存入 wiki/pending/Advertising--New-Discovery.md
     - 更新 wiki/log.md

3️⃣  你查看 wiki/pending/，发现与 practice/ 中的现有方法论有冲突
     - 在页面顶部添加 > [!warning] 冲突块
     - 与原作者沟通

4️⃣  冲突解决后，你通过审核：
     - 更新 Frontmatter（auditor: 你的名字, status: verified）
     - 移动文件至 wiki/practice/
     - 更新 wiki/index.md 索引
     - 更新 wiki/log.md

5️⃣  wiki-lint 检查通过，合并至主分支
```

#### 场景 2：审核拒绝

```
1️⃣  Agent 摄入内容 → wiki/pending/

2️⃣  你审核发现：
     - 内容与官方政策矛盾
     - 没有充分的数据支撑
     - 过时的信息

3️⃣  执行拒绝流程：
     - 在 Frontmatter 中添加：
       status: rejected
       rejection_reason: "与官方政策相悖，需原作者提供更新的数据支撑"
       auditor: 你的名字
     - 移动至 wiki/archive/
     - 更新 wiki/log.md

4️⃣  Agent 或系统发送通知给原提交者（可选）
```

---

### 权限管理

#### 谁可以做什么？

| 操作 | Agent | 审核者 | 管理员 |
|------|--------|----------|---------|
| 摄入 (ingest) | ✅ | ✅ | ✅ |
| 修改 theory/ | ❌ | ❌ | ✅ |
| 编写 pending/ | ✅ | ✅ | ✅ |
| 审核 & 移动 pending→practice | ❌ | ✅ | ✅ |
| 管理 wiki/log.md | ✅ | ✅ | ✅ |
| 运行 wiki-lint | ✅ | ✅ | ✅ |

---

### 常见问题 (FAQ)

#### Q1: Agent 是否可以直接修改 wiki/practice/ 中的现有页面？

**A**: 仅在以下情况允许：
- 修复明显的语法/拼写错误
- 更新过时的官方政策链接
- 添加内部引用链接

其他实质性修改应由审核者进行，确保知识的一致性。

#### Q2: 如果 pending 页面已经过了 7 天还未审核怎么办？

**A**: 
- wiki-lint 会标记为 ⚠️ 警告
- 审核者应优先处理这些滞留页面
- 如认为不重要，主动标记为 rejected 并存档

#### Q3: 如何处理跨越多个层级的更新？

**A**: 例如官方文档（theory）更新了，需要同步到实践层（practice）：
- 不要直接编辑 practice 页面
- 创建新的 pending 页面，记录同步的变更
- 通过审核流程移至 practice

#### Q4: pending 页面可以相互引用吗？

**A**: 可以，但应谨慎。审核时需检查被引用的 pending 页面是否也会被通过，避免孤立的引用。

---

### 标准 Ingest 流程

当添加新原始资料时，Agent 必须执行以下步骤：

#### 1. 阅读源文件
- 完整阅读原始 markdown 或其他格式文档
- 提取关键信息：定义、步骤、政策、限制

#### 2. 创建/更新 Wiki 页面
- **新建页面**：根据源文件创建对应的 wiki 页面
- **更新现有页面**：如果源文件补充了已有页面的内容，追加或更新相关章节
- **合并内容**：多个相关源文件合并到同一页面

#### 3. 自动分类到 theory/practice/pending

**来源识别与路由规则（核心规则，必须遵守）**：

| 来源目录 | 目标目录 | 状态 | 说明 |
|----------|----------|------|------|
| `raw/walmart guide/` | `wiki/theory/` | verified | 官方帮助文档，直接发布 |
| `raw/walmart advertising guide/` | `wiki/theory/` | verified | 官方广告指南，直接发布 |
| `raw/note/` | `wiki/pending/` | pending | 运营笔记，需人工审核后才能进入 practice |
| `raw/Product Research/` | `wiki/pending/` | pending | 竞品调研，需人工审核后才能进入 practice |

**关键规则**：
- ✅ 官方资料直接进入 theory/（标记 status: verified）
- ❌ 非官方内容严禁直接进入 practice/（必须先进 pending/）
- 🔄 所有 pending 内容需通过审核流程后才能移至 practice/

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

**最后更新**：2026-04-26（加入审核与治理工作流 v2.0）
