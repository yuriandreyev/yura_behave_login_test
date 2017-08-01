from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    username = 'username'
    password = 'password'
    login_button = (By.XPATH, ".//*[@id='dijit_form_Form_0']/table/tbody/tr[4]/td[2]/span/input")


class UserPageLocators(object):
    """A class for user page locators. All user page locators should come here"""
    username = (By.XPATH, "//div[contains(text(), 'User: autotest')]")
