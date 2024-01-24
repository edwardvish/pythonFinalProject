from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from extensions.ui_actions import UiActions


class MainPage(UiActions):
    main_title = (By.CLASS_NAME, 'css-1xodasp')

    def get_main_title(self):
        title = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(*self.main_title))
        return title.text

