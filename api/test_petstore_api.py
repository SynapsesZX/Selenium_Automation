import allure
import requests
import json
from api.api_body import PetStoreBody
from globals.info import pet_api_key
from page_objects.base_page import BasePage
import pytest


# Simple API calls for testing the open API base with Pets :) https://petstore.swagger.io/
class TestPetStore:
    # Post method fo creating the Pets
    @allure.tag("Pet,API")
    @allure.description("Testing pet API creation by Post method")
    @pytest.mark.pet_api
    def test_pet_creation(self):
        pet_id = BasePage.random_with_N_digits(value=10)
        category_id = BasePage.random_with_N_digits(value=10)
        category_name = BasePage.randomWord(value=10)
        pet_name = BasePage.randomWord(value=10)
        tag_id = BasePage.random_with_N_digits(value=10)
        tag_name = BasePage.randomWord(value=10)
        pet = requests.post("https://petstore.swagger.io/v2/pet",
                            json=PetStoreBody.create_pet_body(self, pet_id=pet_id, category_id=category_id,
                                                              category_name=category_name, pet_name=pet_name,
                                                              tag_id=tag_id, tag_name=tag_name),
                            auth=pet_api_key)
        assert pet.status_code == 200
        response = pet.json()

        assert response['id'] == pet_id
        assert response['category']['id'] == category_id
        assert response['category']['name'] == category_name
        assert response['name'] == pet_name
        assert response['tags'][0]['id'] == tag_id
        assert response['tags'][0]['name'] == tag_name
        return response['id']

    # Simple Get method for checking the pet ID after creation
    @pytest.mark.pet_api
    @allure.tag("Pet,API")
    @allure.description("Testing pet id by get method")
    def test_pet_id_call_after_creation(self):
        requests.get(f"https://petstore.swagger.io/v2/pet/{self.test_pet_creation()}")

    # Pet delete method
    @pytest.mark.pet_api
    @allure.tag("Pet,API")
    @allure.description("Testing pet id delete by Delete method")
    def test_pet_delete_after_creation(self):
        pet_id = self.test_pet_creation()
        pet_delete = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        assert pet_delete.status_code == 200
        pet_check = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        assert pet_check.status_code == 404
        pet_response_body = pet_check.json()
        assert pet_response_body['message'] == 'Pet not found'
