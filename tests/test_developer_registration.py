import time

import pytest
import allure

from page_objects.developer_registration import DeveloperRegistration


class TestDeveloperRegistration:

    @allure.severity('medium')
    @allure.description('developer registration with valid data step 1')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_step_1(self, driver):
        user = DeveloperRegistration(driver)
        user.open_link("https://qa-h360-marketplace.softservetest.com/developer")
        user.click_the_start_now_button()
        user.write_valid_data_in_the_email_input_field()
        user.write_data_in_the_username_input_field()
        user.write_data_in_the_first_name_input_field()
        user.write_data_in_the_last_name_input_field()
        user.write_valid_data_in_the_mobile_input_field()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()

    @allure.severity('medium')
    @allure.description('developer registration with invalid data step 1')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_required_data_step_1(self, driver):
        user = DeveloperRegistration(driver)
        user.open_link("https://qa-h360-marketplace.softservetest.com/developer")
        user.click_the_start_now_button()
        user.write_invalid_data_in_the_email_input_field()
        user.write_data_in_the_username_input_field()
        user.write_data_in_the_first_name_input_field()
        user.write_data_in_the_last_name_input_field()
        user.email_validation_error_hint_appears()
        user.write_invalid_data_in_the_mobile_input_field()
        user.phone_validation_error_hint_appears()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with empty required data step 1')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_empty_required_data_step_1(self, driver):
        user = DeveloperRegistration(driver)
        user.open_link("https://qa-h360-marketplace.softservetest.com/developer")
        user.click_the_start_now_button()
        user.write_valid_data_in_the_email_input_field()
        user.write_data_in_the_username_input_field()
        user.write_data_in_the_first_name_input_field()
        user.write_data_in_the_last_name_input_field()
        user.remove_data_from_email_input_field()
        user.email_address_is_required_error_hint_appears()
        user.remove_data_from_username_input_field()
        user.username_is_required_error_hint_appears()
        user.remove_data_from_first_name_input_field()
        user.first_name_is_required_error_hint_appears()
        user.remove_data_from_last_name_input_field()
        user.last_name_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with already registered email and username 1')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_already_registered_email_and_username_data_step_1(self, driver):
        user = DeveloperRegistration(driver)
        user.open_link("https://qa-h360-marketplace.softservetest.com/developer")
        user.click_the_start_now_button()
        user.write_the_already_registered_email_input_field()
        user.write_data_in_the_username_input_field()
        user.write_data_in_the_first_name_input_field()
        user.write_data_in_the_last_name_input_field()
        user.write_valid_data_in_the_mobile_input_field()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()
        user.this_email_is_already_registered_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.write_valid_data_in_the_email_input_field()
        user.write_the_already_registered_user_in_the_username_input_field()
        user.click_the_next_button()
        user.this_user_is_already_registered_error_hint_appears()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with valid password step 2')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_password_step_2(self, driver):
        self.test_developer_registration_with_valid_data_step_1(driver)
        user = DeveloperRegistration(driver)
        user.write_valid_password_in_the_password_input_field()
        user.write_valid_password_in_the_confirm_password_input_field()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()

    @allure.severity('medium')
    @allure.description('developer registration with invalid password step 2')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_password_step_2(self, driver):
        self.test_developer_registration_with_valid_data_step_1(driver)
        user = DeveloperRegistration(driver)
        user.write_invalid_password_in_the_password_input_field_without_uppercase_letter()
        user.invalid_password_error_hint_appears_for_uppercase_letter()
        user.the_next_button_displayed_as_inactive()
        user.write_invalid_password_in_the_password_input_field_without_number()
        user.invalid_password_error_hint_appears_for_number()
        user.the_next_button_displayed_as_inactive()
        user.write_invalid_password_in_the_password_input_field_without_symbol()
        user.invalid_password_error_hint_appears_for_symbol()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with invalid confirm password step 2')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_confirm_password_step_2(self, driver):
        self.test_developer_registration_with_valid_data_step_1(driver)
        user = DeveloperRegistration(driver)
        user.write_valid_password_in_the_password_input_field()
        user.write_invalid_password_in_the_confirm_password_input_field()
        user.confirm_password_does_not_match_error_hint_appears()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with invalid password range step 2')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_password_range_step_2(self, driver):
        self.test_developer_registration_with_valid_data_step_1(driver)
        user = DeveloperRegistration(driver)
        user.write_invalid_password_range_in_the_password_input()
        user.invalid_password_range_error_hint_appears()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with valid data step 3')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_step_3(self, driver):
        self.test_developer_registration_with_valid_password_step_2(driver)
        user = DeveloperRegistration(driver)
        user.write_data_in_the_company_name_input_field()
        user.write_valid_url_in_the_company_website_input_field()
        user.upload_company_logo()
        user.write_data_in_the_description_input_field()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()

    @allure.severity('medium')
    @allure.description('developer registration with invalid data step 3')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_data_step_3(self, driver):
        self.test_developer_registration_with_valid_password_step_2(driver)
        user = DeveloperRegistration(driver)
        user.write_data_in_the_company_name_input_field()
        user.write_data_in_the_description_input_field()
        user.write_invalid_url_in_the_company_website_input_field()
        user.upload_invalid_company_logo()
        user.the_next_button_displayed_as_inactive()

    @allure.severity('medium')
    @allure.description('developer registration with empty required data step 3')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_empty_required_data_step_3(self, driver):
        self.test_developer_registration_with_valid_password_step_2(driver)
        user = DeveloperRegistration(driver)
        user.upload_company_logo()
        user.write_data_in_the_company_name_input_field()
        user.write_data_in_the_description_input_field()
        user.write_valid_url_in_the_company_website_input_field()
        user.clear_data_from_company_name_input_field()
        user.company_name_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.write_data_in_the_company_name_input_field()
        user.company_name_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()
        user.clear_data_from_company_website_input_field()
        user.company_website_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.write_valid_url_in_the_company_website_input_field()
        user.company_url_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()
        user.clear_data_from_company_description_text_area()
        user.company_description_is_required_error_hint_appears()
        user.write_data_in_the_description_input_field()
        user.company_description_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()

    @allure.severity('medium')
    @allure.description('developer registration with valid data and without state step 4')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_and_without_state_step_4(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.select_country_without_state()
        user.state_module_is_not_displayed()
        user.write_data_in_the_city_input_field()
        user.write_data_in_the_postal_code_input_field()
        user.write_data_in_the_address_input_field()
        user.accept_the_terms_and_code_development_rules()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()
        user.step4_modal_window_disappears()
        user.success_modal_window_appears()

    @allure.severity('medium')
    @allure.description('developer registration with empty required data step 4')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_empty_required_data_step_4(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.select_country_without_state()
        user.state_module_is_not_displayed()
        user.write_data_in_the_city_input_field()
        user.write_data_in_the_postal_code_input_field()
        user.write_data_in_the_address_input_field()
        user.accept_the_terms_and_code_development_rules()
        user.next_button_is_displayed_as_active()
        user.clear_city_input_field()
        user.city_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.write_data_in_the_city_input_field()
        user.city_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()
        user.clear_postal_code_input_field()
        user.postal_code_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.write_data_in_the_postal_code_input_field()
        user.postal_code_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()
        user.clear_address_input_field()
        user.address_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.write_data_in_the_address_input_field()
        user.address_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()
        user.accept_the_terms_and_code_development_rules()
        user.terms_is_required_error_hint_appears()
        user.the_next_button_displayed_as_inactive()
        user.accept_the_terms_and_code_development_rules()
        user.terms_is_required_error_hint_disappears()
        user.next_button_is_displayed_as_active()

    @allure.severity('medium')
    @allure.description('developer registration with valid data and with canada state step 4')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_and_with_canada_state_step_4(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.select_canada_country()
        user.state_module_is_displayed()
        user.select_state()
        user.write_data_in_the_city_input_field()
        user.write_data_in_the_postal_code_input_field()
        user.write_data_in_the_address_input_field()
        user.accept_the_terms_and_code_development_rules()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()
        user.step4_modal_window_disappears()
        user.success_modal_window_appears()

    @allure.severity('medium')
    @allure.description('developer registration with valid data and with india state step 4')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_and_with_india_state_step_4(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.select_india_country()
        user.state_module_is_displayed()
        user.select_state()
        user.write_data_in_the_city_input_field()
        user.write_data_in_the_postal_code_input_field()
        user.write_data_in_the_address_input_field()
        user.accept_the_terms_and_code_development_rules()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()
        user.step4_modal_window_disappears()
        user.success_modal_window_appears()

    @allure.severity('medium')
    @allure.description('developer registration with valid data and with united states state step 4')
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_and_with_united_states_state_step_4(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.select_united_states_country()
        user.state_module_is_displayed()
        user.select_state()
        user.write_data_in_the_city_input_field()
        user.write_data_in_the_postal_code_input_field()
        user.write_data_in_the_address_input_field()
        user.accept_the_terms_and_code_development_rules()
        user.next_button_is_displayed_as_active()
        user.click_the_next_button()
        user.step4_modal_window_disappears()
        user.success_modal_window_appears()

    @allure.severity('medium')
    @allure.description('test the county list step4')
    @pytest.mark.developer_registration_regression
    def test_the_country_list(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.check_the_country_list()

    @allure.severity('medium')
    @allure.description('check the state list with selected Canada country')
    @pytest.mark.developer_registration_regression
    def test_the_state_list_with_selected_canada_country(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.check_the_state_list_with_selected_canada_country()

    @allure.severity('medium')
    @allure.description('check the state list with selected India country')
    @pytest.mark.developer_registration_regression
    def test_the_state_list_with_selected_india_country(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.check_the_state_list_with_selected_india_country()

    @allure.severity('medium')
    @allure.description('check the state list with selected United States country')
    @pytest.mark.developer_registration_regression
    def test_the_state_list_with_selected_united_states_country(self, driver):
        self.test_developer_registration_with_valid_data_step_3(driver)
        user = DeveloperRegistration(driver)
        user.check_the_state_list_with_selected_united_states_country()


