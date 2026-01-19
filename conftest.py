import pytest
import requests
from generators import generate_user_data
from methods.auth_methods import AuthMethods
from urls import URL


@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = generate_user_data()
    AuthMethods.register_user(user_data)

    yield user_data

    login_response = AuthMethods.login_user(user_data["email"], user_data["password"])
    access_token = login_response.json()["accessToken"]

    AuthMethods.delete_user(access_token)


@pytest.fixture(scope="function")
def cleanup_user():
    user_data = {}

    yield user_data

    login_response = AuthMethods.login_user(user_data["email"], user_data["password"])
    access_token = login_response.json()["accessToken"]

    AuthMethods.delete_user(access_token)


@pytest.fixture(scope="session")
def get_available_ingredients():
    response = requests.get(URL.INGREDIENTS_URL)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    return [ingredient["_id"] for ingredient in data["data"][:2]]