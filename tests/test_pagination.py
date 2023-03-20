import pytest
import re
from tests.test_base import BaseTest
from pageobjects.loginpage import LoginPage
from pageobjects.searchpage import SearchPage


class Test_Pagination(BaseTest):
    pattern1 = r"\d+\-\d+"
    pattern2 = r"\d+\,\d+"

    @pytest.mark.order(2)
    def test_pagination(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        self.pagination = SearchPage(self.driver)
        self.pagination.search_box()
        pagination = self.pagination.verify_pagination()
        match1 = re.search(self.pattern1, pagination)
        match2 = re.search(self.pattern2, pagination)
        page_no = match1.group()
        total_no = match2.group()
        assert pagination == f"{page_no} of over {total_no} results for mobile"
