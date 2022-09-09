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
from nlpage.registration_page import RegisterNl as rng

class TestUnitationNl(unittest.TestCase):
    
    def setUp(self):
        self.driver = Firefox()
        self.driver.get("https://prpi.ifce.edu.br/nl/app_form_add_users/")

    def test_password(self):
        rng.write_email(self.driver, email="asdfg@asjdh")
        rng.mock_test_email(self.driver)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()