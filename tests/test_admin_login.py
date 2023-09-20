from page_objects.admin_login import AdminLogin



class TestAdminLogin:
    def test_login_with_valid_credentials(self,driver):
        user = AdminLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/admin')
        user.admin_login()

