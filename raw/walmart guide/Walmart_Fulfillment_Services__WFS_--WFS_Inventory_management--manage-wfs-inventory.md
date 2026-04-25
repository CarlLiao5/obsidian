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

Manage WFS inventory

WFS multi-box: Manage inventory

WFS Inventory Health page overview

WFS customer orders

WFS inventory movements (MTR)

WFS inventory: Remove items from a fulfillment center

Move aged inventory

###### Walmart Cross Border - Imports

###### Walmart Multichannel Solutions

###### WFS growth opportunities

###### WFS policies & standards

###### WFS programs & services

###### WFS reports

###### Troubleshooting

###### Seller Fulfillment Services

###### Order management

###### Taxes & payments

###### Policies & standards

###### Growth opportunities

###### Advertising

###### Walmart Seller appNew

Guide

Manage WFS inventory

Last updated on Feb 11, 2026

Reading time: 7 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20Inventory%20management/manage-wfs-inventory#Overview)
- [How do I manage my inventory?](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20Inventory%20management/manage-wfs-inventory#manageinventory)
- [Important inventory insights](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20Inventory%20management/manage-wfs-inventory#inventoryinsights)

- [Understanding all table metrics](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20Inventory%20management/manage-wfs-inventory#tablemetrics)

* * *

Overview

The [**WFS Inventory page**](https://login.account.wal-mart.com/authorize?responseType=code&state=RK8AUD0V73&scope=openId&nonce=JYIDJTS17M&clientType=seller&redirectUri=https://seller.walmart.com/aurora/v1/auroraScCoreService/rest/login/sso/hook&clientId=66620dfd-1f3f-479b-8b9c-e11f36c5438b) gives a snapshot of your inventory performance, both overall and at the item level. Check this page to review your stock status, make replenishment decisions and ensure inventory levels are meeting customer demand. You can also access inventory insights from the [**Inventory Health page**](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20Inventory%20management/wfs-inventory-health-page) or the [**Developer Portal**](https://developer.walmart.com/global-marketplace/reference/getwfsinventory) if you use APIs. In this guide, learn how to understand the metrics and manage your inventory.

## How do I manage my inventory?

The [**WFS Inventory page**](https://seller.walmart.com/wfsLite/manage-inventory) page provides a combination of insights and options to help you manage your inventory.

Review the important metrics across the top of the page. These apply to your overall WFS inventory using data that refreshes each day:

- Daily in-stock sales rate is the percentage of your total potential sales of items that are active and have available units.

- Sell-through rate is the total number of units you’ve sold to customers in the last 90 days divided by your average total number of units stored in a WFS fulfillment center during the same period. A sell-through rate of 1.5 or more is considered Excellent, between 1–1.5 is considered Good, between 0.75–1 is considered Average, and less than 0.75 is considered Below Average.

- Aged units is the percentage of your total units stored in a WFS fulfillment center for over 365 days.

- Unpublished units is the percentage of your total units stored in a WFS fulfillment center that are unpublished on walmart.com.


The inventory table allows you to check your individual items’ inventory health. Select each tab for a customized table view that shows all your items, only your out-of-stock and at-risk items, or only your items with surplus and aged units.

![](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blt47daa2e0f51675fa/68125117f787f17743d2a529/whole_page.png?branch=us_mplearn)

There are 2 ways to restock your inventory:

1. Select the _Manage inventory_ button, then choose _Send inventory_ from the dropdown. You'll then be guided through a shipping plan, including adding items you want to send.

2. Select items directly from the table and add them to a new shipping plan by selecting _Send inventory_ from the options that appear.


Perform item-level actions by selecting the 3 dots under the _Actions_ column:

- View the inventory log

- Print a GTIN label

- Send inventory
- Remove inventory


* * *

## Important inventory insights

- Select any item in the _Item name_ column to view its brand, GTIN, SKU, item ID, and condition. You can also edit the item or go to its listing on Walmart.com.


![item_flyout.png](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blta7cca141f3b29bb6/681251174fad9866d3c3dcf7/item_flyout.png?branch=us_mplearn)

- **Sell-through rate** is the number of units you’ve shipped to customers in the last 90 days divided by your average number of units stored in a WFS fulfillment center over the same period. A sell-through rate of 1.5 or more is considered Excellent, between 1–1.5 is considered Good, between 0.75–1 is considered Average, and less than 0.75 is considered Below Average.

- **Unavailable to sell** means these units are unavailable for customers to place orders against. Select the unit quantity in the Unavailable to sell column to see how many units are pending review and how many are currently being moved to another fulfillment center due to a merchandise transfer request (MTR). Inventory reviews typically take 24–48 hours to check for compliance, expiration dates, cycle counts, and more.


![unavilable_flyout.png](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blte9b73ee938b32a6f/681258d335be7a2dad43724b/unavilable_flyout.png?branch=us_mplearn)

- **Surplus units** is the number of units over 180 days of supply based on the item's forecasted sales demand.

- **Aged units** is the number of units stored in a WFS fulfillment center for over 365 days.

- **Suggested units** is the quantity of units our algorithm suggests you send to WFS based on predicted sales demand. To generate these suggestions, our algorithm considers several factors including past sales, seasonality, listing quality, pricing, and more. Select the number under the Suggested units column to see a breakdown of your available-to-sell units, how many units of this item are currently inbounding to WFS, your forecasted item sales for the next 1–4 and 5–8 weeks by date, and the number of suggested units to send.

![](<Base64-Image-Removed>)

- **Publishing status** refers to WFS items on walmart.com. Items can be Published, Unpublished, Processing, Stage, Error, or WFS ineligible. Select an individual item’s status in the **Publishing status** column to learn more details.


  - **Published**: The item’s setup was successful, and customers can purchase the item on walmart.com as long as there’s available inventory.


  - **Unpublished**: The item is temporarily unavailable on walmart.com due to listing issues, such as pricing or trust & safety, or because you selected a publishing start date in the future.


  - **Processing**: This item’s publishing status is in transition and will be updated soon.


  - **Stage**: This item will be published after you complete the onboarding process.


  - **Error**: One or more system errors prevented the item from publishing.

  - **WFS ineligible**: This item is currently not eligible to be fulfilled by Walmart due to updated prohibited item restrictions.


- **Item lifecycle** is 1 of 3 possible stages for an item:


  - **Active**: The item is currently in your catalog, regardless of its publishing status.


  - **Retired**: You’ve removed the item from your catalog, or it’s gone past its listing end date. Retired items can be made active again.


  - **Archived**: You’ve permanently deleted the item from your catalog. Archived items can’t be made active again.


* * *

## Understanding all table metrics

| **Metric** | Definition |
| --- | --- |
| Item name | The title of your item. |
| Brand | The brand name of your item. |
| GTIN | The Global Trade Identification Number associated with this item. If you submit a 12-digit UPC rather than a GTIN, the GTIN will have two 0s followed by the UPC. |
| Item ID | A Walmart-assigned ID used internally to track items. This ID can be found at the end of the item page URL for that item. |
| SKU | The SKU you provided for this item. |
| Stock status | Out-of-stock items have 0 units available to sell. At-risk items have less than 28 days of supply, counting both available to sell and inbound units. In-stock items have more than 28 days of supply. |
| Daily sales | Average sales per day for the last 30 days. It’s total sales divided by number of days when you had at least 1 unit available to sell or sold that day. |
| Daily units sold | Average number of units sold per day in the last 30 days. It's total units sold divided by number of days when you had at least 1 unit available to sell or sold that day. |
| Sell-through rate | Number of units you’ve shipped to customers in the last 90 days divided by your average number of units stored in a WFS fulfillment center over the same period. A sell-through rate of 1.5 or more is considered Excellent, between 1–1.5 is considered Good, between 0.75–1 is considered Average, and less than 0.75 is considered Below Average. |
| Available to sell | Units that are available for customers to place orders against. |
| Unavailable to sell | Units that are temporarily unavailable for customers to place orders against. Select the unit quantity in the Unavailable to sell column to see how many units are pending review and how many are currently being moved to another fulfillment center due to a merchandise transfer request (MTR).  Inventory reviews typically take 24–48 hours to check for compliance, expiration dates, cycle counts, and more. |
| Reserved units | Number of units from customer orders that have been placed, but not yet fulfilled. Reserved units are not counted as available units, which prevents overselling. Once these orders ship, the reserved units will decrease. If there's a canceled order, the reserved units will be available again. |
| Inbound units | Number of units that you’ve sent to WFS but haven’t been received yet.<br>Items are not instantly available to sell after a shipment has been marked as delivered. These units will remain in the Inbound Units column until they reach a sellable state in the warehouse. |
| Surplus units | Number of units over 180 days of supply based on the item's forecasted sales demand. |
| Aged units | Number of units stored in a WFS fulfillment center for over 365 days. |
| Days of supply | Number of days we anticipate your current available and inbound inventory will last based on your forecasted sales demand. |
| Out-of-stock date | The date we estimate you’ll run out of inventory, based on the days of supply. |
| Suggested units | Number of units our algorithm suggests you send to WFS based on the item’s forecasted sales demand. To generate these suggestions, our algorithm considers several factors including past sales, seasonality, listing quality, pricing, and more. |
| Publishing status | WFS items’ publishing status on walmart.com can be Published, Unpublished, Processing, Stage, Error, or WFS ineligible. <br>Select an individual item’s status to learn more details. |
| Item lifecycle | Active: The item is currently in your catalog, regardless of its publishing status. <br>Retired: You’ve removed the item from your catalog, or it’s gone past its listing end date. Retired items can be made active again. <br>Archived: You’ve permanently deleted the item from your catalog. Archived items can’t be made active again. |
| Item condition | State of the item's appearance, quality, packaging, functionality, and previous usage. |

Notes:

Walmart Marketplace has no obligation and makes no promises as to any minimum amount of product you need to purchase or possess as a Marketplace Seller. No person has authority, on Walmart’s behalf, to make any representations or promises to you as a Seller of any expected or possible level of business on the Marketplace, or of Walmart’s intentions or expectations regarding any present or future business with us as a Supplier. All decisions on product amounts are solely made by the seller. Further, seller acknowledges Walmart will not be liable in any way for any decision made or any action taken by seller based on the assortment growth or inventory management tools, dashboards, or recommendations given thereon and agrees that these tools are provided only as forecasts for use by seller in addition to whatever other information seller seeks to consider in making decisions for seller’s business. The seller shall be fully responsible.

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

###### WFS Inventory Health page overview

Walmart Fulfillment Services (WFS)

If you're a Walmart Marketplace seller with established sales history and are using Walmart Fulfillment Services, you can use the WFS Inventory Health page to monitor key metrics about your items stored in Walmart fulfillment centers and take action as needed.

Go to guide

Guide

###### Move aged inventory

Walmart Fulfillment Services (WFS)

Follow these tips and techniques to avoid long-term storage fees and quickly sell through aged inventory.

Go to guide

Guide

###### WFS reports: Inventory health

Walmart Fulfillment Services (WFS)

Learn which metrics and insights are included in the WFS Inventory health report.

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