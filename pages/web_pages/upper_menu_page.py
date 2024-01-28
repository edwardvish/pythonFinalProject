from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions


class UpperMenuPage(UiActions):
    general = (By.CLASS_NAME, 'css-mgcb1x')
    home = (By.CLASS_NAME, 'css-alq3f2')
    panel = (By.CSS_SELECTOR, 'button[aria-label="Add Panel"]')
    save_dash = (By.CSS_SELECTOR, "button[aria-label='Save dashboard']")
    dash_settings = (By.CSS_SELECTOR, "button[aria-label='Dashboard settings']")
    view_mode = (By.CSS_SELECTOR, "button[aria-label='Cycle view mode']")

    def get_general(self):
        return self.find(*self.general)

    def get_home(self):
        return self.find(*self.home)

    def get_panel(self):
        return self.find(*self.panel)

    def get_save_dash(self):
        return self.find(*self.save_dash)

    def get_dash_settings(self):
        return self.find(*self.dash_settings)

    def get_view_mode(self):
        return self.find(*self.view_mode)









