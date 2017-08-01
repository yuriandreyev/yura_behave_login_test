"""This module defines class which is common to all pages elements"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to field"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, value):
        pass


class ButtonElement(object):
    """This class will be common to all buttons on pages"""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(self.locator),
                          message="Can't click button")
