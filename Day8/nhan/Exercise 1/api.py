import requests

class API:
    def __init__(self):
        self.__url = "https://61a4c6e64c822c0017041e6e.mockapi.io/users"

    def get_all_user(self):
        respond = requests.get(self.__url)
        return respond.json()