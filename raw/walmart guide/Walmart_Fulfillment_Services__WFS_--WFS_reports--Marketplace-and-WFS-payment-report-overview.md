Marketplace Learn

Guides

Sign In

* * *

[AcademyNew](https://marketplacelearn.walmart.com/academy)

[Guides](https://marketplacelearn.walmart.com/guides)

[Events](https://marketplacelearn.walmart.com/events)

[ForumNew](https://marketplacelearn.walmart.com/forum)

News

[FAQ](https://marketplacelearn.walmart.com/faqs)

Notifications

* * *

Guides

* * *

###### Getting started

###### Item setup

###### Catalog management

###### Walmart Fulfillment Services (WFS)

###### WFS basics

###### Getting started with WFS

###### WFS item setup

###### Shipping to WFS

###### WFS Inventory management

###### Walmart Cross Border - Imports

###### Walmart Multichannel Solutions

###### WFS growth opportunities

###### WFS policies & standards

###### WFS programs & services

###### WFS reports

WFS reports: Customer returns

WFS reports: GMV penetration

WFS reports: Inbound receipts

WFS reports: Inbound transportation

WFS reports: Inventory health

WFS Reports: Inventory Reconciliation

WFS Reports: Item conversion

WFS reports: Marketplace and WFS payments

WFS Reports: Orders

WFS Reports: Settlement

WFS reports: Storage

###### Troubleshooting

###### Seller Fulfillment Services

###### Order management

###### Taxes & payments

###### Policies & standards

###### Growth opportunities

###### Advertising

###### Walmart Seller appNew

Guide

WFS reports: Marketplace and WFS payments

Last updated on Sep 24, 2025

Reading time: 3 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/Marketplace-and-WFS-payment-report-overview#Overview)
- [Access this report](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/Marketplace-and-WFS-payment-report-overview#access_this_report)
- [Dive into details](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/Marketplace-and-WFS-payment-report-overview#dive_into_details)
- [Understand report metrics](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/Marketplace-and-WFS-payment-report-overview#understand_report_metrics)
- [Frequently asked questions](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/Marketplace-and-WFS-payment-report-overview#frequently-asked-questions)


* * *

Overview

When you fulfill with WFS, you have additional payment details that are important to understand. The Marketplace and WFS payment report includes financial details for all order activity during the payment period, such as shipping charges and referral fee rates. You should review this report each payment cycle to verify that all transactions were processed as expected.

## Access this report

To access this report from Seller Center, log in and go to [**Reports**](https://seller.walmart.com/wfsLite/reports).  This report will be located under the Payments and fees section. Choose a report settlement date to download the file.

To access this report from an API, go to the [developer portal](https://developer.walmart.com/us-marketplace/docs/generate-a-reconciliation-report).

## Dive into details

Start with row 3: this is a summary of your payment period dates, total amount paid to you and the account your payment was deposited to.

The rows below row 3 are line-item records of every payment and deduction within the selected payment period.

### Important insights

This report contains data from optional WFS programs as well, including Walmart Cross Border: Imports, Multichannel Solutions, etc.

## Understand report metrics

| Column Name | Definition |
| --- | --- |
| Period Start Date | When the payment cycle starts. For seller-level payments, like WFS and WPA, it’s the start date for the billing period. It’ll be blank if you don’t participate in these programs. |
| Period End Date | When the payment cycle ends. For seller-level payments, like WFS and WPA, it’s the end date for the billing period. It’ll be blank if you don’t participate in these programs. |
| Total Payable | The net amount transferred to your payment processor account for this payment cycle. It’s the sum of all transactions reflected in Amount (column M). |
| Currency | The currency in which your payment was issued. |
| Transaction key | Identifier that Walmart uses to internally track transactions |
| Transaction Posted Timestamp | Date that the transaction was posted in our payment system |
| Transaction Type | Indicates a debit or a credit <br>- Reserve: Funds debited from your account to cover for future refunds<br>- Release Reserve: Funds credited against a previous account reserve<br>- Sale: Transactions credited to your account for the orders shipped in each payment period<br>- Refund: Transactions refunded against a sale order<br>- Dispute Settlement: Adjustments credited or debited as part of dispute resolution<br>- Adjustment: A miscellaneous credit or debit made by Walmart to your account, including receiving error chargeback, damage in warehouse, lost inventory, and found inventory<br>- Service Fee: Debits applied to your account as payment for different Walmart services, including WFS fulfillment fee, storage fee, and more |
| Transaction Description | Reason for the debit or credit |
| Customer Order # | Order number that the Walmart customer gets. One order number can be associated with multiple transactions |
| Customer Order Line # | Line item number that corresponds to a specific item included in a customer order |
| Purchase Order # | Unique number assigned to a specific shipment |
| Purchase Order Line # | Line item within the PO number  of the particular SKU that was ordered |
| Amount | Amount that was credited or debited to your account for the transaction |
| Amount type | Reason for the amount transaction, such as product price, product tax, shipping, referral fee on product and more |
| Ship Qty | Number of items sold or refunded |
| Commission Rate (referral fee) | Rate applied to your sale, as determined by the contract category (column Y) of the item |
| Transaction Reason Description | Describes the reason for a refund. This is only available if transaction type (column F) is refund. |
| Partner Item ID | SKU of the purchased item |
| Partner GTIN | GTIN of the purchased item (if applicable) |
| Partner Item Name | Name of your item as it appears on Walmart.com |
| Product Tax Code | Item's tax code, used to calculate sales tax for the item |
| Ship to State | Customer state where order was shipped |
| Ship to City | Customer city where order was shipped |
| Ship to Zip Code | Customer zip code where order was shipped |
| Contract Category | Product category used to determine the commission rate (referral fee) for the item. See [Referral fees for contract categories](https://marketplacelearn.walmart.com/guides/Getting%20started/Onboarding/Referral-fee-schedule-for-contract-categories?locale=en-US) for details. |
| Product Type | Type of item sold |
| Commission rule | Dynamic commission rule ID (if applicable) |
| Shipping Method | Shipment speed chosen by the customer |
| Fulfillment Type | Whether the item was seller-fulfilled or Walmart-fulfilled (WFS) |

## Frequently asked questions

* * *

How do I dispute a charge?

If you have questions about your payment report, select the Help button in the Seller Center menu bar to contact Support. Please provide the payment’s transaction key (column E) in the issue description.

* * *

#### Tell us what you think

* * *

More in Walmart Fulfillment Services (WFS)

Guide

###### Walmart Fulfillment Services (WFS): Overview

Walmart Fulfillment Services (WFS)

Walmart Fulfillment Services (WFS) enables you to spend more time focusing on increasing sales, while having confidence that your orders will be delivered quickly and with outstanding customer support.

Go to guide

Guide

###### WFS fees

Walmart Fulfillment Services (WFS)

WFS' fee structure is simple and straightforward, without signup or monthly subscription fees.

Go to guide

Guide

###### WFS cost estimator

Walmart Fulfillment Services (WFS)

See examples of WFS fulfillment and storage fees, as well as how they're calculated.

Go to guide

Related guides

Guide

###### WFS fees

Getting started

WFS' fee structure is simple and straightforward, without signup or monthly subscription fees.

Go to guide

Guide

###### WFS cost estimator

Walmart Fulfillment Services (WFS)

See examples of WFS fulfillment and storage fees, as well as how they're calculated.

Go to guide

Guide

###### WFS settings: Add billing information

Walmart Fulfillment Services (WFS)

The Seller Center billing platform allows you to automatically pay any outstanding WFS fees.

Go to guide

©  2026 Walmart. All Rights Reserved

[Privacy Policy](https://corporate.walmart.com/privacy-security/walmart-marketplace-seller-privacy-policy)

###### Seller Resources

[Developer Portal](https://developer.walmart.com/)

[Seller Center](https://seller.walmart.com/)

[Seller Support](https://seller.walmart.com/support?locale=en-US)

[Seller Better Blog](https://marketplace.walmart.com/sellbetterblog/)

###### Get to know us!

[Shop Walmart.com](https://www.walmart.com/)

[Walmart Inc](https://corporate.walmart.com/)

[@WalmartLabs](https://www.walmartlabs.com/)

[The Walmart Digital Museum](https://www.walmartmuseum.com/)

###### Follow us

Edit

![captcha logo](https://i5.walmartimages.com/dfw/63fd9f59-a377/cc0dfcaf-9f33-4cff-b058-cb80e0cf5065/v1/human_with_cat.svg)Robot or human?

Activate and hold the button to confirm that you’re human. Thank you!