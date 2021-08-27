from behave import *
import os
from configparser import ConfigParser


config = ConfigParser()


@given("We have a Spotify's user and password")
def step_impl(context):
    my_file = os.path.join(os.getcwd(), 'setup.cfg')
    config.read(my_file)
    context.user = config.get('spotify', 'user')
    context.passwd = config.get('spotify', 'password')


@when("We visit {url}")
def step_impl(context, url):
    context.driver.open(url)
    context.driver.maximize()


@step("We hit on the {button_name} button")
def step_impl(context, button_name):
    if button_name.lower() == 'get_token':
        locator = "//button[contains(text(), 'Get Token')]"
        context.driver.click(locator)
    elif button_name.lower() == 'request_token':
        locator = "//input[@type='submit']"
        context.driver.click_by_javascript(locator)
    elif button_name.lower() == 'login':
        locator = "//button[@id='login-button']"
        context.driver.click(locator)
    elif button_name.lower() == 'accept':
        locator = "//button[@id='auth-accept']"
        context.driver.wait_and_click(locator)


@step("We navigate to {name} page")
def step_impl(context, name):
    locator = None
    if name.lower() == 'login':
        locator = "//button[@id='login-button']"
    elif name.lower() == 'accept':
        locator = "//h1[contains(text(), 'Spotify for Developers')]"
    context.driver.is_element_visible(locator)


@step("We select option Login with Google")
def step_impl(context):
    locator = "//a[@analytics-event='Google Button']"
    context.driver.click(locator)


@step("We input user and password to login")
def step_impl(context):
    user = "//input[@name='username']"
    password = "//input[@name='password']"
    context.driver.send_keys(user, context.user)
    context.driver.send_keys(password, context.passwd)


@then("We get the OAuth Token")
def step_impl(context):
    locator = "//input[@id='oauth-input']"
    context.oauth = context.driver.get_attribute(locator, 'value')


@step("We store this token into setup.cfg file")
def step_impl(context):
    config.set('spotify', 'Token', str(context.oauth))
    with open('setup.cfg', 'w') as token:
        config.write(token)