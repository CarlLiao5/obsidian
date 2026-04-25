---
title: "Knowledge Base"
source: "https://advertisinghelp.walmart.com/s/guides?language=en_US&channel=Sponsored+Products&article=000009792"
author:
published:
created: 2026-04-13
description:
tags:
  - "clippings"
---
Loading

Loading

Loading

Loading

Sponsored Products

Loading

Loading

  
  
This article provides an overview of automated rules which help you create automated notifications and optimizations for your campaigns.

Here's a short video on creating and managing automated rules:  

<iframe frameborder="1" width="840" height="473" allowfullscreen="allowfullscreen" src="https://player.vimeo.com/video/781652040?h=6c875c4649&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" title="Introduction to Creating and Managing Automated Rules"></iframe>

## Table of contents

<table><tbody><tr><td colspan="1" rowspan="1"><a href="#automated_rules">About Automated rules</a><br><a href="#create_automated_rules">Create Automated rules</a><br><a href="#email_notifications">Email Notifications</a></td><td colspan="1" rowspan="1"><a href="#rule_results_and_history">Rule results and history</a><br><a href="#best_practices">Best practices</a><br></td></tr></tbody></table>

## About Automated rules

Automated Rules allow you to monitor your in-flight campaigns and make immediate budget and bid adjustments without being actively in the Walmart Connect Ad Center platform. Think of automated rules like having a personal assistant for your campaigns who can notify or take actions on your behalf.  
  
To access Automated Rules, click on **Tools** at the top of the screen and select **Rules** from the drop down.  

![image.png](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004QQ2N)

## Create Automated rules

Setting up automated rules gives you immediate visibility into potential campaign issues and opportunities, enables you to optimize faster and easier, and have more control over ad spend. Use your campaign goals to structure your rules and have these actions performed automatically for you.

After you create rules, you will be able to view, pause, edit and/or filter your rules whenever you would like from the Automated Rules Dashboard. In addition, you can review all the changes that your rules have made to your campaign and review the rule statuses.  
  
To create a rule, click on the Create New Rule button in the top right corner of the Automated Rules dashboard.  
  
**Note:** When creating a rule, you will receive a pop-up acknowledgment which you must agree to before creating your rule.

![Graphical user interface, application, Teams  Description automatically generated](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXCK)  

There are three types of actions that an automated rule can do: send notifications, increase/decrease budget and increase/decrease bids.

### Rule action: Notifications only

This action type allows you to receive real-time email notifications if or when your campaign(s) run out of budget or trigger a custom rule you have set.  

**Example:** You can set up a rule to receive email notifications if your campaign achieves an Average ROAS of $3 over a set period.  

#### Create a rule that notifies you when a campaign is out of budget

This gives you the opportunity to increase the campaign’s daily/total budget in real-time to avoid missed advertisement opportunities.  
  
**Note:** We recommend you run this rule indefinitely or over a long period of time.

- Enter your rule name
- In the *Choose Action* section:
	- Keep **Notification Only (Default)** as your Action Type
		- Select **Out of Budget** as your Notification Type
- In the *Apply the Rule* to section:
	- Select **All Campaigns** or **Selected Campaigns** as your attribute
		- There is also a button to **Exclude Campaigns**. This is an effective option if you want to exclude all your current campaigns, but one or two.
		- If you choose **Selected Campaigns**, there will be a pop-up where you can search for and select the individual campaigns you would like your rule to apply to.
- In the *Select a Date Range* section, either select Indefinite or provide a start and end date for the duration you'd like the rule to run.
- In the *Notification* section, enter the email(s) of the users who will receive the email notifications when the rule is triggered.
	- After entering an email address, press **Enter** to add the email to the list

**Note:** Email notifications can only be sent to email addresses that are associated with your account. You will not be able to save the rule if you use an email not associated with your account. (See this [FAQ](https://advertisinghelp.walmart.com/s/faqs?articlenumber=000008401&article=Login_Questions) for more information.)

- Click **Save**.

#### Create a rule that notifies you when certain conditions are met

- Enter your rule name
- In the *Choose Actio* n section:
	- Keep **Notification Only (Default**) as your Action Type.
		- Select **Custom** as your Notification Type.
- In the *Compare Values* section, select the performance metric(s) that you want to track
	- We offer the following performance metrics: Avg. ROAS, Avg. Ad Spend, Impressions, and Clicks
		- You can select up to a maximum of 3 values to compare
- In the *Apply the Rule to* section:
	- Select **All Campaigns** or **Selected Campaigns** as your attribute.
		- If you choose **Selected Campaigns**, there will be a pop-up where you can search for and select the individual campaigns you would like your rule to apply to.
- In the *Select a Date Range* section:
	- Either select **Indefinite** or provide a start and end date for the duration you'd like the rule to run.
		- Select a **Compare** from time frame: Yesterday, Last 7 days, This month, Last 30 days, Last 60 days
		- Select an **Occurrence**: Once, Daily, Weekly, or Monthly
- In the *Notification* section, enter the email(s) of the users who will receive the email notifications when the rule is triggered.
	- After entering an email address, press Enter to add the email to the list.

**Note:** Email notifications can only be sent to email addresses that are associated with your account. You will not be able to save the rule if you use an email not associated with your account. (See this [FAQ](https://advertisinghelp.walmart.com/s/faqs?articlenumber=000008401&article=Login_Questions) for more information.)

- Click **Save**.

#### Create a rule that notifies you when a performance metric is underperforming

For example, after running your campaign for several days, you’ve established a baseline of 10,000 impressions a week, and you want to ensure your campaign is maintaining or exceeding that number going forward.  
  
Create a custom notification rule to trigger an email that notifies you if your impressions dip below that amount, which may indicate you are being outbid.

- Set your Performance Metric to Impressions.
- Set your Operator to is lesser than.
- Set your Value to 10000.
- Set Occurrence to Weekly.

**Note:** We recommend running this type of rule weekly. Impressions and clicks are cumulative in nature, depending upon the occurrence you have chosen. For example, if your daily impressions are 100, the rule will aggregate impressions to 7000 to evaluate for a weekly run, 100 for daily, and 30000/31000 for monthly.  

![Graphical user interface, application  Description automatically generated](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXCf)

### Rule action: Increase/Decrease budget

This action type allows you to either increase or decrease the campaign daily and/or total budgets by either a dollar amount or percentage based on a performance trigger(s).  
  
**Note:** You can set up a rule to increase your daily budget by $20 if your clicks are greater than 250.  
  
**Create a rule to increase or decrease budget when specific conditions are met**

- Enter your rule name
- In the *Choose Action* section:
	- Select **Increase Budget** or **Decrease Budget** as your Action Type.
		- Select a Budget type you would like to modify when your rule triggers: *Daily Budget, Total Budget* or *Daily* and *Total Budget.*
		- Once you select your Budget type, three more options will populate:
		- Value - Section the amount you would like to increase/decrease by.
				- Measurement - Select with $ or %.
				- Max Total/Daily Budget or Min Total/Daily Budget - Select the maximum or minimum amount that you would like your budget to be set to.
- In the *Compare Values* section, select the performance metric(s) that will trigger the rule
	- We offer the following performance metrics: *Avg RoAS, Avg. Ad Spend, Impressions* and *Clicks*.
		- You can select a maximum of 3 values to compare.
- In the *Apply the Rule* to section:
	- Select **All Campaigns** or **Selected Campaigns** as your attribute.
		- There is also a button to Exclude Campaigns. This is an effective option if you want to all your current campaigns, but one or two.
		- If you choose Selected Campaigns, there will be a pop-up where you can search for and select the individual campaigns you would like your rule to apply to.
- In the *Select a Date Range* section:
	- Either select Indefinite or provide a start and end date for the duration you would like the rule to run.
		- Select a Compare from time frame: Yesterday, Last 7 days, This month, Last 30 days and Last 60 days.
		- Select an Occurrence: Once, Daily, Weekly or Monthly.
- In the *Notification* section, enter the email(s) of the users who will receive the email notifications when the rule is triggered.
	- After entering an email address, press Enter to add the email to the list.

Note: Email notifications can only be sent to email addresses that are associated with your account. You will not be able to save the rule if you use an email not associated with your account. (See this [FAQ](https://advertisinghelp.walmart.com/s/faqs?articlenumber=000008401&article=Login_Questions) for more information.)

- Click Save.

  
**Create a rule to increase daily budgets for campaigns that are performing well.**  
You notice your campaign is hitting its daily budget of $100 and meeting your performance goals of a $3 ROAS. You’d like to allocate an additional $50 in daily budget to the campaign so it continues to be promoted throughout the day, while also maintaining its ROAS.  
  
Create an increase budget rule to increase your daily budget in real-time if your goal is met, while also setting a maximum daily budget amount of $400.

- Set your Action Type to Increase Budget.
- Set your Budget Type to Daily Budget.
- Set your Value to 50.
- Set your Measurement to $.
- Set your Max Daily Budget to 400.
- Set your Performance Metric to Avg. ROAS.
- Set your Operator to is greater or equal to.
- Set your Value to 3.
- Set your Compare from Yesterday.
- Set your Occurrence to Daily.

**Note:** You will not be notified if no changes were made to your campaigns.  

![image.png](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXFO)

### Rule action: Increase/Decrease bid

This action type allows you to either increase or decrease the bid at the ad group level by either a dollar amount or percentage based on a performance trigger(s). This action type functions similarly to the increase and decrease budget actions, but the key difference between budget rules and bid rules is that budget rules are applied at the campaign level whereas bids are applied at the ad group level. Bids will increase or decrease for each item or keyword in the assigned ad group.

#### Create a rule to increase or decrease bid when specific conditions are met

- Enter your rule name
- In the *Choose Action* section:
	- Select **Increase Bid** or **Decrease Bid** as your Action Type.
		- Once you select your action, three more options will populate:
		- Value - Section the amount you would like to increase/decrease by
				- Measurement - Select with $ or %.
				- Min/Max Bid - Select the maximum or minimum amount that you would like your bid to be set at. The rule will not go above (max bid) or below (min bid) that amount set.
- In the *Compare Values* section, select the performance metric(s) that will trigger the rule
	- We offer the following performance metrics: Avg RoAS, Avg. Ad Spend, Impressions and Clicks.
		- You can select a maximum of 3 values to compare.
- In the *Apply the Rule to* section:
	- Select **All Ad groups** or **Selected Ad groups** as your attribute.
		- There is also a button to **Exclude Ad groups**. This is an effective option if you want to all your current campaigns, but one or two.
		- If you choose **Selected Ad groups**, there will be a pop-up where you can search for and select the individual campaigns then their ad groups you would like your rule to apply.
- In the *Select a Date Range* section:
	- Either select Indefinite or provide a start and end date for the duration you would like the rule to run.
		- Select a Compare from time frame: Yesterday, Last 7 days, This month, Last 30 days or Last 60 days.
		- Select an Occurrence: Once, Daily, Weekly or Monthly.
- In the *Notification section*, enter the email(s) of the users who will receive the email notifications when the rule is triggered.
	- After entering an email address, press Enter to add the email to the list.

**Note:** Email notifications can only be sent to email addresses that are associated with your account. You will not be able to save the rule if you use an email not associated with your account. (See this [FAQ](https://advertisinghelp.walmart.com/s/faqs?articlenumber=000008401&article=Login_Questions) for more information).

- Click Save.

#### Create a rule to increase bids for ad groups that are not performing as expected

You notice your campaigns are not showing the click-through-rate that you expected, so you want to see if increasing bids within certain ad groups will help with this.

Create an increase bid rule to increase bids with ad groups in real-time if your goal is met, while also setting a maximum bid amount of $3.50.

- Set your Action Type to Increase Bid.
- Set your Value to 0.20.
- Set your Measurement to $.
- Set your Max Bid to 3.50.
- Set your Performance Metric to CTR.
- Set your Operator to is less than or equal to.
- Set your Value to 40. (CTR is calculated in percentages, so this value is 40%.)
- Set your Compare from Last 7 days.
- Set your Occurrence to Daily.

**Note:** You will not be notified if no changes were made to your campaigns.

## Email notifications

When you create a rule, you can choose to receive email notifications when your rule runs. You'll be notified after each rule is run only if the rule completes successfully and a change has been made to your campaign.  
  
To sign up for email notifications, simply enter an email address as you're creating or editing a rule. If you prefer not to receive email notifications, leave the email field blank.  
  
Any changes to email notifications will show in the rule history.  
  

## Rule results and history

You can view a historical list of all the changes executed by the rule on the Automate Rules Dashboard. To view the changes made by a rule, click on the "Successful" link under the Results column (you may need to scroll to the right to see this column).  
  
**Note:** Only campaigns with changes will appear.  

![](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXFd)

![Graphical user interface, application  Description automatically generated](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXFg)

  
You can view a historical list of all the changes made to a rule, including who created the rule, who modified the rule, and what modifications were made.  
  
To access rule history, click on the clock icon to the far right of the rule. You may have to scroll to see it.  

Types of changes visible:

- Increases or decreases in budgets
- Changes to $ or % increase or decrease of budgets
- Changes to min or max budgets
- Changes to conditions
- Changes to campaigns - additional and removal
- Changes to email notifications - additional and removal
- Changes to occurrence
![](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXFo)

## Best practices

**Be mindful of rules that increase or decrease budgets**

You should take careful consideration when setting up budget rules. Start by running increase/decrease budget rules once and observe performance closely before scheduling it frequently.  
  
**Monitor your rules frequently**  
Review the rules you have created on a bi-weekly basis at minimum to avoid excess budget increases/decreases or unexpected performance spikes/dips.  
  
**Filter by: Rule Status**  
You can also use the Filter By dropdown to filter by rules that are currently on, off, or both (default).

![Graphical user interface, text, application, chat or text message  Description automatically generated](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXEW)  
  
**Filter by: Rule Name**  
If you have created many campaigns, you can use the search box to filter rules by entering the rule’s name.

![Graphical user interface, application  Description automatically generated with medium confidence](https://advertisinghelp.walmart.com/servlet/rtaImage?eid=ka0KW0000002UbA&feoid=00N6100000Hxa5T&refid=0EM8Y000004nXEX)

**Choose the frequency of your rule carefully**  
Impressions and clicks are cumulative in nature, depending on the Compare from time frame you have selected. For example, if your daily impressions are 1000, the rule will aggregate impressions to 30000 to evaluate for the last 30 days run. We recommend you set up a weekly occurrence for notifications. The occurrence for increase/decrease budgets may vary based on your budget strategy.

**Additional Information**

- Rules can only be applied to active/live campaigns.
- Users will only receive rule notifications on desktop through supported emails clients: Gmail, Mail (Mac desktop application), and Outlook.
- Email clients on App and mWeb not currently available.
- Email notifications will only be sent if a rule condition was met and action was made to a campaign.
- Results will only display campaigns that were modified by your rule action.
- Automated rules will only increase/decrease your daily and/or total budget. Users will still need to adjust bids manually.
- Rules cannot be cloned or reverted once ran.
- A maximum of 20 rules can be enabled at one time.
- Rules cannot be deleted, only disabled.
- Rules made to budgets will never override the minimum/maximum campaign budget limits.
- If there is a budget change, the campaign history will show the name of the person who created the rule.

## Related content

For more information on managing keywords, visit the [All Keywords guide](https://advertisinghelp.walmart.com/s/guides?channel=Sponsored&article=000011134).  
For more information on managing budgets and spend, visit the [All Campaigns guide](https://advertisinghelp.walmart.com/s/guides?channel=Sponsored&article=000008410).

How can we improve?

 Article wasn't accurate

 Article wasn't relevant

 Article wasn't clear

 Yes, you may contact me about this feedback.

Loading

Knowledge Base