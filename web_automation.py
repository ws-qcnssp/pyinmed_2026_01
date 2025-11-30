from playwright.sync_api import sync_playwright
from time import sleep

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


def main():
    with sync_playwright() as pw:
        browser = start_pw(pw)
        sleep(5)
        stop_pw(browser)


