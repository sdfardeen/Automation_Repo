from selenium.webdriver.common.by import By


class Amazon_delivery_page:
    address_page_deliver_t0_this_addrs_locator = (By.XPATH, "//body/div[@class='checkout checkout-as checkout-as-desktop']/div[@class='a-container']/div[@class='clearfix']/div[@id='addres-select']/form[@class='a-nostyle']/div[@class='a-spacing-base address-book']/div[@id='address-book-entry-0']/div[2]/span[1]/a[1]")
    address_page_country_dropdown_locator = (By.ID, "a-dropdown-prompt")
    sign_in_ur_accc_locator = (By.XPATH, "//span[contains(text(),'Sign in to your account')]")
    address_page_country_name_locator = (By.NAME, "India")
    address_page_name_locator = (By.ID, "address-ui-widgets-enterAddressFullName")
    address_page_mobile_number_locator = (By.ID, "address-ui-widgets-enterAddressPhoneNumber")
    address_page_postal_code_locator = (By.ID, "address-ui-widgets-enterAddressPostalCode")
    address_page_flat_no_locator = (By.ID, "address-ui-widgets-enterAddressLine1")
    address_page_area_locator = (By.ID, "address-ui-widgets-enterAddressLine2")
    address_page_landmark_locator = (By.ID, "address-ui-widgets-landmark")
    address_page_city_locator = (By.ID, "address-ui-widgets-enterAddressCity")
    address_page_state_dropdown_locator = (By.XPATH, "//span[@id='address-ui-widgets-enterAddressStateOrRegion']//span[@role='button']")
    address_page_address_type_dropdown_locator = (By.XPATH, "//span[@id='address-ui-widgets-addr-details-address-type-and-business-hours']//span[@role='button']")
    address_page_checkout_this_address_locator = (By.XPATH, "//input[@data-testid='Address_selectShipToThisAddress']")
