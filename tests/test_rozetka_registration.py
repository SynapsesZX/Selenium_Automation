import time

from page_objects.rozetka_user_registration import RozetkaUserRegistration


class TestRozetkaUserReg:
    def test_registration_ui_elements(self, driver):
        user = RozetkaUserRegistration(driver)
        user.open_link('https://rozetka.com.ua/ua/')
        user.click_user_reg_icon()
        user.click_user_reg_button()
        user.registration_label_is_displayed()
        user.first_name_label_is_displayed()
        user.surname_name_label_is_displayed()
        user.last_name_input_field_is_displayed()
        user.phone_label_is_displayed()
        user.phone_input_field_is_displayed()
        user.email_input_field_is_displayed()
        user.password_label_is_displayed()
        user.password_input_field_is_displayed()
        user.hide_password_button_is_displayed()
        user.register_rules_label_is_displayed()
        user.personal_data_link_is_displayed()
        user.privacy_data_link_is_displayed()
        user.register_button_is_displayed()
        user.registered_button_is_displayed()
        user.registration_divider_is_displayed()
        user.social_label_is_displayed()
        user.facebook_button_is_displayed()
        user.google_button_is_displayed()
        user.close_button_is_displayed()

    def test_registration_with_valid_data(self, driver):
        user = RozetkaUserRegistration(driver)
        user.open_link('https://rozetka.com.ua/ua/')
        user.click_user_reg_icon()
        user.click_user_reg_button()
        user.write_valid_data_in_first_name_input_field()
        user.write_valid_data_in_last_name_input_field()
        user.write_valid_data_in_phone_input_field()
        user.write_valid_data_in_email_input_field()
        user.write_valid_data_in_password_input_field()
        user.click_the_register_button()


