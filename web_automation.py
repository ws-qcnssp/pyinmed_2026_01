from playwright.sync_api import sync_playwright

URL = 'https://the-internet.herokuapp.com'

def start_pw(pw):
    browser = pw.chromium.launch(
        headless=False,
        slow_mo=2000
    )
    return browser

def stop_pw(browser):
    if browser:
        browser.close()