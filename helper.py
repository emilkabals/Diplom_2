from methods.auth_methods import AuthMethods


def get_user_access_token(user_data):
    login_response = AuthMethods.login_user(user_data["email"], user_data["password"])
    return login_response.json()["accessToken"]
