import tests.conftest as conf


class UiActions:
    @staticmethod
    def find(driver, *locator):
        return driver.find_element(*locator)

    @staticmethod
    def find_multiple(driver, *locator):
        return driver.find_elements(*locator)

    @staticmethod
    def click(driver, locator):
        elem = UiActions.find(driver, *locator)
        elem.click()


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
    def drag_n_drop(src, target):
        conf.action.drag_and_drop(src, target).perform()

    @staticmethod
    def right_click(elem):
        conf.action.context_click(elem).perform()

    @staticmethod
    def mouse_hover(elem1, elem2):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()
