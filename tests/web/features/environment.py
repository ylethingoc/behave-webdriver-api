import logging
import os
from configparser import ConfigParser

from helper.web.initial_browser import get_browser


def before_all(context):
    config = ConfigParser()
    logging.info(os.path.join(os.getcwd(), 'setup.cfg'))
    my_file = os.path.join(os.getcwd(), 'setup.cfg')
    config.read(my_file)

    # Reading the browser type from the setup.cfg
    driver = get_browser(config.get('environment', 'browser'))
    context.driver = driver


def after_all(context):
    context.driver.close()
