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
from nlpage.register import RegisterNl as rng

class TestUnitationNl(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.get("https://prpi.ifce.edu.br/nl/app_form_add_users/")

    def test_register(self):

        # lng.open_cadastro(self.driver)
        rng.write_cpf(self.driver)
        rng.mock_teste(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()