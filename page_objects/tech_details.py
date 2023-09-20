

import globals.info
import locators.tech_details
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By



class ApplicationDetailPageTechDetail(BasePage):

    def proceed_to_the_application_detail_page_with_created_status(self, api_setup_created_status):
        application_id = api_setup_created_status
        self.open_link(
            f'https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/{application_id}')
        self.is_element_no_present_with_wait(*locators.tech_details.APP_LIST)

    def click_edit_icon(self):
        self.wait_and_click(*locators.tech_details.EDIT_ICON)

    def select_mobile_native(self):
        list = []
        self.wait_and_click(*locators.tech_details.MOBILE_NATIVE)
        authentication_type_public = self.get_element_attribute(*locators.tech_details.AUTHENTICATION_TYPE_PUBLIC,
                                                                attribute='class')
        assert 'p-radiobutton-checked' in authentication_type_public
        authentication_type_confidential = self.get_element_attribute(
            *locators.tech_details.AUTHENTICATION_TYPE_CONFIDENTIAL,
            attribute='class')
        assert 'p-radiobutton-disabled' in authentication_type_confidential
        scope_list = self.driver.find_elements(By.CSS_SELECTOR, '[class="scopes-item_scopesListItem__3B3kf"]')
        for result in scope_list:
            list.append(result.text)
        assert globals.info.scopes_for_individual_patient == list

    def select_patient_context(self):
        self.wait_and_click(*locators.tech_details.LAUNCH_CONTEXT_TYPE_PATIENT)

    def select_the_allergy_introlerance_scope(self):
        scope = self.driver.find_elements(By.CSS_SELECTOR,
                                          '[class="tech-details-form_scopesContainer__2Wrel"] [class="p-checkbox p-component"]')
        scope[0].click()

    def write_the_valid_url_to_the_smart_launch_url_field(self):
        self.send_text_to_element(*locators.tech_details.SMART_LAUNCH_URL_INPUT_FIELD, text=globals.info.valid_url)

    def write_the_valid_url_to_the_redirect_url_field(self):
        self.send_text_to_element(*locators.tech_details.REDIRECT_URI_INPUT_FIELD, text=globals.info.valid_url)

    def click_the_save_button(self):
        self.wait_and_click(*locators.tech_details.SAVE_BUTTON)

    def select_version(self):
        self.wait_and_click(*locators.tech_details.VERSION_DROP_DOWN)
        version = self.driver.find_elements(By.CSS_SELECTOR, 'ul[class*="p-dropdown-items"] > li')
        version[0].click()

    def proceed_to_the_application_with_created_status(self, api_setup_with_in_progress_status):
        self.open_link(
            f'https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/{api_setup_with_in_progress_status}')

    def proceed_to_the_application_with_in_review_status(self, api_setup_with_in_review_status):
        self.open_link(
            f'https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/{api_setup_with_in_review_status}')

    def proceed_to_the_application_with_approved_status(self, api_setup_with_approved_status):
        self.open_link(
            f'https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/{api_setup_with_approved_status}')
