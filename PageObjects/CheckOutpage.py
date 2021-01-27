from selenium.webdriver.common.by import By


class CheckOutpage:

    def __init__(self, driver):
        self.driver = driver

    #products = (By.XPATH, "//div[@class='card h-100']")
    product_title = (By.CSS_SELECTOR, ".card-title")
    product_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkoutitem = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkoutbutton = (By.XPATH, "//button[@class='btn btn-success']")


    def get_titles(self):
        return self.driver.find_elements(*CheckOutpage.product_title)

    def get_footers(self):
        return self.driver.find_elements(*CheckOutpage.product_footer)

    def checkout_items(self):
        return self.driver.find_element(*CheckOutpage.checkoutitem)

    def checkout(self):
        return self.driver.find_element(*CheckOutpage.checkoutbutton)


