import requests
import allure
from urls import URL


class OrderMethods:
    def create_order(ingredients, token=None):
        headers = {}
        if token:
            clean_token = token.replace("Bearer ", "")
            headers["Authorization"] = f"Bearer {clean_token}"
        body = {"ingredients": ingredients}
        return requests.post(URL.ORDERS_URL, json=body, headers=headers)