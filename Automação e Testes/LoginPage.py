from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    driver = webdriver.Firefox()

    def escrever_mail(self, email=""):
        d = webdriver.Firefox()
        print(email)
        mail = d.find_element(By.ID, "txtEmail")
        mail.send_keys(email)

    def escrever_senha(self, password):
        ps = self.driver.find_element(By.ID, "pwdSenha")
        ps.send_keys(password)
    
    def clicar(self):
        sbm = self.driver.find_element(By.ID, "sbmLogin")
        sbm.click()
