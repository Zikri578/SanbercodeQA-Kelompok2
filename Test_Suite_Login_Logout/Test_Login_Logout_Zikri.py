import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Hasilnya : Error
    def test_login_failed_with_invalid_username(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        browser.find_element(By.NAME, "username").send_keys("invalid_username")
        time.sleep(3)

        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(3)

        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME, "oxd-alert oxd-alert--error").text
        self.assertIn('Invalid credentials', response_data)

    # Hasilnya : Error
    def test_login_failed_with_invalid_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        browser.find_element(By.NAME, "username").send_keys("admin")
        time.sleep(3)

        browser.find_element(By.NAME, "password").send_keys("invalid_username")
        time.sleep(3)

        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME, "oxd-alert oxd-alert--error").text
        self.assertIn('Invalid credentials', response_data)

    # Hasilnya : Error
    def test_login_failed_with_empty_username_and_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        browser.find_element(By.NAME, "username").send_keys("")
        time.sleep(3)

        browser.find_element(By.NAME, "password").send_keys("")
        time.sleep(3)

        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME, "oxd-alert oxd-alert--error").text
        self.assertIn('Required', response_data)

    # Hasilnya : Berhasil
    def test_login_Logout_sukses(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(3)

        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(3)

        browser.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(3)

        # validasi
        current_url = browser.current_url
        self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

        # Logout
        browser.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        time.sleep(3)
        browser.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(3)

        # Validasi logout berhasil
        # login_form = browser.find_element(By.CLASS_NAME, "orangehrm-login-slot").text
        # self.assertEqual(login_form, "LOGIN- Login")

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()

# =============================================== Untuk Login Copy Aja Scripnya dibawah ini : ===============================================

# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

#     def test_login_Logout_sukses(self):
#         browser = self.browser
#         browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         time.sleep(3)

#         browser.find_element(By.NAME, "username").send_keys("Admin")
#         time.sleep(3)

#         browser.find_element(By.NAME, "password").send_keys("admin123")
#         time.sleep(3)

#         browser.find_element(By.CLASS_NAME, "oxd-button").click()
#         time.sleep(3)

#         # validasi
#         current_url = browser.current_url
#         self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

#     def tearDown(self): 
#         self.browser.close()

# if __name__ == "__main__": 
#     unittest.main()
# =============================================== Untuk Login Copy Aja Scripnya diatas ini : ===============================================