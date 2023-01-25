# Test
import time
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://cutt.ly/h9jsZRf")
    page2 = browser.new_page()
    page2.goto("https://cutt.ly/h9jsZRf")
    page3 = browser.new_page()
    page3.goto("https://cutt.ly/h9jsZRf")
    page4 = browser.new_page()
    page4.goto("https://cutt.ly/h9jsZRf")
    page5 = browser.new_page()
    page5.goto("https://cutt.ly/h9jsZRf")
    time.sleep(300)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
