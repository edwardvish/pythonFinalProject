import utils.manage_pages as page
from extensions.ui_actions import ActionUtils
from extensions.verifications import Verifications
from utils.common_ops import wait_for_element, Oper
# from pages.web_pages.main_page import MainPage


class WebFlows():
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
        wait_for_element(Oper.Element_Displayed, page.MainPage.main_title)
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

    @staticmethod
    def open_users_page(expected: str):
        # locate the server admin element in the left menu page
        elem1 = page.web_left_menu_page.get_server_admin_menu()
        elem2 = page.ws_admin_menu_page.get_users()
        # mouse hover the icon and click on the users
        ActionUtils.mouse_hover(elem1, elem2)
        # wait for page to load, extract the title.
        wait_for_element(Oper.Element_Displayed,page.ws_admin_users.title)
        actual = page.ws_admin_users.get_main_title()
        # verify server admin users page is loaded.
        Verifications.verify_equals(actual, expected)

    @staticmethod
    def create_new_user():
        pass


