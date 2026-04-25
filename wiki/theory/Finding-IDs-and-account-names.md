# 查找广告账户 ID 和名称

> 在 Walmart Connect Ad Center 中查找 Advertiser ID、Campaign ID 和 Account Name 的操作指南。

## 查找 Advertiser ID（广告主 ID）

### Sponsored Search

1. 登录 [Walmart Connect Ad Center](https://advertising.walmart.com/)
2. 在左侧导航栏选择 **Reports** → **Advertiser**
3. Advertiser ID 位于 URL 末尾的数字部分

```
https://advertising.walmart.com/sp/view/report/advertiser/xxxxxx
                                          ↑ Advertiser ID
```

### Display（展示广告）

在 Ad Center 任意页面，URL 中 `aid=` 后面的数字即为 Advertiser ID：

```
https://advertising.walmart.com/display?aid=xxxxxx
                                       ↑ Advertiser ID
```

### Brand Shop and Shelf

在 Shop Builder 平台，URL 中 `aid=` 后面的数字即为 Advertiser ID：

```
https://advertising.walmart.com/shopbuilder?aid=xxxxx
                                             ↑ Advertiser ID
```

---

## 查找 Campaign ID（活动 ID）

### Sponsored Search

1. 在左侧导航栏选择 **All Campaigns**
2. 在活动列表右侧找到 **Campaign Id** 列
3. 对应活动名称即为其 Campaign ID

### Display

1. 在左侧导航栏选择 **Campaigns**
2. 在 **Campaign/Ad Group/Creatives** 列下，活动标题下方即为其 Campaign ID

---

## 查找 Account Name（账户名称）

> 提交 Advertiser Help 工单时必须填写完整的 Advertiser Account Name。

账户命名格式：`Account Name (Organization Name) (Advertiser Type - Demand Channel)`

示例：
- Sponsored Search：`Test Walmart (Walmart Test) (3p-SS)`
- Display：`Walmart Display Test Account (Display)`
- Brand Shop：`Walmart Shop Builder Test Account (Brand Shop)`

### Sponsored Search

- **单账户**：账户名称直接显示在 Ad Center 顶部，无下拉选项
- **多账户**：点击左上角下拉箭头查看所有广告账户名称

### Display

登录后账户名称直接显示在页面顶部。多账户时点击下拉箭头查看完整名称。

### Brand Shop and Shelf

登录后账户名称直接显示在页面顶部。多账户时点击下拉箭头查看完整名称。

---

## 工单提交注意事项

提交 Advertiser Help 工单时，**必须使用完整的广告主账户名称**，包括：

- 账户名称
- 组织名称
- 广告主类型

示例格式：
- Sponsored Search：`Test Walmart (Walmart Test) (3p-SS)`
- Display：`Walmart Display Test Account (Display)`
- Brand Shop：`Walmart Shop Builder Test Account (Brand Shop)`

---

## 相关链接

- [[theory/Open-a-case-with-Advertiser-Help]] — 如何提交 Advertiser Help 工单
- [[theory/Sponsored-Products--Glossary]] — 广告术语表
- [[theory/Marketplace-sellers-Billing-Policy]] — 账单政策
- [[theory/Creating-and-managing-ad-accounts]] — 广告账户管理

---

> 来源：`raw/walmart advertising guide/Finding IDs and account names.md`
> 更新：2026-04-17
