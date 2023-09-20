from page_objects.base_page import BasePage
import locators.login
import globals.info


class AdminLogin(BasePage):
    def admin_login(self):
        self.send_text_to_element(*locators.login.USERNAME_INPUT_FIELD, text=globals.info.admin_login)
        self.send_text_to_element(*locators.login.PASSWORD_INPUT_FIELD, text=globals.info.admin_password)
        self.is_element_enabled(*locators.login.SUBMIT_BUTTON)
        self.wait_and_click(*locators.login.SUBMIT_BUTTON)
        self.is_element_no_present_with_wait(*locators.login.LOGIN_WINDOW)
