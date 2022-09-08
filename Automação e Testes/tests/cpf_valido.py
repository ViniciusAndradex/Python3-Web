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
from selenium.webdriver import Firefox
from nlpage.register import RegisterNl as rng

class TestUnitationNl (unittest.TestCase):

    def setUp(self):
        self.driver = Firefox()
        self.driver.get("https://prpi.ifce.edu.br/nl/app_form_add_users/")

    def test_register(self):

        rng.write_cpf(self.driver, "805.775.890-24")
        rng.mock_teste(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()