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

        #Add Location Element
        add_btn = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        add_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input"
        add_city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
        add_state = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
        add_pos = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input"
        add_slc_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i"
        add_srt_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[101]" #Select Country
        add_telp = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input"
        add_fax = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/div[2]/input"
        add_adrs = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea"
        add_note = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[8]/div/div[2]/textarea"
        add_save_btn = "//button[normalize-space()='Save']"