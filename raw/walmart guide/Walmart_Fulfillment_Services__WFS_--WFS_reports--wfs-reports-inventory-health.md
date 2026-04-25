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

WFS reports: Inventory health

Last updated on Oct 2, 2025

Reading time: 5 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/wfs-reports-inventory-health#Overview)
- [Access this report](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/wfs-reports-inventory-health#access_this_report)
- [Dive into details](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/wfs-reports-inventory-health#dive_into_details)
- [Understand report metrics](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20reports/wfs-reports-inventory-health#understand_report_metrics)

* * *

Overview

The Inventory Health report is helpful in understanding your overall inventory levels, as well as important item-level inventory and sales information. It provides item-level insights such as inbound inventory, inventory pending review, inventory movement in progress and valuable information to make replenishment decisions easier.

## Access this report

To access this report from Seller Center, log in and go to [**Reports**](https://seller.walmart.com/wfsLite/reports). This report will be located under the _Inventory_ section.

To access this report from an API, go to the [developer portal](https://developer.walmart.com/us-marketplace/reference/getinventoryhealthreport).

## Dive into details

#### How to use this report effectively

- View inventory health including units available to sell, inventory age and historical sales data.

-  This is a large report; exports may take additional time.

#### Important insights

- The _Suggested units_ column tells you how much inventory to send based on your forecasted sales demand, current available-to-sell inventory and number of units already in transit to Walmart fulfillment centers.
- The available-to-sell quantity in this report is updated less frequently than the [Inventory page.](https://seller.walmart.com/wfs/inventory)


## Understand report metrics

|     |     |
| --- | --- |
| **Column Name** | **Definition** |
| GTIN | 14-digit Global Trade Item Number, including check digit, that's unique to the item. If you submit a 12-digit UPC rather than a GTIN, the GTIN will have two 0s followed by the UPC. |
| Item ID | A Walmart-assigned ID used internally to track items. This ID can be found at the end of the item page URL for that item. |
| Vendor (Seller) SKU | Vendor SKU ID is a unique item identifier provided during item setup. |
| Product Name | Name   of the item entered on item setup. |
| Brand Name | Brand of the item entered during item setup. |
| Publishing Status | WFS items’ publishing status on [walmart.com](http://walmart.com/) can be Published, Unpublished, Processing, Stage, Error or WFS ineligible. |
| Item Lifecycle | Active: The item is currently in your catalog, regardless of its publishing status. <br>Retired: You’ve removed the item from your catalog, or it’s gone past its listing end date. Retired items can be made active again. <br>Archived: You’ve permanently deleted the item from your catalog. Archived items can’t be made active again. |
| Available Units | Units that have been received and are included in the count of inventory that is available for customers to purchase. Referred to as ATS (available to sell). |
| Reserved Units | Number of units from customer orders that have been placed but not yet fulfilled. Reserved units are not counted as available units, which prevents overselling.<br>Once these orders ship, the reserved units will decrease. If there's a canceled order, the reserved units will move to the pool of available units  . |
| Damaged Receipts | Number of units you have for a SKU that can’t be received into inventory because they were received damaged. |
| Inbound Units | Number of units that you’ve sent to WFS but haven’t been received yet. |
| Inventory Movement | These units are currently being moved to another fulfillment center due to a merchandise transfer request (MTR) and are unavailable for customers to place orders against. |
| Inventory review | These units are undergoing standard review processes such as compliance and expiration date checks, cycle counts and seller-requested inventory removals. This typically takes 24–48 hours. |
| Cube Used | Cubic space taken by the item in the WFS fulfillment network. |
| First In Stock Date | Date when an item physically arrives   for the first time at a fulfillment center. |
| Sell Through Rate | Number of units you’ve shipped to customers in the last 90 days divided by your average number of units stored in a WFS fulfillment center over the same period.<br>≥1.5 = Excellent<br>1 - 1.5 = Good<br>0.75 – 1 = Average<br>≤0.75 = Below average |
| Days of supply | Number of days we anticipate your current available and inbound inventory will last based on your forecasted sales demand. |
| Predicted out of stock date | A calculation of when you will run out of inventory based on your current available units, inbound units and forecasted demand. |
| Forecast <date> - <date> (current month) | The number of units that are forecasted to sell for the current month. |
| Forecast <date> - <date> (next month) | The number of units that are forecasted to sell for the upcoming month. |
| Suggested Units | The number of units we suggest sending to ensure you do not lose opportunity for sales, given the days of supply. |
| Surplus Units | Number of units with more than 180 days of supply   based on the item's forecasted sales demand. |
| ATS 0-90 days | Based on already scheduled inbound shipments, the number of units expected to be available to sell in the next 90 days. |
| ATS 91-180 days | Based on already scheduled inbound shipments, the number of units expected to be available to sell in the next 91 - 180 days. |
| ATS 181-270 days | Based on already scheduled inbound shipments, the number of units expected to be available to sell in the next 181 - 270 days. |
| ATS 271-365 days | Based on already scheduled inbound shipments, the number of units expected to be available to sell in the next 271-365 days. |
| ATS 365+ days | Based on already scheduled inbound shipments, the number of units expected to be available to sell after 1 year. |
| Last 30 days units received | Number of units WFS received through inbound orders for the last 30 days. |
| Last 30 days PO units | Number of units claimed   by the seller to be on inbound orders for the last 30 days. |
| Last 7 days units sales | Number of units sold for an item over the last 7 days. |
| Last 7 days sales | Dollar amount in sales for an item over the last 7 days. |
| Last 7 days in-stock days | Number of days out of the last 7 days that the item has been in stock in the WFS fulfillment network. |
| Last 30 days units sales | Number of units sold for an item over the last 30 days. |
| Last 30 days sales | Dollar amount in sales for an item over the last 30 days. |
| Last 30 days in-stock days | Number of days out of the last 30 days that the item has been in stock in the WFS fulfillment network. |

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