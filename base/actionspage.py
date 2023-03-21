from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from utilities.customlogger import custom_logger


class ActionPage:
    log = custom_logger()


    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException))

    def click(self, locatorvalue, locatortype):
        xpath = (By.XPATH, locatorvalue)
        id = (By.ID, locatorvalue)
        name = (By.NAME, locatorvalue)

        if str(locatortype) == "XPATH":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath)).click()
            self.log.info("Click on the element ::"+ locatorvalue)

        elif str(locatortype) == "ID":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(id)).click()
            self.log.info("Click on the element ::"+ locatorvalue)

        elif str(locatortype) == "NAME":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(name)).click()
            self.log.info("Click on the element ::"+ locatorvalue)

    def sendkeys(self, locatorvalue, locatortype, value):
        xpath = (By.XPATH, locatorvalue)
        id = (By.ID, locatorvalue)
        name = (By.NAME, locatorvalue)

        if str(locatortype) == "XPATH":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath)).send_keys(value)
            self.log.info("sent key as  ::  " + value)

        elif str(locatortype) == "ID":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(id)).send_keys(value)
            self.log.info("sent key as  ::  " + value)


        elif str(locatortype) == "NAME":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(name)).send_keys(value)

    def find_elements(self, locatorvalue, locatortype, index_num):

        if str(locatortype) == "XPATH":
            list_name = self.driver.find_elements(By.XPATH, locatorvalue)
            list_name[index_num].click()

    def text(self, locatorvalue, locatortype):
        xpath = (By.XPATH, locatorvalue)

        if str(locatortype) == "XPATH":
            elem_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath)).text
        return elem_text

    def window_handle(self, index_num):
        window_ids = self.driver.window_handles
        self.driver.switch_to.window(window_ids[index_num])
