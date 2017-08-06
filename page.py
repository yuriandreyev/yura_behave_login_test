"""This module contains Page Object classes."""
from element import BasePageElement
from element import ButtonElement
from locators import MainPageLocators
from locators import UserPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UsernameField(BasePageElement):
    """This class gets the username textbox from the specified locator"""
    locator = MainPageLocators.username


class PasswordField(BasePageElement):
    """This class gets the password textbox from the specified locator"""
    locator = MainPageLocators.password


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. dispatch.navitel.ru"""
    username = UsernameField()  # this attribute will take login
    password = PasswordField()  # this attribute will take password

    def title(self):
        """Verifies that  text "Navitel Dispatch" appears in page title"""
        return self.driver.title

    def click_login_button(self):
        """Method checks if login button is clickable and click it."""

        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='dijit_form_Form_0']/"
                                                                  "table/tbody/tr[4]/td[2]/span/input")),
                            message="Can't click login button")
        '''
        login_button = ButtonElement(self.driver, MainPageLocators.login_button)
        login_button = login_button.find_button()
        login_button.click()
        '''
        button.click()


class UserPage(BasePage):
    """This page describes dispatch.navitel.ru after successful login"""

    def is_login_ok(self):
        """Tests if login was successful by looking for user's name"""
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*UserPageLocators.username),
                                                 message="Can't see user cabinet")
            return True
        except Exception:
            return False
