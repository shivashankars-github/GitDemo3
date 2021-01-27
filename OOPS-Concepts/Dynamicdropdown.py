import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

airtickets = "https://rahulshettyacademy.com/dropdownsPractise/"
url = "https://rahulshettyacademy.com/angularpractice/"


# Dynamic dropdowns example

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get(airtickets)
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").get_attribute("value"))
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"






time.sleep(2)
driver.close()