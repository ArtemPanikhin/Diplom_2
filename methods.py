import requests
from curl import Url

class MethodsUser:
    @staticmethod
    def create_user(register_body):
        response = requests.post(Url.create_user_url(), json=register_body)
        return response

    @staticmethod
    def login_user(auth_body):
        response = requests.post(Url.login_user_url(), json=auth_body)
        return response


class MethodsOrder:
    @staticmethod
    def get_ingredients():
        response = requests.get(Url.get_ingredient_url())
        return response

    @staticmethod
    def create_order(order_body,auth_header):
        response = requests.post(Url.create_order_url(), json=order_body, headers=auth_header)
        return response