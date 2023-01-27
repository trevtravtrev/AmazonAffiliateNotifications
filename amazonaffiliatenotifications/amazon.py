import pyautogui
import pyperclip
from time import sleep
import re


def scrape():
    commissions = pyautogui.locateOnScreen("commissions.png", confidence=0.8)
    if commissions is None:
        commissions = pyautogui.locateOnScreen("commissions2.png", confidence=0.8)
        if commissions is None:
            commissions = pyautogui.locateOnScreen("commissions3.png", confidence=0.8)
            if commissions is None:
                raise Exception("Could not find commissions. Amazon affiliate window might not be open or visible.")
    pyautogui.click(commissions)

    sleep(5)
    pyautogui.hotkey('f5')
    sleep(15)
    pyautogui.hotkey('ctrl', 'a')
    sleep(3)
    pyautogui.hotkey('ctrl', 'c')

    # Get the data from clipboard
    webpage_text = pyperclip.paste()
    return webpage_text


def parse(webpage_text):
    # Use a regular expression to extract the relevant information
    match = re.findall(r'(\d+)(.*)\n(.*)\t(.*)\t(.*)\t(.*)\t\$(.*)', webpage_text)


    # Create an empty list to store the parsed data
    parsed_data = []

    # Iterate through the matches and store the relevant information in the parsed_data list
    for item in match:
        parsed_data.append({
            'sale_number': item[0].strip(),
            'item': item[1].strip(),
            'category': item[2].strip(),
            'amount': item[4].strip(),
            'price': item[6].strip()
        })

        # Print the parsed data
    return parsed_data


if __name__ == '__main__':
    # test_webpage_data = """Idea Hub Today's deals: every amazing deal live right now. See them all
    # Store: pluggrr-20English - EN  United States
    # contactpluggrr@gmail.com
    # 5+
    # HomeProduct LinkingPromotionsTools
    # Reports
    # Help
    # ‹ Go to consolidated summary reports
    # Reports
    # HelpFeedbackDownload ReportsPayment HistoryCommission Schedule
    # Jan 26 2023 / Today Tracking ID: All Last Updated: Jan 25 2023 +00:00
    # Summary
    # Earnings not available for Today
    # Commissions
    # Only Orders data available for Today
    # Bounties
    # Today's Orders Jan 26 2023
    # 1REESE'S Milk Chocolate and Peanut Butter Snack Size Cups Candy, Gluten Free, Individually Wrapped, Pantry Pack, 0.55 oz Packs (25 Count)
    # Grocery & Gourmet Food	Amazon.com	2	pluggrr-20	$5.88
    # 2Olaplex No.5 Bond Maintenance Conditioner, 8.5 Fl Oz
    # Luxury Beauty	Amazon.com	1	pluggrr-20	$15.00
    # 3Olaplex No.5 Bond Maintenance Conditioner, 8.5 Fl Oz
    # Luxury Beauty	Amazon.com	1	pluggrr-20	$15.00
    # 4Reese's Puffs Breakfast Cereal Treat Bars, Peanut Butter & Cocoa, 16 ct
    # Grocery & Gourmet Food	Amazon.com	1	pluggrr-20	$5.23
    # (Showing 1 - 4 Items)
    # Notes
    # Kindle E-Books EarningsYou have referred 0 Kindle Free E-books and 0 Kindle Paid E-Books. Per our operating agreement, certain conditions may cause non payment of advertising fees. Learn More. Transactions Ineligible for FeesPer our operating agreement, certain conditions and exclusions exist that may cause a purchase through a link to not earn advertising fees. Learn More.
    # What do you think?
    #
    # Do you have a suggestion or comment about Associates Central website? Let us know.
    #
    # Learn More
    # Commission Income
    # Resource Center
    # Amazon Trade-in Program
    # AbeBooks.com
    # Reporting
    # Customer Support
    # Help
    # Performance Tips
    # Excluded Products
    # Glossary
    # Contact Us
    # Legal
    # Conditions of Use
    # Privacy Notice
    # Operating Agreement
    # Follow Us
    # YouTube
    # Facebook
    # LinkedIn
    # © 1996-2022, Amazon.com, Inc."""
    webpage_text = scrape()
    parsed_data = parse(webpage_text)
    print(parsed_data)
