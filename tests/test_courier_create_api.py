import pytest
import allure
import requests
from helpers.basement import *
from conftest import *

class TestCourierCreateApi:

    @allure.title('Проверка создания курьера')
    def test_create_new_courier(self, courier_data_new_with_delete):
        response = requests.post(courier_create_endpoint, json=courier_data_new_with_delete)
        assert response.status_code == 201
        assert response.json() == response_success


    @allure.title("Создание курьера без обязательного поля")
    def test_create_courier_password_is_empty(self, courier_data_with_delete_courier):
        courier_data_with_delete_courier.pop("password")
        response = requests.post(courier_create_endpoint, json=courier_data_with_delete_courier)
        assert response.status_code == 400
        assert response.json()["message"] == error_not_enough_info_registration



    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_two_same_courier(self, courier_data_with_delete_courier):

        payload = {
                "login": courier_data_with_delete_courier["login"],
                "password": courier_data_with_delete_courier["password"],
                "firstName": courier_data_with_delete_courier["firstName"]
        }
        response = requests.post(courier_create_endpoint, json=payload)
        assert response.status_code == 409
        assert response.json()["message"] == error_login_already_used

    @allure.title("Проверка создания курьера с логином, который уже есть")
    def test_create_new_courier_which_login_have_in_system(self, courier_data_with_delete_courier):
        with allure.step("Попытка регистрации с тем же логином и другими данными"):
            duplicate_payload = {
                "login": courier_data_with_delete_courier["login"],
                "password": courier_data_with_delete_courier["password"] + "123",
                "firstName": courier_data_with_delete_courier["firstName"] + "123"
            }

            response = requests.post(courier_create_endpoint, json=duplicate_payload)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 409
            assert response.json()["message"] == error_login_already_used