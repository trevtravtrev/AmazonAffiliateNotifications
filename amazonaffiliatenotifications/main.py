# AmazonAffiliateNotifications main file. Run this file to start the application. The Dockerfile is also preconfigured to run this file.
import scraper
import calculate

def main():
    webpage_text = scraper.scrape()
    parsed_data = scraper.parse(webpage_text)
    for sale in parsed_data:
        pass