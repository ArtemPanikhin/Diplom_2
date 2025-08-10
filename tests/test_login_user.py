import allure
import pytest
import requests
from curl import Url
from data import AuthorizationData, RandomAutorizationData
from methods import MethodsUser


class TestAuthUser:
    @allure.title("Вход под существующим пользователем")
    def test_auth_exist_user(self):
        with allure.step("Авторизация с существующими данными"):
            response = MethodsUser.login_user(AuthorizationData.create_body)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)


    @allure.title('Вход с неверным логином и паролем')
    @pytest.mark.parametrize('data_setup', RandomAutorizationData.aut_data)
    def test_login_user_failed_data_error(self,data_setup):
        with allure.step('Отправка запроса с неверными данными'):
            response = requests.post(Url.login_user_url(), data_setup)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 401 and (response.json()['success'] == False) and (response.json()['message'] == 'email or password are incorrect')

