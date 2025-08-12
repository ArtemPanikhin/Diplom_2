import generators
import allure
import requests
from curl import Url
import pytest
from methods import MethodsUser


@pytest.fixture()
@allure.title("Регистрация пользователя, передача данных пользователя")
def return_register_data():
    with allure.step("Получение данных для регистрации"):
        email, password = generators.generate_credentials()
    with allure.step("Создание тела запроса регистрации"):
        register_body = generators.generate_register_body((email, password))
    with allure.step("Передача тела запроса"):
        yield register_body
    with allure.step("Создание тела запроса аутентификации"):
        auth_body = generators.generate_authorization_body((email, password))
    with allure.step("Выполнение запроса аутентификации"):
        auth_response = MethodsUser.login_user(auth_body)
    with allure.step("Проверка успешной авторизации"):
        if auth_response.status_code == 200 and auth_response.json().get('success'):
            with allure.step("Получение accessToken из ответа на запрос"):
                access_token = auth_response.json()['accessToken']
            with allure.step("Создание заголовка запроса с accessToken"):
                auth_header = {"Authorization": f"Bearer {access_token}"}
        else:
            with allure.step("Проверка ожидаемой неуспешной авторизации"):
                assert auth_response.status_code == 401 and auth_response.json()['message'] == 'email or password are incorrect'