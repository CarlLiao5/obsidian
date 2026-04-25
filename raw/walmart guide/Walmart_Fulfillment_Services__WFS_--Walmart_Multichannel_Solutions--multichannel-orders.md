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

Multichannel Solutions (MCS): Overview

Multichannel Solutions: Set up items

Multichannel Solutions: Add sales channels

Multichannel Solutions: Manage customer orders

Multichannel Solutions: Troubleshooting fulfillment

Multichannel Solutions: Create customer returns

Multichannel Solutions: API integration

Multichannel Solutions: Solution providers

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

Multichannel Solutions: Manage customer orders

Last updated on Feb 28, 2026

Reading time: 7 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#overview)
- [Check in-stock inventory](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#checkinventory)
- [Create multiple orders](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#multipleorders)
- [Create a single order](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#singleorder)
- [Cancel orders](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#cancelorders)
- [Track delivery](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#trackdelivery)
- [Frequently asked questions](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#frequently-asked-questions)

* * *

Overview

As customers place orders on your eCommerce sites, you’ll need to add the orders to Seller Center for Walmart to fulfill. In this guide, we’ll show you how to manage customer orders and track delivery progress.

## Check in-stock inventory

Once you’ve sent items to a Walmart fulfillment center, we treat them as a single pool of inventory. This means we fulfill orders on a first-come, first-serve basis, without reserving units for each sales channel.

Multichannel fulfillment is available at all of our fulfillment centers for delivery in the 50 US states and Puerto Rico.

Here’s how to check real-time inventory you have in stock for all of your sales channels:

1. Log into Seller Center and go to **Inventory**.
2. Select **Download** at the top of the table to download the inventory list.
3. In the downloaded file, look for **Available Units** or **Multichannel Solutions Available to Sell Units**. Both columns tell you how many units are available for multichannel orders at that moment.

For a more detailed view, download the [Inventory Health Report](https://seller.walmart.com/wfsLite/reports) and select either **All WFS Inventory** or **Available for Walmart Multichannel Solutions** to see available or expiring inventory. The multichannel option downloads a report for any inventory that’s at a WFS facility and eligible for multichannel fulfillment. This report will show the number of units shipped in the last 7 or 30 days instead of units sold. You can also easily view inventory that will expire in 31 to 90 days. Most inventory will be reflected in both versions.

Notes:

When you first use Multichannel Solutions, it may take up to 1 hour for data to appear in the Inventory Health Report. It may also take up to 3 hours for the report’s data to refresh, compared to the real-time data in the Inventory page download.

## Create multiple orders

If you have multiple customer orders for fulfillment, you can add all of them at once through a downloadable template. If you are unsure how to fill out the bulk order template, each field contains a brief description to help you along the way and avoid errors.

Log in to Seller Center and go to the [**Multichannel Orders**](https://seller.walmart.com/wfs/multi-channel-solutions/orders) page.

1. Select **Manage fulfillment**, then **Multiple orders** from the dropdown.
2. Download the template.
3. Fill in the template with order channel IDs. You can find these in the [**Multichannel Settings**](https://seller.walmart.com/wfs/multi-channel-solutions/sales-channels) page under the Sales channel ID column.
4. Add customer information and item details.
5. Add "US" for country code in column K.
6. Choose the ship speed in the Shipping Method column.
7. Upload the template and submit.

![](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blt67168cb9b23853b0/6723a236ac5a586a3886fb13/Screenshot_2024-10-31_at_11.26.30_AM.png?branch=us_mplearn)

After you submit, our system will check the file. To track the status, go to the **Submission status** link at the top of the Multichannel Orders page. Download the error report to view issues, edit and resubmit. Here are common errors and how to fix them:

| Error message | Next steps |
| --- | --- |
| Orders are failing because of same SKU with same lineId. | There’s a duplicate order. This may happen if you’re creating a row for each unit, rather than each order. <br>Combine order details into 1 row. Then update the Qty column to match the total number of units going to the customer. |
| Delivery promised failed. | There may not be enough inventory to fulfill the order. Please [check your inventory](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#checkinventory) before placing an order and restock if necessary. |
| SellerLineID needs to be unique | Update SellerLineID for multiple SKUs in an order. |

If there are no issues, the customer orders will appear on the Multichannel Orders page. You’ll also see a Delivered by date, based on your chosen ship speed. Once we start fulfilling the order, you can’t make any changes to the items, quantity or delivery address.

Pro tip

Integrate with our APIs to [automate orders](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api).

* * *

## Create a single order

If you want to add customer orders one at a time, you can easily enter all the information.

1. Log into Seller Center and go to the [**Multichannel Orders**](https://seller.walmart.com/wfs/multi-channel-solutions/orders) page.
2. Select **Manage fulfillment**, then **Single order** from the dropdown.
3. Add the sales channel ID, customer information, shipping speed and item details. Your carrier preference package, based on the sales channel, will be displayed here.
4. Review the order, then submit.

Pro tip

Always select **Residential** as the address type, regardless of the actual location. We do ship to commercial addresses but can’t currently specify that for the order. We ship to any valid US address, except PO Boxes.

The customer order will then appear on the page. You’ll also see a Delivered by date, based on your chosen ship speed. Once we start fulfilling the order, you can’t make any changes to the items, quantity or delivery address.

Notes:

Non-sort items, which are typically greater than 30 lb. in shipping weight, can only be shipped by standard (3-5 business day) speed. Your item is non-sortable if it weighs >30 lb. OR if its longest side is >25" OR if its smallest side is >14".

* * *

## Cancel orders

You can **request to cancel within 1 hour** of creating the customer order and if the status is still New. This means we haven't started fulfilling items yet. However, if that 1-hour window interferes with the delivery promise date, your cancellation request will be reviewed but cannot be guaranteed.

![](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blt1200e920a71acb87/68911b8f83b84a05d642aa13/Cancel_order_2.png?branch=us_mplearn)

Notes:

Canceling an order sends a request to the fulfillment center. However, it doesn’t guarantee cancellation if associates have already started preparing the order.

Here’s how to request a cancellation:

1. Log into Seller Center and go to the [**Multichannel Orders**](https://seller.walmart.com/wfs/multi-channel-solutions/orders) page.
2. Find the order, then select the 3 dots and choose **Cancel**.
3. Check the status. If your order is successfully canceled by the fulfillment center, the status will change to Canceled.

If any partial quantity line item within the customer order is canceled, remaining items will still be shipped..

* * *

## Track delivery

The regular Orders page does not have detailed or accurate information about non-Walmart orders. Always track fulfillment on the [**Multichannel Orders**](https://seller.walmart.com/wfs/multi-channel-solutions/orders) page through these statuses:

- **New:** You added a customer order, but we haven’t started fulfilling it yet.
- **Acknowledged:** The fulfillment center is picking and packing items for the order.
- **Shipped:** Items are on their way to the customer.
- **Delivered:** Items have arrived at the customer’s address.
- **Canceled:** You or Walmart canceled the customer order. For example, this may happen if an item is out of stock.

When the status is Shipped or Delivered, you’ll be able to view tracking information:

1. Log into Seller Center and go to the [**Multichannel Orders**](https://seller.walmart.com/wfs/multi-channel-solutions/orders) page.
2. Select a customer order and open the dropdown.
3. Check the **Tracking #** column to view the carrier and tracking number.
4. To view real-time tracking for multiple orders at a time, select **Download**.

If you don't see the **Tracking #** column, make sure to configure the columns in your table.

## Tracking availability

Tracking information availability depends on the day your shipment goes out and the shipping speed based on the following timing examples:

- **Two-day shipping example:** If you were to place an order on a Monday before the 2pm(EST) cutoff time, your shipment would arrive on Wednesday and your tracking would be available Monday or Tuesday. After the 2pm(EST) cutoff time, your shipment would arrive Thursday and tracking would be available Tuesday or Wednesday.

- **3-5 day shipping example:** If you were to place an order on a Monday before the 2pm(EST) cutoff time, your shipment would arrive on Thursday or the two business days after, and your tracking would be available Tuesday or Wednesday. After the 2pm(EST) cutoff time, your shipment would arrive Friday, or the next two business days the following week. Your tracking would be available Wednesday or Thursday.



Please note that these are estimates, and may vary. Delivery estimates are based on business days, Monday-Friday and do not include weekends or holidays. During peak (October 1-December 31), sales events and other circumstances, it may take longer for tracking numbers to appear.


![](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blt4f88b7dfa256d35a/679d490bee57676b5d899dd5/MCS_Tracking_column_on_Orders_Gif_New.gif?branch=us_mplearn)

For a more detailed, historical view, download the [Orders Report](https://seller.walmart.com/wfsLite/reports). This has a separate tab for Walmart Multichannel Solutions, including shipped date, carrier and tracking number. Tracking is updated on the report every 24 hours, compared to the real-time data on the **Multichannel Orders** page.

Notes:

Walmart Multichannel Solutions may require delivery signatures for certain regulated items, and add that requirement to your package at no cost to you.

## Frequently asked questions

* * *

What is the sales channel ID? Where do I find it?

The sales channel ID is a unique, Walmart-created code to tell channels apart. You can find it on the [**Multichannel Settings**](https://seller.walmart.com/wfs/multi-channel-solutions/sales-channels) page.

* * *

Why wasn’t I able to create a customer order?

If you couldn't add an order, there might be an error. Here are common issues:

- The SKU may be invalid, or our system didn’t recognize it. Check that you entered the SKU correctly.
- You may not have enough units to fulfill the order. Send more inventory to Walmart to restock. We recommend [checking in-stock inventory](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#checkinventory) levels before placing an order.

* * *

Why did Walmart cancel my order?

We may cancel if the item is out of stock, damaged or not available at an eligible fulfillment center. Check if [inventory is in stock](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-orders#checkinventory) on the **Inventory** page.

* * *

I canceled the order, but the order still shipped. Why?

Canceling an order sends a request to the fulfillment center. However, it doesn’t guarantee cancellation if associates have already started preparing the order.

* * *

Why can’t I view tracking information?

The order may not have shipped yet. For expedited shipping, tracking number and carrier normally appear within 1 business day. For standard shipping, they normally appear within 2 business days.

* * *

How do you handle expiring inventory?

Based on your [return rules](https://seller.walmart.com/seller-profile/return-policy), we’ll remove expiring inventory from shelves and either dispose or ship back to you. Pull dates are based on the "Minimum Days of Shelf Life from Production" value you entered during item setup. Inventory with an expiration date ships on a first-expired, first-out approach.

* * *

Do you ship to commercial addresses?

Yes. We accept valid US addresses, including commercial locations. We do not deliver to PO Boxes.

* * *

Why does the Orders page show an order total of $0?

Since the transaction happened on another eCommerce site, we can’t show the accurate order total. The Orders page focuses on customer information, so it doesn’t include fees or revenue.

To track delivery, use the [Multichannel Orders](https://seller.walmart.com/wfs/multi-channel-solutions/orders) page instead. To view fees and Walmart.com sales, go to the [Payments](https://seller.walmart.com/payments/statements/period) page.

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

###### Multichannel Solutions: Troubleshooting fulfillment

Walmart Fulfillment Services (WFS)

Learn about our policies when there’s a delay or issue with fulfilling a multichannel order.

Go to guide

Guide

###### Multichannel Solutions: Create customer returns

Walmart Fulfillment Services (WFS)

Explore how customer returns are handled for mlutichannel orders.

Go to guide

Guide

###### Multichannel Solutions: API integration

Walmart Fulfillment Services (WFS)

Automate your business for Walmart Multichannel Solutions using APIs.

Go to guide

Guide

###### Multichannel Solutions: Set up items

Walmart Fulfillment Services (WFS)

We’ll show you how to build your catalog and choose fulfillment types.

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