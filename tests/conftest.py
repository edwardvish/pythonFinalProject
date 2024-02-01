import time

import pytest
import selenium
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.common_ops import get_data
from utils.manage_pages import ManagePages

driver = None
# action = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    timeout = int(get_data('WaitTime'))
    driver.implicitly_wait(timeout)
    driver.get(get_data('URL'))
    request.cls.driver = driver
    # globals()['action'] = ActionChains(request.cls.driver)
    ManagePages.init_web_pages()
    yield
    time.sleep(5)
    driver.close()


def get_web_driver():
    browser = get_data('Browser')
    if browser.lower() == 'chrome':
        driver = get_chrome()

    elif browser.lower() == 'firefox':
        driver = get_firefox()

    elif browser.lower() == 'edge':
        driver = get_edge()

    else:
        driver = None
        raise Exception('Unrecognised browser type')

    return driver
w

def get_chrome():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4.x
    return chrome_driver


def get_firefox():
    gecko_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return gecko_driver


def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Edge(service=srv)
    return edge_driver
