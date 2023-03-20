from base.actionspage import ActionPage
from configuration.testdata import TestData


class CartPage(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cart_btn = "//span[@id='nav-cart-count']"
    empty_cart_lt = "//h1[@class='a-spacing-mini a-spacing-top-base']"
    cart_product_lt = "//span[@class='a-truncate-full a-offscreen']/following::span"
    cart_item_delete_btn = "//input[@value='Delete']"

    def cart_verify(self):
        self.click(self.cart_btn, "XPATH")

    def empty_cart(self):
        self.empty_cart = self.text(self.empty_cart_lt, "XPATH")
        return self.empty_cart

    def verify_cart_item(self):
        cart_product_title = self.text(self.cart_product_lt, "XPATH")
        return cart_product_title[:-2]

    def delete_cart_item(self):
        self.click(self.cart_item_delete_btn, "XPATH")
