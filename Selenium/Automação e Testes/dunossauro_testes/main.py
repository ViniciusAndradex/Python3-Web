import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from teste import TestePage as tp

class TestUnitationDunossaurp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.endereco = "https://selenium.dunossauro.live/aula_07_d"
        self.driver.get(self.endereco)

    def test_possibilidades(self):

        self.assertIn("Digite seu nome", tp.element(self, self.driver, "label").text)

        self.assertIn("0", tp.element(self, self.driver, "p").text)

        tp.click(self, self.driver, "input")

        self.assertIn("está com foco", tp.element(self, self.driver, "span").text)
        tp.click(self, self.driver, "span")
        self.assertIn("está sem foco", tp.element(self, self.driver, "span").text)

        tp.click(self, self.driver, "input")

        tp.write_input(self, self.driver)
        
        tp.click(self, self.driver, "span")
        self.assertIn("1", tp.element(self, self.driver, "p").text)

if __name__ == "__main__":
    unittest.main()
