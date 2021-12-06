import requests

class API:
    def __init__(self):
        self.__url = "https://61a4c6e64c822c0017041e6e.mockapi.io"

    def get_all(self):
        response = requests.get(f"{self.__url}/{self.endpoint}")
        data = response.json()
        return data