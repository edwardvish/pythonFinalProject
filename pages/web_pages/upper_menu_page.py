from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions

general = (By.CLASS_NAME, 'css-mgcb1x')
home = (By.CLASS_NAME, 'css-alq3f2')
panel = (By.CSS_SELECTOR, 'button[aria-label="Add Panel"]')
save_dash = (By.CSS_SELECTOR, "button[aria-label='Save dashboard']")
dash_settings = (By.CSS_SELECTOR, "button[aria-label='Dashboard settings']")
view_mode = (By.CSS_SELECTOR, "button[aria-label='Cycle view mode']")
class UpperMenuPage(UiActions):
    def __init__(self, driver):
        self.driver = driver

    def get_general(self):
        return UiActions.find(self.driver,*general)

    def get_home(self):
        return UiActions.find(self.driver,*home)

    def get_panel(self):
        return UiActions.find(self.driver,*panel)

    def get_save_dash(self):
        return UiActions.find(self.driver,*save_dash)

    def get_dash_settings(self):
        return UiActions.find(self.driver,*dash_settings)

    def get_view_mode(self):
        return UiActions.find(self.driver,*view_mode)









