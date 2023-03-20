from base.actionspage import ActionPage


class AddToCart(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    addtocart_btn = "//input[@id='add-to-cart-button']"
    close_slider_btn = "//a[@id='attach-close_sideSheet-link']"

    def add_to_cart(self):
        self.click(self.addtocart_btn, "XPATH")
        self.click(self.close_slider_btn, "XPATH")
