from selenium.webdriver.common.by import By

class Amazon_signin:
    user_name_locator = (By.ID, "ap_email")
    continue_button_locator = (By.XPATH, "//input[@id='continue']")
    password_locator = (By.ID, "ap_password")
    sign_in_loccator = (By.ID, "signInSubmit")
