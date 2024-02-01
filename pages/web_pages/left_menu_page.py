from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions

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


class LeftMenuPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_grafana_home(self):
        return UiActions.find(self.driver, *grafana_home)

    def get_search_dashboards(self):
        return UiActions.find(self.driver, *search_dashboards)

    def get_create_dashboard(self):
        return UiActions.find(self.driver, *create_dashboard)

    def get_dashboards_menu(self):
        return UiActions.find(self.driver, *dashboards_menu)

    def get_explore(self):
        return UiActions.find(self.driver, *explore)

    def get_alerting_menu(self):
        return UiActions.find(self.driver, *alerting_menu)

    def get_configuration_menu(self):
        return UiActions.find(self.driver, *configuration_menu)

    def get_server_admin_menu(self):
        return UiActions.find(self.driver, *server_admin_menu)

    def get_profile_menu(self):
        return UiActions.find(self.driver, *profile_menu)

    def get_help_menu(self):
        return UiActions.find(self.driver, *help_menu)
