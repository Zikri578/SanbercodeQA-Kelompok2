import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test__nama(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        """ 
        browser.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(1)
        browser.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button').click()
        time.sleep(1)
        """
        browser.find_element(By.NAME, 'firstName').send_keys('Diego')
        time.sleep(1)
        browser.find_element(By.NAME, 'middleName').send_keys('Yanda')
        time.sleep(1)
        browser.find_element(By.NAME, 'lastName').send_keys('Setiawan')
        time.sleep(1)
        
    def test__ID(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        browser.find_element(By.CLASS_NAME, 'oxd-input oxd-input--active').send_keys('111')
        time.sleep(1)
        
    def save__employee(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        browser.find_element(By.NAME, 'firstName').send_keys('Diego')
        time.sleep(1)
        browser.find_element(By.NAME, 'middleName').send_keys('Yanda')
        time.sleep(1)
        browser.find_element(By.NAME, 'lastName').send_keys('Setiawan')
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, 'oxd-input oxd-input--active').send_keys('111')
        time.sleep(1)
        browser.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space").click()
        time.sleep(1)
        
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()