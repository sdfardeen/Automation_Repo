from selenium.webdriver.common.by import By


class AmazonFooter:
    back_to_top = (By.XPATH, "//span[@class='navFooterBackToTopText']")
    # get_us_knw = (By.XPATH, "//div[normalize-space()='Get to Know Us']")
    # cnct_wid_us = (By.XPATH, "//div[normalize-space()='Connect with Us']")
    # mk_mny_wid_us = (By.XPATH, "//div[normalize-space()='Make Money with Us']")
    # let_us_help_u = (By.XPATH, "//div[normalize-space()='Let Us Help You']")
    common_footer_locator1 = "//a[normalize-space()='"
    common_footer_locator2 = "']"
    Get_knw_us= (By.XPATH, "//div[normalize-space()='Get to Know Us']")
    About_us_locator = (By.XPATH, "//a[normalize-space()='About Us']")
    career= (By.XPATH, "//a[normalize-space()='Careers']")
    press_release=(By.XPATH, "//a[normalize-space()='Press Releases']")
    amazon_cares=(By.XPATH, "//a[normalize-space()='Amazon Cares']")
    connect_us=(By.XPATH, "//div[normalize-space()='Connect with Us']")
    facebook_locator=(By.XPATH, "//a[normalize-space()='Facebook']")
    twitter_locator=(By.XPATH, "//a[normalize-space()='Twitter']")
    instagram_locator=(By.XPATH, "//a[normalize-space()='Instagram']")
    make_money_with_us=(By.XPATH, "//div[normalize-space()='Make Money with Us']")
    sell_on_amazon=(By.XPATH, "//a[normalize-space()='Sell on Amazon']")
    Sell_under_Amazon_Accelerator=(By.XPATH, "//a[normalize-space()='Sell under Amazon Accelerator']")
    Amazon_Global_Selling = (By.XPATH, "//a[normalize-space()='Amazon Global Selling']")
    Become_an_Affiliate =(By.XPATH, "//a[normalize-space()='Become an Affiliate']")
    Fulfilment_by_Amazon =(By.XPATH, "//a[normalize-space()='Fulfilment by Amazon']']")
    Advertise_Your_Products =(By.XPATH, "//a[normalize-space()='Advertise Your Products']")
    Amazon_Pay_on_Merchants =(By.XPATH, "//a[normalize-space()='Amazon Pay on Merchants']")
    Let_Us_Help_You=(By.XPATH, "//div[normalize-space()='Let Us Help You']")
    COVID_19=(By.XPATH, "//a[normalize-space()='COVID-19 and Amazon']")
    Your_Account=(By.XPATH, "//a[@class='nav_a'][normalize-space()='Your Account']")
    Returns_Centre=(By.XPATH, "//a[normalize-space()='Returns Centre']")
    Purchase_Protection =(By.XPATH, "//a[normalize-space()='100% Purchase Protection']")
    Amazon_App_Download=(By.XPATH, "//a[normalize-space()='Amazon App Download']")
    Amazon_Assistant_Download=(By.XPATH, "//a[normalize-space()='Amazon Assistant Download']")
    Help=(By.XPATH,"//a[normalize-space()='Help']")
    Amazon_logo = (By.XPATH, "//div[@class='nav-logo-base nav-sprite']")