import tests.conftest as conft
from pages.web_pages.main_page import MainPage
from pages.web_pages.login_page import LoginPage
from pages.web_pages.upper_menu_page import UpperMenuPage


#Web Objects
web_login_page = None
web_main_page = None
web_upper_menu_page = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login_page'] = LoginPage(conft.driver)
        globals()['web_main_page'] = MainPage(conft.driver)
        globals()['web_upper_menu_page'] = UpperMenuPage(conft.driver)
