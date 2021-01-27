from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.get("https//www.familsearch.org/en/")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()

driver.close()
