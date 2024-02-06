import re
from constants import SAUCE_DEMO_URL
from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.Products import ProductsPage

def test_able_to_login_successfully(page: Page):
    page.goto(SAUCE_DEMO_URL)
    
    loginPage = LoginPage(page)
    loginPage.validateSuccessfulLoad()
    loginPage.login('standard_user','secret_sauce')

    productsPage = ProductsPage(page)
    productsPage.validateSuccessfulLoad()
