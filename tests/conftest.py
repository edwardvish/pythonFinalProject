import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager



driver = None
browser = 'Chrome'


@pytest.fixture(scope='class')
def init_web_driver(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('http://localhost:3000')
    request.cls.driver = driver
    yield
    driver.close()


def get_web_driver():
    if browser.lower == 'chrome':
        driver = get_chrome()

    elif browser.lower() == 'firefox':
        driver = get_firefox()

    elif browser.lower() == 'edge':
        driver = get_edge()

    else:
        driver = None
        raise Exception('Unrecognised browser type')

    return driver


def get_chrome():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4.x
    return chrome_driver


def get_firefox():
    gecko_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return gecko_driver


def get_edge():
    edge_driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    return edge_driver





