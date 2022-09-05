import unittest
from selenium import webdriver
from loginpage import LoginPage as lp

class TestUnitationSei(unittest.TestCase):
    # setUp obrigatorio | Recebe todas as config
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.email = "henriquefisicoquimico@gmail.com"
        self.password = "3YCquJNS"
        self.endereco = "https://sei.ifce.edu.br/sei/controlador_externo.php?acao=usuario_externo_logar&acao_origem=usuario_externo_enviar_cadastro&id_orgao_acesso_externo=0"
        self.driver.get(self.endereco)
    
    # Nome test obrigatorio
    def test_login_sei(self):
        # self.driver.get(self.endereco)

        lp.escrever_mail(self, self.driver, self.email)
        lp.escrever_senha(self, self.driver, self.password)
        lp.clicar(self, self.driver)
        
        # self.assertIn("SEI", driver.title)  # esperado, captura | OBJ-> string sei está em driver.title?

    # def test_processos_sei(self):
    #     pesquisa = self.driver.find_element(By.XPATH, "//div/ul/li/ul[@class='sm-nowrap']")
    #     pesquisa.click()

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()
