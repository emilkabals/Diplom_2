class Message:
    # тело ответа: пользователь уже существует
    USER_EXISTS = {
        "success": False,
        "message": "User already exists"
    }

    # тело ответа: не все поля заполнены
    MISSING_FIELDS = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    # тело ответа: ошибка логина
    LOGIN_FAILED = {
        "success": False,
        "message": "email or password are incorrect"
    }

    # тело ответа: не авторизован
    UNAUTHORIZED = {
        "success": False,
        "message": "You should be authorised"
    }

    # тело ответа: не переданы ингредиенты
    NO_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }


class TestData:
    # несуществующий логин и пароль
    NONEXISTENT_EMAIL = 'unknown_login_123_avadakedavra'
    NONEXISTENT_PASSWORD = 'unknown_password_123_avadakedavra'

    # невалидный хеш ингредиентов
    INVALID_INGREDIENT_HASH = ["invalid-hash-123-avadakedavra"]
    