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
    webpage_text = scrape()
    parsed_data = parse(webpage_text)
    print(parsed_data)
