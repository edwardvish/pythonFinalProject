import utils.manage_pages as page
from extensions.verifications import Verifications


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
        actual = page.web_main_page.get_main_title()
        Verifications.verify_equals(actual, expected)





