from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from extensions.ui_actions import UiActions


class LoginPage(UiActions):
    user_name = (By.CSS_SELECTOR, 'input[name="user"]')
    password_field = (By.CSS_SELECTOR, '#current-password')
    login_button = (By.CSS_SELECTOR, 'button[aria-label="Login button"]')
    skip_button = (By.CLASS_NAME, 'css-2vac51-button')
    success_login_msg = (By.XPATH, '//div[contains(text(),"Logged in")]')
    failed_login_msg = (By.XPATH, '//div[contains(text(),"Invalid username or password")]')

    def set_username(self, user):
        self.set_text(self.user_name, user)

    def set_password(self, password):
        self.set_text(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    def login_to_app(self, user, password):
        self.set_username(user)
        self.set_password(password)
        self.click_login_button()
        message = self.get_login_message()
        return message

    def click_skip(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.skip_button)).click()
        # return MainPage

    def get_login_message(self):
        try:
            msg_elem = self.get_text(self.success_login_msg)
            return str(msg_elem)
        except NoSuchElementException:
            try:
                msg_elem = self.get_text(self.failed_login_msg)
                return str(msg_elem)
            except NoSuchElementException:
                return "Login message not found"



















