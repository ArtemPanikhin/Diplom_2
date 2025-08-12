import requests
import allure
from curl import Url
import pytest
from data import DataForRegistration
from methods import MethodsUser
from data import *


class TestsCreateCourier:
    @allure.title("Проверка регистрации уникального пользователя")
    def test_register_new_user(self, return_register_data):
        with allure.step("Регистрация пользователя"):
            response = MethodsUser.create_user(return_register_data)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)


    @allure.title("Проверка регистрации пользователя, который уже зарегистрирован")
    def test_register_existing_user(self, return_register_data):
        with allure.step("Регистрация пользователя"):
            MethodsUser.create_user(return_register_data)
        with allure.step("Повторная регистрация пользователя с теми же данными"):
            response = MethodsUser.create_user(return_register_data)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 403 and (response.json()['success'] == False) and (response.json()['message'] == USER_EXIST_ERROR)


    @allure.title('Проверка регистрации пользователя. Не заполнено одно из обязательных полей.')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_user_deficit_data_error(self, data_setup):
        with allure.step('Отправка запроса с неполными данными'):
            response = requests.post(Url.create_user_url(), data_setup)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 403 and (response.json()['success'] == False) and (response.json()['message'] == REQUIRED_FIELDS_ERROR)
