import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.homepageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_formsubmission(self, getdata):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getdata["name"])
        homepage.get_name().send_keys(getdata["name"])

        homepage.get_email().send_keys(getdata["email"])
        homepage.get_checkbox().click()
        self.selectoptions(homepage.get_gender(), getdata["gender"])

        homepage.get_submitbt().click()

        alerttext = homepage.get_successmessage()

        assert "Successs!" in alerttext.text
        self.driver.refresh()
        log.info("test completed")


    @pytest.fixture(params=HomePageData.get_test_data())
    def getdata(self, request):
        return request.param



