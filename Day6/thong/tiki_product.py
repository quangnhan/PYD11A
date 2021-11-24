import requests
from tiki import Tiki
import uuid


class TikiProduct(Tiki):
    def __init__(self):
        super().__init__()
        self.endpoint = "products"

    def get_all(self):
        return super().get_all()

    def create(self, data):
        data["code"] = uuid.uuid1()
        return super().create(data)

    def edit(self, id, data):
        return super().edit(id, data)

    def delete(self, id):
        return super().delete(id)

    def get_by_id(self, id):
        return super().get_by_id(id)