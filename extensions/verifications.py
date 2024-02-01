from selenium.common import NoSuchElementException
from smart_assertions import *

from extensions.ui_actions import UiActions


class Verifications(UiActions):

    def verify_element_present(self, locator):
        try:
            self.find(*locator)
            return True
        except NoSuchElementException:
            return print('Element ', str(locator),' not found')

    @staticmethod
    def verify_equals(expected, actual):
        assert actual == expected, 'Values not equal, the actual: ' + str(actual) + 'the expected is ' + str(expected)

    # Verify Menu Buttons Flow using smart-assertions
    @staticmethod
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()


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

    @staticmethod
    def verify_num_of_elements(users, actual):
        assert len(users) == actual, 'The number of elements in list:' + str(len(users)) + 'does not match expected'



