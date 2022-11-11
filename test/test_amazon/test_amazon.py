import pytest
import logging

from src import constants
from src.base import TestAmazonBase
from src.common_views import CommonViews
from src.pages.amazon_pages.amzn_header_page import AmazonHeader
from src.pages.amazon_pages.amzn_search_page import Amazon_search_page, Product_details_page
from src.pages.amazon_pages.amzn_delivery_page import Amazon_delivery_page
from src.pages.amazon_pages.amzn_signin_page import Amazon_signin
import time

LOGGER = logging.getLogger("mylogs")
home_page_product_name = "Samsung Galaxy M32 5G (Sky Blue, 6GB RAM, 128GB Storage)"
details_page_product_name = "Samsung Galaxy M32 5G (Sky Blue, 6GB RAM, 128GB Storage)"
quantity = 1


class TestProgram:

    def setup_method(self):
        self.tf = TestAmazonBase("chrome")
        self.cv = CommonViews(self.tf.driver)

    @pytest.mark.order(1)
    # @pytest.mark.skip
    def test_header_validation(self):
        assert self.cv.is_displayed(AmazonHeader.Amazon_logo), "Amazon logo validatation failed"
        assert self.cv.is_displayed(AmazonHeader.Amazon_location), "Amazon location validatation failed"
        assert self.cv.is_displayed(AmazonHeader.Amazon_SearchBox), "Amazon Searchbox validatation failed"
        assert self.cv.is_displayed(AmazonHeader.Amazon_flag), "Amazon Flag validatation failed"
        assert self.cv.is_displayed(AmazonHeader.Amazon_Accounts), "Amazon accounts validatation failed"
        assert self.cv.is_displayed(AmazonHeader.Amazon_orders), "Amazon orders validatation failed"


    @pytest.mark.order(2)
    def test_product_booking_function(self):
        assert self.cv.is_element_present(AmazonHeader.Amazon_SearchBar_locator), "SearchBar_locator not valid"
        self.cv.send_data(AmazonHeader.Amazon_SearchBar_locator, "Samsung Galaxy M32 5g")

        assert self.cv.is_element_present(
            AmazonHeader.Amazon_Search_submit_button_locator), "Amazon_Search_submit_button_locator not valid"
        self.cv.click_objects(AmazonHeader.Amazon_Search_submit_button_locator)

        self.cv.window_scroll_by_element(Amazon_search_page.product_locator, 0, 150)
        assert self.cv.is_element_present(Amazon_search_page.product_locator), "product_locator not valid"
        self.cv.click_objects(Amazon_search_page.product_locator)
        # get all windows , switch to window

        self.cv.switching_windows(1)

        assert home_page_product_name == details_page_product_name, "product name validataion failed"
        self.cv.window_scroll_by_element(Product_details_page.add_to_cart_locator, 0)

        assert self.cv.is_element_present(Product_details_page.add_to_cart_locator), "add_to_cart_locator not valid"
        self.cv.click_objects(Product_details_page.add_to_cart_locator)
        self.cv.click_objects(Product_details_page.go_to_cart_locator)
        # cross check  or use explicit wait
        time.sleep(10)

        self.cv.switching_windows(0)

        assert self.cv.is_element_present(AmazonHeader.home_page_add_cart), "Not found home_page_add_cart_locator"
        self.cv.click_objects(AmazonHeader.home_page_add_cart)

        assert quantity == 1, "validation failed for cart quantitiy"
        self.cv.click_objects(Product_details_page.proceed_to_buy)

        assert self.cv.is_element_present(Amazon_signin.user_name_locator), "user_name_locator not valid"
        self.cv.send_data(Amazon_signin.user_name_locator, constants.username)

        assert self.cv.is_element_present(Amazon_signin.continue_button_locator), "continue_button_locator not valid"
        self.cv.click_objects(Amazon_signin.continue_button_locator)

        assert self.cv.is_element_present(Amazon_signin.password_locator), "password_locator not valid"
        self.cv.send_data(Amazon_signin.password_locator, constants.password)

        assert self.cv.is_element_present(Amazon_signin.sign_in_loccator), "sign_in_loccator not valid"
        self.cv.click_objects(Amazon_signin.sign_in_loccator)

        assert self.cv.is_element_present(
            Amazon_delivery_page.checkout_this_address_locator), "deliver_t0_this_addrs_locator not valid"
        self.cv.click_objects(Amazon_delivery_page.checkout_this_address_locator)

    def teardown_method(self):
        self.cv.close_browser()
