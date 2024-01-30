import utils.manage_pages as page
from extensions.verifications import Verifications
from utils.common_ops import wait_for_element, Oper
from pages.web_pages.main_page import MainPage


class WebFlows:
    @staticmethod
    def login_flow(user: str, password: str):
        # page.web_login_page.set_username(user)
        # page.web_login_page.set_password(password)
        # page.web_login_page.click_login_button()
        # login_msg = page.web_login_page.get_login_message()
        login_msg = page.web_login_page.login_to_app(user, password)
        page.web_login_page.click_skip()
        return login_msg

    @staticmethod
    def verify_grafana_title(expected: str):
        wait_for_element(Oper.Element_Displayed, MainPage.main_title)
        actual = page.web_main_page.get_main_title()
        Verifications.verify_equals(actual, expected)

    @staticmethod
    def verify_upper_menu_buttons():
        elems = [page.web_upper_menu_page.get_general(),
                 page.web_upper_menu_page.get_home(),
                 page.web_upper_menu_page.get_save_dash(),
                 page.web_upper_menu_page.get_dash_settings(),
                 page.web_upper_menu_page.get_view_mode(),
                 ]
        # Verifications.soft_displayed(elems)
        Verifications.soft_assert(elems)







