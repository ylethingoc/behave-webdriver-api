from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBase():
    __TIMEOUT__ = 10

    def __init__(self, driver):
        self._driver_wait = WebDriverWait(driver, SeleniumBase.__TIMEOUT__)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()

    def get_title(self):
        return self._driver.title

    def close(self):
        self._driver.close()

