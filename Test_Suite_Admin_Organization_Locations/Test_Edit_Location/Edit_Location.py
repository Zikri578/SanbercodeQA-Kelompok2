import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from page import elem

class TestEdit(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_edit_success(self):
        browser = self.browser

        browser.get(elem.base_url)
        self.browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH,elem.admin).click() #Open Menu Admin
        time.sleep(1)
        browser.find_element(By.XPATH,elem.org).click() 
        time.sleep(1)
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//input[@class= 'oxd-input oxd-input--active']").clear()
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Software In")
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").clear()
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Jakarta")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.edit_slc_country).click()
        browser.find_element(By.XPATH,elem.edit_search_country).click()
        time.sleep(1)       

if __name__ == "__main__": 
    unittest.main()