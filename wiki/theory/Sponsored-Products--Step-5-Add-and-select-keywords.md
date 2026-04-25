---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# Step 5 — 添加关键词并设置出价 (Add and Select Keywords)

> 为手动 Sponsored Products 广告组添加关键词、选择匹配类型并设置出价。

## 概述

手动活动的关键词设置是精细化广告投放的核心。在关键词部分选择和/或添加关键词，并为每种匹配类型设置出价。

## 匹配类型

| 类型 | 说明 | 竞价建议 |
|------|------|---------|
| **Broad（广泛）** | 词序无关，可插入其他词 | 覆盖最广 |
| **Phrase（短语）** | 词序固定，中间可有其他词 | 中等覆盖 |
| **Exact（精确）** | 词序完全一致 | 最精准 |

**注意：** 出价不能超过 $100，最多 2 位小数。

## 添加关键词的方法

### Suggested Keywords（建议关键词）

系统根据广告组内商品相关性提供最多 220 个关键词建议。实时表现数据还会自动识别新的关键词机会（表现型建议置顶）。

- 点击单个关键词旁的 **Add** + 选择匹配类型
- 或勾选多个 → **Add Keywords** → 选择匹配类型

可下载：建议关键词列表 / 已选关键词列表 / CSV 模板

### Additional Keywords（自定义关键词）

自行添加不在建议列表中的关键词：

**方式一：文本框输入**
- 每行一个关键词，最多 100 个
- 输入后点击 **Add Keywords** → 选择匹配类型

**方式二：CSV 上传**
- 下载模板 → 填写关键词 + 出价 + 状态
- 状态列填 `Enabled` 或留空启用，`Disabled` 禁用
- 保存并上传

**关键词规则：**
- 每条关键词最多 80 字符（含空格）
- 不允许全串特殊字符（`#!%&@`、`$$$$$$`）
- 系统自动标准化关键词（`gift cards` / `gift cardz` → `gift card`）

**归并规则：** 若多个原始关键词被归并为同一标准化关键词，系统选择各匹配类型中的最高出价。

## Selected Keywords（已选关键词）

所有已添加的关键词（含建议和自定义）汇总在此，可：
- 修改出价值
- 批量启用/暂停关键词
- 批量修改出价：勾选 → 选择操作（暂停/恢复/设置出价/应用建议出价）

**广告组限制：** 每广告组最多 1000 个关键词-匹配类型组合。

## 关键词命名最佳实践

为便于识别和管理，建议按以下方式命名广告组：
- 按品牌、类别、畅销品组织
- 使广告组名称与组内商品易于关联

## 相关页面

- [[theory/Sponsored-Products--Create-a-manual-campaign]] — ���建手动活动
- [[theory/Sponsored-Products--Step-4-continued-Add-items-to-an-ad-group]] — 添加商品（上一步）
- [[theory/Keywords-Planner]] — 关键词规划工具
- [[theory/Keyword-recommendations]] — 关键词推荐

---

> 来源：`raw/walmart advertising guide/Step 5 Add and select keywords.md`