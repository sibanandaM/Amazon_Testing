from base.actionspage import ActionPage
from configuration.testdata import TestData


class LoginPage(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    signin_btn = "//span[text()='Hello, sign in']"
    username_tb = "//input[@id='ap_email']"
    continue_btn = "//input[@id='continue']"
    password_tb = "//input[@id='ap_password']"
    submit_btn = "//input[@id='signInSubmit']"

    def login(self):
        self.click(self.signin_btn, "XPATH")
        self.sendkeys(self.username_tb, "XPATH", TestData.user_name)
        self.click(self.continue_btn, "XPATH")
        self.sendkeys(self.password_tb, "XPATH", TestData.password)
        self.click(self.submit_btn, "XPATH")
