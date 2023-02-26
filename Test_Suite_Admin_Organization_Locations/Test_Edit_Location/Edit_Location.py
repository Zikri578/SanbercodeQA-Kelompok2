import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        driver = browser.find_element(By.XPATH,elem.edit_city)
        driver.send_keys(Keys.CONTROL + "a")
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys("Jakarta")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.edit_slc_country).click()
        browser.find_element(By.XPATH,elem.edit_search_country).click()
        time.sleep(1)   
        browser.find_element(By.XPATH,elem.edit_btn_save).click()
        time.sleep(1)    

        #Assert
        response_data = browser.find_element(By.XPATH,elem.edit_assert).text
        self.assertIn(response_data,"OrangeHRM OS 5.3")

    def test_b_edit_failed(self):
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
        browser.find_element(By.XPATH,elem.edit_icon_btn).click()
        time.sleep(3)
        driver = browser.find_element(By.XPATH,elem.edit_city)
        driver.send_keys(Keys.CONTROL + "a")
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys("Jaaaaakkkkkkaaaarrrrrrrrttttttttttttttttttaaaaaaaaaaaaaa")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.edit_slc_country).click()
        browser.find_element(By.XPATH,elem.edit_search_country).click()
        time.sleep(1)   
        driver = browser.find_element(By.XPATH,elem.edit_phone)
        driver.send_keys(Keys.CONTROL + "a")
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys("62 787887676O")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.edit_btn_save).click()
        time.sleep(1)    

        #Assert
        response_data = browser.find_element(By.XPATH,elem.edit_fail_assert).text
        self.assertIn(response_data,"Should not exceed 50 characters")

    def test_c_edit_cancel(self):
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
        browser.find_element(By.XPATH,elem.edit_icon_btn).click()
        time.sleep(3)
        driver = browser.find_element(By.XPATH,elem.edit_city)
        driver.send_keys(Keys.CONTROL + "a")
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys("Jaaaaakkkkkkaaaarrrrrrrrttttttttttttttttttaaaaaaaaaaaaaa")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.edit_slc_country).click()
        browser.find_element(By.XPATH,elem.edit_search_country).click()
        time.sleep(1)   
        driver = browser.find_element(By.XPATH,elem.edit_phone)
        driver.send_keys(Keys.CONTROL + "a")
        driver.send_keys(Keys.BACKSPACE)
        driver.send_keys("62 787887676O")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.edit_btn_cancel).click()
        time.sleep(1)    

        #Assert
        response_data = browser.find_element(By.XPATH,elem.edit_cancel_assert).text
        self.assertIn(response_data,"Locations")

if __name__ == "__main__": 
    unittest.main()