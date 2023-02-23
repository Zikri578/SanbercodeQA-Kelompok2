import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from page import elem

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    def test_a_add_Location_success(self):
        browser = self.browser
        browser.get(self.url) #Open site
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
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode Qu")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_city).send_keys("Palagan")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_state).send_keys("Yogyakarta")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_pos).send_keys("551243")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_slc_country).click()
        browser.find_element(By.XPATH,elem.add_srt_country).click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_telp).send_keys("+62 87654321212")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_fax).send_keys("3224")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_adrs).send_keys("Jln.Palagan")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_note).send_keys("Bootcamp QA")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_save_btn).click()
        time.sleep(1)
        
        response_data = browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]").text
        self.assertIn(response_data,"Admin")

    def test_b_add_Location_success_filled_only_required(self):
        browser = self.browser
        browser.get(self.url) #Open site
        self.browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//span[normalize-space()='Admin']").click() #Open Menu Admin
        time.sleep(1)
        browser.find_element(By.XPATH,"//span[normalize-space()='Organization']").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"//li[normalize-space()='Locations']").click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click() #Add Data
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Sanbercode Quality")
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[101]").click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(1)
        
        response_data = browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]").text
        self.assertIn(response_data,"Admin")

if __name__ == "__main__": 
    unittest.main()