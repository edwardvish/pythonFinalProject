from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions

users = (By.CSS_SELECTOR, "a[href='/admin/users'] ")
orgs = (By.CSS_SELECTOR, "a[href='/admin/orgs'] ")
settings = (By.CSS_SELECTOR, "a[href='/admin/settings'] ")
plugins = (By.CSS_SELECTOR, "a[href='/admin/plugins'] ")
stats = (By.CSS_SELECTOR, "a[href='/admin/upgrading'] ")


class ServerAdminMenuPage(UiActions):
    def __init__(self,driver):
        self.driver = driver

    def get_users(self):
        self.find(*users)

    def get_orgs(self):
        self.find(*orgs)

    def get_settings(self):
        self.find(*settings)

    def get_plugins(self):
        self.find(*plugins)

    def get_stats(self):
        self.find(*stats)
