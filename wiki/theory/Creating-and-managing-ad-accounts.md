# 在 Walmart Connect Ad Center 中创建和管理广告账户

> Super Admin 可以在组织内创建最多 5 个广告主账户，支持独立账单、计费结构和不同业务单元。

## 创建新账户的适用场景

- 入驻组织下的新品牌或供应商
- 不同业务单元需要独立账单或 IO/PO 结构
- 按品牌或渠道设置独立活动结构
- 因品牌/供应商变更重新组织或停用旧账户
- 授予代理商受限访问权限

## 组织层级结构

```
Organization（组织）
  └─ Advertiser Account（广告主账户）
        └─ Media Solution（媒体解决方案）
              └─ Campaign（活动）
```

## 账户可配置项

每个广告主账户可有独立的：

| 配置项 | 说明 |
|--------|------|
| Catalog 映射 | 品牌、供应商或商品 |
| 管理实体 | 供应商、代理商或合作伙伴 |
| 计费实体 | 供应商或代理商 |
| 管理员和用户 | 不同访问级别 |
| 广告渠道 | Display、Sponsored Search、In-store |

## 如何创建新账户

1. 点击右上角 **Account** 图标 → **Manage profile and account**
2. 在 *Manage your ad accounts* 中点击 **+ Create ad account**
3. 输入广告主账户名称
4. （可选）选择合作伙伴/API 代理商
5. 选择关联的品牌或供应商
6. （可选）分配账户管理员
7. 添加账单信息（主要账单联系人）
8. 点击 **Create**

## 如何编辑现有账户

只有 Super Admin 可以更新账户信息：

1. 在 Ad accounts 页面找到要编辑的账户
2. 在 *Actions* 列下点击 **三个点** → **Edit Account**
3. 点击右上角 **Edit** 编辑各部分
4. 点击 **Save** 保存

**注意：** 可以在 *Catalog mapping* 中添加新品牌/供应商，但无法删除已有的。只有支持团队可以移除。

## 相关页面

- [[theory/Accessing-Walmart-Connect-Ad-Center]] — 访问 Ad Center
- [[theory/User-roles-and-permissions]] — 用户角色和权限
- [[theory/Account-access-as-a-non-admin-user]] — 非管理员访问

---

> 来源：`raw/walmart advertising guide/Creating and managing ad accounts in Walmart Connect Ad Center.md`
