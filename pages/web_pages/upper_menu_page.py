from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions


class UpperMenuPage(UiActions):
    general = (By.LINK_TEXT, 'General')
    home = (By.LINK_TEXT, 'Home')
    panel = (By.CSS_SELECTOR, 'button[aria-label="Add Panel"]')
    save_dash = (By.CSS_SELECTOR, 'button[aria-label="Save Dashboard"]')
    dash_settings = (By.CSS_SELECTOR, 'button[aria-label="Dashboard Settings"]')
    view_mode = (By.CSS_SELECTOR, 'button[aria-label="Cycle view mode"]')

    def get_general(self):
        return self.find(self.general)

    def get_home(self):
        return self.find(self.home)

    def get_panel(self):
        return self.find(self.panel)

    def get_save_dash(self):
        return self.find(self.save_dash)

    def get_dash_settings(self):
        return self.find(self.dash_settings)


    def get_dash_settings(self):
        return self.find(self.dash_settings)






