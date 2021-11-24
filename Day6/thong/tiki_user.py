import requests
import uuid

from requests.api import delete
from tiki import Tiki
from code_id import CodeId


class TikiUser(Tiki):
    def __init__(self):
        super().__init__()
        self.endpoint = "users"
        self.unique_id = CodeId()

    def create(self, data):
        data["code"] = self.unique_id.create_id("CVN")
        return super().create(data)

    def get_all(self):
        return super().get_all()

    def edit(self, id, data):
        return super().edit(id, data)

    def delete(self, id):
        return super().delete(id)

    def get_by_id(self, id):
        return super().get_by_id(id)