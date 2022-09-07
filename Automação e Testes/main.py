from time import sleep
import unittest
from selenium import webdriver
from LoginPage import LoginPage as lp

class TestUnitationSei(unittest.TestCase):
    # setUp obrigatorio | Recebe todas as config
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.email = "henriquefisicoquimico@gmail.com"
        self.password = "********"
        self.endereco = "https://sei.ifce.edu.br/sei/controlador_externo.php?acao=usuario_externo_logar&acao_origem=usuario_externo_enviar_cadastro&id_orgao_acesso_externo=0"

    def open_site(self):
        self.driver.get(self.endereco)

    # Nome test obrigatorio
    # def test_login_sei(self):

    #     lp.escrever_mail(self.email)
        # sleep(2)
        # lp.escrever_senha(self.password)
        # sleep(2)
        # lp.clicar()
        
        # self.assertIn("SEI", driver.title)  # esperado, captura | OBJ-> string sei está em driver.title?

    # def test_processos_sei(self):
    #     driver = self.driver
    #     pesquisa = driver.find_element(By.XPATH, "//div/ul/li/ul/li/a[.=\"Processo Novo\"]")
    #     pesquisa.click()

    # def tearDown(self):
    #     # self.driver.close()

if __name__ == "__main__":
    unittest.main()
