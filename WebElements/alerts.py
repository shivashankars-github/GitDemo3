import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("name").send_keys("shiva")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alert.dismiss()

time.sleep(2)
driver.close()
