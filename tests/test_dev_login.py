import pytest

from page_objects.developer_login import DevLogin


class TestDevLogin:
    @pytest.mark.smoke
    def test_user_login(self, driver):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.dev_login()


class TestDevLogin2:
    @pytest.mark.regression
    @pytest.mark.win10
    def test_user_login2(self, driver):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.dev_login()
