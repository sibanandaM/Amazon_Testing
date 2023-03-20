import pytest
from tests.test_base import BaseTest
from pageobjects.loginpage import LoginPage
from pageobjects.cartpage import CartPage


class TestLoginPage(BaseTest):
    @pytest.mark.order(1)
    def test_loginpage(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.cartPage = CartPage(self.driver)
        self.cartPage.cart_verify()
        assert self.cartPage.empty_cart() == "Your Amazon Cart is empty."
