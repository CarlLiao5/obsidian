# 税务与支付子分类

> [[theory/Taxes_&_payments]] 的详细子分类索引。

## 子分类

| 子分类 | 说明 | 页面数 |
|--------|------|--------|
| [[theory/Taxes_&_payments--Billing_Information]] | 账单支付方式（ACH/信用卡/PayPal）| 1 |
| [[theory/Taxes_&_payments--Payments]] | 收款方式、结算周期、付款活动、市场钱包 | 1 |
| [[theory/Taxes_&_payments--Settings]] | 支付设置与市场钱包注册 | 1 |
| [[Taxes_&_payments--Tax_information]] | 销售税代收、产品税、1099-K、税务分类 | 1 |
| [[theory/Taxes_&_payments--Troubleshooting]] | 推荐费争议 | 1 |

## 核心流程

```
收款设置 → [[theory/Payment-processing]]
  ├─ Marketplace Wallet（无手续费，推荐）
  ├─ Payoneer / Hyperwallet / PingPong（有手续费）
  └─ LianLian / Airwallex / WorldFirst（仅中港）
    ↓
结算周期 → 双周结算（每14天），Cut-off 后进入下一周期
    ↓
新卖家冻结 → [[theory/new-seller-payment-hold-policy]]（90天+$7,500门槛）
    ↓
税务     → [[theory/Sales-tax-collection]]（Walmart 代收代缴46州）
          [[theory/Product-tax-codes-for-shipping-fees]]（运输费税务代码）
          [[theory/Product-fees-&-tax-collection]]（产品费用与税务）
          [[theory/Retrieve-form-1099-K]]（年度税表）
```

## 收款服务商对比

| 注册地 | 可选服务商 |
|--------|-----------|
| 美国 | Marketplace Wallet（推荐）、Hyperwallet、Payoneer、PingPong |
| 中国/香港 | Payoneer、PingPong、LianLian、Airwallex、WorldFirst、NetEase |
| 加拿大 | Payoneer |
| 其他 | Payoneer、PingPong |

## 关联分类

- [[Policies_&_standards--Payments]] — 支付政策层
- [[theory/Growth_opportunities--Financing_options]] — 融资选项（Marketplace Capital）

---

> 源文件目录：`raw/Taxes_&_payments/`