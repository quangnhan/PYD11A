import requests


class Tiki:
    def __init__(self):
        self.__url = "https://619b87292782760017445671.mockapi.io"

    # def get_all_users(self):
    #     endpoint = "users"
    #     response = requests.get(f"{self.__url}/{endpoint}")
    #     data = response.json()
    #     return data

    # def get_all_products(self):
    #     endpoint = "products"
    #     response = requests.get(f"{self.__url}/{endpoint}")
    #     data = response.json()
    #     return data

    # def create_user(self, data):
    #     endpoint = "users"
    #     response = requests.post(f"{self.__url}/{endpoint}", data=data)
    #     return response.json()

    # def edit_user(self, id, data):
    #     endpoint = f"users/{id}"
    #     response = requests.put(f"{self.__url}/{endpoint}", data=data)
    #     return response.json()

    # def delete_user(self, id):
    #     endpoint = f"users/{id}"
    #     response = requests.delete(f"{self.__url}/{endpoint}")
    #     return response.json()

    # def get_by_user_id(self, id):
    #     endpoint = f"users/{id}"
    #     response = requests.get(f"{self.__url}/{endpoint}")
    #     return response.json()
