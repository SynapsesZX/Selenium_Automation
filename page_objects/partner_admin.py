import globals.info
from page_objects.base_page import BasePage
import locators.developer_registration


class AdminPartner(BasePage):

    def open_the_partner_with_active_status(self, api_setup_partner_with_active_status):
        self.open_link(
            f'https://qa-h360-marketplace.softservetest.com/admin/partners/{api_setup_partner_with_active_status}')
