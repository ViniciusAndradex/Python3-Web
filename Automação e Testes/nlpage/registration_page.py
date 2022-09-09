try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'  # quanto mais /.. mais pastas para dentro está o módulo do meu desejo.
            )
        )
    )
except ImportError:
    raise
from string import ascii_letters
from selenium.webdriver.common.by import By
from support.gerador_cpf import cpf_gerado

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
    def mock_test_cpf(driver):
        password = driver.find_element(By.ID, "id_sc_field_pswd")
        password.send_keys("123456")
        confirm_password = driver.find_element(By.ID, "id_sc_field_confirm_pswd")
        confirm_password.send_keys("123456")
        email = driver.find_element(By.ID, "id_sc_field_email")
        email.send_keys("jorginho2@kdjdjd.kancsk")
        register = driver.find_element(By.ID, "sc_b_ins_b")
        register.click()

    @staticmethod
    def write_password(driver, password="", confirm_password=""):
        write_password = driver.find_element(By.ID, "id_sc_field_pswd")
        write_password.send_keys(password)
        write_confirm_password = driver.find_element(By.ID, "id_sc_field_confirm_pswd")
        write_confirm_password.send_keys(confirm_password)

    @staticmethod
    def mock_test_password(driver):
        cpf = driver.find_element(By.ID, "id_sc_field_login")
        cpf.send_keys(cpf_gerado())
        email = driver.find_element(By.ID, "id_sc_field_email")
        email.send_keys("jorginho2@kdjdjd.kancsk")
        register = driver.find_element(By.ID, "sc_b_ins_b")
        register.click()

    @staticmethod
    def write_email(driver, email=False):
        if email:
            emailx = ""
            mail = driver.find_element(By.ID, "id_sc_field_email")
            mail.send_keys(emailx)
        

    @staticmethod
    def mock_test_email(driver):
        cpf = driver.find_element(By.ID, "id_sc_field_login")
        cpf.send_keys(cpf_gerado())
        password = driver.find_element(By.ID, "id_sc_field_pswd")
        password.send_keys("123456")
        confirm_password = driver.find_element(By.ID, "id_sc_field_confirm_pswd")
        confirm_password.send_keys("123456")
        register = driver.find_element(By.ID, "sc_b_ins_b")
        register.click()