import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem

class TestDelete(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_delete_success(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
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
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Locations
        time.sleep(1)
        #Scroll 
        browser.execute_script(elem.scroll_page)
        time.sleep(1)
        browser.find_element(By.XPATH,elem.del_icon).click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.del_btn_confirm).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.del_assert).text
        self.assertIn(response_data,"Locations")

    def test_b_cancel_delete(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
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
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Locations
        time.sleep(1)
        #Scroll 
        browser.execute_script(elem.scroll_page)
        time.sleep(1)
        browser.find_element(By.XPATH,elem.del_icon).click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.del_btn_cancel).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.del_assert).text
        self.assertIn(response_data,"Locations")

    def test_c_delete_some_data(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
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
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Locations
        time.sleep(2)
        #Scroll 
        browser.find_element(By.XPATH,elem.del_checkbox).click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.del_btn_select).click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.del_btn_confirm).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.del_assert).text
        self.assertIn(response_data,"Locations")

if __name__ == "__main__":
    unittest.main()