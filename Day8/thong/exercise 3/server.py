import requests


class UserAPI:
    def __init__(self):
        self.url = "https://619b87292782760017445671.mockapi.io/"
        self.endpoint = "users"

    def get_all(self):
        response = requests.get(f"{self.url}/{self.endpoint}")
        data = response.json()
        return data
