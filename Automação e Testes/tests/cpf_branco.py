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
import unittest
from selenium import webdriver
from nlpage.login import LoginNl as lng


class TestUnitationNl(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.get("https://prpi.ifce.edu.br/nl/app_Login/")

    def test_open_site(self):

        lng.open_cadastro(self.driver)
        print()
        lng.write_cpf(self.driver, '153')

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()