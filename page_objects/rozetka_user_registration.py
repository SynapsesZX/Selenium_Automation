from page_objects.base_page import BasePage
from faker import Faker
import locators.rozetka_reg_user


class RozetkaUserRegistration(BasePage):
    f = Faker('Uk')

    def click_user_reg_icon(self):
        self.wait_and_click(*locators.rozetka_reg_user.REG_ICON)

    def click_user_reg_button(self):
        self.js_click(*locators.rozetka_reg_user.REG_BUTTON)

    def user_name_input_is_empty(self):
        self.check_input_field_empty_state(*locators.rozetka_reg_user.USERNAME_INPUT_FIELD)

    def registration_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTRATION_LABEL)

    def first_name_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTER_NAME_LABEL)

    def first_name_input_field_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.USERNAME_INPUT_FIELD)

    def surname_name_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTER_SURNAME_LABEL)

    def last_name_input_field_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.SURNAME_INPUT_FIELD)

    def phone_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTER_USER_PHONE_LABEL)

    def phone_input_field_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.USER_PHONE_INPUT_FIELD)

    def email_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTER_USER_EMAIL_LABEL)

    def email_input_field_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.USER_EMAIL_INPUT_FIELD)

    def password_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTER_USER_PASSWORD_LABEL)

    def password_input_field_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.USER_PASSWORD_INPUT_FIELD)

    def hide_password_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.HIDER_PASSWORD_BUTTON)

    def register_rules_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.USER_FORM_CAPTION)

    def personal_data_link_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.PERSONAL_DATA_LINK)

    def privacy_data_link_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.PRIVACY_LINK)

    def register_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTER_BUTTON)

    def registered_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.REGISTERED_BUTTON)

    def registration_divider_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.MODAL_DIVIDER)

    def social_label_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.SOCIAL_LABEL)

    def facebook_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.FACEBOOK_BUTTON)

    def google_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.GOOGLE_BUTTON)

    def close_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.CLOSE_BUTTON)

    def vacancy_button_is_displayed(self):
        self.check_element_is_displayed_ui(*locators.rozetka_reg_user.VACANCY_BUTTON)

    def write_valid_data_in_first_name_input_field(self):
        self.send_text_to_element(*locators.rozetka_reg_user.USERNAME_INPUT_FIELD,
                                  text=RozetkaUserRegistration.f.first_name())

    def write_valid_data_in_last_name_input_field(self):
        self.send_text_to_element(*locators.rozetka_reg_user.SURNAME_INPUT_FIELD,
                                  text=RozetkaUserRegistration.f.last_name())

    def write_valid_data_in_phone_input_field(self):
        self.send_text_to_element(*locators.rozetka_reg_user.USER_PHONE_INPUT_FIELD,
                                  text='066' + RozetkaUserRegistration.f.phone_number())

    def write_valid_data_in_email_input_field(self):
        self.send_text_to_element(*locators.rozetka_reg_user.USER_EMAIL_INPUT_FIELD,
                                  text=RozetkaUserRegistration.f.email())

    def write_valid_data_in_password_input_field(self):
        self.send_text_to_element(*locators.rozetka_reg_user.USER_PASSWORD_INPUT_FIELD,
                                  text=RozetkaUserRegistration.f.password())

    def click_the_register_button(self):
        self.wait_and_click(*locators.rozetka_reg_user.REGISTER_BUTTON)
