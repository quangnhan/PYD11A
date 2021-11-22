import requests

class Tiki:
    def __init__(self):
        self.__url = "https://619b8723278276001744566f.mockapi.io"

    def get_all(self):
        response = requests.get(f"{self.__url}/{self.endpoint}")
        data = response.json()
        return data

    def create(self, data):
        response = requests.post(f"{self.__url}/{self.endpoint}", data=data)
        return response.json()

    def edit(self, id, data):
        response = requests.put(f"{self.__url}/{self.endpoint}/{id}", data=data)
        return response.json()

    def delete(self, id):
        response = requests.delete(f"{self.__url}/{self.endpoint}/{id}")
        return response.json()

    def get_by_id(self, id):
        response = requests.get(f"{self.__url}/{self.endpoint}/{id}")
        return response.json()