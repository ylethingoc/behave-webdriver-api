import logging
import os
from behave import *
from configparser import ConfigParser

from helper.web import locators
from helper import constants
from helper.web.initial_browser import get_browser


logging.basicConfig(level=logging.INFO)


@given("We have a Spotify's user and password")
def step_impl(context):
    context.user = os.environ['user']
    context.passwd = os.environ['password']
    logging.info("User: " + str(context.user))
    logging.info("Password: " + str(context.passwd))


@when("We visit Spotify Develop website")
def step_impl(context):
    context.driver = get_browser(os.environ['browser'])
    context.driver.open(constants.SPOTIFY_TOKEN)
    context.driver.maximize()


@step("We hit on the {button_name} button")
def step_impl(context, button_name):
    if button_name.lower() == 'get_token':
        context.driver.click_by_javascript(locators.get_token)
    elif button_name.lower() == 'request_token':
        context.driver.click_by_javascript(locators.request_token)
    elif button_name.lower() == 'login':
        context.driver.click(locators.login)
    elif button_name.lower() == 'accept':
        context.driver.wait_and_click(locators.accept)


@step("We navigate to {name} page")
def step_impl(context, name):
    if name.lower() == 'login':
        assert context.driver.is_element_visible(locators.login)
    elif name.lower() == 'accept':
        assert context.driver.is_element_visible(locators.accept_page_text)


@step("We input user and password to login")
def step_impl(context):
    context.driver.send_keys(locators.user, context.user)
    context.driver.send_keys(locators.password, context.passwd)


@then("We get the OAuth Token")
def step_impl(context):
    context.oauth = context.driver.get_attribute(locators.token_box, 'value')


@step("We store this token into token.cfg file")
def step_impl(context):
    config = ConfigParser()
    config.read('token.cfg')
    config.set('spotify', 'token', str(context.oauth))
    with open('token.cfg', 'w') as token:
        config.write(token)
        token.close()
    context.driver.close()
