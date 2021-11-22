import requests

class TikiAPI:
    def __init__(self):
        self.__url = "https://619b8723278276001744566f.mockapi.io"

    def get_all_users(self):
        endpoint = "users"
        response = requests.get(f"{self.__url}/{endpoint}")
        data = response.json()
        return data
    
    def get_all_products(self):
        endpoint = "products"
        response = requests.get(f"{self.__url}/{endpoint}")
        data = response.json()
        return data
