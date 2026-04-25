# Marketplace 卖家账单政策

> Marketplace 卖家自助 Sponsored Search 和 Onsite Display 广告的账单管理说明。

## 支付方式

| 支付方式 | 说明 |
|----------|------|
| **Seller Balance** | 默认主要支付方式（即净销售额） |
| **信用卡/借记卡** | 添加为主要或备用付款方式 |

**重要说明：**
- 每笔广告主账户关联独立的 Billing Manager 账户
- 欠费发票将从 Billing Manager 中选择的支付方式扣款
- 只能将一个支付方式设为"主要"，一个设为"备用"
- 超过 $50,000 的发票不能使用信用卡，只能使用 Seller Balance

## 开票规则

发票金额基于**账单周期的广告花费**：

| 触发条件 | 说明 |
|----------|------|
| 达到 **Advertiser Invoice Threshold** | 次日开票（最高 $20,000） |
| 达到组织消费限额的 **70%** | 次日开票 |
| 账单周期结束 | 按周期定期开票 |

**Organization Spend Limit（组织消费限额）：**
- 在组织级别设置，适用于所有广告主账户
- 一旦达到，全组织所有广告暂停
- 根据卖家的 GMV 和表现自动评估
- 可以申请提高（提交 case）

## 支付流程

| 支付方式 | 自动扣款 | 手动支付 |
|----------|----------|----------|
| 信用卡/借记卡（主要） | 发票生成日自动扣款 | Pay Now 按钮 |
| Seller Balance | 账单周期结束自动扣除 | 不可用 |

**Pay Now 功能：**
- 支付失败发票 → 自动扣款失败后可用
- Pending 状态发票 → 随时可用
- 可用信用卡/借记卡立即支付

## 访问 Billing Manager

以下用户可访问 Billing Manager：Super Admin、Org Admin、Account Admin、Org/Account Standard（有 Billing Manager 访问权限的用户）。

## 相关页面

- [[theory/Open-a-case-with-Advertiser-Help]] — 联系广告主支持
- [[theory/User-roles-and-permissions]] — 用户角色和权限
- [[theory/Finding-IDs-and-account-names]] — 查找 ID 和账户名称

---

> 来源：`raw/walmart advertising guide/Marketplace sellers Billing Policy.md`
