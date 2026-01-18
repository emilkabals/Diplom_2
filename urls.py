class URL:
    BASE_URL = 'https://stellarburgers.education-services.ru' # сайт Stellar Burgers

    # Пользователь: регистрация и авторизация
    REGISTER_USER_URL = f'{BASE_URL}/api/auth/register' # POST - создание пользователя
    LOGIN_USER_URL = f'{BASE_URL}/api/auth/login' # POST - авторизация пользователя
    USER_URL = f'{BASE_URL}/api/auth/user' # GET/PATCH - получение и обновление инфо о пользователе

    # Ингредиенты и заказы
    INGREDIENTS_URL = f'{BASE_URL}/api/ingredients' # GET - получение списка ингредиентов
    ORDERS_URL = f'{BASE_URL}/api/orders' # POST - создание заказа, GET - получение заказов пользователя
