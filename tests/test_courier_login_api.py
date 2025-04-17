import pytest
import allure
import requests
from helpers.basement import *
from conftest import *

class TestCourierLoginApi:
    @allure.title("Проверка авторизации курьера")
    def test_courier_login(self, courier_data_with_delete_courier):

        payload = {
            "login": courier_data_with_delete_courier["login"],
            "password": courier_data_with_delete_courier["password"]
        }
        response = requests.post(courier_login_endpoint, json=payload)
        assert response.status_code == 200
        assert "id" in response.json()


    @allure.title('Проверка ошибки авторизации при неверном логине')
    def test_login_with_invalid_login(self, courier_data_with_delete_courier):

        login = courier_data_with_delete_courier["login"]
        password = courier_data_with_delete_courier["password"]

        payload = {
                "login": login + '123',
                "password": password
        }

        response = requests.post(courier_login_endpoint, json=payload)
        assert response.json()["message"] == error_account_not_find
        assert response.status_code == 404

    @allure.title("Ошибка авторизации несуществующего пользователя")
    def test_login_with_nonexistent_user(self, courier_data_new_with_delete):

        login = courier_data_new_with_delete["login"]
        password = courier_data_new_with_delete["password"]
        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(courier_login_endpoint, json=payload)
        assert response.status_code == 404
        assert response.json()["message"] == error_account_not_find

    @allure.title(
        "Ошибка авторизации без пароля")  # API на момент написания кода не отрабатывал, код должен быть рабочим, но тест не проходит по этой причине
    def test_login_without_password_field(self, courier_data_with_delete_courier):
        login = courier_data_with_delete_courier["login"]
        payload = {"login": login}
        response = requests.post(courier_login_endpoint, json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == error_not_enough_info

    @allure.title(
        "Ошибка авторизации без логина")  # API на момент написания кода не отрабатывал, код должен быть рабочим, но тест не проходит по этой причине
    def test_login_without_login_field(self, courier_data_with_delete_courier):
        password = courier_data_with_delete_courier["password"]
        payload = {"password": password}
        response = requests.post(courier_login_endpoint, json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == error_not_enough_info


