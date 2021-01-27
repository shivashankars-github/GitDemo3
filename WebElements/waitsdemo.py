import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements_by_xpath("//div[@class='products']/div")

pricelist = []
namesofveggies = []
for product in products:
    product.find_element_by_xpath("div/button").click()
    namesofveggies.append(product.find_element_by_xpath("h4").text)
    pricelist.append(int(product.find_element_by_xpath("p").text))

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
totalprice = sum(pricelist)


wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element_by_class_name("promoInfo").text)

namesofveggies2 = []
vegitables = driver.find_elements_by_xpath("//tbody/tr/td[2]/p")
for veggie in vegitables:
    namesofveggies2.append(veggie.text)
assert namesofveggies2 == namesofveggies, "vegitables not matched"


pricelist2 = driver.find_elements_by_xpath("//tbody/tr/td[5]/p")
totalamount2 = 0
for i in pricelist2:
    totalamount2 += int(i.text)
assert totalamount2 == totalprice , "price is not matched between first and second page"

assert totalamount2 == int(driver.find_element_by_css_selector("span.totAmt").text)
assert totalamount2 > float(driver.find_element_by_css_selector("span.discountAmt").text)





driver.close()
