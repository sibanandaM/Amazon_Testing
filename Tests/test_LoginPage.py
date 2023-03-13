import pytest
from Tests.test_base import BaseTest
from PageObjects.loginPage import LoginPage
from  PageObjects.cartPage import cartPage

class Test_Login(BaseTest):

    @pytest.mark.order(1)
    def test_loginpage(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.cartPage = cartPage(self.driver)
        self.cartPage.cart_verify()
        assert self.cartPage.empty_cart() == "Your Amazon Cart is empty."



