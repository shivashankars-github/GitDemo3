from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    submitbt = (By.CSS_SELECTOR, "input[type='submit']")
    successmessage = (By.CSS_SELECTOR, "div[class*='alert-success']")


    def shopitems(self):
        return self.driver.find_element(*HomePage.shop)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submitbt(self):
        return self.driver.find_element(*HomePage.submitbt)

    def get_successmessage(self):
        return self.driver.find_element(*HomePage.successmessage)