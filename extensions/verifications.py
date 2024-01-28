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


    @staticmethod
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.append(elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed in failed_elems:
                print('Soft Display Failed, Elements failed:' + str(failed))
            raise AssertionError('Soft Display Failed')



