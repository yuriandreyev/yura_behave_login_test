"""This module tests login feature of https://www.dispatch.navitel.ru/"""

import page
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@given('web page is opened')
def set_driver(context):
    """Webdriver initialization"""
    context.driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    context.driver.get('https://www.dispatch.navitel.ru/')
    # Load the main page. In this case the home page of dispatch.navitel.ru.
    context.main_page = page.MainPage(context.driver)
    # Checks if the text "Navitel Dispatch" is in title
    assert context.main_page.is_title_matches(), "dispatch.navitel.ru title doesn't match."


@when('set username, password to fields and press Enter')
def authorization(context):
    """Tests login feature of 'https://www.dispatch.navitel.ru/'. Detects username in the page after login."""
    context.main_page.username = 'autotest'  # Sending username to username textbox.
    context.main_page.password = '111111'  # Sending password to password textbox.
    context.main_page.password = Keys.RETURN  # Press Enter
    # context.main_page.click_login_button()  # Clicking login button does not work


@then('user can see his account page')
def test_userpage(context):
    """Function tests if authorization was successful"""
    user_page = page.UserPage(context.driver)
    assert user_page.is_login_ok(), "login have not been successful"


@then('browser should be closed')
def close_browser(context):
    context.driver.close()



