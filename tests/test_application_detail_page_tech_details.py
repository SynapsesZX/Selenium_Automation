import time

import pytest

import conftest
from page_objects.developer_login import DevLogin
from page_objects.tech_details import ApplicationDetailPageTechDetail
from page_objects.developer_registration import DeveloperRegistration
from api.application_detail_page import ApiSetup
from page_objects.base_page import BasePage


class TestApplicationDetailPageTechDetails:

    def test_app_with_created_status(self, driver, api_setup_with_in_progress_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApplicationDetailPageTechDetail(driver)
        user.proceed_to_the_application_with_created_status(api_setup_with_in_progress_status)

    def test_app_with_in_review_status(self, driver, api_setup_with_in_review_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApplicationDetailPageTechDetail(driver)
        user.proceed_to_the_application_with_in_review_status(api_setup_with_in_review_status)

    def test_app_with_approved_status(self, driver, api_setup_with_approved_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApplicationDetailPageTechDetail(driver)
        user.proceed_to_the_application_with_approved_status(api_setup_with_approved_status)

    @pytest.mark.parametrize(('text'), [('Igor'), ('Semen')])
    def test_registration(self, driver, text):
        user = DeveloperRegistration(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.click_the_start_now_button()
