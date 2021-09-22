from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from helper.web import SeleniumBase


def get_browser(browser):
    if browser == 'chrome':
        return SeleniumBase(webdriver.Chrome(ChromeDriverManager().install()))
    elif browser == 'firefox':
        return SeleniumBase(webdriver.Firefox(executable_path=GeckoDriverManager().install()))
    elif browser == 'edge':
        return SeleniumBase(webdriver.Edge(EdgeChromiumDriverManager().install()))
    else:
        raise (Exception('{} browser not supported'.format(browser)))
