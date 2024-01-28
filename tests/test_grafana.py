import pytest

from utils.base_test import BaseTest
from utils.common_ops import get_data
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    def test_verify_login(self):
        msg = WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        assert msg.lower() == 'logged in'
        WebFlows.verify_grafana_title('Welcome to Grafana')

