import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.select import Select
from page import elem
from Base_locations import TestLoc

class TestSearch(unittest.TestCase):
    #def setUp(self):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_success_By_Name(self):
        #self.browser = TestLoc.base_loc
        browser = self.browser
        TestLoc.base_loc(browser)
    
        browser.find_element(By.XPATH,elem.src_city).send_keys("Canadian Regional HQ")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Validate
        #response_data = browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text
        #browser.assertIn(response_data,"(1) Record Found")


if __name__ == "__main__": 
    unittest.main()