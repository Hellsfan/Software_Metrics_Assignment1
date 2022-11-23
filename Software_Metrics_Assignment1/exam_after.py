import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Checkboxes(unittest.TestCase):
    """http://the-internet.herokuapp.com/checkboxes"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = ("http://the-internet.herokuapp.com/checkboxes")
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)
        self.assertIn(self.base_url, self.driver.current_url)

    def test_checkboxes(self):
        check1_xpath = '//*[@id="checkboxes"]/input[1]'
        self.checkbox1 = self.driver.find_element(By.XPATH, check1_xpath)
        self.assertTrue(self.checkbox1)
        self.checkbox1.click()
        time.sleep(2)
        check2_xpath = '//*[@id="checkboxes"]/input[2]'
        self.checkbox2 = self.driver.find_element(By.XPATH, check2_xpath)
        self.assertTrue(self.checkbox2)
        self.checkbox2.click()
        time.sleep(2)
        # self.driver.save_screenshot("checkboxes.png")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
