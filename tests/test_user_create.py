import pytest
import allure

from conftest import create_and_delete_user, cleanup_user
from generators import generate_user_data
from methods.auth_methods import AuthMethods
from data import Message

@allure.feature('Создание пользователя')
class TestCreateUser:
    @allure.title('Успешное создание уникального пользователя')
    def test_create_user_success(self, cleanup_user):
        with allure.step('Сгенерировать валидные данные пользователя'):
            user_data = generate_user_data()
            cleanup_user.update(user_data)

        with allure.step('Отправить POST-запрос на регистрацию'):
            response = AuthMethods.register_user(user_data)

        with allure.step('Проверить, что статус-код 200 и ответ содержит ожидаемые данные (email)'):
            assert response.status_code == 200
            assert response.json()["success"] == True
            assert response.json()["user"]["email"] == user_data["email"]

    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_create_user_existing_email(self, create_and_delete_user):
        with allure.step('Получить данные существующего пользователя'):
            user_data = create_and_delete_user

        with allure.step('Повторно отправить запрос на регистрацию'):
            response = AuthMethods.register_user(user_data)

        with allure.step('Проверить, что статус 403 и ошибка "User already exists"'):
            assert response.status_code == 403
            assert response.json() == Message.USER_EXISTS

    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    @allure.title('Нельзя создать пользователя без обязательного поля email, password, name')
    def test_create_user_missing_field(self, field):
        with allure.step('Сгенерировать валидные данные и удалить поле'):
            user_data = generate_user_data()
            user_data.pop(field)

        with allure.step('Отправить POST-запрос на регистрацию'):
            response = AuthMethods.register_user(user_data)

        with allure.step('Проверить, что статус 403 и ошибка "Email, password and name are required fields"'):
            assert response.status_code == 403
            assert response.json() == Message.MISSING_FIELDS