from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

icon = driver.find_element(By.CSS_SELECTOR, '#user-name')
icon1 = driver.find_element(By.CSS_SELECTOR, '#password')
icon2 = driver.find_element(By.CSS_SELECTOR, '#login-button')

if icon and icon1 and icon2 is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')

