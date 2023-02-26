class elem():

    #Base URL
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    #Page Locations
    admin = "//span[normalize-space()='Admin']"
    org = "//span[normalize-space()='Organization']"
    loc = "//li[normalize-space()='Locations']"

    #Elemen
    edit_icon_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]"
    edit_city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    edit_slc_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]"
    edit_search_country = "//div[@class='oxd-select-dropdown --positon-bottom']//span[normalize-space()='Gabon']" #Select Country
    edit_phone = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input"
    edit_btn_save = "//Button[normalize-space() = 'Save']"
    edit_btn_cancel = "//Button[normalize-space() = 'Cancel']"

    #Assert
    edit_assert = "//p[normalize-space()='OrangeHRM OS 5.3']"
    edit_fail_assert = "//span[normalize-space()='Should not exceed 50 characters']"
    edit_cancel_assert = "//div[normalize-space()='Locations']"