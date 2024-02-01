from selenium.webdriver import ActionChains


class UiActions:
    @staticmethod
    def find(driver, *locator):
        return driver.find_element(*locator)

    @staticmethod
    def find_multiple(driver, *locator):
        return driver.find_elements(*locator)

    @staticmethod
    def click(driver, locator):
        UiActions.find(driver, *locator).click()

    @staticmethod
    def select_dropdown(driver, locator1, locator2):
        UiActions.click(driver, locator1)
        UiActions.click(driver, locator2)

    @staticmethod
    def set_text(driver, locator, value: str):
        element = UiActions.find(driver, *locator)
        element.clear()
        element.send_keys(value)

    @staticmethod
    def get_text(driver, locator):
        return UiActions.find(driver, *locator).text

    @staticmethod
    def get_title(driver):
        return driver.title()

    @staticmethod
    def drag_n_drop(driver, src, target):
        action = ActionChains(driver)
        action.drag_and_drop(src, target).perform()

    @staticmethod
    def right_click(driver, elem):
        action = ActionChains(driver)
        action.context_click(elem).perform()

    @staticmethod
    def mouse_hover(driver, elem1, elem2):
        action = ActionChains(driver)
        action.move_to_element(elem1).move_to_element(elem2).click().perform()
