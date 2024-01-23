from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from extensions.ui_actions import UiActions


class LoginPage(UiActions):
    user_name = (By.CSS_SELECTOR, 'input[name="user"]')
    password_field = (By.CSS_SELECTOR, '#current-password')
    login_button = (By.CSS_SELECTOR, 'button[aria-label="Login button"]')
    skip_button = (By.LINK_TEXT, 'skip')
    success_login_msg = (By.XPATH, '//div[contains(text(),"Logged in")]')
    failed_login_msg = (By.XPATH, '//div[contains(text(),"Invalid username or password")]')

    # def __init__(self, driver):
    #     super().__init__(driver)

    def set_username(self, user):
        self.set_text(self.user_name, user)

    def set_password(self, password):
        self.set_text(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    def skip(self):
        skip = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(*self.skip_button))
        skip.click()
        return MainPage(self.driver)


















