import pytest
import allure
import requests
from helpers.basement import *
from helpers.generate_user_and_order_data import *
from conftest import *


class TestCreateOrder:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize('color', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_create_order_with_different_color(self, color):
        payload = order_data()
        payload["color"] = color
        response = requests.post(orders_endpoint, json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(orders_endpoint)
        assert response.status_code == 200
        assert "orders" in response.json()