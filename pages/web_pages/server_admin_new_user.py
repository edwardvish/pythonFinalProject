from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions

menu_drop_down = (By.CSS_SELECTOR, ".gf-form-input.dropdown-toggle")
form_title = (By.XPATH, "//div[@class='page-container page-body']/h1")
name = (By.CSS_SELECTOR, "#name-input")
email = (By.CSS_SELECTOR, "#email-input")
username = (By.CSS_SELECTOR, "#username-input")
password = (By.CSS_SELECTOR, "#password-input")
create_button = (By.CSS_SELECTOR, ".css-sqvqs4-button")


class ServerAdminNewUser(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_dropdown(self):
        return UiActions.find(self.driver, *menu_drop_down)

    def get_form_title(self):
        return UiActions.find(self.driver, *form_title)

    def get_name(self):
        return UiActions.find_multiple(self.driver, *name)

    def set_name(self, value):
        return UiActions.set_text(self.driver, name, value)

    def get_email(self):
        return UiActions.find(self.driver, *email)

    def set_email(self, value):
        return UiActions.set_text(self.driver, email, value)

    def get_username(self):
        return UiActions.find(self.driver, *username)

    def set_username(self, uname):
        return UiActions.set_text(self.driver, username, uname)

    def get_password(self):
        return UiActions.find(self.driver, *password)

    def set_password(self, upass):
        return UiActions.set_text(self.driver, password, upass)

    def get_create_button(self):
        return UiActions.find(self.driver, *create_button)

    def click_create_button(self):
        UiActions.click(self.driver, create_button)
