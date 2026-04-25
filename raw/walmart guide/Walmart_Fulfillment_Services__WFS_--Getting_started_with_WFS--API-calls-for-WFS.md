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

WFS seller onboarding and setup

API integration for WFS

WFS settings: Add contact information

WFS settings: Add billing information

WFS settings: Customize return rules

WFS international sellers

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

###### Seller Fulfillment Services

###### Order management

###### Taxes & payments

###### Policies & standards

###### Growth opportunities

###### Advertising

###### Walmart Seller appNew

Guide

API integration for WFS

Last updated on Jan 19, 2026

Reading time: 4 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Getting%20started%20with%20WFS/API-calls-for-WFS#overview)
- [How does it work?](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Getting%20started%20with%20WFS/API-calls-for-WFS#howdoesitwork)
- [Optimize your business with recommendations APIs](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Getting%20started%20with%20WFS/API-calls-for-WFS#recommendationsAPIs)
- [Solution providers](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Getting%20started%20with%20WFS/API-calls-for-WFS#solutionproviders)
- [Get help](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Getting%20started%20with%20WFS/API-calls-for-WFS#gethelp) [​​​​​​​](https://sellerhelp.walmart.com/s/guide?article=000009385&language=en_US#FAQ)
- [Frequently asked questions](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Getting%20started%20with%20WFS/API-calls-for-WFS#frequently-asked-questions)

* * *

Overview

Learn how to automate your Walmart Fulfillment Services (WFS) business by integrating directly with APIs. As an alternative to Seller Center, you can use APIs to convert items, manage inventory, submit inbound orders and more. Explore all APIs and documentation in the [Developer Portal](https://developer.walmart.com/us-marketplace).

## How does it work?

Walmart Marketplace APIs create a seamless data exchange between your system and ours. To get started, you need a Client ID and a Client Secret to access the APIs. You’ll need these credentials to generate a token for every API call. Go to the [Getting started guide for sellers](https://developer.walmart.com/us-marketplace/docs/get-started-as-a-seller) to learn how.

In [Developer Portal](https://developer.walmart.com/us-marketplace), you’ll see all available APIs and reference guides. You can manage almost every part of your business through APIs, including:

- Add or convert items in your catalog
- Check if items are on hold due to hazardous materials
- View or update current inventory
- Create shipping plans to send inventory
- Get a recommended item quantity for a shipment
- Get payment and inventory health reports

Some functionality will be through Marketplace APIs (such as **GET All orders**), and other functionality will be through WFS APIs (such as **POST Convert items for WFS**). For WFS-specific actions, look for Walmart Fulfillment Services in the left-hand menu, or search for actions.

Notes:

You may still need to do some actions in Seller Center. For example, Walmart Preferred Carrier quotes are not available for full truckload (FTL) via API.

## Optimize your business with recommendations APIs

Once you're integrated with WFS, you can use our recommendations APIs to determine the best ways to minimize costs and maximize sales potential:

- [Restock recommendations](https://developer.walmart.com/us-marketplace/docs/get-wfs-restock-recommendations): Use this API call to get suggestions for the items you should restock with WFS based on your current inventory and forecasted sales demand.
- [Fulfill with WFS recommendations](https://developer.walmart.com/us-marketplace/docs/get-wfs-convert-recommendations): Use this API call to pull a list of the seller-fulfilled items in your catalog that are likely to perform best when fulfilled by WFS instead.
- [Unpublished recommendations](https://developer.walmart.com/us-marketplace/docs/get-wfs-unpublished-recommendations): This API call shows you your current unpublished WFS items, why they're unpublished, and how it may impact your business.

## Solution providers

A solution provider is a third-party company in the Walmart network that provides specialized services to help you run your business. For example, they can help you with item management, inventory, pricing and more. Each integration is tailored to your specific needs, so reach out to an [approved solution provider](https://marketplace.walmart.com/solutions-providers/) to learn about costs, features and capabilities. You can also use multiple solution providers to manage different parts of your business.

Here are solution providers that are tailored to WFS:

| Type | Services | Solution provider |
| --- | --- | --- |
| Full service | Item setup and management, inventory, order fulfillment, pricing and more | - [ChannelEngine](https://www.channelengine.com/channels/online-marketplaces/walmart/)<br>- [Rithum](https://www.channeladvisor.com/)<br>- [Sellercloud](https://sellercloud.com/) |
| Specialty | Management of specific business functionalities rather than a full suite | - GeekSeller <br>- Zentail |

To give an approved solution provider access to your Marketplace data, [connect them](https://marketplacelearn.walmart.com/guides/Getting%20started/Getting%20ready%20to%20sell/connect-a-solution-provider-in-seller-center) from the **Apps** page in Seller Center.

Pro tip

If you’re using Multichannel Solutions, learn more about which [APIs and solution providers](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Walmart%20Multichannel%20Solutions/multichannel-api) we offer for the program.

## Get help

If you have any trouble setting up APIs or solution providers, contact Support. Select the _Help_ button in the [Seller Center](http://seller.walmart.com/) menu bar, then describe your issue.

If you’re having issues with adding items, creating a shipping plan or checking customer orders, check out these guides for common errors and how to solve them:

- [_Troubleshooting common integration errors_](https://marketplacelearn.walmart.com/guides/Item%20setup/Troubleshooting/Troubleshooting-common-integration-errors)
- [_Troubleshoot WFS item feed errors_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-item-feed-errors)
- [_Troubleshoot WFS shipping plan issues_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-WFS-inbound-order-issues)

## Frequently asked questions

* * *

How do I start integrating with APIs?

Log into Developer Portal and follow the [Getting started guide for sellers](https://developer.walmart.com/us-marketplace/docs/direct-sellers) _._ This guide explains how to access and authenticate APIs, as well as links to sandboxes where you can test the API calls. If you need more help, select the _Help_ button in the [Seller Center](http://seller.walmart.com/) menu bar to contact Support.

* * *

Can I use APIs to view WFS orders?

Yes. By default, **GET All orders** retrieves only customer orders that you fulfill _(SellerFulfilled_) _._ To get WFS orders, set the _shipNodeType_ to _WFSFulfilled_ instead.

* * *

How do I report an issue with data I receive from an API?

Select the _Help_ button in the [Seller Center](http://seller.walmart.com/) menu bar to contact Support. Please include the name of the API and call details, as well as the error or issue you're having.

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

###### Integrate with APIs: Overview

Getting started

In this guide, we explain APIs and how you can use them to automate and scale your business operations.

Go to guide

Guide

###### Connect an approved Solution Provider in Seller Center

Getting started

If you work with a Solution Provider to manage your Walmart Marketplace business, you can set up your Solution Provider integration through the App Store in Seller Center. In this guide, we’ll show you how to do it.

Go to guide

Guide

###### Multichannel Solutions: API integration

Walmart Fulfillment Services (WFS)

Automate your business for Walmart Multichannel Solutions using APIs.

Go to guide

Guide

###### Troubleshoot common integration errors

Getting started

This guide outlines common integration errors you may encounter when working with Walmart APIs or approved Solution Providers.

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