from base.actionspage import ActionPage
from configuration.testdata import TestData


class ProductPage(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_product_img = "//div[@class='s-main-slot s-result-list s-search-results sg-row']//span[@class='a-size-medium a-color-base a-text-normal']"
    product_title_text = "//span[@id = 'productTitle']"
    product_price_text = "//span[@class = 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span[2]/span[2]"
    product_rating_text = "//a[@id ='acrCustomerReviewLink']/span"

    def search_product(self):
        self.find_elements(self.search_product_img, "XPATH", 0)
        self.window_handle(1)

    def verify_product_details(self):
        product_title = self.text(self.product_title_text, "XPATH")
        print("Product title is :", product_title)
        product_price = self.text(self.product_price_text, "XPATH")
        print("Product price is :", product_price)
        product_rating = self.text(self.product_rating_text, "XPATH")
        print("Product rating is :", product_rating)

    def product_details(self):
        product_title = self.text(self.product_title_text, "XPATH")
        return product_title
