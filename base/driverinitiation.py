from selenium import webdriver
from configuration.testdata import TestData
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Driver:

    def getDriverMethod(self):
        ser_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser_obj)
        driver.get(TestData.base_url)
        driver.maximize_window()
        driver.implicitly_wait(15)
        return driver
