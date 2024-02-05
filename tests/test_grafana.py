import pytest

from utils.base_test import BaseTest
from utils.common_ops import get_data, By, read_csv, SearchBy
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    driver = None
    user_data = WebFlows.user_data

    def test_verify_login(self):
        msg = WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        assert msg.lower() == 'logged in'
        WebFlows.verify_grafana_title('Welcome to Grafana')

    def test_verify_upper_menu(self):
        WebFlows.verify_upper_menu_buttons()

    # def test_add_new_user(self):
    #     WebFlows.open_users_page('Server Admin')
    #     WebFlows.create_new_user('Add new user', 'john', 'john', 'test@test.com', 'abc123456')
    #     WebFlows.create_new_user('Add new user', 'edward', 'edward', 'test2@test.com', '2abc123456')
    #     WebFlows.verify_user_num(3)

    # def test_delete_user_by_index(self):
    #     WebFlows.delete_user_by_index(self.driver, 0)
    #     WebFlows.verify_user_num(2)

    def test_add_new_users(self):
        WebFlows.open_users_page('Server Admin')
        for i in range(3):  # Assuming you want to add 3 users
            user = self.user_data[i]  # Get the user data
            WebFlows.create_new_user('Add new user', user['Name'], user['Username'], user['Email'], user['Password'])
        WebFlows.verify_user_num(4)

    def test_user_filtering(self):
        WebFlows.open_users_page('Server Admin')
        for item in range(3):
            WebFlows.search_user(self.driver, SearchBy.UNAME, item)
            WebFlows.verify_user_num(1)

    def test_delete_user(self):
        WebFlows.open_users_page('Server Admin')
        WebFlows.delete_user(self.driver, By.USER, 'Daniel Hernandez')
        # WebFlows.delete_user(self.driver, By.INDEX, 1)
        WebFlows.verify_user_num(3)

    def teardown_method(self):
        WebFlows.grafana_home(self.driver)
