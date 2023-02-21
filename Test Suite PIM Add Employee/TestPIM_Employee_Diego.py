import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_nama(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        self.browser.maximize_window()
        time.sleep(5)
        browser.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(3)
        browser.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.NAME, 'firstName').send_keys('Diego')
        time.sleep(3)
        browser.find_element(By.NAME, 'middleName').send_keys('Yanda')
        time.sleep(3)
        browser.find_element(By.NAME, 'lastName').send_keys('Setiawan')
        time.sleep(3)
        
    def test_cancel_employee(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        self.browser.maximize_window()
        time.sleep(5)
        browser.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(3)
        browser.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.NAME, 'firstName').send_keys('Diego')
        time.sleep(3)
        browser.find_element(By.NAME, 'middleName').send_keys('Yanda')
        time.sleep(3)
        browser.find_element(By.NAME, 'lastName').send_keys('Setiawan')
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
        time.sleep(3)
        
    def test_save_employee(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        self.browser.maximize_window()
        time.sleep(5)
        browser.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(3)
        browser.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.NAME, 'firstName').send_keys('Diego')
        time.sleep(3)
        browser.find_element(By.NAME, 'middleName').send_keys('Yanda')
        time.sleep(3)
        browser.find_element(By.NAME, 'lastName').send_keys('Setiawan')
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(3)

unittest.main()
