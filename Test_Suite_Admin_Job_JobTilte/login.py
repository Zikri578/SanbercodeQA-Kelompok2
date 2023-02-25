import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_login_Logout_sukses(self):
    browser = self.browser
    browser.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    browser.find_element(By.NAME, "username").send_keys("Admin")
    time.sleep(3)

    browser.find_element(By.NAME, "password").send_keys("admin123")
    time.sleep(3)

    browser.find_element(By.CLASS_NAME, "oxd-button").click()
    time.sleep(3)

    # validasi
    current_url = browser.current_url
    self.assertEqual(
        current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
