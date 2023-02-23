class elem():
        #Base URL
        base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        #Page Locations
        admin = "//span[normalize-space()='Admin']"
        org = "//span[normalize-space()='Organization']"
        loc = "//li[normalize-space()='Locations']"

        #Search Element
        src_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"
        src_city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
        slc_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]"
        srt_slc_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[39]"
        srt_slc_wrong_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[30]" #Select Country
        src_btn = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
        src_reset_btn = "//button[@class= 'oxd-button oxd-button--medium oxd-button--ghost']"
      
        #Assert
        src_assert_a = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_b = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_c = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_d = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_e = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_f = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_g = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_h = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
        src_assert_i = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]"