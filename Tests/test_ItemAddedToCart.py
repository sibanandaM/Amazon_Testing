import time

import pytest
from Tests.test_base import BaseTest
from PageObjects.loginPage import LoginPage
from PageObjects.searchPage import SearchPage
from PageObjects.cartPage import cartPage
from PageObjects.addToCartPage import AddToCart
from PageObjects.productPage import ProductPage

class Test_VerifyCartItem(BaseTest):

    @pytest.mark.order(4)
    def test_verifycartitem(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.searchpage = SearchPage(self.driver)
        self.searchpage.search_box()
        self.productpage = ProductPage(self.driver)
        self.productpage.search_product()
        self.actual_product = self.productpage.product_details()
        self.addtocart = AddToCart(self.driver)
        self.addtocart.add_to_cart()
        time.sleep(5)
        self.cartpage = cartPage(self.driver)
        self.cartpage.cart_verify()

        assert self.cartpage.verify_cart_item() in self.actual_product
        """Testing"""