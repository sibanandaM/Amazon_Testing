import pytest
from tests.test_base import BaseTest
from pageobjects.loginpage import LoginPage
from pageobjects.searchpage import SearchPage
from pageobjects.productpage import ProductPage


class Test_ProductResult(BaseTest):

    @pytest.mark.order(3)
    def test_productresult(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.pagination = SearchPage(self.driver)
        self.pagination.search_box()
        self.productresult = ProductPage(self.driver)
        self.productresult.search_product()
        self.productresult.verify_product_details()
