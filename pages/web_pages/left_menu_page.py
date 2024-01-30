from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from extensions.ui_actions import UiActions
from utils.common_ops import get_data


class LeftMenuPage(UiActions):
    grafana_home = (By.CSS_SELECTOR, "a[aria-label='Home']")
    search_dashboards = (By.CSS_SELECTOR, "button[aria-label='Search dashboards']")
    create_dashboard = (By.CSS_SELECTOR, "a[aria-label='Create']")
    dashboards_menu = (By.CSS_SELECTOR, "a[aria-label='Dashboards']")
    explore = (By.CSS_SELECTOR, "a[aria-label='Explore']")
    alerting_menu = (By.CSS_SELECTOR, "a[aria-label='Alerting']")
    configuration_menu = (By.CSS_SELECTOR, "a[aria-label='Configuration']")
    server_admin_menu = (By.CSS_SELECTOR, "a[aria-label='Server Admin']")
    profile_menu = (By.CSS_SELECTOR, "a[aria-label='admin']")
    help_menu = (By.CSS_SELECTOR, "a[aria-label='Help']")

    def get_grafana_home(self):
        self.find(*self.grafana_home)

    def get_search_dashboards(self):
        self.find(*self.search_dashboards)

    def get_create_dashboard(self):
        self.find(*self.create_dashboard)

    def get_dashboards_menu(self):
        self.find(*self.dashboards_menu)

    def get_explore(self):
        self.find(*self.explore)

    def get_alerting_menu(self):
        self.find(*self.alerting_menu)

    def get_configuration_menu(self):
        self.find(*self.configuration_menu)

    def get_server_admin_menu(self):
        self.find(*self.server_admin_menu)

    def get_profile_menu(self):
        self.find(*self.profile_menu)

    def get_help_menu(self):
        self.find(*self.help_menu)
