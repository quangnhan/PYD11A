import requests
from requests.sessions import _Data


class TikiAPI:
    def __init__(self):
        self.__url = "https://619b87292782760017445671.mockapi.io/users"

    def get_all_users(self):
        endpoint = "users"
        response = request.get(f"{self.__url}/{endpoint}")
        data = response.json()
        return data

    def get_all_products(self):
        endpoint = "products"
        response = requests.get(f"{self.__url}/{endpoint}")
        data = response.json()
        return data

    def create_user(self, data):
        endpoint = "users"
        response = requests.post(f"{self.__url}/{endpoint}", data)
        return data

    def edit_user(self, data, id):
        endpoint = f"users/{id}"
        response = requests.put(f"{self.__url}/{endpoint}", data)
        return data

    def delete_user(self, id):
        endpoint = f"users/{id}"
        response = request.delete(f"{self.__url}/{endpoint}")
        return data

    def get_by_user_id(self, id):
        endpoint = f"users/{id}"
        response = request.get(f"{self.__url}/{endpoint}")
        return data
