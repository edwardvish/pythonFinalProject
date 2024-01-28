import pytest

from utils.base_test import BaseTest
from workflows.web_flows import WebFlows


class TestWeb(BaseTest):
    def test_verify_login(self):
        msg = WebFlows.login_flow('admin', 'admin')
        assert msg.lower() == 'logged in'
        WebFlows.verify_grafana_title('Welcome to Grafana')

