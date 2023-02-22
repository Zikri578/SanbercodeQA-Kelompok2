import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_edit_description_file_attachment_personal_data(self):
        # steps
        driver = self.browser #buka web browser
        time.sleep(5)
        driver.get("http://opensource-demo.orangehrmlive.com/") # buka situs
        self.browser.maximize_window()
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//i[contains(@class,'oxd-icon bi-pencil-fill')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(100,document.body.scrollHeight)")
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:\\Users\\ASUS\\Downloads\\testfile\\kucing1.jpg")
        time.sleep(3)
        driver.find_element(By.XPATH,"//textarea").send_keys("Uji coba upload gambar")
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(3)
        

    #def tearDown(self):
     #   self.browser.close()

if __name__ == "__main__":
    unittest.main()