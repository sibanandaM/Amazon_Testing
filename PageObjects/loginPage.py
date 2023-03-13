from Base.ActionsPage import ActionPage
from Configuration.TestData import TestData

class LoginPage(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    signin_BTN = "//span[text()='Hello, sign in']"
    username_TB = "//input[@id='ap_email']"
    continue_BTN = "//input[@id='continue']"
    password_TB = "//input[@id='ap_password']"
    submit_BTN = "//input[@id='signInSubmit']"

    def login(self):
        self.click(self.signin_BTN,"XPATH")
        self.sendKeys(self.username_TB, "XPATH", TestData.user_name)
        self.click(self.continue_BTN, "XPATH")
        self.sendKeys(self.password_TB, "XPATH", TestData.password)
        self.click(self.submit_BTN, "XPATH")


