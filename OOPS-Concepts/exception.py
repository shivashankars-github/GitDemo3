import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Shivashankar")
checkbox = driver.find_element_by_id("exampleCheck1").click()








time.sleep(2)
driver.close()