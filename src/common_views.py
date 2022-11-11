from selenium.common.exceptions import NoSuchElementException


class CommonViews:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        # import pdb;pdb.set_trace()
        return self.driver.title

    def is_displayed(self, locators):
        return self.driver.find_element(*locators).is_displayed()

    def click_objects(self, locators):
        self.driver.find_element(*locators).click()

    def send_data(self, locators, data):
        self.driver.find_element(*locators).send_keys(data)

    def maximize_window(self):
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()

    def window_scroll_by_element(self, locator, start_pos=0, end_pos=100):

        element_not_found = True
        start_value, end_value = start_pos, end_pos
        while element_not_found:
            self.driver.execute_script("window.scrollTo({}, {})".format(start_value, end_value))
            try:
                self.driver.find_element(*locator).is_displayed()
                element_not_found = False
            except NoSuchElementException as e:
                start_value += end_pos
                end_value += end_pos
                pass
        return element_not_found

    def window_scroll_up(self):
        self.driver.execute_script("window.scroll(0, 0);")

    def window_scroll_till_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();","")

    def switching_windows(self, position):
        self.driver.switch_to.window(self.driver.window_handles[position])

    def is_element_present(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False
