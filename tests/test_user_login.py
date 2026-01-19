import pytest
import allure

from methods.auth_methods import AuthMethods
from data import Message, TestData


@allure.feature('Логин пользователя')
class TestLoginUser:

    @allure.title('Успешный вход под существующим пользователем')
    def test_login_user_success(self, create_and_delete_user):
        user_data = create_and_delete_user

        with allure.step('Отправить POST-запрос на авторизацию пользователя'):
            response = AuthMethods.login_user(user_data["email"], user_data["password"])

        with allure.step('Проверить, что статус-код 200 и ответ содержит ожидаемые данные (email)'):
            assert response.status_code == 200
            assert response.json()["success"] == True
            assert response.json()["user"]["email"] == user_data["email"]

    @allure.title('Вход с неверным логином (email)')
    def test_login_invalid_email(self, create_and_delete_user):
        with allure.step('Получить данные пользователя и изменить email'):
            user_data = create_and_delete_user
            wrong_email = TestData.NONEXISTENT_EMAIL

        with allure.step('Отправить POST-запрос на авторизацию с неверным email'):
            response = AuthMethods.login_user(wrong_email, user_data["password"])

        with allure.step('Проверить, что статус-код 401 и сообщение об ошибке "email or password are incorrect"'):
            assert response.status_code == 401
            assert response.json() == Message.LOGIN_FAILED

    @allure.title('Вход с неверным паролем')
    def test_login_invalid_password(self, create_and_delete_user):
        with allure.step('Получить данные пользователя и изменить пароль'):
            user_data = create_and_delete_user
            wrong_password = TestData.NONEXISTENT_PASSWORD

        with allure.step('Отправить POST-запрос на авторизацию с неверным паролем'):
            response = AuthMethods.login_user(user_data["email"], wrong_password)

        with allure.step('Проверить, что статус-код 401 и сообщение об ошибке "email or password are incorrect"'):
            assert response.status_code == 401
            assert response.json() == Message.LOGIN_FAILED