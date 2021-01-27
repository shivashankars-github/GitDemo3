import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))


shopbutton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopbutton)

#selenium has no capability of scrolling down, so that we can use java script
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


time.sleep(8)
driver.close()
