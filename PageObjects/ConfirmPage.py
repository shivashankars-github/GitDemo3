from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    checkbox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[type='submit']")
    message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def get_successmessage(self):
        return self.driver.find_element(*ConfirmPage.message)