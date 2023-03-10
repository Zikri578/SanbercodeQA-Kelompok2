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

    def test_a_search_success_by_name(self):
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
        browser.find_element(By.XPATH,elem.src_name).send_keys("Canadian Regional HQ") #Right Name
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_a).text
        self.assertIn(response_data,"(1) Record Found")

    def test_b_search_success_by_city(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_city).send_keys("Ottawa") #Right City
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_b).text
        self.assertIn(response_data,"(1) Record Found")

    def test_c_search_success_by_country(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.slc_country).click()
        browser.find_element(By.XPATH,elem.srt_slc_country).click() #Right Country
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_c).text
        self.assertIn(response_data,"(1) Record Found")


    def test_d_search_success_by_came_city_country(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_name).send_keys("Canadian Regional HQ") #Right Name
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_city).send_keys("Ottawa") #Right City
        time.sleep(1)
        browser.find_element(By.XPATH,elem.slc_country).click()
        browser.find_element(By.XPATH,elem.srt_slc_country).click() #Right Country
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_d).text
        self.assertIn(response_data,"(1) Record Found")

    def test_e_search_failed_invalid_name(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_name).send_keys("Canadian HQ") #Wrong Name
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_e).text
        self.assertIn(response_data,"No Records Found")

    def test_f_search_failed_invalid_city(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_name).send_keys("Canada") #Wrong City
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_f).text
        self.assertIn(response_data,"No Records Found")

    def test_g_search_failed_invalid_country(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.slc_country).click()
        browser.find_element(By.XPATH,elem.srt_slc_wrong_country).click() #Wrong Country
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_g).text
        self.assertIn(response_data,"No Records Found")

    def test_h_search_failed_invalid_name_city_country(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_name).send_keys("Canadian HQ") #Wrong Name
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_name).send_keys("Canada") #Wrong City
        time.sleep(1)
        browser.find_element(By.XPATH,elem.slc_country).click()
        browser.find_element(By.XPATH,elem.srt_slc_wrong_country).click() #Wrong Country
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(1)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_h).text
        self.assertIn(response_data,"No Records Found")

    def test_i_search_reset_success(self):
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
        browser.find_element(By.XPATH,elem.loc).click() #Menu Locations
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_city).send_keys("Ottawa") #Right City
        time.sleep(1)
        browser.find_element(By.XPATH,elem.src_btn).click()
        time.sleep(2)
        browser.find_element(By.XPATH,elem.src_reset_btn).click()
        time.sleep(2)

        #Assert
        response_data = browser.find_element(By.XPATH,elem.src_assert_i).text
        self.assertIn(response_data,"Organization")

if __name__ == "__main__": 
    unittest.main()