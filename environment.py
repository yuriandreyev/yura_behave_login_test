from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Firefox()  # Webdriver initialization
    # context.driver = webdriver.Chrome()


def after_scenario(context, scenario):
    context.driver.close()
