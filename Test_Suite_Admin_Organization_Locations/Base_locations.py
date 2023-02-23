import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from page import elem

class TestLoc(unittest.TestCase):

    #def setUp(self):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def base_loc(browser):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(elem.base_url) #Open site
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH,elem.admin).click() #Open Menu Admin
        time.sleep(2)
        browser.find_element(By.XPATH,elem.org).click() 
        time.sleep(1)
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)

if __name__ == "__main__": 
    unittest.main()