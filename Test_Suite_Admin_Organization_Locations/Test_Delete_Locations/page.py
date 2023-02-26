class elem():

    #Base URL
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    #Page Locations
    admin = "//span[normalize-space()='Admin']"
    org = "//span[normalize-space()='Organization']"
    loc = "//li[normalize-space()='Locations']"

    #Delete Element
    scroll_page = "window.scrollTo(0,document.body.scrollHeight)"
    del_icon = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]"
    del_btn_confirm = "//Button[normalize-space()='Yes, Delete']"
    del_btn_cancel = "//Button[normalize-space()='No, Cancel']"
    del_btn_select = "//Button[normalize-space()= 'Delete Selected']"
    del_checkbox = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/label/span"
    
    #Assert
    del_assert = "//div[normalize-space()='Locations']"