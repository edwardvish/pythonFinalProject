import pages
import utils.manage_pages as page
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from pages.web_pages.server_admin_users import ServerAdminUsersPage
from utils.common_ops import wait_for_element, Oper
# from pages.web_pages.main_page import MainPage


class WebFlows:
    def __init__(self, driver):
        self.ui_actions = UiActions(driver)
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
        # ui_actions = UiActions(driver)
        # locate the server admin element in the left menu page
        elem1 = page.web_left_menu_page.get_server_admin_menu()
        elem2 = page.ws_admin_menu_page.get_users()
        # mouse hover the icon and click on the users
        UiActions.mouse_hover(elem1, elem2)
        # wait for page to load, extract the title.
        wait_for_element(Oper.Element_Displayed,page.ws_admin_users.title)
        actual = page.ws_admin_users.get_main_title()
        # verify server admin users page is loaded.
        Verifications.verify_equals(actual.lower(), expected.lower())

    @staticmethod
    def create_new_user(expected: str, name: str, user : str, email: str, password: str):
        # locate and click the new user form
        page.ws_admin_users.open_new_user_from()
        # wait for the form to load and get the form title
        wait_for_element(Oper.Element_Displayed,page.ws_admin_new_user.form_title)
        # store and compare the title is as expected
        actual = page.ws_admin_new_user.get_form_title()
        Verifications.verify_equals(actual, expected)
        # set all form fields
        page.ws_admin_new_user.set_name(name)
        page.ws_admin_new_user.set_email(email)
        page.ws_admin_new_user.set_username(user)
        page.ws_admin_new_user.set_password(password)
        page.ws_admin_new_user.click_create()

    @staticmethod
    def verify_user_num(number):

        if number > 0:
            wait_for_element(Oper.Element_Displayed, ServerAdminUsersPage.users_list)
            actual = page.ws_admin_users.get_users_list()
            Verifications.verify_num_of_elements(actual, number)









