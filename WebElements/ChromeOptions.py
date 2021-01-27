import time

from selenium import webdriver

chrome_optons = webdriver.ChromeOptions()
chrome_optons.add_argument("--start-maximized")
#chrome_optons.add_argument("headless")
chrome_optons.add_argument("--ingnore-certificate-errors")

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ", options=chrome_optons)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
shopbutton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopbutton)
time.sleep(2)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print(driver.title)
driver.close()