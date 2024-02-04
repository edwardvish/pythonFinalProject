from utils.base_test import BaseTest
from utils.common_ops import get_data, By
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    driver = None

    def test_verify_login(self):
        msg = WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        assert msg.lower() == 'logged in'
        WebFlows.verify_grafana_title('Welcome to Grafana')

    def test_verify_upper_menu(self):
        WebFlows.verify_upper_menu_buttons()

    def test_add_new_user(self):
        WebFlows.open_users_page('Server Admin')
        WebFlows.create_new_user('Add new user','john','john','test@test.com','abc123456')
        WebFlows.create_new_user('Add new user','edward','edward','test2@test.com','2abc123456')
        WebFlows.verify_user_num(3)

    # def test_delete_user_by_index(self):
    #     WebFlows.delete_user_by_index(self.driver, 0)
    #     WebFlows.verify_user_num(2)

    def test_delete_user(self):
        WebFlows.open_users_page('Server Admin')
        WebFlows.delete_user(self.driver, By.USER, 'john')
        WebFlows.delete_user(self.driver, By.INDEX, 1)
        WebFlows.verify_user_num(1)

    def teardown_method(self):
        WebFlows.grafana_home(self.driver)














 