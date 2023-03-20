import time

import pytest
from tests.test_base import BaseTest
from pageobjects.loginpage import LoginPage
from pageobjects.searchpage import SearchPage
from pageobjects.cartpage import CartPage
from pageobjects.addtocartpage import AddToCart
from pageobjects.productpage import ProductPage


class TestVerifyCartItem(BaseTest):

    @pytest.mark.order(4)
    def test_verify_cart_item(self):
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
        self.cartpage = CartPage(self.driver)
        self.cartpage.cart_verify()

        assert self.cartpage.verify_cart_item() in self.actual_product
