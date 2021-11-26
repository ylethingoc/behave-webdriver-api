import logging
import os

from helper.web.initial_browser import get_browser


def before_feature(context, feature):
    logging.basicConfig(level=logging.INFO)
    if 'web' in feature.name.lower():
        driver = get_browser(os.environ['browser'])
        context.driver = driver


def after_feature(context, feature):
    if 'web' in feature.name.lower():
        context.driver.close()
