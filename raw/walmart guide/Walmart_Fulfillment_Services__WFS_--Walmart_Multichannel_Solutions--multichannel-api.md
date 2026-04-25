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

Multichannel Solutions: API integration

Last updated on Feb 5, 2026

Reading time: 3 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api#overview)


- [About API integration](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api#aboutapiintegration)


- [How to get started](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api#getstarted)


- [API calls for MCS](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api#apicalls)

- [Java OpenAPI client integration](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api#java)


- [Webhook](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api#webhook)


* * *

Overview

Learn more about the API calls that are unique to Walmart Multichannel Solutions (MCS) and how to integrate them with your existing tools.

![](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blt896713e327ee90bc/66c3873354be6cf971184740/Multichannel-Onboarding_Infographic.jpg?branch=us_mplearn)

## About API integration

APIs allow the seamless sharing of data between your system and ours. By integrating APIs into your existing tools, like inventory management software, you can automate routine tasks that would otherwise be done manually, such as updating inventory counts and processing orders. All documentation is available in [Developer Portal-Multichannel Solutions](https://developer.walmart.com/us-marketplace/reference/walmart-multichannel-solutions). To get started, [generate your credentials](https://developer.walmart.com/us-marketplace/docs/get-started-as-a-seller#retrieve-your-api-keys-option-one).

The Multichannel Solutions API sandbox in the developer portal provides a secure early testing environment prior to production integration. Within this environment, sellers and solution providers can test items and sales channels and even simulate customer orders throughout a fulfillment cycle. The sandbox lets you experiment and debug prior to live production safely and securely. [Find out more here.](https://developer.walmart.com/us-marketplace/docs/multichannel-solutions-sandbox)

## How to get started

Create a Walmart catalog and configure settings in Seller Center by following the steps outlined in [_Multichannel Solutions: Set up items_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-set-up-items) and [_Manage sales channels_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-sales-channels). Once you’ve onboarded, you can use APIs to automate inventory and orders.

Pro tip

We can provide consultation for API integration. Select the _Help_ button in the [Seller Center](https://seller.walmart.com/home) menu bar to contact Support, then describe your issue. You can also try [troubleshooting common integration errors](https://marketplacelearn.walmart.com/guides/Item%20setup/Troubleshooting/Troubleshooting-common-integration-errors).

### API calls for Multichannel Solutions

Some functionality will be through Marketplace and WFS APIs, but Multichannel Solutions also has these unique APIs.

|     |     |
| --- | --- |
| **Multichannel API** | **Function** |
| [Create Customer Order](https://developer.walmart.com/us-marketplace/reference/createfulfillment) | Submit customer orders. To specify which ecommerce channel, use the [sales channel ID](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-sales-channels) you added during onboarding. This will help you identify and resolve potential order creation issues upfront—aligned with error descriptions shown in Seller Center. |
| [Get WFS Inventory](https://developer.walmart.com/us-marketplace/reference/getwfsinventorydetails-1) | Check real-time inventory levels. This allows you to view total inventory levels across all channels, as well as inventory available for each channel by a particular SKU. You can query 300 SKUs at a time. <br>If the same item is distributed across your network, this API also helps you check that you have enough multichannel-eligible inventory in a WFS facility. That way, you can avoid overselling or canceling orders.<br>NOTE: [WFS inventory (Legacy)](https://developer.walmart.com/us-marketplace/reference/getwfsinventory-1) API is being deprecated and will be removed after March 03, 2026. We recommend transitioning to the new [WFS Inventory API](https://developer.walmart.com/us-marketplace/reference/getwfsinventorydetails-1). |
| [Fetch Delivery Promise](https://developer.walmart.com/us-marketplace/reference/promisefulfillments) | View the estimated delivery date. Make sure that your chosen shipping speed is appropriate for the promise. |
| [Cancel Customer Order](https://developer.walmart.com/us-marketplace/reference/cancelfulfillment) | Cancel a fulfillment request. In most cases, you can cancel within 1 hour of creating the customer order. If the fulfillment center cancels the order, you’ll get a success message on the API call.<br>_Note that canceling an order sends a request to the fulfillment center. However, it doesn’t guarantee cancellation if associates have already started preparing the order._ |
| [Get Fulfillment Order Status](https://developer.walmart.com/us-marketplace/reference/getfulfillmentordersstatus) | Track the fulfillment progress. |
| [Create Customer Return Order](https://developer.walmart.com/us-marketplace/reference/createreturnfulfillment) | Create an RMA for a delivered order. You’ll be able to generate a return shipping label. |
| [Cancel Customer Return Order](https://developer.walmart.com/us-marketplace/reference/cancelreturnfulfillment) | Cancel a previously placed return order. |
| [Create MCS Sales Channel Details](https://developer.walmart.com/us-marketplace/reference/mcsselleronboarding) | Set up a new sales channel in MCS, including channel name, ship from and return addresses, and carrier preferences. |
| [Update MCS Sales Channel Details](https://developer.walmart.com/us-marketplace/reference/updatemcsselleronboarding) | Updates the sales channel details you created for MCS, including name, ship from and return address, and carrier preferences. |
| [Retrieve MCS Sales Channel Details](https://developer.walmart.com/us-marketplace/reference/getmcssellerorderchannelids) | Retrieve MCS sales channel details. |

Notes:

To minimize the chance for customer order cancellations due to insufficient inventory or item restrictions, run the **Fetch Delivery Promise API** before running the Create Customer Order API. This will help validate that the items you want to create the order for can be fulfilled without issue.

## Java OpenAPI client integration

The Multichannel Solutions Java OpenAPI Client enables seamless connectivity between your Java-based systems and Walmart Multichannel Solutions. By using an official Walmart API specification, you can automatically generate a ready-to-use Java client and integrate it into your existing tools to handle order creation, tracking, and management without building custom connections from scratch. All required specifications and setup guidance are available in the [Developer Portal for Multichannel Solutions](https://developer.walmart.com/us-marketplace/reference/multichannel-solutions-java-openapi-client-integration-guide) to help you get started quickly.

## Webhook

We also have a webhook that will publish notifications to your endpoint URL. Whenever the status of an order or return changes, you’ll automatically get a notification. To receive notifications, you’ll need to share your endpoint URL with WFS and allow up to 1 week for us to configure it on our end.

To enable the webhook, please [subscribe to notifications](https://developer.walmart.com/api/us/mp/notifications). If you have questions, [find out more about notifications](https://developer.walmart.com/us-marketplace/docs/notifications-overview), or select the _Help_ button in the [Seller Center](https://seller.walmart.com/home) menu bar to contact Support.

Notes:

The information found within this guide, and the related hyperlinks, is for general informational purposes only, and is not considered legal advice. This guide may contain links to third party content, which Walmart does not warrant, endorse, or assume liability for and your reliance on such content is solely at your own discretion.

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

###### API integration for WFS

Walmart Fulfillment Services (WFS)

Learn how to automate your WFS business by integrating directly with APIs.

Go to guide

Guide

###### Multichannel Solutions (MCS): Overview

Getting started

Walmart Multichannel Solutions is a flexible and affordable way to fulfill customer orders from any eCommerce site.

Go to guide

Guide

###### Integrate with APIs: Overview

Getting started

In this guide, we explain APIs and how you can use them to automate and scale your business operations.

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