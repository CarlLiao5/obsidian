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

Troubleshoot WFS item template errors

Last updated on Aug 13, 2025

Reading time: 3 min

* * *

In this guide:

- [Overview](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-item-feed-errors#overview)
- [Track status](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-item-feed-errors#trackstatus)
- [Common error messages](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-item-feed-errors#commonerrors)
- [Formatting issues](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-item-feed-errors#formatting)
- [Frequently asked questions](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/Troubleshooting/Troubleshoot-item-feed-errors#frequently-asked-questions)

* * *

Overview

To use Walmart Fulfillment Services (WFS), you can add or convert several items at once using the [Full Setup template](https://marketplacelearn.walmart.com/guides/Item%20setup/Item%20setup%20methods/Add-items-in-bulk:-full-setup). If your items haven’t been published after 24 hours, there may be issues. In this guide, learn how to find and fix WFS errors in your template.

## Track status

After submitting a template, track the status in the [**Activity Feed**](https://seller.walmart.com/items-and-inventory/feed-status) page. You can filter by feed type or date created to find a specific submission. If there are any errors blocking item setup, select the number in the _Errors_ column to review or download a report from the _Error report_ column. Then make changes and resubmit the items or template.

If you download the report, it highlights rows with errors and describes the reasons. Correct the errors in the report itself, then reupload it in the [Spreadsheet setup](https://seller.walmart.com/catalog/add-items/bulk?returnPATH=%2Fcatalog%2Fadd-items) page. Track the status again in the Activity Feed to make sure the errors have been fixed.

![](https://azure-na-images.contentstack.com/v3/assets/blta7903c6b840b702d/blt55cec588ef974dc8/65004e67066da0000df61113/9238_Feed_Status_Error.jpeg?branch=us_mplearn)

Make sure to also check the [**Pending Review**](https://seller.walmart.com/catalog/pending-review) page for errors. If your items have hazardous materials, they may be put on hold for up to 3 business days for a [compliance review](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20item%20setup/WFS-hazmat-item-setup%22%20/l%20%22ComplianceReview).

## Common error messages

| Error message | Next steps |
| ‘Each’ pack config is required. | Go to the _Trade Item Configurations_ tab of the template. Then add the width, height, depth and weight of the item, including any packaging. |
| \`Product is or Contains this Battery Type\` is a required attribute. Enter value for the attribute \`Product is or Contains this Battery Type\`. | Go to the _Product Content and Site Exp_ tab of the template. If your item is or contains a battery, select the type from the dropdown list. You can find this information on the battery, its packaging or within a [Safety Data Sheet](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20item%20setup/WFS-compliance-safety-data-sheets?locale=en-US).<br>If your item doesn't have a battery, choose "Does Not Contain a Battery." |
| ‘Country of Origin’ is a required attribute. Enter value for the attribute ‘Country of Origin.’ | Go to the _Trade Item Configurations_ tab of the template. From the dropdown list, select the country where the item was manufactured.<br>If the item was made in multiple countries, you can insert another column. Copy the cells in rows 4–6 and paste them into the corresponding new cells. |
| ‘Selling Price’ is a required attribute. Enter value for the attribute ‘Selling Price.’ | Go to the _Product Content and Site Exp_ tab of the template. Add the price that the customer pays for the item. Do not include commas or currency symbols. |
| Under hazmat review. Item will be on-hold for up to 48 business hours while review process takes place. Please use Seller Center ‘Pending Review’ page for status tracking. | Your item may contain a chemical, aerosol, pesticide or battery. The compliance team will put the item on hold to review, which can take up to 3 business days. Track the status on the [**Pending Review**](https://seller.walmart.com/catalog/pending-review) page or [Hazmat Items On Hold API](https://developer.walmart.com/us-marketplace/reference/wercsfeedback). <br>Learn more about the compliance review at [_WFS hazardous materials: Item setup_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20item%20setup/WFS-hazmat-item-setup). |
| ‘Unit’ is a required attribute. Enter value for the attribute ‘Unit.’ | For certain fields, you must specify the unit of measurement.<br>Go to the _Product Content and Site Exp_ tab of the template. Look for fields that ask about measurement, like Net Content, Assembled Product Width and Assembled Product Length. In the corresponding column, choose a unit from the dropdown list. |
| ‘Main Image URL' does not meet our image URL requirements. For more details, visit: https://sellerhelp.walmart.com/s/guide?article=000009378&language=en\_US#filetyperequirements | Go to the _Product Content and Site Exp_ tab of the template. Add a link to the main image of your item. It should be publicly accessible and end in an image file type (.jpg, .png, etc).<br>For all URL requirements, visit [_Image guidelines and requirements_](https://marketplacelearn.walmart.com/guides/Item%20setup/Item%20content%2C%20imagery%2C%20and%20media/Product-detail-page:-Image-guidelines-&-requirements). |
| It looks like there was a glitch on our end. Please try again. If the problem persists, contact Walmart Partner Support. | Try uploading your items again. If the issue continues, contact Support by selecting the _Help_ button in the [Seller Center](https://seller.walmart.com/home) menu bar. |
| You cannot use this SKU because it was previously used with a different GTIN. You had created a SKU with this ID and later changed it to another ID. This SKU is being used as a reference ID for previously created SKU in your catalog. Please setup the item with a unique SKU ID. For more details, review this Help article: https://sellerhelp.walmart.com/s/guide?article=000007896 | The SKU is already being used by another item. Please use another SKU that’s unique.<br>Go to the _Product Content and Site Exp_ tab of the template. Then update the first column with a new SKU. |
| ‘State Restrictions’ is a required attribute. Enter value for the attribute ‘State Restrictions.’ | State restrictions mean your item cannot be sold in certain regions, due to legal or supplier reasons.<br>Go to the _Product Content and Site Exp_ tab of the template. Look for the State Restrictions fields. If your item has state restrictions, select the reason from the dropdown list. Then add the states or zip codes where the item can’t be sold.<br>If your item doesn’t have any restrictions, select “None.” |

If you can’t fix errors on your own, please contact Support by selecting the _Help_ button in the [Seller Center](https://seller.walmart.com/home) menu bar. Make sure to include this information:

- Impacted GTINs or UPCs
- Feed ID

## Formatting issues

If your items still aren’t going through, check for these formatting errors in your template. They may cause our system to read the file incorrectly.

- Make sure the order of SKUs is the same in both the product content and trade item configuration tabs.
- Some cells in the template have dropdown lists. Make sure to choose from the list. Do not paste or type into these cells, which may lead to errors.
- If you need to copy data from another source, only paste the values and not the formatting. You can do this by right-clicking to open _Paste Special_ and selecting _Values_.
- Do not put “N/A” in any fields. You can just skip the field and leave it blank if it's not required.
- Avoid special characters, like slashes and asterisks. the slash in "N/A."

## Frequently asked questions

* * *

How are Walmart-fulfilled errors different from seller-fulfilled?

When you use WFS, we require additional information to safely store and handle your items. This includes country of origin, dimensions and hazardous materials. During item setup, you may encounter errors that are specific to those WFS fields.

To learn more, review these guides:

- [_WFS trade item configuration_](https://marketplacelearn.walmart.com/guides/Getting%20started/Walmart%20Fulfillment%20Services%20(WFS)/WFS-trade-item-configuration)
- [_WFS hazardous materials: Item setup_](https://marketplacelearn.walmart.com/guides/Walmart%20Fulfillment%20Services%20(WFS)/WFS%20item%20setup/WFS-hazmat-item-setup)

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

###### Item template for WFS

Walmart Fulfillment Services (WFS)

Learn what’s in the full setup template and how to fill it out for Walmart-fulfilled items.

Go to guide

Guide

###### WFS hazardous materials (hazmat): Overview

Walmart Fulfillment Services (WFS)

If you use Walmart Fulfillment Services (WFS) to fulfill items, you must declare hazardous materials during item setup.

Go to guide

Guide

###### Add multiple items: Full setup

Item setup

In this guide, we’ll show you how to use the Full Setup template to add several items to your Marketplace catalog at once.

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