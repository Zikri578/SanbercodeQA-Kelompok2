class elem():
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
        src_btn = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
