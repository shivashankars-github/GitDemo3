import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
#driver.get("https://www.familysearch.org/en/")
#driver.find_element_by_css_selector("button[aria-controls='search']").click()
#action = ActionChains(driver)
#action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://www.chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
time.sleep(2)
driver.switch_to.alert.accept()
#driver.close()