from selenium.webdriver.common.by import By


class Amazon_delivery_page:
    deliver_t0_this_addrs_locator = (By.XPATH, "//body/div[@class='checkout checkout-as checkout-as-desktop']/div[@class='a-container']/div[@class='clearfix']/div[@id='addres-select']/form[@class='a-nostyle']/div[@class='a-spacing-base address-book']/div[@id='address-book-entry-0']/div[2]/span[1]/a[1]")
    country_dropdown_locator = (By.ID, "a-dropdown-prompt")
    sign_in_ur_accc_locator = (By.XPATH, "//span[contains(text(),'Sign in to your account')]")
    country_name_locator = (By.NAME, "India")
    name_locator = (By.ID, "address-ui-widgets-enterAddressFullName")
    mobile_number_locator = (By.ID, "address-ui-widgets-enterAddressPhoneNumber")
    postal_code_locator = (By.ID, "address-ui-widgets-enterAddressPostalCode")
    flat_no_locator = (By.ID, "address-ui-widgets-enterAddressLine1")
    area_locator = (By.ID, "address-ui-widgets-enterAddressLine2")
    landmark_locator = (By.ID, "address-ui-widgets-landmark")
    city_locator = (By.ID, "address-ui-widgets-enterAddressCity")
    state_dropdown_locator = (By.XPATH, "//span[@id='address-ui-widgets-enterAddressStateOrRegion']//span[@role='button']")
    address_type_dropdown_locator = (By.XPATH, "//span[@id='address-ui-widgets-addr-details-address-type-and-business-hours']//span[@role='button']")
    checkout_this_address_locator = (By.XPATH, "//input[@data-testid='Address_selectShipToThisAddress']")
