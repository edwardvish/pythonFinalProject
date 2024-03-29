from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions

title = (By.CSS_SELECTOR, '.page-header__title')
search = (By.CSS_SELECTOR, "input[class='css-fcoerl-input-input']")
new_user = (By.CSS_SELECTOR, ".css-1mhnkuh")
users_list = (By.XPATH, "//table[@class='filter-table form-inline filter-table--hover']/tbody/tr")
all_users = (By.XPATH, "//label[text()='All users']")
active_30_days = (By.XPATH, "//label[text()='Active last 30 days']")
delete_user = (By.XPATH, "//div/button[@class='css-19vct9a-button']")
delete_dialog = (By.CSS_SELECTOR, ".css-14jhtpp-modalHeader")
dialog_confirm_delete = (By.CSS_SELECTOR, "button[aria-label='Confirm Modal Danger Button']")


class ServerAdminUsersPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        page_title = UiActions.get_text(self.driver, title)
        return page_title

    # def get_search(self):
    #     return self.find(*self.search)

    def get_new_user(self):
        return UiActions.find(self.driver, *new_user)

    def open_new_user_from(self):
        UiActions.click(self.driver, new_user)

    def get_users_list(self):
        return UiActions.find_multiple(self.driver, *users_list)

    # def get_all_users(self):
    #     return self.find(*self.all_users)

    def get_user_by_index(self, index):
        return self.get_users_list()[index]

    def get_user_by_name(self, name):
        elem = f"//a[@title='{str(name)}']"
        user_by_user_name = (By.XPATH, elem)
        return UiActions.find(self.driver, *user_by_user_name)

    # def get_active_30_days(self):
    #     return self.find(*self.active_30_days)

    # def get_delete_user(self):
    #     return self.find(*self.delete_user)

    # def get_delete_dialog(self):
    #     return self.find(*self.delete_dialog)

    # def get_confirm_delete(self):
    #     return self.find(*self.dialog_confirm_delete)
