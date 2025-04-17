main_endpoint = 'https://qa-scooter.praktikum-services.ru/api/v1'
courier_create_endpoint = main_endpoint + '/courier'
courier_delete_endpoint = main_endpoint + '/courier'
courier_login_endpoint = main_endpoint + '/courier/login'

orders_endpoint = main_endpoint + '/orders'
orders_accept_endpoint = main_endpoint + '/orders/accept'
orders_get_endpoint = main_endpoint + '/orders/track'

error_account_not_find = "Учетная запись не найдена"
error_login_already_used = "Этот логин уже используется. Попробуйте другой."
error_not_enough_info = "Недостаточно данных для входа"
error_not_enough_info_registration = "Недостаточно данных для создания учетной записи"


response_success = {"ok": True}