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

###### Troubleshooting

Troubleshoot WFS item template errors

Troubleshoot WFS shipping plan issues

Troubleshoot WFS shipments with receiving issues

Troubleshoot WFS receiving issues: Request an investigation

Troubleshoot Walmart-fulfilled orders switching to seller-fulfilled

Troubleshoot rejected or returned WFS inventory

WFS returns overview

WFS customer returns reimbursement and dispute processes

###### Seller Fulfillment Services

###### Order management

###### Taxes & payments

###### Policies & standards

###### Growth opportunities

###### Advertising

###### Walmart Seller appNew

Guide

Troubleshoot WFS shipping plan issues

Last updated on Jul 21, 2025

Reading time: 3 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-WFS-inbound-order-issues#overview)
- [Errors and next steps](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-WFS-inbound-order-issues#errors)

* * *

Overview

When you send inventory to Walmart Fulfillment Services (WFS), there might be issues with your shipping plan. This could be due to incorrect information or a system error. In this guide, learn about common errors and ways to fix them. If you still can’t solve the issue, please contact Support by selecting the _Help_ button in the [Seller Center](https://seller.walmart.com/home) menu bar.

## Errors and next steps

This table lists the most common errors for shipping plans and how to fix them. Some will only apply if you’re using the template to add multiple items at a time or if you're directly integrated with our APIs.

| Error message | Next steps |
| --- | --- |
| Expected Delivery Date should be of future and not the past | Make sure the estimated ship date is at least 2 days from now. |
| expectedDeliveryDate cannot be null/empty | Enter an estimated ship date that’s at least 2 days from today. |
| itemQty should be product of innerPackQty and vendorPackQty | Check that item quantity, vendor pack quantity and inner pack quantity are at least 1. The item quantity should equal the vendor pack quantity multiplied by the inner pack quantity. |
| postalCode cannot be null/empty | Enter a valid zip code. |
| Shipment Plan is already created for this inbound order | This shipping plan ID already exists. Please enter a new one. |
| innerPackQty should be great then zero | The inner pack quantity must be at least 1. |
| vendorPackQty should be great then zero | The vendor pack quantity must be at least 1. |
| itemQty should be great then zero | The item quantity must be at least 1. |
| sellerId and inboundOrderId is mandatory | The shipping plan is missing your seller ID and plan ID. |
| addressLine1 is invalid. enter valid addressLine1 String in english language characters | Make sure the address is in English. |
| Error parsing json input | The template is missing required rows or columns. Please download a new template and resubmit. |
| Items Dimensions are not suitable for creating po for sku | Your item is larger than the maximum dimensions for WFS. We allow items up to 120″ x 105″ x 93″ and 500 lb, including packaging. |
| OrderItem in create Shipment request is repeated more than once | Make sure items are only entered once. If there are duplicate rows, please combine them. |
| productType is invalid | Select a product ID type from the dropdown. GTIN is the only option for the template. |
| productId with productType GTIN should be 14 digit | Check that the GTIN is 14 digits. If your GTIN is shorter than 14 digits, add leading zeros in front. |
| Product ID with Product Type UPC should be 12 digit | Check that the UPC is 12 digits. |
| Item is not WFS Eligible for sku | The item may be prohibited. Please check the [_WFS prohibited products policy_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20item%20setup/wfs-prohibited-products-policy). |
| inboundOrderId is invalid. enter valid inboundOrderId String in english language and without '?','/','\|','\\','+','#' characters | The shipping plan ID is invalid. Check that it uses only English letters, numbers or these special characters: -, \_ |
| Item information is not present for sku, Please set it up as Walmart Fulfilled item in the Seller Center. | Your item may not be set up as Walmart-fulfilled. No matter what the fulfillment type is, please try converting the item again. <br>You must convert using a template. The other item setup methods won’t work in this case. Please follow the steps in [_Convert seller-fulfilled items to WFS_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20item%20setup/Convert-seller-fulfilled-items-to-WFS#multipleitems). |
| itemDesc length cannot be greater than 450 chars | Check that the item description is shorter than 450 characters. |
| itemDesc cannot be null/empty | Enter an item description. |
| addressLine1 cannot be null/empty | Enter a valid address. |
| countryCode cannot be null/empty | Enter a valid country code. |
| stateCode code cannot be more then 10 chars | Check that the state code is 2 letters only. |
| city is invalid. enter valid city String in english language characters | Make sure the city is correct and in English. |
| postalCode is invalid .enter valid postalCode | Make sure the zip code is correct. |
| number of items should be more then one and less then five thousand | Confirm that your shipping plan has between 1 and 5,000 items. If you want to send more than 5,000 items, please create a second shipping plan. |

### Template errors report

If you submitted a template, our system will automatically check it and create an error report that will appear in a pop-up window. Select _Download errors_ to download the error report. Then make changes and resubmit the template.

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

###### WFS shipping plans: Send domestic inventory

Walmart Fulfillment Services (WFS)

Learn how to create a WFS shipping plan, pack shipments and track progress.

Go to guide

Guide

###### Troubleshoot WFS receiving issues: Request an investigation

Walmart Fulfillment Services (WFS)

If you’re experiencing discrepancies with your inbound inventory, you can create a dispute claim.

Go to guide

Guide

###### WFS shipping plans: Receiving

Walmart Fulfillment Services (WFS)

Learn what the WFS receiving process is like, how long it takes and how to manage issues along the way.

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

Accessible challenge