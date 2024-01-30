from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions


class ServerAdminMenuPage(UiActions):
    users = (By.CSS_SELECTOR, "a[href='/admin/users'] ")
    orgs = (By.CSS_SELECTOR, "a[href='/admin/orgs'] ")
    settings = (By.CSS_SELECTOR, "a[href='/admin/settings'] ")
    plugins = (By.CSS_SELECTOR, "a[href='/admin/plugins'] ")
    stats = (By.CSS_SELECTOR, "a[href='/admin/upgrading'] ")

    def get_users(self):
        self.find(*self.users)

    def get_orgs(self):
        self.find(*self.orgs)

    def get_settings(self):
        self.find(*self.settings)

    def get_plugins(self):
        self.find(*self.plugins)

    def get_stats(self):
        self.find(*self.stats)
