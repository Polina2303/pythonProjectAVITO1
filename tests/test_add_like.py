from pages.cardPage import CardPage
from selenium import webdriver


def test_add_like():
    driver = webdriver.Chrome()
    page = CardPage(driver)

    page.visit()
    page.btn_like.click()

