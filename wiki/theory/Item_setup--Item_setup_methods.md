---
author: Walmart 官方文档
auditor: 知识库管理员
status: verified
audit_date: 2026-04-26
tags: [官方文档, 知识库]
---

# 商品设置方法（Item Setup Methods）

> 在 Walmart Marketplace 上架商品的 6 种方法详解。

## 上架方法对比

| 方法                                | 适用场景                          | 操作路径                                             |
| --------------------------------- | ----------------------------- | ------------------------------------------------ |
| **Express setup**                 | 已在 Walmart 目录的商品，一次最多 50 件    | Catalog → Add items → Match items                |
| **Create new items**              | Walmart 目录中不存在的新品             | Catalog → Add items → Create items → Single item |
| **Bulk upload**                   | 大量商品（使用 Full Setup 模板）        | Catalog → Add items → Upload in bulk             |
| **Match Walmart catalog**         | 一次匹配数千件商品                     | Catalog → Add items → Match items（批量勾选）          |
| **Import from other marketplace** | 从 Amazon/eBay/Supplier One 导入 | Catalog → Add items → Import items               |
| **Virtual packs**                 | 创建多件捆绑 SKU                    | Catalog → Add items → Virtual packs              |

## 单个商品设置流程（Create a new item）

1. Catalog → Add items → Create items → Single item
2. 选择分类和子分类
3. 填写商品识别符（GTIN/UPC）
4. 选择配送选项
5. 填写属性（内容/图片/规格）
6. 提交 → Activity Feed 跟踪（最多 24 小时）

## WFS 商品设置

WFS 商品需要额外信息：
- 原产国
- 贸易品层次结构（Trade Item Hierarchy）
- 危险品合规信息（如适用）

## AI 辅助

在设置过程中可使用 **AI 助手** 生成：
- 产品名称
- 描述
- 关键特性

AI 生成内容须准确、真实，符合市场政策。

## 关联页面

- [[theory/Add-a-New-Item_-Create-a-new-item]] — 单个新商品设置详解
- [[theory/Add-items-in-bulk_-Upload-a-spreadsheet]] — 批量上传指南
- [[theory/Add-items-in-bulk_-Set-up-items-by-match]] — 批量匹配指南
- [[theory/WFS_item_setup]] — WFS 商品设置（转换）

---

> 源文件目录：`raw/Item_setup--Item_setup_methods/`