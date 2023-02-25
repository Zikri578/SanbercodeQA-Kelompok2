class elem():

    #Base URL
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    #Page Locations
    admin = "//span[normalize-space()='Admin']"
    org = "//span[normalize-space()='Organization']"
    loc = "//li[normalize-space()='Locations']"

    #Elemen
    edit_slc_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]"
    edit_search_country = "//div[@class='oxd-select-dropdown --positon-bottom']//span[normalize-space()='Indonesia']" #Select Country
