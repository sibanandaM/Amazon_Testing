import pytest
from Tests.test_base import BaseTest
from PageObjects.loginPage import LoginPage
from PageObjects.searchPage import SearchPage

class Test_Pagination(BaseTest):

    @pytest.mark.order(2)
    def test_pagination(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.pagination = SearchPage(self.driver)
        self.pagination.search_box()
        assert self.pagination.verify_pagination() == "1-16 of over 6,000 results for mobile"



