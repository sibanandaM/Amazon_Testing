from Base.ActionsPage import ActionPage


class AddToCart(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    addTocart_BTN = "//input[@id='add-to-cart-button']"
    close_slider_BTN = "//a[@id='attach-close_sideSheet-link']"

    def add_to_cart(self):
        self.click(self.addTocart_BTN,"XPATH")
        self.click(self.close_slider_BTN,"XPATH")
