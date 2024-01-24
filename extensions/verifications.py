from selenium.common import NoSuchElementException

from extensions.ui_actions import UiActions


class Verifications(UiActions):

    def verify_element_present(self, locator):
        try:
            self.find(*locator)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def verify_equals(expected, actual):
        assert actual == expected, 'Values not equal, the actual: ' + str(actual) + 'the expected is ' + str(expected)

