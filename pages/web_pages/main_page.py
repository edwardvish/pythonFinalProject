from selenium.webdriver.common.by import By

from extensions.ui_actions import UiActions


class MainPage(UiActions):
    main_title = (By.CLASS_NAME, 'css-1aanzv4')

    def get_main_title(self):
        title = self.get_text(self.main_title)
        return title



