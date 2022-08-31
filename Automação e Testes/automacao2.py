from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.amazon.com.br/ref=nav_logo")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("bola de basquete")

bottom = driver.find_element(By.ID, "nav-search-submit-button")
bottom.click()

search2 = driver.find_element(By.XPATH, "//div/span[.='bolsa de basquete']")

if search2.text == 'bolsa de basquete':
    print('True')
else:
    print('False')