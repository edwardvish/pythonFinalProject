
from utils.base_test import BaseTest
from utils.common_ops import get_data
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):

    def test_verify_login(self):
        msg = WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        assert msg.lower() == 'logged in'
        WebFlows.verify_grafana_title('Welcome to Grafana')

    def test_verify_upper_menu(self):
        WebFlows.verify_upper_menu_buttons()

    def test_add_new_user(self):
        WebFlows.open_users_page('Server Admin')
        WebFlows.create_new_user('Add new user','Edward','Edward1','test@test.com','abc123456')
        WebFlows.create_new_user('Add new user','Edward2','Edward3','test2@test.com','2abc123456')
        WebFlows.verify_user_num(3)







 