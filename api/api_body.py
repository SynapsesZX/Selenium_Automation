import json
import requests
import page_objects

import globals.info
from globals.info import bearer
from page_objects.base_page import BasePage


def create_app_body(app_name):
    create_app_body = ''' 
    {
    "categories": [
    "3275b7bf-b4ff-46cb-9930-cdd70e385738"],
    "name": "hgfhgfhfgfgfggghg",
    "products": ["e89cd570-f2f5-43d3-a6e3-84494d507b3f"],
    "short_description": "Some_QA_testsss",
    "facing":"PROVIDER"
    }'''

    json_structure = json.loads(create_app_body)
    json_structure['name'] = app_name
    return json_structure


def pet_app_body(category_id, category_name):
    create_app_body = '''
    {
  "id": 2,
  "category": {
    "id": 2,
    "name": "Maya"
  },
  "name": "allie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 1,
      "name": "Maya"
    }
  ],
  "status": "available"
}
'''

    data = json.loads(create_app_body)
    data['category']['id'] = category_id
    data['category']['name'] = category_name
    return data


def app_in_progress_body():
    create_app_body = '''
    {"application_launch_type":"466d9830-9e3f-4d3f-bea6-d592538a4d8a",
    "product_version_id":"ca17a22b-16f7-4345-aba3-e7bcc0e203d4",
    "has_patient_context":true,"has_encounter_context":false,
    "token_introspection":true,
    "scopes":[{"system_r":false,"patient_population_r":true,"system_w":false,
    "individual_patient_w":false,"patient_population_w":false,
    "individual_patient_r":false,"id":"5997e983-b399-4180-b57f-bdf0a79a29e0"},
    {"system_r":false,"patient_population_r":true,"system_w":false,"individual_patient_w":false,
    "patient_population_w":false,"individual_patient_r":false,"id":"e9411cd7-c12c-44c3-8239-27c6d7a0a0e3"}],
    "development":{"development_client_id":"1j6pk81o0n90bui5lguo566icj",
    "development_smart_launch_url":"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/927a7313-58a6-406a-b568-5e13556df029",
    "development_redirect_uri":"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/927a7313-58a6-406a-b568-5e13556df029",
    "development_client_secret":""},"production":{"production_smart_launch_url":"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/927a7313-58a6-406a-b568-5e13556df029",
    "production_redirect_uri":"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/927a7313-58a6-406a-b568-5e13556df029","production_client_id":"",
    "production_client_secret":""},"is_production_enabled":true}
    
    
    
    
    '''
    data = json.loads(create_app_body)
    return data


def app_in_progress_description_body():
    create_app_body = '''
    {"url":"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/927a7313-58a6-406a-b568-5e13556df029",
    "long_description":"fgfgffgfgfgfggffgfgf","icon":"",
    "preview_images":["1660899478926791file_kpklz9fi26c8424645998d5.jpg"]}
    '''
    data = json.loads(create_app_body)
    return data


def app_in_review_body():
    create_app_body = '''
    {"status":"IN_REVIEW"}
    '''
    data = json.loads(create_app_body)
    return data


def app_approved_body():
    create_app_body = '''
    {"status":"READY_FOR_PUBLISH"}
    '''
    data = json.loads(create_app_body)
    return data


def partner_body():
    create_partner_body = '''
    {"address":"Dob-2A",
    "city":"Kyiv",
    "company_name":"QA",
    "country":"UA",
    "description":"<p>fg fghfghfg ffgf fhfghfghf</p>",
    "categories":["47de5ab7-1500-4928-942c-9a7c567b8f7d","150b6a84-be3b-4074-a80f-ff398b0a19d5"],
    "short_description":"fghgfhfghg gfhgfhfghf gfghfgg hfghfghf f",
    "logo_path":"1669011606130179file_ugs4z4uljq34ee9dc1gh6dd.jpg",
    "postal_code":"1223-A",
    "state":"",
    "website":"https://www.google.com/"}'''
    data = json.loads(create_partner_body)
    data['company_name'] = BasePage.randomWord(value=6)
    data['description'] = BasePage.randomWord(value=35)
    data['short_description'] = BasePage.randomWord(value=35)

    return data


class PetStoreBody:
    # function for generating the PetBody by Post method
    def create_pet_body(self, pet_id, category_id, category_name, pet_name, tag_id, tag_name):
        pet_body = '''
    {
      "id": 1,
      "category": {
        "id": 1,
        "name": "Dog"
      },
      "name": "Rex",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 1,
          "name": "Pet"
        }
      ],
      "status": "available"
    }'''
        pet_api = json.loads(pet_body)
        pet_api["id"] = pet_id
        pet_api["category"]["id"] = category_id
        pet_api["category"]["name"] = category_name
        pet_api["name"] = pet_name
        pet_api['tags'][0]["id"] = tag_id
        pet_api['tags'][0]["name"] = tag_name
        return pet_api
