import logging
import os
from configparser import ConfigParser

from helper.web.initial_browser import get_browser


def before_all(context):
    logging.basicConfig(level=logging.INFO)

    config = ConfigParser()
    logging.info(os.path.join(os.getcwd(), 'setup.cfg'))
    my_file = os.path.join(os.getcwd(), 'setup.cfg')
    config.read(my_file)

    driver = get_browser(config.get('environment', 'browser'))
    context.driver = driver


def after_all(context):
    context.driver.close()
