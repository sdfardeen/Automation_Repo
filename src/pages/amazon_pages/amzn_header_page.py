from selenium.webdriver.common.by import By


class AmazonHeader:
    Amazon_logo = (By.ID, "nav-logo-sprites")
    Amazon_location = (By.ID, "nav-global-location-popover-link")
    Amazon_SearchBox = (By.ID, "nav-search")
    Amazon_SearchBar_locator = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    Amazon_Search_submit_button_locator = (By.ID, "nav-search-submit-button")
    Amazon_flag = (By.ID, "icp-nav-flyout")
    Amazon_Accounts = (By.ID, "nav-link-accountList")
    Amazon_orders = (By.ID, "nav-orders")
    home_page_add_cart = (By.ID, "nav-cart")
