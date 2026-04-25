# Step 4（续）— 添加商品到广告组 (Add Items to an Ad Group)

> 将商品添加到广告组并设置出价（自动活动）或通过 CSV 上传批量添加。

## 添加商品的方式

### 方式一：搜索添加

在广告组的 *Item List* 部分点击搜索图标，输入：
- 商品 ID（部分或完整）
- 商品名称（单词或完整名称）
- 商品关键词
- 品牌名称

找到后点击 **Add** 或 **Add All** 添加到广告组。

### 方式二：CSV 上传

1. 点击下载 CSV 模板
2. 填写必填字段：
   - **Item ID**：商品 ID
   - **Bid（自动活动）**：出价金额
   - **Status**：填 `Enabled` 或留空启用，`Disabled` 禁用
3. 保存并上传 CSV

**出价规则：**
- 不能超过 $100
- 最多 2 位小数
- 每个广告组最多 2000 个商品

## 变体商品

变体组是一组只在少数属性（如颜色、尺寸、图案）上有差异的商品。添加变体的方法：

1. 搜索**主变体**（Primary Variant）的商品 ID
2. 在下拉菜单中选择：
   - **Add item**：仅添加主变体
   - **Add all variations**：添加变体组全部商品
   - **Add specific variations**：选择特定变体添加

**注意：** 活动上线后无法删除商品，只能将状态改为 Off。每个变体占用广告组的 2000 个商品限额。

## 建议出价

所有商品均显示**建议出价**。为保持竞争力，建议将出价设置为建议出价值。

## 手动活动说明

手动活动的广告组**不出价列**，出价在 Step 5 的关键词层面设置。

## 商品不可用的常见原因

| 原因 | 说明 |
|------|------|
| 最近修改了商品标题/描述/价格 | 同步延迟 1-2 天 |
| 添加刚发布的商品 | 同步延迟 |
| 变体角色变更 | 变体不能作为主变体添加到 Sponsored Brands/Videos |
| 商品状态未发布 | 商品必须在 Seller/Supplier Center 处于发布状态 |
| 未赢得 Buy Box 或无库存 | 无法推广 |

## 相关页面

- [[theory/Sponsored-Products--Step-4-Create-ad-groups]] — 创建广告组（上一步）
- [[theory/Sponsored-Products--Step-5-Add-and-select-keywords]] — 添加关键词（手动活动下一步）

---

> 来源：`raw/walmart advertising guide/Step 4 (continued)Add items to an ad group.md`