import unittest 
import time 
from selenium import webdriver 
from selenium.webdriver import ActionChains 
from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import GeckoDriverManager 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoAlertPresentException 

class Checkboxes(unittest.TestCase): 

    """http://the-internet.herokuapp.com/checkboxes""" 

    def setUp(self): 
        firefox_options = webdriver.FirefoxOptions() 
        firefox_options.accept_insecure_certs = True 
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())) 
        self.base_url = ("http://the-internet.herokuapp.com/checkboxes") 
        self.driver.maximize_window() 
        self.driver.get(self.base_url) 
        time.sleep(3) 
        self.assertIn(self.base_url, self.driver.current_url) 

    def test_checkboxes(self): 
        self.checkbox1 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]') 
        self.assertTrue(self.checkbox1) 
        self.checkbox1.click() 
        time.sleep(2) 
        self.checkbox2 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]') 
        self.assertTrue(self.checkbox2) 
        self.checkbox2.click() 
        time.sleep(2) 
        #self.driver.save_screenshot("checkboxes.png") 

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()
