from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException


class ActionPage:

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=(ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException))

    def click(self, locatorvalue, locatortype):

        if str(locatortype) == "XPATH":
            self.driver.find_element(By.XPATH, locatorvalue).click()

        elif str(locatortype) == "ID":
            self.driver.find_element(By.ID, locatorvalue).click()

        elif str(locatortype) == "NAME":
            self.driver.find_element(By.NAME, locatorvalue).click()

    def sendKeys(self, locatorvalue, locatortype, value):

        if str(locatortype) == "XPATH":
            self.driver.find_element(By.XPATH, locatorvalue).send_keys(value)

        elif str(locatortype) == "ID":
            self.driver.find_element(By.ID, locatorvalue).send_keys(value)

        elif str(locatortype) == "NAME":
            self.driver.find_element(By.NAME, locatorvalue).send_keys(value)

    def find_elements(self, locatorvalue, locatortype, index_num):

        if str(locatortype) == "XPATH":
            list_name = self.driver.find_elements(By.XPATH, locatorvalue)
            list_name[index_num].click()

    def text(self, locatorvalue, locatortype):

        if str(locatortype) == "XPATH":
            elem_text = self.driver.find_element(By.XPATH, locatorvalue).text
        return elem_text

    def window_handle(self,index_num):
        window_ids = self.driver.window_handles
        self.driver.switch_to.window(window_ids[index_num])

