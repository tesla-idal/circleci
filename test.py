# Test
import time
from playwright.sync_api import sync_playwright

def file_get_contents(filename):
    return open(filename).read()

def run(playwright):
    text = file_get_contents('proxy.txt')
    chromium = playwright.chromium
    browser = chromium.launch(proxy={"server": "per-context"})
    context = browser.new_context(proxy={"server": str(text)})
    page = browser.new_page()
    page.goto("https://cutt.ly/h9jsZRf")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
