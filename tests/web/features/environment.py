import logging
import os

from helper.web.initial_browser import get_browser


def before_all(context):
    logging.basicConfig(level=logging.INFO)
    driver = get_browser(os.environ['browser'])
    context.driver = driver


def after_all(context):
    context.driver.close()
