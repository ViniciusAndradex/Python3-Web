from selenium.webdriver.common.by import By
from time import sleep

class LoginNl():

    @staticmethod
    def open_cadastro(driver):
        cad = driver.find_element(By.XPATH, "//div/div/div/a[.='Cadastrar Usuário']")
        driver.execute_script("arguments[0].click()", cad)
    
    @staticmethod
    def write_cpf(driver, cpf=""):
        cpf_write = driver.find_element(By.ID, "id_sc_field_login")
        cpf_write.send_keys(cpf)

    @staticmethod
    def warning_potencial(driver):
        sleep(2)
        advanced = driver.find_element(By.ID, "advancedButton")
        advanced.click()
        # sleep(2)
        # advanced_exception = driver.find_element(By.ID, "exceptionDialogButton")
        # advanced_exception.click()
        # sleep(6)
