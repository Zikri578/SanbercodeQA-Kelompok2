class elem():
        #Base URL
        base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        #Page Locations
        admin = "//span[normalize-space()='Admin']"
        org = "//span[normalize-space()='Organization']"
        loc = "//li[normalize-space()='Locations']"

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
        add_cancel_btn = "//button[normalize-space()='Cancel']"

        #Add Assert
        add_assert_a = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]"
        add_assert_b = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]"
        add_assert_c = "//span[normalize-space()='Required']"
        add_assert_d = "//span[normalize-space()='Should not exceed 50 characters']"
        add_assert_e = "//span[normalize-space()='Allows numbers and only + - / ( )']"
        add_assert_f = "//span[normalize-space()='Already exists']"