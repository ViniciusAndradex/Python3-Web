from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.set_window_size(400, 1080)
driver.get('http://automationpractice.com/index.php')

card1 = driver.find_element(By.XPATH, "//div/a[@data-id-product='1']")
card1.click()
sleep(7)
card1 = driver.find_element(By.XPATH, '//div/span/span/i')
card1.click()

card2 = driver.find_element(By.XPATH, "//div/a[@data-id-product='2']")
card2.click()

sleep(7)
card2 = driver.find_element(By.XPATH, '//div/span/span/i')
card2.click()

card3 = driver.find_element(By.XPATH, "//div/a[@data-id-product='3']")
card3.click()
sleep(7)

elemento = driver.find_element(By.XPATH, "//div/h2/i/..")

assert "successfully" in elemento.text

checkout = driver.find_element(By.XPATH, "//div/a/span/i")
checkout.click()

driver.quit()