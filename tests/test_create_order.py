import pytest
import allure

from methods.order_methods import OrderMethods
from data import Message, TestData
from helper import get_user_access_token


@allure.feature('Создание заказа')
class TestOrderCreation:

    @allure.title('Создание заказа с авторизацией и с валидными ингредиентами')
    def test_create_order_with_auth_and_ingredients_success(self, create_and_delete_user, get_available_ingredients):
        user_data = create_and_delete_user

        with allure.step('Авторизоваться под пользователем'):
            access_token = get_user_access_token(user_data)

        with allure.step('Отправить POST-запрос на создание заказа с токеном'):
            response = OrderMethods.create_order(get_available_ingredients, access_token)

        with allure.step('Проверить, что статус-код 200 и заказ успешно создан'):
            assert response.status_code == 200
            assert response.json()["success"] == True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_error_400(self, create_and_delete_user):
        user_data = create_and_delete_user

        with allure.step('Авторизоваться под пользователем'):
            access_token = get_user_access_token(user_data)

        with allure.step('Отправить POST-запрос на создание заказа с пустым списком ингредиентов'):
            response = OrderMethods.create_order([], access_token)

        with allure.step('Проверить, что статус-код 400 и ошибка "Ingredient ids must be provided"'):
            assert response.status_code == 400
            assert response.json() == Message.NO_INGREDIENTS

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_hash_error_500(self, create_and_delete_user):
        user_data = create_and_delete_user

        with allure.step('Авторизоваться под пользователем'):
            access_token = get_user_access_token(user_data)

        with allure.step('Отправить POST-запрос на создание заказа с невалидным хешем ингредиента'):
            response = OrderMethods.create_order(TestData.INVALID_INGREDIENT_HASH, access_token)

        with allure.step('Проверить, что статус-код 500 (внутренняя ошибка сервера)'):
            assert response.status_code == 500

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_error_401(self, get_available_ingredients):
        with allure.step('Отправить POST-запрос на создание заказа без токена'):
            response = OrderMethods.create_order(get_available_ingredients)

        with allure.step('Проверить, что статус-код 401 и ошибка "You should be authorised"'):
            assert response.status_code == 401 # Ожидаем 401 по документации, но сервер возвращает 200, тест будет падать
            assert response.json() == Message.UNAUTHORIZED