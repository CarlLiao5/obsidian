# 用户角色与权限

> 组织层级结构、用户角色定义及其权限范围。

## 组织层级结构

```
Organization（组织）— 代表 Walmart 供应商或 Marketplace 卖家
  └─ Advertiser Account（广告主账户）— 管理品牌和活动
        └─ Media Solution（媒体解决方案）— Sponsored Search / Display / Shop Builder 等
```

## 角色定义与权限

| 角色 | 人数上限 | 定义 | 核心权限 |
|------|----------|------|----------|
| **Super Admin** | 5 人 | 最高权限，完全控制 | 创建/管理账户、授予/移除用户访问、管理所有组件、访问所有数据 |
| **Org Admin** | 10 人 | 组织级管理员 | 授予/移除用户访问、管理活动、访问所有账户和数据 |
| **Org Standard** | 20 人 | 组织级标准用户 | 按组件分配 View/Edit 权限、访问组织内所有数据 |
| **Account Admin** | 20 人 | 账户级管理员 | 为特定账户分配用户/合作伙伴访问、管理活动 |
| **Account Standard** | 100 人 | 账户级标准用户 | 按组件分配权限、访问账户内数据 |

## 组件权限（可分配）

- 活动管理（Display + Sponsored Search）
- 活动报告（Display + Sponsored Search）
- 创意（Display）
- 资产库（Display）
- 计费管理（Billing Manager）
- 访问管理（Org 或 Account 级别）
- Shop Builder（Brand Shops）
- Shelf Builder（Shop Builder）

## 账户整合

- 只有 Sponsored Search 广告账户可以通过单一广告账户整合
- Display 和 Shop Builder 账户无法整合
- Marketplace 卖家和 Walmart 供应商账户无法合并

## 相关页面

- [[theory/Accessing-Walmart-Connect-Ad-Center]] — 访问 Ad Center
- [[theory/Creating-and-managing-ad-accounts]] — 创建和管理广告账户
- [[theory/Account-access-as-a-non-admin-user]] — 非管理员访问

---

> 来源：`raw/walmart advertising guide/User roles and permissions.md`
