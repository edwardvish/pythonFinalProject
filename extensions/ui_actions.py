
from selenium.webdriver import ActionChains

from tests.conftest import action


class UiActions:
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_multiple(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def select_dropdown(self, locator1, locator2):
        self.click(locator1)
        self.click(locator2)

    def set_text(self, locator, value: str):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title()

# There is a separation between the UIActions and the ActionsUtils:

# UiActions focuses on interactions with web elements specific
# to the state of a page, which is typical in Page Object Model (POM) design.

# ActionUtils provides utility functions for generic actions
# that are not tied to a specific page's state.


class ActionUtils:
    @staticmethod
    def mouse_hover(elem1, elem2):
        action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    def right_click(elem):
        action.context_click(elem).perform()

    @staticmethod
    def drag_n_drop(src, target):
        action.drag_and_drop(src, target).perform()



