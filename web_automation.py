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

def test_login(page):
    page.goto(URL)
    page.locator("a[href*=login]").click()
    page.locator("input[id=username]").fill('tomsmith')
    page.locator("input[id=password]").fill('SuperSecretPassword!')
    page.locator("button[type=submit]").click()
    alert = page.locator("div[id=flash]")
    alert.wait_for(state="visible")
    if "You logged into a secure area!" in alert.inner_text():
        print('Zalogowano!')
    page.locator("a[href*=logout]").click()
    if "You logged out of the secure area!" in alert.inner_text():
        print('Wylogowano!')


def test_wybor(page):
    page.goto(URL)
    page.locator("a[href*=dropdown]").click()

def main():
    with sync_playwright() as pw:
        browser = start_pw(pw)
        page = browser.new_page()
        test_login(page)
        sleep(5)
        stop_pw(browser)

if __name__ == '__main__':
    main()
