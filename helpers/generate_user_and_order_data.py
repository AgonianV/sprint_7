import random
import requests
import string
from helpers.basement import *
from faker import Faker

fake = Faker('ru_RU')

def delete_courier(courier_id):
    del_url = courier_create_endpoint + '/' + str(courier_id)
    print(del_url)
    return requests.delete(del_url)


def get_courier_id(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(courier_login_endpoint, json=payload)
    return response.json().get("id")

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

def order_data():
    payload_order = {
        "firstName": fake.first_name_male(),
        "lastName": fake.last_name_male(),
        "address": "Санкт-Петербург, Невский проспект 24",
        "metroStation": 2,
        "phone": "+7 921 335 39 13 ",
        "rentTime": 5,
        "deliveryDate": str(fake.future_date()),
        "comment": "Добрый вечер",
        "color": ["BLACK"]
    }
    return payload_order