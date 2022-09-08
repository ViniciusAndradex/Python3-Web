from selenium.webdriver.common.by import By
from time import sleep

class RegisterNl():

    @staticmethod
    def open_cadastro(driver):
        cad = driver.find_element(By.XPATH, "//div/div/div/a[.='Cadastrar Usuário']")
        driver.execute_script("arguments[0].click()", cad)
    
    @staticmethod
    def write_cpf(driver, cpf=""):
        cpf_write = driver.find_element(By.ID, "id_sc_field_login")
        cpf_write.send_keys(cpf)

    @staticmethod
    def mock_teste(driver):
        senha = driver.find_element(By.ID, "id_sc_field_pswd")
        senha.send_keys("123456")
        conf_senha = driver.find_element(By.ID, "id_sc_field_confirm_pswd")
        conf_senha.send_keys("123456")
        email = driver.find_element(By.ID, "id_sc_field_email")
        email.send_keys("jorginho2@kdjdjd.kancsk")
        cadastrar = driver.find_element(By.ID, "sc_b_ins_b")
        cadastrar.click()