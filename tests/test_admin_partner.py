import time

from page_objects.admin_login import AdminLogin
from page_objects.partner_admin import AdminPartner


class TestAdminPartner:
    def test_partner_with_active_status(self,driver,api_setup_partner_with_active_status):
        user = AdminLogin(driver)
        user.open_link("https://qa-h360-marketplace.softservetest.com/admin")
        user.admin_login()
        user = AdminPartner(driver)
        user.open_the_partner_with_active_status(api_setup_partner_with_active_status)

