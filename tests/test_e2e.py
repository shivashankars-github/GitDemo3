import pytest

from PageObjects.CheckOutpage import CheckOutpage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

@pytest.mark.skip
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        hommepage = HomePage(self.driver)
        hommepage.shopitems().click()

        checkoutpage = CheckOutpage(self.driver)
        #products = checkoutpage.get_products()
        product_names = checkoutpage.get_titles()
        product_footer = checkoutpage.get_footers()
        checkout_item = checkoutpage.checkout_items()

        i = -1
        for name in product_names:
            i = i+1
            product_name = name.text
            log.info(product_name)
            if product_name == "Blackberry":
                product_footer[i].click()
        checkout_item.click()
        checkoutbt = checkoutpage.checkout()
        checkoutbt.click()

        confirmpage = ConfirmPage(self.driver)
        country = confirmpage.get_country()
        country.send_keys("Ind")
        self.verifylinkpresence("India")
        self.driver.find_element_by_link_text("India").click()

        checkbox = confirmpage.get_checkbox()
        checkbox.click()
        purchase = confirmpage.get_purchase()
        purchase.click()
        message = confirmpage.get_successmessage()
        log.info("text received from application" + message.text)

        assert "Success!" in message.text

        #self.driver.get_screenshot_as_file("sereenshot1.png")
