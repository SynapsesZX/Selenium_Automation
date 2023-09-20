from page_objects.base_page import BasePage
import api.api_body
import globals.info
import requests


class ApiSetup(BasePage):

    #   def __init__(self, driver):
    #      self.driver = driver
    #      self.application_id = self.get_app_id()

    def get_app_id(self):
        app_name = BasePage.randomWord(value=15)
        request = requests.post('https://qa-h360-marketplace.softservetest.com/api/applications',
                                json=api.api_body.create_app_body(app_name=app_name), headers=globals.info.bearer)
        response_body = request.json()
        assert response_body['data']['name'] == app_name
        app_id = response_body['data']['id']
        return app_id

    def delete_app(self, app):
        request = requests.delete(
            f"https://qa-h360-marketplace.softservetest.com/api/applications/{app}",
            headers=globals.info.bearer)
        return request

    def change_app_status_to_in_progress(self):
        app_id = self.get_app_id()
        request = requests.post(
            f'https://qa-h360-marketplace.softservetest.com/api/applications/{app_id}/tech-details',
            json=api.api_body.app_in_progress_body(), headers=globals.info.bearer)
        assert request.status_code == 201
        return app_id


def test_get_api_name():
    request = requests.get(
        "https://qa-h360-marketplace.softservetest.com/api/developers/0faaf9d6-ec1e-4fb8-8601-9b99e6063417/applications",
        headers=globals.info.bearer, verify=False)
    response = request.json()
    application_name = []
    for search in response['data']['items']:
        application_name.append(search['name'])
    assert "fetchPostApplicationlllllllyuiui" in application_name
