from selenium.webdriver.common.by import By

class WebElements:
    def __init__(self, locator, driver):
        self.locator = locator
        self.driver = driver

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.find_element().click()
