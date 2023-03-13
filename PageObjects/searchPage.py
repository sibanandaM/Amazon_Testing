from Base.ActionsPage import ActionPage
from Configuration.TestData import TestData

class SearchPage(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_box_IT = "//input[@id ='twotabsearchtextbox']"
    search_submit_BTN = "//input[@id ='nav-search-submit-button']"
    pagination_text_1 = "//span[contains(text(),'of over')]"
    pagination_text_2 = "//span[@class='a-color-state a-text-bold']"

    def search_box(self):
        self.sendKeys(self.search_box_IT, "XPATH", TestData.search_data)
        self.click(self.search_submit_BTN,"XPATH")

    def verify_pagination(self):
        self.pagination1 = self.text(self.pagination_text_1,"XPATH")
        self.pagination2 = self.text(self.pagination_text_2,"XPATH")
        self.pagination = self.pagination1+" "+self.pagination2[1:-2]

        return self.pagination
