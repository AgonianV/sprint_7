import pytest
from helpers.generate_user_and_order_data import *



@pytest.fixture
def courier_data_new_with_delete():
    payload = generate_courier_data()
    yield payload
    courier_id = get_courier_id(payload["login"], payload["password"])
    if courier_id:
        delete_courier(courier_id)
    else:
        print(f"Курьер не существует логин - {payload['login']}")



@pytest.fixture()
def courier_data_with_delete_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield payload

    courier_id = get_courier_id(login, password)
    if courier_id:
        delete_courier(courier_id)
    else:
        print(f"Курьер не существует логин - '{login}' ")