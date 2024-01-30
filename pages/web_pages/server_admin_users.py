from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions


class ServerAdminUsersPage(UiActions):
    search = (By.CLASS_NAME, "input[class='css-fcoerl-input-input']")
    new_user = (By.CSS_SELECTOR, "a[href='/admin/orgs'] ")
    users_list = (By.CSS_SELECTOR, "a[href='/admin/settings'] ")
    all_users_radio = (By.XPATH, "//label[text()='All users']")
    active_30_days = (By.XPATH, "//label[text()='Active last 30 days']")

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


