import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image



class TestAddJobTitle(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())


    def test_cancel_delete_data(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
        delete_2 = browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[11]/div/div/div[1]/div[2]/div/div/button[1]").click()
        self.assertIn('Database Administrator', delete_2)
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[1]").click()
        time.sleep(2)
        

    def test_delete_data(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        delete_1 = browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[7]/div/div/div[1]/div[2]/div/div/button[1]/i").text.click()
        self.assertIn('Database Administrator', delete_1)
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        time.sleep(2)

    def test_Update_empty_data(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[7]/div/div/div[1]/div[2]/div/div/button[2]").click()
        time.sleep(3)

    def test_Update_data(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[7]/div/div/div[1]/div[2]/div/div/button[2]").click()
        time.sleep(3)
        
    
    def test_add_empty_data(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        browser.find_element(By.XPATH, "//Button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
        time.sleep(3)

    def test_add_same_just_job_title(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        browser.find_element(By.XPATH, "//Button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Manager Trainee")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
        time.sleep(3)

        # validation
        response_data = browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span").text
        self.assertIn('Already exists', response_data) 


    def test_add_just_job_title(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        browser.find_element(By.XPATH, "//Button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Manager Trainee")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
        time.sleep(3)

    def test_a_add_success_job_title(self):
        # steps Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT, 'Job Titles').click()
        time.sleep(2)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")

        browser.find_element(By.XPATH, "//Button[normalize-space()='Add']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Desain Grafis")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/i").click().send_keys("I:\\applications\\SanbercodeQA-Kelompok2\\Test_Suite_Admin_Job_JobTilte\\Final Project Batch 42.docx")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
        time.sleep(3)


    

    





    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()