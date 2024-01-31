import tests.conftest as conft
from pages.web_pages.left_menu_page import LeftMenuPage
from pages.web_pages.main_page import MainPage
from pages.web_pages.login_page import LoginPage
from pages.web_pages.server_admin_menu_page import ServerAdminMenuPage
from pages.web_pages.server_admin_new_user import ServerAdminNewUser
from pages.web_pages.server_admin_users import ServerAdminUsersPage
from pages.web_pages.upper_menu_page import UpperMenuPage


#Web Objects
web_login_page = None
web_main_page = None
web_upper_menu_page = None
web_left_menu_page = None
ws_admin_users = None
ws_admin_menu_page = None
ws_admin_new_user = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login_page'] = LoginPage(conft.driver)
        globals()['web_main_page'] = MainPage(conft.driver)
        globals()['web_upper_menu_page'] = UpperMenuPage(conft.driver)
        globals()['web_left_menu_page'] = LeftMenuPage(conft.driver)
        globals()['ws_admin_users'] = ServerAdminUsersPage(conft.driver)
        globals()['ws_admin_menu_page'] = ServerAdminMenuPage(conft.driver)
        globals()['ws_admin_new_user'] = ServerAdminNewUser(conft.driver)

