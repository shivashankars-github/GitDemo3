from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe  ")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productname = product.find_element_by_xpath("div/h4/a").text
    if productname == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys("Ind")
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()

assert "Success!" in driver.find_element_by_css_selector("div[class*='alert-success']").text

driver.get_screenshot_as_file("sereenshot1.png")
driver.close()

