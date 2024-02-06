from playwright.sync_api import Page, expect
import re

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('[placeholder="Username"]')
        self.password = page.locator('[placeholder="Password"]')
        self.loginButton = page.locator('[type="submit"]')

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginButton.click()

    def validateSuccessfulLoad(self):
        expect(self.page).to_have_title(re.compile("Swag Labs"))
