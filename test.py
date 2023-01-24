# Test
import time
from playwright.sync_api import Page, expect, sync_playwright

def file_get_contents(filename):
    return open(filename).read()

def run(playwright):
    text = file_get_contents('proxy.txt')
    chromium = playwright.chromium
    browser = chromium.launch(channel='chrome', proxy={"server":"http://" + str(text)})
    page = browser.new_page()
    page.goto("https://cutt.ly/h9jsZRf")
    time.sleep(300)

with sync_playwright() as playwright:
    run(playwright)
