import time
import pytest
from tests.test_base import BaseTest
from pageobjects.loginpage import LoginPage
from pageobjects.searchpage import SearchPage
from pageobjects.cartpage import CartPage
from pageobjects.addtocartpage import AddToCart
from pageobjects.productpage import ProductPage


class Test_RemoveItemFromCart(BaseTest):

    @pytest.mark.order(5)
    def test_verifyremoveitem(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.searchpage = SearchPage(self.driver)
        self.searchpage.search_box()
        self.productpage = ProductPage(self.driver)
        self.productpage.search_product()
        self.addtocart = AddToCart(self.driver)
        self.addtocart.add_to_cart()
        time.sleep(5)
        self.cartpage = CartPage(self.driver)
        self.cartpage.cart_verify()
        self.cartpage.delete_cart_item()

        assert self.cartpage.empty_cart() == "Your Amazon Cart is empty."
