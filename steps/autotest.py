"""This module tests login feature of https://www.dispatch.navitel.ru/"""

import page
from behave import *
from selenium.webdriver.common.keys import Keys


@given('web page is opened')
def step_impl(context):

    context.driver.get('https://www.dispatch.navitel.ru/')
    # Checks if the text "Navitel Dispatch" is in the title
    assert 'Navitel Dispatch' in context.driver.title, "dispatch.navitel.ru title doesn't match."


@when('set username "{login}", password "{password}" to fields and press Enter')
def step_impl(context, login, password):
    """Tests login feature of 'https://www.dispatch.navitel.ru/'. Detects username in the page after login."""
    main_page = page.MainPage(context.driver)
    main_page.username = login  # Sending username to username textbox.
    main_page.password = password  # Sending password to password textbox.
    main_page.password = Keys.RETURN  # Press Enter
    # context.main_page.click_login_button()  # Clicking login button does not work


@then('user can see his account page')
def step_impl(context):
    """Function tests if authorization was successful"""
    user_page = page.UserPage(context.driver)
    assert user_page.is_login_ok(), "login have not been successful"



