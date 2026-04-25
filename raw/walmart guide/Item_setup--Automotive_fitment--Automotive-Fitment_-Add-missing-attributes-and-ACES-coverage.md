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

###### Item setup methods

###### Item content, imagery, and media

###### Variant management

###### Resold

###### Automotive fitment

Automotive fitment: Overview

Troubleshoot automotive fitment errors

Automotive fitment: Add missing attributes and ACES coverage

###### Troubleshooting

###### Catalog management

###### Walmart Fulfillment Services (WFS)

###### Seller Fulfillment Services

###### Order management

###### Taxes & payments

###### Policies & standards

###### Growth opportunities

###### Advertising

###### Walmart Seller appNew

Guide

Automotive fitment: Add missing attributes and ACES coverage

Last updated on Oct 5, 2025

Reading time: 7 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Item%20setup/Automotive%20fitment/Automotive-Fitment:-Add-missing-attributes-and-ACES-coverage#overview)
- [Add missing attributes and ACES coverage](https://marketplacelearn.walmart.com/guides/Item%20setup/Automotive%20fitment/Automotive-Fitment:-Add-missing-attributes-and-ACES-coverage#add)
- [Frequently asked questions](https://marketplacelearn.walmart.com/guides/Item%20setup/Automotive%20fitment/Automotive-Fitment:-Add-missing-attributes-and-ACES-coverage#frequently-asked-questions)

* * *

Overview

To help ensure your listings appear when shoppers use the [Auto Parts Fitment widget](https://www.walmart.com/search?q=auto+filters) on Walmart.com, you need an Aftermarket Catalog Exchange Standard (ACES) record on file.  In this guide, you'll learn how to update missing fitment attributes and provide ACES vehicle compatibility data.

## Add missing attributes and ACES coverage

### Step 1 – Get started

If you haven’t already, you’ll need to set up your automotive listings on Walmart Marketplace. Review [this guide](https://marketplacelearn.walmart.com/guides/Getting%20started/Getting%20ready%20to%20sell/Item-setup-methods:-Overview) for more information on how to set up your catalog.

### Step 2 – Update fitment attributes

The AAIA Brand ID, Manufacturer Part Number and Part Terminology ID attributes must be updated for fitment to be enabled.

In Seller Center, select _Update items._ On the **Update items in bulk GTINs** screen, select your fulfillment type and choose _By GTIN Match_. Add your item’s GTINs inside the box and selec _t Match._ Choose the **Download** button to download your template. Now you’re ready to update your items and ensure they’re compatible with fitment requirements.

Pro tip

If you’re a reseller, Walmart can confirm if you have corresponding ACES records on file for your items directly from the manufacturer when you update your items with the appropriate attributes.

Notes:

If you’re an API seller or work with a Solution Provider, make sure your content feeds have mapping turned on for the three fitment attributes listed above.

In the template, you must update the Part Terminology ID, Manufacturer Part Number and AAIA Brand ID. To gather this information, refer to your Product Information Exchange Standard (PIES) file. If you don’t have a PIES file, reference the following to locate the details:

- AAIA brand ID (BrandAAIAID): The header of your ACES file


- Manufacturer Part Number (Part): In each record in the ACES file


- Part Terminology ID (PartType id): In each record in the ACES file


When you’re ready, re-upload the template back into Seller Center. It must have the exact format and title as it did when it was downloaded.  Alternatively, you can submit the PIES file and the template details will flow to the related Walmart item attributes. Confirm the attributes were updated after submitting the PIES file.

Notes:

If you've submitted a record for the item and it appears on the report, confirm that the values tagged for the fitment attributes match the values in the corresponding ACES, XML or ACES Excel.

Pro tip

You can generate a **Fitment missing attributes** report to ensure you’ve completed all steps correctly by navigating to your [**Catalog**](https://seller.walmart.com/catalog/list-items) in Seller Center and choosing _Download view_. Select _go to reports page_ to download the report. Blank cells mean the attribute is missing information.

#### Additional guidelines for light bulbs

If your light bulb has multiple Part Type Applications, use PTID 11718 for Multi-Purpose Light Bulbs to tag the item Part Terminology ID. Provide multiple individual ACES records for each specific Part Terminology ID (PartType id) that the bulb is compatible with.

Pro tip

Don’t use the Multi-Purpose Light Bulb PTID in the ACES records; only use it to tag the Part Terminology ID Item attribute in the file. Any ACES records that use multipurpose PTID 11718 will be rejected.

### Step 3 – Upload files

Before submitting your files, make sure each file adheres to our [file requirements](https://azure-na-assets.contentstack.com/v3/assets/blta7903c6b840b702d/blt6c2fd56f6019e9e4/Automotive-Fitment-file-requirements.pdf?branch=us_mplearn) to avoid errors during the uploading process. Once you've created your ACES or PIES files using the information found in the reports, you'll upload them into Seller Center or via [Walmart APIs](https://developer.walmart.com/).

If you don’t have an ACES standard XML file, you can use this [Excel template](https://azure-na-assets.contentstack.com/v3/assets/blta7903c6b840b702d/blta1be4d5dc1e941cf/66291ae0f258a8000afb20b8/AcesTestFileExcelNewHeader.xlsx) alternative.

There are two ways to upload your ACES and PIES files. You can use the [Fitment landing page](https://seller.walmart.com/items-and-inventory/fitment-update), or you can navigate to your [**Catalog**](https://seller.walmart.com/catalog/list-items) in Seller Center. Select the checkbox next to the items you wish to update and select _Update fitment info_ from the Manage items dropdown menu. Then choose your preferred file type and upload your file.

Pro tip

You can generate a **Fitment ACES Coverage Report** to ensure that your uploads have been processed by navigating to your [**Catalog**](https://seller.walmart.com/catalog/list-items) in Seller Center and choosing _Download view_. Select _go to reports page_ to download the report. Blank cells mean the item is missing a corresponding ACES record.

## Frequently asked questions

* * *

As a brand owner how do I register and get an AAIA Brand ID?

Follow the instructions for how to register and get an AAIA Brand ID directly from the Auto Care Association [here.](https://digital.autocare.org/data-standards-documentation/)

* * *

How will I know if my attributes updated successfully?

In the [**Catalog**](https://seller.walmart.com/catalog/list-items) page in Seller Center, you can view your fitment product details and filter by **Fitment Fit Type** or **Fitment Attributes** to check if items may be missing information or have been updated. Once you update the fitment attributes or upload a PIES file, you'll be able to identify the Brand AAIA, Manufacturing Part Number, and Part Terminology ID for your products.

* * *

How can I add new items to my catalog?

When adding new items via your preferred item setup method, be sure to fill in the Brand AAIA, Manufacturing Part Number, Part Terminology ID and Fit Type. As a reminder, these fitment attributes can be found on the [Auto Care Association’s website](https://digital.autocare.org/data-standards-documentation/). For more information on how to set up new items, visit [_Item setup methods_.](https://marketplacelearn.walmart.com/guides/Getting%20started/Getting%20ready%20to%20sell/Item-setup-methods:-Overview)

* * *

Why are some cells blank in the Fitment Missing ACES Report and the Fitment Missing Attributes Report?

Blank cells indicate where your products are missing ACES coverage or fitment required attributes.  The **Fitment Missing ACES Report** lists all items that don’t have ACES Coverage. The report only pulls items that have the AAIA Brand ID, Part Terminology ID and Manufacturer Part Number attributes tagged. If those three attributes are not tagged, the ACES report will not run for that item. The **Fitment Missing Attributes Report** lists all items that have one or more fitment attributes missing.

Notes

For fitment to enable, the three fitment attributes tagged on the item need to exactly match the record on your ACES upload.

* * *

What should I update within the template?

- **Brand AAIA**: A four-letter code mapped to a brand name provided by the Auto Care Association. Visit the [Auto Care Association’s website](https://digital.autocare.org/data-standards-documentation/) to find your product’s Brand code.
- **Manufacturing Part Number:** A unique identifier set by the product's manufacturer or brand owner.
- **Part Terminology ID**: This is the primary key and identifier of each record. Visit the [Auto Care Association’s website](https://digital.autocare.org/data-standards-documentation/) to find your product’s Part Terminology ID.

* * *

I updated my fitment attributes and provided ACES records for my items but they still appear on the Fitment Missing ACES Report. Why?

It’s likely that one or more of the attributes tagged to your items doesn’t match the ACES record on file. (e.g., The Manufacturer Part Number attribute tagged to the item doesn’t match the Manufacturer Part Number in the ACES file (“Part” in ACES file). The Part Terminology ID, AAIA Brand ID and Manufacturer Part number tagged to the item must match the ACES file exactly for fitment to be enabled including spaces, hyphens, underscores, etc.

There may be competing sources submitting attribute updates and ACES records. If you’rea brand owner, register your brand in the Brand Portal to gain more control over your content. Be sure to include your AAIA brand code in your submission.

* * *

Why are there items in the report that I’ve previously entered information for?

All items that populate in the report are missing an ACES record. If you’ve submitted a record for the item and it appears on the report, confirm that the values tagged for the fitment attributes match the values in the corresponding ACES xml or ACES Excel exactly.

* * *

Some of my attribute updates aren’t showing after I uploaded my file.

You may not always define which content will be displayed on a product page if there are multiple sellers providing content for the same item. Walmart determines the best available content for items unless it is provided by a brand owner or authorized reseller.

* * *

What should I do if I received an error?

Review [this guide](https://marketplacelearn.walmart.com/guides/Item%20setup/Troubleshooting/troubleshoot-automotive-fitment-errors) on troubleshooting automotive fitment errors for help.

* * *

What should I do if I’ve followed all the instructions but still have an issue?

If you still have questions, select the _Help_ button in the [Seller Center](https://seller.walmart.com/home) menu bar to contact Support.

Notes

As a reminder and consistent with your commitment under the Marketplace Retailer Agreement, by using the Auto Parts Fitment Widget, you're affirming that all information you're providing is accurate, complies with the law and that you have the right to provide the information.

* * *

#### Tell us what you think

* * *

More in Item setup

Guide

###### Item setup methods: Overview

Item setup

This guide gives a high-level overview to start to build your product listings on Walmart Marketplace.

Go to guide

Guide

###### Add multiple items: Express setup

Item setup

This guide shows you how to add a new item to your catalog by searching products that are currently listed on Walmart.com. If you’re adding a new item to your catalog that’s not currently offered on Walmart, review Add a single item: Full setup.

Go to guide

Guide

###### Add multiple items: Match Walmart’s catalog

Item setup

In this guide, you’ll learn how to add multiple items to your catalog in Seller Center by matching them to products that are currently listed on Walmart.com.

Go to guide

Related guides

Guide

###### Item setup methods: Overview

Getting started

This guide gives a high-level overview to start to build your product listings on Walmart Marketplace.

Go to guide

Guide

###### Data Standards Document

External URL

Data Standards Document

Read more

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