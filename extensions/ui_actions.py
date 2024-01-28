
from selenium.webdriver import ActionChains


class UiActions:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set_text(self, locator, value: str):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title()

    def mouse_hover(self, *locators):
        for locator in locators:
            elem = self.find(*locator)
            self.action.move_to_element(elem)
        self.action.perform()

    def right_click(self, locator):
        elem = self.find(locator)
        self.action.context_click(elem).perform()

    def drag_n_drop(self, locator1, locator2):
        src_elem = self.find(*locator1)
        trgt_elem = self.find(*locator2)
        self.action.drag_and_drop(src_elem, trgt_elem).perform()

