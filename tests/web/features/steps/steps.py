from behave import *


@when('We visit dev.to')
def step_impl(context):
    context.driver.open('http://www.dev.to')
    context.driver.maximize()


@then('It should have a title "DEV Community"')
def step_impl(context):
    title = context.driver.get_title()
    assert "DEV Community" in title, 'Wrong title! {} not in {}'.format("'DEV Community'",  "'" + title + "'")
