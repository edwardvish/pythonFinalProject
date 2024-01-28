from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import tests.conftest as conft
import xml.etree.ElementTree as ET


def get_data(node_name):
    tree = ET.parse('C:/pythonProject/FinalProject/pythonProject/configuration/data.xml')
    root = tree.getroot()
    return root.find('.//' + node_name).text


def wait_for_element(oper, locator):
    timeout = int(get_data('WaitTime'))
    try:
        if oper == 'exists':
            WebDriverWait(conft.driver, timeout).until(ec.presence_of_element_located(locator))
        elif oper == 'displayed':
            WebDriverWait(conft.driver, timeout).until(ec.visibility_of_element_located(locator))

    except NoSuchElementException:
        print("Element not found on the page.")


# Enum for selecting either displayed or existing element on page
class Oper:
    Element_Exists = 'exists'
    Element_Displayed = 'displayed'



