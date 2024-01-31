from selenium.webdriver.common.by import By
from extensions.ui_actions import UiActions


class ServerAdminNewUser(UiActions):
    menu_drop_down = (By.CSS_SELECTOR, ".gf-form-input.dropdown-toggle")
    form_title = (By.XPATH, "//div[@class='page-container page-body']/h1'] ")
    name = (By.XPATH, "#name-input")
    email = (By.XPATH, "#email-input")
    username = (By.XPATH, "#username-input")
    password = (By.XPATH, "#password-input")
    create_button = (By.CSS_SELECTOR, ".css-sqvqs4-button")

    def get_dropdown(self):
        self.find(*self.menu_drop_down)

    def get_form_title(self):
        self.find(*self.form_title)

    def get_name(self):
        self.find_multiple(*self.name)

    def get_email(self):
        self.find(*self.email)

    def get_username(self):
        self.find(*self.username)

    def get_password(self):
        self.find(*self.password)

    def get_create_button(self):
        self.find(*self.create_button)






