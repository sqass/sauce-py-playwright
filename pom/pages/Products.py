from playwright.sync_api import Page, expect
import re

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.header = page.locator('//div[@class="app_logo"]')

    def validateSuccessfulLoad(self):
        expect(self.page).to_have_title(re.compile("Swag Labs"))
        expect(self.header).to_be_visible()