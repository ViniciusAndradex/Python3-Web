from selenium.webdriver.common.by import By

class LoginPage:
    
    def escrever_mail(self, driver ,mail):
        email = driver.find_element(By.ID, "txtEmail")
        email.send_keys(mail)

    def escrever_senha(self, driver, password):
        ps = driver.find_element(By.ID, "pwdSenha")
        ps.send_keys(password)
    
    def clicar(self, driver):
        sbm = driver.find_element(By.ID, "sbmLogin")
        sbm.click()
