import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
checkboxes[1].click()
assert checkboxes[1].is_selected(), "checkbox is not selected"
print(len(checkboxes))


radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected(), "radio button is not selected"

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()

time.sleep(3)
driver.close()