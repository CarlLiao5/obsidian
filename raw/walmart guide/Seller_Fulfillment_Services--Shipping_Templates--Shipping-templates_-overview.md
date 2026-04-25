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

###### Seller Fulfillment Services

###### Shipping methods

###### Fulfillment settings

###### Simplified Shipping Settings

###### Shipping Templates

Shipping Templates: Overview

Shipping Templates: Domestic or international shipping settings

Shipping Templates: Assign SKUs

Shipping Templates: Manage settings

###### Ship with Walmart

###### Order management

###### Taxes & payments

###### Policies & standards

###### Growth opportunities

###### Advertising

###### Walmart Seller appNew

Guide

Shipping Templates: Overview

Last updated on Dec 18, 2025

Reading time: 3 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-overview#overview)
- [How does it work?](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-overview#how)
- [Additional guidelines](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-overview#additional)
- [Frequently asked questions](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-overview#frequently-asked-questions)
- [Helpful resources](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-overview#helpful-resources)

* * *

Overview

Before you can start shipping your products to customers, you’ll need to set up your shipping settings and define shipping rules for each region you deliver to. You can create a Shipping Template in [Seller Center](https://seller.walmart.com/settings/shipping-profile/shipping-templates) or by using [Walmart APIs](https://developer.walmart.com/doc/us/us-mp/us-mp-settings/). In this guide, we’ll show you the different types of templates you can create.

## How does it work?

In your Shipping Template configuration, you’ll choose your preferred shipping method, regions and ship cost.

### Manual shipping settings (domestic)

If you don’t use an approved shipping carrier, you’ll need to [add your shipping settings manually](https://marketplacelearn.walmart.com/guides/Shipping%20&%20fulfillment/Shipping%20Templates/Shipping-templates:-add-settings-manually). There are several types of templates you can add:

- **Default:** Each Seller Center account has one Default Shipping Template that you can’t delete but you can customize to your shipping needs. The Default configurations will apply to your entire catalog unless you’ve created and assigned SKUs to other custom Shipping Templates. We suggest applying your longest anticipated transit time to your Default template if you intend on having multiple custom Shipping Templates to avoid your Default template overriding your custom templates.
- **Custom:** You can create up to 60 different Custom Shipping Templates for your seller-fulfilled items. If you use a third-party fulfillment provider, such as [Deliverr](https://www.flexport.com/) (also known as Flexport), you can create 30 additional templates for the items that they fulfill on your behalf. If SKUs [aren't assigned](https://marketplacelearn.walmart.com/guides/Shipping%20&%20fulfillment/Shipping%20Templates/Shipping-templates:-Assign-SKUs) to a Custom Shipping Template, the items will reflect the settings set in the Default Shipping Template. This includes transit times, delivery estimates and shipping cost rules.

- **Paid Standard:** Use the **Paid Standard Shipping Template** for items that don’t qualify for free standard shipping. You’ll also use this template if you need to disable Value shipping. To set up this template, choose the _Set up special template_ link on the [**Shipping Templates**](https://seller.walmart.com/settings/shipping-profile/shipping-templates) page and choose _Paid Standard Template_. After setting up the paid template, you'll need to assign which SKUs will be linked to the newly created Paid Standard Template.

- **Freight:** Use the **Freight Shipping Template** for domestically shipping large and bulky items that require less-than-truckload (LTL). An item qualifies for freight if it falls within a designated freight category or if its shipping weight exceeds 150 pounds. If you attempt to add an item to the template that doesn't qualify, the non-qualifying SKU will remain on the previously assigned template. Once the template is set up, choose a transit time from six to 10 days.



To set up this template, choose the  _Set up special template_ link on the [**Shipping Templates**](https://seller.walmart.com/settings/shipping-profile/shipping-templates) page and choose _Freight Template_.


### International shipping settings

- **International:** Use the **International Shipping Template** for items that are shipped from China, Hong Kong or India. The International Shipping Template allows you to configure longer transit times up to 13 days.

## Additional guidelines

Once you determine the right Shipping Template for your business, you’ll set up the template in Seller Center and assign SKUs to your template. Learn more below:

| Feature | Get started |
| --- | --- |
| **Add shipping settings** | Learn how to create a Shipping Template for domestic or international shipping settings. To get started, visit [_Shipping Templates: Domestic or international shipping settings_](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-add-settings-manually). |
| **Assign SKUs to templates** | After creating a Shipping Template, you’ll need to assign SKUs to it. To get started, check out [_Shipping Templates: Assign SKUs_](https://marketplacelearn.walmart.com/guides/Shipping%20&%20fulfillment/Shipping%20Templates/Shipping-templates:-Assign-SKUs). |
| **Update shipping settings** | Modify your Shipping Templates if you need to make updates or changes to your shipping settings. To get started, visit [_Shipping Templates: Manage settings_](https://marketplacelearn.walmart.com/guides/Seller%20Fulfillment%20Services/Shipping%20Templates/Shipping-templates:-manage-settings) _._ |

Notes:

Only international templates should be used to manage international shipping. Similarly, an International Shipping Template can’t be applied to an item located in a U.S. fulfillment center.

## Frequently asked questions

* * *

What do I do after I create a Shipping Template?

If you’re manually setting up the template, you’ll need to assign SKUs to a fulfillment center and a Shipping Template. After creating a new template, you must wait a minimum of four hours before assigning SKUs. If you don’t wait the required time, your shipping settings will revert to the Default Shipping Template and the desired template you created won’t be activated.

* * *

How do I remove SKUs from Value shipping?

To remove SKUs from Value Shipping, you must create a Paid Standard Shipping Template. After creating the template, you must wait four hours and then add the SKUs to the Paid Standard Shipping Template. This will remove the SKUs from the Value Shipping Template and add them to the Paid Standard Template.

* * *

Why don’t my customer-facing delivery estimates match my assigned Shipping Template settings?

In many cases, Walmart adjusts customer-facing delivery estimates based on historical shipping carrier performance, seller performance and external factors.

* * *

How can I confirm which template my SKUs are assigned to?

If you want to confirm which template each of your SKUs are assigned to you can pull a shipping and configuration report from your [**Reports**](https://seller.walmart.com/analytics/reports) center  in Seller Center.

* * *

Why am I unable to edit the shipping cost for my template?

You’re limited to one change per hour for each template. You can make up to 10 edits per day. If you exceed this limit, your Shipping Template will be locked for 24 hours.

* * *

## Helpful resources

Shipping Templates: Overview from Walmart Inc. on Vimeo

![video thumbnail](https://i.vimeocdn.com/video/2109819772-6b60b351c4820c173a2a0d0c510b99bbf0645b7c8e3d9194b6a249cf05f348b2-d?mw=80&q=85)

Playing in picture-in-picture

Play

Introduction00:00

01:26

CC/subtitlesSettingsTranscript

QualityAuto

SpeedNormal

CC/subtitlesOff

Chapters

Introduction

00:00

Copy link

Overview

00:07

Copy link

Benefits of Shipping Templates

00:24

Copy link

How to configure your settings

00:35

Copy link

Manual configuration of templates

01:00

Copy link

Keep learning

01:20

Copy link

Picture-in-PictureFullscreen

;

#### Tell us what you think

* * *

More in Seller Fulfillment Services

Guide

###### Shipping & Fulfillment Policy

Seller Fulfillment Services

In this guide, you'll learn more about the requirements of the shipping and fulfillment policy, along with additional guidelines.

Go to guide

Guide

###### Shipping methods: Overview

Seller Fulfillment Services

As a Marketplace seller, you have five shipping method options to ship orders to customers: Value, Standard, TwoDay, OneDay or Freight shipping.

Go to guide

Guide

###### Shipping methods: Parcel shipping carriers

Seller Fulfillment Services

In this guide,&nbsp;you’ll learn&nbsp;more&nbsp;about&nbsp;Walmart-approved&nbsp;carriers&nbsp;that you can&nbsp;use for parcel delivery.

Go to guide

Related guides

Guide

###### Shipping Templates: Assign SKUs

Seller Fulfillment Services

In this guide, we’ll show you how to assign SKUs to your Shipping Template.

Go to guide

Guide

###### Shipping Templates: Domestic or international shipping settings

Seller Fulfillment Services

In this guide, you'll learn how to add domestic and international shipping settings using Shipping Templates in Seller Center..

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