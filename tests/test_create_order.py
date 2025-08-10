import allure
import pytest
import requests
import generators
from curl import Url
from methods import MethodsOrder


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией пользователя")
    def test_create_order_authorized(self, return_register_data):
        with allure.step("Запрос ингредиентов"):
            ingredients = MethodsOrder.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][2]['_id'], ingredients['data'][3]['_id']]
        with allure.step("Создание заказа"):
            response = MethodsOrder.create_order(generators.generate_order_body(hash_ids), auth_header=return_register_data)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)


    @allure.title("Создание заказа без авторизации пользователя")
    def test_create_order_not_authorized(self):
        with allure.step("Запрос ингредиентов"):
            ingredients = MethodsOrder.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][2]['_id']]
        with allure.step("Создание заказа"):
            response = MethodsOrder.create_order(order_body=generators.generate_order_body(hash_ids), auth_header="")
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)


    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, return_register_data):
        with allure.step("Запрос ингредиентов"):
            ingredients = MethodsOrder.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][3]['_id'], ingredients['data'][4]['_id'],
                        ingredients['data'][5]['_id']]
        with allure.step("Создание заказа"):
            response = MethodsOrder.create_order(generators.generate_order_body(hash_ids),auth_header=return_register_data)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)


    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, return_register_data):
        with allure.step("Список ингредиентов пуст"):
            ingredients = []
        with allure.step("Создание заказа"):
            response = MethodsOrder.create_order(generators.generate_order_body(ingredients), auth_header=return_register_data)
        with allure.step("Проверка кода ответа и сообщения"):
            assert response.status_code == 400 and (response.json()['success'] == False) and (response.json()['message'] == 'Ingredient ids must be provided')


    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_incorrect_ingredients_hash(self, return_register_data):
        with allure.step("Запрос ингредиентов"):
            ingredients = MethodsOrder.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][8]['_id']]
        with allure.step("Внесение ошибки в хеш ингредиента для заказа"):
            hash_ids[0] = hash_ids[0] + '123'
        with allure.step("Создание заказа"):
            response = MethodsOrder.create_order(generators.generate_order_body(hash_ids), auth_header=return_register_data)
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 500