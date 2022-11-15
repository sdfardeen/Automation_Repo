from selenium.webdriver.common.by import By


class Amazon_search_page:
    dropdown_box_locator = (By.XPATH, "//div[@aria-label='samsung s20 fe 5g mobile']")
    product_locator = (By.XPATH, "//div[contains(@class,'SEARCH_RESULTS widgetId=search-results_3')]//span[contains(text(),'Sky Blue')]")


class Product_details_page:
    product_page_add_to_cart_locator = (By.XPATH, "//input[@id='add-to-cart-button']")
    product_page_go_to_cart_locator = (By.XPATH, "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']")
    product_page_proceed_to_checkout_locator = (By.XPATH, "//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']")
    product_page_side_close_key = (By.ID, "attach-close_sideSheet-link")
    product_page_proceed_to_buy = (By.NAME, "proceedToRetailCheckout")
    product_page_product_in_add_cart_locator = (By.XPATH, "//span[@class='a-truncate-cut'][contains(text(),'Sky Blue, 6GB RAM]")
    shopping_cart_quantity_locator = (By.CLASS_NAME, "a-button-text a-declarative")
