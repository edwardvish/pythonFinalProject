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
        return self.find(*self.menu_drop_down)

    def get_form_title(self):
        return self.find(*self.form_title)

    def get_name(self):
        return self.find_multiple(*self.name)

    def set_name(self, name):
        return self.set_text(self.name, name)

    def get_email(self):
        return self.find(*self.email)

    def set_email(self, email):
        return self.set_text(self.email,email)

    def get_username(self):
        return self.find(*self.username)

    def set_username(self, username):
        return self.set_text(self.name, username)

    def get_password(self):
        return self.find(*self.password)

    def set_password(self, password):
        return self.set_text(self.password, password)

    def get_create_button(self):
        return self.find(*self.create_button)

    def click_create_button(self):
        return self.click(self.create_button)








