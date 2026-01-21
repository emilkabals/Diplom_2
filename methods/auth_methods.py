import requests
import allure
from urls import URL


class AuthMethods:
    @staticmethod
    @allure.step('Регистрация пользователя')
    def register_user(body):
        return requests.post(URL.REGISTER_USER_URL, json=body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(email, password):
        return requests.post(URL.LOGIN_USER_URL, json={"email": email, "password": password})

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(URL.USER_URL, headers=headers)