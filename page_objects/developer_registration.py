import time

import globals.info
from page_objects.base_page import BasePage
import locators.developer_registration
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class DeveloperRegistration(BasePage):

    def click_the_start_now_button(self):
        self.wait_and_click(*locators.developer_registration.START_NOW_BUTTON)
        step_header = self.get_element_text(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)
        assert step_header == 'Create your account 1 of 4 steps'
        next_button = self.get_element_attribute(*locators.developer_registration.NEXT_BUTTON, attribute='class')
        assert 'p-disabled' in next_button

    def write_valid_data_in_the_email_input_field(self):
        self.clear_input_field(*locators.developer_registration.EMAIL_INPUT_FIELD)
        self.send_text_to_element(*locators.developer_registration.EMAIL_INPUT_FIELD,
                                  text=BasePage.randomWord_mails(value=7))

    def write_the_already_registered_email_input_field(self):
        self.send_text_to_element(*locators.developer_registration.EMAIL_INPUT_FIELD,
                                  text=('igorzyabrov2050@gmail.com'))

    def this_email_is_already_registered_error_hint_appears(self):
        already_registered_username_hint = self.get_element_text(
            *locators.developer_registration.ALREADY_REGISTERED_EMAIL_ERROR_HINT)
        assert already_registered_username_hint == "We found a user with this e-mail address. If this is you, please log in."

    def write_data_in_the_username_input_field(self):
        self.send_text_to_element(*locators.developer_registration.USERNAME_INPUT_FIELD,
                                  text=BasePage.randomWord(value=10))

    def write_the_already_registered_user_in_the_username_input_field(self):
        self.clear_input_field(*locators.developer_registration.USERNAME_INPUT_FIELD)
        self.send_text_to_element(*locators.developer_registration.USERNAME_INPUT_FIELD,
                                  text=('igor'))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def this_user_is_already_registered_error_hint_appears(self):
        already_registered_username_hint = self.get_element_text(
            *locators.developer_registration.ALREADY_REGISTERED_USERNAME_ERROR_HINT)
        assert already_registered_username_hint == "This Username is already exists"

    def write_data_in_the_first_name_input_field(self):
        self.send_text_to_element(*locators.developer_registration.FIRST_NAME_INPUT_FIELD,
                                  text=BasePage.randomWord(value=10))

    def write_data_in_the_last_name_input_field(self):
        self.send_text_to_element(*locators.developer_registration.LAST_NAME_INPUT_FIELD,
                                  text=BasePage.randomWord(value=10))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_valid_data_in_the_mobile_input_field(self):
        self.send_text_to_element(*locators.developer_registration.MOBILE_PHONE_INPUT_FIELD,
                                  text=BasePage.random_with_N_digits(value=12))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_data_in_the_mobile_input_field(self):
        self.send_text_to_element(*locators.developer_registration.MOBILE_PHONE_INPUT_FIELD,
                                  text=BasePage.random_with_N_digits(value=3))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def phone_validation_error_hint_appears(self):
        phone_validation_hint = self.get_element_text(*locators.developer_registration.MOBILE_VALIDATION_ERROR_HINT)
        assert phone_validation_hint == 'Please use this pattern phone +1 (123) 456-7890'

    def next_button_is_displayed_as_active(self):
        self.wait_until_element_will_be_clickable(*locators.developer_registration.NEXT_BUTTON)
        next_button_active = self.get_element_attribute(*locators.developer_registration.NEXT_BUTTON, attribute='class')
        assert 'p-disabled' not in next_button_active

    def click_the_next_button(self):
        self.wait_and_click(*locators.developer_registration.NEXT_BUTTON)

    def write_invalid_data_in_the_email_input_field(self):
        self.send_text_to_element(*locators.developer_registration.EMAIL_INPUT_FIELD,
                                  text=BasePage.randomWord(value=7))

    def the_next_button_displayed_as_inactive(self):
        next_button_inactive = self.get_element_attribute(*locators.developer_registration.NEXT_BUTTON,
                                                          attribute='class')
        assert 'p-disabled' in next_button_inactive

    def email_validation_error_hint_appears(self):
        email_error_text = self.get_element_text(*locators.developer_registration.EMAIL_ERROR_HINT)
        assert email_error_text == 'E-mail address should be contain a valid email address'

    def remove_data_from_email_input_field(self):
        self.clear_input_field(*locators.developer_registration.EMAIL_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def email_address_is_required_error_hint_appears(self):
        email_is_required_error_hint = self.get_element_text(
            *locators.developer_registration.EMAIL_IS_REQUIRED_ERROR_HINT)
        assert email_is_required_error_hint == 'E-mail address is required'

    def remove_data_from_username_input_field(self):
        self.clear_input_field(*locators.developer_registration.USERNAME_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def username_is_required_error_hint_appears(self):
        email_is_required_error_hint = self.get_element_text(
            *locators.developer_registration.USERNAME_IS_REQUIRED_ERROR_HINT)
        assert email_is_required_error_hint == 'Username is required'

    def remove_data_from_first_name_input_field(self):
        self.clear_input_field(*locators.developer_registration.FIRST_NAME_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def first_name_is_required_error_hint_appears(self):
        email_is_required_error_hint = self.get_element_text(
            *locators.developer_registration.FIRST_NAME_IS_REQUIRED_ERROR_HINT)
        assert email_is_required_error_hint == 'First name is required'

    def remove_data_from_last_name_input_field(self):
        self.clear_input_field(*locators.developer_registration.LAST_NAME_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def last_name_is_required_error_hint_appears(self):
        email_is_required_error_hint = self.get_element_text(
            *locators.developer_registration.LAST_NAME_IS_REQUIRED_ERROR_HINT)
        assert email_is_required_error_hint == 'Last name is required'

    def write_valid_password_in_the_password_input_field(self):
        self.send_text_to_element(*locators.developer_registration.PASSWORD_INPUT_FIELD, text='I5594176960infqy!')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_password_in_the_confirm_password_input_field(self):
        self.send_text_to_element(*locators.developer_registration.CONFIRM_PASSWORD_INPUT_FIELD,
                                  text='I5594176960infqy')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def confirm_password_does_not_match_error_hint_appears(self):
        self.is_element_present(*locators.developer_registration.CONFIRM_PASSWORD_ERROR_HINT)

    def write_valid_password_in_the_confirm_password_input_field(self):
        self.send_text_to_element(*locators.developer_registration.CONFIRM_PASSWORD_INPUT_FIELD,
                                  text='I5594176960infqy!')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_password_in_the_password_input_field_without_uppercase_letter(self):
        self.clear_input_field(*locators.developer_registration.PASSWORD_INPUT_FIELD)
        self.send_text_to_element(*locators.developer_registration.PASSWORD_INPUT_FIELD, text='5594176960infqy!')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_password_in_the_password_input_field_without_number(self):
        self.clear_input_field(*locators.developer_registration.PASSWORD_INPUT_FIELD)
        self.send_text_to_element(*locators.developer_registration.PASSWORD_INPUT_FIELD, text='infqydfgdfgdfgG')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_password_in_the_password_input_field_without_symbol(self):
        self.clear_input_field(*locators.developer_registration.PASSWORD_INPUT_FIELD)
        self.send_text_to_element(*locators.developer_registration.PASSWORD_INPUT_FIELD, text='infqydfgdfgdfgG1')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_password_range_in_the_password_input(self):
        self.clear_input_field(*locators.developer_registration.PASSWORD_INPUT_FIELD)
        self.send_text_to_element(*locators.developer_registration.PASSWORD_INPUT_FIELD, text='w')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def invalid_password_error_hint_appears_for_uppercase_letter(self):
        assert self.is_element_present(*locators.developer_registration.PASSWORD_VALIDATION_ERROR_HINT_UPPER_CASE)

    def invalid_password_error_hint_appears_for_number(self):
        assert self.is_element_present(*locators.developer_registration.PASSWORD_VALIDATION_ERROR_HINT_NUMBER)

    def invalid_password_error_hint_appears_for_symbol(self):
        assert self.is_element_present(*locators.developer_registration.PASSWORD_VALIDATION_ERROR_HINT_SYMBOL)

    def invalid_password_range_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.PASSWORD_RANGE_ERROR_HINT)

    def write_data_in_the_company_name_input_field(self):
        self.send_text_to_element(*locators.developer_registration.COMPANY_NAME_INPUT_FIELD, text="softserve")
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def clear_data_from_company_name_input_field(self):
        self.clear_input_field(*locators.developer_registration.COMPANY_NAME_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def company_name_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.COMPANY_NAME_REQUIRED_ERROR_HINT)

    def company_name_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.COMPANY_NAME_REQUIRED_ERROR_HINT)

    def write_valid_url_in_the_company_website_input_field(self):
        self.send_text_to_element(*locators.developer_registration.COMPANY_WEB_SITE_URL_INPUT_FIELD,
                                  text="https://www.google.com/")
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_invalid_url_in_the_company_website_input_field(self):
        self.send_text_to_element(*locators.developer_registration.COMPANY_WEB_SITE_URL_INPUT_FIELD,
                                  text="httpswww.google")
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)
        assert self.is_element_present(*locators.developer_registration.COMPANY_INVALID_URL_ERROR_HINT)

    def clear_data_from_company_website_input_field(self):
        self.clear_input_field(*locators.developer_registration.COMPANY_WEB_SITE_URL_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def company_website_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.COMPANY_WEB_SITE_REQUIRED_ERROR_HINT)

    def company_url_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(
            *locators.developer_registration.COMPANY_WEB_SITE_REQUIRED_ERROR_HINT)

    def upload_company_logo(self):
        self.upload_the_file(*locators.developer_registration.COMPANY_LOGO_INPUT,
                             file_part='D:\Automation\images\company_logo.png')

    def upload_invalid_company_logo(self):
        self.upload_the_file(*locators.developer_registration.COMPANY_LOGO_INPUT,
                             file_part='D:\Automation\images\invalid_company_logo.jpg')
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)
        invalid_company_logo_error_hint = self.get_element_text(
            *locators.developer_registration.COMPANY_LOGO_SIZE_ERROR_HINT)
        assert invalid_company_logo_error_hint == "Max size 1MB"

    def write_data_in_the_description_input_field(self):
        self.send_text_to_element(*locators.developer_registration.DESCRIPTION_TEXT_AREA,
                                  text=BasePage.randomWord(value=15))

        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def clear_data_from_company_description_text_area(self):
        self.clear_input_field(*locators.developer_registration.DESCRIPTION_TEXT_AREA)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def company_description_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.DESCRIPTION_IS_REQUIRED_ERROR_HINT)

    def company_description_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(
            *locators.developer_registration.DESCRIPTION_IS_REQUIRED_ERROR_HINT)

    def select_country_without_state(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.select_element_from_list(*locators.developer_registration.COUNTRY_DROP_DOWN_LIST, value=0)

    def select_canada_country(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.js_click(*locators.developer_registration.CANADA_COUNTRY)

    def select_india_country(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.js_click(*locators.developer_registration.INDIA_COUNTRY)

    def select_united_states_country(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.js_click(*locators.developer_registration.USA_COUNTRY)

    def write_data_in_the_city_input_field(self):
        self.send_text_to_element(*locators.developer_registration.CITY_INPUT_FIELD, text=BasePage.randomWord(value=10))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_data_in_the_postal_code_input_field(self):
        self.send_text_to_element(*locators.developer_registration.POSTAL_CODE_INPUT_FIELD,
                                  text=BasePage.randomWord(value=10))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def write_data_in_the_address_input_field(self):
        self.send_text_to_element(*locators.developer_registration.ADDRESS_INPUT_FIELD,
                                  text=BasePage.randomWord(value=10))
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def accept_the_terms_and_code_development_rules(self):
        self.js_click(*locators.developer_registration.TERMS_CHECKBOX)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def step4_modal_window_disappears(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.STEP4_MODAL)

    def success_modal_window_appears(self):
        success_header = self.get_element_text(*locators.developer_registration.SUCCESS_HEADER)
        assert success_header == 'Success'
        assert self.is_element_present(*locators.developer_registration.SUCCESS_CLOSE_BUTTON)
        confirmation_text = self.get_element_text(*locators.developer_registration.CONFIRMATION_TEXT)
        assert confirmation_text == 'A confirmation e-mail message has been sent to the address you provided. Please verify your address via the link provided in that message.'

    def clear_city_input_field(self):
        self.clear_input_field(*locators.developer_registration.CITY_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def clear_postal_code_input_field(self):
        self.clear_input_field(*locators.developer_registration.POSTAL_CODE_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def clear_address_input_field(self):
        self.clear_input_field(*locators.developer_registration.ADDRESS_INPUT_FIELD)
        self.wait_and_click(*locators.developer_registration.CREATE_YOUR_ACCOUNT_STEPS_HEADER)

    def city_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.CITY_IS_REQUIRED_ERROR_HINT)

    def city_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.CITY_IS_REQUIRED_ERROR_HINT)

    def postal_code_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.POSTAL_CODE_IS_REQUIRED_ERROR_HINT)

    def postal_code_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.POSTAL_CODE_IS_REQUIRED_ERROR_HINT)

    def address_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.ADDRESS_IS_REQUIRED_ERROR_HINT)

    def address_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.ADDRESS_IS_REQUIRED_ERROR_HINT)

    def terms_is_required_error_hint_appears(self):
        assert self.is_element_present(*locators.developer_registration.TERMS_IS_REQUIRED_ERROR_HINT)

    def terms_is_required_error_hint_disappears(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.TERMS_IS_REQUIRED_ERROR_HINT)

    def state_module_is_displayed(self):
        assert self.is_element_present(*locators.developer_registration.STATE_DROP_DOWN_TRIGGER)

    def state_module_is_not_displayed(self):
        self.is_element_no_present_with_wait(*locators.developer_registration.STATE_DROP_DOWN_TRIGGER)

    def select_state(self):
        self.wait_and_click(*locators.developer_registration.STATE_DROP_DOWN_TRIGGER)
        self.select_element_from_list(*locators.developer_registration.STATE_DROP_DOWN_LIST, value=0)

    def check_the_country_list(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        element = self.driver.find_elements(By.CSS_SELECTOR, '.p-dropdown-items li.p-dropdown-item')
        country_list = []
        for result in element:
            country_list.append(result.text)
        assert country_list == globals.info.country_list

    def check_the_state_list_with_selected_canada_country(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.js_click(*locators.developer_registration.CANADA_COUNTRY)
        self.wait_and_click(*locators.developer_registration.STATE_DROP_DOWN_TRIGGER)
        element = self.driver.find_elements(By.CSS_SELECTOR, '.p-dropdown-items li')
        country_list = []
        for result in element:
            country_list.append(result.text)
        assert country_list == globals.info.canada_states

    def check_the_state_list_with_selected_india_country(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.js_click(*locators.developer_registration.INDIA_COUNTRY)
        self.wait_and_click(*locators.developer_registration.STATE_DROP_DOWN_TRIGGER)
        element = self.driver.find_elements(By.CSS_SELECTOR, '.p-dropdown-items li')
        country_list = []
        for result in element:
            country_list.append(result.text)
        assert country_list == globals.info.india_states

    def check_the_state_list_with_selected_united_states_country(self):
        self.wait_and_click(*locators.developer_registration.COUNTRY_DROP_DOWN_TRIGGER)
        self.js_click(*locators.developer_registration.USA_COUNTRY)
        self.wait_and_click(*locators.developer_registration.STATE_DROP_DOWN_TRIGGER)
        element = self.driver.find_elements(By.CSS_SELECTOR, '.p-dropdown-items li')
        country_list = []
        for result in element:
            country_list.append(result.text)
        assert country_list == globals.info.united_states
