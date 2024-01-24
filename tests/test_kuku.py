import time

import pytest

from extensions.ui_actions import UiActions
from workflows.web_flows import WebFlows


class Test_Web(UiActions):

    def test_verify_login(self):
        message = WebFlows.login_flow('admin', 'admin')
        assert message == 'Logged in'

    def test_kuku(self):
        time.sleep(15)

