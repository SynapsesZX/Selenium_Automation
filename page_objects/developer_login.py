import time

from page_objects.base_page import BasePage
import locators.login
import globals.info


class DevLogin(BasePage):
    def dev_login(self):
        self.wait_and_click(*locators.login.LOGIN)
        self.send_text_to_element(*locators.login.USERNAME_INPUT_FIELD, text=globals.info.user_login)
        self.check_element_attribute(*locators.login.USERNAME_INPUT_FIELD, attribute='value',
                                     attribute_result=globals.info.user_login)
        self.send_text_to_element(*locators.login.PASSWORD_INPUT_FIELD, text=globals.info.user_password)
        self.check_element_attribute(*locators.login.PASSWORD_INPUT_FIELD, attribute='value',
                                     attribute_result=globals.info.user_password)
        self.is_element_enabled(*locators.login.SUBMIT_BUTTON)
        self.wait_and_click(*locators.login.SUBMIT_BUTTON)
        self.is_element_no_present_with_wait(*locators.login.LOGIN_WINDOW)
