from selenium.webdriver.common.by import By


class Amazon_search_page:
    dropdown_box_locator = (By.XPATH, "//div[@aria-label='samsung s20 fe 5g mobile']")
    product_locator = (By.XPATH, "//div[contains(@class,'SEARCH_RESULTS widgetId=search-results_3')]//span[contains(text(),'Sky Blue')]")


class Product_details_page:
    add_to_cart_locator = (By.XPATH, "//input[@id='add-to-cart-button']")
    go_to_cart_locator = (By.XPATH, "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']")
    proceed_to_checkout_locator = (By.XPATH, "//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']")
    side_close_key = (By.XPATH, "//a[@id='attach-close_sideSheet-link']")
    proceed_to_buy = (By.XPATH, "//input[@name='proceedToRetailCheckout']")
    product_in_add_cart_locator = (By.XPATH, "//span[@class='a-truncate-cut'][contains(text(),'Sky Blue, 6GB RAM]")
    quantity_locator = (By.XPATH, "//span[@class='a-button-text a-declarative']")
