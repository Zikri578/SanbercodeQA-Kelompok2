import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from page import elem

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_add_Location_success(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode")
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
        
        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_a).text
        self.assertIn(response_data,"Admin")

    def test_b_add_Location_success_filled_only_required(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
        self.browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.admin).click() #Open Menu Admin
        time.sleep(1)
        browser.find_element(By.XPATH,elem.org).click() 
        time.sleep(1)
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add Data
        time.sleep(2)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode PTN")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_slc_country).click()
        browser.find_element(By.XPATH,elem.add_srt_country).click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_save_btn).click()
        time.sleep(1)
        
        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_b).text
        self.assertIn(response_data,"Admin")
        
    def test_c_add_Location_failed_required_blank(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
        self.browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(1)

        browser.find_element(By.XPATH,elem.admin).click() #Open Menu Admin
        time.sleep(1)
        browser.find_element(By.XPATH,elem.org).click() 
        time.sleep(1)
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)

        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_save_btn).click()
        time.sleep(1)
        
        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_c).text
        self.assertIn(response_data,"Required")

    def test_d_add_Location_failed_exceed_the_character_limit(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add
        time.sleep(2)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode QZXSa")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_state).send_keys("Jaaaaakkkkkkaaaarrrrrrrrttttttttttttttttttaaaaaaaaaaaaaa")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_slc_country).click()
        browser.find_element(By.XPATH,elem.add_srt_country).click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_save_btn).click()
        time.sleep(1)
        
        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_d).text
        self.assertIn(response_data,"Should not exceed 50 characters")

    def test_e_add_Location_failed_wrong_characters(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode QQaQW")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_slc_country).click()
        browser.find_element(By.XPATH,elem.add_srt_country).click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_telp).send_keys("+628765432121O")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_fax).send_keys("3224A")
        browser.find_element(By.XPATH,elem.add_save_btn).click()
        time.sleep(1)
        
        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_e).text
        self.assertIn(response_data,"Allows numbers and only + - / ( )")

    def test_f_add_Location_failed_data_alredy_exist(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
        self.browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.admin).click() #Open Menu Admin
        time.sleep(1)
        browser.find_element(By.XPATH,elem.org).click() 
        time.sleep(1)
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add Data
        time.sleep(2)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_slc_country).click()
        browser.find_element(By.XPATH,elem.add_srt_country).click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_save_btn).click()
        time.sleep(1)
        
        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_f).text
        self.assertIn(response_data,"Already exists")

    def test_g_add_Location_cancel(self):
        browser = self.browser
        browser.get(elem.base_url) #Open site
        self.browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") #Right Username
        browser.find_element(By.NAME, "password").send_keys("admin123") #Right Password
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,elem.admin).click() #Open Menu Admin
        time.sleep(1)
        browser.find_element(By.XPATH,elem.org).click() 
        time.sleep(1)
        browser.find_element(By.XPATH,elem.loc).click() #Open Menu Location
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_btn).click() #Click Add Data
        time.sleep(2)
        browser.find_element(By.XPATH,elem.add_name).send_keys("Sanbercode GAS")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_slc_country).click()
        browser.find_element(By.XPATH,elem.add_srt_country).click()
        #Select(browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()).select_by_visible_text("Albania")
        time.sleep(1)
        browser.find_element(By.XPATH,elem.add_cancel_btn).click()
        time.sleep(1)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.add_assert_a).text
        self.assertIn(response_data,"Admin")

if __name__ == "__main__": 
    unittest.main()