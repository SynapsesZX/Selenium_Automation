from page_objects.base_page import BasePage
import api.api_body
import globals.info
import requests


class PartnerSetup(BasePage):
    def get_partner_id(self):
        request = requests.post(' https://b08cbmkhu1.execute-api.us-west-2.amazonaws.com/api/partners',
                                json=api.api_body.partner_body(), headers=globals.info.admin_bearer)
        response_body = request.json()
        partner_id = response_body['data']['id']
        return partner_id



