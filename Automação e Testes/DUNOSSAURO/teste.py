from selenium.webdriver.common.by import By

class TestePage:

    def element(self, driver, elemento):
        point = driver.find_element(By.TAG_NAME, elemento)
        return point
    
    def write_input(self, driver):
        write = driver.find_element(By.TAG_NAME, "input")
        write.send_keys("frase")

    def click(self, driver, elemento):
        clicar = driver.find_element(By.TAG_NAME, elemento)
        clicar.click()